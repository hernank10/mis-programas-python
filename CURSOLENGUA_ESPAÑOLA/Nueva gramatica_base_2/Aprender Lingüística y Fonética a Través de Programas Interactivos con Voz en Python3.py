import random

# Diccionario de ejemplos fijos con traducciones
ejemplos_fijos = {
    "Nivel semántico categorial": {
        "casa": ("Sustantivo: nombra un objeto.", "house"),
        "grande": ("Adjetivo calificativo: expresa una cualidad.", "big"),
        "correr": ("Verbo: indica acción.", "run"),
        "rápidamente": ("Adverbio: modifica el verbo.", "quickly"),
        "ella": ("Pronombre: sustituye al sustantivo femenino.", "she")
    },
    "Nivel morfológico": {
        "florista": ("Derivación: flor + ista.", "florist"),
        "soleado": ("Derivación: sol + eado.", "sunny"),
        "comíamos": ("Flexión verbal: 1.ª persona plural, pretérito imperfecto.", "we used to eat"),
        "niños": ("Flexión nominal: plural del sustantivo.", "children"),
        "infeliz": ("Derivación con prefijo: in- + feliz.", "unhappy")
    },
    "Nivel sintáctico": {
        "El gato duerme": ("Oración simple. Sujeto: 'El gato'. Predicado: 'duerme'.", "The cat sleeps"),
        "Estudió mucho y aprobó el examen": ("Coordinada copulativa.", "He studied a lot and passed the exam"),
        "Me alegra que hayas venido": ("Subordinada sustantiva.", "I’m glad you came"),
        "Juan comió manzanas": ("Complemento directo: 'manzanas'.", "Juan ate apples"),
        "Pedro aunque estaba cansado siguió caminando": ("Conector concesivo: 'aunque'.", "Pedro, although tired, kept walking")
    },
    "Nivel fonológico y ortográfico": {
        "zapato": ("Fonema /s/ representado con 'z'.", "shoe"),
        "queso": ("Fonema /k/ representado con 'qu'.", "cheese"),
        "gente": ("Fonema /x/ representado con 'g' ante 'e'.", "people"),
        "lluvia": ("Fonema palatal /ʝ/ representado con 'll'.", "rain"),
        "niño": ("Fonema nasal palatal /ɲ/ representado con 'ñ'.", "boy")
    }
}

# Diccionario para ejemplos creados por el usuario
ejemplos_usuario = {
    "Nivel semántico categorial": [],
    "Nivel morfológico": [],
    "Nivel sintáctico": [],
    "Nivel fonológico y ortográfico": []
}

# Función para mostrar diapositiva con conceptos teóricos
def mostrar_diapositiva():
    print("\n📖 DIAPOSITIVA TEÓRICA\n")
    print("a. Nivel semántico categorial:\n   - Estudia los significados y funciones de cada clase de palabra.\n   - Ej: el sustantivo nombra, el adjetivo califica.\n")
    print("b. Nivel morfológico:\n   - Analiza la estructura de las palabras: raíces y morfemas.\n   - Considera accidentes gramaticales (género, número, etc.).\n")
    print("c. Nivel sintáctico:\n   - Estudia cómo se combinan las palabras para formar oraciones.\n   - Identifica funciones como sujeto, predicado, modificadores.\n")
    print("d. Nivel fonológico y ortográfico:\n   - Estudia los sonidos (fonemas) y su representación escrita (grafemas).\n   - Incluye reglas de pronunciación y ortografía.\n")

