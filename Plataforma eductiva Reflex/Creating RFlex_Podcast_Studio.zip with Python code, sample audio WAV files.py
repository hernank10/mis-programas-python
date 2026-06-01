# Creating RFlex_Podcast_Studio.zip with Python code, sample audio WAV files (intro, debate, cierre),
# and a simple PDF guide (fallback to TXT if reportlab not available).
import os, zipfile, wave, struct, math, contextlib
from pathlib import Path

BASE = "/mnt/data/RFlex_Podcast_Studio"
if os.path.exists(BASE):
    import shutil
    shutil.rmtree(BASE)
os.makedirs(BASE, exist_ok=True)

# 1) Write the Python code file (rflex_podcast_studio.py)
code = r'''# RFlex Podcast Studio - Advanced generator (placeholder)
# This is the main script to produce podcasts using gTTS and pydub.
# It expects intro.mp3, debate.mp3, cierre.mp3 (or WAV) in the same folder.
# See included guide for installation and usage.
from gtts import gTTS
from pydub import AudioSegment
import os

def generar_podcast(voice='femenina'):
    intro_text = "Bienvenidos al podcast académico del Laboratorio RFlex EduTech."
    debate_text = "En este foro participan docentes, investigadores y programadores educativos."
    cierre_text = "Gracias por acompañarnos. Desde el Laboratorio RFlex, donde la educación tiene voz y sentido."
    
    # create temporary audio segments
    tts_intro = gTTS(text=intro_text, lang='es', tld='com.co', slow=False)
    tts_intro.save('voz_intro.mp3')
    intro_voice = AudioSegment.from_mp3('voz_intro.mp3')
    
    tts_debate = gTTS(text=debate_text, lang='es', tld='com.co', slow=False)
    tts_debate.save('voz_debate.mp3')
    debate_voice = AudioSegment.from_mp3('voz_debate.mp3')
    
    tts_cierre = gTTS(text=cierre_text, lang='es', tld='com.co', slow=False)
    tts_cierre.save('voz_cierre.mp3')
    cierre_voice = AudioSegment.from_mp3('voz_cierre.mp3')
    
    # load background music if present
    def load_bg(name):
        if os.path.exists(name):
            return AudioSegment.from_file(name)
        return AudioSegment.silent(duration=1000)
    
    intro_bg = load_bg('intro.mp3')
    debate_bg = load_bg('debate.mp3')
    cierre_bg = load_bg('cierre.mp3')
    
    # mix (simple overlay)
    intro_final = intro_bg.overlay(intro_voice, position=0)
    debate_final = debate_bg.overlay(debate_voice, position=0)
    cierre_final = cierre_bg.overlay(cierre_voice, position=0)
    
    podcast = intro_final + debate_final + cierre_final
    podcast.export('RFlex_Podcast_Studio_output.mp3', format='mp3')
    print("Podcast generado: RFlex_Podcast_Studio_output.mp3")

if __name__ == '__main__':
    generar_podcast()
'''
code_path = os.path.join(BASE, "rflex_podcast_studio.py")
with open(code_path, "w", encoding="utf-8") as f:
    f.write(code)

# 2) Create sample WAV audio files (intro.wav, debate.wav, cierre.wav) as short musical tones / chimes
def create_tone(filename, freq=440.0, duration_ms=3000, volume=0.2, sample_rate=44100):
    n_samples = int(sample_rate * (duration_ms/1000.0))
    with wave.open(filename, 'w') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)  # 2 bytes per sample
        wf.setframerate(sample_rate)
        max_amp = 32767 * volume
        for i in range(n_samples):
            t = float(i) / sample_rate
            # simple harmonic with slight envelope
            envelope = 1.0 if t < 0.9*(duration_ms/1000.0) else (1.0 - (t - 0.9*(duration_ms/1000.0))*10)
            sample = int(max_amp * envelope * math.sin(2 * math.pi * freq * t))
            data = struct.pack('<h', sample)
            wf.writeframesraw(data)
    # ensure correct file size/frame count
    with contextlib.closing(wave.open(filename,'r')) as r:
        frames = r.getnframes()

