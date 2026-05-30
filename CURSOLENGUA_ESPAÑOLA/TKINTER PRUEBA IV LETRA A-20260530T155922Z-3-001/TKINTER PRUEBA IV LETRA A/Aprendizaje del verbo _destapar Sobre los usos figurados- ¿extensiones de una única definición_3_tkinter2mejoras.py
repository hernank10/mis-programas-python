import random

ejercicios = [
    ("El mesero ______ la olla para servir la sopa.", "destapó"),
    ("El periodista ______ una gran conspiración en el gobierno.", "destapó"),
    ("El fontanero ______ la tubería obstruida.", "destapó"),
    ("La investigación ______ secretos ocultos de la empresa.", "destapó"),
    ("El arqueólogo ______ una tumba antigua.", "destapó")
]

correctas = 0
incorrectas = 0

def mostrar_teoria():
    print("\nTeoría sobre el verbo 'destapar':")
    print("- Uso recto: Quitar la tapa de algo (Ej: Destapó la botella).")
    print("- Uso figurado: Revelar información oculta (Ej: Destaparon un escándalo).\n")

def nuevo_ejercicio():
    return random.choice(ejercicios)

def verificar_respuesta(ejercicio, respuesta_usuario):
    global correctas, incorrectas
    if respuesta_usuario.lower().strip() == ejercicio[1]:
        print("✅ Correcto!")
        correctas += 1
    else:
        print(f"❌ Incorrecto! La respuesta correcta es: {ejercicio[1]}")
        incorrectas += 1

def mostrar_progreso():
    print(f"\nProgreso: \n✅ Correctas: {correctas}\n❌ Incorrectas: {incorrectas}\n")

def exportar_resultados():
    with open("resultados.txt", "w") as file:
        file.write(f"Correctas: {correctas}\nIncorrectas: {incorrectas}\n")
    print("Resultados guardados en 'resultados.txt'\n")

def main():
    while True:
        print("Menú:")
        print("1. Ver teoría")
        print("2. Nuevo ejercicio")
        print("3. Mostrar progreso")
        print("4. Exportar resultados")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            mostrar_teoria()
        elif opcion == "2":
            ejercicio = nuevo_ejercicio()
            print(f"\n{ejercicio[0]}")
            respuesta_usuario = input("Tu respuesta: ")
            verificar_respuesta(ejercicio, respuesta_usuario)
        elif opcion == "3":
            mostrar_progreso()
        elif opcion == "4":
            exportar_resultados()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, intenta de nuevo.\n")

if __name__ == "__main__":
    main()
