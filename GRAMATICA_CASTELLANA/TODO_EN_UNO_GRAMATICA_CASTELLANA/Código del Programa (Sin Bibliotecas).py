# Lista de oraciones para traducir (Español - Inglés)
oraciones_para_traducir = [
    ("La casa es grande.", "The house is big."),
    ("El perro corre rápido.", "The dog runs fast."),
    ("Nosotros estamos felices.", "We are happy."),
    ("Ella estudia todos los días.", "She studies every day."),
    ("El cielo está azul.", "The sky is blue."),
    ("¿Dónde está el baño?", "Where is the bathroom?"),
    ("Yo tengo un libro nuevo.", "I have a new book."),
    ("Ellos viven en Londres.", "They live in London."),
    ("Él juega al fútbol los fines de semana.", "He plays soccer on weekends."),
    ("Nos gusta viajar.", "We like to travel.")
]

# Función para mostrar una oración y verificar la traducción
def traducir_oracion(oracion, traduccion_correcta):
    print("\nTraduce la siguiente oración:")
    print(oracion)
    respuesta_usuario = input("Escribe tu traducción: ").strip()
    if respuesta_usuario.lower() == traduccion_correcta.lower():
        print("¡Correcto!")
        return True
    else:
        print(f"Incorrecto. La traducción correcta es: {traduccion_correcta}")
        return False

# Cuestionario de traducción
def cuestionario_traduccion():
    print("\n--- Cuestionario de Traducción ---")
    print("1. Español a Inglés")
    print("2. Inglés a Español")
    try:
        opcion = int(input("Elige el tipo de traducción (1/2): "))
        if opcion == 1:
            print("\n--- Traducción: Español a Inglés ---")
            puntuacion = 0
            for oracion, traduccion in oraciones_para_traducir:
                if traducir_oracion(oracion, traduccion):
                    puntuacion += 1
            print(f"\nTu puntuación final: {puntuacion}/{len(oraciones_para_traducir)}")
        elif opcion == 2:
            print("\n--- Traducción: Inglés a Español ---")
            puntuacion = 0
            for oracion, traduccion in oraciones_para_traducir:
                if traducir_oracion(traduccion, oracion):
                    puntuacion += 1
            print(f"\nTu puntuación final: {puntuacion}/{len(oraciones_para_traducir)}")
        else:
            print("Opción no válida. Inténtalo de nuevo.")
    except ValueError:
        print("Entrada inválida. Por favor, selecciona una opción válida.")

# Menú principal
def menu_principal():
    print("\n¡Bienvenido al Cuestionario de Traducción!")
    nombre_usuario = input("Por favor, ingresa tu nombre: ")
    while True:
        print("\n--- Menú Principal ---")
        print("1. Traducir Oraciones")
        print("2. Salir")
        opcion = input("Elige una opción (1-2): ")
        if opcion == "1":
            cuestionario_traduccion()
        elif opcion == "2":
            print(f"\n¡Gracias por participar, {nombre_usuario}! ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

# Ejecutar el programa
menu_principal()
