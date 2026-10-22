#!/usr/bin/env python3
"""
ESALUD Academic Program SCORM Package Builder
Converts the academic program markdown file into a beautifully styled HTML SCORM 1.2 package in Spanish.
"""

import re
import zipfile
from pathlib import Path

# Paths
ROOT_DIR = Path("c:/Users/mfischer/Documents/antigravitiy proyectos/CURSO SCORM/scorm-course-generator")
INPUT_FILE = ROOT_DIR / "programa-academico-esalud.md"
OUTPUT_DIR = ROOT_DIR / "output/esalud-scorm"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Course metadata
COURSE_TITLE = "Gestión y Creación de Aulas Virtuales en el Campus ESALUD"
COURSE_SUBTITLE = "Programa Académico bajo los lineamientos de la Circular 5"
COURSE_DESCRIPTION = "Capacitación continua para autoridades, direcciones, jefaturas y equipos docentes del Ministerio de Salud y Deportes."
COURSE_LANGUAGE = "es"

def markdown_to_html(md_content):
    """Convert markdown to HTML with proper styling"""
    html = md_content

    # Headers
    html = re.sub(r'^# (.+)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^#### (.+)$', r'<h4>\1</h4>', html, flags=re.MULTILINE)

    # Bold and italic
    html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*(.+?)\*', r'<em>\1</em>', html)

    # Links
    html = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2" target="_blank">\1</a>', html)

    # Lists - unordered
    html = re.sub(r'^- (.+)$', r'<li>\1</li>', html, flags=re.MULTILINE)
    html = re.sub(r'^\* (.+)$', r'<li>\1</li>', html, flags=re.MULTILINE)

    # Wrap consecutive <li> items in <ul>
    html = re.sub(r'(<li>.*?</li>\n)+', lambda m: '<ul>\n' + m.group(0) + '</ul>\n', html, flags=re.DOTALL)

    # Tables - convert markdown tables to HTML
    def convert_table(match):
        table_text = match.group(0)
        lines = table_text.strip().split('\n')

        if len(lines) < 3:
            return table_text

        # Parse header
        header_cells = [cell.strip() for cell in lines[0].split('|')[1:-1]]

        # Parse rows (skip separator line)
        rows = []
        for line in lines[2:]:
            cells = [cell.strip() for cell in line.split('|')[1:-1]]
            if cells and any(cells):
                rows.append(cells)

        # Build HTML table
        table_html = '<table class="data-table">\n<thead>\n<tr>\n'
        for cell in header_cells:
            table_html += f'<th>{cell}</th>\n'
        table_html += '</tr>\n</thead>\n<tbody>\n'

        for row in rows:
            table_html += '<tr>\n'
            for cell in row:
                table_html += f'<td>{cell}</td>\n'
            table_html += '</tr>\n'

        table_html += '</tbody>\n</table>\n'
        return table_html

    # Find and convert tables
    table_pattern = r'\|.+\|\n\|[-:\s|]+\|\n(?:\|.+\|\n)+'
    html = re.sub(table_pattern, convert_table, html, flags=re.MULTILINE)

    # Blockquotes
    html = re.sub(r'^> (.+)$', r'<blockquote>\1</blockquote>', html, flags=re.MULTILINE)

    # Horizontal rules
    html = re.sub(r'^---$', r'<hr>', html, flags=re.MULTILINE)

    # Paragraphs - wrap non-tagged lines
    lines = html.split('\n')
    new_lines = []
    in_tag = False

    for line in lines:
        stripped = line.strip()
        if not stripped:
            new_lines.append(line)
            continue

        if re.match(r'<(h[1-6]|ul|ol|li|table|thead|tbody|tr|th|td|blockquote|pre|hr|div|p)', stripped):
            in_tag = True
            new_lines.append(line)
        elif stripped.startswith('</'):
            new_lines.append(line)
            in_tag = False
        elif not in_tag and not re.match(r'<.+>', stripped):
            new_lines.append(f'<p>{stripped}</p>')
        else:
            new_lines.append(line)

    html = '\n'.join(new_lines)

    # Clean up double wrapping
    html = re.sub(r'<p><(h[1-6]|ul|ol|table|blockquote|pre|hr)>', r'<\1>', html)
    html = re.sub(r'</(h[1-6]|ul|ol|table|blockquote|pre|hr)></p>', r'</\1>', html)

    return html

