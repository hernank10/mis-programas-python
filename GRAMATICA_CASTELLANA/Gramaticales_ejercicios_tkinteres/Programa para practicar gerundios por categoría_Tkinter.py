import tkinter as tk
from tkinter import messagebox
import random

# Datos
categorias = {
    "Instantaneidad": [
        "Estoy leyendo un libro fascinante.",
        "Te estoy buscando en la estación.",
        "Estoy preparando una ensalada.",
        "Estamos llegando al aeropuerto.",
        "Estoy escribiendo una carta urgente.",
        "Estamos escuchando música clásica.",
        "Estoy haciendo mi tarea ahora mismo.",
        "Estoy hablando con mi abuela.",
        "Estoy cerrando la puerta.",
        "Estoy viendo una película."
    ],
    "Duración de un acto": [
        "Estoy viviendo en Barcelona.",
        "Estoy trabajando en una empresa internacional.",
        "Estoy estudiando medicina.",
        "Estoy investigando sobre energías renovables.",
        "Estoy construyendo una cabaña en el bosque.",
        "Estoy pintando mi casa.",
        "Estoy escribiendo una novela.",
        "Estoy reparando mi coche.",
        "Estoy aprendiendo francés.",
        "Estoy enseñando a mis alumnos."
    ],
    "Repetición de un acto": [
        "Estoy disparando flechas al blanco.",
        "Estoy golpeando la puerta.",
        "Estoy aplaudiendo en el concierto.",
        "Estoy martillando clavos en la madera.",
        "Estoy barriendo el patio.",
        "Estoy tocando la guitarra repetidamente.",
        "Estoy lanzando piedras al río.",
        "Estoy tecleando en el ordenador.",
        "Estoy parpadeando rápido por el polvo.",
        "Estoy soplando burbujas."
    ],
    "Percepción de actos en proceso": [
        "Vi a mi hermano bailando en la fiesta.",
        "Oí a un perro ladrando en la noche.",
        "Encontré a María escribiendo poemas.",
        "Descubrí a Pedro durmiendo en clase.",
        "Vi al jardinero podando los árboles.",
        "Oí a los niños cantando en el patio.",
        "Sorprendí a Juan leyendo en la biblioteca.",
        "Encontré a Laura cocinando galletas.",
        "Vi a un artista pintando un mural.",
        "Oí al viento silbando entre los árboles."
    ],
    "Acciones simultáneas o modificadoras": [
        "Jaime entra al salón cantando.",
        "Marta cruzó la calle corriendo.",
        "Luis salió de casa silbando.",
        "El niño bajó la escalera saltando.",
        "El gato se acercó maullando.",
        "El soldado avanzó gritando órdenes.",
        "La maestra llegó sonriendo.",
        "Mi padre salió manejando rápido.",
        "El ciclista pedaleaba sonriendo.",
        "El chef cocinaba cantando."
    ],
    "Motivos de la acción principal": [
        "El soldado, viendo que era su hermano, bajó el arma.",
        "El profesor, recordando su primera clase, sonrió.",
        "El alumno, entendiendo el error, corrigió su examen.",
        "El conductor, percibiendo el peligro, frenó bruscamente.",
        "La madre, oyendo el llanto de su bebé, corrió a su cuna.",
        "El deportista, sabiendo su marca personal, aceleró.",
        "El anciano, reconociendo la voz, se alegró.",
        "El turista, comprendiendo las indicaciones, cambió de dirección.",
        "El guardia, observando movimientos extraños, llamó refuerzos.",
        "El científico, descubriendo un error, repitió el experimento."
    ],
    "Concesión, condición o causa": [
        "Estudiando tanto, aún fallé en el examen.",
        "Siendo tan tarde, no había taxis disponibles.",
        "Habiendo terminado la tarea, salimos a jugar.",
        "Estando cansado, continuó trabajando.",
        "Habiendo dormido poco, rindió bien en el maratón.",
        "Sabiendo la respuesta, no quiso intervenir.",
        "Trabajando juntos, lograron terminar el proyecto.",
        "Lloviendo fuerte, no salimos de casa.",
        "Estando enfermo, asistió a la reunión.",
        "Habiendo perdido el tren, tomamos un taxi."
    ]
}

class GerundioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Práctica de Gerundios")
        
        self.frame_inicio = tk.Frame(root)
        self.frame_menu = tk.Frame(root)
        self.frame_practica = tk.Frame(root)

        self.configurar_inicio()
        self.configurar_menu()
        self.configurar_practica()

        self.frame_inicio.pack()

    def configurar_inicio(self):
        tk.Label(self.frame_inicio, text="Bienvenido a la práctica de Gerundios", font=("Arial", 18)).pack(pady=20)
        tk.Label(self.frame_inicio, text="Instrucciones:\n- Elige una categoría.\n- Copia ejemplos.\n- Crea oraciones nuevas.\n- Cambia sujetos o verbos.\n- Subraya el gerundio con _guiones bajos_.", font=("Arial", 12)).pack(pady=20)
        tk.Button(self.frame_inicio, text="Comenzar", command=self.mostrar_menu).pack()

    def configurar_menu(self):
        tk.Label(self.frame_menu, text="Selecciona una categoría:", font=("Arial", 16)).pack(pady=10)
        self.lista_categorias = tk.Listbox(self.frame_menu, width=50)
        for cat in categorias.keys():
            self.lista_categorias.insert(tk.END, cat)
        self.lista_categorias.pack(pady=10)
        tk.Button(self.frame_menu, text="Ver Ejemplos y Practicar", command=self.mostrar_practica).pack()
        tk.Button(self.frame_menu, text="Salir", command=self.root.quit).pack(pady=10)

    def configurar_practica(self):
        self.label_categoria = tk.Label(self.frame_practica, text="", font=("Arial", 14))
        self.label_categoria.pack(pady=10)
        self.texto_ejemplo = tk.Text(self.frame_practica, height=10, width=60)
        self.texto_ejemplo.pack(pady=10)
        tk.Label(self.frame_practica, text="Escribe tu oración nueva aquí:", font=("Arial", 12)).pack()
        self.entry_oracion = tk.Entry(self.frame_practica, width=60)
        self.entry_oracion.pack(pady=5)
        tk.Button(self.frame_practica, text="Enviar oración", command=self.verificar_oracion).pack(pady=5)
        tk.Button(self.frame_practica, text="Volver al Menú", command=self.mostrar_menu).pack(pady=10)

    def mostrar_menu(self):
        self.frame_inicio.pack_forget()
        self.frame_practica.pack_forget()
        self.frame_menu.pack()

    def mostrar_practica(self):
        seleccion = self.lista_categorias.curselection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Por favor selecciona una categoría.")
            return
        self.categoria_actual = self.lista_categorias.get(seleccion)
        self.ejemplos_actuales = random.sample(categorias[self.categoria_actual], 5)
        
        self.texto_ejemplo.delete(1.0, tk.END)
        for ejemplo in self.ejemplos_actuales:
            self.texto_ejemplo.insert(tk.END, f"- {ejemplo}\n")
        
        self.label_categoria.config(text=f"Categoría: {self.categoria_actual}")
        self.frame_menu.pack_forget()
        self.frame_practica.pack()

    def verificar_oracion(self):
        oracion = self.entry_oracion.get()
        if "_" in oracion:
            messagebox.showinfo("¡Bien hecho!", "Has subrayado correctamente el gerundio.")
        else:
            messagebox.showwarning("Intenta mejorar", "Recuerda subrayar el gerundio usando _guiones bajos_.")
        self.entry_oracion.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = GerundioApp(root)
    root.mainloop()
