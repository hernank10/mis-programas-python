# Listas de palabras iniciales
sinonimos = [
    ("Alegre", "Contento"), ("Casa", "Hogar"), ("Bello", "Hermoso"),
    ("Rápido", "Veloz"), ("Difícil", "Complicado"), ("Enseñar", "Instruir"),
    ("Comprender", "Entender"), ("Triste", "Melancólico"), ("Amigo", "Compañero"),
    ("Escribir", "Redactar")
]

isonimos = [
    ("Coche (Esp)", "Carro (LatAm)"), ("Ordenador (Esp)", "Computadora (LatAm)"), 
    ("Zumo (Esp)", "Jugo (LatAm)"), ("Tarta (Esp)", "Pastel (LatAm)"), 
    ("Móvil (Esp)", "Celular (LatAm)"), ("Autobús (Esp)", "Bus (LatAm)"), 
    ("Aparcar (Esp)", "Estacionar (LatAm)"), ("Gafas (Esp)", "Lentes (LatAm)"), 
    ("Piso (Esp)", "Departamento (LatAm)"), ("Chaqueta (Esp)", "Campera (LatAm)")
]

homonimos = [
    ("Banco (institución financiera)", "Banco (asiento)"), 
    ("Gato (animal)", "Gato (herramienta)"), ("Vela (cera para iluminar)", "Vela (navegar)"), 
    ("Caja (recipiente)", "Caja (verbo 'cajar')"), ("Cura (sacerdote)", "Cura (sanación)"), 
    ("Bota (calzado)", "Bota (verbo 'botar')"), ("Hoja (planta)", "Hoja (papel)"), 
    ("Río (cuerpo de agua)", "Río (verbo 'reír')"), ("Carta (misiva)", "Carta (menú)"), 
    ("Ratón (animal)", "Ratón (dispositivo de computadora)")
]

homofonas = [
    ("Haya (verbo 'haber')", "Haya (árbol)"), ("Vaya (verbo 'ir')", "Valla (cerca)"), 
    ("Cazar (atrapar)", "Casar (unir en matrimonio)"), ("Grabar (registrar)", "Gravar (imponer un impuesto)"), 
    ("Basto (tosco)", "Vasto (amplio)"), ("Hondo (profundo)", "Onda (curva)"), 
    ("Herrar (poner herraduras)", "Errar (equivocarse)"), ("Bello (hermoso)", "Vello (pelusa)"), 
    ("Hierba (planta)", "Hierva (verbo 'hervir')"), ("Votar (sufragar)", "Botar (arrojar)")
]

antonimos = [
    ("Día", "Noche"), ("Alto", "Bajo"), ("Frío", "Calor"), 
    ("Feliz", "Triste"), ("Blanco", "Negro"), ("Rápido", "Lento"), 
    ("Grande", "Pequeño"), ("Claro", "Oscuro"), ("Abierto", "Cerrado"), 
    ("Nuevo", "Viejo")
]

# Función para practicar
def practicar_palabras(palabras, categoria):
    print(f"\nPracticando {categoria}:")
    correctas = 0
    for par in palabras:
        significado = input(f"Escribe el significado de '{par[0]}': ").strip()
        respuesta = input(f"Escribe el sinónimo de '{par[0]}': ").strip()
        if respuesta.lower() == par[1].lower():
            print("¡Correcto!")
            correctas += 1
        else:
            print(f"Incorrecto. La respuesta correcta es '{par[1]}'")
    print(f"Obtuviste {correctas} de {len(palabras)} correctas.\n")

# Función para agregar más palabras
def agregar_palabras(palabras, categoria):
    while True:
        palabra1 = input(f"Escribe una nueva palabra para la categoría '{categoria}': ").strip()
        palabra2 = input(f"Escribe el par (sinónimo/isonimo/homónimo/homófono/antónimo) de '{palabra1}': ").strip()
        palabras.append((palabra1, palabra2))
        continuar = input("¿Quieres agregar otra palabra? (sí/no): ").strip().lower()
        if continuar != 'sí':
            break

# Función para escribir un ensayo
def escribir_ensayo(palabras, categoria):
    print(f"\nEscribiendo un ensayo para la categoría {categoria}:")
    ensayo = input("Escribe un pequeño ensayo usando algunas de las palabras que has aprendido: ")
    print("\nGracias por tu ensayo. Aquí está lo que escribiste:")
    print(ensayo)

# Menú principal
def menu():
    while True:
        print("Selecciona una categoría para practicar:")
        print("1. Sinónimos")
        print("2. Isónimos")
        print("3. Homónimos")
        print("4. Homófonas")
        print("5. Antónimos")
        print("6. Agregar más palabras")
        print("7. Escribir un ensayo")
        print("8. Salir")

        opcion = input("Ingresa el número de la opción deseada: ").strip()
        
        if opcion == "1":
            practicar_palabras(sinonimos, "Sinónimos")
        elif opcion == "2":
            practicar_palabras(isonimos, "Isónimos")
        elif opcion == "3":
            practicar_palabras(homonimos, "Homónimos")
        elif opcion == "4":
            practicar_palabras(homofonas, "Homófonas")
        elif opcion == "5":
            practicar_palabras(antonimos, "Antónimos")
        elif opcion == "6":
            print("Selecciona una categoría para agregar palabras:")
            print("1. Sinónimos")
            print("2. Isónimos")
            print("3. Homónimos")
            print("4. Homófonas")
            print("5. Antónimos")
            categoria_opcion = input("Ingresa el número de la opción deseada: ").strip()
            if categoria_opcion == "1":
                agregar_palabras(sinonimos, "Sinónimos")
            elif categoria_opcion == "2":
                agregar_palabras(isonimos, "Isónimos")
            elif categoria_opcion == "3":
                agregar_palabras(homonimos, "Homónimos")
            elif categoria_opcion == "4":
                agregar_palabras(homofonas, "Homófonas")
            elif categoria_opcion == "5":
                agregar_palabras(antonimos, "Antónimos")
        elif opcion == "7":
            print("Selecciona una categoría para escribir un ensayo:")
            print("1. Sinónimos")
            print("2. Isónimos")
            print("3. Homónimos")
            print("4. Homófonas")
            print("5. Antónimos")
            categoria_opcion = input("Ingresa el número de la opción deseada: ").strip()
            if categoria_opcion == "1":
                escribir_ensayo(sinonimos, "Sinónimos")
            elif categoria_opcion == "2":
                escribir_ensayo(isonimos, "Isónimos")
            elif categoria_opcion == "3":
                escribir_ensayo(homonimos, "Homónimos")
            elif categoria_opcion == "4":
                escribir_ensayo(homofonas, "Homófonas")
            elif categoria_opcion == "5":
                escribir_ensayo(antonimos, "Antónimos")
        elif opcion == "8":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")

# Ejecutar el menú principal
menu()
