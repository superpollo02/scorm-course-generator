#!/usr/bin/env python3
"""
Create SCORM 1.2 package for Sicurezza sul Lavoro course
Compatible with all Moodle versions
Handles 4 modules + final test with proper formatting
"""

import os
import zipfile

def markdown_to_html(md_text):
    """Delega la conversión al motor canónico optimizado de scorm_modern."""
    from scorm_modern.renderer import markdown_to_html as _m2h
    return _m2h(md_text)


def convert_table(table_rows):
    """Delega la conversión de tablas al motor canónico optimizado de scorm_modern."""
    from scorm_modern.renderer import _convert_table
    return _convert_table(table_rows)


def create_scorm_html(title, content, prev_page=None, next_page=None, is_index=False):
    """Create SCORM-compatible HTML page with beautiful styling"""

    nav_buttons = ''
    if not is_index:
        nav_buttons = '<div class="navigation">'
        if prev_page:
            nav_buttons += f'<button onclick="gotoPrevious()">&larr; Anterior</button>'
        nav_buttons += '<button onclick="gotoIndex()">&#8962; Índice</button>'
        if next_page:
            nav_buttons += f'<button onclick="gotoNext()">Siguiente &rarr;</button>'
        nav_buttons += '</div>'

    scorm_script = ''
    if not is_index:
        scorm_script = f'''
<script type="text/javascript">
    var API = null;

    function findAPI(win) {{
        while (win.API == null && win.parent != null && win.parent != win) {{
            win = win.parent;
        }}
        return win.API;
    }}

    function initSCORM() {{
        API = findAPI(window);
        if (API != null) {{
            API.LMSInitialize("");
            API.LMSSetValue("cmi.core.lesson_status", "incomplete");
        }}
    }}

    function finishSCORM() {{
        if (API != null) {{
            API.LMSSetValue("cmi.core.lesson_status", "completed");
            API.LMSSetValue("cmi.core.score.raw", "100");
            API.LMSFinish("");
        }}
    }}

    function gotoPrevious() {{
        {f'window.location.href = "{prev_page}";' if prev_page else ''}
    }}

    function gotoNext() {{
        {f'window.location.href = "{next_page}";' if next_page else ''}
    }}

    function gotoIndex() {{
        window.location.href = "index.html";
    }}

    window.onload = initSCORM;
    window.onbeforeunload = finishSCORM;
</script>
'''

    html = f'''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    {scorm_script}
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            max-width: 1000px;
            margin: 0 auto;
            padding: 20px;
            color: #333;
            background: #f5f5f5;
        }}
        .container {{
            background: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        h1 {{
            color: #c62828;
            border-bottom: 3px solid #c62828;
            padding-bottom: 10px;
            margin-top: 0;
        }}
        h2 {{
            color: #e65100;
            margin-top: 30px;
            border-left: 4px solid #e65100;
            padding-left: 15px;
        }}
        h3 {{
            color: #f57c00;
            margin-top: 25px;
        }}
        h4 {{
            color: #ef6c00;
            margin-top: 20px;
        }}
        ul, ol {{
            margin: 15px 0;
            padding-left: 30px;
        }}
        li {{
            margin: 8px 0;
        }}
        strong {{
            color: #000;
            font-weight: 600;
        }}
        em {{
            color: #555;
        }}
        p {{
            margin: 15px 0;
            text-align: justify;
        }}
        hr {{
            border: none;
            border-top: 2px solid #e0e0e0;
            margin: 30px 0;
        }}
        pre {{
            background: #f5f5f5;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
            border-left: 4px solid #c62828;
        }}
        code {{
            font-family: 'Courier New', monospace;
            font-size: 14px;
        }}
        details {{
            margin: 20px 0;
            padding: 15px;
            background: #fff3e0;
            border-left: 4px solid #ff9800;
            border-radius: 5px;
        }}
        summary {{
            cursor: pointer;
            font-weight: bold;
            color: #e65100;
            margin-bottom: 10px;
        }}
        summary:hover {{
            color: #c62828;
        }}
        .navigation {{
            position: sticky;
            top: 0;
            background: #c62828;
            padding: 15px;
            margin: -30px -30px 30px -30px;
            border-radius: 8px 8px 0 0;
            display: flex;
            justify-content: space-between;
            gap: 10px;
            z-index: 100;
        }}
        .navigation button {{
            background: white;
            color: #c62828;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 14px;
            font-weight: bold;
            transition: all 0.3s;
        }}
        .navigation button:hover {{
            background: #ffebee;
            transform: translateY(-2px);
        }}
        .index-list {{
            list-style: none;
            padding: 0;
        }}
        .index-list li {{
            margin: 15px 0;
        }}
        .index-list a {{
            display: block;
            padding: 15px;
            background: #ffebee;
            color: #c62828;
            text-decoration: none;
            border-radius: 5px;
            border-left: 4px solid #c62828;
            transition: all 0.3s;
            font-size: 16px;
        }}
        .index-list a:hover {{
            background: #c62828;
            color: white;
            transform: translateX(10px);
        }}
        .course-header {{
            text-align: center;
            margin-bottom: 40px;
            padding: 30px;
            background: linear-gradient(135deg, #c62828, #e65100);
            color: white;
            border-radius: 8px;
        }}
        .course-header h1 {{
            color: white;
            border: none;
            margin: 0;
            font-size: 32px;
        }}
        .course-header p {{
            margin: 10px 0 0 0;
            font-size: 18px;
        }}
        .data-table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            background: white;
        }}
        .data-table thead {{
            background: linear-gradient(135deg, #c62828, #e65100);
            color: white;
        }}
        .data-table th {{
            padding: 12px 15px;
            text-align: left;
            font-weight: bold;
            border: 1px solid #ddd;
        }}
        .data-table td {{
            padding: 10px 15px;
            border: 1px solid #ddd;
        }}
        .data-table tbody tr:nth-child(even) {{
            background: #fff3e0;
        }}
        .data-table tbody tr:hover {{
            background: #ffebee;
            transition: background 0.3s;
        }}
        .warning-box {{
            background: #fff3e0;
            border-left: 5px solid #ff9800;
            padding: 15px;
            margin: 20px 0;
            border-radius: 5px;
        }}
        .info-box {{
            background: #e3f2fd;
            border-left: 5px solid #2196f3;
            padding: 15px;
            margin: 20px 0;
            border-radius: 5px;
        }}
    </style>
</head>
<body>
    <div class="container">
        {nav_buttons}
        {content}
    </div>
</body>
</html>
'''
    return html

