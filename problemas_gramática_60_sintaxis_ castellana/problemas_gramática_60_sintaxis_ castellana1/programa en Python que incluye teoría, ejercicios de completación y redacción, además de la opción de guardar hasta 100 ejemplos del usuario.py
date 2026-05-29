import json

class NegacionGerundioApp:
    def __init__(self):
        self.ejemplos_usuario = []
        self.cargar_datos()

    def cargar_datos(self):
        try:
            with open("ejemplos.json", "r", encoding="utf-8") as file:
                self.ejemplos_usuario = json.load(file)
        except FileNotFoundError:
            self.ejemplos_usuario = []

    def guardar_datos(self):
        with open("ejemplos.json", "w", encoding="utf-8") as file:
            json.dump(self.ejemplos_usuario, file, ensure_ascii=False, indent=4)

    def mostrar_teoria(self):
        print("""
        **Teoría sobre la negación con gerundio en español:**
        - La construcción <no + gerundio> no es aceptada en todos los casos.
        - En algunos contextos, se prefiere <sin + infinitivo>.
        - Ejemplo correcto: "Juan fumaba sin tragarse el humo."
        - Ejemplo no aceptado: "Aprobó el examen no estudiando." (Se debe decir "sin estudiar").
        """)

    def ejercicio_completacion(self):
        print("Completa la siguiente oración:")
        oracion = "Aprobó el examen _______ estudiar."
        respuesta = input("Tu respuesta: ")
        if respuesta.lower().strip() == "sin":
            print("Correcto! 'sin estudiar' es la forma correcta.")
        else:
            print("Incorrecto. La forma correcta es 'sin estudiar'.")

    def ejercicio_redaccion(self):
        if len(self.ejemplos_usuario) >= 100:
            print("Has alcanzado el límite de 100 ejemplos guardados.")
            return
        
        ejemplo = input("Escribe una oración usando correctamente 'no + gerundio' o 'sin + infinitivo': ")
        self.ejemplos_usuario.append(ejemplo)
        self.guardar_datos()
        print("Ejemplo guardado correctamente.")

    def menu(self):
        while True:
            print("\nMenú de opciones:")
            print("1. Ver teoría")
            print("2. Ejercicio de completación")
            print("3. Ejercicio de redacción")
            print("4. Ver ejemplos guardados")
            print("5. Salir")
            opcion = input("Elige una opción: ")

            if opcion == "1":
                self.mostrar_teoria()
            elif opcion == "2":
                self.ejercicio_completacion()
            elif opcion == "3":
                self.ejercicio_redaccion()
            elif opcion == "4":
                print("Ejemplos guardados:")
                for i, ejemplo in enumerate(self.ejemplos_usuario, 1):
                    print(f"{i}. {ejemplo}")
            elif opcion == "5":
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    app = NegacionGerundioApp()
    app.menu()
