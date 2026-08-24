"""
config.py
=========
Configuración del curso para el generador SCORM moderno (scorm_modern).

Define la estructura de configuración de un curso (`CursoConfig`) y de sus
enlaces externos (`Enlace`), junto con las validaciones necesarias antes de
construir el paquete SCORM.

Formato de configuración esperado (YAML o dict):

    identificador: mi-curso-2026
    titulo: "Mi Curso de Ejemplo"
    idioma: es
    contenido_md: curso.md
    salida_dir: output
    puntaje_minimo: 70
    enlaces:
      - titulo: "Guía oficial"
        url: "https://ejemplo.com/guia"
        descripcion: "Documento de referencia del módulo 1"
      - titulo: "Video complementario"
        url: "https://youtube.com/watch?v=xxxx"
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable

__all__ = ["Enlace", "CursoConfig", "ConfigError"]

# URL razonablemente válida (http/https, sin espacios).
_URL_RE = re.compile(r"^https?://[^\s]+$", re.IGNORECASE)

# Identificador de curso: alfanumérico, guiones, puntos y guiones bajos.
_ID_RE = re.compile(r"^[A-Za-z0-9_.-]+$")


class ConfigError(ValueError):
    """Se lanza cuando una configuración no pasa la validación."""


@dataclass
class Enlace:
    """Un enlace externo (recurso, video en la nube, referencia, etc.)."""

    titulo: str
    url: str
    descripcion: str = ""

    def validar(self) -> list[str]:
        errores: list[str] = []
        if not self.titulo or not self.titulo.strip():
            errores.append("Un enlace no tiene 'titulo'.")
        if not self.url or not _URL_RE.match(self.url.strip()):
            errores.append(
                f"URL inválida en el enlace '{self.titulo or '(sin título)'}': "
                f"{self.url!r} (debe comenzar con http:// o https://)"
            )
        return errores

    def to_markdown(self) -> str:
        """Representación en una línea de lista Markdown para ENLACES.md."""
        base = f"- [{self.titulo}]({self.url})"
        if self.descripcion:
            base += f" — {self.descripcion}"
        return base

    @classmethod
    def from_any(cls, data: "Enlace | dict[str, Any]") -> "Enlace":
        if isinstance(data, Enlace):
            return data
        if isinstance(data, dict):
            return cls(
                titulo=str(data.get("titulo", "")).strip(),
                url=str(data.get("url", "")).strip(),
                descripcion=str(data.get("descripcion", "")).strip(),
            )
        raise ConfigError(f"Formato de enlace no soportado: {data!r}")


@dataclass
class CursoConfig:
    """Configuración completa de un curso a empaquetar como SCORM."""

    identificador: str
    titulo: str
    idioma: str = "es"
    contenido_md: str = "curso.md"
    salida_dir: str = "output"
    version: str = "1.0"
    puntaje_minimo: int = 70
    enlaces: list[Enlace] = field(default_factory=list)

    # ------------------------------------------------------------------
    # Construcción
    # ------------------------------------------------------------------
    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "CursoConfig":
        data = dict(data)  # copia defensiva
        enlaces_raw: Iterable[Any] = data.pop("enlaces", []) or []
        enlaces = [Enlace.from_any(e) for e in enlaces_raw]

        campos_validos = {f for f in cls.__dataclass_fields__ if f != "enlaces"}
        desconocidos = set(data) - campos_validos
        if desconocidos:
            raise ConfigError(
                f"Campos de configuración desconocidos: {sorted(desconocidos)}"
            )

        return cls(enlaces=enlaces, **data)

    @classmethod
    def from_yaml(cls, path: str | Path) -> "CursoConfig":
        try:
            import yaml  # type: ignore
        except ImportError as exc:  # pragma: no cover
            raise ConfigError(
                "PyYAML es requerido para leer configuración YAML. "
                "Instálalo con: pip install pyyaml"
            ) from exc

        ruta = Path(path)
        if not ruta.exists():
            raise ConfigError(f"No se encontró el archivo de configuración: {ruta}")

        with ruta.open("r", encoding="utf-8") as f:
            datos = yaml.safe_load(f) or {}

        if not isinstance(datos, dict):
            raise ConfigError(
                f"El archivo de configuración {ruta} debe contener un mapeo YAML."
            )

        return cls.from_dict(datos)

    # ------------------------------------------------------------------
    # Validación
    # ------------------------------------------------------------------
    def validar(self) -> list[str]:
        """Devuelve una lista de errores de validación (vacía si es válida)."""
        errores: list[str] = []

        if not self.identificador or not _ID_RE.match(self.identificador):
            errores.append(
                "El campo 'identificador' es obligatorio y solo puede contener "
                "letras, números, guiones, puntos o guiones bajos "
                f"(recibido: {self.identificador!r})."
            )

        if not self.titulo or not self.titulo.strip():
            errores.append("El campo 'titulo' es obligatorio.")

        if not self.contenido_md or not self.contenido_md.strip():
            errores.append("El campo 'contenido_md' es obligatorio.")

        if not isinstance(self.puntaje_minimo, int) or not (0 <= self.puntaje_minimo <= 100):
            errores.append(
                "El campo 'puntaje_minimo' debe ser un entero entre 0 y 100 "
                f"(recibido: {self.puntaje_minimo!r})."
            )

        # Enlaces: cada uno válido y sin URLs duplicadas.
        urls_vistas: set[str] = set()
        for enlace in self.enlaces:
            errores.extend(enlace.validar())
            url_norm = enlace.url.strip().rstrip("/")
            if url_norm in urls_vistas:
                errores.append(f"Enlace duplicado (misma URL): {enlace.url}")
            urls_vistas.add(url_norm)

        return errores

    def es_valida(self) -> bool:
        return not self.validar()

    def validar_o_lanzar(self) -> None:
        errores = self.validar()
        if errores:
            detalle = "\n  - ".join(errores)
            raise ConfigError(f"Configuración inválida:\n  - {detalle}")

    # ------------------------------------------------------------------
    # Utilidades
    # ------------------------------------------------------------------
    def ruta_contenido(self, base_dir: str | Path | None = None) -> Path:
        base = Path(base_dir) if base_dir else Path(".")
        return base / self.contenido_md

    def ruta_salida(self, base_dir: str | Path | None = None) -> Path:
        base = Path(base_dir) if base_dir else Path(".")
        return base / self.salida_dir / self.identificador
