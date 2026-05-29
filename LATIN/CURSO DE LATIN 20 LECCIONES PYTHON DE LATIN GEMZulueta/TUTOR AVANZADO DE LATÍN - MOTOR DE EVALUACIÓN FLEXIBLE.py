import os
import sys
import unicodedata

def normalizar_cadena(texto):
    """
    Limpia el texto eliminando espacios extras, mayúsculas y tildes
    para permitir una validación pedagógica flexible y justa.
    """
    if not texto:
        return ""
    # Pasar a minúsculas y quitar espacios en los extremos
    texto = texto.strip().lower()
    # Eliminar acentos/tildes usando descomposición Unicode
    texto = "".join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )
    # Reemplazar múltiples espacios internos por uno solo
    return " ".join(texto.split())

# BANCO DE DATOS (Se pueden añadir los 100 ejercicios con esta misma estructura)
EJERCICIOS_LATIN = [
    {
        "id": 1,
        "tema": "Sintaxis: Primera Declinación",
        "oracion": "Poetae puellam laudant.",
        "pregunta": "Identifica el Sujeto (Nominativo) y el Objeto Directo (Acusativo).",
        "respuestas_validas": [
            "sujeto poetae objeto directo puellam",
            "sujeto poetae cd puellam",
            "sujeto poetae complemento directo puellam"
        ],
        "ayuda": "Poetae es nominativo plural (Sujeto). Puellam termina en -am, acusativo singular (Objeto Directo).",
        "retroalimentacion": "¡Excelente análisis! El verbo laudant (3ª plural) concuerda con Poetae."
    },
    {
        "id": 2,
        "tema": "Figuras Retóricas / Sintaxis",
        "oracion": "Magnam in silvam puella ambulat.",
        "pregunta": "¿Qué nombre recibe la alteración del orden lógico/sintáctico habitual de las palabras?",
        "respuestas_validas": [
            "hiperbaton",
            "el hiperbaton",
            "hiperbato"
        ],
        "ayuda": "Es una figura muy común en la poesía latina debido a la flexibilidad que otorgan los casos.",
        "retroalimentacion": "¡Correcto! El hipérbaton separa el adjetivo 'magnam' de su sustantivo 'silvam'."
    },
    {
        "id": 3,
        "tema": "Ablativo de Modo (Primera Declinación)",
        "oracion": "Traduce al latín: 'Con gran cuidado' (Cura, -ae / Magnus, -a, -um)",
        "pregunta": "Escribe la estructura en caso ablativo (puedes usar o no la preposición 'cum').",
        "respuestas_validas": [
            "magna cura",
            "magna cum cura"
        ],
        "ayuda": "El ablativo de modo con adjetivo puede omitir el 'cum' o intercalarlo en el medio.",
        "retroalimentacion": "¡Perfecto! Ambas variantes (magna cura o magna cum cura) son académicamente impecables."
    }
]

class TutorLatinPro:
    def __init__(self, banco_ejercicios):
        self.ejercicios = banco_ejercicios
        self.puntuacion = 0

    def limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def mostrar_banner(self):
        print("═" * 65)
        print("   🏛️  TUTOR AVANZADO DE LATÍN - MOTOR DE EVALUACIÓN FLEXIBLE 🏛️")
        print("═" * 65)

    def ejecutar_taller(self):
        self.limpiar_pantalla()
        self.mostrar_banner()
        print(f"Se han cargado {len(self.ejercicios)} ejercicios interactivos.")
        input("Presiona ENTER para comenzar el taller...")

        for ej in self.ejercicios:
            while True:
                self.limpiar_pantalla()
                self.mostrar_banner()
                print(f"\n▶️  Ejercicio {ej['id']} / {len(self.ejercicios)}")
                print(f"📌 Tema: {ej['tema']}")
                if "oracion" in ej and ej["oracion"]:
                    print(f"📖 Oración: '{ej['oracion']}'")
                print(f"❓ Pregunta: {ej['pregunta']}")
                print("-" * 65)
                
                respuesta_usuario = input("✍️  Tu respuesta: ")
                
                # Proceso crucial de normalización
                usuario_limpio = normalizar_cadena(respuesta_usuario)
                
                # Verificar si coincide con alguna de las respuestas aceptadas
                acierto = False
                for r_valida in ej["respuestas_validas"]:
                    if normalizar_cadena(r_valida) in usuario_limpio or usuario_limpio == normalizar_cadena(r_valida):
                        acierto = True
                        break
                
                if acierto:
                    print("\n✅ ¡CORRECTO!")
                    print(f"💡 {ej['retroalimentacion']}")
                    self.puntuacion += 1
                    input("\nPresiona ENTER para avanzar al siguiente ejercicio...")
                    break
                else:
                    print("\n❌ Respuesta no reconocida o incompleta.")
                    print(f"ℹ️  Ayuda: {ej['ayuda']}")
                    print(f"📝 Una respuesta esperada podría ser: '{ej['respuestas_validas'][0]}'")
                    
                    opcion = input("\n¿Quieres reintentar este ejercicio? (s/n): ").strip().lower()
                    if opcion != 's':
                        print("\nAvanzando de lección...")
                        input("Presiona ENTER para continuar...")
                        break

        # Cierre del programa
        self.limpiar_pantalla()
        self.mostrar_banner()
        print("\n🏁 ¡Taller completado con éxito!")
        print(f"📊 Puntuación final: {self.puntuacion} / {len(self.ejercicios)}")
        print("¡Sigue estudiando las estructuras de la lengua castellana y latina!")
        print("═" * 65)

if __name__ == "__main__":
    # Instanciar y lanzar el programa sin peligro de congelamiento por nombres largos
    tutor = TutorLatinPro(EJERCICIOS_LATIN)
    tutor.ejecutar_taller()