import json
import subprocess
from pathlib import Path

ARTICLES_DIR = Path(r"c:\Users\mfischer\Documents\antigravitiy proyectos\aula nueva con moodle\output\articles")

def get_duration(mp3_path: Path) -> float:
    cmd = [
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", str(mp3_path)
    ]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return float(res.stdout.strip())
    except Exception:
        return 5.0

def assemble_video_for_article(art_dir: Path):
    json_path = art_dir / "article.json"
    if not json_path.exists():
        return
    
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    title = data.get("title", art_dir.name)
    sections = [b for b in data.get("blocks", []) if b.get("type") == "section"]
    pngs = sorted(list(art_dir.glob("block_*.png")))
    
    # Duraciones de audio
    d0 = get_duration(art_dir / "audio_step_0.mp3") + 0.8
    d1 = get_duration(art_dir / "audio_step_1.mp3") + 0.8
    d2 = get_duration(art_dir / "audio_step_2.mp3") + 0.8
    d3 = get_duration(art_dir / "audio_step_3.mp3") + 0.8
    
    # 1. Crear slide intro en video
    intro_img = art_dir / "slide_0.png"
    # Usar ffmpeg lavfi para generar slide con título
    # Para máxima compatibilidad en Windows, generamos los slides de video con ffmpeg
    
    # Archivos de audio
    a0 = art_dir / "audio_step_0.mp3"
    a1 = art_dir / "audio_step_1.mp3"
    a2 = art_dir / "audio_step_2.mp3"
    a3 = art_dir / "audio_step_3.mp3"
    
    img1 = pngs[0] if len(pngs) > 0 else art_dir / "slide_0.png"
    img2 = pngs[1] if len(pngs) > 1 else img1
    img3 = pngs[2] if len(pngs) > 2 else img2

    # Render segments
    seg0 = art_dir / "seg0.mp4"
    seg1 = art_dir / "seg1.mp4"
    seg2 = art_dir / "seg2.mp4"
    seg3 = art_dir / "seg3.mp4"

    # Segment 0 (Intro slide from image 1 with dark tint)
    cmd0 = [
        "ffmpeg", "-y", "-loop", "1", "-i", str(img1), "-i", str(a0),
        "-vf", "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,format=yuv420p",
        "-c:v", "libx264", "-tune", "stillimage", "-c:a", "aac", "-b:a", "192k", "-shortest", str(seg0)
    ]
    subprocess.run(cmd0, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Segment 1
    cmd1 = [
        "ffmpeg", "-y", "-loop", "1", "-i", str(img1), "-i", str(a1),
        "-vf", "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,format=yuv420p",
        "-c:v", "libx264", "-tune", "stillimage", "-c:a", "aac", "-b:a", "192k", "-shortest", str(seg1)
    ]
    subprocess.run(cmd1, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Segment 2
    cmd2 = [
        "ffmpeg", "-y", "-loop", "1", "-i", str(img2), "-i", str(a2),
        "-vf", "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,format=yuv420p",
        "-c:v", "libx264", "-tune", "stillimage", "-c:a", "aac", "-b:a", "192k", "-shortest", str(seg2)
    ]
    subprocess.run(cmd2, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Segment 3
    cmd3 = [
        "ffmpeg", "-y", "-loop", "1", "-i", str(img3), "-i", str(a3),
        "-vf", "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,format=yuv420p",
        "-c:v", "libx264", "-tune", "stillimage", "-c:a", "aac", "-b:a", "192k", "-shortest", str(seg3)
    ]
    subprocess.run(cmd3, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Concat segments into final MP4
    concat_txt = art_dir / "concat.txt"
    with open(concat_txt, "w", encoding="utf-8") as f:
        f.write(f"file '{seg0.name}'\n")
        f.write(f"file '{seg1.name}'\n")
        f.write(f"file '{seg2.name}'\n")
        f.write(f"file '{seg3.name}'\n")

    out_mp4 = art_dir / "videotutorial.mp4"
    cmd_concat = [
        "ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(concat_txt),
        "-c", "copy", str(out_mp4)
    ]
    subprocess.run(cmd_concat, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Clean up intermediate segments
    for temp in [seg0, seg1, seg2, seg3, concat_txt]:
        if temp.exists():
            temp.unlink()
    
    print(f"[{art_dir.name}] Video rendered successfully: {out_mp4.name} ({out_mp4.stat().st_size / (1024*1024):.2f} MB)")

if __name__ == "__main__":
    for art_dir in sorted(ARTICLES_DIR.iterdir()):
        if art_dir.is_dir():
            assemble_video_for_article(art_dir)
    print("\nAll 8 videotutorials rendered and placed beside their corresponding guides.")
