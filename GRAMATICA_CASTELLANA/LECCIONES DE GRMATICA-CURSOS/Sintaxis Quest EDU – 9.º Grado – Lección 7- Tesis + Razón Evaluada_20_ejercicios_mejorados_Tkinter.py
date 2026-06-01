import tkinter as tk
from tkinter import messagebox, ttk

# 📚 Ejercicios con modelos
ejercicios = [
    {"tesis": "Las tareas escolares deben tener un propósito claro", 
     "ejemplo": "Porque refuerzan lo aprendido y no solo ocupan tiempo."},
    {"tesis": "El reciclaje debe enseñarse desde primaria", 
     "ejemplo": "Ya que promueve conciencia ambiental desde temprana edad."},
    {"tesis": "La lectura diaria mejora el desempeño escolar", 
     "ejemplo": "Porque desarrolla vocabulario y comprensión lectora."},
    {"tesis": "Los teléfonos en clase deben estar regulados", 
     "ejemplo": "Ya que pueden distraer si se usan sin control."},
    {"tesis": "Los videojuegos pueden ser positivos", 
     "ejemplo": "Porque estimulan coordinación y toma de decisiones."},
    {"tesis": "La puntualidad debe enseñarse como valor escolar", 
     "ejemplo": "Debido a que fomenta responsabilidad y respeto por el tiempo."},
    {"tesis": "Las excursiones educativas son valiosas", 
     "ejemplo": "Porque permiten aprender en contextos reales."},
    {"tesis": "La alimentación saludable debe ser promovida", 
     "ejemplo": "Ya que mejora concentración y previene enfermedades."},
    {"tesis": "El arte urbano merece reconocimiento", 
     "ejemplo": "Porque expresa cultura e identidad social."},
    {"tesis": "El descanso entre clases es necesario", 
     "ejemplo": "Porque renueva la atención y evita el agotamiento."},
    {"tesis": "Los estudiantes deben respetar a sus compañeros", 
     "ejemplo": "Ya que el respeto crea buena convivencia."},
    {"tesis": "La historia es una materia clave en la educación", 
     "ejemplo": "Porque permite comprender el presente desde el pasado."},
    {"tesis": "El deporte debe formar parte del horario escolar", 
     "ejemplo": "Porque mejora la salud y fortalece valores."},
    {"tesis": "La escritura mejora el pensamiento crítico", 
     "ejemplo": "Ya que obliga a organizar ideas y reflexionar."},
    {"tesis": "Los estudiantes deben aprender economía básica", 
     "ejemplo": "Porque ayuda a tomar decisiones financieras responsables."},
    {"tesis": "La música estimula la memoria y concentración", 
     "ejemplo": "Porque activa áreas cognitivas importantes."},
    {"tesis": "Los profesores deben recibir apoyo emocional", 
     "ejemplo": "Ya que enfrentan retos y necesitan acompañamiento."},
    {"tesis": "Las actividades en grupo ayudan al aprendizaje", 
     "ejemplo": "Porque promueven colaboración e intercambio de ideas."},
    {"tesis": "El bullying debe tratarse con firmeza", 
     "ejemplo": "Debido a que daña la autoestima y salud emocional."},
    {"tesis": "La tecnología debe usarse con responsabilidad", 
     "ejemplo": "Porque puede educar, pero también desinformar."
    }
]

# 🎯 Evaluación de argumentos
def evaluar_respuesta(razon):
    razon = razon.strip().lower()
    puntos = 0
    conectores = ["porque", "ya que", "debido a"]
    if any(c in razon for c in conectores):
        puntos += 1
    if len(razon.split()) >= 5:
        puntos += 1
    if "." in razon or "," in razon:
        puntos += 1
    return puntos

# 🧠 Evaluar y mostrar retroalimentación
def evaluar():
    idx = ejercicio_var.get()
    razon = entrada.get("1.0", tk.END).strip()
    if not razon:
        messagebox.showwarning("Aviso", "Escribe una razón antes de evaluar.")
        return
    puntos = evaluar_respuesta(razon)
    if puntos == 3:
        fb = "🏅 ¡Argumento sólido, bien estructurado!"
    elif puntos == 2:
        fb = "✅ ¡Buena razón, podrías agregar más detalle!"
    elif puntos == 1:
        fb = "⚠️ Tu razón tiene potencial, pero le falta estructura."
    else:
        fb = "❌ Falta conexión lógica o desarrollo en la respuesta."
    resultado.set(f"Tesis: {ejercicios[idx]['tesis']}\nTu razón: {razon}\n\n{fb}\nPuntaje: {puntos}/3")

