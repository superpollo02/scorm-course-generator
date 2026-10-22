from scorm_modern.renderer import markdown_to_html
from scorm_modern.manifest import generar_manifest, ItemManifest

def test_xss_script_sanitization():
    # Intento de inyectar <script>
    payload = "<script>alert('pwned')</script>"
    html = markdown_to_html(payload)
    assert "<script>" not in html
    assert "&lt;script&gt;" in html


def test_xss_onerror_event_sanitization():
    # Intento de inyectar manejador de evento onerror
    payload = "<img src=x onerror=alert(1)>"
    html = markdown_to_html(payload)
    # Debe escapar las etiquetas para que no se ejecuten en el navegador
    assert "<img" not in html
    assert "&lt;img" in html


def test_xml_injection_sanitization():
    # Intento de inyectar comillas y nodos adicionales en identificador
    malicious_item = ItemManifest(
        identificador='my_item" inject="true',
        titulo='Test Item <script>',
        archivo='item.html" evil="yes'
    )
    manifest_xml = generar_manifest(
        identificador_curso='curso" malicioso="yes',
        titulo_curso='Curso Seguro',
        items=[malicious_item]
    )
    # Debe haber sanitizado comillas y espacios en identificadores alfanuméricos
    assert 'identifier="com.scorm_modern.curso__malicioso__yes"' in manifest_xml
    assert 'resource_my_item__inject__true' in manifest_xml
    # El título debe estar escapado
    assert "&lt;script&gt;" in manifest_xml
