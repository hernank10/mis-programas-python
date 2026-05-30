import json
import os

# Archivo donde se guardarán los datos
ARCHIVO_DATOS = "palabras_prefijacion_composicion.json"

# Cargar datos si existe el archivo
def cargar_datos():
    if os.path.exists(ARCHIVO_DATOS):
        with open(ARCHIVO_DATOS, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

# Guardar datos
def guardar_datos(data):
    with open(ARCHIVO_DATOS, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# Inicializar la base de datos
tabla_clasificatoria = cargar_datos()

def mostrar_menu():
    print("\n=== GESTOR DE PALABRAS POR PREFIJACIÓN Y COMPOSICIÓN ===")
    print("1. Ver todas las categorías")
    print("2. Ver palabras por categoría")
    print("3. Buscar palabra")
    print("4. Agregar nueva palabra")
    print("5. Editar palabra")
    print("6. Guardar cambios")
    print("7. Crear nueva lista desde cero")
    print("8. Ver todas las palabras (100+)")
    print("9. Salir")

def ver_categorias():
    print("\nCategorías disponibles:")
    for categoria in tabla_clasificatoria:
        print(f"- {categoria}")

def ver_palabras_por_categoria():
    ver_categorias()
    categoria = input("Escribe una categoría exacta: ")
    if categoria in tabla_clasificatoria:
        print(f"\nPalabras en {categoria}:")
        for i, (palabra, formacion, significado) in enumerate(tabla_clasificatoria[categoria]):
            print(f"{i+1}. {palabra} ({formacion}) → {significado}")
    else:
        print("Categoría no encontrada.")

def buscar_palabra():
    palabra_buscada = input("Escribe la palabra a buscar: ").lower()
    for categoria, palabras in tabla_clasificatoria.items():
        for palabra, formacion, significado in palabras:
            if palabra == palabra_buscada:
                print(f"\nResultado:")
                print(f"• Palabra: {palabra}")
                print(f"• Formación: {formacion}")
                print(f"• Significado: {significado}")
                print(f"• Categoría: {categoria}")
                return
    print("Palabra no encontrada.")

def agregar_palabra():
    categoria = input("Categoría (nueva o existente): ")
    palabra = input("Nueva palabra: ").lower()
    formacion = input("Tipo de formación (ej: prefijo + base): ")
    significado = input("Significado: ")
    if categoria not in tabla_clasificatoria:
        tabla_clasificatoria[categoria] = []
    tabla_clasificatoria[categoria].append((palabra, formacion, significado))
    print(f"✅ Palabra '{palabra}' agregada a la categoría '{categoria}'.")

def editar_palabra():
    ver_categorias()
    categoria = input("Selecciona la categoría de la palabra a editar: ")
    if categoria not in tabla_clasificatoria:
        print("Categoría no encontrada.")
        return
    palabras = tabla_clasificatoria[categoria]
    for i, (palabra, formacion, significado) in enumerate(palabras):
        print(f"{i+1}. {palabra} ({formacion}) → {significado}")
    try:
        idx = int(input("Número de la palabra a editar: ")) - 1
        if 0 <= idx < len(palabras):
            nueva_palabra = input("Nueva palabra: ").lower()
            nueva_formacion = input("Nueva formación: ")
            nuevo_significado = input("Nuevo significado: ")
            tabla_clasificatoria[categoria][idx] = (nueva_palabra, nueva_formacion, nuevo_significado)
            print("✅ Palabra actualizada.")
        else:
            print("Índice fuera de rango.")
    except ValueError:
        print("Entrada inválida.")

def crear_lista_nueva():
    global tabla_clasificatoria
    confirm = input("⚠️ ¿Seguro que deseas eliminar todos los datos actuales y comenzar desde cero? (sí/no): ")
    if confirm.lower() == "sí":
        tabla_clasificatoria = {}
        guardar_datos(tabla_clasificatoria)
        print("🔄 Lista reiniciada.")
    else:
        print("❌ Operación cancelada.")

def ver_todas_las_palabras():
    print("\n=== TODAS LAS PALABRAS REGISTRADAS ===")
    total = 0
    for categoria, palabras in tabla_clasificatoria.items():
        for palabra, formacion, significado in palabras:
            total += 1
            print(f"{total}. {palabra} ({formacion}) → {significado} [{categoria}]")
    print(f"\n✅ Total: {total} palabras registradas.")

# Bucle principal
while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")
    if opcion == "1":
        ver_categorias()
    elif opcion == "2":
        ver_palabras_por_categoria()
    elif opcion == "3":
        buscar_palabra()
    elif opcion == "4":
        agregar_palabra()
    elif opcion == "5":
        editar_palabra()
    elif opcion == "6":
        guardar_datos(tabla_clasificatoria)
        print("💾 Cambios guardados correctamente.")
    elif opcion == "7":
        crear_lista_nueva()
    elif opcion == "8":
        ver_todas_las_palabras()
    elif opcion == "9":
        print("👋 ¡Hasta luego!")
        break
    else:
        print("❌ Opción no válida. Intenta de nuevo.")
