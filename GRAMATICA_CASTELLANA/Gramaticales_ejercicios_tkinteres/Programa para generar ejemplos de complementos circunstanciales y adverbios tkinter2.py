import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, simpledialog
import json

# Datos iniciales (pueden cargarse desde un archivo JSON)
ejemplos = {
    "Complementos circunstanciales (con comas)": [],
    "Orden lógico (esencia + circunstancial)": [],
    "Orden psicológico (énfasis en el circunstancial)": [],
    "Adverbios vs. complementos circunstanciales": [],
    "Ejemplos mixtos (varios complementos)": []
}

# Cargar ejemplos desde archivo (si existe)
try:
    with open("ejemplos.json", "r", encoding="utf-8") as archivo:
        ejemplos = json.load(archivo)
except FileNotFoundError:
    pass

# Función para guardar ejemplos en JSON
def guardar_ejemplos():
    with open("ejemplos.json", "w", encoding="utf-8") as archivo:
        json.dump(ejemplos, archivo, ensure_ascii=False, indent=2)

# Teoría conceptual
TEORIA = """
➤ TEORÍA DE COMPLEMENTOS CIRCUNSTANCIALES

1. Definición:
   - Son modificadores del verbo que responden a: CÓMO, CUÁNDO, DÓNDE, POR QUÉ y PARA QUÉ.
   - Ej: "Estudiaremos *con dedicación* (modo), *hasta medianoche* (tiempo)".

2. Reglas clave:
   • Usar coma cuando el complemento va después del verbo.
   • Orden lógico: Primero lo esencial (sujeto + verbo), luego circunstanciales.
   • Orden psicológico: Empezar con el circunstancial para énfasis.

3. Adverbios vs. Complementos:
   ✔ Adverbios: Palabras breves (aquí, mañana, bien) SIN coma.
   ✘ Complementos: Frases largas CON coma.
"""

def mostrar_teoria():
    texto_ejemplos.delete(1.0, tk.END)
    texto_ejemplos.insert(tk.END, TEORIA, "teoria")

def mostrar_ejemplos(categoria):
    texto_ejemplos.delete(1.0, tk.END)
    texto_ejemplos.insert(tk.END, f"\n★ {categoria} ★\n", "titulo")
    for ejemplo in ejemplos[categoria][-100:]:  # Muestra últimos 100
        texto_ejemplos.insert(tk.END, f"- {ejemplo}\n", "ejemplo")

def crear_ejemplo():
    dialogo = tk.Toplevel()
    dialogo.title("Crear nuevo ejemplo")
    
    ttk.Label(dialogo, text="Categoría:").grid(row=0, column=0, padx=5, pady=5)
    combo_categorias = ttk.Combobox(dialogo, values=list(ejemplos.keys()))
    combo_categorias.grid(row=0, column=1, padx=5, pady=5)
    
    ttk.Label(dialogo, text="Ejemplo:").grid(row=1, column=0, padx=5, pady=5)
    entrada_ejemplo = ttk.Entry(dialogo, width=40)
    entrada_ejemplo.grid(row=1, column=1, padx=5, pady=5)
    
    def guardar():
        categoria = combo_categorias.get()
        ejemplo = entrada_ejemplo.get()
        
        if not categoria or not ejemplo:
            messagebox.showerror("Error", "¡Completa todos los campos!")
            return
        
        if len(ejemplos[categoria]) >= 100:
            messagebox.showerror("Límite", "¡Máximo 100 ejemplos por categoría!")
            return
            
        ejemplos[categoria].append(ejemplo)
        guardar_ejemplos()
        messagebox.showinfo("Éxito", "¡Ejemplo guardado correctamente!")
        dialogo.destroy()
    
    ttk.Button(dialogo, text="Guardar", command=guardar).grid(row=2, column=1, pady=10)
    ttk.Button(dialogo, text="Cancelar", command=dialogo.destroy).grid(row=2, column=0, pady=10)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Complementos Circunstanciales")
ventana.geometry("1000x700")
ventana.configure(bg="#f0f0f0")

# Estilos
estilo = ttk.Style()
estilo.configure("TButton", padding=6, font=('Arial', 10))
estilo.configure("TFrame", background="#f0f0f0")

# Marco principal
marco_principal = ttk.Frame(ventana)
marco_principal.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

# Marco de botones
marco_botones = ttk.Frame(marco_principal)
marco_botones.pack(side=tk.LEFT, fill=tk.Y, padx=10)

# Botones principales
botones_principales = [
    ("Teoría", mostrar_teoria),
    ("Crear Ejemplo", crear_ejemplo),
    *[(categoria, lambda c=categoria: mostrar_ejemplos(c)) for categoria in ejemplos.keys()],
    ("Salir", ventana.destroy)
]

for texto, comando in botones_principales:
    boton = ttk.Button(marco_botones, text=texto, command=comando, width=25)
    boton.pack(pady=5, fill=tk.X)

# Área de texto
texto_ejemplos = scrolledtext.ScrolledText(
    marco_principal,
    wrap=tk.WORD,
    font=('Arial', 11),
    padx=15,
    pady=15,
    width=70,
    height=25
)
texto_ejemplos.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Formatos de texto
texto_ejemplos.tag_configure("teoria", foreground="#2c3e50", font=('Arial', 11))
texto_ejemplos.tag_configure("titulo", foreground="#e74c3c", font=('Arial', 12, 'bold'))
texto_ejemplos.tag_configure("ejemplo", foreground="#34495e")

ventana.mainloop()