def create_imsmanifest(modules):
    """Create SCORM 1.2 imsmanifest.xml"""

    resources = ''
    items = ''

    # Index page
    resources += '''    <resource identifier="resource_index" type="webcontent" adlcp:scormtype="sco" href="index.html">
      <file href="index.html"/>
    </resource>
'''
    items += '''      <item identifier="item_index" identifierref="resource_index">
        <title>Índice del Curso</title>
      </item>
'''

    # Module pages
    for i, module in enumerate(modules, 1):
        filename = module['filename']
        resource_id = f"resource_{i:02d}"
        item_id = f"item_{i:02d}"
        title = module['title']

        resources += f'''    <resource identifier="{resource_id}" type="webcontent" adlcp:scormtype="sco" href="{filename}">
      <file href="{filename}"/>
    </resource>
'''
        items += f'''      <item identifier="{item_id}" identifierref="{resource_id}">
        <title>{title}</title>
      </item>
'''

    manifest = f'''<?xml version="1.0" encoding="UTF-8"?>
<manifest identifier="com.sicurezzalavoro.scorm" version="1.0"
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
      <title>Sicurezza sul Lavoro - Formazione Generale Lavoratori</title>
{items}
    </organization>
  </organizations>
  <resources>
{resources}
  </resources>
</manifest>
'''
    return manifest

