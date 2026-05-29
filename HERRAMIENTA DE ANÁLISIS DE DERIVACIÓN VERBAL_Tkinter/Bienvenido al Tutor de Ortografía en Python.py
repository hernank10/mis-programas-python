import json
import pyttsx3
from tabulate import tabulate

class PracticaOrtografia:
    def __init__(self):
        self.ejemplos = []
        self.categorias = {
            1: "B/V", 
            2: "C/S/Z",
            3: "G/J",
            4: "LL/Y",
            5: "H muda",
            6: "Dígrafos",
            7: "Diptongos/Hiatos",
            8: "Tildes",
            9: "Homófonas/Etimológicas"
        }
        self.progreso = {v: 0 for v in self.categorias.values()}
        self.engine = pyttsx3.init()
        self.cargar_datos()

    def cargar_datos(self):
        try:
            with open('ejemplos.json') as f:
                data = json.load(f)
                self.ejemplos = data['ejemplos']
                self.progreso = data['progreso']
        except FileNotFoundError:
            pass

    def guardar_datos(self):
        with open('ejemplos.json', 'w') as f:
            json.dump({'ejemplos': self.ejemplos, 'progreso': self.progreso}, f)

    def mostrar_menu(self):
        print("\n" + "═"*50)
        print(" PRÁCTICA DE ORTOGRAFÍA - MENÚ PRINCIPAL ")
        print("═"*50)
        print("1. 🆕 Agregar nuevo ejemplo")
        print("2. ✏️ Editar ejemplo existente")
        print("3. 👀 Ver todos los ejemplos")
        print("4. 🔊 Escuchar ejemplo")
        print("5. 📊 Ver progreso")
        print("6. 🚪 Salir")
        return input("Seleccione una opción: ")

    def agregar_ejemplo(self):
        if len(self.ejemplos) >= 100:
            print("¡Límite de 100 ejemplos alcanzado!")
            return
            
        print("\n" + "═"*50)
        print(" CATEGORÍAS DISPONIBLES ")
        print("═"*50)
        for num, cat in self.categorias.items():
            print(f"{num}. {cat}")
            
        categoria = input("\nSeleccione el número de categoría: ")
        palabra = input("Palabra a practicar: ")
        oracion = input("Oración de ejemplo: ")
        regla = input("Regla ortográfica aplicable: ")
        
        if categoria.isdigit() and int(categoria) in self.categorias:
            cat_seleccionada = self.categorias[int(categoria)]
            nuevo_ejemplo = {
                'categoria': cat_seleccionada,
                'palabra': palabra,
                'oracion': oracion,
                'regla': regla
            }
            self.ejemplos.append(nuevo_ejemplo)
            self.progreso[cat_seleccionada] += 1
            self.guardar_datos()
            print("✅ Ejemplo agregado correctamente!")
        else:
            print("❌ Categoría inválida")

    def editar_ejemplo(self):
        self.ver_ejemplos()
        try:
            idx = int(input("\nIngrese el número de ejemplo a editar: ")) - 1
            ejemplo = self.ejemplos[idx]
            
            print("\nDeje en blanco para mantener el valor actual")
            nueva_palabra = input(f"Nueva palabra ({ejemplo['palabra']}): ") or ejemplo['palabra']
            nueva_oracion = input(f"Nueva oración ({ejemplo['oracion']}): ") or ejemplo['oracion']
            nueva_regla = input(f"Nueva regla ({ejemplo['regla']}): ") or ejemplo['regla']
            
            self.ejemplos[idx] = {
                'categoria': ejemplo['categoria'],
                'palabra': nueva_palabra,
                'oracion': nueva_oracion,
                'regla': nueva_regla
            }
            self.guardar_datos()
            print("✅ Ejemplo actualizado!")
        except (ValueError, IndexError):
            print("❌ Índice inválido")

    def ver_ejemplos(self):
        print("\n" + "═"*50)
        print(" LISTA DE EJEMPLOS ")
        print("═"*50)
        if not self.ejemplos:
            print("No hay ejemplos registrados")
            return
            
        headers = ["#", "Categoría", "Palabra", "Oración", "Regla"]
        tabla = []
        for i, ej in enumerate(self.ejemplos, 1):
            tabla.append([i, ej['categoria'], ej['palabra'], ej['oracion'], ej['regla']])
        print(tabulate(tabla, headers=headers, tablefmt="grid"))

    def escuchar_ejemplo(self):
        self.ver_ejemplos()
        try:
            idx = int(input("\nIngrese el número de ejemplo a escuchar: ")) - 1
            ejemplo = self.ejemplos[idx]
            texto = f"Palabra: {ejemplo['palabra']}. Oración: {ejemplo['oracion']}"
            self.engine.say(texto)
            self.engine.runAndWait()
        except (ValueError, IndexError):
            print("❌ Índice inválido")

    def mostrar_progreso(self):
        print("\n" + "═"*50)
        print(" PROGRESO POR CATEGORÍA ")
        print("═"*50)
        headers = ["Categoría", "Ejemplos Registrados"]
        tabla = [[k, v] for k, v in self.progreso.items()]
        print(tabulate(tabla, headers=headers, tablefmt="grid"))

    def ejecutar(self):
        while True:
            opcion = self.mostrar_menu()
            
            if opcion == '1':
                self.agregar_ejemplo()
            elif opcion == '2':
                self.editar_ejemplo()
            elif opcion == '3':
                self.ver_ejemplos()
            elif opcion == '4':
                self.escuchar_ejemplo()
            elif opcion == '5':
                self.mostrar_progreso()
            elif opcion == '6':
                self.guardar_datos()
                print("¡Hasta pronto! 👋")
                break
            else:
                print("Opción inválida, intente nuevamente")

if __name__ == "__main__":
    print("¡Bienvenido al Tutor de Ortografía en Python! 📚✍️")
    app = PracticaOrtografia()
    app.ejecutar()
