import random

def detective_ortografico(puntos):
    print("\n🔎 El Detective Ortográfico")
    errores = {"haber": "a ver", "vaca": "baca", "echo": "hecho"}
    palabra, correccion = random.choice(list(errores.items()))
    respuesta = input(f"Corrige el error en esta palabra: {palabra}: ")
    if respuesta.lower() == correccion:
        print("✅ Correcto!")
        puntos += 1
    else:
        print(f"❌ Incorrecto. La respuesta correcta era: {correccion}")
    return puntos

def palabra_perdida(puntos):
    print("\n❌🔠 Palabra Perdida")
    palabras = {"ca_illo": "caballo", "ha_a": "haya", "a_ecto": "afecto"}
    incompleta, completa = random.choice(list(palabras.items()))
    respuesta = input(f"Completa la palabra: {incompleta}: ")
    if respuesta.lower() == completa:
        print("✅ Correcto!")
        puntos += 1
    else:
        print(f"❌ Incorrecto. La respuesta correcta era: {completa}")
    return puntos

def carrera_de_letras(puntos):
    print("\n🚀✏️ La Carrera de Letras")
    palabras = ["ortografía", "gramática", "puntación"]
    palabra = random.choice(palabras)
    desordenada = list(palabra)
    random.shuffle(desordenada)
    print("Ordena la palabra:", "".join(desordenada))
    respuesta = input("Tu respuesta: ")
    if respuesta.lower() == palabra:
        print("✅ Correcto!")
        puntos += 1
    else:
        print(f"❌ Incorrecto. La respuesta correcta era: {palabra}")
    return puntos

def ortografo_rapido(puntos):
    print("\n⏳🔥 El Ortógrafo Rápido")
    opciones = {"tubo": "tuvo", "halla": "haya", "valla": "vaya"}
    palabra1, palabra2 = random.choice(list(opciones.items()))
    oracion = f"No sé si {palabra1}/{palabra2} vendrá hoy."
    print(oracion)
    respuesta = input("Elige la palabra correcta: ")
    if respuesta.lower() == palabra2:
        print("✅ Correcto!")
        puntos += 1
    else:
        print(f"❌ Incorrecto. La respuesta correcta era: {palabra2}")
    return puntos

def constructor_de_frases(puntos):
    print("\n🏗️📜 El Constructor de Frases")
    frases = {"Usar punto y coma": "Voy al mercado; compraré frutas."}
    regla, frase = random.choice(list(frases.items()))
    print(f"Regla: {regla}")
    respuesta = input("Escribe la frase correctamente: ")
    if respuesta.lower() == frase.lower():
        print("✅ Correcto!")
        puntos += 1
    else:
        print(f"❌ Incorrecto. La respuesta correcta era: {frase}")
    return puntos

def menu():
    puntos = 0
    while True:
        print("\n📚 MENÚ DE JUEGOS ORTOGRÁFICOS")
        print("1. Detective Ortográfico")
        print("2. Palabra Perdida")
        print("3. Carrera de Letras")
        print("4. Ortógrafo Rápido")
        print("5. Constructor de Frases")
        print("6. Ver progreso")
        print("7. Salir")
        opcion = input("Elige un juego: ")
        
        if opcion == "1":
            puntos = detective_ortografico(puntos)
        elif opcion == "2":
            puntos = palabra_perdida(puntos)
        elif opcion == "3":
            puntos = carrera_de_letras(puntos)
        elif opcion == "4":
            puntos = ortografo_rapido(puntos)
        elif opcion == "5":
            puntos = constructor_de_frases(puntos)
        elif opcion == "6":
            print(f"\n🎯 Tu progreso actual: {puntos} puntos")
        elif opcion == "7":
            print("👋 ¡Gracias por jugar! Hasta la próxima.")
            break
        else:
            print("❌ Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    menu()
