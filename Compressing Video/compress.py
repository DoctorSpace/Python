import subprocess
import json
import sys
from pathlib import Path

TARGET_MB = 16
AUDIO_KBPS = 96
MIN_VIDEO_KBPS = 300

VIDEO_DIR = Path("video")
OUTPUT_DIR = Path("compress")

def get_duration(path: Path) -> float:
    result = subprocess.run(
        [
            "ffprobe",
            "-v", "error",
            "-show_entries", "format=duration",
            "-of", "json",
            str(path)
        ],
        capture_output=True,
        text=True,
        check=True
    )
    return float(json.loads(result.stdout)["format"]["duration"])

def compress_mp4(input_path: Path, output_path: Path):
    duration = get_duration(input_path)

    total_kbps = (TARGET_MB * 8192) / duration
    video_kbps = max(int(total_kbps - AUDIO_KBPS), MIN_VIDEO_KBPS)

    null_device = "NUL" if sys.platform == "win32" else "/dev/null"

    print(f"▶ Сжимаю: {input_path.name}")

    # pass 1
    subprocess.run([
        "ffmpeg", "-y",
        "-i", str(input_path),
        "-c:v", "libx264",
        "-b:v", f"{video_kbps}k",
        "-pass", "1",
        "-an",
        "-f", "mp4",
        null_device
    ], check=True)

    # pass 2
    subprocess.run([
        "ffmpeg", "-y",
        "-i", str(input_path),
        "-c:v", "libx264",
        "-b:v", f"{video_kbps}k",
        "-pass", "2",
        "-c:a", "aac",
        "-b:a", f"{AUDIO_KBPS}k",
        "-movflags", "+faststart",
        str(output_path)
    ], check=True)

    print(f"✔ Готово: {output_path}\n")

def main():
    if not VIDEO_DIR.exists():
        print("❌ Папка 'video' не найдена")
        return

    OUTPUT_DIR.mkdir(exist_ok=True)

    videos = list(VIDEO_DIR.glob("*.mp4"))

    if not videos:
        print("❌ В папке 'video' нет mp4 файлов")
        return

    for video in videos:
        output_name = f"compress-{video.stem}.mp4"
        output_path = OUTPUT_DIR / output_name

        compress_mp4(video, output_path)

if __name__ == "__main__":
    main()


# python compress.py video.mp4