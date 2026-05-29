import random

# Datos de ejemplo en varios idiomas
palabras_espanol = {"sol": "sol.png", "casa": "casa.png", "perro": "perro.png"}
palabras_ingles = {"sun": "sun.png", "house": "house.png", "dog": "dog.png"}
palabras_ruso = {"солнце": "sun.png", "дом": "house.png", "собака": "dog.png"}

def ejercicio_asociacion(idioma):
    if idioma == "espanol":
        palabras = palabras_espanol
    elif idioma == "ingles":
        palabras = palabras_ingles
    else:
        palabras = palabras_ruso
    
    palabra = random.choice(list(palabras.keys()))
    respuesta = input(f"¿Qué palabra corresponde a la imagen? ({palabras[palabra]}) ")
    if respuesta.lower() == palabra:
        print("¡Correcto! ¡Bien hecho!")
    else:
        print(f"Incorrecto. La respuesta correcta es: {palabra}")

def main():
    while True:
        print("\nSeleccione el idioma:")
        print("1. Español")
        print("2. Inglés")
        print("3. Ruso")
        print("4. Salir")
        opcion = input("Ingrese el número: ")
        
        if opcion == "1":
            ejercicio_asociacion("espanol")
        elif opcion == "2":
            ejercicio_asociacion("ingles")
        elif opcion == "3":
            ejercicio_asociacion("ruso")
        elif opcion == "4":
            break
        else:
            print("Entrada inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
