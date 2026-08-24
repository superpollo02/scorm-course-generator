# scorm_modern

Generador de paquetes SCORM 1.2 con estructura moderna: **1 Lección + 1
Evaluación (quiz interactivo) + N Actividades**, enlaces externos
(`ENLACES.md`) y embebido de video en la nube (YouTube / Google Drive).

Este paquete nace del plan descrito en la sesión de trabajo previa (ver
`cod.cambios.curso.scorm.txt`) y lo implementa completo, ya que el código no
existía todavía en el repositorio.

## Instalación

```bash
pip install pyyaml pytest --break-system-packages   # o sin el flag si usas venv
```

## Uso rápido (CLI)

```bash
# Validar configuración + contenido markdown
python -m scorm_modern.cli validate ejemplo/config.yaml

# Listar los objetos parseados del curso
python -m scorm_modern.cli list ejemplo/config.yaml

# Construir el paquete SCORM (.zip)
python -m scorm_modern.cli build ejemplo/config.yaml
```

El build genera, dentro de `<salida_dir>/<identificador>/`:

- `index.html` — índice con enlaces a lección/evaluación/actividades
- `leccion.html`, `evaluacion.html`, `actividad_NN.html`
- `imsmanifest.xml` — manifiesto SCORM 1.2 con título real por objeto
- `ENLACES.md` — enlaces del `config.yaml` + los declarados en el markdown
- `<identificador>-SCORM.zip` — paquete final listo para subir al LMS

## Formato de `config.yaml`

```yaml
identificador: mi-curso-2026     # alfanumérico, sin espacios
titulo: "Mi Curso"
idioma: es
contenido_md: curso.md           # ruta relativa al propio config.yaml
salida_dir: output
puntaje_minimo: 70               # % mínimo para aprobar la evaluación
enlaces:
  - titulo: "Guía oficial"
    url: "https://ejemplo.com/guia"
    descripcion: "Opcional"
```

## Formato del markdown fuente

```markdown
# Lección: <título>
Contenido... (encabezados ##/###, listas, tablas, negrita/cursiva)

:::apoyo
Nota o tip destacado. Puede incluir:
VIDEO: https://www.youtube.com/watch?v=xxxx
:::

# Evaluación: <título>
## Pregunta 1
**Texto de la pregunta**

A) Opción
B) Opción
C) Opción
D) Opción

**Respuesta correcta: B**
**Explicación:** Texto opcional.

# Actividad: <título>          (o "# Ejercicio: <título>")
Contenido de la actividad...

# Enlaces
- [Título](https://url) - descripción opcional
```

Reglas:
- Debe existir **exactamente una** sección `# Lección:`.
- Puede existir **0 o 1** sección `# Evaluación:`.
- Debe existir **al menos una** sección `# Actividad:` / `# Ejercicio:`.
- Los bloques `:::apoyo ... :::` se pueden usar dentro de Lección, Evaluación
  o Actividad.

## Tests

```bash
python -m pytest tests/ -v
```

## Estructura

```
scorm_modern/
├── __init__.py
├── config.py       # CursoConfig, Enlace, validación
├── parser.py        # markdown -> Leccion/Evaluacion/Actividad
├── renderer.py       # HTML + embed de video + quiz interactivo
├── manifest.py       # imsmanifest.xml con títulos por objeto
├── builder.py        # orquesta todo y genera el .zip
├── cli.py             # validate / build / list
├── tests/             # pytest
└── ejemplo/            # config.yaml + curso_ejemplo.md de muestra
```
