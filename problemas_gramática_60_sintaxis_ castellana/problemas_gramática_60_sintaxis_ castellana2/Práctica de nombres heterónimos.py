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

def practicar_oraciones():
    palabra_masculina, palabra_femenina = random.choice(heteronimos)
    print(f"Crea una oración usando la palabra: {palabra_masculina}")
    oracion1 = input("Escribe tu oración: ")
    print(f"Ahora crea una oración usando la palabra: {palabra_femenina}")
    oracion2 = input("Escribe tu oración: ")
    
    print("\nEvaluación de tus oraciones:")
    if palabra_masculina in oracion1:
        print(f"✔ Buen uso de '{palabra_masculina}' en tu oración.")
    else:
        print(f"✖ No se detectó '{palabra_masculina}' en tu oración. Intenta incluirla correctamente.")
    
    if palabra_femenina in oracion2:
        print(f"✔ Buen uso de '{palabra_femenina}' en tu oración.")
    else:
        print(f"✖ No se detectó '{palabra_femenina}' en tu oración. Intenta incluirla correctamente.")
    
    print("¡Bien hecho! Puedes seguir practicando con más palabras.\n")

def clasificar_formalidad():
    palabra_masculina, palabra_femenina = random.choice(heteronimos)
    print(f"Clasifica esta palabra en formal o informal: {palabra_masculina}")
    clasificacion1 = input("(Formal/Informal): ").strip().lower()
    print(f"Clasifica esta palabra en formal o informal: {palabra_femenina}")
    clasificacion2 = input("(Formal/Informal): ").strip().lower()
    
    formales = ["gobernador", "presidente", "juez", "rey", "emperador", "cónsul", "duque"]
    
    print("\nEvaluación de tu clasificación:")
    if (palabra_masculina in formales and clasificacion1 == "formal") or (palabra_masculina not in formales and clasificacion1 == "informal"):
        print(f"✔ Correcto: '{palabra_masculina}' está bien clasificado.")
    else:
        print(f"✖ Incorrecto: '{palabra_masculina}' debería clasificarse como {'formal' if palabra_masculina in formales else 'informal'}.")
    
    if (palabra_femenina in formales and clasificacion2 == "formal") or (palabra_femenina not in formales and clasificacion2 == "informal"):
        print(f"✔ Correcto: '{palabra_femenina}' está bien clasificado.")
    else:
        print(f"✖ Incorrecto: '{palabra_femenina}' debería clasificarse como {'formal' if palabra_femenina in formales else 'informal'}.")
    
    print("¡Gracias por clasificar! Puedes intentarlo de nuevo con otras palabras.\n")

def menu():
    while True:
        print("\n=== Práctica de nombres heterónimos ===")
        print("1. Practicar escribiendo oraciones")
        print("2. Clasificar palabras según su formalidad")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            practicar_oraciones()
        elif opcion == "2":
            clasificar_formalidad()
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    menu()
