import json
import tkinter as tk
from tkinter import simpledialog, messagebox, scrolledtext

# Lista de ejercicios con ejemplos y respuestas modelo
EJERCICIOS = [
    {"titulo": "Forme los femeninos de una serie de sustantivos.", "ejemplo": "Ej: el león → la leona", "modelo": "el doctor → la doctora"},
    {"titulo": "Separe sujeto y predicado.", "ejemplo": "Ej: El niño juega en el parque → sujeto: El niño / predicado: juega en el parque", "modelo": "Mi hermana cocina galletas → sujeto: Mi hermana / predicado: cocina galletas"},
    {"titulo": "Escriba la familia de palabras del sustantivo 'flor'.", "ejemplo": "Ej: flor, florero, florista, florido", "modelo": "flor, floral, florecer, floreado"},
    {"titulo": "Determine cuántos fonemas y cuántas letras tienen las palabras de la serie.", "ejemplo": "Ej: casa → 4 letras, 4 fonemas", "modelo": "niño → 4 letras, 4 fonemas"},
    {"titulo": "Señale los complementos del sujeto.", "ejemplo": "Ej: El gato negro de mi vecina → núcleo: gato / complementos: negro, de mi vecina", "modelo": "La niña rubia con trenzas → núcleo: niña / complementos: rubia, con trenzas"},
    {"titulo": "Señale la función de los siguientes grupos.", "ejemplo": "Ej: en el jardín → complemento circunstancial de lugar", "modelo": "por la tarde → complemento circunstancial de tiempo"},
    {"titulo": "Forme el plural de los siguientes grupos sustantivos.", "ejemplo": "Ej: el árbol frondoso → los árboles frondosos", "modelo": "la casa blanca → las casas blancas"},
    {"titulo": "Extraiga los sustantivos abstractos.", "ejemplo": "Ej: La alegría, la bondad, la tristeza", "modelo": "La inteligencia, la amistad, la justicia"},
    {"titulo": "Enuncie la regla de los verbos terminados en '-bir'.", "ejemplo": "Ej: Se escriben con 'b' todos los verbos terminados en '-bir', excepto hervir, servir y vivir", "modelo": "Los verbos en '-bir' llevan 'b', salvo excepciones como hervir, servir y vivir"},
    {"titulo": "Señale los núcleos de los grupos subrayados.", "ejemplo": "Ej: El coche rojo → núcleo: coche", "modelo": "Los niños alegres → núcleo: niños"},
    {"titulo": "Extraiga del texto los adjetivos relacionales.", "ejemplo": "Ej: escolar, laboral, presidencial", "modelo": "infantil, cultural, profesional"},
    {"titulo": "De la siguiente lista de adjetivos y verbos derive sustantivos abstractos.", "ejemplo": "Ej: feliz → felicidad; crear → creación", "modelo": "generoso → generosidad; leer → lectura"}
]

RESPUESTAS_USUARIO = []

# Guardar en archivo JSON
def guardar_respuestas():
    with open('respuestas_ejercicios.json', 'w', encoding='utf-8') as f:
        json.dump(RESPUESTAS_USUARIO[:100], f, indent=4, ensure_ascii=False)

# Interfaz gráfica con Tkinter
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Ejercicios de Lengua")

        self.lista = tk.Listbox(root, width=70)
        for i, ejercicio in enumerate(EJERCICIOS):
            self.lista.insert(tk.END, f"{i+1}. {ejercicio['titulo']}")
        self.lista.pack(padx=10, pady=10)

        self.boton_ver = tk.Button(root, text="Seleccionar ejercicio", command=self.ver_ejercicio)
        self.boton_ver.pack(pady=5)

        self.boton_guardar = tk.Button(root, text="Guardar respuestas", command=self.guardar_datos)
        self.boton_guardar.pack(pady=5)

        self.boton_ver_respuestas = tk.Button(root, text="Ver respuestas guardadas", command=self.ver_respuestas)
        self.boton_ver_respuestas.pack(pady=5)

    def ver_ejercicio(self):
        idx = self.lista.curselection()
        if not idx:
            messagebox.showwarning("Aviso", "Seleccione un ejercicio.")
            return

        ejercicio = EJERCICIOS[idx[0]]
        mensaje = f"Ejercicio: {ejercicio['titulo']}\n\nEjemplo: {ejercicio['ejemplo']}\nModelo: {ejercicio['modelo']}"
        respuesta = simpledialog.askstring("Respuesta", mensaje + "\n\nEscriba una respuesta similar:")
        if respuesta:
            RESPUESTAS_USUARIO.append({"titulo": ejercicio['titulo'], "respuesta": respuesta})
            messagebox.showinfo("✔", "Respuesta registrada.")

    def guardar_datos(self):
        guardar_respuestas()
        messagebox.showinfo("✔", "Respuestas guardadas correctamente.")

    def ver_respuestas(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Respuestas guardadas")
        texto = scrolledtext.ScrolledText(ventana, width=80, height=20)
        texto.pack(padx=10, pady=10)
        for r in RESPUESTAS_USUARIO:
            texto.insert(tk.END, f"- {r['titulo']}: {r['respuesta']}\n")

# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
