import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.scrolledtext import ScrolledText

class VerbGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Analizador de Verbos Español")
        self.geometry("800x600")
        
        self.analyzer = VerbAnalyzer()
        self.conjugator = Conjugator()
        self.soundex = SpanishSoundex()
        self.db = VerbDatabase()
        
        self._create_widgets()
        self._load_initial_data()
    
    def _create_widgets(self):
        self.notebook = ttk.Notebook(self)
        
        # Pestaña de Análisis
        self.analysis_frame = ttk.Frame(self.notebook)
        self._create_analysis_tab()
        
        # Pestaña de Conjugación
        self.conjugation_frame = ttk.Frame(self.notebook)
        self._create_conjugation_tab()
        
        # Pestaña de Búsqueda
        self.search_frame = ttk.Frame(self.notebook)
        self._create_search_tab()
        
        # Pestaña de Agregar
        self.add_frame = ttk.Frame(self.notebook)
        self._create_add_tab()
        
        self.notebook.add(self.analysis_frame, text="Análisis")
        self.notebook.add(self.conjugation_frame, text="Conjugación")
        self.notebook.add(self.search_frame, text="Búsqueda")
        self.notebook.add(self.add_frame, text="Agregar")
        self.notebook.pack(expand=True, fill=tk.BOTH)
    
    def _create_analysis_tab(self):
        ttk.Label(self.analysis_frame, text="Verbo a analizar:").pack(pady=5)
        self.analysis_entry = ttk.Entry(self.analysis_frame, width=30)
        self.analysis_entry.pack(pady=5)
        
        ttk.Button(self.analysis_frame, text="Analizar", 
                 command=self._handle_analysis).pack(pady=5)
        
        self.analysis_result = ScrolledText(self.analysis_frame, height=10)
        self.analysis_result.pack(pady=10, fill=tk.BOTH, expand=True)
    
    def _create_conjugation_tab(self):
        ttk.Label(self.conjugation_frame, text="Verbo a conjugar:").pack(pady=5)
        self.conjugation_entry = ttk.Entry(self.conjugation_frame, width=30)
        self.conjugation_entry.pack(pady=5)
        
        ttk.Button(self.conjugation_frame, text="Conjugar",
                 command=self._handle_conjugation).pack(pady=5)
        
        self.conjugation_result = ScrolledText(self.conjugation_frame, height=15)
        self.conjugation_result.pack(pady=10, fill=tk.BOTH, expand=True)
    
    def _create_search_tab(self):
        ttk.Label(self.search_frame, text="Buscar similares a:").pack(pady=5)
        self.search_entry = ttk.Entry(self.search_frame, width=30)
        self.search_entry.pack(pady=5)
        
        ttk.Button(self.search_frame, text="Buscar",
                 command=self._handle_search).pack(pady=5)
        
        self.search_result = tk.Listbox(self.search_frame, height=10)
        self.search_result.pack(pady=10, fill=tk.BOTH, expand=True)
    
    def _create_add_tab(self):
        fields = [
            ("Verbo:", "add_verb"),
            ("Base:", "add_base"),
            ("Sufijo:", "add_suffix"),
            ("Tipo:", "add_type")
        ]
        
        for text, var_name in fields:
            frame = ttk.Frame(self.add_frame)
            ttk.Label(frame, text=text).pack(side=tk.LEFT, padx=5)
            entry = ttk.Entry(frame, width=25)
            entry.pack(side=tk.LEFT, expand=True)
            setattr(self, var_name, entry)
            frame.pack(pady=2, fill=tk.X)
        
        ttk.Button(self.add_frame, text="Agregar Verbo",
                 command=self._handle_add_verb).pack(pady=10)
    
    def _handle_analysis(self):
        verb = self.analysis_entry.get().lower()
        if not verb:
            messagebox.showwarning("Entrada vacía", "Por favor ingrese un verbo")
            return
        
        analysis = self.analyzer.analyze(verb)
        self.analysis_result.delete(1.0, tk.END)
        for key, value in analysis.items():
            self.analysis_result.insert(tk.END, f"{key.capitalize()}: {value}\n")
    
    def _handle_conjugation(self):
        verb = self.conjugation_entry.get().lower()
        if not verb:
            messagebox.showwarning("Entrada vacía", "Por favor ingrese un verbo")
            return
        
        try:
            conjugations = self.conjugator.conjugate(verb)
            self.conjugation_result.delete(1.0, tk.END)
            for tense, persons in conjugations.items():
                self.conjugation_result.insert(tk.END, f"\n{tense.capitalize()}:\n")
                for person, form in persons.items():
                    self.conjugation_result.insert(tk.END, f"  {person}: {form}\n")
        except Exception as e:
            messagebox.showerror("Error", f"Error al conjugar: {str(e)}")
    
    def _handle_search(self):
        term = self.search_entry.get().lower()
        if not term:
            messagebox.showwarning("Entrada vacía", "Por favor ingrese un término")
            return
        
        results = self.db.search_soundex(term)
        self.search_result.delete(0, tk.END)
        for result in results:
            self.search_result.insert(tk.END, result)
    
    def _handle_add_verb(self):
        verb_data = {
            'verb': self.add_verb.get(),
            'base': self.add_base.get(),
            'suffix': self.add_suffix.get(),
            'type': self.add_type.get()
        }
        
        if not all(verb_data.values()):
            messagebox.showwarning("Datos incompletos", "Todos los campos son requeridos")
            return
        
        try:
            self.db.save_verb(verb_data)
            messagebox.showinfo("Éxito", "Verbo agregado correctamente")
            self._clear_add_fields()
        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar: {str(e)}")
    
    def _clear_add_fields(self):
        self.add_verb.delete(0, tk.END)
        self.add_base.delete(0, tk.END)
        self.add_suffix.delete(0, tk.END)
        self.add_type.delete(0, tk.END)
    
    def _load_initial_data(self):
        for verb in ['amar', 'temer', 'partir', 'tener', 'hacer']:
            self.db.save_verb({'verb': verb, **self.analyzer.analyze(verb)})

if __name__ == '__main__':
    app = VerbGUI()
    app.mainloop()
