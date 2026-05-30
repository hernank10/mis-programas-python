import tkinter as tk
from tkinter import messagebox
import random

ejercicios = [
    ("El mesero ______ la olla para servir la sopa.", "destapó"),
    ("El periodista ______ una gran conspiración en el gobierno.", "destapó"),
    ("El fontanero ______ la tubería obstruida.", "destapó"),
    ("La investigación ______ secretos ocultos de la empresa.", "destapó"),
    ("El arqueólogo ______ una tumba antigua.", "destapó")
]

class DestaparApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ejercicios de Destapar")
        self.root.configure(bg="white")
        
        self.correctas = 0
        self.incorrectas = 0
        self.current_exercise = None
        
        self.label_teoria = tk.Label(root, text="Ejercicios sobre el verbo 'destapar'", bg="white", font=("Arial", 12))
        self.label_teoria.pack(pady=5)
        
        self.btn_teoria = tk.Button(root, text="Ver Teoría", command=self.mostrar_teoria)
        self.btn_teoria.pack(pady=5)
        
        self.label_ejercicio = tk.Label(root, text="", bg="white", font=("Arial", 12))
        self.label_ejercicio.pack(pady=5)
        
        self.entry_respuesta = tk.Entry(root)
        self.entry_respuesta.pack(pady=5)
        
        self.btn_nuevo = tk.Button(root, text="Nuevo Ejercicio", command=self.nuevo_ejercicio)
        self.btn_nuevo.pack(pady=5)
        
        self.btn_verificar = tk.Button(root, text="Verificar", command=self.verificar_respuesta)
        self.btn_verificar.pack(pady=5)
        
        self.btn_progreso = tk.Button(root, text="Mostrar Progreso", command=self.mostrar_progreso)
        self.btn_progreso.pack(pady=5)
        
        self.btn_exportar = tk.Button(root, text="Exportar a Archivo", command=self.exportar_resultados)
        self.btn_exportar.pack(pady=5)
        
    def mostrar_teoria(self):
        teoria = "El verbo 'destapar' tiene usos rectos y figurados:\n- Uso recto: Quitar la tapa de algo (Ej: Destapó la botella).\n- Uso figurado: Revelar información oculta (Ej: Destaparon un escándalo)."
        messagebox.showinfo("Teoría", teoria)
    
    def nuevo_ejercicio(self):
        self.current_exercise = random.choice(ejercicios)
        self.label_ejercicio.config(text=self.current_exercise[0])
        self.entry_respuesta.delete(0, tk.END)
    
    def verificar_respuesta(self):
        if self.current_exercise:
            respuesta_usuario = self.entry_respuesta.get().strip().lower()
            if respuesta_usuario == self.current_exercise[1]:
                self.correctas += 1
                messagebox.showinfo("Resultado", "✅ Correcto!")
            else:
                self.incorrectas += 1
                messagebox.showerror("Resultado", f"❌ Incorrecto! La respuesta correcta es: {self.current_exercise[1]}")
    
    def mostrar_progreso(self):
        messagebox.showinfo("Progreso", f"✅ Correctas: {self.correctas}\n❌ Incorrectas: {self.incorrectas}")
    
    def exportar_resultados(self):
        with open("resultados.txt", "w") as file:
            file.write(f"Correctas: {self.correctas}\nIncorrectas: {self.incorrectas}\n")
        messagebox.showinfo("Exportación", "Resultados guardados en 'resultados.txt'")

if __name__ == "__main__":
    root = tk.Tk()
    app = DestaparApp(root)
    root.mainloop()
