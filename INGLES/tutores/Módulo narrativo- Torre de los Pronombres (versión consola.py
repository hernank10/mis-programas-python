# Módulo narrativo: Torre de los Pronombres (versión consola)

import time

# Datos de personajes
personajes = [
    {
        "nombre": "Sir He",
        "descripcion": "Un caballero con capa azul y espada dorada.",
        "pista": "Es un doctor.",
        "pronombre": "he",
        "respuesta_correcta": "Is he a doctor?",
        "opciones": ["Is he a doctor?", "Is she a doctor?", "Are they doctors?"]
    },
    {
        "nombre": "Lady She",
        "descripcion": "Una reina con corona de plata.",
        "pista": "Es una profesora.",
        "pronombre": "she",
        "respuesta_correcta": "Is she a teacher?",
        "opciones": ["Is he a teacher?", "Is she a teacher?", "Are they teachers?"]
    },
    {
        "nombre": "The Twins",
        "descripcion": "Dos figuras idénticas con túnicas verdes.",
        "pista": "Son músicos.",
        "pronombre": "they",
        "respuesta_correcta": "Are they musicians?",
        "opciones": ["Is he a musician?", "Is she a musician?", "Are they musicians?"]
    }
]

# Estadísticas
puntaje = 0
aciertos = 0
errores = 0

# Función de validación
def validar_respuesta(opcion, personaje):
    if opcion == personaje["respuesta_correcta"]:
        return True
    else:
        return False

# Función de retroalimentación
def mostrar_regla(personaje):
    pronombre = personaje["pronombre"]
    verbo = "am" if pronombre == "I" else "are" if pronombre in ["you", "we", "they"] else "is"
    print(f"\n📘 Regla aplicada:")
    print(f"Pronombre: {pronombre} → Verbo 'to be': {verbo}")
    print(f"Pregunta correcta: {personaje['respuesta_correcta']}")
    print(f"Comparación en español: ¿{personaje['pista']}?")

# Juego principal
def jugar_mision():
    global puntaje, aciertos, errores
    print("\n🏰 Bienvenido a la Torre de los Pronombres")
    print("Responde correctamente para desbloquear cada puerta...\n")

    for personaje in personajes:
        print(f"\n🔓 Puerta: {personaje['nombre']}")
        print(f"🧙 Descripción: {personaje['descripcion']}")
        print(f"🎯 Pista: {personaje['pista']}")
        print("\nOpciones:")
        for i, opcion in enumerate(personaje["opciones"], 1):
            print(f"{i}. {opcion}")

        try:
            eleccion = int(input("✍️ Elige la opción correcta (1-3): "))
            seleccionada = personaje["opciones"][eleccion - 1]
        except:
            print("⚠️ Entrada inválida. Se contará como error.")
            errores += 1
            puntaje -= 5
            continue

        if validar_respuesta(seleccionada, personaje):
            print("✅ ¡Correcto! Has desbloqueado la puerta.")
            puntaje += 10
            aciertos += 1
        else:
            print("❌ Incorrecto.")
            puntaje -= 5
            errores += 1

        mostrar_regla(personaje)
        time.sleep(1)

    # Resultados
    print("\n🎉 Misión completada")
    print(f"✅ Aciertos: {aciertos}")
    print(f"❌ Errores: {errores}")
    print(f"🏆 Puntaje total: {puntaje}")

# Ejecutar
if __name__ == "__main__":
    jugar_mision()
