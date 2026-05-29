import json
import os

# Datos iniciales
ejemplos = [
    # ... (Inserta aquí los 50 ejemplos del paso anterior en formato: {"categoria": "...", "ejemplo": "..."})
]

# Archivos para guardar datos
EJEMPLOS_FILE = "ejemplos.json"
USUARIO_FILE = "usuario_ejemplos.json"

# Cargar o inicializar datos
def cargar_datos():
    if os.path.exists(EJEMPLOS_FILE):
        with open(EJEMPLOS_FILE, 'r') as f:
            return json.load(f)
    else:
        with open(EJEMPLOS_FILE, 'w') as f:
            json.dump(ejemplos, f)
        return ejemplos

def cargar_usuario():
    if os.path.exists(USUARIO_FILE):
        with open(USUARIO_FILE, 'r') as f:
            return json.load(f)
    else:
        return []

# Menú principal
def menu_principal():
    print("\n" + "═"*40)
    print("  ESTUDIO DE DERIVADOS VERBALES - MENÚ  ")
    print("═"*40)
    print("1. Modo Estudio")
    print("2. Cuestionario Interactivo")
    print("3. Crear nuevos ejemplos")
    print("4. Ver ejemplos guardados")
    print("5. Ayuda Conceptual")
    print("6. Salir")

# Diapositiva conceptual
def ayuda_conceptual():
    print("\n" + "═"*40)
    print("  CONCEPTOS CLAVE  ")
    print("═"*40)
    print("Infinitivo: -ar, -er, -ir → Funciona como sustantivo")
    print("Participio: -ado/-ido → Con 'ser/estar' (adjetivo) o 'haber' (invariable)")
    print("Gerundio: -ando/-iendo → Modifica al verbo principal")
    print("═"*40 + "\n")

# Modo estudio
def modo_estudio():
    datos = cargar_datos() + cargar_usuario()
    for idx, item in enumerate(datos, 1):
        print(f"\nEjemplo {idx}/{len(datos)}: {item['ejemplo']}")
        respuesta = input("¿Qué categoría es? (infinitivo/participio/gerundio): ").lower()
        
        if respuesta == item['categoria']:
            print("¡Correcto! ✅")
        else:
            print(f"❌ Incorrecto. Es {item['categoria'].capitalize()}.")
        
        oracion = input("Escribe una oración usando este ejemplo: ")
        # Guardar oración (puedes implementar almacenamiento adicional aquí)
    
    print("\n¡Estudio completado!")

# Cuestionario interactivo
def cuestionario():
    datos = cargar_datos() + cargar_usuario()
    puntaje = 0
    total = min(10, len(datos))
    
    for _ in range(total):
        item = random.choice(datos)
        print(f"\nEjemplo: {item['ejemplo']}")
        respuesta = input("Categoría: ").lower()
        
        if respuesta == item['categoria']:
            print("✅ Correcto!")
            puntaje +=1
        else:
            print(f"❌ Incorrecto. Correcto: {item['categoria']}")
    
    print(f"\nPuntaje final: {puntaje}/{total}")

# Crear nuevos ejemplos
def crear_ejemplos():
    ejemplos_usuario = cargar_usuario()
    
    while len(ejemplos_usuario) < 100:
        ejemplo = input("\nIngrese el ejemplo (o 'salir'): ").strip()
        if ejemplo.lower() == 'salir':
            break
        
        # Validar terminaciones
        categoria = None
        if ejemplo.endswith(('ar', 'er', 'ir')):
            categoria = 'infinitivo'
        elif ejemplo.endswith(('ado', 'ada', 'idos', 'idas', 'ido', 'ida')):
            categoria = 'participio'
        elif ejemplo.endswith(('ando', 'endo')):
            categoria = 'gerundio'
        
        if categoria:
            ejemplos_usuario.append({'categoria': categoria, 'ejemplo': ejemplo})
            with open(USUARIO_FILE, 'w') as f:
                json.dump(ejemplos_usuario, f)
            print("¡Ejemplo guardado!")
        else:
            print("Formato no válido. Revise las terminaciones.")
    
    print("\n¡Límite de 100 ejemplos alcanzado!")

# Ver ejemplos
def ver_ejemplos():
    datos = cargar_datos() + cargar_usuario()
    for idx, item in enumerate(datos, 1):
        print(f"{idx}. [{item['categoria'].upper()}] {item['ejemplo']}")

# Ejecución principal
if __name__ == "__main__":
    import random
    cargar_datos()
    
    while True:
        menu_principal()
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == '1':
            modo_estudio()
        elif opcion == '2':
            cuestionario()
        elif opcion == '3':
            crear_ejemplos()
        elif opcion == '4':
            ver_ejemplos()
        elif opcion == '5':
            ayuda_conceptual()
        elif opcion == '6':
            print("¡Hasta luego! 👋")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
