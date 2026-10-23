#!/usr/bin/env python3
"""
Create SCORM 1.2 package for Workplace Safety Course (Sicurezza sul Lavoro)
Compatible with all Moodle versions
"""

import os
import zipfile
import re
from pathlib import Path

def markdown_to_html(md_text):
    """Convert markdown to HTML"""
    html = md_text

    # Headers
    html = re.sub(r'^# (.*?)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.*?)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^### (.*?)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^#### (.*?)$', r'<h4>\1</h4>', html, flags=re.MULTILINE)

    # Bold and italic
    html = re.sub(r'\*\*\*(.*?)\*\*\*', r'<strong><em>\1</em></strong>', html)
    html = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*(.*?)\*', r'<em>\1</em>', html)

    # Convert tables and lists
    lines = html.split('\n')
    in_ul = False
    in_ol = False
    in_table = False
    table_rows = []
    result = []

    for line in lines:
        stripped = line.strip()

        # Check if this is a table row
        if '|' in stripped and not stripped.startswith('<'):
            if not in_table:
                in_table = True
                table_rows = []
            table_rows.append(stripped)
        else:
            # End of table, process it
            if in_table:
                result.append(convert_table(table_rows))
                in_table = False
                table_rows = []

            # Process lists
            if stripped.startswith('- ') or stripped.startswith('* '):
                if not in_ul:
                    result.append('<ul>')
                    in_ul = True
                content = stripped[2:]
                result.append(f'  <li>{content}</li>')
            elif re.match(r'^\d+\.\s', stripped):
                if not in_ol:
                    result.append('<ol>')
                    in_ol = True
                content = re.sub(r'^\d+\.\s', '', stripped)
                result.append(f'  <li>{content}</li>')
            else:
                if in_ul:
                    result.append('</ul>')
                    in_ul = False
                if in_ol:
                    result.append('</ol>')
                    in_ol = False
                if stripped:
                    result.append(line)

    # Handle remaining table
    if in_table:
        result.append(convert_table(table_rows))

    if in_ul:
        result.append('</ul>')
    if in_ol:
        result.append('</ol>')

    return '\n'.join(result)

def convert_table(table_rows):
    """Convert markdown table to HTML with beautiful styling"""
    if len(table_rows) < 2:
        return '\n'.join(table_rows)

    html = '<table class="data-table">\n'

    for i, row in enumerate(table_rows):
        # Skip separator row (usually row 1)
        if i == 1 and re.match(r'^\|[\s\-:|]+\|$', row):
            continue

        # Clean up the row
        cells = [cell.strip() for cell in row.split('|')]
        cells = [c for c in cells if c]  # Remove empty cells

        if not cells:
            continue

        # First row is header
        if i == 0:
            html += '<thead>\n<tr>\n'
            for cell in cells:
                html += f'  <th>{cell}</th>\n'
            html += '</tr>\n</thead>\n<tbody>\n'
        else:
            html += '<tr>\n'
            for cell in cells:
                html += f'  <td>{cell}</td>\n'
            html += '</tr>\n'

    html += '</tbody>\n</table>'
    return html