def parse_markdown_file(file_path):
    """Split the markdown file into sections"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find position of Module 1
    m1_match = re.search(r'### Módulo 1:', content)
    m2_match = re.search(r'### Módulo 2:', content)
    metodologia_match = re.search(r'## V\.', content)

    if not (m1_match and m2_match and metodologia_match):
        raise ValueError("Could not find section markers in markdown file.")

    pos_m1 = m1_match.start()
    pos_m2 = m2_match.start()
    pos_metodologia = metodologia_match.start()

    # Extract sections
    sec_general = content[:pos_m1].strip()
    sec_m1 = content[pos_m1:pos_m2].strip()
    sec_m2 = content[pos_m2:pos_metodologia].strip()
    sec_metodologia = content[pos_metodologia:].strip()

    return [
        {
            "id": "info_general",
            "title": "Datos Generales y Fundamentación",
            "content": sec_general,
            "duration": "Introducción al Curso"
        },
        {
            "id": "modulo_01",
            "title": "Módulo 1: Introducción y Circular 5",
            "content": sec_m1,
            "duration": "Semana 1 - 2"
        },
        {
            "id": "modulo_02",
            "title": "Módulo 2: Profundización e Integridad Técnica",
            "content": sec_m2,
            "duration": "Semana 3 - 4"
        },
        {
            "id": "metodologia",
            "title": "Metodología, Evaluación y Docentes",
            "content": sec_metodologia,
            "duration": "Información Académica"
        }
    ]

def create_module_html(module, modules, index, prev_mod=None, next_mod=None):
    """Create HTML file for a module"""
    content_html = markdown_to_html(module["content"])

    # Navigation buttons
    nav_html = '<div class="navigation">\n'
    if prev_mod:
        nav_html += f'  <a href="{prev_mod["id"]}.html" class="nav-button">← Anterior: {prev_mod["title"]}</a>\n'
    else:
        nav_html += '  <span></span>\n'

    nav_html += '  <div class="nav-center">\n'
    nav_html += '    <a href="index.html" class="nav-button">📚 Índice</a>\n'
    nav_html += '  </div>\n'

    if next_mod:
        nav_html += f'  <a href="{next_mod["id"]}.html" class="nav-button">Siguiente: {next_mod["title"]} →</a>\n'
    else:
        nav_html += '  <span></span>\n'
    nav_html += '</div>\n'

    html_template = f'''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{module["title"]} - {COURSE_TITLE}</title>
    <link rel="stylesheet" href="styles.css">
    <script src="scorm_api.js"></script>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>{module["title"]}</h1>
            <div class="subtitle">{COURSE_TITLE}</div>
            <div class="progress-indicator">{module["duration"]}</div>
        </div>

        <div class="content">
            {content_html}
        </div>

        {nav_html}
    </div>

    <script>
        window.addEventListener('load', function() {{
            initializeSCORM();
        }});

        window.addEventListener('beforeunload', function() {{
            completeSCORM();
        }});
    </script>
</body>
</html>'''

    output_file = OUTPUT_DIR / f"{module['id']}.html"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_template)

    print(f"  [OK] Creado: {output_file.name}")

def create_index_html(modules):
    """Create index/landing page"""
    modules_cards = ""
    for i, module in enumerate(modules, 1):
        modules_cards += f'''
        <a href="{module['id']}.html" class="module-card">
            <h3>Sección {i}</h3>
            <div class="duration">{module['duration']}</div>
            <div class="description">{module['title']}</div>
        </a>'''

    html_template = f'''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{COURSE_TITLE}</title>
    <link rel="stylesheet" href="styles.css">
    <script src="scorm_api.js"></script>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>{COURSE_TITLE}</h1>
            <div class="subtitle">{COURSE_SUBTITLE}</div>
            <div class="progress-indicator">Duración: 4 semanas (40 hs)</div>
        </div>

        <div class="content">
            <div class="module-info">
                <h3>Resumen Académico</h3>
                <p>{COURSE_DESCRIPTION}</p>
                <p>Este curso ha sido estructurado bajo los requisitos de la <strong>Circular 5</strong> para la creación secuencial, predecible e integral de aulas virtuales en la plataforma Moodle del Ministerio de Salud y Deportes.</p>
            </div>

            <h2>Estructura del Programa</h2>
            <div class="module-grid">
                {modules_cards}
            </div>

            <div class="info-box">
                <strong>Instrucción de cursado:</strong> Haz clic en la primera sección para iniciar el programa. Puedes navegar secuencialmente usando los botones en la parte inferior de cada página. Tu progreso se guardará automáticamente en el Campus.
            </div>
        </div>
    </div>

    <script>
        window.addEventListener('load', function() {{
            initializeSCORM();
        }});
    </script>
</body>
</html>'''

    output_file = OUTPUT_DIR / "index.html"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_template)

    print(f"  [OK] Creado: {output_file.name}")

def create_css():
    """Create CSS styles using a professional medical/health blue-green theme"""
    css_content = '''/* ESALUD SCORM Professional Stylesheet - Medical/Health Theme */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    line-height: 1.6;
    color: #2c3e50;
    background: linear-gradient(135deg, #e0f2f1 0%, #b2dfdb 100%);
    min-height: 100vh;
    padding: 20px;
}

.container {
    max-width: 900px;
    margin: 0 auto;
    background: white;
    border-radius: 12px;
    box-shadow: 0 10px 30px rgba(0,77,64,0.15);
    overflow: hidden;
}

.header {
    background: linear-gradient(135deg, #00695c 0%, #00897b 100%);
    color: white;
    padding: 35px 30px;
    text-align: center;
}

.header h1 {
    font-size: 1.8em;
    margin-bottom: 10px;
    font-weight: 600;
    line-height: 1.3;
}

.header .subtitle {
    font-size: 1.1em;
    opacity: 0.9;
    font-weight: 300;
}

.progress-indicator {
    background: rgba(255,255,255,0.18);
    padding: 8px 16px;
    border-radius: 20px;
    display: inline-block;
    margin-top: 15px;
    font-weight: 500;
    font-size: 0.9em;
}

.content {
    padding: 40px;
}

p {
    margin-bottom: 20px;
    text-align: justify;
}

h2 {
    color: #004d40;
    font-size: 1.5em;
    margin: 35px 0 15px 0;
    border-bottom: 2px solid #b2dfdb;
    padding-bottom: 8px;
}

h3 {
    color: #00695c;
    font-size: 1.25em;
    margin: 25px 0 12px 0;
}

h4 {
    color: #00796b;
    font-size: 1.1em;
    margin: 20px 0 10px 0;
}

ul, ol {
    margin-bottom: 20px;
    padding-left: 25px;
}

li {
    margin-bottom: 8px;
}

blockquote {
    border-left: 5px solid #00897b;
    background-color: #f2faf9;
    padding: 15px 20px;
    margin: 20px 0;
    font-style: italic;
    border-radius: 0 8px 8px 0;
}

.module-info {
    background: #efebe9;
    border-left: 4px solid #8d6e63;
    padding: 20px;
    margin-bottom: 30px;
    border-radius: 4px;
}

.module-info h3 {
    color: #5d4037;
    margin-top: 0;
    margin-bottom: 10px;
}

/* Module Grid */
.module-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
    margin: 25px 0;
}

@media (max-width: 600px) {
    .module-grid {
        grid-template-columns: 1fr;
    }
    .content {
        padding: 20px;
    }
}

.module-card {
    display: block;
    text-decoration: none;
    background: #f1f8e9;
    border: 1px solid #dcedc8;
    border-left: 4px solid #7cb342;
    padding: 20px;
    border-radius: 6px;
    transition: all 0.3s ease;
}

.module-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 5px 15px rgba(0,0,0,0.08);
    background: #f9fbe7;
}

.module-card h3 {
    margin: 0 0 8px 0;
    color: #558b2f;
    font-size: 1.15em;
}

.module-card .duration {
    font-size: 0.85em;
    color: #689f38;
    font-weight: bold;
    text-transform: uppercase;
    margin-bottom: 10px;
}

.module-card .description {
    color: #555;
    font-size: 0.95em;
    line-height: 1.4;
}

.info-box {
    background-color: #e8f5e9;
    border: 1px solid #c8e6c9;
    color: #2e7d32;
    padding: 15px;
    border-radius: 6px;
    margin-top: 30px;
}

/* Tables */
.data-table {
    width: 100%;
    border-collapse: collapse;
    margin: 25px 0;
    box-shadow: 0 2px 5px rgba(0,0,0,0.05);
}

.data-table th {
    background-color: #00695c;
    color: white;
    font-weight: bold;
    padding: 12px;
    border: 1px solid #004d40;
    text-align: left;
}

.data-table td {
    padding: 10px 12px;
    border: 1px solid #e0e0e0;
}

.data-table tbody tr:nth-child(even) {
    background-color: #f2faf9;
}

.data-table tbody tr:hover {
    background-color: #e0f2f1;
}

/* Navigation buttons */
.navigation {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: #f5f5f5;
    padding: 20px 30px;
    border-top: 1px solid #e0e0e0;
}

.nav-button {
    text-decoration: none;
    background-color: #00695c;
    color: white;
    padding: 10px 18px;
    border-radius: 4px;
    font-weight: 600;
    font-size: 0.95em;
    transition: background-color 0.2s;
}

.nav-button:hover {
    background-color: #004d40;
}

.nav-center {
    display: flex;
    justify-content: center;
}

.nav-center .nav-button {
    background-color: #37474f;
}

.nav-center .nav-button:hover {
    background-color: #263238;
}
'''
    output_file = OUTPUT_DIR / "styles.css"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(css_content)
    print(f"  [OK] Creado: {output_file.name}")

def create_scorm_api():
    """Create SCORM API wrapper JavaScript"""
    js_content = '''// SCORM 1.2 API Wrapper
var scorm = {
    version: "1.2",
    handleError: function(errorCode) {
        console.error("SCORM Error " + errorCode);
    },
    get: function(parameter) {
        var API = this.getAPI();
        if (API) {
            var value = API.LMSGetValue(parameter);
            var error = API.LMSGetLastError();
            if (error != "0") {
                this.handleError(error);
            }
            return value;
        }
        return "";
    },
    set: function(parameter, value) {
        var API = this.getAPI();
        if (API) {
            var result = API.LMSSetValue(parameter, value);
            var error = API.LMSGetLastError();
            if (error != "0") {
                this.handleError(error);
            }
            return result;
        }
        return "false";
    },
    initialize: function() {
        var API = this.getAPI();
        if (API) {
            var result = API.LMSInitialize("");
            var error = API.LMSGetLastError();
            if (error != "0") {
                this.handleError(error);
            }
            return result;
        }
        return "false";
    },
    commit: function() {
        var API = this.getAPI();
        if (API) {
            var result = API.LMSCommit("");
            var error = API.LMSGetLastError();
            if (error != "0") {
                this.handleError(error);
            }
            return result;
        }
        return "false";
    },
    finish: function() {
        var API = this.getAPI();
        if (API) {
            var result = API.LMSFinish("");
            var error = API.LMSGetLastError();
            if (error != "0") {
                this.handleError(error);
            }
            return result;
        }
        return "false";
    },
    getAPI: function() {
        var API = null;
        var findAPITries = 0;

        while ((API == null) && (findAPITries < 7)) {
            if (window.API != null) {
                API = window.API;
            } else if (window.parent != null && window.parent != window) {
                findAPITries++;
                window = window.parent;
            } else {
                findAPITries++;
            }
        }
        return API;
    }
};

function initializeSCORM() {
    scorm.initialize();
    scorm.set("cmi.core.lesson_status", "incomplete");
    scorm.set("cmi.core.session_time", "00:00:00");
    scorm.commit();
}

function completeSCORM() {
    scorm.set("cmi.core.lesson_status", "completed");
    scorm.set("cmi.core.score.raw", "100");
    scorm.commit();
    scorm.finish();
}
'''
    output_file = OUTPUT_DIR / "scorm_api.js"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(js_content)
    print(f"  [OK] Creado: {output_file.name}")

def create_imsmanifest(modules):
    """Create SCORM 1.2 manifest file"""
    resources_xml = ""
    for module in modules:
        resources_xml += f'''
    <resource identifier="{module['id']}" type="webcontent" adlcp:scormtype="sco" href="{module['id']}.html">
      <file href="{module['id']}.html"/>
      <file href="styles.css"/>
      <file href="scorm_api.js"/>
    </resource>'''

    items_xml = ""
    for i, module in enumerate(modules, 1):
        items_xml += f'''
      <item identifier="item_{module['id']}" identifierref="{module['id']}">
        <title>Sección {i}: {module['title']}</title>
      </item>'''

    manifest = f'''<?xml version="1.0" encoding="UTF-8"?>
<manifest identifier="esalud_aulas_virtuales" version="1.0"
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

  <organizations default="org_default">
    <organization identifier="org_default">
      <title>{COURSE_TITLE}</title>
      <item identifier="item_index" identifierref="index">
        <title>Índice del Programa</title>
      </item>{items_xml}
    </organization>
  </organizations>

  <resources>
    <resource identifier="index" type="webcontent" adlcp:scormtype="sco" href="index.html">
      <file href="index.html"/>
      <file href="styles.css"/>
      <file href="scorm_api.js"/>
    </resource>{resources_xml}
  </resources>

</manifest>'''

    output_file = OUTPUT_DIR / "imsmanifest.xml"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(manifest)
    print(f"  [OK] Creado: {output_file.name}")

def create_zip_package():
    """Create final SCORM ZIP package"""
    zip_path = ROOT_DIR / "output" / "programa-academico-esalud-scorm.zip"

    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file in OUTPUT_DIR.iterdir():
            if file.is_file():
                zipf.write(file, file.name)

    print(f"\n[OK] ¡Paquete SCORM creado con éxito!: {zip_path.name}")
    print(f"[OK] Tamaño: {zip_path.stat().st_size / 1024:.1f} KB")
    return zip_path

def main():
    print("=" * 60)
    print("ESALUD Academic Program SCORM Builder")
    print("=" * 60)
    print()

    # Parse sections
    print("Leyendo y procesando el archivo markdown...")
    modules = parse_markdown_file(INPUT_FILE)
    print(f"Encontradas {len(modules)} secciones académicas.")
    print()

    # Generate pages
    print("Generando páginas HTML...")
    create_index_html(modules)
    for i, module in enumerate(modules):
        prev_mod = modules[i-1] if i > 0 else None
        next_mod = modules[i+1] if i < len(modules)-1 else None
        create_module_html(module, modules, i, prev_mod, next_mod)
    print()

    # Create CSS, JS & XML Manifest
    print("Generando archivos de soporte...")
    create_css()
    create_scorm_api()
    create_imsmanifest(modules)
    print()

    # Create Zip
    print("Creando el paquete ZIP SCORM...")
    zip_path = create_zip_package()
    print()
    print("=" * 60)
    print("[OK] ¡Proceso de compilación finalizado con éxito!")
    print(f"Ubicación del paquete: {zip_path.absolute()}")
    print("=" * 60)

if __name__ == "__main__":
    main()
