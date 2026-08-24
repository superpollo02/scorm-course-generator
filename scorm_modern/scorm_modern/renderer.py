"""
renderer.py
===========
Convierte los objetos parseados (Leccion, Evaluacion, Actividad) en páginas
HTML compatibles con SCORM 1.2, con:

  - Markdown -> HTML (encabezados, listas, tablas, negrita/cursiva)
  - Bloques de apoyo (`{{APOYO_n}}`) renderizados como cajas destacadas,
    con embebido de video de YouTube/Google Drive cuando corresponde
  - Un quiz interactivo para la Evaluación, con seguimiento SCORM
    (cmi.core.lesson_status / cmi.core.score.raw) según `puntaje_minimo`
  - Navegación Anterior / Índice / Siguiente entre páginas
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass

from .parser import Actividad, BloqueApoyo, Evaluacion, Leccion

__all__ = [
    "embed_video",
    "markdown_to_html",
    "render_apoyo",
    "render_leccion",
    "render_evaluacion",
    "render_actividad",
    "render_indice",
    "PaginaNav",
]

# ----------------------------------------------------------------------
# Utilidades de markdown -> HTML (compartidas con los generadores previos
# del proyecto, extendidas para reconocer marcadores {{APOYO_n}}).
# ----------------------------------------------------------------------

_RE_APOYO_MARCADOR = re.compile(r"\{\{APOYO_(\d+)\}\}")


def _youtube_id(url: str) -> str | None:
    patrones = [
        r"youtube\.com/watch\?v=([\w-]+)",
        r"youtu\.be/([\w-]+)",
        r"youtube\.com/embed/([\w-]+)",
        r"youtube\.com/shorts/([\w-]+)",
    ]
    for patron in patrones:
        m = re.search(patron, url)
        if m:
            return m.group(1)
    return None


def _drive_id(url: str) -> str | None:
    patrones = [
        r"drive\.google\.com/file/d/([\w-]+)",
        r"drive\.google\.com/open\?id=([\w-]+)",
        r"[?&]id=([\w-]+)",
    ]
    for patron in patrones:
        m = re.search(patron, url)
        if m:
            return m.group(1)
    return None


def embed_video(url: str) -> str:
    """Devuelve el HTML de embebido para un video de YouTube o Google Drive.

    Si la URL no coincide con ninguno de los dos proveedores soportados,
    se devuelve un enlace simple como alternativa segura.
    """
    url = url.strip()

    yid = _youtube_id(url)
    if yid:
        return (
            '<div class="video-embed">'
            f'<iframe src="https://www.youtube-nocookie.com/embed/{yid}" '
            'title="Video incrustado" frameborder="0" allowfullscreen '
            'allow="accelerometer; autoplay; clipboard-write; encrypted-media; '
            'gyroscope; picture-in-picture"></iframe>'
            "</div>"
        )

    did = _drive_id(url)
    if did:
        return (
            '<div class="video-embed">'
            f'<iframe src="https://drive.google.com/file/d/{did}/preview" '
            'title="Video incrustado" frameborder="0" allow="autoplay"></iframe>'
            "</div>"
        )

    return f'<p class="video-fallback"><a href="{url}" target="_blank" rel="noopener">Ver video ↗</a></p>'


def markdown_to_html(md_text: str, apoyos: list[BloqueApoyo] | None = None) -> str:
    """Convierte markdown básico (encabezados, listas, tablas, negrita/cursiva,
    bloques de código) a HTML, reemplazando los marcadores {{APOYO_n}} por su
    caja de apoyo renderizada."""
    apoyos = apoyos or []
    html = md_text

    html = re.sub(r"^#### (.*?)$", r"<h4>\1</h4>", html, flags=re.MULTILINE)
    html = re.sub(r"^### (.*?)$", r"<h3>\1</h3>", html, flags=re.MULTILINE)
    html = re.sub(r"^## (.*?)$", r"<h2>\1</h2>", html, flags=re.MULTILINE)
    html = re.sub(r"^# (.*?)$", r"<h1>\1</h1>", html, flags=re.MULTILINE)

    html = re.sub(r"\*\*\*(.*?)\*\*\*", r"<strong><em>\1</em></strong>", html)
    html = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", html)
    html = re.sub(r"(?<!\*)\*([^*\n]+?)\*(?!\*)", r"<em>\1</em>", html)
    html = re.sub(r"^---$", r"<hr>", html, flags=re.MULTILINE)

    lines = html.split("\n")
    result: list[str] = []
    in_ul = in_ol = in_table = in_code = False
    table_rows: list[str] = []

    def cerrar_listas() -> None:
        nonlocal in_ul, in_ol
        if in_ul:
            result.append("</ul>")
            in_ul = False
        if in_ol:
            result.append("</ol>")
            in_ol = False

    for line in lines:
        stripped = line.strip()

        if stripped.startswith("```"):
            in_code = not in_code
            result.append("<pre><code>" if in_code else "</code></pre>")
            continue
        if in_code:
            result.append(line)
            continue

        marcador = _RE_APOYO_MARCADOR.match(stripped)
        if marcador:
            cerrar_listas()
            idx = int(marcador.group(1))
            if idx < len(apoyos):
                result.append(render_apoyo(apoyos[idx]))
            continue

        if "|" in stripped and not stripped.startswith("<"):
            if not in_table:
                in_table = True
                table_rows = []
            table_rows.append(stripped)
            continue
        elif in_table:
            result.append(_convert_table(table_rows))
            in_table = False
            table_rows = []

        if stripped.startswith("- ") or stripped.startswith("* "):
            if not in_ul:
                result.append("<ul>")
                in_ul = True
            result.append(f"  <li>{stripped[2:]}</li>")
        elif re.match(r"^\d+\.\s", stripped):
            if not in_ol:
                result.append("<ol>")
                in_ol = True
            result.append(f"  <li>{re.sub(r'^\\d+\\.\\s', '', stripped)}</li>")
        else:
            cerrar_listas()
            if stripped.startswith("<"):
                result.append(line)
            elif stripped:
                result.append(f"<p>{line}</p>")

    if in_table:
        result.append(_convert_table(table_rows))
    cerrar_listas()

    return "\n".join(result)


def _convert_table(table_rows: list[str]) -> str:
    if len(table_rows) < 2:
        return "\n".join(table_rows)

    html = '<table class="data-table">\n'
    for i, row in enumerate(table_rows):
        if i == 1 and re.match(r"^\|[\s\-:|]+\|$", row):
            continue
        cells = [c.strip() for c in row.split("|") if c.strip()]
        if not cells:
            continue
        if i == 0:
            html += "<thead>\n<tr>\n"
            html += "".join(f"  <th>{c}</th>\n" for c in cells)
            html += "</tr>\n</thead>\n<tbody>\n"
        else:
            html += "<tr>\n" + "".join(f"  <td>{c}</td>\n" for c in cells) + "</tr>\n"
    html += "</tbody>\n</table>"
    return html


def render_apoyo(apoyo: BloqueApoyo) -> str:
    contenido_html = markdown_to_html(apoyo.contenido_md) if apoyo.contenido_md else ""
    video_html = embed_video(apoyo.video_url) if apoyo.video_url else ""
    return (
        '<div class="apoyo-box">'
        '<div class="apoyo-icono">💡</div>'
        f'<div class="apoyo-contenido">{contenido_html}{video_html}</div>'
        "</div>"
    )


# ----------------------------------------------------------------------
# Plantilla base de página (compartida por lección / evaluación / actividad)
# ----------------------------------------------------------------------

_ESTILOS = """
body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6;
       max-width: 900px; margin: 0 auto; padding: 20px; color: #2b2b2b; background: #f5f5f5; }
