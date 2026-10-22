from scorm_modern.parser import parsear_markdown
from scorm_modern.renderer import embed_video, markdown_to_html, render_evaluacion, render_leccion


def test_embed_video_youtube():
    html = embed_video("https://www.youtube.com/watch?v=abc123")
    assert "youtube-nocookie.com/embed/abc123" in html


def test_embed_video_youtube_corto():
    html = embed_video("https://youtu.be/abc123")
    assert "youtube-nocookie.com/embed/abc123" in html


def test_embed_video_drive():
    html = embed_video("https://drive.google.com/file/d/XYZ987/view")
    assert "drive.google.com/file/d/XYZ987/preview" in html


def test_embed_video_vimeo():
    html = embed_video("https://vimeo.com/12345")
    assert "player.vimeo.com/video/12345" in html


def test_embed_video_mp4_local():
    html = embed_video("media/video_clase.mp4")
    assert "video-local-wrapper" in html
    assert "media/video_clase.mp4" in html


def test_embed_video_desconocido_usa_fallback():
    html = embed_video("https://dailymotion.com/video/x7xyz")
    assert "video-fallback" in html
    assert "https://dailymotion.com/video/x7xyz" in html


def test_markdown_to_html_tabla_y_lista():
    md = "# Título\n\n- item 1\n- item 2\n\n| A | B |\n|---|---|\n| 1 | 2 |\n"
    html = markdown_to_html(md)
    assert "<h1>Título</h1>" in html
    assert "<ul>" in html and "<li>item 1</li>" in html
    assert '<table class="data-table">' in html


def test_render_leccion_incluye_apoyo_y_video():
    md = (
        "# Lección: Test\n\nContenido.\n\n"
        ":::apoyo\nTip.\n\nVIDEO: https://www.youtube.com/watch?v=zzz\n:::\n"
    )
    curso = parsear_markdown(md + "\n# Actividad: A\ncontenido\n")
    html = render_leccion(curso.leccion)
    assert "apoyo-box" in html
    assert "youtube-nocookie.com/embed/zzz" in html


def test_render_evaluacion_incluye_preguntas_y_js():
    md = (
        "# Lección: L\ncontenido\n"
        "# Evaluación: Quiz\n\n## Pregunta 1\n**P?**\n\nA) x\nB) y\n\n"
        "**Respuesta correcta: A**\n\n# Actividad: A\ncontenido\n"
    )
    curso = parsear_markdown(md)
    html = render_evaluacion(curso.evaluacion, puntaje_minimo=80)
    assert "quiz-pregunta" in html
    assert "PUNTAJE_MINIMO = 80" in html
    assert 'name="p1"' in html