# 📘 Mostrar teoría
def ver_teoria():
    texto = (
        "📘 LECCIÓN 7 – Tesis + Razón\n\n"
        "Una tesis es una afirmación clara sobre un tema.\n"
        "Debe ir acompañada de una razón que la justifique.\n\n"
        "Usa conectores como:\n- porque\n- ya que\n- debido a\n\n"
        "Ejemplo:\n"
        "La escuela debe tener biblioteca, porque fomenta la lectura y el pensamiento."
    )
    messagebox.showinfo("Teoría", texto)

# ✍️ Argumentos propios
def escribir_propios():
    argumentos = []
    total = 0
    ventana = tk.Toplevel(root)
    ventana.title("Tus 5 argumentos")
    tk.Label(ventana, text="✍️ Escribe tus 5 tesis y razones").pack(pady=5)
    for i in range(5):
        frame = tk.Frame(ventana)
        frame.pack(pady=3)
        tk.Label(frame, text=f"Tesis {i+1}:").grid(row=0, column=0)
        t_entry = tk.Entry(frame, width=50)
        t_entry.grid(row=0, column=1)
        tk.Label(frame, text="Razón:").grid(row=1, column=0)
        r_entry = tk.Entry(frame, width=50)
        r_entry.grid(row=1, column=1)
        argumentos.append((t_entry, r_entry))
    def evaluar_propios():
        nonlocal total
        total = 0
        resultado = ""
        for i, (t, r) in enumerate(argumentos, 1):
            tesis = t.get().strip()
            razon = r.get().strip()
            pts = evaluar_respuesta(razon)
            total += pts
            resultado += f"{i}. {tesis} — {razon} (Puntaje: {pts}/3)\n"
        resultado += f"\nTotal: {total}/15"
        messagebox.showinfo("Resultados", resultado)
    tk.Button(ventana, text="Evaluar argumentos", command=evaluar_propios).pack(pady=5)

# 🖼️ Interfaz principal
root = tk.Tk()
root.title("Sintaxis Quest EDU – 9.º Grado – Lección 7")
root.geometry("750x600")

tk.Label(root, text="🧠 Lección 7: Tesis + Razón Argumentativa", font=("Arial", 16, "bold")).pack(pady=10)
tk.Button(root, text="📘 Ver teoría", command=ver_teoria).pack(pady=5)

frame_sel = tk.Frame(root)
frame_sel.pack()
tk.Label(frame_sel, text="Elige ejercicio:").grid(row=0, column=0, padx=5)
ejercicio_var = tk.IntVar()
ejercicio_menu = ttk.Combobox(frame_sel, textvariable=ejercicio_var, width=5, values=list(range(20)))
ejercicio_menu.grid(row=0, column=1)
ejercicio_menu.current(0)

modelo_var = tk.StringVar()
def mostrar_ejercicio(*args):
    idx = ejercicio_var.get()
    modelo_var.set(
        f"Tesis: {ejercicios[idx]['tesis']}\nEjemplo: {ejercicios[idx]['ejemplo']}"
    )
ejercicio_var.trace_add("write", mostrar_ejercicio)
mostrar_ejercicio()

tk.Label(root, textvariable=modelo_var, wraplength=700, font=("Arial", 12), justify="left").pack(pady=10)

tk.Label(root, text="✍️ Escribe tu razón:", font=("Arial", 12)).pack()
entrada = tk.Text(root, height=4, width=80)
entrada.pack()

tk.Button(root, text="🧠 Evaluar respuesta", command=evaluar).pack(pady=10)
resultado = tk.StringVar()
tk.Label(root, textvariable=resultado, wraplength=700, font=("Arial", 11), justify="left").pack(pady=10)

tk.Button(root, text="✍️ Escribir tus propios 5 argumentos", command=escribir_propios).pack(pady=5)
tk.Label(root, text="✨ Recuerda usar conectores como 'porque', 'ya que', 'debido a'...", fg="blue").pack(pady=
