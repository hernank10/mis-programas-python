import random

# Diccionario de ejemplos por nivel con análisis
ejemplos = {
    "Nivel semántico categorial": {
        "casa": "Sustantivo: nombra un objeto.",
        "grande": "Adjetivo calificativo: expresa una cualidad.",
        "correr": "Verbo: indica acción.",
        "rápidamente": "Adverbio: modifica el verbo.",
        "ella": "Pronombre: sustituye al sustantivo femenino."
    },
    "Nivel morfológico": {
        "florista": "Derivación: flor + ista.",
        "soleado": "Derivación: sol + eado.",
        "comíamos": "Flexión verbal: 1.ª persona plural, pretérito imperfecto.",
        "niños": "Flexión nominal: plural del sustantivo.",
        "infeliz": "Derivación con prefijo: in- + feliz."
    },
    "Nivel sintáctico": {
        "El gato duerme": "Oración simple. Sujeto: 'El gato'. Predicado: 'duerme'.",
        "Estudió mucho y aprobó el examen": "Coordinada copulativa.",
        "Me alegra que hayas venido": "Subordinada sustantiva.",
        "Juan comió manzanas": "Complemento directo: 'manzanas'.",
        "Pedro aunque estaba cansado siguió caminando": "Conector concesivo: 'aunque'."
    },
    "Nivel fonológico y ortográfico": {
        "zapato": "Fonema /s/ representado con 'z'.",
        "queso": "Fonema /k/ representado con 'qu'.",
        "gente": "Fonema /x/ representado con 'g' ante 'e'.",
        "lluvia": "Fonema palatal /ʝ/ representado con 'll'.",
        "niño": "Fonema nasal palatal /ɲ/ representado con 'ñ'."
    }
}

# Función principal del juego
def practicar_niveles():
    puntos = 0
    total = 0
    print("\n📚 Bienvenido al programa de práctica lingüística.\n")
    niveles = list(ejemplos.keys())
    random.shuffle(niveles)

    for nivel in niveles:
        print(f"\n🧠 Nivel: {nivel}\n")
        ejemplos_nivel = ejemplos[nivel]
        items = list(ejemplos_nivel.items())
        random.shuffle(items)

        for palabra, descripcion in items:
            print(f"👉 Escribe correctamente la siguiente palabra u oración: {descripcion}")
            respuesta = input("Tu respuesta: ").strip()
            total += 1
            if respuesta.lower() == palabra.lower():
                print("✅ ¡Correcto!\n")
                puntos += 1
            else:
                print(f"❌ Incorrecto. La respuesta correcta era: '{palabra}'\n")

    print(f"\n🎯 Has acertado {puntos} de {total} preguntas.")
    porcentaje = (puntos / total) * 100
    print(f"🏁 Puntuación final: {porcentaje:.2f}%\n")

# Ejecutar el programa
if __name__ == "__main__":
    practicar_niveles()
