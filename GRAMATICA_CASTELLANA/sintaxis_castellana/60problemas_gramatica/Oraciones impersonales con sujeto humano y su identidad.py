import json

PROGRESO_FILE = "progreso_impersonales.json"

def cargar_progreso():
    try:
        with open(PROGRESO_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def guardar_progreso(progreso):
    with open(PROGRESO_FILE, "w") as file:
        json.dump(progreso, file, indent=4)

def mostrar_introduccion():
    print("\n📖 Introducción")
    print("Las oraciones impersonales con sujeto humano se caracterizan por una identidad definida dentro del discurso. Estas estructuras plantean cuestiones importantes sobre la referencia y la función sintáctica del sujeto.Cuando alguien llama a la puerta, el pronombre indefinido alguien introduce un referente humano en el discurso con la suficiente identidad como para ser el antecedente de los pronombres personales le y él. Esto implica que alguien posee una existencia discursiva clara, lo que permite su referencia anafórica dentro del texto. Sin embargo, en la construcción con se impersonal, como en se llama a la puerta, la identidad del sujeto humano se diluye hasta convertirse en una persona arbitraria. En este caso, no es posible establecer una referencia clara que permita el uso de los pronombres personales le o él")

def mostrar_teoria():
    print("\n📚 Teoría")
    print("Explicación detallada sobre las oraciones impersonales y su identidad discursiva...")

def ejercicios():
    preguntas = [
        "1. Escribe una oración con 'se impersonal' y un sujeto humano.",
        "2. Explica por qué en la construcción 'se dice que...' el sujeto no tiene identidad definida.",
        "3. Reescribe la oración 'Alguien llamó a la puerta' en una forma impersonal.",
        "4. ¿Por qué no se puede usar 'le' como antecedente de un sujeto impersonal? Explica con un ejemplo.",
        "5. Identifica el tipo de sujeto en la oración: 'Se vendieron todas las entradas'.",
        "6. ¿Cómo cambia el significado de una oración al pasar de 'alguien' a 'se impersonal'? Da un ejemplo.",
        "7. Escribe una oración en la que el sujeto impersonal tenga una identidad más definida.",
        "8. Explica por qué el sujeto de 'Se vive bien aquí' es impersonal y no tiene referente claro.",
        "9. Escribe una oración con 'se' impersonal en la que el sujeto humano no pueda ser antecedente de 'le'.",
        "10. Reescribe la oración 'Alguien cerró la ventana' usando una construcción impersonal." 
    ]
    progreso = cargar_progreso()
    
    for i, pregunta in enumerate(preguntas):
        print(f"\n{pregunta}")
        respuesta = input("✍️ Tu respuesta: ")
        progreso[str(i)] = respuesta
        guardar_progreso(progreso)
        print("✅ Respuesta guardada.")

def ver_progreso():
    progreso = cargar_progreso()
    if not progreso:
        print("⚠️ Aún no has registrado respuestas.")
    else:
        print("\n📊 Progreso guardado:")
        for i, respuesta in progreso.items():
            print(f"Ejercicio {int(i) + 1}: {respuesta}")

def menu():
    while True:
        print("\n🔹 Menú 🔹")
        print("1. Introducción 📖")
        print("2. Teoría 📚")
        print("3. Ejercicios ✍️")
        print("4. Ver progreso 📊")
        print("5. Salir ❌")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            mostrar_introduccion()
        elif opcion == "2":
            mostrar_teoria()
        elif opcion == "3":
            ejercicios()
        elif opcion == "4":
            ver_progreso()
        elif opcion == "5":
            print("👋 Saliendo del programa. ¡Hasta la próxima!")
            break
        else:
            print("⚠️ Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    menu()