# create three distinct tones
create_tone(os.path.join(BASE, "intro.wav"), freq=330.0, duration_ms=4000, volume=0.25)
create_tone(os.path.join(BASE, "debate.wav"), freq=440.0, duration_ms=5000, volume=0.20)
create_tone(os.path.join(BASE, "cierre.wav"), freq=262.0, duration_ms=3500, volume=0.22)

# 3) Create a simple PDF guide if reportlab available; otherwise a TXT guide
guide_pdf_path = os.path.join(BASE, "RFlex_Podcast_Studio_Guide.pdf")
guide_txt_path = os.path.join(BASE, "RFlex_Podcast_Studio_Guide.txt")
guide_content = """
RFlex Podcast Studio - Guía de instalación y uso
------------------------------------------------

Contenido:
1. Descripción del paquete
2. Requisitos
3. Uso rápido
4. Personalización de voces y música
5. Publicación y recomendaciones

1. Descripción
Este paquete incluye:
- rflex_podcast_studio.py : script principal que combina voces TTS y música de fondo.
- intro.wav, debate.wav, cierre.wav : archivos de audio de ejemplo para la música/efectos.
- RFlex_Podcast_Studio_Guide.pdf (o TXT) : esta guía.
- rflex_podcast_studio.py (código fuente).

2. Requisitos
- Python 3.8+
- pip install gtts pydub
- FFmpeg instalado (necesario para pydub si exportas MP3)
  - macOS: brew install ffmpeg
  - Ubuntu/Debian: sudo apt install ffmpeg
  - Windows: descargar desde ffmpeg.org

3. Uso rápido
- Coloque los archivos intro.wav, debate.wav y cierre.wav en la misma carpeta.
- Edite rflex_podcast_studio.py para cambiar los textos del guion.
- Ejecute: python rflex_podcast_studio.py
- El script generará RFlex_Podcast_Studio.mp3 o RFlex_Podcast_Studio_output.mp3

4. Personalización
- Reemplace los WAV por MP3 de música libre de derechos (por ejemplo, intro.mp3).
- Cambie la voz (gTTS) modificando los parámetros de tld (por ejemplo 'com.co') o use servicios TTS avanzados.
- Para voces múltiples, genere archivos de voz por sección y combínelos con pydub.

5. Publicación
- Verifique niveles de volumen y normalice el audio antes de subir.
- Añada metadatos ID3 y una imagen de portada si lo sube a Spotify o plataformas de podcast.
- Licencia: se recomienda Creative Commons Atribución para materiales educativos.
"""

# try to create PDF using reportlab
created_pdf = False
try:
    from reportlab.lib.pagesizes import letter
    from reportlab.pdfgen import canvas
    c = canvas.Canvas(guide_pdf_path, pagesize=letter)
    textobject = c.beginText(40, 750)
    for line in guide_content.splitlines():
        textobject.textLine(line)
    c.drawText(textobject)
    c.showPage()
    c.save()
    created_pdf = True
except Exception as e:
    # fallback: write TXT guide
    with open(guide_txt_path, "w", encoding="utf-8") as f:
        f.write(guide_content)

# 4) Create a simple README
readme = f"""RFlex Podcast Studio - Package
Includes:
- rflex_podcast_studio.py  (main script)
- intro.wav, debate.wav, cierre.wav  (example audio)
- RFlex_Podcast_Studio_Guide.{ 'pdf' if created_pdf else 'txt' }

How to use:
1. Install dependencies: pip install gtts pydub
2. Install ffmpeg on your OS
3. Run: python rflex_podcast_studio.py
"""
with open(os.path.join(BASE, "README.txt"), "w", encoding="utf-8") as f:
    f.write(readme)

# 5) Zip the folder
zip_path = "/mnt/data/RFlex_Podcast_Studio.zip"
with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
    for root, dirs, files in os.walk(BASE):
        for fn in files:
            full = os.path.join(root, fn)
            arc = os.path.relpath(full, BASE)
            zf.write(full, arc)

zip_path

