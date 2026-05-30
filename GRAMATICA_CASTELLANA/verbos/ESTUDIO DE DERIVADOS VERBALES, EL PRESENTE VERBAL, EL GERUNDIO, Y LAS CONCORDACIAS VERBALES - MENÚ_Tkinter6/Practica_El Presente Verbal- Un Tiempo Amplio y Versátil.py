import random
import json

# Base de datos de ejemplos
ejemplos = [
    {"oracion": "Desayuno cereal todas las mañanas.", "categoria": "Presente habitual"},
    {"oracion": "Estoy leyendo un libro interesante.", "categoria": "Presente actual"},
    {"oracion": "Mañana compro los boletos del concierto.", "categoria": "Presente por futuro"},
    {"oracion": "El agua hierve a 100 grados Celsius.", "categoria": "Presente nómino"},
    # Puedes agregar más ejemplos aquí...
]

# Cargar frases personalizadas
def cargar_personales():
    try:
        with open("frases_personales.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Guardar frases personalizadas
def guardar_personales(frases):
    with open("frases_personales.json", "w", encoding="utf-8") as file:
        json.dump(frases, file, indent=2, ensure_ascii=False)

# Mostrar un ejemplo y pedir categoría
def identificar_categoria():
    ejemplo = random.choice(ejemplos)
    print(f"\nOración: {ejemplo['oracion']}")
    respuesta = input("¿A qué categoría pertenece? (Presente habitual / actual / por futuro / nómino): ").strip().lower()
    if respuesta in ejemplo['categoria'].lower():
        print("✅ ¡Correcto!")
    else:
        print(f"❌ Incorrecto. La respuesta correcta era: {ejemplo['categoria']}.")

# Reescribir en otro tiempo verbal (simulado)
def reescribir_oracion():
    ejemplo = random.choice(ejemplos)
    print(f"\nOración original: {ejemplo['oracion']}")
    nuevo_tiempo = input("Cambia la oración a otro tiempo verbal (escribe tú la nueva versión): ")
    print(f"Tu nueva oración: {nuevo_tiempo}")

# Crear una nueva frase
def crear_frase(frases_personales):
    if len(frases_personales) >= 100:
        print("⚠️ Ya alcanzaste el límite de 100 frases.")
        return
    oracion = input("Escribe tu nueva oración: ").strip()
    categoria = input("¿Qué categoría tiene? (Presente habitual / actual / por futuro / nómino): ").strip()
    frases_personales.append({"oracion": oracion, "categoria": categoria})
    guardar_personales(frases_personales)
    print("✅ Frase guardada correctamente.")

# Ver tus frases guardadas
def ver_frases(frases_personales):
    if not frases_personales:
        print("No tienes frases guardadas aún.")
    else:
        for idx, frase in enumerate(frases_personales, 1):
            print(f"{idx}. {frase['oracion']} ({frase['categoria']})")

# Menú principal
def menu():
    frases_personales = cargar_personales()
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Identificar categoría de una oración")
        print("2. Reescribir una oración en otro tiempo verbal")
        print("3. Crear una nueva frase")
        print("4. Ver frases guardadas")
        print("5. Salir")
        opcion = input("Selecciona una opción (1-5): ")
        
        if opcion == "1":
            identificar_categoria()
        elif opcion == "2":
            reescribir_oracion()
        elif opcion == "3":
            crear_frase(frases_personales)
        elif opcion == "4":
            ver_frases(frases_personales)
        elif opcion == "5":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutar programa
if __name__ == "__main__":
    menu()
