"""
manifest.py
===========
Genera el `imsmanifest.xml` (SCORM 1.2) para un paquete compuesto por:

  - 1 página de índice
  - 1 lección
  - 0 o 1 evaluación
  - N actividades

Cada `item` del manifiesto usa el título real del objeto (lección,
evaluación o actividad), no un nombre genérico.
"""

from __future__ import annotations

from dataclasses import dataclass
from xml.sax.saxutils import escape

__all__ = ["ItemManifest", "generar_manifest"]


@dataclass
class ItemManifest:
    """Un elemento a incluir en el manifiesto (índice, lección, evaluación o actividad)."""

    identificador: str
    titulo: str
    archivo: str


def generar_manifest(
    identificador_curso: str,
    titulo_curso: str,
    items: list[ItemManifest],
    version: str = "1.0",
) -> str:
    """Construye el XML completo de imsmanifest.xml para SCORM 1.2."""

    resources = []
    entradas = []

    for item in items:
        resource_id = f"resource_{item.identificador}"
        item_id = f"item_{item.identificador}"
        titulo_esc = escape(item.titulo)

        resources.append(
            f'    <resource identifier="{resource_id}" type="webcontent" '
            f'adlcp:scormtype="sco" href="{item.archivo}">\n'
            f'      <file href="{item.archivo}"/>\n'
            f"    </resource>"
        )
        entradas.append(
            f'      <item identifier="{item_id}" identifierref="{resource_id}">\n'
            f"        <title>{titulo_esc}</title>\n"
            f"      </item>"
        )

    titulo_curso_esc = escape(titulo_curso)

    manifest = f"""<?xml version="1.0" encoding="UTF-8"?>
<manifest identifier="com.scorm_modern.{identificador_curso}" version="{version}"
          xmlns="http://www.imsproject.org/xsd/imscp_rootv1p1p2"
          xmlns:adlcp="http://www.adlnet.org/xsd/adlcp_rootv1p2"
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xsi:schemaLocation="http://www.imsproject.org/xsd/imscp_rootv1p1p2 imscp_rootv1p1p2.xsd
                              http://www.imsglobal.org/xsd/imsmd_rootv1p2p1 imsmd_rootv1p2p1.xsd
                              http://www.adlnet.org/xsd/adlcp_rootv1p2 adlcp_rootv1p2.xsd">
  <metadata>
    <schema>ADL SCORM</schema>
    <schemaversion>1.2</schemaversion>
  </metadata>
  <organizations default="org_01">
    <organization identifier="org_01">
      <title>{titulo_curso_esc}</title>
{chr(10).join(entradas)}
    </organization>
  </organizations>
  <resources>
{chr(10).join(resources)}
  </resources>
</manifest>
"""
    return manifest
