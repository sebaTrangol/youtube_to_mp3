import os
from yt_dlp import YoutubeDL

# Carpeta de salida
OUTPUT_FOLDER = "tuRutaDestino"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Pedir URL
raw_url = input("🎥 Ingresa la URL del video de YouTube: ").strip()
video_url = raw_url.split('&')[0]  # Elimina todo lo que venga después de "&"

# Opciones de descarga
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': os.path.join(OUTPUT_FOLDER, '%(title)s.%(ext)s'),
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'quiet': False,
    'no_warnings': True
}

try:
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
        print("✅ Descarga y conversión completadas.")
except Exception as e:
    print(f"❌ Error durante la descarga: {e}")
