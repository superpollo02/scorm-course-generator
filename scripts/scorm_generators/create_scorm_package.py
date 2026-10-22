#!/usr/bin/env python3
"""
Create SCORM 1.2 package for the AI course
Compatible with all Moodle versions
"""

import os
import zipfile
import re

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

    # Convert tables
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
    """Convert markdown table to HTML"""
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

def split_into_modules(content):
    """Split content file into modules"""
    modules = []
    current_module = None
    current_content = []

    lines = content.split('\n')

    for line in lines:
        if line.startswith('# Modulo '):
            if current_module:
                modules.append({
                    'title': current_module,
                    'content': '\n'.join(current_content)
                })
            current_module = line.replace('# ', '').strip()
            current_content = []
        else:
            current_content.append(line)

    if current_module:
        modules.append({
            'title': current_module,
            'content': '\n'.join(current_content)
        })

    return modules

def create_scorm_html(title, content, prev_page=None, next_page=None, is_index=False):
    """Create SCORM-compatible HTML page"""

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
            max-width: 900px;
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
            color: #1f77b4;
            border-bottom: 3px solid #1f77b4;
            padding-bottom: 10px;
            margin-top: 0;
        }}
        h2 {{
            color: #2ca02c;
            margin-top: 30px;
            border-left: 4px solid #2ca02c;
            padding-left: 15px;
        }}
        h3 {{
            color: #ff7f0e;
            margin-top: 25px;
        }}
        h4 {{
            color: #d62728;
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
        .navigation {{
            position: sticky;
            top: 0;
            background: #1f77b4;
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
            color: #1f77b4;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 14px;
            font-weight: bold;
            transition: all 0.3s;
        }}
        .navigation button:hover {{
            background: #f0f8ff;
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
            background: #f0f8ff;
            color: #1f77b4;
            text-decoration: none;
            border-radius: 5px;
            border-left: 4px solid #1f77b4;
            transition: all 0.3s;
            font-size: 16px;
        }}
        .index-list a:hover {{
            background: #1f77b4;
            color: white;
            transform: translateX(10px);
        }}
        .course-header {{
            text-align: center;
            margin-bottom: 40px;
            padding: 20px;
            background: linear-gradient(135deg, #1f77b4, #2ca02c);
            color: white;
            border-radius: 8px;
        }}
        .course-header h1 {{
            color: white;
            border: none;
            margin: 0;
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
            background: linear-gradient(135deg, #1f77b4, #2ca02c);
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
            background: #f8f9fa;
        }}
        .data-table tbody tr:hover {{
            background: #f0f8ff;
            transition: background 0.3s;
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
        filename = f"modulo_{i:02d}.html"
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
<manifest identifier="com.aiprincipanti.scorm" version="1.0"
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
      <title>Introduzione all'Intelligenza Artificiale per Principianti</title>
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
    """Create complete SCORM package"""

    # Read content
    content_file = 'course-content-edited.md'
    if not os.path.exists(content_file):
        print(f"Error: {content_file} not found")
        return

    with open(content_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split into modules
    modules = split_into_modules(content)

    # Create temp directory
    scorm_dir = 'scorm_package'
    os.makedirs(scorm_dir, exist_ok=True)

    print("Creating SCORM package...")
    print(f"Found {len(modules)} modules")

    # Create index page
    index_content = '''<div class="course-header">
    <h1>Introduzione all'Intelligenza Artificiale per Principianti</h1>
    <p>Corso completo in 10 moduli</p>
</div>
<p><strong>Benvenuto!</strong> Questo corso ti guiderà attraverso i fondamenti dell'intelligenza artificiale.</p>
<p>Seleziona un modulo dall'elenco qui sotto per iniziare:</p>
<ul class="index-list">
'''

    for i, module in enumerate(modules, 1):
        title = module['title']
        filename = f"modulo_{i:02d}.html"
        index_content += f'  <li><a href="{filename}">{title}</a></li>\n'

    index_content += '</ul>'

    index_html = create_scorm_html(
        "Indice del Corso",
        index_content,
        is_index=True
    )

    with open(os.path.join(scorm_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(index_html)

    print("  [OK] Created index.html")

    # Create module pages
    for i, module in enumerate(modules, 1):
        title = module['title']
        filename = f"modulo_{i:02d}.html"

        # Determine prev/next
        prev_page = f"modulo_{i-1:02d}.html" if i > 1 else None
        next_page = f"modulo_{i+1:02d}.html" if i < len(modules) else None

        # Convert content to HTML
        html_content = markdown_to_html(module['content'])

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
    zip_filename = 'AI-Principianti-SCORM.zip'
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(scorm_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, scorm_dir)
                zipf.write(file_path, arcname)

    print(f"\n[OK] SCORM package created: {zip_filename}")
    print(f"[OK] Size: {os.path.getsize(zip_filename) / 1024:.1f} KB")
    print(f"\nTo import in Moodle:")
    print("1. Go to your course")
    print("2. Click 'Aggiungi un'attività o una risorsa'")
    print("3. Select 'Pacchetto SCORM'")
    print("4. Upload AI-Principianti-SCORM.zip")
    print("5. Save - Done!")

if __name__ == '__main__':
    create_scorm_package()
