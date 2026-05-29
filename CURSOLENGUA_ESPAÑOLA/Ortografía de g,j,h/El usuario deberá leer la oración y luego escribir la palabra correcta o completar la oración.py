def practicar_reglas():
    reglas = [
        ("g", "gente", "La **gente** en la plaza estaba animada."),
        ("g", "gigante", "El **gigante** caminaba por el bosque."),
        ("g", "guerra", "La **guerra** afectó a toda la región."),
        ("j", "cruje", "El viejo puente **cruje** cuando pasas sobre él."),
        ("j", "trabaja", "Mi hermana **trabaja** en una tienda de ropa."),
        ("j", "cajita", "Guardé las joyas en una pequeña **cajita**."),
    ]

    print("¡Bienvenido! Vamos a practicar las reglas de la 'g' y la 'j'.")
    print("Lee la oración y escribe la palabra correcta según la regla indicada:")

    for regla, palabra, oracion in reglas:
        respuesta = input(f"Regla: Palabras con '{regla}': {oracion}: ")
        if respuesta.lower() == palabra.lower():
            print("¡Correcto! ¡Sigue así!")
        else:
            print(f"La palabra correcta era '{palabra}'. ¡Inténtalo de nuevo!")

if __name__ == "__main__":
    practicar_reglas()