def create_scorm_package():
    """Create complete SCORM package for Sicurezza sul Lavoro course"""

    # Define the 4 modules
    modules = [
        {
            'source_file': 'modulo1-content.md',
            'filename': 'modulo1.html',
            'title': 'Modulo 1: Rischio, Prevenzione e Organizzazione Aziendale'
        },
        {
            'source_file': 'modulo2-content.md',
            'filename': 'modulo2.html',
            'title': 'Modulo 2: I Soggetti della Sicurezza e i Loro Ruoli'
        },
        {
            'source_file': 'modulo3-content.md',
            'filename': 'modulo3.html',
            'title': 'Modulo 3: Protezione, Vigilanza e Formazione Continua'
        },
        {
            'source_file': 'test-finale.md',
            'filename': 'test-finale.html',
            'title': 'Test Finale'
        }
    ]

    # Verify all source files exist
    for module in modules:
        if not os.path.exists(module['source_file']):
            print(f"ERROR: File not found: {module['source_file']}")
            return

    # Create temp directory
    scorm_dir = 'scorm_package'
    os.makedirs(scorm_dir, exist_ok=True)

    print("Creating SCORM package for Sicurezza sul Lavoro...")
    print(f"Found {len(modules)} modules")

    # Create index page
    index_content = '''<div class="course-header">
    <h1>Sicurezza sul Lavoro</h1>
    <p>Formazione Generale Lavoratori - D.Lgs. 81/2008</p>
    <p>Durata: 4 ore</p>
</div>
<div class="info-box">
    <p><strong>Benvenuto!</strong> Questo corso ti fornirà le conoscenze fondamentali sulla sicurezza sul lavoro, come previsto dal D.Lgs. 81/2008.</p>
    <p>Il corso è diviso in 3 moduli teorici seguiti da un test finale di verifica.</p>
</div>
<p>Seleziona un modulo dall'elenco qui sotto per iniziare:</p>
<ul class="index-list">
'''

    for module in modules:
        title = module['title']
        filename = module['filename']
        index_content += f'  <li><a href="{filename}">{title}</a></li>\n'

    index_content += '''</ul>
<div class="warning-box">
    <p><strong>Attenzione:</strong> Al termine dei 3 moduli è obbligatorio completare il test finale con un punteggio minimo del 70% (21/30) per ottenere l'attestato.</p>
</div>
'''

    index_html = create_scorm_html(
        "Indice del Corso",
        index_content,
        is_index=True
    )

    with open(os.path.join(scorm_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(index_html)

    print("  [OK] Created index.html")

    # Create module pages
    for i, module in enumerate(modules):
        source_file = module['source_file']
        filename = module['filename']
        title = module['title']

        # Read source content
        with open(source_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Determine prev/next
        prev_page = modules[i-1]['filename'] if i > 0 else None
        next_page = modules[i+1]['filename'] if i < len(modules) - 1 else None

        # Convert content to HTML
        html_content = markdown_to_html(content)

        # Create full page
        page_html = create_scorm_html(
            title,
            html_content,
            prev_page=prev_page,
            next_page=next_page
        )

        filepath = os.path.join(scorm_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(page_html)

        print(f"  [OK] Created {filename}")

    # Create imsmanifest.xml
    manifest = create_imsmanifest(modules)
    with open(os.path.join(scorm_dir, 'imsmanifest.xml'), 'w', encoding='utf-8') as f:
        f.write(manifest)

    print("  [OK] Created imsmanifest.xml")

    # Create ZIP package
    zip_filename = 'sicurezza-lavoro-scorm.zip'
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(scorm_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, scorm_dir)
                zipf.write(file_path, arcname)

    print(f"\n[SUCCESS] SCORM package created: {zip_filename}")
    print(f"[INFO] Size: {os.path.getsize(zip_filename) / 1024:.1f} KB")
    print(f"[INFO] Location: {os.path.abspath(zip_filename)}")
    print(f"\n" + "="*60)
    print("ISTRUZIONI PER L'IMPORT IN MOODLE:")
    print("="*60)
    print("1. Accedi al tuo corso Moodle")
    print("2. Clicca su 'Aggiungi un'attività o una risorsa'")
    print("3. Seleziona 'Pacchetto SCORM'")
    print("4. Carica il file: sicurezza-lavoro-scorm.zip")
    print("5. Salva e visualizza")
    print("="*60)

if __name__ == '__main__':
    create_scorm_package()
