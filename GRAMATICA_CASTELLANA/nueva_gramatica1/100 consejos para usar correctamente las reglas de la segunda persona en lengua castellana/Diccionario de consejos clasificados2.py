import random

# Diccionario de consejos clasificados
consejos = {
    "Diseño pedagógico": [
        "Divide el curso en niveles progresivos según la dificultad.",
        "Establece objetivos de aprendizaje claros para cada lección.",
        "Utiliza una rúbrica común para evaluar ejercicios.",
        "Incluye actividades prácticas en cada tema."
    ],
    "Desarrollo técnico": [
        "Usa Python para prototipos rápidos.",
        "Usa Tkinter o PyQt para interfaces de escritorio.",
        "Usa Kivy para apps móviles.",
        "Aplica POO para escalabilidad del código."
    ],
    "Distribución multiplataforma": [
        "Compila para Android con buildozer o Kotlin.",
        "Usa PyInstaller para apps de escritorio.",
        "Adapta la UI según el sistema operativo.",
        "Documenta dependencias necesarias."
    ],
}

def ver_consejos(categoria):
    print(f"\n📘 Consejos en categoría: {categoria}")
    for i, consejo in enumerate(consejos[categoria], 1):
        print(f"{i}. {consejo}")

def practicar_categoria(categoria):
    aciertos = 0
    errores = []
    lista = consejos[categoria][:]
    random.shuffle(lista)

    print(f"\n🧠 Practicando: {categoria}")
    for original in lista:
        print("\nRecuerda este consejo y escríbelo lo más exacto posible:")
        respuesta = input("➤ Escribe: ")
        if respuesta.strip().lower() == original.strip().lower():
            print("✅ ¡Correcto!")
            aciertos += 1
        else:
            print(f"❌ Incorrecto. El consejo era:\n   {original}")
            errores.append((respuesta, original))

    print(f"\n📊 Resultado final: {aciertos}/{len(lista)}")
    if errores:
        print("\n❗ Consejos con errores:")
        for tu_respuesta, correcto in errores:
            print(f"- Tú escribiste: {tu_respuesta}\n  Correcto era: {correcto}\n")

def menu_principal():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        categorias = list(consejos.keys())
        for i, categoria in enumerate(categorias, 1):
            print(f"{i}. {categoria}")
        print("V. Ver consejos antes de practicar")
        print("0. Salir")

        eleccion = input("Selecciona una opción: ").strip().lower()

        if eleccion == "0":
            break
        elif eleccion == "v":
            for i, categoria in enumerate(categorias, 1):
                print(f"{i}. {categoria}")
            try:
                idx = int(input("¿De qué categoría deseas ver los consejos? ")) - 1
                ver_consejos(categorias[idx])
            except:
                print("❌ Opción no válida.")
        else:
            try:
                idx = int(eleccion) - 1
                practicar_categoria(categorias[idx])
            except:
                print("❌ Opción inválida.")

# Ejecutar
if __name__ == "__main__":
    menu_principal()
