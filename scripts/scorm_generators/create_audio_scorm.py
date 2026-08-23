#!/usr/bin/env python3
"""
Create SCORM 1.2 package with audio player
Supports MP3, WAV, OGG formats
"""

import os
import zipfile
import sys
from pathlib import Path

def create_audio_player_html(audio_filename, title, description=""):
    """Create HTML page with audio player"""

    # Detect audio type
    ext = audio_filename.lower().split('.')[-1]
    audio_type = {
        'mp3': 'audio/mpeg',
        'wav': 'audio/wav',
        'ogg': 'audio/ogg',
        'm4a': 'audio/mp4',
        'aac': 'audio/aac'
    }.get(ext, 'audio/mpeg')

    html = f'''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <script type="text/javascript">
        var API = null;

        function findAPI(win) {{
            var attempts = 0;
            while (win.API == null && win.parent != null && win.parent != win) {{
                attempts++;
                if (attempts > 7) {{
                    return null;
                }}
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

        // Track audio completion
        var audioCompleted = false;

        function onAudioEnded() {{
            audioCompleted = true;
            if (API != null) {{
                API.LMSSetValue("cmi.core.lesson_status", "completed");
                API.LMSSetValue("cmi.core.score.raw", "100");
            }}
            document.getElementById('completion-message').style.display = 'block';
        }}

        function onAudioPlay() {{
            if (API != null && API.LMSGetValue("cmi.core.lesson_status") === "not attempted") {{
                API.LMSSetValue("cmi.core.lesson_status", "incomplete");
            }}
        }}

        window.onload = function() {{
            initSCORM();
            var audio = document.getElementById('audioPlayer');
            audio.addEventListener('ended', onAudioEnded);
            audio.addEventListener('play', onAudioPlay);
        }};

        window.onbeforeunload = finishSCORM;
    </script>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }}

        .container {{
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            padding: 40px;
            max-width: 600px;
            width: 100%;
            text-align: center;
        }}

        h1 {{
            color: #333;
            margin-bottom: 10px;
            font-size: 28px;
        }}

        .description {{
            color: #666;
            margin-bottom: 30px;
            line-height: 1.6;
        }}

        .audio-icon {{
            font-size: 80px;
            margin: 20px 0;
            color: #667eea;
        }}

        .player-wrapper {{
            background: #f8f9fa;
            border-radius: 15px;
            padding: 30px;
            margin: 20px 0;
        }}

        audio {{
            width: 100%;
            outline: none;
            border-radius: 10px;
        }}

        audio::-webkit-media-controls-panel {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }}

        .controls {{
            margin-top: 20px;
        }}

        .info {{
            background: #e3f2fd;
            border-left: 4px solid #2196f3;
            padding: 15px;
            margin: 20px 0;
            text-align: left;
            border-radius: 5px;
        }}

        .info strong {{
            color: #1976d2;
        }}

        #completion-message {{
            display: none;
            background: #c8e6c9;
            border-left: 4px solid #4caf50;
            padding: 15px;
            margin: 20px 0;
            border-radius: 5px;
            color: #2e7d32;
            font-weight: bold;
        }}

        .footer {{
            margin-top: 30px;
            color: #999;
            font-size: 14px;
        }}

        @media (max-width: 600px) {{
            .container {{
                padding: 20px;
            }}

            h1 {{
                font-size: 22px;
            }}

            .audio-icon {{
                font-size: 60px;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="audio-icon">🎵</div>
        <h1>{title}</h1>
        {f'<p class="description">{description}</p>' if description else ''}

        <div class="player-wrapper">
            <audio id="audioPlayer" controls preload="metadata">
                <source src="{audio_filename}" type="{audio_type}">
                Tu navegador no soporta el elemento de audio.
            </audio>
        </div>

        <div class="info">
            <strong>ℹ️ Instrucciones:</strong><br>
            Haz clic en el botón de reproducción para escuchar el audio. Tu progreso se registrará automáticamente.
        </div>

        <div id="completion-message">
            ✅ ¡Audio completado! Tu progreso ha sido registrado.
        </div>

        <div class="footer">
            Paquete SCORM 1.2 - Compatible con Moodle
        </div>
    </div>
</body>
</html>
'''
    return html

