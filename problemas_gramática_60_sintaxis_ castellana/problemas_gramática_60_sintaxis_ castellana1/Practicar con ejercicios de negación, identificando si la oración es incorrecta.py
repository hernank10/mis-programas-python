import json

# Lista de ejemplos con negación compatible e incompatible
ejemplos = [
    {"afirmativa": "Bastantes problemas tenemos.", "negativa": "Bastantes problemas no tenemos.", "correcta": "No tenemos bastantes problemas."},
    {"afirmativa": "Con poco se conforma María.", "negativa": "Con poco no se conforma María.", "correcta": "María no se conforma con poco."},
    {"afirmativa": "Eso haría él.", "negativa": "Eso no haría él.", "correcta": "Él no haría eso."},
    {"afirmativa": "Mucho ha trabajado Pedro.", "negativa": "Mucho no ha trabajado Pedro.", "correcta": "Pedro no ha trabajado mucho."},
    # Agregar más ejemplos según sea necesario...
]

# Cargar ejemplos del usuario si existen
try:
    with open("ejemplos_usuario.json", "r") as f:
        ejemplos_usuario = json.load(f)
except FileNotFoundError:
    ejemplos_usuario = []

def practicar():
    for i, ejemplo in enumerate(ejemplos, start=1):
        print(f"Ejemplo {i}:")
        print("Oración afirmativa:", ejemplo["afirmativa"])
        print("Oración con negación:", ejemplo["negativa"])
        respuesta = input("¿Es correcta la negación? (sí/no): ").strip().lower()
        
        if respuesta == "no":
            print("Respuesta correcta. La negación es incorrecta.")
            print("Forma correcta:", ejemplo["correcta"])
        else:
            print("Incorrecto. La negación es incompatible.")
            print("Forma correcta:", ejemplo["correcta"])
        
        print("\n---\n")

def agregar_ejemplo():
    if len(ejemplos_usuario) >= 100:
        print("Se ha alcanzado el límite de 100 ejemplos guardados.")
        return
    afirmativa = input("Ingrese una oración afirmativa: ")
    negativa = input("Ingrese la versión con negación: ")
    correcta = input("Ingrese la forma correcta si la negación es incompatible: ")
    ejemplos_usuario.append({"afirmativa": afirmativa, "negativa": negativa, "correcta": correcta})
    with open("ejemplos_usuario.json", "w") as f:
        json.dump(ejemplos_usuario, f, indent=4)
    print("Ejemplo guardado exitosamente.\n")

def main():
    while True:
        print("\nMenú de práctica de negación en estructuras con anteposición:")
        print("1. Practicar con ejemplos")
        print("2. Agregar un nuevo ejemplo")
        print("3. Salir")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            practicar()
        elif opcion == "2":
            agregar_ejemplo()
        elif opcion == "3":
            print("Saliendo del programa. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()
