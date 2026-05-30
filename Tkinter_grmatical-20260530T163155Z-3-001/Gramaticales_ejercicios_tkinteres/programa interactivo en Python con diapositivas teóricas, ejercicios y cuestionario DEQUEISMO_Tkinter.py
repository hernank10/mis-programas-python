import os
import random
from collections import deque

MAX_EJEMPLOS = 100
ARCHIVO_EJEMPLOS = "ejemplos.txt"

# Cargar ejemplos desde archivo
def cargar_ejemplos():
    ejemplos = []
    if os.path.exists(ARCHIVO_EJEMPLOS):
        with open(ARCHIVO_EJEMPLOS, "r", encoding="utf-8") as f:
            for linea in f.readlines():
                tipo, oracion, correccion = linea.strip().split("|")
                ejemplos.append((tipo, oracion, correccion))
    return ejemplos

def guardar_ejemplo(tipo, oracion, correccion):
    with open(ARCHIVO_EJEMPLOS, "a", encoding="utf-8") as f:
        f.write(f"{tipo}|{oracion}|{correccion}\n")

def mostrar_teoria():
    teoria = [
        ("📖 DEQUEÍSMO", 
         "Error de usar 'de que' cuando no es necesario:\n\n"
         "Incorrecto: ➤ 'Pienso de que lloverá'\n"
         "Correcto:   ✅ 'Pienso que lloverá'\n\n"
         "Regla: Si se puede reemplazar por 'eso', usar QUE\n"
         "Ejemplo: 'Pienso eso' → 'Pienso QUE...'"),
         
        ("📖 QUEÍSMO", 
         "Error de omitir 'de' cuando es necesario:\n\n"
         "Incorrecto: ➤ 'Estoy seguro que vendrá'\n"
         "Correcto:   ✅ 'Estoy seguro DE que vendrá'\n\n"
         "Regla: Si se puede reemplazar por 'de eso', usar DE QUE\n"
         "Ejemplo: 'Hablaron de eso' → 'Hablaron DE QUE...'")
    ]
    
    for titulo, contenido in teoria:
        print("\n" + "═" * 50)
        print(f"\n{titulo}\n")
        print(contenido)
        input("\nPresiona Enter para continuar...")

def agregar_ejemplo():
    ejemplos = cargar_ejemplos()
    if len(ejemplos) >= MAX_EJEMPLOS:
        print(f"❌ Límite de {MAX_EJEMPLOS} ejemplos alcanzado")
        return
    
    print("\n" + "✍ AGREGAR EJEMPLO ✍".center(50))
    tipo = input("\nTipo (queismo/dequeismo): ").lower()
    while tipo not in ["queismo", "dequeismo"]:
        print("Solo 'queismo' o 'dequeismo'!")
        tipo = input("Tipo (queismo/dequeismo): ").lower()
    
    oracion = input("\nOración incorrecta: ").strip()
    correccion = input("Oración corregida: ").strip()
    
    guardar_ejemplo(tipo, oracion, correccion)
    print("✅ Ejemplo guardado exitosamente!")

def cuestionario_interactivo():
    ejemplos = cargar_ejemplos()
    random.shuffle(ejemplos)
    puntaje = 0
    
    print("\n" + "🎯 CUESTIONARIO INTERACTIVO 🎯".center(50))
    
    for i, (tipo, incorrecta, correcta) in enumerate(ejemplos[:10], 1):
        print("\n" + "-" * 50)
        print(f"\nPregunta {i}/10")
        tipo_pregunta = random.choice(["identificacion", "correccion", "clasificacion"])
        
        if tipo_pregunta == "identificacion":
            print(f"\nIdentifica el error en:\n'{incorrecta}'")
            print("\na) Queísmo\nb) Dequeísmo\nc) Correcto")
            respuesta = input("\nOpción (a/b/c): ").lower()
            correcto = "a" if tipo == "queismo" else "b" if tipo == "dequeismo" else "c"
            
        elif tipo_pregunta == "correccion":
            print(f"\nCorrige la oración:\n'{incorrecta}'")
            respuesta = input("\nTu corrección: ").strip()
            correcto = correcta
            
        elif tipo_pregunta == "clasificacion":
            print(f"\n¿Es correcta esta oración?\n'{incorrecta if random.random() < 0.5 else correcta}'")
            respuesta = input("\n(a) Correcta\n(b) Incorrecta\nOpción (a/b): ").lower()
            es_correcta = (incorrecta == correcta)  # Solo verdadero si la oración ya era correcta
            correcto = "a" if es_correcta else "b"
        
        if respuesta == correcto:
            print("✅ Correcto! +10 puntos")
            puntaje += 10
        else:
            print(f"❌ Incorrecto. La respuesta correcta era: {correcto}")
        
        time.sleep(1)
    
    print("\n" + "⭐ PUNTUACIÓN FINAL ⭐".center(50))
    print(f"\nTotal: {puntaje}/100 puntos")
    if puntaje == 100:
        print("🏆 ¡Perfecto! Dominas el tema completamente!")
    elif puntaje >= 70:
        print("👍 ¡Buen trabajo! Sigue practicando")
    else:
        print("💪 ¡Sigue intentándolo! La práctica hace al maestro")

def menu_principal():
    while True:
        print("\n" + "=" * 50)
        print(" MENÚ PRINCIPAL ".center(50))
        print("1. Teoría y ejemplos")
        print("2. Agregar nuevo ejemplo")
        print("3. Cuestionario interactivo")
        print("4. Ver todos los ejemplos")
        print("5. Salir")
        
        opcion = input("\nElige una opción (1-5): ")
        
        if opcion == "1":
            mostrar_teoria()
        elif opcion == "2":
            agregar_ejemplo()
        elif opcion == "3":
            cuestionario_interactivo()
        elif opcion == "4":
            mostrar_ejemplos()
        elif opcion == "5":
            print("\n¡Gracias por usar el programa! Hasta pronto 👋")
            break
        else:
            print("❌ Opción no válida. Intenta nuevamente.")

def mostrar_ejemplos():
    ejemplos = cargar_ejemplos()
    print("\n" + "🗂 EJEMPLOS ALMACENADOS 🗂".center(50))
    for idx, (tipo, incorrecta, correcta) in enumerate(ejemplos, 1):
        print(f"\n{idx}. [{tipo.upper()}]")
        print(f"   Original:   {incorrecta}")
        print(f"   Corregido:  {correcta}")
    input("\nPresiona Enter para volver al menú...")

if __name__ == "__main__":
    # Inicializar archivo si no existe
    if not os.path.exists(ARCHIVO_EJEMPLOS):
        with open(ARCHIVO_EJEMPLOS, "w") as f:
            pass
    
    menu_principal()
