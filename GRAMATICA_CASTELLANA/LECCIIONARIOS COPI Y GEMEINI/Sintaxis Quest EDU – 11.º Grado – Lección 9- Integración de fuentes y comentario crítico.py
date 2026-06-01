import random

# 📘 Teoría
teoria = """
📘 LECCIÓN 9 – ¿CÓMO ESCRIBIMOS CON IDEAS QUE VIENEN DE FUERA?

Integrar una fuente externa en nuestro texto no es solo copiar: es pensar junto con esa voz.

✍️ Estructura recomendada:

1️⃣ Introducción de la fuente → “Según…”, “Como afirma…”  
2️⃣ Fragmento o cita  
3️⃣ Comentario personal → interpretación, reflexión, valoración

🎯 Conectores útiles:
• “Esta idea muestra que…”  
• “Esto permite pensar en…”  
• “Podemos relacionarlo con…”  
• “Esta afirmación revela que…”
"""

# 📚 Fuentes simuladas para usar
fuentes = [
    "'Los estudiantes que participan en actividades artísticas desarrollan mayor empatía' (Revista Educación Humanista, 2023)",
    "'Solo el 25% de los jóvenes lee por iniciativa propia' (Informe nacional de hábitos lectores, 2022)",
    "'El uso de la tecnología debe estar mediado por el pensamiento crítico' (Artículo en EduDigital, 2024)",
    "'Cuando el estudiante es parte del diseño curricular, aumenta su motivación' (Congreso Pedagógico Internacional, 2023)",
    "'La escritura permite reconstruir emociones que no pueden expresarse verbalmente' (Ensayo de A. Jiménez sobre educación emocional, 2022)",
    "'Los adolescentes buscan sentido en lo que aprenden, no solo aprobación' (Entrevista publicada en Proyecto Aula, 2021)",
    "'La creatividad no es un lujo, es una necesidad en contextos escolares actuales' (Editorial Educare, 2023)"
]

elogios = [
    "🌟 ¡Buen uso de la fuente y comentario bien reflexionado!",
    "✅ ¡Integraste la cita con sentido y lógica!",
    "🧠 ¡Tu texto conecta lo externo con tu propia voz!",
    "👏 ¡Tu comentario muestra profundidad y pensamiento crítico!",
]

# 📘 Mostrar teoría
def mostrar_teoria():
    print(teoria)

# 📚 Mostrar ejemplos guiados
def mostrar_ejemplos():
    print("\n📚 EJEMPLO DE INTEGRACIÓN DE FUENTE:")
    print("Fuente: 'Los estudiantes que participan en actividades artísticas desarrollan mayor empatía'")
    print("Tu texto:")
    print("Según la Revista Educación Humanista, 'los estudiantes que participan en actividades artísticas desarrollan mayor empatía'. Esta idea muestra que el arte no solo entretiene, sino que mejora la convivencia y el entendimiento entre pares.\n")

# 📝 Práctica con fuentes
def practicar_insercion():
    print("\n📝 INTEGRA CADA FUENTE EN UN TEXTO PROPIO CON COMENTARIO:")
    total = 0
    for i, fuente in enumerate(fuentes, 1):
        print(f"\n{str(i).zfill(2)}. Fuente:\n📚 {fuente}")
        texto = input("👉 Tu párrafo con fuente + comentario: ").strip().lower()
        puntos = 0
        if any(c in texto for c in ["según", "como afirma", "de acuerdo con"]):
            puntos += 1
        if any(c in texto for c in ["esta idea", "esto muestra", "podemos relacionarlo", "esta afirmación"]):
            puntos += 1
        if len(texto.split()) >= 25:
            puntos += 1
        print(f"{random.choice(elogios)} (Puntos: {puntos}/3)")
        total += puntos
    print(f"\n📊 Puntaje total: {total}/21")

# ✍️ Composición libre
def redactar_ensayo():
    print("\n✍️ ESCRIBE UN TEXTO CON 2 FUENTES DIFERENTES + TUS COMENTARIOS:")
    tema = input("📝 ¿Qué tema elegiste?: ").strip()
    fuente1 = input("📚 Fuente 1 (título o frase): ").strip()
    comentario1 = input("✍️ Comentario crítico sobre fuente 1: ").strip()
    fuente2 = input("📚 Fuente 2 (título o frase): ").strip()
    comentario2 = input("✍️ Comentario crítico sobre fuente 2: ").strip()
    texto = f"TEMA: {tema}\n\nFuente 1: {fuente1}\nComentario: {comentario1}\n\nFuente 2: {fuente2}\nComentario: {comentario2}"
    puntos = 0
    if len(comentario1.split()) >= 20 and len(comentario2.split()) >= 20:
        puntos += 1
    if any(c in comentario1.lower()+comentario2.lower() for c in ["esta idea", "esto muestra", "podemos pensar", "esta afirmación"]):
        puntos += 1
    if "." in comentario1 and "." in comentario2:
        puntos += 1
    print("\n📝 Texto generado:")
    print(texto)
    print(f"\n🎯 Puntos: {puntos}/3")
    if puntos == 3:
        print("🌟 ¡Tu ensayo muestra integración auténtica de ideas externas y pensamiento propio!")
    elif puntos == 2:
        print("✅ Buen trabajo. Puedes afinar la conexión entre fuente y comentario.")
    else:
        print("📘 Revisa cómo vincular la fuente con tu reflexión personal.")

# 🎮 Menú principal
def menu():
    while True:
        print("\n🧠 Sintaxis Quest EDU – 11.º Grado – Lección 9: Integración de fuentes y comentario crítico")
        print("1. Ver teoría 📘")
        print("2. Ver ejemplo guiado 📚")
        print("3. Practicar con 7 fuentes 📝")
        print("4. Redactar ensayo libre ✍️")
        print("5. Salir 👋")
        opcion = input("👉 Elige una opción: ")
        if opcion == "1":
            mostrar_teoria()
        elif opcion == "2":
            mostrar_ejemplos()
        elif opcion == "3":
            practicar_insercion()
        elif opcion == "4":
            redactar_ensayo()
        elif opcion == "5":
            print("👋 ¡Gracias por escribir con otras voces y tu propia mirada reflexiva!")
            break
        else:
            print("⚠️ Opción no válida. Intenta otra vez.")

# 🚀 Ejecutar programa
if __name__ == "__main__":
    menu()
