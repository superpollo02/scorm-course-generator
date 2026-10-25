#!/usr/bin/env python3
"""
Sistemas de Salud Comparados SCORM Package Builder
Converts the markdown units into a beautifully styled HTML SCORM 1.2 package.
"""

import re
import zipfile
from pathlib import Path
from scorm_core import generar_manifest_scorm_unificado

# Paths
ROOT_DIR = Path(__file__).parent.resolve()
CONTENT_DIR = ROOT_DIR / "content/sistemas-salud-comparados"
OUTPUT_DIR = ROOT_DIR / "output/sistemas-salud-comparados"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Course metadata
COURSE_TITLE = "Sistemas de Salud Comparados"
COURSE_SUBTITLE = "Plan de Estudios 2025 - Lic. en Administración de Salud"
COURSE_DESCRIPTION = "Estudio sistemático de los modelos sanitarios a nivel internacional y análisis del proceso de reconversión del Sector Salud en la República Argentina."
COURSE_LANGUAGE = "es"

MODULES = [
    {
        "id": "unidad1",
        "file": "unidad1.md",
        "title": "Unidad I: La Salud y las Ciencias Sociales",
        "duration": "Lectura estimada: 25 min"
    },
    {
        "id": "unidad2",
        "file": "unidad2.md",
        "title": "Unidad II: Evolución de la Salud Pública",
        "duration": "Lectura estimada: 25 min"
    },
    {
        "id": "unidad3",
        "file": "unidad3.md",
        "title": "Unidad III: Sistemas de Salud",
        "duration": "Lectura estimada: 25 min"
    },
    {
        "id": "unidad4",
        "file": "unidad4.md",
        "title": "Unidad IV: Economía de la Salud",
        "duration": "Lectura estimada: 25 min"
    }
]

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

        header_cells = [cell.strip() for cell in lines[0].split('|')[1:-1]]
        rows = []
        for line in lines[2:]:
            cells = [cell.strip() for cell in line.split('|')[1:-1]]
            if cells and any(cells):
                rows.append(cells)

        table_html = '<table>\n<thead>\n<tr>\n'
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

    table_pattern = r'\|.+\|\n\|[-:\s|]+\|\n(?:\|.+\|\n)+'
    html = re.sub(table_pattern, convert_table, html, flags=re.MULTILINE)

    # Blockquotes
    html = re.sub(r'^> (.+)$', r'<blockquote>\1</blockquote>', html, flags=re.MULTILINE)

    # Code/Text blocks
    html = re.sub(r'```(.+?)```', r'<pre><code>\1</code></pre>', html, flags=re.DOTALL)
    html = re.sub(r'`(.+?)`', r'<code>\1</code>', html)

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

        if re.match(r'<(h[1-6]|ul|ol|li|table|thead|tbody|tr|th|td|blockquote|pre|hr|div)', stripped):
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
    html = re.sub(r'<p><(h[1-6]|ul|ol|table|blockquote|pre|hr)>', r'<\1>', html)
    html = re.sub(r'</(h[1-6]|ul|ol|table|blockquote|pre|hr)></p>', r'</\1>', html)

    return html

def create_module_html(module, prev_mod=None, next_mod=None):
    """Create HTML file for a module"""
    md_file = CONTENT_DIR / module["file"]
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()

    content_html = markdown_to_html(md_content)

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

def create_index_html():
    """Create index/landing page"""
    modules_cards = ""
    for i, module in enumerate(MODULES, 1):
        modules_cards += f'''
        <a href="{module['id']}.html" class="module-card">
            <h3>Unidad {i}</h3>
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
            <div class="progress-indicator">4 Unidades Temáticas</div>
        </div>

        <div class="content">
            <div class="module-info">
                <h3>Resumen de la Asignatura</h3>
                <p>{COURSE_DESCRIPTION}</p>
                <p>Este espacio digital interactivo te guiará a través de la evolución de las ciencias sociales aplicadas a la salud, el surgimiento y organización de la salud pública, los modelos sanitarios y el análisis del gasto desde la economía de la salud.</p>
            </div>

            <h2>Programa del Curso</h2>
            <div class="module-grid">
                {modules_cards}
            </div>

            <div class="info-box">
                <strong>Instrucciones:</strong> Haz clic en la primera unidad para iniciar. Puedes avanzar y retroceder usando los botones inferiores. Tu progreso se guardará automáticamente en el aula virtual.
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
    css_content = '''/* SCORM Professional Stylesheet - Medical/Health Theme */
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
    background: #f7fdfc;
    border-left: 4px solid #00897b;
    padding: 20px;
    border-radius: 4px;
    margin-bottom: 30px;
}

