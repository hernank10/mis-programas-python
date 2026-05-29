import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import json
import random
import os

MAX_EJEMPLOS = 100
ARCHIVO_EJEMPLOS = "ejemplos_guardados.json"

class CDPracticaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🧠 Práctica de Complemento Directo")
        self.root.geometry("600x520")
        self.estilo()
        self.ejemplos_guardados = self.cargar_ejemplos()
        self.ejemplos_base = [
            ("Leí un libro interesante.", "un libro interesante"),
            ("Cocinamos una paella deliciosa.", "una paella deliciosa"),
            ("Ella escribió una carta larga.", "una carta larga"),
            ("Compré un regalo para mi madre.", "un regalo"),
            ("Pintaron la casa de azul.", "la casa"),
            ("Escucharon una canción alegre.", "una canción alegre"),
            ("Perdiste las llaves del coche.", "las llaves del coche"),
            ("Rompimos el vaso sin querer.", "el vaso"),
            ("Encontré una moneda antigua.", "una moneda antigua"),
            ("Bebí un jugo de naranja.", "un jugo de naranja"),
            ("Vi la película completa.", "la película completa"),
            ("Escribí una nota rápida.", "una nota rápida"),
            ("Tomé una decisión importante.", "una decisión importante"),
            ("Compraron una bicicleta nueva.", "una bicicleta nueva"),
            ("Limpié la mesa.", "la mesa"),
            ("Leímos el periódico.", "el periódico"),
            ("Adoptaron un cachorro.", "un cachorro"),
            ("Pinté la pared.", "la pared"),
            ("Rompieron el silencio.", "el silencio"),
            ("Tradujeron el texto.", "el texto"),
            ("Canté una canción.", "una canción"),
            ("Hice una pausa.", "una pausa"),
            ("Le regalé un libro.", "un libro"),
            ("Vendieron el coche.", "el coche"),
            ("Ganamos el partido.", "el partido"),
            ("Dibujó un paisaje.", "un paisaje"),
            ("Organizaron la fiesta.", "la fiesta"),
            ("Describí la escena.", "la escena"),
            ("Escribimos un poema.", "un poema"),
            ("Revisé el correo.", "el correo"),
            ("Tomaron la decisión.", "la decisión"),
            ("Compraste una camisa.", "una camisa"),
            ("Pagamos la cuenta.", "la cuenta"),
            ("Envié el paquete.", "el paquete"),
            ("Visitamos el museo.", "el museo"),
            ("Fotografié el paisaje.", "el paisaje"),
            ("Abrí la puerta.", "la puerta"),
            ("Cerramos la ventana.", "la ventana"),
            ("Acaricié al gato.", "al gato"),
            ("Vimos el amanecer.", "el amanecer"),
            ("Escuché el mensaje.", "el mensaje"),
            ("Desayuné pan con queso.", "pan con queso"),
            ("Bebieron café caliente.", "café caliente"),
            ("Prepararon la cena.", "la cena"),
            ("Limpió el piso.", "el piso"),
            ("Rompiste la promesa.", "la promesa"),
            ("Estudiamos la lección.", "la lección"),
            ("Jugamos un partido.", "un partido"),
            ("Ayudé a mi hermano.", "a mi hermano"),
            ("Escogí una película.", "una película"),
            ("Reparé el reloj.", "el reloj")
        ]

        self.menu_principal()

    def estilo(self):
        estilo = ttk.Style()
        estilo.configure("TButton", font=("Arial", 12), padding=10)
        estilo.configure("TLabel", font=("Arial", 14))

    def cargar_ejemplos(self):
        if os.path.exists(ARCHIVO_EJEMPLOS):
            with open(ARCHIVO_EJEMPLOS, "r", encoding="utf-8") as f:
                return json.load(f)
        return []

    def guardar_ejemplos(self):
        with open(ARCHIVO_EJEMPLOS, "w", encoding="utf-8") as f:
            json.dump(self.ejemplos_guardados, f, ensure_ascii=False, indent=2)

    def menu_principal(self):
        ttk.Label(self.root, text="Complemento Directo - Práctica").pack(pady=10)

        botones = [
            ("📖 Ver teoría", self.ver_teoria),
            ("✅ Practicar modo corrección", self.modo_correccion),
            ("➕ Crear nuevo ejemplo", self.crear_ejemplo),
            ("🔁 Practicar ejemplos guardados", self.practicar_guardados),
            ("🚪 Salir", self.root.quit)
        ]

        for texto, comando in botones:
            ttk.Button(self.root, text=texto, command=comando, width=40).pack(pady=5)

    def ver_teoria(self):
        teoria = (
            "El complemento directo (CD), también llamado objeto directo,\n"
            "es la parte de la oración que recibe directamente la acción del verbo.\n\n"
            "Ejemplo: 'Ha fotografiado las nubes' → CD: 'las nubes'.\n"
            "Se detecta preguntando ¿qué...? al verbo."
        )
        messagebox.showinfo("Teoría", teoria)

    def modo_correccion(self):
        oracion, cd = random.choice(self.ejemplos_base)
        respuesta = simpledialog.askstring("Modo corrección", f"¿Cuál es el complemento directo en:\n\n{oracion}")
        if not respuesta:
            messagebox.showinfo("Resultado", "No escribiste ninguna respuesta.")
        elif respuesta.strip().lower() == cd.lower():
            messagebox.showinfo("Resultado", "✅ ¡Correcto!")
        else:
            messagebox.showwarning("Resultado", f"❌ Incorrecto. La respuesta correcta era: {cd}")

    def crear_ejemplo(self):
        if len(self.ejemplos_guardados) >= MAX_EJEMPLOS:
            messagebox.showerror("Límite alcanzado", "Ya tienes 100 ejemplos guardados.")
            return

        oracion = simpledialog.askstring("Nuevo ejemplo", "Escribe una oración con complemento directo:")
        if not oracion or len(oracion.split()) < 3:
            messagebox.showerror("Error", "La oración debe tener al menos 3 palabras.")
            return

        cd = simpledialog.askstring("Complemento directo", "¿Cuál es el CD en la oración?")
        if not cd or cd.lower() not in oracion.lower():
            messagebox.showerror("Error", "El CD debe estar contenido en la oración.")
            return

        self.ejemplos_guardados.append({"oracion": oracion, "cd": cd})
        self.guardar_ejemplos()
        messagebox.showinfo("Guardado", "Ejemplo guardado exitosamente.")

    def practicar_guardados(self):
        if not self.ejemplos_guardados:
            messagebox.showwarning("Sin ejemplos", "No hay ejemplos guardados aún.")
            return

        ejemplo = random.choice(self.ejemplos_guardados)
        respuesta = simpledialog.askstring("Ejemplo guardado", f"Oración:\n{ejemplo['oracion']}\n\n¿Cuál es el CD?")
        if not respuesta:
            messagebox.showinfo("Resultado", "No escribiste ninguna respuesta.")
        elif respuesta.strip().lower() == ejemplo['cd'].lower():
            messagebox.showinfo("Resultado", "✅ ¡Correcto!")
        else:
            messagebox.showwarning("Resultado", f"❌ Incorrecto. El CD era: {ejemplo['cd']}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CDPracticaApp(root)
    root.mainloop()
