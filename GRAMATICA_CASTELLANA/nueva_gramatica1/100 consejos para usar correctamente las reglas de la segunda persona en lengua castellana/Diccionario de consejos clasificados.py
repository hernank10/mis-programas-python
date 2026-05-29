import random
import time

# Diccionario de consejos clasificados
consejos = {
    "Diseño pedagógico": [
        "Divide el curso en niveles progresivos según la dificultad.",
        "Establece objetivos de aprendizaje claros para cada lección.",
        "Utiliza una rúbrica común para evaluar ejercicios.",
        # ... (agrega hasta el 25)
    ],
    "Desarrollo técnico": [
        "Usa Python para prototipos rápidos.",
        "Usa Tkinter o PyQt para interfaces de escritorio.",
        "Usa Kivy para apps móviles.",
        # ... hasta el 50
    ],
    "Distribución multiplataforma": [
        "Compila para Android con buildozer o Kotlin.",
        "Usa PyInstaller para apps de escritorio.",
        # ... hasta el 65
    ],
    "Seguimiento del progreso": [
        "Registra el puntaje por lección.",
        "Muestra un gráfico de evolución.",
        # ... hasta el 75
    ],
    "Enfoque profesional y empleabilidad": [
        "Explica cómo aplicar el contenido en redacción profesional.",
        "Ofrece prácticas simuladas de corrección de textos.",
        # ... hasta el 85
    ],
    "Gestión del proyecto y escalabilidad": [
        "Usa Trello o Notion para planificar cada módulo.",
        "Define entregables semanales.",
        # ... hasta el 95
    ],
    "Expansión y sostenibilidad": [
        "Ofrece versiones adaptadas para niños o adultos mayores.",
        "Traduce el sistema a otros idiomas.",
        # ... hasta el 100
    ]
}

def practicar_categoria(categoria):
    aciertos = 0
    errores = []

    print(f"\n🧠 Practicando: {categoria}\n")
    lista = consejos[categoria]
    random.shuffle(lista)

    for original in lista:
        print("\nRecuerda este consejo (escríbelo lo más exacto posible):")
        respuesta = input("➤ Escribe: ")
        if respuesta.strip().lower() == original.strip().lower():
            print("✅ ¡Correcto!")
            aciertos += 1
        else:
            print(f"❌ Incorrecto. El consejo era:\n   {original}")
            errores.append((respuesta, original))

    print(f"\nPuntuación: {aciertos}/{len(lista)}")
    if errores:
        print("\n❗ Errores cometidos:")
        for tu_respuesta, correcto in errores:
            print(f"- Tú escribiste: {tu_respuesta}\n  Correcto era: {correcto}\n")

def menu_principal():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        for i, categoria in enumerate(consejos.keys(), 1):
            print(f"{i}. {categoria}")
        print("0. Salir")

        eleccion = input("Selecciona una categoría para practicar: ")
        if eleccion == "0":
            break
        else:
            try:
                categoria = list(consejos.keys())[int(eleccion)-1]
                practicar_categoria(categoria)
            except (IndexError, ValueError):
                print("❌ Opción inválida.")

# Ejecutar
if __name__ == "__main__":
    menu_principal()
