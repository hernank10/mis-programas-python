import re
import pyperclip
from colorama import Fore, Style, init

init(autoreset=True)  # Para colores en la consola

class GerundioConsola:
    def __init__(self):
        self.categorias = {
            1: {
                "nombre": "Simultaneidad",
                "ejemplos": [
                    "El niño terminó la tarea silbando una canción",
                    "La bailarina giró extendiendo los brazos"
                ]
            },
            2: {
                "nombre": "Modo",
                "ejemplos": [
                    "El perro escapó saltando la cerca",
                    "El bombero rescató al gato trepando al árbol"
                ]
            },
            3: {
                "nombre": "Errores Comunes",
                "ejemplos": [
                    "✖ Terminó el examen yéndose del aula → ✓ Salió después de terminar"
                ]
            }
        }
        
        self.ejercicios = [
            ("El niño comió helado (derramar)", "El niño comió helado derramando gotas"),
            ("La actriz declamó (gesticular)", "La actriz declamó gesticulando exageradamente")
        ]
        
        self.puntaje = 0

    def mostrar_menu_principal(self):
        print("\n" + "═"*50)
        print(f"{Fore.CYAN} PRÁCTICA DE GERUNDIOS ".center(50, '═'))
        print("═"*50)
        print(f"{Fore.YELLOW}1. Ver categorías y ejemplos")
        print(f"{Fore.YELLOW}2. Practicar con ejercicios")
        print(f"{Fore.YELLOW}3. Crear nuevos ejemplos")
        print(f"{Fore.YELLOW}4. Mostrar puntaje")
        print(f"{Fore.RED}5. Salir")
        print("═"*50 + Style.RESET_ALL)

    def resaltar_gerundios(self, texto):
        palabras = texto.split()
        for palabra in palabras:
            limpia = re.sub(r'[^\w]', '', palabra).lower()
            if re.search(r'(ando|iendo)$', limpia):
                print(f"{Fore.BLUE}{palabra}{Style.RESET_ALL}", end=' ')
            else:
                print(palabra, end=' ')
        print()

    def mostrar_categorias(self):
        print("\n" + "═"*50)
        print(f"{Fore.GREEN} CATEGORÍAS DISPONIBLES ".center(50, '═'))
        for key in self.categorias:
            print(f"{Fore.YELLOW}{key}. {self.categorias[key]['nombre']}")
        print("═"*50 + Style.RESET_ALL)

    def mostrar_ejemplos(self, categoria):
        print(f"\n{Fore.GREEN}Ejemplos de {self.categorias[categoria]['nombre']}:")
        for idx, ejemplo in enumerate(self.categorias[categoria]['ejemplos'], 1):
            print(f"\n{idx}. ", end='')
            self.resaltar_gerundios(ejemplo)

    def practicar_ejercicios(self):
        print("\n" + "═"*50)
        print(f"{Fore.MAGENTA} MODO PRÁCTICA ".center(50, '═'))
        for ejercicio, respuesta in self.ejercicios:
            print(f"\n{Fore.WHITE}Reescribe usando gerundio:")
            print(f"Original: {ejercicio}")
            user_input = input("Tu versión: ")
            
            if any(palabra.endswith(('ando', 'iendo')) for palabra in user_input.split()):
                self.puntaje += 10
                print(f"{Fore.GREEN}✓ Correcto! +10 puntos")
                print(f"Versión sugerida: {respuesta}")
            else:
                self.puntaje = max(0, self.puntaje - 5)
                print(f"{Fore.RED}✗ Falta gerundio! -5 puntos")
        print("═"*50 + Style.RESET_ALL)

    def crear_ejemplo(self):
        print("\n" + "═"*50)
        print(f"{Fore.CYAN} CREAR NUEVO EJEMPLO ".center(50, '═'))
        self.mostrar_categorias()
        categoria = int(input("Selecciona categoría (número): "))
        sujeto = input("Ingresa el sujeto (ej: El gato): ")
        verbo = input("Ingresa el verbo en infinitivo (ej: correr): ").lower()
        
        if verbo.endswith('ar'):
            gerundio = verbo[:-2] + 'ando'
        elif verbo.endswith(('er', 'ir')):
            gerundio = verbo[:-2] + 'iendo'
        else:
            gerundio = verbo + ' (gerundio irregular)'
        
        nueva_oracion = f"{sujeto} está {gerundio}"
        self.categorias[categoria]['ejemplos'].append(nueva_oracion)
        print(f"\n{Fore.GREEN}Nueva oración creada:")
        self.resaltar_gerundios(nueva_oracion)
        print("═"*50 + Style.RESET_ALL)

    def copiar_ejemplos(self, categoria):
        ejemplos = '\n'.join(self.categorias[categoria]['ejemplos'])
        pyperclip.copy(ejemplos)
        print(f"{Fore.GREEN}¡Ejemplos copiados al portapapeles!")

    def ejecutar(self):
        while True:
            self.mostrar_menu_principal()
            opcion = input("\nSelecciona una opción: ")

            if opcion == '1':
                self.mostrar_categorias()
                cat = int(input("\nIngresa el número de categoría: "))
                self.mostrar_ejemplos(cat)
                if input("\n¿Copiar ejemplos? (s/n): ").lower() == 's':
                    self.copiar_ejemplos(cat)

            elif opcion == '2':
                self.practicar_ejercicios()

            elif opcion == '3':
                self.crear_ejemplo()

            elif opcion == '4':
                print(f"\n{Fore.YELLOW}Puntaje actual: {self.puntaje}")

            elif opcion == '5':
                print(f"{Fore.RED}\n¡Hasta luego! Sigue practicando tus gerundios.")
                break

            else:
                print(f"{Fore.RED}Opción inválida. Intenta nuevamente.")

if __name__ == "__main__":
    practica = GerundioConsola()
    practica.ejecutar()
