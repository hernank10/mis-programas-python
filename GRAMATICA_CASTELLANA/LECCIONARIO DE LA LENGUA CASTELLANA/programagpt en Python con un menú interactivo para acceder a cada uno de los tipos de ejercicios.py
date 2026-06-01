def menu():
    print("\n===== MENÚ DE EJERCICIOS DE LENGUAJE =====")
    print("1. Selección múltiple")
    print("2. Completar oraciones")
    print("3. Detectar errores")
    print("4. Reescribir frases")
    print("5. Ordenar oraciones")
    print("6. Clasificación de palabras")
    print("7. Conjugación verbal")
    print("8. Uso correcto de tildes")
    print("9. Identificación de funciones sintácticas")
    print("10. Transformación de oraciones")
    print("0. Salir")

def seleccion_multiple():
    print("\n--- Ejercicio de Selección Múltiple ---")
    print("¿Cuál es la forma correcta?")
    print("a) Hiba\nb) Iva\nc) Iba")
    r = input("Respuesta: ")
    if r.lower() == "c":
        print("¡Correcto!")
    else:
        print("Incorrecto. La respuesta correcta es: Iba")

def completar_oraciones():
    print("\n--- Completar Oraciones ---")
    oracion = "El ___ corre en el parque."
    print(oracion)
    r = input("Palabra que falta: ")
    if r.lower() == "niño":
        print("¡Correcto!")
    else:
        print("Incorrecto. La respuesta correcta es: niño")

def detectar_errores():
    print("\n--- Detectar Errores ---")
    frase = "Ayer fuí al cine."
    print("¿Qué error contiene esta frase?")
    r = input("Respuesta: ")
    if "fui" in r.lower():
        print("¡Correcto! 'Fuí' lleva tilde incorrectamente.")
    else:
        print("Revisa de nuevo. La palabra 'fuí' es incorrecta.")

def reescribir_frases():
    print("\n--- Reescribir Frases ---")
    print("Reescribe en estilo formal: 'Voy a la tienda pa' comprar pan.'")
    r = input("Tu versión: ")
    print("Gracias, se evaluará tu respuesta manualmente.")

def ordenar_oraciones():
    print("\n--- Ordenar Oraciones ---")
    palabras = ["la", "mañana", "temprano", "se", "levantó", "ella"]
    print("Ordena estas palabras: ", palabras)
    r = input("Tu oración: ")
    print("Gracias, se evaluará tu respuesta manualmente.")

def clasificacion_palabras():
    print("\n--- Clasificación de Palabras ---")
    palabra = "árbol"
    print(f"Clasifica la palabra '{palabra}' (sustantivo, verbo, adjetivo, etc.)")
    r = input("Respuesta: ")
    if "sustantivo" in r.lower():
        print("¡Correcto!")
    else:
        print("Incorrecto. Es un sustantivo.")

def conjugacion_verbal():
    print("\n--- Conjugación Verbal ---")
    print("Conjuga el verbo 'comer' en pretérito, primera persona del plural.")
    r = input("Respuesta: ")
    if r.lower() == "comimos":
        print("¡Correcto!")
    else:
        print("Incorrecto. La forma correcta es 'comimos'.")

def uso_tildes():
    print("\n--- Uso Correcto de Tildes ---")
    print("¿Cuál es la forma correcta?")
    print("a) Publico\nb) Público\nc) Publicó")
    r = input("Respuesta: ")
    if r.lower() == "b":
        print("¡Correcto!")
    else:
        print("Incorrecto. Es 'Público'.")

def funciones_sintacticas():
    print("\n--- Identificación de Funciones Sintácticas ---")
    print("Identifica la función de 'el perro' en la frase: 'El perro ladra fuerte.'")
    r = input("Respuesta: ")
    if "sujeto" in r.lower():
        print("¡Correcto!")
    else:
        print("Incorrecto. 'El perro' es el sujeto.")

def transformacion_oraciones():
    print("\n--- Transformación de Oraciones ---")
    print("Transforma esta oración activa en pasiva:")
    print("'El chef preparó la cena.'")
    r = input("Respuesta: ")
    if "la cena fue preparada por el chef" in r.lower():
        print("¡Correcto!")
    else:
        print("Incorrecto. Una posible respuesta es: 'La cena fue preparada por el chef.'")

def main():
    while True:
        menu()
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            seleccion_multiple()
        elif opcion == "2":
            completar_oraciones()
        elif opcion == "3":
            detectar_errores()
        elif opcion == "4":
            reescribir_frases()
        elif opcion == "5":
            ordenar_oraciones()
        elif opcion == "6":
            clasificacion_palabras()
        elif opcion == "7":
            conjugacion_verbal()
        elif opcion == "8":
            uso_tildes()
        elif opcion == "9":
            funciones_sintacticas()
        elif opcion == "10":
            transformacion_oraciones()
        elif opcion == "0":
            print("Gracias por practicar. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
