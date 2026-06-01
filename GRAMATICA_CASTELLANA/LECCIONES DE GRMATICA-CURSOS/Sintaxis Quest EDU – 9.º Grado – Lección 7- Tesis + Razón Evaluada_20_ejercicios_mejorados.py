import time

# 📚 Lista de ejercicios
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
     "ejemplo": "Porque puede educar, pero también desinformar."}
]

elogios = [
    "✅ ¡Razón clara y lógica!",
    "🎯 ¡Tu tesis tiene fuerza!",
    "🌟 ¡Excelente justificación!",
    "👏 ¡Buena conexión entre postura y argumento!",
    "🧠 ¡Pensamiento argumentativo sólido!"
]

def mostrar_teoria():
    print("\n📘 LECCIÓN 7 – Tesis + Razón\n")
    print("Una tesis es una afirmación clara sobre un tema.")
    print("Debe ir acompañada de una razón que la justifique.\n")
    print("Usa conectores como:\n- porque\n- ya que\n- debido a\n")
    print("Ejemplo:\nTesis: La escuela debe tener biblioteca.")
    print("Razón: Porque fomenta la lectura y el pensamiento.")

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
    if puntos == 3:
        return "🏅 ¡Argumento sólido, bien estructurado!", puntos
    elif puntos == 2:
        return "✅ ¡Buena razón, podrías agregar más detalle!", puntos
    elif puntos == 1:
        return "⚠️ Tu razón tiene potencial, pero le falta estructura.", puntos
    else:
        return "❌ Falta conexión lógica o desarrollo en la respuesta.", puntos

def practicar_ejercicios():
    print("\n📝 PRACTICA DE LOS 20 EJERCICIOS CON RETROALIMENTACIÓN:\n")
    total = 0
    for i, ej in enumerate(ejercicios, 1):
        print(f"Ejercicio {i}:")
        print(f"Tesis: {ej['tesis']}")
        print(f"Ejemplo de razón: {ej['ejemplo']}")
        razon = input("👉 Escribe tu propia razón: ").strip()
        fb, puntos = evaluar_respuesta(razon)
        print(f"{fb} (Puntaje: {puntos}/3)\n")
        total += puntos
    print("📊 Evaluación final:")
    print(f"🌟 Puntaje acumulado: {total}/60")
    if total >= 50:
        print("🏅 ¡Nivel avanzado! Tus argumentos son sólidos y bien justificados.")
    elif total >= 35:
        print("👍 ¡Buen nivel! Puedes profundizar más tus razones.")
    else:
        print("📘 ¡Sigue practicando! Conectores y claridad harán tu pensamiento más fuerte.")

# 🎮 Menú principal
def menu():
    while True:
        print("\n🧠 Sintaxis Quest EDU – 9.º Grado – Lección 7: Tesis + Razón")
        print("1. Ver teoría 📘")
        print("2. Practicar los 20 ejercicios completos 📝")
        print("3. Salir 👋")
        opcion = input("👉 Elige una opción: ")
        if opcion == "1":
            mostrar_teoria()
        elif opcion == "2":
            practicar_ejercicios()
        elif opcion == "3":
            print("👋 ¡Gracias por argumentar con claridad y lógica!")
            break
        else:
            print("⚠️ Opción no válida. Intenta de nuevo.")

# 🚀 Ejecutar
if __name__ == "__main__":
    menu()
