import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import random

class SpanishTrainerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Entrenador de Español GUI")
        self.root.geometry("800x600")
        
        # Base de datos de ejemplos
        self.ejemplos = [
            {"sentence": "¡Ganaron! 🎉", "quien": "", "verbo": "ganaron", "que": "", 
             "a_quien": "", "contexto": "cotidiano", "tiempo": "pasado", "complejidad": 1},
            # ... agregar todos los ejemplos aquí
        ]
        
        # Configurar estilo
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#F0F0F0')
        self.style.configure('TButton', font=('Arial', 10), padding=5)
        self.style.configure('TLabel', background='#F0F0F0', font=('Arial', 11))
        
        # Crear widgets principales
        self.create_main_menu()

    def create_main_menu(self):
        # Frame principal
        main_frame = ttk.Frame(self.root)
        main_frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        # Botones del menú
        ttk.Button(main_frame, text="📖 Tutorial", command=self.show_tutorial).pack(pady=10, fill='x')
        ttk.Button(main_frame, text="🧩 Practicar", command=self.start_practice).pack(pady=10, fill='x')
        ttk.Button(main_frame, text="🧠 Memorización", command=self.start_memorization).pack(pady=10, fill='x')
        ttk.Button(main_frame, text="✏️ Crear Ejemplos", command=self.create_example_window).pack(pady=10, fill='x')
        ttk.Button(main_frame, text="📚 Ver Ejemplos", command=self.view_examples).pack(pady=10, fill='x')
        ttk.Button(main_frame, text="🚪 Salir", command=self.root.quit).pack(pady=10, fill='x')

    def show_tutorial(self):
        tutorial_win = tk.Toplevel(self.root)
        tutorial_win.title("Tutorial Interactivo")
        
        slides = [
            ("👤 QUIÉN", "Sujeto que realiza la acción\nEj: 'El profesor' | 'La empresa'"),
            ("🎬 VERBO", "Acción principal\nEj: 'explicó' (pasado) | 'organizarán' (futuro)"),
            ("📦 QUÉ", "Objeto/contenido de la acción\nEj: 'los resultados' | 'un nuevo proyecto'"),
            ("🎯 A QUIÉN", "Destinatario o beneficiario\nEj: 'para estudiantes' | 'a las autoridades'"),
            ("🌟 EJEMPLO", "La biblioteca organizará\nun taller de escritura ✍️\npara jóvenes autores 🧑🎓")
        ]
        
        current_slide = 0
        slide_label = ttk.Label(tutorial_win, font=('Arial', 14), justify='center')
        slide_label.pack(padx=20, pady=20)
        
        def update_slide(delta):
            nonlocal current_slide
            current_slide = (current_slide + delta) % len(slides)
            title, content = slides[current_slide]
            slide_label.config(text=f"{title}\n\n{content}")
        
        ttk.Button(tutorial_win, text="Anterior", command=lambda: update_slide(-1)).pack(side='left', padx=10)
        ttk.Button(tutorial_win, text="Siguiente", command=lambda: update_slide(1)).pack(side='right', padx=10)
        
        update_slide(0)

    def start_practice(self):
        practice_win = tk.Toplevel(self.root)
        practice_win.title("Modo Práctica")
        
        ejemplo = random.choice(self.ejemplos)
        
        ttk.Label(practice_win, text=ejemplo['sentence'], font=('Arial', 12, 'bold')).pack(pady=10)
        
        entries = {}
        for component in ['quien', 'verbo', 'que', 'a_quien']:
            frame = ttk.Frame(practice_win)
            frame.pack(fill='x', padx=10, pady=5)
            
            ttk.Label(frame, text=f"{component.capitalize()}:").pack(side='left')
            entry = ttk.Entry(frame, width=30)
            entry.pack(side='right', expand=True)
            entries[component] = entry
        
        feedback_label = ttk.Label(practice_win, text="")
        feedback_label.pack(pady=10)
        
        def check_answers():
            correct = 0
            for component, entry in entries.items():
                user_answer = entry.get().strip().lower()
                correct_answer = ejemplo.get(component, "").lower()
                if user_answer == correct_answer:
                    entry.config(foreground='green')
                    correct += 1
                else:
                    entry.config(foreground='red')
            
            feedback_label.config(text=f"Correctas: {correct}/4")
            if correct == 4:
                feedback_label.config(foreground='green')
            else:
                feedback_label.config(foreground='red')
        
        ttk.Button(practice_win, text="Comprobar", command=check_answers).pack(pady=10)

    def start_memorization(self):
        mem_win = tk.Toplevel(self.root)
        mem_win.title("Modo Memorización")
        
        ejemplo = random.choice(self.ejemplos)
        
        ttk.Label(mem_win, text="Reconstruye la frase completa:", font=('Arial', 12)).pack(pady=10)
        
        components_frame = ttk.Frame(mem_win)
        components_frame.pack()
        
        ttk.Label(components_frame, text="👤 QUIÉN:").grid(row=0, column=0, sticky='w')
        ttk.Label(components_frame, text=ejemplo['quien'] or "[Por determinar]").grid(row=0, column=1)
        
        ttk.Label(components_frame, text="🎬 VERBO:").grid(row=1, column=0, sticky='w')
        ttk.Label(components_frame, text=ejemplo['verbo']).grid(row=1, column=1)
        
        ttk.Label(components_frame, text="📦 QUÉ:").grid(row=2, column=0, sticky='w')
        ttk.Label(components_frame, text=ejemplo['que'] or "[Por determinar]").grid(row=2, column=1)
        
        ttk.Label(components_frame, text="🎯 A QUIÉN:").grid(row=3, column=0, sticky='w')
        ttk.Label(components_frame, text=ejemplo['a_quien'] or "[Por determinar]").grid(row=3, column=1)
        
        entry = ttk.Entry(mem_win, width=50)
        entry.pack(pady=10)
        
        feedback_label = ttk.Label(mem_win, text="")
        feedback_label.pack()
        
        def check_sentence():
            user_sentence = entry.get().strip().lower()
            original = ejemplo['sentence'].lower()
            if user_sentence == original:
                feedback_label.config(text="¡Correcto! 🎉", foreground='green')
            else:
                feedback_label.config(text=f"Original: {ejemplo['sentence']}", foreground='red')
        
        ttk.Button(mem_win, text="Comprobar", command=check_sentence).pack(pady=10)

    def create_example_window(self):
        create_win = tk.Toplevel(self.root)
        create_win.title("Crear Nuevo Ejemplo")
        
        fields = {}
        components = ['quien', 'verbo', 'que', 'a_quien', 'contexto', 'tiempo']
        
        for i, component in enumerate(components):
            frame = ttk.Frame(create_win)
            frame.grid(row=i, column=0, sticky='ew', padx=10, pady=5)
            
            label = ttk.Label(frame, text=f"{component.capitalize()}:")
            label.pack(side='left')
            
            entry = ttk.Entry(frame)
            entry.pack(side='right', expand=True, fill='x')
            fields[component] = entry
        
        ttk.Button(create_win, text="Guardar", command=lambda: self.save_example(fields)).grid(row=6, column=0, pady=10)

    def save_example(self, fields):
        # Validación y guardado de ejemplo
        if len(self.ejemplos) >= 100:
            messagebox.showwarning("Límite alcanzado", "¡Base de datos llena! Máximo 100 ejemplos.")
            return
        
        new_example = {key: entry.get().strip() for key, entry in fields.items()}
        new_example['sentence'] = f"{new_example['quien']} {new_example['verbo']} {new_example['que']} {new_example['a_quien']}"
        self.ejemplos.append(new_example)
        messagebox.showinfo("Éxito", "Ejemplo guardado correctamente ✅")

    def view_examples(self):
        view_win = tk.Toplevel(self.root)
        view_win.title("Ejemplos Guardados")
        
        scroll = scrolledtext.ScrolledText(view_win, width=80, height=20)
        scroll.pack(padx=10, pady=10)
        
        for idx, ej in enumerate(self.ejemplos, 1):
            scroll.insert('end', f"{idx}. {ej['sentence']}\n")
        
        scroll.config(state='disabled')

if __name__ == "__main__":
    root = tk.Tk()
    app = SpanishTrainerApp(root)
    root.mainloop()
