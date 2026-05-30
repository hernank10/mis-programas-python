import json
import random
from pathlib import Path

# Configuración inicial
DB_FILE = "ejemplos_guardados.json"
MAX_EJEMPLOS = 100

# Teoría integrada
TEORIA = """
📚 TEORÍA: Frases Subordinadas Explicativas vs. Especificativas

1. Explicativas:
   - Agregan información adicional no esencial.
   - Van entre comas.
   - Ej: "El río Magdalena, que es el más largo de Colombia, cruza varias regiones."

2. Especificativas:
   - Definen o restringen el significado del antecedente.
   - No usan comas.
   - Ej: "Los libros que tienen tapas rojas son clásicos."

Clave: Si al quitar la subordinada el sentido esencial se mantiene, es explicativa.
"""

# Base de datos inicial
ejemplos_base = [
    # ... (incluir aquí los 50 ejemplos previos en formato diccionario)
]

# Cargar/Crear archivo de ejemplos personalizados
def cargar_ejemplos():
    try:
        if Path(DB_FILE).exists():
            with open(DB_FILE, 'r') as f:
                return json.load(f)
        return []
    except:
        return []

def guardar_ejemplo(ejemplo):
    ejemplos = cargar_ejemplos()
    if len(ejemplos) >= MAX_EJEMPLOS:
        print("❌ Límite alcanzado (100 ejemplos). Borra algunos primero.")
        return False
    ejemplos.append(ejemplo)
    with open(DB_FILE, 'w') as f:
        json.dump(ejemplos, f, indent=2)
    return True

# Funcionalidades avanzadas
def ejercicio_identificacion():
    ejemplos = ejemplos_base + cargar_ejemplos()
    ejemplo = random.choice(ejemplos)
    
    print(f"\n📝 Frase completa: {ejemplo['principal']}, {ejemplo['subordinada']}.")
    input("\nPresiona Enter para ver la versión sin la subordinada...")
    
    print(f"\n🚀 Versión reducida: {ejemplo['principal']}.")
    
    respuesta = input("\n¿La subordinada era explicativa? (s/n): ").lower()
    explicativa = ", " in ejemplo['subordinada']
    
    if (respuesta == 's' and explicativa) or (respuesta == 'n' and not explicativa):
        print("✅ Correcto!")
    else:
        print("❌ Incorrecto")
    
    print(f"\n🔍 Explicación: {'ES explicativa' if explicativa else 'NO es explicativa'} porque {'se puede eliminar sin cambiar el sentido esencial' if explicativa else 'es necesaria para entender el antecedente'}.")

def practica_reescritura():
    ejemplos = cargar_ejemplos()
    if not ejemplos:
        ejemplos = ejemplos_base
    
    ejemplo = random.choice(ejemplos)
    print(f"\n✍️ Reescribe esta frase cambiando la subordinada explicativa:")
    print(f"Original: {ejemplo['principal']}, {ejemplo['subordinada']}.")
    
    nueva_sub = input("\nTu versión (incluye comas): ")
    
    # Análisis automático
    errores = []
    if ejemplo['antecedente'] not in nueva_sub:
        errores.append(f"El antecedente '{ejemplo['antecedente']}' no está presente")
    if not nueva_sub.startswith(", "):
        errores.append("Falta coma inicial")
    if not any(palabra in nueva_sub.lower() for palabra in ["que", "quien", "cuyo"]):
        errores.append("No se usó un conector relativo adecuado")
    
    if errores:
        print("\n🚨 Errores encontrados:")
        for error in errores:
            print(f"- {error}")
    else:
        print("\n🎉 ¡Versión válida! Comparación:")
        print(f"- Original: {ejemplo['subordinada']}")
        print(f"- Tu versión: {nueva_sub}")

# Menú principal mejorado
def menu_principal():
    while True:
        print(f"""
        🧠 ENTRENADOR DE SUBORDINADAS EXPLICATIVAS
        -----------------------------------------
        1. 📚 Ver teoría
        2. ❓ Cuestionario interactivo
        3. ✍️ Crear nuevo ejemplo
        4. 📂 Ver ejemplos guardados
        5. 🎯 Ejercicio de identificación
        6. 🔄 Práctica de reescritura
        7. 🚪 Salir
        """)
        
        opcion = input("Selecciona una opción (1-7): ")
        
        if opcion == "1":
            print(TEORIA)
        elif opcion == "2":
            cuestionario_conceptual()  # Función del código anterior
        elif opcion == "3":
            principal = input("Frase principal: ")
            subordinada = input("Subordinada explicativa: ")
            antecedente = input("Antecedente (último sustantivo de la principal): ")
            if guardar_ejemplo({"principal": principal, "subordinada": subordinada, "antecedente": antecedente}):
                print("💾 Ejemplo guardado!")
        elif opcion == "4":
            ejemplos = cargar_ejemplos()
            print(f"\n📚 Tienes {len(ejemplos)} ejemplos guardados:")
            for i, ej in enumerate(ejemplos, 1):
                print(f"{i}. {ej['principal']}, {ej['subordinada']}.")
        elif opcion == "5":
            ejercicio_identificacion()
        elif opcion == "6":
            practica_reescritura()
        elif opcion == "7":
            print("👋 ¡Hasta la próxima!")
            break
        else:
            print("❌ Opción inválida")
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    menu_principal()
