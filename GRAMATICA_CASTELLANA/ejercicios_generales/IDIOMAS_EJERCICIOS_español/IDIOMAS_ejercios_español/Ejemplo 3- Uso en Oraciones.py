import random
oraciones = {"brillante": "El sol está muy ______ hoy."}
def completar_oracion():
    palabra, oracion = random.choice(list(oraciones.items()))
    print(oracion)
    respuesta = input("Completa la oración: ").strip()
    if respuesta == palabra:
        print("Correcto!")
    else:
        print(f"Incorrecto. La respuesta correcta es '{palabra}'")

completar_oracion()
