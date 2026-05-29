def corregir_bloque():
    # Lista de palabras con errores y sus correcciones
    palabras_con_errores = {
        "vueno": "bueno",
        "aparisio": "aparicio",
        "exámen": "examen",
        "suscita": "suscita",
        "rebolver": "revolver",
        "bisteck": "bistec",
        "huvo": "hubo",
        "enserio": "en serio",
        "aquélla": "aquella",
        "intención": "intención",
        "balcón": "balcón",
        "bailó": "bailó",
        "direción": "dirección",
        "malisima": "malísima",
        "utilisación": "utilización",
        "solucionó": "solucionó",
        "utilisó": "utilizó",
        "habrir": "abrir",
        "produción": "producción",
        "cansió": "cansó"
    }

    print("💻 🏛️ 👩 Escribe un bloque de texto con las siguientes palabras ‍🏫 🏛:")
    print(", ".join(palabras_con_errores.keys()))
    print("\n 👩👉 Intenta corregirlas al escribir. Al finalizar, presiona Enter para enviar tu respuesta.")

    texto_usuario = input("\nTu bloque: ").strip()
    palabras_usuario = texto_usuario.split()

    if len(palabras_usuario) != 20:
        print(f"⚠️‍🏫 🏛  👩Debes escribir exactamente 20 palabras. Escribiste {len(palabras_usuario)}. Intenta nuevamente.")
        return

    print("\n🔍 Evaluando tus respuestas...")
    errores = 0

    for i, palabra in enumerate(palabras_usuario):
        palabra_correcta = list(palabras_con_errores.values())[i]
        if palabra.lower() != palabra_correcta:
            errores += 1
            print(f"❌  👩Palabra incorrecta: '{palabra}' | Respuesta esperada: '{palabra_correcta}'")

    print("\n✅ Corrección final:")
    texto_correcto = " ".join(palabras_con_errores.values())
    print(texto_correcto)

    if errores == 0:
        print(" 👩🎉 ¡Perfecto! No tuviste errores.")
    else:
        print(f"👩✏️ Tuviste {errores} errores. ¡Sigue practicando!")

# Ejecutar el programa
if __name__ == "__main__":
    corregir_bloque()
