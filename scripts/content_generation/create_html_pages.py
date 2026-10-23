#!/usr/bin/env python3
"""
Create individual HTML files for each module section
Ready to copy-paste into Moodle pages
"""

import os
import re
from pathlib import Path

def markdown_to_html(md_text):
    """Convert basic markdown to HTML"""
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
    html = re.sub(r'__(.*?)__', r'<strong>\1</strong>', html)
    html = re.sub(r'_(.*?)_', r'<em>\1</em>', html)

    # Convert markdown lists to HTML
    lines = html.split('\n')
    in_ul = False
    in_ol = False
    result = []

    for line in lines:
        stripped = line.lstrip()
        indent = len(line) - len(stripped)

        # Unordered list
        if stripped.startswith('- ') or stripped.startswith('* '):
            if not in_ul:
                result.append('<ul>')
                in_ul = True
            content = stripped[2:]
            result.append(f'<li>{content}</li>')
        # Ordered list
        elif re.match(r'^\d+\.\s', stripped):
            if not in_ol:
                result.append('<ol>')
                in_ol = True
            content = re.sub(r'^\d+\.\s', '', stripped)
            result.append(f'<li>{content}</li>')
        else:
            if in_ul:
                result.append('</ul>')
                in_ul = False
            if in_ol:
                result.append('</ol>')
                in_ol = False
            result.append(line)

    if in_ul:
        result.append('</ul>')
    if in_ol:
        result.append('</ol>')

    html = '\n'.join(result)

    # Paragraphs (simple approach)
    paragraphs = html.split('\n\n')
    html = ''
    for p in paragraphs:
        p = p.strip()
        if p and not p.startswith('<'):
            html += f'<p>{p}</p>\n\n'
        else:
            html += p + '\n\n'

    return html

def split_into_modules(content):
    """Split content into modules"""
    modules = []
    current_module = None
    current_content = []

    lines = content.split('\n')

    for line in lines:
        # Check for module header
        if line.startswith('# Modulo '):
            if current_module:
                modules.append({
                    'title': current_module,
                    'content': '\n'.join(current_content)
                })
            current_module = line.replace('# ', '')
            current_content = []
        else:
            current_content.append(line)

    # Add last module
    if current_module:
        modules.append({
            'title': current_module,
            'content': '\n'.join(current_content)
        })

    return modules

def create_html_files():
    """Create HTML files for each module"""

    # Read the edited content
    content_file = 'course-content-edited.md'
    if not os.path.exists(content_file):
        print(f"Error: {content_file} not found")
        return

    with open(content_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split into modules
    modules = split_into_modules(content)

    # Create output directory
    output_dir = 'html_pages'
    os.makedirs(output_dir, exist_ok=True)

    print(f"Creating HTML files in {output_dir}/")

    # Create HTML for each module
    for i, module in enumerate(modules, 1):
        title = module['title']
        html_content = markdown_to_html(module['content'])

        # Create full HTML page
        html_page = f"""<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            line-height: 1.6;
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
            color: #333;
        }}
        h1 {{
            color: #1f77b4;
            border-bottom: 3px solid #1f77b4;
            padding-bottom: 10px;
        }}
        h2 {{
            color: #2ca02c;
            margin-top: 30px;
        }}
        h3 {{
            color: #ff7f0e;
        }}
        h4 {{
            color: #d62728;
        }}
        ul, ol {{
            margin: 10px 0;
            padding-left: 30px;
        }}
        li {{
            margin: 5px 0;
        }}
        strong {{
            color: #000;
        }}
        p {{
            margin: 15px 0;
        }}
        .activity {{
            background: #f0f8ff;
            border-left: 4px solid #1f77b4;
            padding: 15px;
            margin: 20px 0;
        }}
        .summary {{
            background: #fff9e6;
            border: 2px solid #ffc107;
            padding: 15px;
            margin: 20px 0;
            border-radius: 5px;
        }}
    </style>
</head>
<body>
{html_content}
</body>
</html>
"""

        # Save HTML file
        filename = f"modulo_{i:02d}_{title.replace(' ', '_').replace(':', '').replace('/', '-')}.html"
        filepath = os.path.join(output_dir, filename)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html_page)

        print(f"  ✓ Created: {filename}")

    # Create index file
    index_html = """<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <title>Indice Corso AI</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
        }
        h1 {
            color: #1f77b4;
            text-align: center;
        }
        ul {
            list-style: none;
            padding: 0;
        }
        li {
            margin: 15px 0;
        }
        a {
            color: #1f77b4;
            text-decoration: none;
            font-size: 18px;
            display: block;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 5px;
            transition: background 0.3s;
        }
        a:hover {
            background: #f0f8ff;
        }
    </style>
</head>
<body>
    <h1>Introduzione all'Intelligenza Artificiale per Principianti</h1>
    <p><strong>Indice dei Moduli</strong></p>
    <ul>
"""

    for i, module in enumerate(modules, 1):
        title = module['title']
        filename = f"modulo_{i:02d}_{title.replace(' ', '_').replace(':', '').replace('/', '-')}.html"
        index_html += f'        <li><a href="{filename}">{title}</a></li>\n'

    index_html += """    </ul>
</body>
</html>
"""

    with open(os.path.join(output_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(index_html)

    print(f"\n✓ Created {len(modules)} HTML files")
    print(f"✓ Created index.html")
    print(f"\nFiles are in: {output_dir}/")
    print("\nYou can now:")
    print("1. Open each HTML file in a browser")
    print("2. Copy the content (Ctrl+A, Ctrl+C)")
    print("3. Paste directly into Moodle Page activities")

if __name__ == '__main__':
    create_html_files()
