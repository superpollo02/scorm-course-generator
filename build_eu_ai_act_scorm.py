#!/usr/bin/env python3
"""
EU AI Act SCORM Package Builder
Converts 4 modules from markdown to beautifully styled HTML SCORM 1.2 package
"""

import re
import zipfile
from pathlib import Path
from scorm_core import generar_manifest_scorm_unificado

# Base paths
CONTENT_DIR = Path("content/eu-ai-act-pmi")
OUTPUT_DIR = Path("output/eu-ai-act-pmi")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Course metadata
COURSE_TITLE = "EU AI Act: essentials e azioni pratiche per PMI"
COURSE_DESCRIPTION = "Corso completo sull'AI Act europeo per PMI italiane - 4 moduli, 2 ore totali"
COURSE_LANGUAGE = "it"

# Modules configuration
MODULES = [
    {
        "id": "modulo1",
        "file": "modulo1-panoramica.md",
        "title": "Modulo 1: Panoramica rapida e timeline AI Act",
        "duration": "20-25 minuti"
    },
    {
        "id": "modulo2",
        "file": "modulo2-casi-uso.md",
        "title": "Modulo 2: Mappa dei casi d'uso e rischio",
        "duration": "25-30 minuti"
    },
    {
        "id": "modulo3",
        "file": "modulo3-governance.md",
        "title": "Modulo 3: Governance e controlli minimi",
        "duration": "30-35 minuti"
    },
    {
        "id": "modulo4",
        "file": "modulo4-piano-90-giorni.md",
        "title": "Modulo 4: Piano 90 giorni",
        "duration": "25-30 minuti"
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

    # Wrap consecutive <li> items in <ul>
    html = re.sub(r'(<li>.*?</li>\n)+', lambda m: '<ul>\n' + m.group(0) + '</ul>\n', html, flags=re.DOTALL)

    # Tables - convert markdown tables to HTML
    def convert_table(match):
        table_text = match.group(0)
        lines = table_text.strip().split('\n')

        if len(lines) < 3:  # Need at least header, separator, and one row
            return table_text

        # Parse header
        header_cells = [cell.strip() for cell in lines[0].split('|')[1:-1]]

        # Parse rows (skip separator line)
        rows = []
        for line in lines[2:]:
            cells = [cell.strip() for cell in line.split('|')[1:-1]]
            if cells and any(cells):  # Only add non-empty rows
                rows.append(cells)

        # Build HTML table
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

    # Find and convert tables
    table_pattern = r'\|.+\|\n\|[-:\s|]+\|\n(?:\|.+\|\n)+'
    html = re.sub(table_pattern, convert_table, html, flags=re.MULTILINE)

    # Blockquotes
    html = re.sub(r'^> (.+)$', r'<blockquote>\1</blockquote>', html, flags=re.MULTILINE)

    # Code blocks
    html = re.sub(r'```(.+?)```', r'<pre><code>\1</code></pre>', html, flags=re.DOTALL)

    # Inline code
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

        # Check if line starts with HTML tag
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

    # Clean up double wrapping
    html = re.sub(r'<p><(h[1-6]|ul|ol|table|blockquote|pre|hr)>', r'<\1>', html)
    html = re.sub(r'</(h[1-6]|ul|ol|table|blockquote|pre|hr)></p>', r'</\1>', html)

    return html


def create_module_html(module, prev_module=None, next_module=None):
    """Create HTML file for a module"""

    # Read markdown content
    md_file = CONTENT_DIR / module["file"]
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Convert to HTML
    content_html = markdown_to_html(md_content)

    # Build navigation
    nav_html = '<div class="navigation">\n'

    if prev_module:
        nav_html += f'  <a href="{prev_module["id"]}.html" class="nav-button">← Anterior: {prev_module["title"]}</a>\n'
    else:
        nav_html += '  <span></span>\n'

    nav_html += '  <div class="nav-center">\n'
    nav_html += '    <a href="index.html" class="nav-button">📚 Índice</a>\n'
    nav_html += '  </div>\n'

    if next_module:
        nav_html += f'  <a href="{next_module["id"]}.html" class="nav-button">Siguiente: {next_module["title"]} →</a>\n'
    else:
        nav_html += '  <span></span>\n'

    nav_html += '</div>\n'

    # Full HTML template
    html_template = f'''<!DOCTYPE html>
<html lang="it">
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
        // Initialize SCORM
        window.addEventListener('load', function() {{
            initializeSCORM();
        }});

        window.addEventListener('beforeunload', function() {{
            completeSCORM();
        }});
    </script>
</body>
</html>'''

    # Write HTML file
    output_file = OUTPUT_DIR / f"{module['id']}.html"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_template)

    print(f"Created: {output_file.name}")


def create_index_html():
    """Create index/landing page"""

    modules_cards = ""
    for i, module in enumerate(MODULES, 1):
        modules_cards += f'''
        <a href="{module['id']}.html" class="module-card">
            <h3>Módulo {i}</h3>
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
            <div class="subtitle">Curso completo para PYMEs italianas</div>
            <div class="progress-indicator">Duración total: ~2 horas | 4 Módulos</div>
        </div>

        <div class="content">
            <div class="module-info">
                <h3>Objetivos del curso</h3>
                <ul>
                    <li>Comprender la Ley de IA de la UE y sus implicaciones para las PYMEs</li>
                    <li>Clasificar los sistemas de IA en las categorías de riesgo</li>
                    <li>Implementar controles mínimos de gobernanza</li>
                    <li>Planificar el cumplimiento con un plan operativo de 90 días</li>
                </ul>
            </div>

            <h2>Módulos del curso</h2>
            <div class="module-grid">
                {modules_cards}
            </div>

            <div class="info-box">
                <strong>Nota:</strong> Este curso está diseñado específicamente para PYMEs italianas que utilizan o planean utilizar sistemas de inteligencia artificial. Cada módulo incluye ejemplos prácticos, listas de verificación operativas y plantillas descargables.
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

    print(f"Created: {output_file.name}")


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

    print(f"Created: {output_file.name}")


def create_imsmanifest():
    """Create SCORM 1.2 manifest file using canonical scorm_core."""
    items = [{"id": "index", "title": "Índice del Curso", "href": "index.html"}]
    for i, m in enumerate(MODULES, 1):
        items.append({
            "id": m["id"],
            "title": f"Módulo {i}: {m['title']}",
            "href": f"{m['id']}.html"
        })
    manifest = generar_manifest_scorm_unificado(
        identifier="eu_ai_act_pmi",
        title=COURSE_TITLE,
        items=items,
        generator_name="Aula Lista EDUCAI Monolithic Course Builder"
    )
    output_file = OUTPUT_DIR / "imsmanifest.xml"
    output_file.write_text(manifest, encoding="utf-8")
    print(f"  [OK] Creado: {output_file.name}")

def create_zip_package():
    """Create final SCORM ZIP package"""

    zip_path = Path("output") / "eu-ai-act-pmi-scorm.zip"

    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file in OUTPUT_DIR.iterdir():
            if file.is_file():
                zipf.write(file, file.name)

    print(f"\n[SUCCESS] SCORM package created: {zip_path}")
    print(f"[OK] Size: {zip_path.stat().st_size / 1024:.1f} KB")
    return zip_path


def main():
    """Main build process"""
    print("=" * 60)
    print("EU AI Act SCORM Package Builder")
    print("=" * 60)
    print()

    # Create index page
    print("Creating index page...")
    create_index_html()
    print()

    # Create module pages
    print("Creating module pages...")
    for i, module in enumerate(MODULES):
        prev_module = MODULES[i-1] if i > 0 else None
        next_module = MODULES[i+1] if i < len(MODULES)-1 else None
        create_module_html(module, prev_module, next_module)
    print()

    # Create SCORM API
    print("Creating SCORM API...")
    create_scorm_api()
    print()

    # Create manifest
    print("Creating SCORM manifest...")
    create_imsmanifest()
    print()

    # Create ZIP package
    print("Creating ZIP package...")
    zip_path = create_zip_package()
    print()

    print("=" * 60)
    print("[SUCCESS] SCORM package build complete!")
    print("=" * 60)
    print()
    print(f"Package location: {zip_path.absolute()}")
    print()
    print("Para importar en Moodle:")
    print("1. Ve a tu curso de Moodle")
    print("2. Haz clic en 'Añadir una actividad o un recurso'")
    print("3. Selecciona 'Paquete SCORM'")
    print("4. Sube el archivo ZIP")
    print("5. Guardar cambios y mostrar")
    print()


if __name__ == "__main__":
    main()
