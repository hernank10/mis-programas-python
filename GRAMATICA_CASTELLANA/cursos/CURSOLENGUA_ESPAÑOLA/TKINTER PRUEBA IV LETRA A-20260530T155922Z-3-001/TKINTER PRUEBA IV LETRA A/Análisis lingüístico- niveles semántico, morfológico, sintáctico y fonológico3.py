import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json
import os
import sounddevice as sd
from scipy.io.wavfile import write
from gtts import gTTS
import eng_to_ipa as ipa
import time

class LinguisticApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Linguistic Analysis Suite")
        self.root.geometry("1000x700")
        
        # Configuración inicial
        self.AUDIO_DIR = "audio_samples"
        os.makedirs(self.AUDIO_DIR, exist_ok=True)
        
        self.niveles = {
            "semántico": {"ejemplos": [], "max": 100},
            "morfológico": {"ejemplos": [], "max": 100},
            "sintáctico": {"ejemplos": [], "max": 100},
            "fonológico": {"ejemplos": [], "max": 100}
        }
        
        # Variables de estado
        self.current_audio = []
        self.current_level = tk.StringVar()
        self.recording = False
        
        # Configurar interfaz
        self.setup_ui()
        
    def setup_ui(self):
        # Notebook principal
        self.notebook = ttk.Notebook(self.root)
        
        # Pestañas
        self.tab_create = ttk.Frame(self.notebook)
        self.tab_view = ttk.Frame(self.notebook)
        self.tab_manage = ttk.Frame(self.notebook)
        
        self.notebook.add(self.tab_create, text="Crear Ejemplo")
        self.notebook.add(self.tab_view, text="Ver Ejemplos")
        self.notebook.add(self.tab_manage, text="Gestión de Datos")
        self.notebook.pack(expand=True, fill='both')
        
        # Widgets para creación de ejemplos
        self.create_example_ui()
        self.view_examples_ui()
        self.manage_data_ui()
        
    def create_example_ui(self):
        frame = ttk.LabelFrame(self.tab_create, text="Nuevo Ejemplo")
        frame.pack(padx=20, pady=20, fill='both', expand=True)
        
        # Nivel
        ttk.Label(frame, text="Nivel:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.level_combo = ttk.Combobox(frame, values=list(self.niveles.keys()), 
                                      textvariable=self.current_level)
        self.level_combo.grid(row=0, column=1, padx=5, pady=5, sticky='ew')
        
        # Texto español
        ttk.Label(frame, text="Texto en español:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.text_es = tk.Text(frame, height=3, width=50)
        self.text_es.grid(row=1, column=1, columnspan=2, padx=5, pady=5, sticky='ew')
        
        # Texto inglés
        ttk.Label(frame, text="Texto en inglés:").grid(row=2, column=0, padx=5, pady=5, sticky='e')
        self.text_en = tk.Text(frame, height=3, width=50)
        self.text_en.grid(row=2, column=1, columnspan=2, padx=5, pady=5, sticky='ew')
        
        # Botones de audio
        ttk.Button(frame, text="Grabar Audio (5s)", command=self.record_audio).grid(
            row=3, column=1, padx=5, pady=5, sticky='ew')
        ttk.Button(frame, text="Generar TTS", command=self.generate_tts).grid(
            row=3, column=2, padx=5, pady=5, sticky='ew')
        
        # Visualización AFI
        ttk.Label(frame, text="AFI Español:").grid(row=4, column=0, padx=5, pady=5, sticky='e')
        self.afi_es = ttk.Label(frame, text="", wraplength=400)
        self.afi_es.grid(row=4, column=1, columnspan=2, padx=5, pady=5, sticky='w')
        
        ttk.Label(frame, text="AFI Inglés:").grid(row=5, column=0, padx=5, pady=5, sticky='e')
        self.afi_en = ttk.Label(frame, text="", wraplength=400)
        self.afi_en.grid(row=5, column=1, columnspan=2, padx=5, pady=5, sticky='w')
        
        # Botón final
        ttk.Button(frame, text="Guardar Ejemplo", command=self.save_example).grid(
            row=6, column=1, columnspan=2, padx=5, pady=20, sticky='ew')
        
    def view_examples_ui(self):
        frame = ttk.Frame(self.tab_view)
        frame.pack(padx=20, pady=20, fill='both', expand=True)
        
        # Lista de ejemplos
        self.example_list = ttk.Treeview(frame, columns=('level', 'text_es'), show='headings')
        self.example_list.heading('level', text='Nivel')
        self.example_list.heading('text_es', text='Texto (ES)')
        self.example_list.pack(side='left', fill='both', expand=True)
        
        # Detalles del ejemplo
        detail_frame = ttk.Frame(frame)
        detail_frame.pack(side='right', fill='both', expand=True, padx=10)
        
        self.detail_text = tk.Text(detail_frame, height=10, width=40)
        self.detail_text.pack(pady=5)
        
        ttk.Button(detail_frame, text="Reproducir TTS ES", 
                 command=lambda: self.play_audio('tts_es')).pack(side='left', padx=2)
        ttk.Button(detail_frame, text="Reproducir TTS EN", 
                 command=lambda: self.play_audio('tts_en')).pack(side='left', padx=2)
        ttk.Button(detail_frame, text="Reproducir Grabación", 
                 command=lambda: self.play_audio('user')).pack(side='left', padx=2)
        
    def manage_data_ui(self):
        frame = ttk.Frame(self.tab_manage)
        frame.pack(padx=20, pady=20, fill='both', expand=True)
        
        ttk.Button(frame, text="Guardar Datos", command=self.save_data).pack(pady=10)
        ttk.Button(frame, text="Cargar Datos", command=self.load_data).pack(pady=10)
        
    def generate_tts(self):
        texto_es = self.text_es.get("1.0", "end-1c")
        texto_en = self.text_en.get("1.0", "end-1c")
        
        if texto_es:
            tts_es = gTTS(text=texto_es, lang='es')
            tts_es.save(os.path.join(self.AUDIO_DIR, f"tts_es_{int(time.time())}.mp3"))
            
        if texto_en:
            tts_en = gTTS(text=texto_en, lang='en')
            tts_en.save(os.path.join(self.AUDIO_DIR, f"tts_en_{int(time.time())}.mp3"))
            
        messagebox.showinfo("TTS Generado", "Audios generados exitosamente")
        
    def record_audio(self):
        self.recording = True
        fs = 44100
        duration = 5
        
        def recording_thread():
            recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
            sd.wait()
            filename = os.path.join(self.AUDIO_DIR, f"user_{int(time.time())}.wav")
            write(filename, fs, recording)
            self.current_audio.append(filename)
            self.recording = False
            
        import threading
        threading.Thread(target=recording_thread).start()
        
    def save_example(self):
        # Validación de datos
        level = self.current_level.get()
        if not level:
            messagebox.showerror("Error", "Selecciona un nivel")
            return
            
        # Obtener textos
        texto_es = self.text_es.get("1.0", "end-1c")
        texto_en = self.text_en.get("1.0", "end-1c")
        
        # Generar AFI
        afi_es = self.spanish_to_ipa(texto_es)
        afi_en = ipa.convert(texto_en)
        
        # Guardar datos
        ejemplo = {
            "texto": {"es": texto_es, "en": texto_en},
            "audio": {
                "tts_es": os.path.join(self.AUDIO_DIR, f"tts_es_{int(time.time())}.mp3"),
                "tts_en": os.path.join(self.AUDIO_DIR, f"tts_en_{int(time.time())}.mp3"),
                "user": self.current_audio[-1] if self.current_audio else ""
            },
            "afi": {"es": afi_es, "en": afi_en}
        }
        
        self.niveles[level]["ejemplos"].append(ejemplo)
        messagebox.showinfo("Éxito", "Ejemplo guardado correctamente")
        
    def play_audio(self, audio_type):
        # Implementar lógica de reproducción
        pass
        
    def save_data(self):
        file = filedialog.asksaveasfilename(defaultextension=".json")
        if file:
            with open(file, 'w') as f:
                json.dump(self.niveles, f)
                
    def load_data(self):
        file = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if file:
            with open(file, 'r') as f:
                self.niveles = json.load(f)
                
    def spanish_to_ipa(self, texto):
        # Implementar conversión a AFI para español
        return " ".join([f"/{c}/" for c in texto.lower()])

if __name__ == "__main__":
    root = tk.Tk()
    app = LinguisticApp(root)
    root.mainloop()
