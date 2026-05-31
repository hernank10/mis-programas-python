def menu_principal():
    print("\n***🏛️ Bienvenido a la Biblioteca de Alejandría 🏛️***")
    print("Tomson📜️🕵️✏: ¡Bienvenido, aprendiz🏛️! Esta no es una biblioteca cualquiera 📜️🕵️✏, sino el epicentro de la sabiduría.")
    print("Elige una opción para explorar:")
    print("1.  🌟📌Aprender sobre las partes de la gramática✔️")
    print("2.  🌟📌Ejercicios de nivel básico✔️")
    print("3.  🌟📌Ejercicios de nivel intermedio✔️")
    print("4.  🌟📌Ejercicios de nivel avanzado")
    print("5.  🌟📌Agregar nuevos niveles y explorar más secretos gramaticales✔️")
    print("0. Salir de la biblioteca")
    
    opcion = input("Selecciona un número: ")
    if opcion == '1':
        menu_aprender_gramatica()
    elif opcion == '2':
        nivel_basico()
    elif opcion == '3':
        nivel_intermedio()
    elif opcion == '4':
        nivel_avanzado()
    elif opcion == '5':
        agregar_nivel()
    elif opcion == '0':
        print("Tomson📜️🕵️✏: ¡Vuelve pronto, la biblioteca siempre tendrá más secretos para ti!")
    else:
        print("Opción no válida. Inténtalo de nuevo.")
        menu_principal()

def menu_aprender_gramatica():
    print("\n*** Salón de los Manuscritos: 📜️🕵️✏Aprender sobre las partes de la gramática ***")
    print("Profesora Laurent👋📖 : Aquí, los manuscritos antiguos revelan los misterios de la gramática.")
    print("1. Sustantivos")
    print("2. Verbos")
    print("3. Adjetivos")
    print("4. Pronombres")
    print("0. Volver al menú principal")
    
    opcion = input("Selecciona un número: ")
    if opcion == '1':
        print("\nKoko📟: Los sustantivos son los nombres que damos a personas, lugares o cosas. ¡Como esta biblioteca!")
    elif opcion == '2':
        print("\nProfesora Laurent👋📖: Los verbos nos permiten describir acciones, desde correr por los pasillos hasta leer en silencio.")
    elif opcion == '3':
        print("\nTomson📜️🕵: Los adjetivos pintan las palabras, describen y aportan color a lo que decimos.")
    elif opcion == '4':
        print("\nKoko📟: Los pronombres son palabras que reemplazan a los sustantivos, como 'él' o 'ella'.")
    elif opcion == '0':
        menu_principal()
    else:
        print("Opción no válida👋📖 , por favor elige de nuevo👋📖 .")
        menu_aprender_gramatica()
    menu_aprender_gramatica()

def nivel_basico():
    print("\n***🏛 Sala de los Rollos Básicos 🏛***")
    print("Tomson📝🤔: ¿Listo para tu primera misión? Encuentra los sustantivos en esta frase:")
    print("Frase: '📜️🕵El sabio explora los manuscritos antiguos de la biblioteca📜️🕵.'")
    respuesta = input("¿Cuál es el sustantivo principal👋📖?: ")
    if respuesta.lower() in ["sabio", "manuscritos", "biblioteca"]:
        print("Koko📟: ¡Correcto! Has desbloqueado una insignia de Explorador de la Sabiduría.")
    else:
        print("Profesora Laurent: No es correcto. Los sustantivos eran 'sabio', 'manuscritos' o 'biblioteca'.")
    menu_principal()

def nivel_intermedio():
    print("\n***🏛 Patio de los Jeroglíficos 🏛***")
    print("Profesora Laurent👋: Busca el verbo en esta antigua inscripción.")
    print("Frase👋👋: 'El aprendiz lee con atención cada pergamino📜️🕵.'")
    respuesta = input("¿Cuál es el verbo principal📜️🕵?: ")
    if respuesta.lower() == "lee":
        print("Tomson: ¡Bien hecho! Has ganado el título de Lector Ávido de Alejandría.")
    else:
        print("Koko📟: No es correcto, la respuesta era 'lee'. Intenta de nuevo.")
    menu_principal()

def nivel_avanzado():
    print("\n***🏛 Sala de los Desafíos Avanzados 🏛***")
    print("Profesora Laurent👋: Debes separar las sílabas de la siguiente palabra.")
    palabra = "biblioteca"
    respuesta = input(f"👋¿Cómo se separan las sílabas de la palabra '{palabra}'?: ")
    if respuesta.lower() == "bi-blio-te-ca":
        print("Koko📟: ¡Magnífico📜️✔️🕵! Has alcanzado el rango de Sabio Silábico.")
    else:
        print("Profesora Laurent👋: Incorrecto. La respuesta correcta era 'bi-blio-te-ca'.")
    menu_principal()

def agregar_nivel():
    print("\n***🏛 Agregar Nuevos Conocimientos 🏛***")
    print("Profesora Laurent👋: Puedes incluir más reglas y ejercicios en tu próxima visita.")
    print("Tomson📜️🕵: ¡Explora y expande la biblioteca para descubrir más✔️!")
    menu_principal()

# Inicia el juego
menu_principal()
