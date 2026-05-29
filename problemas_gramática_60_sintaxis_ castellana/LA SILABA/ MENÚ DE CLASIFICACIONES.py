import csv
import random

# Cargar datos desde archivo CSV
def cargar_ejemplos(ruta_archivo):
    ejemplos = []
    with open(ruta_archivo, newline='', encoding='utf-8') as csvfile:
        lector = csv.DictReader(csvfile)
        for fila in lector:
            ejemplos.append({
                "ejemplo": fila["Ejemplo"],
                "afi": fila["AFI"],
                "interpretaciones": fila["Interpretaciones"],
                "clasificacion": fila["Clasificación"]
            })
    return ejemplos

# Mostrar menú por clasificación
def menu_por_clasificacion(ejemplos):
    clasificaciones = sorted(set(e["clasificacion"] for e in ejemplos))
    print("\n--- MENÚ DE CLASIFICACIONES ---")
    for idx, clasif in enumerate(clasificaciones, 1):
        print(f"{idx}. {clasif}")
    print("0. Salir")
    return clasificaciones

# Práctica del usuario
def practicar_categoria(ejemplos, clasificacion):
    seleccionados = [e for e in ejemplos if e["clasificacion"] == clasificacion]
    random.shuffle(seleccionados)
    print(f"\nPracticando: {clasificacion} ({len(seleccionados)} ejemplos)\n")

    correctos = 0
    for i, ejemplo in enumerate(seleccionados, 1):
        print(f"{i}. Ejemplo: {ejemplo['ejemplo']}")
        respuesta = input("Escribe la transcripción AFI: ").strip()
        if respuesta == ejemplo["afi"]:
            print("✅ ¡Correcto!\n")
            correctos += 1
        else:
            print(f"❌ Incorrecto. La respuesta correcta es: {ejemplo['afi']}\n")
    print(f"Has respondido correctamente {correctos} de {len(seleccionados)} ejemplos.")

# Programa principal
def main():
    ruta_csv = "ejemplos_afi_ambiguedad.csv"
    ejemplos = cargar_ejemplos(ruta_csv)

    while True:
        clasificaciones = menu_por_clasificacion(ejemplos)
        try:
            opcion = int(input("\nSelecciona una categoría (número): "))
            if opcion == 0:
                print("Gracias por practicar. ¡Hasta luego!")
                break
            elif 1 <= opcion <= len(clasificaciones):
                practicar_categoria(ejemplos, clasificaciones[opcion - 1])
            else:
                print("Opción inválida.")
        except ValueError:
            print("Por favor, introduce un número.")

if __name__ == "__main__":
    main()
