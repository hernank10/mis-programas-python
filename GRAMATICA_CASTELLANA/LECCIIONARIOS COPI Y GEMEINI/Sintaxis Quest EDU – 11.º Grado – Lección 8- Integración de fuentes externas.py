import random

# 📘 Teoría
teoria = """
📘 LECCIÓN 8 – ¿CÓMO INTEGRAR VOCES EXTERNAS A NUESTRA ARGUMENTACIÓN?

Cuando usamos una idea externa en un texto argumentativo, debemos:

1️⃣ Introducirla → ¿Quién lo dijo? ¿Dónde?
2️⃣ Integrarla con conectores → según, como afirma, en palabras de...
3️⃣ Comentarla → ¿Qué aporta? ¿Cómo conecta con nuestra tesis?
4️⃣ Mantener nuestra voz dominante → que sea apoyo, no reemplazo

🎯 Ejemplo:
"El pensamiento crítico es esencial en la educación.
Como afirma Paulo Freire, 'leer es también reescribir lo leído'.
Esa idea refuerza que interpretar y posicionarse son parte del aprendizaje reflexivo."
"""

# 📚 Ejemplos guiados
ejemplos = [
    "La participación juvenil fortalece la democracia escolar.\nComo señala la UNESCO, 'la educación debe formar ciudadanos activos'. Esta cita enfatiza que enseñar no es solo transmitir contenidos, sino crear espacios de acción.",
    "La lectura crítica transforma la forma en que pensamos.\nSegún Daniel Cassany, entender un texto requiere 'dialogar con sus ideas'. Esto muestra que el lector no solo recibe, sino que responde y construye.",
    "El arte debe estar presente en todas las áreas del saber.\nEn palabras de Leonardo da Vinci, 'la pintura es una forma de pensamiento silencioso'. Este enfoque valida al arte como lenguaje intelectual, no solo emocional."
]

# 📝 20 tesis para insertar citas y comentarios
temas = [
    "La poesía puede ser una herramienta educativa.",
    "Aprender otro idioma amplía la visión del mundo.",
    "La filosofía ayuda a pensar con profundidad.",
    "La educación ambiental debe ser prioritaria.",
    "Las redes sociales pueden formar ciudadanos críticos.",
    "La escritura creativa mejora la comunicación emocional.",
    "Estudiar historia forma conciencia social.",
    "El cine puede enseñar valores éticos.",
    "Leer literatura clásica ayuda a entender la sociedad actual.",
    "Las salidas pedagógicas conectan teoría con experiencia.",
    "El humor en clase mejora el clima de aprendizaje.",
    "Los adolescentes pueden enseñar entre ellos.",
    "La tecnología educativa transforma la enseñanza.",
    "La música desarrolla sensibilidad y concentración.",
    "El pensamiento argumentativo debe enseñarse desde primaria.",
    "La participación democrática fortalece la escuela.",
    "Las ciencias sociales ayudan a entender el mundo.",
    "La escritura crítica permite posicionarse frente al mundo.",
    "El arte estimula la reflexión ética y estética.",
    "La filosofía potencia el pensamiento autónomo."
]

elogios = [
    "🌟 ¡La cita enriquece tu argumento!",
    "✅ ¡Bien integrada y comentada!",
    "👏 ¡Excelente conexión entre voz externa y postura propia!",
    "🧠 ¡Tu párrafo tiene solidez intelectual!",
]

# 📘 Mostrar teoría
def mostrar_teoria():
    print(teoria)

# 📚 Mostrar ejemplos guiados
def mostrar_ejemplos():
    print("\n📚 EJEMPLOS CON CITA + COMENTARIO:")
    for ej in ejemplos:
        print(f"📝 {ej}\n")

# 📝 Practicar con inserción de cita
def practicar_citas():
    print("\n📝 AGREGA UNA CITA Y COMENTARIO A CADA TESIS:")
    total = 0
    for i, frase in enumerate(temas, 1):
        print(f"\n{str(i).zfill(2)}. Tesis: {frase}")
        cita = input("👉 Escribe una cita (real o inventada): ").strip()
        comentario = input("👉 ¿Cómo conecta con tu tesis?: ").strip()
        puntos = 0
        if any(p in cita.lower() for p in ["según", "como afirma", "en palabras de", "dice", "escribe"]):
            puntos += 1
        if len(comentario.split()) >= 10:
            puntos += 1
        if "." in comentario or "," in comentario:
            puntos += 1
        print(f"{random.choice(elogios)} (Puntos: {puntos}/3)")
        total += puntos
    print(f"\n📊 Total final: {total}/60")
    if total >= 50:
        print("🏅 ¡Dominas el arte de citar y comentar con propósito!")
    elif total >= 35:
        print("👍 Buen esfuerzo. Puedes afinar la relación entre fuente y argumento.")
    else:
        print("📘 Practica cómo incorporar ideas externas sin perder tu voz propia.")

# ✍️ Redacción libre
def redactar_argumento():
    print("\n✍️ REDACTA UN PÁRRAFO CON TU TESIS + UNA CITA + COMENTARIO:")
    tesis = input("📝 Tu tesis: ").strip()
    cita = input("👉 Tu cita: ").strip()
    comentario = input("👉 Tu reflexión sobre la cita: ").strip()
    texto = f"{tesis} {cita} {comentario}"
    puntos = 0
    if any(p in cita.lower() for p in ["según", "como afirma", "en palabras de", "dice", "escribe"]):
        puntos += 1
    if len(texto.split()) >= 40:
        puntos += 1
    if "." in texto and "," in texto:
        puntos += 1
    print(f"\n🎯 Puntos: {puntos}/3")
    if puntos == 3:
        print("🌟 ¡Tu párrafo está bien fundamentado y articulado!")
    elif puntos == 2:
        print("✅ Buen intento. Puedes afinar la integración de la fuente.")
    else:
        print("📘 Revisa cómo combinar tu voz con la de otros autores sin perder claridad.")

# 🎮 Menú principal
def menu():
    while True:
        print("\n🧠 Sintaxis Quest EDU – 11.º Grado – Lección 8: Integración de fuentes externas")
        print("1. Ver teoría 📘")
        print("2. Ver ejemplos guiados 📚")
        print("3. Practicar 20 inserciones de cita 📝")
        print("4. Redactar tu propio párrafo ✍️")
        print("5. Salir 👋")
        opcion = input("👉 Elige una opción: ")
        if opcion == "1":
            mostrar_teoria()
        elif opcion == "2":
            mostrar_ejemplos()
        elif opcion == "3":
            practicar_citas()
        elif opcion == "4":
            redactar_argumento()
        elif opcion == "5":
            print("👋 ¡Gracias por pensar con profundidad y citar con propósito!")
            break
        else:
            print("⚠️ Opción no válida. Intenta otra vez.")

# 🚀 Ejecutar programa
if __name__ == "__main__":
    menu()
