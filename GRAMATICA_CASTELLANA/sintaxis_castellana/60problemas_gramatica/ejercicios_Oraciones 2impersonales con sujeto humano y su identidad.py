import json

class PracticaVerbal:
    def __init__(self):
        self.progreso = {}
        self.puntuacion = 0
        self.cargar_progreso()

    def cargar_progreso(self):
        try:
            with open("progreso.json", "r") as file:
                self.progreso = json.load(file)
                self.puntuacion = self.progreso.get("puntuacion", 0)
        except FileNotFoundError:
            self.progreso = {}

    def guardar_progreso(self):
        self.progreso["puntuacion"] = self.puntuacion
        with open("progreso.json", "w") as file:
            json.dump(self.progreso, file, indent=4)

    def mostrar_ejercicio(self, enunciado, respuesta_correcta):
        print(f"\n{enunciado}")
        respuesta = input("Tu respuesta: ")
        if respuesta.strip().lower() == respuesta_correcta.lower():
            print("✅ Correcto!")
            self.puntuacion += 1
        else:
            print(f"❌ Incorrecto. La respuesta correcta era: {respuesta_correcta}")
        self.guardar_progreso()

    def completar_oraciones(self):
        print("\n📝 Completar oraciones:")
        ejercicios = [
            ("_______ se dice que la gramática es compleja.", "Se"),
            ("_______ necesita estudiar más para mejorar en español.", "Se"),
            ("En este país, _______ habla español con fluidez.", "se")
        ]
        for enunciado, respuesta in ejercicios:
            self.mostrar_ejercicio(enunciado, respuesta)

    def identificacion_oraciones(self):
        print("\n✅ Identificación de oraciones impersonales:")
        ejercicios = [
            ("Se dice que mañana lloverá.", "Sí"),
            ("Pedro ha comprado un coche nuevo.", "No"),
            ("En esta escuela, se enseña inglés.", "Sí")
        ]
        for enunciado, respuesta in ejercicios:
            self.mostrar_ejercicio(f"¿Es esta una oración impersonal? {enunciado}", respuesta)

    def reescribir_oraciones(self):
        print("\n✍️ Reescribir oraciones en forma impersonal:")
        ejemplos = [
            "Juan paseó por el parque.",
            "El profesor explicó la lección.",
            "María vendió todas las entradas.",
            "Ellos arreglaron el coche.",
            "Los estudiantes resolvieron el examen."
        ]
        for oracion in ejemplos:
            print(f"\nReescribe esta oración de forma impersonal: {oracion}")
            respuesta = input("Tu respuesta: ")
            self.progreso[oracion] = respuesta
        self.guardar_progreso()

    def mostrar_progreso(self):
        print("\n📊 Progreso:")
        print(f"Puntuación: {self.puntuacion}")
        for ejercicio, respuesta in self.progreso.items():
            if ejercicio != "puntuacion":
                print(f"- {ejercicio}: {respuesta}")

    def menu(self):
        while True:
            print("\n📚 Práctica sobre valores de 'se' en el verbo")
            print("1. Completar oraciones")
            print("2. Identificar oraciones impersonales")
            print("3. Reescribir oraciones en forma impersonal")
            print("4. Ver progreso y puntuación")
            print("5. Salir")
            opcion = input("Elige una opción: ")
            
            if opcion == "1":
                self.completar_oraciones()
            elif opcion == "2":
                self.identificacion_oraciones()
            elif opcion == "3":
                self.reescribir_oraciones()
            elif opcion == "4":
                self.mostrar_progreso()
            elif opcion == "5":
                print("👋 ¡Hasta luego!")
                break
            else:
                print("❌ Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    practica = PracticaVerbal()
    practica.menu()
