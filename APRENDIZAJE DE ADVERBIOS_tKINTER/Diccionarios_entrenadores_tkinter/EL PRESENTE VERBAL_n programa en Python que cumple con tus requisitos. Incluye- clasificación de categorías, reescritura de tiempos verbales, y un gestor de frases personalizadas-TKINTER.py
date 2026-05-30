import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import re
import csv
from datetime import datetime

class PresentacionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Estudio del Tiempo Presente")
        self.root.geometry("1000x700")
        
        self.create_main_menu()
        self.frases = []
        self.load_phrases()

    def create_main_menu(self):
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack(expand=True, fill='both')

        ttk.Label(main_frame, text="ESTUDIO DEL TIEMPO PRESENTE", 
                 font=('Arial', 16, 'bold')).pack(pady=10)

        buttons = [
            ("Ver Presentación Teórica", self.show_theory),
            ("Clasificar Oración", self.show_classifier),
            ("Reescribir Tiempos Verbales", self.show_rewriter),
            ("Gestor de Frases", self.show_phrase_manager),
            ("Salir", self.root.quit)
        ]

        for text, command in buttons:
            ttk.Button(main_frame, text=text, command=command, width=30).pack(pady=5)

    def show_theory(self):
        theory_window = tk.Toplevel(self.root)
        theory_window.title("Presentación Teórica")
        theory_window.geometry("900x600")

        notebook = ttk.Notebook(theory_window)
        
        # Pestaña 1: Presente Habitual
        tab1 = ttk.Frame(notebook)
        self.create_tab_content(tab1, 
            "Presente Habitual\n\nAcciones recurrentes y hábitos\n\nEjemplos:",
            ["- Mi hermana practica yoga los miércoles y viernes",
             "- Los árboles pierden sus hojas en otoño",
             "- El profesor revisa los exámenes cada mes",
             "- Siempre desayuno café con tostadas"])
        
        # Pestaña 2: Presente Actual
        tab2 = ttk.Frame(notebook)
        self.create_tab_content(tab2,
            "Presente Actual\n\nAcciones en curso\n\nEjemplos:",
            ["- Ahora mismo escribo un poema",
             "- El bebé duerme profundamente",
             "- Mientras hablamos, el sol se oculta",
             "- En este momento firmo el contrato"])
        
        # Pestaña 3: Presente Noómico
        tab3 = ttk.Frame(notebook)
        self.create_tab_content(tab3,
            "Presente Noómico\n\nVerdades universales\n\nEjemplos:",
            ["- La Tierra gira alrededor del Sol",
             "- El agua hierve a 100°C al nivel del mar",
             "- Los seres humanos necesitan oxígeno",
             "- 'A quien madruga, Dios lo ayuda'"])
        
        # Pestaña 4: Presente por Futuro
        tab4 = ttk.Frame(notebook)
        self.create_tab_content(tab4,
            "Presente por Futuro\n\nPlanes y decisiones\n\nEjemplos:",
            ["- Mañana viajo a Nueva York",
             "- La próxima semana inicio el curso",
             "- Esta noche cenamos paella",
             "- En diciembre compramos la casa"])

        notebook.add(tab1, text="Habitual")
        notebook.add(tab2, text="Actual")
        notebook.add(tab3, text="Noómico")
        notebook.add(tab4, text="Por Futuro")
        notebook.pack(expand=True, fill='both')

    def create_tab_content(self, tab, title, examples):
        title_label = ttk.Label(tab, text=title, font=('Arial', 12, 'bold'))
        title_label.pack(pady=10, anchor='w')
        
        examples_text = scrolledtext.ScrolledText(tab, width=80, height=15)
        examples_text.pack(padx=10, pady=5, fill='both', expand=True)
        
        for example in examples:
            examples_text.insert(tk.END, f"• {example}\n")
        examples_text.configure(state='disabled')

    def show_classifier(self):
        classifier_window = tk.Toplevel(self.root)
        classifier_window.title("Clasificador de Tiempos Verbales")
        
        frame = ttk.Frame(classifier_window, padding=20)
        frame.pack()
        
        ttk.Label(frame, text="Ingrese una oración:").pack(pady=5)
        self.entry_classify = ttk.Entry(frame, width=50)
        self.entry_classify.pack(pady=5)
        
        ttk.Button(frame, text="Clasificar", 
                  command=self.classify_sentence).pack(pady=10)
        
        self.result_label = ttk.Label(frame, text="", font=('Arial', 10, 'bold'))
        self.result_label.pack(pady=10)

    def classify_sentence(self):
        oracion = self.entry_classify.get()
        categoria = self.clasificar_categoria(oracion)
        self.result_label.config(text=f"Categoría: {categoria}")

    def show_rewriter(self):
        rewriter_window = tk.Toplevel(self.root)
        rewriter_window.title("Reescribir Tiempos Verbales")
        
        frame = ttk.Frame(rewriter_window, padding=20)
        frame.pack()
        
        ttk.Label(frame, text="Ingrese una oración en futuro:").pack(pady=5)
        self.entry_rewrite = ttk.Entry(frame, width=50)
        self.entry_rewrite.pack(pady=5)
        
        ttk.Button(frame, text="Reescribir", 
                  command=self.rewrite_sentence).pack(pady=10)
        
        self.rewrite_result = ttk.Label(frame, text="", font=('Arial', 10))
        self.rewrite_result.pack(pady=10)

    def rewrite_sentence(self):
        oracion = self.entry_rewrite.get()
        reescrita = self.reescribir_futuro_a_presente(oracion)
        self.rewrite_result.config(text=f"Oración reescrita: {reescrita}")

    def show_phrase_manager(self):
        manager_window = tk.Toplevel(self.root)
        manager_window.title("Gestor de Frases Personalizadas")
        manager_window.geometry("800x500")
        
        frame = ttk.Frame(manager_window, padding=20)
        frame.pack(expand=True, fill='both')
        
        ttk.Label(frame, text="Nueva frase:").pack(pady=5)
        self.entry_phrase = ttk.Entry(frame, width=60)
        self.entry_phrase.pack(pady=5)
        
        ttk.Button(frame, text="Guardar Frase", 
                  command=self.save_phrase).pack(pady=5)
        
        ttk.Separator(frame).pack(fill='x', pady=10)
        
        self.phrases_list = scrolledtext.ScrolledText(frame, width=80, height=15)
        self.phrases_list.pack(pady=5, expand=True, fill='both')
        self.update_phrases_list()

    def save_phrase(self):
        frase = self.entry_phrase.get()
        if len(self.frases) >= 100:
            messagebox.showwarning("Límite alcanzado", "Se ha alcanzado el máximo de 100 frases.")
            return
        
        categoria = self.clasificar_categoria(frase)
        self.frases.append([frase, categoria, datetime.now().strftime("%Y-%m-%d %H:%M")])
        self.update_phrases_list()
        self.save_to_csv()
        messagebox.showinfo("Éxito", "Frase guardada correctamente.")
        self.entry_phrase.delete(0, tk.END)

    def update_phrases_list(self):
        self.phrases_list.configure(state='normal')
        self.phrases_list.delete(1.0, tk.END)
        for i, (f, c, d) in enumerate(self.frases, 1):
            self.phrases_list.insert(tk.END, f"{i}. [{c}] {f} ({d})\n")
        self.phrases_list.configure(state='disabled')

    def load_phrases(self):
        try:
            with open('frases_personalizadas.csv', 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                self.frases = [row for row in reader][:100]
        except FileNotFoundError:
            self.frases = []

    def save_to_csv(self):
        with open('frases_personalizadas.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(self.frases)

    # Funciones de lógica (adaptadas del código anterior)
    def clasificar_categoria(self, oracion):
        habitual_keywords = ['todos los', 'cada', 'siempre', 'nunca', 'regularmente', 'mañanas', 'tardes']
        futuro_keywords = ['mañana', 'próxima semana', 'esta noche', 'el año próximo', 'en dos días']
        nomico_keywords = ['siempre', 'nunca', 'eterno', 'universal', 'refrán', 'dice', 'proverbio']

        if any(palabra in oracion.lower() for palabra in nomico_keywords) or re.search(r'\“.*\”', oracion) or 'dios' in oracion.lower():
            return "Presente Noómico"
        if any(palabra in oracion.lower() for palabra in futuro_keywords):
            return "Presente por Futuro"
        if any(palabra in oracion.lower() for palabra in habitual_keywords) or re.search(r'\b(?:los|lunes|martes|miércoles|jueves|viernes|sábado|domingo)s\b', oracion, flags=re.IGNORECASE):
            return "Presente Habitual"
        if 'ahora' in oracion.lower() or 'en este momento' in oracion.lower() or re.search(r'\b(?:estoy|estás|está|estamos|están)\b', oracion, flags=re.IGNORECASE):
            return "Presente Actual"
        return "Indeterminado"

    def reescribir_futuro_a_presente(self, oracion):
        conjugaciones = {
            r'é\b': 'o', r'ás\b': 'as', r'á\b': 'a',
            r'emos\b': 'emos', r'éis\b': 'éis', r'án\b': 'an'
        }
        for patron, reemplazo in conjugaciones.items():
            oracion = re.sub(patron, reemplazo, oracion, flags=re.IGNORECASE)
        return oracion

if __name__ == "__main__":
    root = tk.Tk()
    app = PresentacionApp(root)
    root.mainloop()
