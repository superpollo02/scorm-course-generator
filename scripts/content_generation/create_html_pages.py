#!/usr/bin/env python3
"""
Create individual HTML files for each module section
Ready to copy-paste into Moodle pages
"""

import os

def markdown_to_html(md_text):
    """Delega la conversión al motor canónico optimizado de scorm_modern."""
    from scorm_modern.renderer import markdown_to_html as _m2h
    return _m2h(md_text)


def convert_table(table_rows):
    """Delega la conversión de tablas al motor canónico optimizado de scorm_modern."""
    from scorm_modern.renderer import _convert_table
    return _convert_table(table_rows)


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