.container { background: #fff; padding: 30px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,.1); }
h1 { color: #1f77b4; border-bottom: 3px solid #1f77b4; padding-bottom: 10px; margin-top: 0; }
h2 { color: #2ca02c; margin-top: 30px; border-left: 4px solid #2ca02c; padding-left: 15px; }
h3 { color: #ff7f0e; margin-top: 25px; }
ul, ol { margin: 15px 0; padding-left: 30px; }
li { margin: 8px 0; }
p { margin: 15px 0; text-align: justify; }
.badge { display:inline-block; font-size: 12px; font-weight:700; text-transform:uppercase;
         letter-spacing:.05em; padding:4px 10px; border-radius:999px; margin-bottom:10px; }
.badge-leccion { background:#e3f2fd; color:#1f77b4; }
.badge-evaluacion { background:#fdecea; color:#d62728; }
.badge-actividad { background:#e8f5e9; color:#2ca02c; }
.navigation { position: sticky; top: 0; background: #1f77b4; padding: 15px; margin: -30px -30px 30px -30px;
              border-radius: 8px 8px 0 0; display: flex; justify-content: space-between; gap: 10px; z-index: 100; }
.navigation button { background: #fff; color: #1f77b4; border: none; padding: 10px 20px; border-radius: 5px;
                      cursor: pointer; font-size: 14px; font-weight: bold; transition: all .2s; }
.navigation button:hover { background: #f0f8ff; transform: translateY(-2px); }
.index-list { list-style: none; padding: 0; }
.index-list li { margin: 12px 0; }
.index-list a { display: block; padding: 15px; background: #f0f8ff; color: #1f77b4; text-decoration: none;
                border-radius: 5px; border-left: 4px solid #1f77b4; transition: all .2s; }
.index-list a:hover { background: #1f77b4; color: #fff; transform: translateX(8px); }
.course-header { text-align: center; margin-bottom: 40px; padding: 20px; color: #fff; border-radius: 8px;
                 background: linear-gradient(135deg, #1f77b4, #2ca02c); }
.course-header h1 { color: #fff; border: none; margin: 0; }
.data-table { width: 100%; border-collapse: collapse; margin: 20px 0; background: #fff;
              box-shadow: 0 2px 8px rgba(0,0,0,.08); }
.data-table thead { background: linear-gradient(135deg, #1f77b4, #2ca02c); color: #fff; }
.data-table th, .data-table td { padding: 10px 15px; border: 1px solid #ddd; text-align: left; }
.data-table tbody tr:nth-child(even) { background: #f8f9fa; }
.apoyo-box { display:flex; gap:14px; background:#fff8e1; border-left:4px solid #ff7f0e; border-radius:6px;
             padding:16px 18px; margin:20px 0; }
.apoyo-icono { font-size: 22px; line-height:1; }
.apoyo-contenido p:first-child { margin-top: 0; }
.video-embed { position: relative; width: 100%; padding-top: 56.25%; margin: 14px 0; border-radius: 6px;
               overflow: hidden; background:#000; }
.video-embed iframe { position: absolute; inset: 0; width: 100%; height: 100%; border: 0; }
.video-fallback a { color:#1f77b4; font-weight:600; }
.quiz-pregunta { margin: 26px 0; padding: 18px; border: 1px solid #e0e0e0; border-radius: 8px; }
.quiz-opcion { display:block; margin:8px 0; padding:10px 14px; border:1px solid #ddd; border-radius:6px;
               cursor:pointer; transition: all .15s; }
.quiz-opcion:hover { background:#f0f8ff; }
.quiz-opcion input { margin-right: 10px; }
.quiz-opcion.correcta { background:#e8f5e9; border-color:#2ca02c; }
.quiz-opcion.incorrecta { background:#fdecea; border-color:#d62728; }
.quiz-explicacion { margin-top: 10px; padding: 10px 14px; background:#f5f5f5; border-radius:6px;
                     font-size: 14px; display:none; }
#quiz-resultado { margin-top: 24px; padding: 20px; border-radius: 8px; text-align:center; font-size: 18px;
                   font-weight: 700; display:none; }
#quiz-resultado.aprobado { background:#e8f5e9; color:#1b5e20; }
#quiz-resultado.reprobado { background:#fdecea; color:#8e0000; }
#quiz-enviar { display:block; margin: 20px auto 0; background:#1f77b4; color:#fff; border:none;
               padding: 12px 28px; font-size:16px; font-weight:700; border-radius:6px; cursor:pointer; }
#quiz-enviar:hover { background:#155d8b; }
"""

_SCORM_JS = """
var API = null;
function findAPI(win) {
    while (win.API == null && win.parent != null && win.parent != win) { win = win.parent; }
    return win.API;
}
function initSCORM() {
    API = findAPI(window);
    if (API != null) {
        API.LMSInitialize("");
        API.LMSSetValue("cmi.core.lesson_status", "incomplete");
    }
}
function finishSCORM(status, score) {
    if (API != null) {
        API.LMSSetValue("cmi.core.lesson_status", status || "completed");
        if (typeof score !== "undefined") { API.LMSSetValue("cmi.core.score.raw", String(score)); }
        API.LMSCommit("");
        API.LMSFinish("");
    }
}
window.onload = initSCORM;
"""


@dataclass
class PaginaNav:
    """Datos de navegación entre páginas del paquete SCORM."""

    anterior: str | None = None
    siguiente: str | None = None


def _nav_html(nav: PaginaNav) -> str:
    botones = '<div class="navigation">'
    if nav.anterior:
        botones += f'<button onclick="window.location.href=\'{nav.anterior}\'">&larr; Anterior</button>'
    botones += '<button onclick="window.location.href=\'index.html\'">&#8962; Índice</button>'
    if nav.siguiente:
        botones += f'<button onclick="window.location.href=\'{nav.siguiente}\'">Siguiente &rarr;</button>'
    botones += "</div>"
    return botones


def _pagina_html(titulo: str, badge: str, badge_clase: str, cuerpo: str,
                  nav: PaginaNav | None, extra_js: str = "", es_indice: bool = False) -> str:
    nav_html = "" if es_indice else _nav_html(nav or PaginaNav())
    script_scorm = "" if es_indice else f"<script>{_SCORM_JS}\n{extra_js}</script>"
    badge_html = "" if es_indice else f'<span class="badge {badge_clase}">{badge}</span>'

    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{titulo}</title>
{script_scorm}
<style>{_ESTILOS}</style>
</head>
<body>
<div class="container">
{nav_html}
{badge_html}
{cuerpo}
</div>
</body>
</html>
"""


def render_leccion(leccion: Leccion, nav: PaginaNav | None = None) -> str:
    cuerpo = f"<h1>{leccion.titulo}</h1>" + markdown_to_html(leccion.contenido_md, leccion.apoyos)
    extra_js = 'window.onbeforeunload = function () { finishSCORM("completed", 100); };'
    return _pagina_html(leccion.titulo, "Lección", "badge-leccion", cuerpo, nav, extra_js)


def render_actividad(actividad: Actividad, nav: PaginaNav | None = None) -> str:
    cuerpo = f"<h1>{actividad.titulo}</h1>" + markdown_to_html(actividad.contenido_md, actividad.apoyos)
    extra_js = 'window.onbeforeunload = function () { finishSCORM("completed", 100); };'
    return _pagina_html(actividad.titulo, "Actividad", "badge-actividad", cuerpo, nav, extra_js)


def render_evaluacion(evaluacion: Evaluacion, puntaje_minimo: int = 70,
                       nav: PaginaNav | None = None) -> str:
    preguntas_html = []
    datos_js = []

    for p in evaluacion.preguntas:
        opciones_html = "".join(
            f'<label class="quiz-opcion" data-pregunta="{p.numero}" data-letra="{letra}">'
            f'<input type="radio" name="p{p.numero}" value="{letra}"> {letra}) {texto}'
            "</label>"
            for letra, texto in sorted(p.opciones.items())
        )
        explicacion_html = (
            f'<div class="quiz-explicacion" id="exp-{p.numero}">{p.explicacion}</div>'
            if p.explicacion else f'<div class="quiz-explicacion" id="exp-{p.numero}"></div>'
        )
        preguntas_html.append(
            f'<div class="quiz-pregunta" id="pregunta-{p.numero}">'
            f"<p><strong>{p.numero}. {p.texto}</strong></p>"
            f"{opciones_html}{explicacion_html}"
            "</div>"
        )
        datos_js.append({"numero": p.numero, "correcta": p.correcta})

    apoyos_html = "".join(render_apoyo(a) for a in evaluacion.apoyos)

    cuerpo = (
        f"<h1>{evaluacion.titulo}</h1>"
        f'<p>Responde todas las preguntas y presiona <strong>Enviar</strong> para ver tu resultado. '
        f"Puntaje mínimo para aprobar: <strong>{puntaje_minimo}%</strong>.</p>"
        f"{apoyos_html}"
        f'<form id="quiz-form">{"".join(preguntas_html)}</form>'
        '<button id="quiz-enviar" onclick="corregirQuiz()">Enviar respuestas</button>'
        '<div id="quiz-resultado"></div>'
    )

    extra_js = f"""
var RESPUESTAS_CORRECTAS = {json.dumps(datos_js)};
var PUNTAJE_MINIMO = {puntaje_minimo};

function corregirQuiz() {{
    var total = RESPUESTAS_CORRECTAS.length;
    var aciertos = 0;

    RESPUESTAS_CORRECTAS.forEach(function (item) {{
        var seleccionado = document.querySelector('input[name="p' + item.numero + '"]:checked');
        var letraSeleccionada = seleccionado ? seleccionado.value : null;
        var esCorrecta = letraSeleccionada === item.correcta;
        if (esCorrecta) {{ aciertos++; }}

        var opciones = document.querySelectorAll('.quiz-opcion[data-pregunta="' + item.numero + '"]');
        opciones.forEach(function (op) {{
            op.classList.remove('correcta', 'incorrecta');
            if (op.dataset.letra === item.correcta) {{ op.classList.add('correcta'); }}
            else if (op.dataset.letra === letraSeleccionada) {{ op.classList.add('incorrecta'); }}
        }});

        var exp = document.getElementById('exp-' + item.numero);
        if (exp) {{ exp.style.display = 'block'; }}
    }});

    var puntaje = Math.round((aciertos / total) * 100);
    var aprobado = puntaje >= PUNTAJE_MINIMO;

    var resultado = document.getElementById('quiz-resultado');
    resultado.style.display = 'block';
    resultado.className = aprobado ? 'aprobado' : 'reprobado';
    resultado.textContent = (aprobado ? '✓ Aprobado' : '✗ No aprobado') +
        ' — ' + aciertos + '/' + total + ' correctas (' + puntaje + '%)';

    finishSCORM(aprobado ? 'passed' : 'failed', puntaje);
}}
"""
    return _pagina_html(evaluacion.titulo, "Evaluación", "badge-evaluacion", cuerpo, nav, extra_js)


def render_indice(titulo_curso: str, items: list[tuple[str, str, str]]) -> str:
    """items: lista de (etiqueta, archivo, tipo) para el listado del índice."""
    filas = "".join(
        f'<li><a href="{archivo}">{etiqueta} <em>({tipo})</em></a></li>'
        for etiqueta, archivo, tipo in items
    )
    cuerpo = (
        f'<div class="course-header"><h1>{titulo_curso}</h1></div>'
        "<p>Selecciona una sección para comenzar:</p>"
        f'<ul class="index-list">{filas}</ul>'
    )
    return _pagina_html(f"Índice — {titulo_curso}", "", "", cuerpo, None, es_indice=True)
