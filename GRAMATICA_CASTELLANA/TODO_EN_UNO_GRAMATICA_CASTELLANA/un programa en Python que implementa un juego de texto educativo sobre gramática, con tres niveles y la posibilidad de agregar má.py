class JuegoDeGramatica:
    def __init__(self):
        self.niveles = {
            1: 'Aprender sobre las partes de la gramática',
            2: 'Ejercicios de nivel básico',
            3: 'Ejercicios de nivel intermedio',
            4: 'Ejercicios de nivel avanzado'
        }
        self.recompensas = []

    def mostrar_menu(self):
        print("\nBienvenido al Juego de Gramática")
        print("Elige una opción:")
        for nivel, descripcion in self.niveles.items():
            print(f"{nivel}. {descripcion}")
        print("0. Salir")

    def jugar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Selecciona un número: ")
            if opcion == '0':
                print("¡Gracias por jugar! Hasta la próxima.")
                break
            elif opcion in ['1', '2', '3', '4']:
                self.procesar_nivel(int(opcion))
            else:
                print("Opción no válida, por favor elige de nuevo.")

    def procesar_nivel(self, nivel):
        if nivel == 1:
            print("\n*** Nivel 1: Aprender sobre las partes de la gramática ***")
            print("La profesora Laurent te enseña las diferentes partes de la gramática: sustantivos, verbos, adjetivos, etc.")
            print("Tomson y Koko también te acompañan en esta clase.")
            input("Presiona Enter para continuar...")
        elif nivel == 2:
            print("\n*** Nivel 2: Ejercicios de nivel básico ***")
            print("Misión: Completa ejercicios sencillos para identificar las partes de la oración.")
            self.mision_basica()
        elif nivel == 3:
            print("\n*** Nivel 3: Ejercicios de nivel intermedio ***")
            print("Misión: Resuelve preguntas sobre separación de sílabas y formación de diptongos.")
            self.mision_intermedia()
        elif nivel == 4:
            print("\n*** Nivel 4: Ejercicios de nivel avanzado ***")
            print("Misión: Completa desafíos sobre triptongos y acentuación.")
            self.mision_avanzada()
        else:
            print("Nivel no disponible aún. ¡Vuelve más tarde!")

    def mision_basica(self):
        print("Tomson: ¡Vamos, Koko! Ayuda a completar esta oración:")
        print("Ejercicio: ¿Cuál es el sustantivo en la siguiente frase? 'El perro juega en el parque.'")
        respuesta = input("Tu respuesta: ")
        if respuesta.lower() == "perro":
            print("¡Correcto! Ganaste una insignia de Explorador Gramático.")
            self.recompensas.append("Insignia de Explorador Gramático")
        else:
            print("Incorrecto, la respuesta era 'perro'.")

    def mision_intermedia(self):
        print("Profesora Laurent: Vamos a practicar la separación de sílabas.")
        print("Ejercicio: Separa la palabra 'aventura' en sílabas.")
        respuesta = input("Tu respuesta (ejemplo: a-ven-tu-ra): ")
        if respuesta == "a-ven-tu-ra":
            print("¡Bien hecho! Has completado la misión de las sílabas.")
            self.recompensas.append("Insignia de Separador de Sílabas")
        else:
            print("Respuesta incorrecta. Intenta de nuevo la próxima vez.")

    def mision_avanzada(self):
        print("Tomson: ¡Este es un desafío complejo, pero sé que puedes hacerlo!")
        print("Ejercicio: ¿La palabra 'hacia' contiene un diptongo o un triptongo?")
        respuesta = input("Tu respuesta (diptongo/triptongo): ")
        if respuesta.lower() == "diptongo":
            print("¡Correcto! Has ganado la Insignia de Maestro de Diptongos.")
            self.recompensas.append("Insignia de Maestro de Diptongos")
        else:
            print("Incorrecto, la respuesta es 'diptongo'.")

        print("\nRecompensas obtenidas:")
        for r in self.recompensas:
            print(f"- {r}")
        input("Presiona Enter para continuar...")

# Iniciar el juego
juego = JuegoDeGramatica()
juego.jugar()