# Función para crear ejemplos
def crear_ejemplo():
    print("\n📝 Crear nuevo ejemplo")
    nivel = input("Escribe el nivel (semántico, morfológico, sintáctico, fonológico): ").strip().lower()
    clave = f"Nivel {nivel} categorial" if nivel == "semántico" else f"Nivel {nivel}" if nivel in ["morfológico", "sintáctico"] else "Nivel fonológico y ortográfico"
    
    if clave not in ejemplos_usuario:
        print("❌ Nivel no válido.")
        return

    if len(ejemplos_usuario[clave]) >= 10:
        print("⚠️ Ya tienes 10 ejemplos guardados en esta categoría.")
        return

    palabra = input("Palabra u oración: ")
    descripcion = input("Explicación o análisis: ")
    traduccion = input("Traducción al inglés: ")

    ejemplos_usuario[clave].append((palabra, descripcion, traduccion))
    print("✅ Ejemplo guardado.")

# Función para ver ejemplos creados por el usuario
def ver_ejemplos():
    print("\n📂 Ejemplos guardados por el usuario:")
    for nivel, lista in ejemplos_usuario.items():
        print(f"\n🔹 {nivel}:")
        if lista:
            for palabra, desc, trad in lista:
                print(f"  - {palabra} | {desc} | EN: {trad}")
        else:
            print("  (sin ejemplos aún)")

# Función para guardar ejemplos en archivo
def guardar_ejemplos():
    with open("ejemplos_usuario.txt", "w", encoding="utf-8") as f:
        for nivel, lista in ejemplos_usuario.items():
            f.write(f"== {nivel} ==\n")
            for palabra, desc, trad in lista:
                f.write(f"{palabra} - {desc} - {trad}\n")
            f.write("\n")
    print("💾 Ejemplos guardados en 'ejemplos_usuario.txt'")

# Función para practicar traducción al inglés
def practicar_traduccion():
    total = 0
    aciertos = 0
    for nivel, ejemplos in ejemplos_fijos.items():
        print(f"\n📘 Nivel: {nivel}")
        items = list(ejemplos.items())
        random.shuffle(items)
        for palabra, (_, traduccion) in items:
            print(f"Traduce: {palabra}")
            respuesta = input("Tu traducción: ").strip().lower()
            total += 1
            if respuesta == traduccion.lower():
                print("✅ Correcto!\n")
                aciertos += 1
            else:
                print(f"❌ Incorrecto. Respuesta correcta: {traduccion}\n")
    mostrar_resultado(aciertos, total)

# Función para practicar escritura en español
def practicar_escritura():
    total = 0
    aciertos = 0
    for nivel, ejemplos in ejemplos_fijos.items():
        print(f"\n🧠 Nivel: {nivel}")
        items = list(ejemplos.items())
        random.shuffle(items)
        for palabra, (descripcion, _) in items:
            print(f"Escribe: {descripcion}")
            respuesta = input("Tu respuesta: ").strip()
            total += 1
            if respuesta.lower() == palabra.lower():
                print("✅ Correcto!\n")
                aciertos += 1
            else:
                print(f"❌ Incorrecto. Era: {palabra}\n")
    mostrar_resultado(aciertos, total)

def mostrar_resultado(aciertos, total):
    print(f"\n🎯 Aciertos: {aciertos}/{total}")
    print(f"📊 Porcentaje: {aciertos/total*100:.2f}%\n")

# Menú principal
def menu():
    while True:
        print("\n📚 MENÚ PRINCIPAL")
        print("1. Ver diapositiva teórica")
        print("2. Practicar escritura en español")
        print("3. Practicar traducción al inglés")
        print("4. Crear nuevo ejemplo")
        print("5. Ver ejemplos guardados")
        print("6. Guardar ejemplos en archivo")
        print("7. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            mostrar_diapositiva()
        elif opcion == "2":
            practicar_escritura()
        elif opcion == "3":
            practicar_traduccion()
        elif opcion == "4":
            crear_ejemplo()
        elif opcion == "5":
            ver_ejemplos()
        elif opcion == "6":
            guardar_ejemplos()
        elif opcion == "7":
            print("👋 ¡Hasta pronto!")
            break
        else:
            print("❗ Opción inválida.")

# Ejecutar
if __name__ == "__main__":
    menu()
