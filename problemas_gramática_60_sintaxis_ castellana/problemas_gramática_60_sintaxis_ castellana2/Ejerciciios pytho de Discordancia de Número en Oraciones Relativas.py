import json

class ConcordanciaEjercicios:
    def __init__(self):
        self.ejemplos_usuario = []
        self.max_ejemplos = 100
        self.teoria = """
        Discordancia de Número en Oraciones Relativas:
        En construcciones partitivas como "Fui de los que se {negaron/negó} a aceptar la propuesta", 
        el verbo puede aparecer en plural o singular. La normativa favorece el plural porque el sujeto 
        de la relativa es "los que", pero el singular se usa por una reestructuración sintáctica.
        """
        self.ejercicios_completacion = [
            ("Pedro fue de los que se ______ (opuso/opusieron) a la decisión.", "opusieron"),
            ("Ana es de las que siempre ______ (defiende/defienden) sus ideas.", "defienden"),
            ("Luis es de los que nunca ______ (acepta/aceptan) una derrota.", "aceptan")
        ]
        self.ejercicios_traduccion = [
            ("Fui de los que se negaron a aceptar la propuesta.", "I was one of those who refused to accept the proposal."),
            ("Él era de los que siempre defendían sus ideas.", "He was one of those who always defended their ideas."),
            ("Ana es de las que nunca aceptan una crítica.", "Ana is one of those who never accept criticism.")
        ]
    
    def mostrar_teoria(self):
        print(self.teoria)
    
    def practicar_completacion(self):
        print("Ejercicios de completación:")
        for i, (oracion, respuesta) in enumerate(self.ejercicios_completacion, 1):
            user_input = input(f"{i}. {oracion}\nSu respuesta: ").strip()
            while user_input.lower() != respuesta.lower():
                print("❌ Incorrecto. Intente de nuevo.")
                user_input = input(f"{i}. {oracion}\nSu respuesta: ").strip()
            print("✅ Correcto!")
    
    def practicar_redaccion(self):
        if len(self.ejemplos_usuario) >= self.max_ejemplos:
            print("Has alcanzado el límite de ejemplos guardados (100).")
            return
        ejemplo = input("Escribe tu propia oración siguiendo el patrón de discordancia: ")
        self.ejemplos_usuario.append(ejemplo)
        print("Ejemplo guardado correctamente.")
    
    def practicar_traduccion(self):
        print("Ejercicios de traducción (Español - Inglés):")
        for i, (oracion_es, oracion_en) in enumerate(self.ejercicios_traduccion, 1):
            user_input = input(f"{i}. Traduce al inglés: '{oracion_es}'\nSu respuesta: ").strip()
            while user_input.lower() != oracion_en.lower():
                print("❌ Incorrecto. Intente de nuevo.")
                user_input = input(f"{i}. Traduce al inglés: '{oracion_es}'\nSu respuesta: ").strip()
            print("✅ Correcto!")
    
    def guardar_ejemplos(self, archivo="ejemplos_usuario.json"):
        with open(archivo, "w") as f:
            json.dump(self.ejemplos_usuario, f, ensure_ascii=False, indent=4)
        print("Ejemplos guardados en archivo.")
    
    def cargar_ejemplos(self, archivo="ejemplos_usuario.json"):
        try:
            with open(archivo, "r") as f:
                self.ejemplos_usuario = json.load(f)
            print("Ejemplos cargados correctamente.")
        except FileNotFoundError:
            print("No hay ejemplos guardados aún.")
    
    def menu(self):
        while True:
            print("\nMenú de práctica")
            print("1. Ver teoría")
            print("2. Practicar completación")
            print("3. Escribir y guardar ejemplos")
            print("4. Practicar traducción (Español - Inglés)")
            print("5. Guardar ejemplos en archivo")
            print("6. Cargar ejemplos desde archivo")
            print("7. Salir")
            
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                self.mostrar_teoria()
            elif opcion == "2":
                self.practicar_completacion()
            elif opcion == "3":
                self.practicar_redaccion()
            elif opcion == "4":
                self.practicar_traduccion()
            elif opcion == "5":
                self.guardar_ejemplos()
            elif opcion == "6":
                self.cargar_ejemplos()
            elif opcion == "7":
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    app = ConcordanciaEjercicios()
    app.menu()
