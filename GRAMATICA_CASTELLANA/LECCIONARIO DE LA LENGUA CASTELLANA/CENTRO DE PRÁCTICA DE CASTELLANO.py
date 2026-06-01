import random

# Datos de ejemplo por categoría, nivel y tipo de ejercicio
datos_ejemplo = {
    'ortografia': {
        '1': [
            {"tipo": "completar", "pregunta": "Completa: Se escri__e con 'b' después de 'm'.", "respuesta": "be"},
            {"tipo": "opcion", "pregunta": "¿Cuál es la forma correcta?", "opciones": ["invitar", "inbitar"], "respuesta": "invitar"}
        ],
    },
    'morfologia': {
        '1': [
            {"tipo": "clasificar", "pregunta": "¿Qué tipo de palabra es 'corriendo'?", "respuesta": "gerundio"},
        ]
    },
    'sintaxis': {
        '1': [
            {"tipo": "funcion", "pregunta": "Identifica la función sintáctica de 'el perro' en: 'El perro duerme'.", "respuesta": "sujeto"},
        ]
    }
}

def mostrar_menu_principal():
    print("\n📘 CENTRO DE PRÁCTICA DE CASTELLANO 📘")
    print("1. Ortografía")
    print("2. Morfología")
    print("3. Sintaxis")
    print("4. Salir")

def elegir_nivel():
    print("\n📊 Elige nivel:")
    print("1. Básico")
    print("2. Intermedio (no disponible aún)")
    print("3. Avanzado (no disponible aún)")
    nivel = input("Tu elección: ")
    return nivel if nivel in ['1', '2', '3'] else '1'

def ejecutar_ejercicio(ejercicio):
    print(f"\n🧠 {ejercicio['pregunta']}")
    if ejercicio["tipo"] == "opcion":
        for i, op in enumerate(ejercicio["opciones"], 1):
            print(f"{i}. {op}")
        respuesta = input("Tu respuesta: ")
        if ejercicio["opciones"][int(respuesta)-1].lower() == ejercicio["respuesta"].lower():
            print("✅ ¡Correcto!")
        else:
            print(f"❌ Incorrecto. La respuesta correcta es: {ejercicio['respuesta']}")
    else:
        respuesta = input("Tu respuesta: ")
        if respuesta.strip().lower() == ejercicio["respuesta"].lower():
            print("✅ ¡Correcto!")
        else:
            print(f"❌ Incorrecto. La respuesta correcta es: {ejercicio['respuesta']}")

def iniciar_practica():
    while True:
        mostrar_menu_principal()
        opcion = input("Elige una opción: ")

        if opcion == "4":
            print("👋 ¡Gracias por practicar!")
            break

        tema = {"1": "ortografia", "2": "morfologia", "3": "sintaxis"}.get(opcion)
        nivel = elegir_nivel()
        ejercicios = datos_ejemplo.get(tema, {}).get(nivel, [])

        if not ejercicios:
            print("⚠️ No hay ejercicios disponibles para esta opción.")
            continue

        random.shuffle(ejercicios)
        for ejercicio in ejercicios:
            ejecutar_ejercicio(ejercicio)

        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    iniciar_practica()
