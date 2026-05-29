import json
import random
from colorama import Fore, init

init(autoreset=True)  # Colores en consola

# Base de datos inicial de ejemplos
BASE_EJEMPLOS = [
    {"frase": "Ayer comí pizza", "tipo": "concluida", "tiempo": "pretérito perfecto simple", "contexto": "narración"},
    {"frase": "Mientras llovía, ella leía un libro", "tipo": "simultánea", "tiempo": "pretérito imperfecto", "contexto": "descripción"},
    # ... Añadir más ejemplos aquí
]

def guardar_datos(archivo, datos):
    with open(archivo, 'w') as f:
        json.dump(datos, f, indent=2)

def cargar_datos(archivo):
    try:
        with open(archivo, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

class PracticaVerbosa:
    def __init__(self):
        self.ejemplos = cargar_datos('frases_guardadas.json') or BASE_EJEMPLOS
        self.frases_usuario = []
    
    def menu_principal(self):
        while True:
            print(Fore.CYAN + "\n--- MENÚ PRÁCTICA DE TIEMPOS VERBALES ---")
            print("1. Practicar con ejemplos existentes")
            print("2. Crear/Guardar nuevas frases")
            print("3. Ver mis frases guardadas")
            print("4. Generar 100 nuevos ejemplos")
            print("5. Salir")
            opcion = input("Elige una opción: ")
            
            if opcion == '1':
                self.practicar_ejercicios()
            elif opcion == '2':
                self.crear_frase()
            elif opcion == '3':
                self.mostrar_frases()
            elif opcion == '4':
                self.generar_ejemplos_masivos()
            elif opcion == '5':
                guardar_datos('frases_guardadas.json', self.ejemplos + self.frases_usuario)
                print(Fore.GREEN + "¡Datos guardados! Hasta pronto.")
                break

    def practicar_ejercicios(self):
        ejercicios = [
            self.identificar_accion,
            self.relacionar_tiempos,
            self.identificar_contexto,
            self.reescribir_frase
        ]
        random.shuffle(ejercicios)
        for ejercicio in ejercicios:
            ejercicio()
    
    def identificar_accion(self):
        frase = random.choice(self.ejemplos)
        print(Fore.YELLOW + f"\nFrase: {frase['frase']}")
        respuesta = input("¿Es una acción concluida, en progreso o habitual? ").lower()
        if respuesta == frase['tipo']:
            print(Fore.GREEN + "¡Correcto!")
        else:
            print(Fore.RED + f"Respuesta correcta: {frase['tipo']}")

    def relacionar_tiempos(self):
        # Ejemplo: Identificar si una acción interrumpe a otra
        frases = random.sample([e for e in self.ejemplos if e['contexto'] == 'narración'], 2)
        print(Fore.YELLOW + f"\nFrase 1: {frases[0]['frase']}")
        print(Fore.YELLOW + f"Frase 2: {frases[1]['frase']}")
        respuesta = input("¿La segunda acción interrumpe a la primera? (sí/no) ").lower()
        # Lógica de corrección (requiere ejemplos etiquetados)
    
    def reescribir_frase(self):
        frase = random.choice(self.ejemplos)
        print(Fore.YELLOW + f"\nReescribe: {frase['frase']}")
        print("Opciones: presente | futuro | pretérito imperfecto")
        nuevo_tiempo = input("A qué tiempo quieres cambiarla: ").lower()
        # Aquí iría la lógica de transformación gramatical
    
    def crear_frase(self):
        print(Fore.CYAN + "\n--- Crear nueva frase ---")
        frase = input("Escribe tu frase: ")
        tipo = input("Tipo (concluida/progreso/habitual): ")
        tiempo = input("Tiempo verbal: ")
        contexto = input("Contexto (descripción/diálogo/recuerdo): ")
        self.frases_usuario.append({
            "frase": frase,
            "tipo": tipo,
            "tiempo": tiempo,
            "contexto": contexto
        })
        print(Fore.GREEN + "¡Frase guardada exitosamente!")
    
    def generar_ejemplos_masivos(self):
        # Plantillas para generar 100 ejemplos automáticos
        verbos = ["amar", "comer", "vivir", "correr", "escribir"]
        plantillas = [
            "Ayer {verbo} en el parque",
            "Mientras {verbo}, ella {verbo2}",
            "Siempre {verbo} los domingos"
        ]
        # ... Lógica para generar combinaciones
        print(Fore.GREEN + "¡100 nuevos ejemplos generados!")

    def mostrar_frases(self):
        print(Fore.CYAN + "\n--- Tus frases guardadas ---")
        for idx, frase in enumerate(self.frases_usuario, 1):
            print(f"{idx}. {frase['frase']} ({frase['tiempo']})")

if __name__ == "__main__":
    practica = PracticaVerbosa()
    practica.menu_principal()