def create_scorm_html(title, content, prev_page=None, next_page=None, is_index=False):
    """Create SCORM-compatible HTML page"""

    nav_buttons = ''
    if not is_index:
        nav_buttons = '<div class="navigation">'
        if prev_page:
            nav_buttons += f'<button onclick="gotoPrevious()">&larr; Precedente</button>'
        nav_buttons += '<button onclick="gotoIndex()">&#8962; Indice</button>'
        if next_page:
            nav_buttons += f'<button onclick="gotoNext()">Successivo &rarr;</button>'
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
<html lang="it">
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
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        }}
        .container {{
            background: white;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.15);
        }}
        h1 {{
            color: #d32f2f;
            border-bottom: 4px solid #d32f2f;
            padding-bottom: 12px;
            margin-top: 0;
            font-size: 28px;
        }}
        h2 {{
            color: #f57c00;
            margin-top: 30px;
            border-left: 5px solid #f57c00;
            padding-left: 15px;
            font-size: 24px;
        }}
        h3 {{
            color: #1976d2;
            margin-top: 25px;
            font-size: 20px;
        }}
        h4 {{
            color: #388e3c;
            margin-top: 20px;
            font-size: 18px;
        }}
        ul, ol {{
            margin: 15px 0;
            padding-left: 30px;
        }}
        li {{
            margin: 10px 0;
            line-height: 1.8;
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
            line-height: 1.8;
        }}
        .navigation {{
            position: sticky;
            top: 0;
            background: linear-gradient(135deg, #d32f2f, #c62828);
            padding: 15px;
            margin: -30px -30px 30px -30px;
            border-radius: 12px 12px 0 0;
            display: flex;
            justify-content: space-between;
            gap: 10px;
            z-index: 100;
            box-shadow: 0 2px 10px rgba(0,0,0,0.2);
        }}
        .navigation button {{
            background: white;
            color: #d32f2f;
            border: none;
            padding: 12px 24px;
            border-radius: 6px;
            cursor: pointer;
            font-size: 14px;
            font-weight: bold;
            transition: all 0.3s;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }}
        .navigation button:hover {{
            background: #fff3e0;
            transform: translateY(-2px);
            box-shadow: 0 4px 10px rgba(0,0,0,0.2);
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
            padding: 18px;
            background: linear-gradient(135deg, #fff3e0, #ffe0b2);
            color: #d32f2f;
            text-decoration: none;
            border-radius: 8px;
            border-left: 5px solid #d32f2f;
            transition: all 0.3s;
            font-size: 16px;
            font-weight: 500;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }}
        .index-list a:hover {{
            background: linear-gradient(135deg, #d32f2f, #c62828);
            color: white;
            transform: translateX(10px);
            box-shadow: 0 4px 15px rgba(211, 47, 47, 0.3);
        }}
        .course-header {{
            text-align: center;
            margin-bottom: 40px;
            padding: 30px;
            background: linear-gradient(135deg, #d32f2f, #f57c00);
            color: white;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(211, 47, 47, 0.3);
        }}
        .course-header h1 {{
            color: white;
            border: none;
            margin: 0;
            font-size: 32px;
        }}
        .course-header p {{
            margin: 15px 0 0 0;
            font-size: 18px;
            opacity: 0.95;
        }}
        .data-table {{
            width: 100%;
            border-collapse: collapse;
            margin: 25px 0;
            box-shadow: 0 2px 15px rgba(0,0,0,0.1);
            background: white;
            border-radius: 8px;
            overflow: hidden;
        }}
        .data-table thead {{
            background: linear-gradient(135deg, #d32f2f, #f57c00);
            color: white;
        }}
        .data-table th {{
            padding: 15px 18px;
            text-align: left;
            font-weight: bold;
            border: 1px solid #ddd;
            font-size: 15px;
        }}
        .data-table td {{
            padding: 12px 18px;
            border: 1px solid #e0e0e0;
            font-size: 14px;
        }}
        .data-table tbody tr:nth-child(even) {{
            background: #fff3e0;
        }}
        .data-table tbody tr:hover {{
            background: #ffe0b2;
            transition: background 0.3s;
        }}
        .warning-box {{
            background: #fff3e0;
            border-left: 5px solid #f57c00;
            padding: 15px;
            margin: 20px 0;
            border-radius: 5px;
        }}
        .info-box {{
            background: #e3f2fd;
            border-left: 5px solid #1976d2;
            padding: 15px;
            margin: 20px 0;
            border-radius: 5px;
        }}
        hr {{
            border: none;
            border-top: 2px solid #e0e0e0;
            margin: 30px 0;
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
        <title>Indice del Corso</title>
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
    """Create complete SCORM package for workplace safety course"""

    # Define modules with their source files
    modules = [
        {
            'source_file': 'modulo1-content.md',
            'title': 'Modulo 1: Rischio, Prevenzione e Organizzazione Aziendale',
            'filename': 'modulo_01.html'
        },
        {
            'source_file': 'modulo2-content.md',
            'title': 'Modulo 2: I Soggetti della Sicurezza e i Loro Ruoli',
            'filename': 'modulo_02.html'
        },
        {
            'source_file': 'modulo3-content.md',
            'title': 'Modulo 3: I Principali Rischi e le Misure di Prevenzione',
            'filename': 'modulo_03.html'
        },
        {
            'source_file': 'test-finale.md',
            'title': 'Test Finale - Valutazione Conoscenze',
            'filename': 'test_finale.html'
        }
    ]

    # Create temp directory
    scorm_dir = 'scorm_package'
    os.makedirs(scorm_dir, exist_ok=True)

    print("Creating SCORM package for Workplace Safety Course...")
    print(f"Modules to process: {len(modules)}\n")

    # Create index page
    index_content = '''<div class="course-header">
    <h1>Sicurezza sul Lavoro</h1>
    <p>Formazione Generale Lavoratori - D.Lgs. 81/2008</p>
    <p style="font-size: 16px; margin-top: 10px;">Durata: 4 ore + Test Finale</p>
</div>
<div class="info-box">
    <p><strong>Benvenuto al corso di formazione sulla sicurezza sul lavoro!</strong></p>
    <p>Questo corso è conforme al D.Lgs. 81/2008 e ti fornirà le conoscenze fondamentali per lavorare in sicurezza.</p>
    <p>Il corso è strutturato in 3 moduli formativi più un test finale di verifica dell'apprendimento.</p>
</div>
<p style="font-size: 18px; font-weight: 600; margin-top: 30px;">Seleziona un modulo per iniziare:</p>
<ul class="index-list">
'''

    for i, module in enumerate(modules, 1):
        title = module['title']
        filename = module['filename']
        index_content += f'  <li><a href="{filename}">{title}</a></li>\n'

    index_content += '''</ul>
<div class="warning-box">
    <p><strong>Nota importante:</strong> Per ottenere l'attestato devi completare tutti i moduli e superare il test finale con almeno il 70% di risposte corrette.</p>
</div>
'''

    index_html = create_scorm_html(
        "Indice del Corso - Sicurezza sul Lavoro",
        index_content,
        is_index=True
    )

    with open(os.path.join(scorm_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(index_html)

    print("  [OK] Created index.html")

    # Create module pages
    for i, module in enumerate(modules, 1):
        source_file = module['source_file']
        title = module['title']
        filename = module['filename']

        # Check if source file exists
        if not os.path.exists(source_file):
            print(f"  [ERROR] Source file not found: {source_file}")
            continue

        # Read source content
        with open(source_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Determine prev/next
        prev_page = modules[i-2]['filename'] if i > 1 else None
        next_page = modules[i]['filename'] if i < len(modules) else None

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

        print(f"  [OK] Created {filename} from {source_file}")

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

    file_size_kb = os.path.getsize(zip_filename) / 1024

    print(f"\n{'='*70}")
    print(f"SUCCESS! SCORM package created successfully!")
    print(f"{'='*70}")
    print(f"Package: {zip_filename}")
    print(f"Size: {file_size_kb:.1f} KB")
    print(f"Location: {os.path.abspath(zip_filename)}")
    print(f"\n{'='*70}")
    print("IMPORT TO MOODLE:")
    print(f"{'='*70}")
    print("1. Accedi al tuo corso Moodle")
    print("2. Clicca su 'Aggiungi un'attività o una risorsa'")
    print("3. Seleziona 'Pacchetto SCORM'")
    print(f"4. Carica il file: {zip_filename}")
    print("5. Salva - Fatto!")
    print(f"{'='*70}\n")

if __name__ == '__main__':
    create_scorm_package()
