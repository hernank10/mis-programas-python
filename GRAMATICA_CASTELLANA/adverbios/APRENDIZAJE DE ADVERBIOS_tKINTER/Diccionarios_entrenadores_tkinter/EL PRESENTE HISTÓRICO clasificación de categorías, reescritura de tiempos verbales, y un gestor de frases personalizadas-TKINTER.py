import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import re
import csv
from datetime import datetime

class PresenteHistoricoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Estudio del Presente Histórico")
        self.root.geometry("1000x700")
        
        self.frases = []
        self.load_phrases()
        self.create_widgets()

    def create_widgets(self):
        self.notebook = ttk.Notebook(self.root)
        
        # Pestaña de Clasificación
        self.tab_clasificar = ttk.Frame(self.notebook)
        self.create_clasificar_tab()
        
        # Pestaña de Reescribir
        self.tab_reescribir = ttk.Frame(self.notebook)
        self.create_reescribir_tab()
        
        # Pestaña de Gestión
        self.tab_gestion = ttk.Frame(self.notebook)
        self.create_gestion_tab()
        
        self.notebook.add(self.tab_clasificar, text="Clasificar")
        self.notebook.add(self.tab_reescribir, text="Reescribir")
        self.notebook.add(self.tab_gestion, text="Mis Frases")
        self.notebook.pack(expand=True, fill='both')

    def create_clasificar_tab(self):
        frame = ttk.Frame(self.tab_clasificar, padding=15)
        frame.pack(fill='both', expand=True)
        
        ttk.Label(frame, text="Clasificador de Presente Histórico", font=('Arial', 14)).pack(pady=10)
        
        self.txt_input = scrolledtext.ScrolledText(frame, height=8, wrap=tk.WORD)
        self.txt_input.pack(fill='x', pady=5)
        
        ttk.Button(frame, text="Analizar", command=self.clasificar_texto).pack(pady=5)
        
        self.lbl_resultado = ttk.Label(frame, text="", font=('Arial', 10))
        self.lbl_resultado.pack(pady=10)
        
        self.txt_output = scrolledtext.ScrolledText(frame, height=12, wrap=tk.WORD, state='disabled')
        self.txt_output.pack(fill='both', expand=True)

    def create_reescribir_tab(self):
        frame = ttk.Frame(self.tab_reescribir, padding=15)
        frame.pack(fill='both', expand=True)
        
        ttk.Label(frame, text="Reescribir Tiempos Verbales", font=('Arial', 14)).pack(pady=10)
        
        self.cmb_modo = ttk.Combobox(frame, values=["Pasado a Histórico", "Futuro a Histórico"], state="readonly")
        self.cmb_modo.pack(pady=5)
        
        self.txt_original = scrolledtext.ScrolledText(frame, height=8, wrap=tk.WORD)
        self.txt_original.pack(fill='x', pady=5)
        
        ttk.Button(frame, text="Transformar", command=self.reescribir_texto).pack(pady=5)
        
        self.txt_transformado = scrolledtext.ScrolledText(frame, height=12, wrap=tk.WORD, state='disabled')
        self.txt_transformado.pack(fill='both', expand=True)

    def create_gestion_tab(self):
        frame = ttk.Frame(self.tab_gestion, padding=15)
        frame.pack(fill='both', expand=True)
        
        ttk.Label(frame, text="Gestión de Ejemplos", font=('Arial', 14)).pack(pady=10)
        
        ttk.Label(frame, text="Nueva frase:").pack(anchor='w')
        self.entry_frase = ttk.Entry(frame, width=70)
        self.entry_frase.pack(fill='x', pady=5)
        
        ttk.Button(frame, text="Guardar Frase", command=self.guardar_frase).pack(pady=5)
        
        self.txt_ejemplos = scrolledtext.ScrolledText(frame, height=20, wrap=tk.WORD, state='disabled')
        self.txt_ejemplos.pack(fill='both', expand=True)
        
        self.actualizar_lista_ejemplos()

    def clasificar_texto(self):
        texto = self.txt_input.get("1.0", tk.END).strip()
        resultados = []
        
        for oracion in re.split(r'[.!?]', texto):
            oracion = oracion.strip()
            if oracion:
                categoria = self.detectar_presente_historico(oracion)
                resultados.append(f"«{oracion}»\n   → {categoria}\n")
        
        self.txt_output.config(state='normal')
        self.txt_output.delete('1.0', tk.END)
        self.txt_output.insert(tk.END, ''.join(resultados))
        self.txt_output.config(state='disabled')

    def detectar_presente_historico(self, oracion):
        # Detectar fechas pasadas con verbos en presente
        if re.search(r'\b\d{3,4}\b', oracion) and any(self.es_presente_verbal(palabra) for palabra in oracion.split()):
            return "Presente Histórico"
        
        # Contextos narrativos típicos
        narrativos = ['cuando de repente', 'entonces', 'en ese momento']
        if any(expr in oracion.lower() for expr in narrativos):
            return "Presente Histórico Narrativo"
        
        return "Otro tiempo verbal"

    def es_presente_verbal(self, palabra):
        terminaciones = ['o', 'as', 'a', 'amos', 'áis', 'an',
                        'es', 'e', 'imos', 'ís', 'en']
        return any(palabra.lower().endswith(terminacion) for terminacion in terminaciones)

    def reescribir_texto(self):
        texto = self.txt_original.get("1.0", tk.END).strip()
        modo = self.cmb_modo.get()
        
        if modo == "Pasado a Histórico":
            transformado = self.pasado_a_historico(texto)
        else:
            transformado = self.futuro_a_historico(texto)
        
        self.txt_transformado.config(state='normal')
        self.txt_transformado.delete('1.0', tk.END)
        self.txt_transformado.insert(tk.END, transformado)
        self.txt_transformado.config(state='disabled')

    def pasado_a_historico(self, texto):
        conjugaciones = {
            r'ó\b': 'a',
            r'aron\b': 'an',
            r'eron\b': 'en',
            r'í\b': 'o',
            r'aste\b': 'as',
            r'amos\b': 'amos'
        }
        for patron, reemplazo in conjugaciones.items():
            texto = re.sub(patron, reemplazo, texto, flags=re.IGNORECASE)
        return texto

    def futuro_a_historico(self, texto):
        conjugaciones = {
            r'é\b': 'o',
            r'ás\b': 'as',
            r'á\b': 'a',
            r'emos\b': 'emos',
            r'án\b': 'an'
        }
        for patron, reemplazo in conjugaciones.items():
            texto = re.sub(patron, reemplazo, texto, flags=re.IGNORECASE)
        return texto

    def guardar_frase(self):
        frase = self.entry_frase.get().strip()
        if not frase:
            return
        
        if len(self.frases) >= 100:
            messagebox.showwarning("Límite alcanzado", "¡Has alcanzado el máximo de 100 frases!")
            return
        
        categoria = self.detectar_presente_historico(frase)
        self.frases.append((frase, categoria, datetime.now().strftime("%Y-%m-%d %H:%M")))
        self.actualizar_lista_ejemplos()
        self.save_phrases()
        self.entry_frase.delete(0, tk.END)

    def actualizar_lista_ejemplos(self):
        self.txt_ejemplos.config(state='normal')
        self.txt_ejemplos.delete('1.0', tk.END)
        for idx, (frase, cat, fecha) in enumerate(self.frases, 1):
            self.txt_ejemplos.insert(tk.END, f"{idx:03d}. [{cat}] {frase} ({fecha})\n")
        self.txt_ejemplos.config(state='disabled')

    def load_phrases(self):
        try:
            with open('frases_historicas.csv', 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                self.frases = [tuple(row) for row in reader][:100]
        except FileNotFoundError:
            self.frases = []

    def save_phrases(self):
        with open('frases_historicas.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(self.frases)

if __name__ == "__main__":
    root = tk.Tk()
    app = PresenteHistoricoApp(root)
    root.mainloop()
