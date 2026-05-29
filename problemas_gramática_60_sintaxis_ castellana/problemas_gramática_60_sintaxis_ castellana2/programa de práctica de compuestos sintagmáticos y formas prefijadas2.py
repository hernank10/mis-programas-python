import json

# Archivo donde se guardarán los ejemplos del usuario
FILE_NAME = "ejemplos_usuario.json"

# Teoría sobre los compuestos sintagmáticos y formas prefijadas
TEORIA = """
Los compuestos sintagmáticos y algunas formas prefijadas pueden escribirse de distintas maneras. 
Algunos se escriben en una sola palabra (ej. "mediodía"), mientras que otros deben mantenerse en dos palabras (ej. "medio ambiente").

Ejemplos:
- "Medio día" (incorrecto) → "Mediodía" (correcto)
- "Centro derecha" (incorrecto) → "Centroderecha" (correcto)
- "Sin techo" (correcto) → "Sintecho" (correcto en algunos casos, dependiendo del uso)

Practiquemos con ejercicios.
"""

# Lista de ejercicios de completación
EJERCICIOS_COMPLETACION = [
    {"oracion": "Cuidamos el ____ ambiente.", "respuesta": "medioambiente"},
    {"oracion": "Se reunieron los líderes de ____ derecha.", "respuesta": "centroderecha"},
    {"oracion": "Salimos a caminar al ____ día.", "respuesta": "mediodía"},
    {"oracion": "Vive en la calle, es un ____ techo.", "respuesta": "sintecho"},
    {"oracion": "El futbolista juega en el ____ campo.", "respuesta": "mediocampo"}
]

# Lista de palabras para los ejercicios de redacción
PALABRAS_REDACCION = [
    "medioambiente", "centroderecha", "mediodía", "sintecho", "mediocampo", "gran hombre", "gran amigo", 
    "gran dependiente", "en medio", "en torno", "centro izquierda", "medio tiempo", "media luna", 
    "media punta", "ocho mil", "cincuenta y seis", "cuatrocientos", "diecisiete", "trigesimosegundo", 
    "segundamano", "tercermundista", "primeramente", "sinvergüenza", "sinsabor", "sinfín", "sinduda", 
    "sinrazón", "sinvivir", "sinusoide", "sinretorno", "sindiós", "sinecura", "siniestro", "sinfónico", 
    "sinopsis", "sincrónico", "sinergia", "sinónimo", "sintaxis", "sintonía", "sinusoidal", "sinfónico", 
    "sinvergonzonería", "sinóptico", "sinuoso", "sincrética", "sinfonía", "sinfín", "sinapismo"
]

# Cargar ejemplos del usuario si existen
def cargar_ejemplos():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Guardar ejemplos del usuario
def guardar_ejemplos(ejemplo):
    ejemplos = cargar_ejemplos()
    if len(ejemplos) < 100:
        ejemplos.append(ejemplo)
        with open(FILE_NAME, "w") as file:
            json.dump(ejemplos, file, indent=4)
    else:
        print("\n⚠️ Has alcanzado el límite de 100 ejemplos guardados. ⚠️")

# Función para los ejercicios de completación
def ejercicios_completacion():
    print("\n✍️ Ejercicios de completación:")
    for ejercicio in EJERCICIOS_COMPLETACION:
        respuesta = input(f"{ejercicio['oracion']} → ").strip()
        if respuesta.lower() == ejercicio["respuesta"]:
            print("✅ Correcto!")
        else:
            print(f"❌ Incorrecto. La respuesta correcta es: {ejercicio['respuesta']}\n")

# Función para los ejercicios de redacción
def ejercicios_redaccion():
    print("\n📝 Escribe una oración con una de las siguientes palabras:")
    print(", ".join(PALABRAS_REDACCION))
    oracion = input("Tu oración: ")
    guardar_ejemplos(oracion)
    print("\n✅ Tu oración ha sido guardada.")

# Función principal
def main():
    print("📘 Bienvenido al programa de práctica de compuestos sintagmáticos y formas prefijadas.")
    print(TEORIA)
    while True:
        print("\nMenú:")
        print("1️⃣ - Ejercicios de completación")
        print("2️⃣ - Ejercicios de redacción")
        print("3️⃣ - Ver mis ejemplos guardados")
        print("4️⃣ - Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            ejercicios_completacion()
        elif opcion == "2":
            ejercicios_redaccion()
        elif opcion == "3":
            ejemplos = cargar_ejemplos()
            print("\n📂 Ejemplos guardados:")
            for idx, ej in enumerate(ejemplos, 1):
                print(f"{idx}. {ej}")
        elif opcion == "4":
            print("👋 ¡Hasta la próxima!")
            break
        else:
            print("⚠️ Opción no válida. Inténtalo de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
