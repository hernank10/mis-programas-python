import json

def mostrar_teoria():
    print("\nTEORÍA")
    print("Los modificadores locativos en sustantivos sin determinación presentan restricciones en su uso.")
    print("Ejemplo agramatical: *Tengo coche en el garaje.")
    print("Ejemplo correcto: Tengo un coche en el garaje.")
    print("Ejemplo correcto en función predicativa: Es catedrático en la Complutense.\n")

def mostrar_ejemplos():
    print("\nEJEMPLOS")
    ejemplos = [
        "*Tengo coche en el garaje.",
        "Tengo un coche en el garaje.",
        "Es catedrático en la Complutense.",
        "Son catedráticos en la universidad.",
        "*Vivo piso en el centro.",
        "Vivo en un piso en el centro."
    ]
    for ej in ejemplos:
        print(f"- {ej}")
    print()

def practicar_escritura():
    oracion = input("Escribe una oración con un modificador locativo: ")
    print(f"Tu oración registrada: {oracion}\n")
    actualizar_estadisticas("escritos", 1)

def realizar_test():
    preguntas = [
        ("¿Cuál de estas frases es correcta?", ["Tengo coche en el garaje.", "Tengo un coche en el garaje."], 1),
        ("¿Cuál de estas frases es incorrecta?", ["Es profesor en la UNAM.", "*Es médico en hospital."], 1)
    ]
    
    correctas = 0
    for i, (pregunta, opciones, correcta) in enumerate(preguntas):
        print(f"\nPregunta {i+1}: {pregunta}")
        for idx, opcion in enumerate(opciones):
            print(f"{idx+1}. {opcion}")
        respuesta = int(input("Tu respuesta (1 o 2): ")) - 1
        if respuesta == correcta:
            print("¡Correcto!")
            correctas += 1
        else:
            print("Incorrecto.")
    
    actualizar_estadisticas("aciertos", correctas)
    print(f"Has acertado {correctas} de {len(preguntas)}.\n")

def actualizar_estadisticas(tipo, valor):
    try:
        with open("estadisticas.json", "r") as file:
            stats = json.load(file)
    except FileNotFoundError:
        stats = {"escritos": 0, "aciertos": 0}
    
    stats[tipo] += valor
    
    with open("estadisticas.json", "w") as file:
        json.dump(stats, file)

def mostrar_estadisticas():
    try:
        with open("estadisticas.json", "r") as file:
            stats = json.load(file)
        print("\nESTADÍSTICAS")
        print(f"Oraciones escritas: {stats['escritos']}")
        print(f"Respuestas correctas en test: {stats['aciertos']}\n")
    except FileNotFoundError:
        print("\nNo hay estadísticas registradas aún.\n")

def menu():
    while True:
        print("\nMenú:")
        print("1. Ver teoría")
        print("2. Ver ejemplos")
        print("3. Practicar escritura")
        print("4. Realizar test")
        print("5. Ver estadísticas")
        print("6. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            mostrar_teoria()
        elif opcion == "2":
            mostrar_ejemplos()
        elif opcion == "3":
            practicar_escritura()
        elif opcion == "4":
            realizar_test()
        elif opcion == "5":
            mostrar_estadisticas()
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
