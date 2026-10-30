"""Podcast Audio Engine for Educational Units (Kit Aula Nueva).

Generates high-quality two-host or single-host pedagogical podcasts using
free neural TTS (edge-tts) with authentic Argentine (Rioplatense) accent
and professional audio mastering via ffmpeg (warm EQ + loudness normalization).
"""

import asyncio
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import edge_tts

# Audio polish filter chain inspired by Claudemy
POLISH_AF = (
    "highpass=f=90,equalizer=f=200:t=q:w=1:g=-2,equalizer=f=3000:t=q:w=1:g=2.5,"
    "deesser,lowpass=f=13500,acompressor=ratio=2.5,aecho=0.8:0.5:40:0.08,loudnorm=I=-16"
)

DEFAULT_VOICE_A = "es-AR-ElenaNeural"   # Femenina rioplatense (principal/docente)
DEFAULT_VOICE_B = "es-AR-TomasNeural"   # Masculina rioplatense (residente/copresentador)


def parse_turns(text: str):
    """Parse dialogue turns from text formatted as 'A: ...' and 'B: ...'."""
    turns = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        speaker, sep, said = line.partition(":")
        if sep and speaker.strip() in ("A", "B", "Elena", "Tomas", "Tomás") and said.strip():
            spk_norm = "A" if speaker.strip() in ("A", "Elena") else "B"
            turns.append((spk_norm, said.strip()))
        elif not turns and line:
            # Single speaker mode if no prefix is given
            turns.append(("A", line))
        elif turns and not sep:
            # Append continuation lines to the previous turn
            prev_spk, prev_text = turns[-1]
            turns[-1] = (prev_spk, f"{prev_text} {line}")
    return turns


async def _render_turn_audio(text: str, voice: str, out_path: Path):
    """Render a single turn via edge-tts."""
    comm = edge_tts.Communicate(text, voice=voice, rate="+0%", pitch="+0Hz")
    await comm.save(str(out_path))


async def render_dialogue_to_mp3(script_text: str, output_path: Path, voice_a: str = DEFAULT_VOICE_A, voice_b: str = DEFAULT_VOICE_B):
    """Render full script into a single polished MP3 file."""
    turns = parse_turns(script_text)
    if not turns:
        raise ValueError("No valid speech turns found in script.")

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp = Path(tmp_dir)
        part_files = []

        for idx, (spk, said) in enumerate(turns):
            voice = voice_a if spk == "A" else voice_b
            part_file = tmp / f"turn_{idx:03d}.mp3"
            await _render_turn_audio(said, voice, part_file)
            part_files.append(part_file)

        # Concatenate using ffmpeg concat filter or file list
        concat_list = tmp / "concat.txt"
        with open(concat_list, "w", encoding="utf-8") as f:
            for pf in part_files:
                f.write(f"file '{pf.as_posix()}'\n")

        raw_merged = tmp / "merged_raw.mp3"
        subprocess.run(
            ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(concat_list), "-c", "copy", str(raw_merged)],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        # Apply polish filter
        subprocess.run(
            ["ffmpeg", "-y", "-i", str(raw_merged), "-af", POLISH_AF, "-b:a", "128k", str(output_path)],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )


def generate_podcast_sync(script_text: str, output_path: str | Path, voice_a: str = DEFAULT_VOICE_A, voice_b: str = DEFAULT_VOICE_B):
    """Synchronous helper for easy embedding in build scripts."""
    asyncio.run(render_dialogue_to_mp3(script_text, Path(output_path), voice_a, voice_b))


if __name__ == "__main__":
    sample_script = """
    A: Hola, te damos la bienvenida a este podcast de la unidad. Hoy vamos a analizar por qué gestionar no es lo mismo que administrar.
    B: Totalmente, Elena. En la guardia médica muchas veces nos quedamos atrapados en el papeleo normativo y perdemos de vista el liderazgo real del equipo.
    A: Exacto. Fijate que el SER de la institución no se negocia; se vive en el ESTAR cotidiano de cada servicio.
    """
    out_test = Path(__file__).parent / "test_podcast.mp3"
    print("Generating test podcast...")
    generate_podcast_sync(sample_script, out_test)
    print(f"Generated: {out_test} (Size: {out_test.stat().st_size} bytes)")
    if out_test.exists():
        out_test.unlink()
