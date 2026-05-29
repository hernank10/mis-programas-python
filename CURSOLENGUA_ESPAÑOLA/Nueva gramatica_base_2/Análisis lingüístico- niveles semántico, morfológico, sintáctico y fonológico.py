# -*- coding: utf-8 -*-
import json

# Estructura de datos principal
niveles = {
    "semántico": {
        "conceptos": {
            "es": "📚 Nivel Semántico-Categorial\nEstudia el significado de palabras y categorías gramaticales.\nEj: Sustantivos (seres), verbos (acciones), adjetivos (cualidades).",
            "en": "📚 Categorial-Semantic Level\nStudies word meanings and grammatical categories.\nE.g.: Nouns (beings), verbs (actions), adjectives (qualities)."
        },
        "ejemplos": [],
        "max_ejemplos": 100
    },
    "morfológico": {
        "conceptos": {
            "es": "🔍 Nivel Morfológico\nAnaliza estructura interna de palabras (morfemas y lexemas).\nEj: Flexiones (género/número) y derivaciones (amor → amoroso).",
            "en": "🔍 Morphological Level\nAnalyzes internal word structure (morphemes and lexemes).\nE.g.: Inflections (gender/number) and derivations (love → loving)."
        },
        "ejemplos": [],
        "max_ejemplos": 100
    },
    "sintáctico": {
        "conceptos": {
            "es": "📐 Nivel Sintáctico\nEstudia combinación de palabras en oraciones.\nFunciones: Sujeto, predicado, complementos.",
            "en": "📐 Syntactic Level\nStudies word combination in sentences.\nFunctions: Subject, predicate, complements."
        },
        "ejemplos": [],
        "max_ejemplos": 100
    },
    "fonológico": {
        "conceptos": {
            "es": "🎵 Nivel Fonológico\nAnaliza sonidos del lenguaje y su organización.\nEj: Fonemas /b/ vs /p/, sílabas, acentuación.",
            "en": "🎵 Phonological Level\nAnalyzes speech sounds and their organization.\nE.g.: Phonemes /b/ vs /p/, syllables, stress."
        },
        "ejemplos": [],
        "max_ejemplos": 100
    }
}

def mostrar_diapositiva(nivel):
    print("\n" + "="*50)
    print(f"CONCEPTOS - {nivel.upper()} (ES):")
    print(niveles[nivel]["conceptos"]["es"])
    print("\n" + "-"*50)
    print(f"CONCEPTS - {nivel.upper()} (EN):")
    print(niveles[nivel]["conceptos"]["en"])
    print("="*50 + "\n")

def crear_ejemplo(nivel):
    if len(niveles[nivel]["ejemplos"]) >= niveles[nivel]["max_ejemplos"]:
        print(f"❌ Límite alcanzado (Máx: {niveles[nivel]['max_ejemplos']} ejemplos)")
        return
    
    print(f"\nCreando ejemplo para nivel {nivel}:")
    ejemplo_es = input("Ejemplo en español: ").strip()
    ejemplo_en = input("Traducción al inglés: ").strip()
    respuesta = input("Respuesta correcta: ").strip()
    analisis = input("Análisis/explicación: ").strip()
    
    nuevos_datos = {
        "ejemplo_es": ejemplo_es,
        "ejemplo_en": ejemplo_en,
        "respuesta": respuesta,
        "analisis": analisis
    }
    
    niveles[nivel]["ejemplos"].append(nuevos_datos)
    print("✅ Ejemplo guardado exitosamente!")

def ver_ejemplos(nivel):
    if not niveles[nivel]["ejemplos"]:
        print(f"\nNo hay ejemplos guardados en {nivel}.")
        return
    
    print(f"\n📂 Ejemplos guardados en {nivel} ({len(niveles[nivel]['ejemplos']}/100):")
    for idx, ejemplo in enumerate(niveles[nivel]["ejemplos"], 1):
        print(f"\nEjemplo {idx}:")
        print(f"ES: {ejemplo['ejemplo_es']}")
        print(f"EN: {ejemplo['ejemplo_en']}")
        print(f"Respuesta: {ejemplo['respuesta']}")
        print(f"Análisis: {ejemplo['analisis']}")

def guardar_cargar_datos(accion):
    filename = "datos_linguisticos.json"
    try:
        if accion == "guardar":
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(niveles, f, ensure_ascii=False)
            print("✅ Datos guardados en archivo!")
        elif accion == "cargar":
            with open(filename, "r", encoding="utf-8") as f:
                datos = json.load(f)
                niveles.update(datos)
            print("✅ Datos cargados desde archivo!")
    except Exception as e:
        print(f"❌ Error: {str(e)}")

def menu_principal():
    print("""
    ░▒▓═══════ LINGUISTIC PRACTICE SYSTEM ═══════▓▒░
    1. Seleccionar nivel lingüístico
    2. Ver diapositivas conceptuales
    3. Crear nuevo ejemplo
    4. Ver ejemplos guardados
    5. Guardar/Cargar datos
    6. Salir
    """)

def main():
    while True:
        menu_principal()
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            nivel = input("Niveles disponibles: semántico, morfológico, sintáctico, fonológico\n> ").lower()
            if nivel in niveles:
                print(f"\nNivel {nivel} seleccionado.")
            else:
                print("❌ Nivel no válido")
        
        elif opcion == "2":
            nivel = input("Ingrese nivel para ver diapositivas: ").lower()
            if nivel in niveles:
                mostrar_diapositiva(nivel)
            else:
                print("❌ Nivel no válido")
        
        elif opcion == "3":
            nivel = input("Ingrese nivel para crear ejemplo: ").lower()
            if nivel in niveles:
                crear_ejemplo(nivel)
            else:
                print("❌ Nivel no válido")
        
        elif opcion == "4":
            nivel = input("Ingrese nivel para ver ejemplos: ").lower()
            if nivel in niveles:
                ver_ejemplos(nivel)
            else:
                print("❌ Nivel no válido")
        
        elif opcion == "5":
            accion = input("¿Guardar o cargar datos? (guardar/cargar): ").lower()
            if accion in ["guardar", "cargar"]:
                guardar_cargar_datos(accion)
            else:
                print("❌ Opción no válida")
        
        elif opcion == "6":
            print("¡Hasta luego! 👋")
            break
        
        else:
            print("❌ Opción no válida")

if __name__ == "__main__":
    main()
