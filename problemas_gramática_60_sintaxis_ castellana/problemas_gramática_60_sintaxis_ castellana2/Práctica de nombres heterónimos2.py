import random

heteronimos = [
    ("padre", "madre"), ("hombre", "mujer"), ("yerno", "nuera"), ("caballo", "yegua"),
    ("toro", "vaca"), ("carnero", "oveja"), ("conde", "condesa"), ("rey", "reina"),
    ("príncipe", "princesa"), ("monje", "monja"), ("poeta", "poetisa"), ("héroe", "heroína"),
    ("zar", "zarina"), ("duque", "duquesa"), ("marqués", "marquesa"), ("abad", "abadesa"),
    ("emperador", "emperatriz"), ("actor", "actriz"), ("sacerdote", "sacerdotisa"),
    ("dios", "diosa"), ("gobernador", "gobernadora"), ("presidente", "presidenta"),
    ("cónsul", "cónsul"), ("barón", "baronesa"), ("hechicero", "hechicera"),
    ("brujo", "bruja"), ("alcalde", "alcaldesa"), ("testigo", "testigo"),
    ("cliente", "clienta"), ("sirviente", "sirvienta"), ("asistente", "asistenta"),
    ("amo", "ama"), ("juez", "jueza"), ("infante", "infanta"), ("vidente", "vidente"),
    ("soldado", "soldado"), ("mártir", "mártir"), ("cantante", "cantante"),
    ("prófugo", "prófuga"), ("prisionero", "prisionera"), ("huérfano", "huérfana"),
    ("zorro", "zorra"), ("león", "leona"), ("tigre", "tigresa"), ("gallo", "gallina"),
    ("ratón", "rata"), ("ciervo", "cierva")
]

ejemplos_usuario = []

def mostrar_teoria():
    print("\n=== Teoría sobre nombres heterónimos ===")
    print("Los nombres heterónimos son aquellos que tienen formas completamente diferentes para el masculino y el femenino.")
    print("Ejemplo: 'padre' (masculino) y 'madre' (femenino). No se forma simplemente agregando una 'a' o 'o'.\n")

def practicar_completacion():
    palabra_masculina, palabra_femenina = random.choice(heteronimos)
    oracion = f"Mi {palabra_masculina} y mi ____ me enseñaron grandes valores."
    print("\nEjercicio de completación:")
    print(oracion)
    respuesta = input("Completa la oración: ").strip().lower()
    
    if respuesta == palabra_femenina:
        print("✔ Correcto! Has completado la oración correctamente.\n")
    else:
        print(f"✖ Incorrecto. La respuesta correcta era '{palabra_femenina}'.\n")

def practicar_redaccion():
    if len(ejemplos_usuario) >= 100:
        print("Has alcanzado el límite de 100 ejemplos guardados.\n")
        return
    
    palabra_masculina, palabra_femenina = random.choice(heteronimos)
    print(f"\nEscribe una oración usando la palabra: {palabra_masculina}")
    oracion1 = input("Tu oración: ")
    print(f"Ahora escribe una oración usando la palabra: {palabra_femenina}")
    oracion2 = input("Tu oración: ")
    
    ejemplos_usuario.append((oracion1, oracion2))
    print("✔ Tus ejemplos han sido guardados. Puedes seguir practicando.\n")

def mostrar_ejemplos_guardados():
    print("\n=== Ejemplos guardados ===")
    if not ejemplos_usuario:
        print("No hay ejemplos guardados aún.\n")
    else:
        for i, (o1, o2) in enumerate(ejemplos_usuario, 1):
            print(f"{i}. {o1}")
            print(f"   {o2}\n")

def menu():
    while True:
        print("\n=== Práctica de nombres heterónimos ===")
        print("1. Ver teoría")
        print("2. Ejercicios de completación de oraciones")
        print("3. Ejercicios de redacción (guardar hasta 100 ejemplos)")
        print("4. Ver ejemplos guardados")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            mostrar_teoria()
        elif opcion == "2":
            practicar_completacion()
        elif opcion == "3":
            practicar_redaccion()
        elif opcion == "4":
            mostrar_ejemplos_guardados()
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    menu()
