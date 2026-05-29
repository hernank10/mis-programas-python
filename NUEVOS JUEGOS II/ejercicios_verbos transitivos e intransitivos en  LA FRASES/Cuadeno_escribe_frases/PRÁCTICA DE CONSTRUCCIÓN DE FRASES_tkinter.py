import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import random

class SentencePracticeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Práctica de Construcción de Frases")
        self.root.geometry("800x600")
        
        # Base de datos de frases
        self.frases = [
            {
                "español": "El gobierno entregó a los agricultores un paquete de subsidios para mejorar la producción.",
                "componentes": {
                    "quien": "El gobierno",
                    "verbo": "entregó",
                    "a_quien": "a los agricultores",
                    "que": "un paquete de subsidios para mejorar la producción"
                },
                "ingles": "The government gave farmers a subsidy package to improve production."
            },
            # Agregar más frases aquí...
        ]
        
        self.current_sentence = None
        self.create_widgets()
    
    def create_widgets(self):
        # Frame principal
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Botones del menú principal
        ttk.Button(self.main_frame, text="Reglas y Componentes", 
                  command=self.show_rules).pack(pady=5, fill=tk.X)
        ttk.Button(self.main_frame, text="Practicar Orden Correcto", 
                  command=self.practice_order).pack(pady=5, fill=tk.X)
        ttk.Button(self.main_frame, text="Traducir Frases", 
                  command=self.practice_translation).pack(pady=5, fill=tk.X)
        ttk.Button(self.main_frame, text="Reescribir Frases", 
                  command=self.practice_rewrite).pack(pady=5, fill=tk.X)
        ttk.Button(self.main_frame, text="Salir", 
                  command=self.root.quit).pack(pady=5, fill=tk.X)
        
        # Frame para contenido dinámico
        self.content_frame = ttk.Frame(self.main_frame)
        self.content_frame.pack(fill=tk.BOTH, expand=True, pady=20)
    
    def clear_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
    
    def show_rules(self):
        self.clear_content()
        
        rules_text = """REGLAS PARA CONSTRUCCIÓN DE FRASES:
        
1. Orden recomendado:
   QUIÉN + VERBO + A QUIÉN/PARA QUIÉN (corto) + QUÉ (largo)
   
2. El complemento indirecto (A QUIÉN) debe colocarse primero si es más corto que el directo
   
3. En inglés, usar preposiciones 'to' o 'for' para el complemento indirecto
   
4. Mantener la estructura paralela en traducciones
   
Ejemplo correcto:
   [El profesor] [explicó] [a los estudiantes] [los conceptos avanzados de física cuántica]"""
        
        rules_area = scrolledtext.ScrolledText(self.content_frame, wrap=tk.WORD, height=10)
        rules_area.insert(tk.INSERT, rules_text)
        rules_area.pack(fill=tk.BOTH, expand=True)
        rules_area.configure(state='disabled')
    
    def practice_order(self):
        self.clear_content()
        self.current_sentence = random.choice(self.frases)
        
        ttk.Label(self.content_frame, text="Ordena los componentes:", 
                 font=('Arial', 12, 'bold')).pack(pady=10)
        
        components = [
            self.current_sentence["componentes"]["quien"],
            self.current_sentence["componentes"]["verbo"],
            self.current_sentence["componentes"]["a_quien"],
            self.current_sentence["componentes"]["que"]
        ]
        random.shuffle(components)
        
        for comp in components:
            ttk.Label(self.content_frame, text=f"• {comp}").pack()
            
        self.answer_entry = ttk.Entry(self.content_frame, width=80)
        self.answer_entry.pack(pady=20)
        
        ttk.Button(self.content_frame, text="Verificar", 
                  command=self.check_order).pack()
    
    def check_order(self):
        user_answer = self.answer_entry.get().strip()
        correct_answer = f'{self.current_sentence["componentes"]["quien"]} ' \
                        f'{self.current_sentence["componentes"]["verbo"]} ' \
                        f'{self.current_sentence["componentes"]["a_quien"]} ' \
                        f'{self.current_sentence["componentes"]["que"]}'
        
        if user_answer.lower() == correct_answer.lower():
            messagebox.showinfo("Resultado", "✅ ¡Orden correcto!")
        else:
            messagebox.showerror("Resultado", 
                               f"❌ Mejor opción:\n{correct_answer}")
    
    def practice_translation(self):
        self.clear_content()
        self.current_sentence = random.choice(self.frases)
        
        ttk.Label(self.content_frame, text="Traduce al inglés:", 
                 font=('Arial', 12, 'bold')).pack(pady=10)
        ttk.Label(self.content_frame, 
                 text=self.current_sentence["español"]).pack(pady=5)
        
        self.translation_entry = ttk.Entry(self.content_frame, width=80)
        self.translation_entry.pack(pady=20)
        
        ttk.Button(self.content_frame, text="Verificar Traducción", 
                  command=self.check_translation).pack()
    
    def check_translation(self):
        user_translation = self.translation_entry.get().strip()
        correct_translation = self.current_sentence["ingles"]
        
        if user_translation.lower() == correct_translation.lower():
            messagebox.showinfo("Resultado", "✅ ¡Traducción correcta!")
        else:
            messagebox.showerror("Resultado", 
                                f"❌ Traducción sugerida:\n{correct_translation}")
    
    def practice_rewrite(self):
        self.clear_content()
        self.current_sentence = random.choice(self.frases)
        
        # Crear versión desordenada
        components = [
            self.current_sentence["componentes"]["quien"],
            self.current_sentence["componentes"]["verbo"],
            self.current_sentence["componentes"]["que"],
            self.current_sentence["componentes"]["a_quien"]
        ]
        bad_sentence = " ".join(components)
        
        ttk.Label(self.content_frame, text="Reescribe la frase:", 
                 font=('Arial', 12, 'bold')).pack(pady=10)
        ttk.Label(self.content_frame, text=bad_sentence).pack(pady=5)
        
        self.rewrite_entry = ttk.Entry(self.content_frame, width=80)
        self.rewrite_entry.pack(pady=20)
        
        ttk.Button(self.content_frame, text="Verificar", 
                  command=self.check_rewrite).pack()
    
    def check_rewrite(self):
        user_answer = self.rewrite_entry.get().strip()
        correct_answer = f'{self.current_sentence["componentes"]["quien"]} ' \
                         f'{self.current_sentence["componentes"]["verbo"]} ' \
                         f'{self.current_sentence["componentes"]["a_quien"]} ' \
                         f'{self.current_sentence["componentes"]["que"]}'
        
        if user_answer.lower() == correct_answer.lower():
            messagebox.showinfo("Resultado", "✅ ¡Estructura mejorada!")
        else:
            messagebox.showerror("Resultado", 
                                f"❌ Versión óptima:\n{correct_answer}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SentencePracticeApp(root)
    root.mainloop()