def create_audio_scorm_manifest(title, audio_filename):
    """Create imsmanifest.xml for audio SCORM"""

    manifest = f'''<?xml version="1.0" encoding="UTF-8"?>
<manifest identifier="com.audio.scorm" version="1.0"
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
  <organizations default="org_audio">
    <organization identifier="org_audio">
      <title>{title}</title>
      <item identifier="item_audio" identifierref="resource_audio">
        <title>{title}</title>
      </item>
    </organization>
  </organizations>
  <resources>
    <resource identifier="resource_audio" type="webcontent" adlcp:scormtype="sco" href="index.html">
      <file href="index.html"/>
      <file href="{audio_filename}"/>
    </resource>
  </resources>
</manifest>
'''
    return manifest

def create_audio_scorm(audio_file, title=None, description="", output_name=None):
    """Create SCORM package with audio file"""

    # Validate audio file exists
    if not os.path.exists(audio_file):
        print(f"Errore: File audio '{audio_file}' non trovato!")
        return False

    # Get audio filename
    audio_filename = os.path.basename(audio_file)

    # Auto-generate title if not provided
    if title is None:
        title = Path(audio_file).stem.replace('_', ' ').replace('-', ' ').title()

    # Auto-generate output name
    if output_name is None:
        output_name = f"{Path(audio_file).stem}-SCORM.zip"

    print(f"Creazione pacchetto SCORM per: {audio_filename}")
    print(f"Titolo: {title}")

    # Create temp directory
    scorm_dir = 'audio_scorm_temp'
    os.makedirs(scorm_dir, exist_ok=True)

    try:
        # Create HTML player
        html_content = create_audio_player_html(audio_filename, title, description)
        with open(os.path.join(scorm_dir, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(html_content)
        print("  [OK] Creato player HTML")

        # Copy audio file
        import shutil
        shutil.copy(audio_file, os.path.join(scorm_dir, audio_filename))
        print(f"  [OK] Copiato file audio: {audio_filename}")

        # Create manifest
        manifest = create_audio_scorm_manifest(title, audio_filename)
        with open(os.path.join(scorm_dir, 'imsmanifest.xml'), 'w', encoding='utf-8') as f:
            f.write(manifest)
        print("  [OK] Creato imsmanifest.xml")

        # Create ZIP package
        with zipfile.ZipFile(output_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(scorm_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, scorm_dir)
                    zipf.write(file_path, arcname)
        # Cleanup temp directory
        shutil.rmtree(scorm_dir)

        file_size = os.path.getsize(output_name) / 1024
        print(f"\n[OK] Pacchetto SCORM creato: {output_name}")
        print(f"[INFO] Dimensione: {file_size:.1f} KB")
        print(f"\n[INFO] Come importare in Moodle:")
        print("1. Vai al tuo corso")
        print("2. Clicca 'Aggiungi un'attivita o una risorsa'")
        print("3. Seleziona 'Pacchetto SCORM'")
        print(f"4. Carica il file: {output_name}")
        print("5. Salva - Fatto!")

        return True

    except Exception as e:
        print(f"\n[ERROR] Errore: {e}")
        # Cleanup on error
        if os.path.exists(scorm_dir):
            import shutil
            shutil.rmtree(scorm_dir)
        return False

def main():
    """Main function"""
    print("=" * 60)
    print("  Creatore Pacchetto SCORM Audio per Moodle")
    print("=" * 60)
    print()

    if len(sys.argv) < 2:
        print("Uso: python create_audio_scorm.py <file_audio> [titolo] [descrizione]")
        print()
        print("Esempi:")
        print("  python create_audio_scorm.py lezione.mp3")
        print("  python create_audio_scorm.py lezione.mp3 \"Lezione 1\"")
        print("  python create_audio_scorm.py lezione.mp3 \"Lezione 1\" \"Introduzione al corso\"")
        print()
        print("Formati supportati: MP3, WAV, OGG, M4A, AAC")
        return

    audio_file = sys.argv[1]
    title = sys.argv[2] if len(sys.argv) > 2 else None
    description = sys.argv[3] if len(sys.argv) > 3 else ""

    create_audio_scorm(audio_file, title, description)

if __name__ == '__main__':
    main()