.module-info h3 {
    margin-top: 0;
}

.info-box {
    background-color: #e8f5e9;
    border-left: 4px solid #2e7d32;
    padding: 15px;
    margin-top: 30px;
    border-radius: 4px;
}

/* Module Grid */
.module-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
    margin-top: 20px;
}

@media(max-width: 600px) {
    .module-grid {
        grid-template-columns: 1fr;
    }
    .content {
        padding: 20px;
    }
}

.module-card {
    background: #fafafa;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    padding: 20px;
    text-decoration: none;
    color: inherit;
    transition: all 0.3s ease;
    display: flex;
    flex-direction: column;
}

.module-card:hover {
    border-color: #00897b;
    box-shadow: 0 5px 15px rgba(0,137,123,0.1);
    transform: translateY(-2px);
}

.module-card h3 {
    margin: 0 0 10px 0;
    font-size: 1.1em;
}

.module-card .duration {
    font-size: 0.85em;
    color: #00796b;
    font-weight: 600;
    margin-bottom: 8px;
}

.module-card .description {
    font-size: 0.9em;
    color: #555;
    flex-grow: 1;
}

/* Navigation Buttons */
.navigation {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 20px 40px;
    background: #f5f5f5;
    border-top: 1px solid #e0e0e0;
}

.nav-button {
    background-color: #00796b;
    color: white;
    padding: 10px 20px;
    border-radius: 4px;
    text-decoration: none;
    font-weight: 500;
    font-size: 0.9em;
    transition: background-color 0.2s;
}

.nav-button:hover {
    background-color: #004d40;
}

.nav-center {
    display: flex;
    justify-content: center;
}

/* Tables styling */
table {
    width: 100%;
    border-collapse: collapse;
    margin: 25px 0;
    font-size: 0.9em;
}

th, td {
    padding: 12px 15px;
    text-align: left;
    border-bottom: 1px solid #e0e0e0;
}

th {
    background-color: #00796b;
    color: white;
    font-weight: 600;
}

tr:hover {
    background-color: #f2faf9;
}

pre {
    background-color: #f5f5f5;
    padding: 15px;
    border-radius: 5px;
    overflow-x: auto;
    margin: 20px 0;
}

code {
    font-family: 'Courier New', Courier, monospace;
    background-color: #f5f5f5;
    padding: 2px 5px;
    border-radius: 3px;
    font-size: 0.9em;
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
        var currentWindow = window;

        while ((API == null) && (findAPITries < 7)) {
            if (currentWindow.API != null) {
                API = currentWindow.API;
            } else if (currentWindow.parent != null && currentWindow.parent != currentWindow) {
                findAPITries++;
                currentWindow = currentWindow.parent;
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

def create_imsmanifest():
    """Create SCORM 1.2 manifest file using canonical scorm_core."""
    items = [{"id": "index", "title": "Índice del Curso", "href": "index.html"}]
    for i, m in enumerate(MODULES, 1):
        items.append({
            "id": m["id"],
            "title": f"Unidad {i}: {m['title']}",
            "href": f"{m['id']}.html"
        })
    manifest = generar_manifest_scorm_unificado(
        identifier="sistemas_salud_comparados",
        title=COURSE_TITLE,
        items=items,
        generator_name="Aula Lista EDUCAI Monolithic Course Builder"
    )
    output_file = OUTPUT_DIR / "imsmanifest.xml"
    output_file.write_text(manifest, encoding="utf-8")
    print(f"  [OK] Creado: {output_file.name}")

def create_zip_package():
    """Create final SCORM ZIP package"""
    zip_path = ROOT_DIR / "output/sistemas-salud-comparados-scorm.zip"

    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file in OUTPUT_DIR.iterdir():
            if file.is_file():
                zipf.write(file, file.name)

    print(f"\n[OK] Paquete SCORM ZIP creado en: {zip_path}")
    print(f"     Tamaño: {zip_path.stat().st_size / 1024:.1f} KB")
    return zip_path

def main():
    print("=" * 60)
    print("Sistemas de Salud Comparados SCORM Builder")
    print("=" * 60)

    # Create supporting assets
    create_css()
    create_scorm_api()

    # Create index
    create_index_html()

    # Create module pages
    for i, module in enumerate(MODULES):
        prev_mod = MODULES[i-1] if i > 0 else None
        next_mod = MODULES[i+1] if i < len(MODULES)-1 else None
        create_module_html(module, prev_mod, next_mod)

    # Create manifest
    create_imsmanifest()

    # Zip
    create_zip_package()
    print("=" * 60)

if __name__ == "__main__":
    main()
