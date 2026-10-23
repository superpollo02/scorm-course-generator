#!/usr/bin/env python3
"""
Create SCORM 1.2 package with video player
Supports MP4, WEBM, MOV, AVI formats
"""

import os
import zipfile
import sys
from pathlib import Path

def create_video_player_html(video_filename, title, description=""):
    """Create HTML page with video player"""

    # Detect video type
    ext = video_filename.lower().split('.')[-1]
    video_type = {
        'mp4': 'video/mp4',
        'webm': 'video/webm',
        'ogg': 'video/ogg',
        'mov': 'video/mp4',
        'avi': 'video/x-msvideo',
        'mkv': 'video/x-matroska'
    }.get(ext, 'video/mp4')

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

        // Track video completion
        var videoCompleted = false;
        var watchedPercentage = 0;

        function onVideoEnded() {{
            videoCompleted = true;
            if (API != null) {{
                API.LMSSetValue("cmi.core.lesson_status", "completed");
                API.LMSSetValue("cmi.core.score.raw", "100");
            }}
            document.getElementById('completion-message').style.display = 'block';
        }}

        function onVideoPlay() {{
            if (API != null && API.LMSGetValue("cmi.core.lesson_status") === "not attempted") {{
                API.LMSSetValue("cmi.core.lesson_status", "incomplete");
            }}
        }}

        function onVideoTimeUpdate() {{
            var video = document.getElementById('videoPlayer');
            if (video.duration > 0) {{
                watchedPercentage = Math.floor((video.currentTime / video.duration) * 100);
                document.getElementById('progress-text').textContent = watchedPercentage + '%';

                // Update progress bar
                document.getElementById('progress-fill').style.width = watchedPercentage + '%';

                // Mark as completed if watched 90% or more
                if (watchedPercentage >= 90 && !videoCompleted) {{
                    videoCompleted = true;
                    if (API != null) {{
                        API.LMSSetValue("cmi.core.lesson_status", "completed");
                        API.LMSSetValue("cmi.core.score.raw", "100");
                    }}
                    document.getElementById('completion-message').style.display = 'block';
                }}
            }}
        }}

        window.onload = function() {{
            initSCORM();
            var video = document.getElementById('videoPlayer');
            video.addEventListener('ended', onVideoEnded);
            video.addEventListener('play', onVideoPlay);
            video.addEventListener('timeupdate', onVideoTimeUpdate);
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
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            min-height: 100vh;
            padding: 20px;
        }}

        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            overflow: hidden;
        }}

        .header {{
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }}

        h1 {{
            font-size: 28px;
            margin-bottom: 10px;
        }}

        .description {{
            font-size: 16px;
            opacity: 0.9;
        }}

        .video-wrapper {{
            position: relative;
            background: #000;
        }}

        video {{
            width: 100%;
            height: auto;
            display: block;
            max-height: 70vh;
        }}

        .content {{
            padding: 30px;
        }}

        .progress-container {{
            background: #f0f0f0;
            border-radius: 10px;
            padding: 20px;
            margin: 20px 0;
        }}

        .progress-label {{
            font-weight: bold;
            color: #333;
            margin-bottom: 10px;
        }}

        .progress-bar {{
            background: #e0e0e0;
            height: 30px;
            border-radius: 15px;
            overflow: hidden;
            position: relative;
        }}

        .progress-fill {{
            background: linear-gradient(90deg, #4caf50 0%, #8bc34a 100%);
            height: 100%;
            width: 0%;
            transition: width 0.3s ease;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-weight: bold;
        }}

        .info {{
            background: #e3f2fd;
            border-left: 4px solid #2196f3;
            padding: 15px;
            margin: 20px 0;
            border-radius: 5px;
        }}

        .info strong {{
            color: #1976d2;
        }}

        #completion-message {{
            display: none;
            background: #c8e6c9;
            border-left: 4px solid #4caf50;
            padding: 20px;
            margin: 20px 0;
            border-radius: 5px;
            text-align: center;
        }}

        #completion-message h3 {{
            color: #2e7d32;
            margin-bottom: 10px;
        }}

        .video-icon {{
            font-size: 60px;
            margin: 10px 0;
        }}

        .controls-info {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            margin: 20px 0;
        }}

        .control-item {{
            background: #f8f9fa;
            padding: 15px;
            border-radius: 10px;
            text-align: center;
        }}

        .control-item-icon {{
            font-size: 30px;
            margin-bottom: 10px;
        }}

        .footer {{
            text-align: center;
            padding: 20px;
            color: #999;
            font-size: 14px;
            border-top: 1px solid #eee;
        }}

        @media (max-width: 768px) {{
            .header {{
                padding: 20px;
            }}

            h1 {{
                font-size: 22px;
            }}

            .content {{
                padding: 20px;
            }}

            .controls-info {{
                grid-template-columns: 1fr;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="video-icon">🎬</div>
            <h1>{title}</h1>
            {f'<p class="description">{description}</p>' if description else ''}
        </div>

        <div class="video-wrapper">
            <video id="videoPlayer" controls preload="metadata">
                <source src="{video_filename}" type="{video_type}">
                Tu navegador no soporta el elemento de video.
            </video>
        </div>

        <div class="content">
            <div class="progress-container">
                <div class="progress-label">Progreso de Visualización:</div>
                <div class="progress-bar">
                    <div id="progress-fill" class="progress-fill">
                        <span id="progress-text">0%</span>
                    </div>
                </div>
            </div>

            <div class="info">
                <strong>ℹ️ Instrucciones:</strong><br>
                Haz clic en el botón de reproducción para ver el video. Tu progreso se registrará automáticamente.
                El video se considerará completado cuando alcances el 90% de la visualización.
            </div>

            <div class="controls-info">
                <div class="control-item">
                    <div class="control-item-icon">▶️</div>
                    <strong>Reproducir/Pausa</strong><br>
                    Controla la reproducción
                </div>
                <div class="control-item">
                    <div class="control-item-icon">🔊</div>
                    <strong>Volumen</strong><br>
                    Ajusta el volumen
                </div>
                <div class="control-item">
                    <div class="control-item-icon">⛶</div>
                    <strong>Pantalla completa</strong><br>
                    Visualización ampliada
                </div>
            </div>

            <div id="completion-message">
                <h3>✅ ¡Video Completado!</h3>
                <p>¡Excelente trabajo! Tu progreso ha sido registrado.</p>
            </div>

            <div class="footer">
                Paquete SCORM 1.2 - Compatible con Moodle
            </div>
        </div>
    </div>
</body>
</html>
'''
    return html

def create_video_scorm_manifest(title, video_filename):
    """Create imsmanifest.xml for video SCORM"""

    manifest = f'''<?xml version="1.0" encoding="UTF-8"?>
<manifest identifier="com.video.scorm" version="1.0"
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
  <organizations default="org_video">
    <organization identifier="org_video">
      <title>{title}</title>
      <item identifier="item_video" identifierref="resource_video">
        <title>{title}</title>
      </item>
    </organization>
  </organizations>
  <resources>
    <resource identifier="resource_video" type="webcontent" adlcp:scormtype="sco" href="index.html">
      <file href="index.html"/>
      <file href="{video_filename}"/>
    </resource>
  </resources>
</manifest>
'''
    return manifest

def create_video_scorm(video_file, title=None, description="", output_name=None):
    """Create SCORM package with video file"""

    # Validate video file exists
    if not os.path.exists(video_file):
        print(f"Errore: File video '{video_file}' non trovato!")
        return False

    # Get video filename
    video_filename = os.path.basename(video_file)

    # Auto-generate title if not provided
    if title is None:
        title = Path(video_file).stem.replace('_', ' ').replace('-', ' ').title()

    # Auto-generate output name
    if output_name is None:
        output_name = f"{Path(video_file).stem}-SCORM.zip"

    print(f"Creazione pacchetto SCORM per: {video_filename}")
    print(f"Titolo: {title}")

    # Create temp directory
    scorm_dir = 'video_scorm_temp'
    os.makedirs(scorm_dir, exist_ok=True)

    try:
        # Create HTML player
        html_content = create_video_player_html(video_filename, title, description)
        with open(os.path.join(scorm_dir, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(html_content)
        print("  [OK] Creato player HTML")

        # Copy video file
        import shutil
        shutil.copy(video_file, os.path.join(scorm_dir, video_filename))
        print(f"  [OK] Copiato file video: {video_filename}")

        # Create manifest
        manifest = create_video_scorm_manifest(title, video_filename)
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

        file_size = os.path.getsize(output_name) / (1024 * 1024)
        print(f"\n[OK] Pacchetto SCORM creato: {output_name}")
        print(f"[OK] Dimensione: {file_size:.1f} MB")
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
    print("  Creatore Pacchetto SCORM Video per Moodle")
    print("=" * 60)
    print()

    if len(sys.argv) < 2:
        print("Uso: python create_video_scorm.py <file_video> [titolo] [descrizione]")
        print()
        print("Esempi:")
        print("  python create_video_scorm.py lezione.mp4")
        print('  python create_video_scorm.py lezione.mp4 "Lezione 1"')
        print('  python create_video_scorm.py lezione.mp4 "Lezione 1" "Introduzione al corso"')
        print()
        print("Formati supportati: MP4, WEBM, MOV, AVI, MKV")
        return

    video_file = sys.argv[1]
    title = sys.argv[2] if len(sys.argv) > 2 else None
    description = sys.argv[3] if len(sys.argv) > 3 else ""

    create_video_scorm(video_file, title, description)

if __name__ == '__main__':
    main()
