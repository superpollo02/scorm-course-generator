import os
import subprocess
from pathlib import Path

IMG_DIR = Path(r"c:\Users\mfischer\Documents\antigravitiy proyectos\aula nueva con moodle\cursos\gestion_personas_talento\img")
IMG_DIR.mkdir(parents=True, exist_ok=True)

banners = [
    {
        "filename": "banner_general_curso",
        "tag": "CAMPUS VIRTUAL ESALUD • MINISTERIO DE SALUD Y DEPORTES DE MENDOZA",
        "title": "Gestión de Personas y Talento Humano en Salud",
        "subtitle": "Cultura Organizacional, Comunicación Asertiva, Trabajo en Equipo y Liderazgo Situacional",
        "badge": "Curso 3 • 30 Horas Reloj • Circular N° 5",
        "accent": "#008080",
        "bg1": "#0a192f",
        "bg2": "#112240"
    },
    {
        "filename": "banner_unidad_1",
        "tag": "UNIDAD 1 • DOCENTE: DRA. SUSANA SALOMÓN",
        "title": "Cultura Organizacional y Desafíos de la Gestión",
        "subtitle": "Gestión vs. Administración • El SER, el HACER y el ESTAR • Tipologías Culturales y Clima Laboral",
        "badge": "Modelo Pedagógico Tripartito • Semanas 1 y 2",
        "accent": "#0ea5e9",
        "bg1": "#0f172a",
        "bg2": "#1e3a8a"
    },
    {
        "filename": "banner_unidad_2",
        "tag": "UNIDAD 2 • DOCENTE: LIC. CARLA NANI",
        "title": "Comunicación, Trabajo en Equipo y Liderazgo",
        "subtitle": "Factor Humano (2+2≠4) • Esquema Emisor-Perceptor • Paradigma del Quirófano • Liderazgo Situacional",
        "badge": "Modelo Pedagógico Tripartito • Semanas 3 y 4",
        "accent": "#10b981",
        "bg1": "#064e3b",
        "bg2": "#0f172a"
    },
    {
        "filename": "banner_cierre_evaluacion",
        "tag": "CIERRE Y ACREDITACIÓN • CIRCULAR N° 5",
        "title": "Evaluación Final Integradora y Certificación",
        "subtitle": "Sistema de Doble Candado Automatizado: Examen Integrador (≥70%) + Encuesta de Calidad Educativa",
        "badge": "Certificado Oficial • 30 Horas Reloj",
        "accent": "#f59e0b",
        "bg1": "#1e1b4b",
        "bg2": "#31102f"
    }
]

svg_template = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 320" width="1200" height="320">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{bg1}"/>
      <stop offset="100%" stop-color="{bg2}"/>
    </linearGradient>
    <linearGradient id="accentGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{accent}"/>
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0.2"/>
    </linearGradient>
  </defs>
  <rect width="1200" height="320" fill="url(#bg)" rx="16"/>
  
  <!-- Decorative geometric grid & circles -->
  <circle cx="1080" cy="80" r="180" fill="{accent}" opacity="0.12"/>
  <circle cx="1120" cy="260" r="140" fill="{accent}" opacity="0.08"/>
  <rect x="0" y="0" width="14" height="320" fill="{accent}" rx="4"/>
  
  <!-- Top Tag -->
  <rect x="50" y="38" width="580" height="30" rx="6" fill="{accent}" opacity="0.22"/>
  <text x="64" y="58" font-family="Segoe UI, Roboto, Arial, sans-serif" font-size="13" font-weight="700" fill="#e2e8f0" letter-spacing="1.2">{tag}</text>
  
  <!-- Main Title -->
  <text x="50" y="130" font-family="Segoe UI, Roboto, Arial, sans-serif" font-size="40" font-weight="800" fill="#ffffff">{title}</text>
  
  <!-- Divider line -->
  <rect x="50" y="152" width="420" height="4" fill="url(#accentGrad)" rx="2"/>
  
  <!-- Subtitle -->
  <text x="50" y="195" font-family="Segoe UI, Roboto, Arial, sans-serif" font-size="20" font-weight="400" fill="#cbd5e1">{subtitle}</text>
  
  <!-- Bottom Badge -->
  <rect x="50" y="235" width="380" height="42" rx="8" fill="#ffffff" opacity="0.1"/>
  <circle cx="75" cy="256" r="7" fill="{accent}"/>
  <text x="95" y="262" font-family="Segoe UI, Roboto, Arial, sans-serif" font-size="16" font-weight="600" fill="#f8fafc">{badge}</text>
</svg>
"""

for b in banners:
    svg_path = IMG_DIR / f"{b['filename']}.svg"
    svg_content = svg_template.format(**b)
    svg_path.write_text(svg_content, encoding="utf-8")
    print(f"Created SVG: {svg_path}")

# Now render SVG to PNG using Edge or Chrome headless via HTML wrapper
browser_paths = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"
]
browser = next((p for p in browser_paths if os.path.exists(p)), None)

if browser:
    for b in banners:
        svg_path = IMG_DIR / f"{b['filename']}.svg"
        png_path = IMG_DIR / f"{b['filename']}.png"
        html_wrapper = IMG_DIR / f"temp_{b['filename']}.html"
        svg_text = svg_path.read_text(encoding="utf-8")
        html_wrapper.write_text(f"""<!DOCTYPE html>
<html><head><style>* {{ margin:0; padding:0; box-sizing:border-box; }} body {{ width:1200px; height:320px; overflow:hidden; background:transparent; }}</style></head>
<body>{svg_text}</body></html>""", encoding="utf-8")
        cmd = [
            browser,
            "--headless",
            "--disable-gpu",
            f"--screenshot={png_path}",
            "--window-size=1200,320",
            "--hide-scrollbars",
            str(html_wrapper.resolve().as_uri())
        ]
        subprocess.run(cmd, check=True)
        html_wrapper.unlink(missing_ok=True)
        print(f"Rendered PNG: {png_path} ({png_path.stat().st_size} bytes)")
else:
    print("No browser found for headless PNG rendering")
