from scorm_modern.parser import parsear_markdown
from scorm_modern.checkpoint_parser import parse_checkpoint_markdown
from scorm_modern.renderer import render_leccion

def test_clase_con_video_principal_y_adicional():
    md = """# Clase: Modelos Sanitarios Comparados

En esta clase analizaremos los modelos Bismarck y Beveridge.

:::apoyo
VIDEO: https://youtu.be/abc12345
VIDEO_ADICIONAL: https://vimeo.com/998877 | Cápsula de Profundización Bismarck
VIDEO_ADICIONAL: media/resumen_microlearning.mp4 | Microlearning Resumen
:::

# Actividad: Análisis
Realiza el análisis comparativo.
"""
    curso = parsear_markdown(md)
    leccion = curso.leccion
    assert len(leccion.apoyos) == 1
    apoyo = leccion.apoyos[0]
    assert apoyo.video_url == "https://youtu.be/abc12345"
    assert len(apoyo.videos_adicionales) == 2
    assert apoyo.videos_adicionales[0]["url"] == "https://vimeo.com/998877"
    assert apoyo.videos_adicionales[0]["titulo"] == "Cápsula de Profundización Bismarck"
    assert apoyo.videos_adicionales[1]["url"] == "media/resumen_microlearning.mp4"

    # Verificar renderizado en HTML
    html = render_leccion(leccion)
    assert "youtube-nocookie.com/embed/abc12345" in html
    assert "player.vimeo.com/video/998877" in html
    assert "video-local-wrapper" in html
    assert "media/resumen_microlearning.mp4" in html
    assert "Cápsula de Profundización Bismarck" in html


def test_checkpoint_con_videos_adicionales():
    cp_text = """# Curso: Sistemas Sanitarios
## ID Unidad: U1
## Clase: Fundamentos
## Video URL: https://youtu.be/video_main
## Video Adicional URL: https://vimeo.com/video_extra
## Video Adicional: media/micro.mp4 | Microlearning Corto

# Introducción
Texto de bienvenida a la clase.

# Lectura 1: Modelos
Texto de la lectura.

# Evaluación: Test
## Pregunta 1
**¿Pregunta 1?**
A) Opción A
B) Opción B
**Respuesta correcta: A**
**Explicación:** Correcto.
"""
    parsed = parse_checkpoint_markdown(cp_text)
    assert parsed["metadata"]["video_url"] == "https://youtu.be/video_main"
    assert len(parsed["metadata"]["videos_adicionales"]) == 2
    assert parsed["metadata"]["videos_adicionales"][0]["url"] == "https://vimeo.com/video_extra"
    assert parsed["metadata"]["videos_adicionales"][1]["url"] == "media/micro.mp4"
    assert parsed["metadata"]["videos_adicionales"][1]["titulo"] == "Microlearning Corto"
