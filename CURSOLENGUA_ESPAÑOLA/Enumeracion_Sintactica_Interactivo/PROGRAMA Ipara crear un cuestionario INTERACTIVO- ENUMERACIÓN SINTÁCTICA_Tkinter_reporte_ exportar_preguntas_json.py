import os
import json
import tkinter as tk
from tkinter import messagebox, simpledialog

# Rutas base
BASE_DIR = "./Enumeracion_Sintactica_Interactivo"
EJEMPLOS = os.path.join(BASE_DIR, "ejemplos_usuario")
os.makedirs(EJEMPLOS, exist_ok=True)

# Archivos JSON
ARCHIVOS_JSON = {
    "preguntas": os.path.join(BASE_DIR, "preguntas.json"),
    "progreso": os.path.join(BASE_DIR, "progreso.json"),
    "errores": os.path.join(BASE_DIR, "errores.json")
}

# Crear archivos JSON si no existen
if not os.path.exists(ARCHIVOS_JSON["preguntas"]):
    preguntas_default = [
        {
            "pregunta": "¿Qué función tiene la coma en una enumeración?",
            "opciones": ["Separar sujeto y verbo", "Separar elementos similares", "Separar oraciones completas", "Terminar la oración"],
            "respuesta": 1
        }
    ]
    with open(ARCHIVOS_JSON["preguntas"], 'w', encoding='utf-8') as f:
        json.dump(preguntas_default, f, ensure_ascii=False, indent=4)

for key in ["progreso", "errores"]:
    if not os.path.exists(ARCHIVOS_JSON[key]):
        with open(ARCHIVOS_JSON[key], 'w', encoding='utf-8') as f:
            json.dump([], f, ensure_ascii=False, indent=4)

# Guardar ejemplo validado
def guardar_ejemplo_validado(oracion):
    if "," not in oracion:
        messagebox.showerror("Validación", "La oración debe contener comas para ser válida.")
        return
    archivo = os.path.join(EJEMPLOS, "ejemplos.json")
    ejemplos = []
    if os.path.exists(archivo):
        with open(archivo, 'r', encoding='utf-8') as f:
            ejemplos = json.load(f)
    ejemplos.append(oracion)
    with open(archivo, 'w', encoding='utf-8') as f:
        json.dump(ejemplos, f, indent=4, ensure_ascii=False)
    messagebox.showinfo("Guardado", "Ejercicio guardado correctamente.")

# Guardar errores
def guardar_error(original, correccion):
    with open(ARCHIVOS_JSON["errores"], 'r+', encoding='utf-8') as f:
        errores = json.load(f)
        errores.append({"original": original, "correccion": correccion})
        f.seek(0)
        json.dump(errores, f, indent=4, ensure_ascii=False)

# Exportar reporte
def exportar_reporte():
    with open(ARCHIVOS_JSON["errores"], 'r', encoding='utf-8') as f:
        errores = json.load(f)
    with open(os.path.join(BASE_DIR, "reporte.txt"), 'w', encoding='utf-8') as f:
        for err in errores:
            f.write(f"Original: {err['original']}\nCorrección: {err['correccion']}\n\n")
    messagebox.showinfo("Reporte Exportado", "El reporte ha sido guardado en reporte.txt")

# Interfaz
class App:
    def __init__(self, root):
        self.root = root
        root.title("Enumeración Sintáctica Avanzada")

        tk.Button(root, text="➕ Crear ejercicio", command=self.crear_ejercicio).pack(pady=5)
        tk.Button(root, text="🛠 Corregir oraciones", command=self.corregir_oraciones).pack(pady=5)
        tk.Button(root, text="📤 Exportar reporte", command=exportar_reporte).pack(pady=5)
        tk.Button(root, text="❌ Salir", command=root.quit).pack(pady=5)

    def crear_ejercicio(self):
        oracion = simpledialog.askstring("Nuevo ejercicio", "Escribe una oración con enumeración:")
        if oracion:
            guardar_ejemplo_validado(oracion)

    def corregir_oraciones(self):
        oraciones = [
            "Los estudiantes, aprobaron matemáticas, ciencias y, literatura.",
            "Los doctores Pérez, Ramírez operaron, a Juan y a, Carlos."
        ]
        for i, oracion in enumerate(oraciones):
            correccion = simpledialog.askstring("Corrección", f"Corrige la oración {i+1}:\n{oracion}")
            if correccion:
                guardar_error(oracion, correccion)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
