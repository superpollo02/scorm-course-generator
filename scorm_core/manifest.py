"""
manifest.py
===========
Generador canónico y unificado de manifiestos SCORM 1.2 (imsmanifest.xml).
Centraliza la lógica para evitar discrepancias entre los distintos generadores del proyecto
(Trivia, Conectabloques, SCORM Modern y módulos temáticos).
"""

from __future__ import annotations

import html
from typing import Any, List, Optional


def generar_manifest_scorm_unificado(
    identifier: str,
    title: str,
    masteryscore: Optional[int] = None,
    items: Optional[List[dict[str, Any]]] = None,
    default_href: str = "index.html",
    generator_name: str = "Aula Lista EDUCAI SCORM Core"
) -> str:
    """
    Genera el contenido XML de un imsmanifest.xml estándar SCORM 1.2.
    
    Parámetros:
    - identifier: Identificador alfanumérico único para el paquete.
    - title: Título del curso/actividad visible en el LMS.
    - masteryscore: Puntaje mínimo de aprobación (opcional).
    - items: Lista opcional de elementos para cursos multi-página:
             [{"id": "mod1", "title": "Módulo 1", "href": "modulo1.html"}, ...]
    - default_href: Archivo de inicio si no se especifican múltiples items (default: "index.html").
    - generator_name: Nombre del generador para comentarios de metadatos.
    """
    safe_id = "".join(c if c.isalnum() or c in ("-", "_") else "_" for c in identifier) or "SCORM_PACKAGE"
    safe_title = html.escape(title.strip())

    items_xml_lines = []
    resources_xml_lines = []

    if items and len(items) > 0:
        for it in items:
            it_id = "".join(c if c.isalnum() or c in ("-", "_") else "_" for c in str(it.get("id", "item")))
            it_title = html.escape(str(it.get("title", it_id)).strip())
            it_href = str(it.get("href", f"{it_id}.html"))

            mastery_tag = f"\n        <adlcp:masteryscore>{masteryscore}</adlcp:masteryscore>" if masteryscore is not None else ""
            items_xml_lines.append(
                f'      <item identifier="item_{it_id}" identifierref="res_{it_id}">'
                f'\n        <title>{it_title}</title>{mastery_tag}'
                f'\n      </item>'
            )
            resources_xml_lines.append(
                f'    <resource identifier="res_{it_id}" type="webcontent" adlcp:scormtype="sco" href="{html.escape(it_href)}">'
                f'\n      <file href="{html.escape(it_href)}"/>'
                f'\n    </resource>'
            )
        items_block = "\n".join(items_xml_lines)
        resources_block = "\n".join(resources_xml_lines)
    else:
        mastery_tag = f"\n        <adlcp:masteryscore>{masteryscore}</adlcp:masteryscore>" if masteryscore is not None else ""
        items_block = (
            f'      <item identifier="item_{safe_id}" identifierref="res_{safe_id}">'
            f'\n        <title>{safe_title}</title>{mastery_tag}'
            f'\n      </item>'
        )
        resources_block = (
            f'    <resource identifier="res_{safe_id}" type="webcontent" adlcp:scormtype="sco" href="{html.escape(default_href)}">'
            f'\n      <file href="{html.escape(default_href)}"/>'
            f'\n    </resource>'
        )

    return f"""<?xml version="1.0" standalone="no" ?>
<!-- Generator: {generator_name} -->
<manifest identifier="{safe_id}" version="1.2"
          xmlns="http://www.imsproject.org/xsd/imscp_rootv1p1p2"
          xmlns:adlcp="http://www.adlnet.org/xsd/adlcp_rootv1p2"
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xsi:schemaLocation="http://www.imsproject.org/xsd/imscp_rootv1p1p2 imscp_rootv1p1p2.xsd
                              http://www.adlnet.org/xsd/adlcp_rootv1p2 adlcp_rootv1p2.xsd">
  <metadata>
    <schema>ADL SCORM</schema>
    <schemaversion>1.2</schemaversion>
  </metadata>
  <organizations default="org_{safe_id}">
    <organization identifier="org_{safe_id}">
      <title>{safe_title}</title>
{items_block}
    </organization>
  </organizations>
  <resources>
{resources_block}
  </resources>
</manifest>
"""
