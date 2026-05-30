import tkinter as tk
from tkinter import messagebox

class PunctuationPractice:
    def __init__(self, root):
        self.root = root
        self.root.title("Práctica de Puntuación")
        self.root.geometry("500x400")

        self.ejemplos = [
            # Guiones
            {"sin_puntuacion": "El acuerdo comercial entre México Estados Unidos y Canadá", 
             "correcto": "El acuerdo comercial entre México, Estados Unidos y Canadá."},
            
            # Signos de interrogación
            {"sin_puntuacion": "Que hora es", 
             "correcto": "¿Qué hora es?"},
            
            # Signos de exclamación
            {"sin_puntuacion": "Que sorpresa verte aquí", 
             "correcto": "¡Qué sorpresa verte aquí!"},
            
            # Paréntesis
            {"sin_puntuacion": "El autor Gabriel García Márquez es conocido por su obra Cien años de soledad", 
             "correcto": "El autor Gabriel García Márquez (es conocido por su obra Cien años de soledad)."},
            
            # Comillas
            {"sin_puntuacion": "Ella dijo No quiero ir a la fiesta", 
             "correcto": "Ella dijo: \"No quiero ir a la fiesta\"."},
            
            # Puntos suspensivos
            {"sin_puntuacion": "No sé qué decir", 
             "correcto": "No sé qué decir..."},
            
            # Guiones cortos
            {"sin_puntuacion": "El problema es económico político y social", 
             "correcto": "El problema es económico-político y social."},
            
            # Signos de interrogación y exclamación
            {"sin_puntuacion": "De verdad te gusta", 
             "correcto": "¿De verdad te gusta?"},
            
            # Signos de exclamación y puntos suspensivos
            {"sin_puntuacion": "No me lo puedo creer", 
             "correcto": "¡No me lo puedo creer!"},
            
            # Paréntesis y comillas
            {"sin_puntuacion": "El término entre comillas inteligencia artificial es muy amplio", 
             "correcto": "El término (entre comillas) \"inteligencia artificial\" es muy amplio."},
            
            # Puntos suspensivos y signos de exclamación
            {"sin_puntuacion": "No puede ser", 
             "correcto": "¡No puede ser!"},
            
            # Guiones cortos y comillas
            {"sin_puntuacion": "Es un problema económico político y cultural", 
             "correcto": "Es un problema económico-político y cultural."},
        ]

        self.current_example = 0

        self.create_widgets()

    def create_widgets(self):
        # Texto para instrucciones
        self.instructions_label = tk.Label(self.root, text="Practica con los signos de puntuación. Corrige la oración.", font=("Arial", 14))
        self.instructions_label.pack(pady=20)

        # Mostrar ejemplo
        self.example_label = tk.Label(self.root, text=f"Ejemplo: {self.ejemplos[self.current_example]['sin_puntuacion']}", font=("Arial", 12))
        self.example_label.pack(pady=20)

        # Entrada de usuario
        self.user_input = tk.Entry(self.root, font=("Arial", 12), width=50)
        self.user_input.pack(pady=20)

        # Botón para verificar la respuesta
        self.check_button = tk.Button(self.root, text="Verificar respuesta", font=("Arial", 12), command=self.check_answer)
        self.check_button.pack(pady=20)

    def check_answer(self):
        user_answer = self.user_input.get().strip()
        correct_answer = self.ejemplos[self.current_example]['correcto']

        if user_answer == correct_answer:
            messagebox.showinfo("Correcto", "¡Respuesta correcta!")
        else:
            messagebox.showerror("Incorrecto", f"Respuesta incorrecta. La respuesta correcta es: {correct_answer}")

        # Avanzar al siguiente ejercicio
        self.current_example += 1
        if self.current_example < len(self.ejemplos):
            self.update_example()
        else:
            messagebox.showinfo("¡Fin!", "¡Has completado todos los ejercicios!")
            self.root.quit()

    def update_example(self):
        self.example_label.config(text=f"Ejemplo: {self.ejemplos[self.current_example]['sin_puntuacion']}")
        self.user_input.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = PunctuationPractice(root)
    root.mainloop()
