# -*- coding: utf-8 -*-
"""
Tutor interactivo de latín en la consola.
Este programa se enfoca en:
1. Infinitivo (presente, perfecto, futuro - activo y pasivo).
2. Gerundio.
3. Gerundivo.
4. Supino.
"""
import random

# --- Datos para los ejercicios ---

ejercicios_infinitivo = [
    {"pregunta": "Traduce el infinitivo de presente activo 'laudare'.", "respuesta_correcta": "alabar"},
    {"pregunta": "Traduce el infinitivo de presente pasivo 'laudari'.", "respuesta_correcta": "ser alabado"},
    {"pregunta": "Traduce el infinitivo de perfecto activo 'laudavisse'.", "respuesta_correcta": "haber alabado"},
    {"pregunta": "Traduce el infinitivo de perfecto pasivo 'laudatum esse'.", "respuesta_correcta": "haber sido alabado"},
    {"pregunta": "Traduce el infinitivo de futuro activo 'laudaturum esse'.", "respuesta_correcta": "ir a alabar"},
    {"pregunta": "Traduce el infinitivo de futuro pasivo 'laudatum iri'.", "respuesta_correcta": "ir a ser alabado"},
]

ejercicios_gerundio = [
    {"pregunta": "Traduce el gerundio 'videndi' (genitivo).", "respuesta_correcta": "de ver"},
    {"pregunta": "Traduce el gerundio 'videndo' (dativo o ablativo).", "respuesta_correcta": "para ver o viendo"},
    {"pregunta": "Traduce 'amando', gerundio en ablativo.", "respuesta_correcta": "amando o por amar"},
    {"pregunta": "El gerundio es un sustantivo verbal de género neutro. ¿Qué casos tiene?", "respuesta_correcta": "genitivo, dativo, acusativo, ablativo"},
]

ejercicios_gerundivo = [
    {"pregunta": "¿Cómo se usa el gerundivo?", "respuesta_correcta": "como adjetivo"},
    {"pregunta": "Traduce 'urbs delenda' (la ciudad que debe ser destruida).", "respuesta_correcta": "la ciudad que debe ser destruida"},
    {"pregunta": "El gerundivo de 'amare' es 'amandus, a, um'. ¿Qué significa?", "respuesta_correcta": "el que debe ser amado"},
    {"pregunta": "Traduce 'liber legendus' (el libro que debe ser leído).", "respuesta_correcta": "el libro que debe ser leído"},
]

ejercicios_supino = [
    {"pregunta": "El supino de 'amare' es 'amatum'. ¿Qué significa?", "respuesta_correcta": "para amar"},
    {"pregunta": "El supino de 'audire' es 'auditu'. ¿Qué significa?", "respuesta_correcta": "de oír o para ser oído"},
    {"pregunta": "El supino en acusativo se usa con verbos de movimiento. ¿Qué indica?", "respuesta_correcta": "finalidad"},
    {"pregunta": "El supino en ablativo se usa con adjetivos. ¿Qué indica?", "respuesta_correcta": "circunstancia"},
]

ejercicios_diferenciacion = [
    {"pregunta": "Diferencia entre gerundio y gerundivo. ¿Cuál es la principal distinción?", "respuesta_correcta": "el gerundio es un sustantivo y el gerundivo es un adjetivo"},
    {"pregunta": "Traduce 'ad scribendum' (gerundio).", "respuesta_correcta": "para escribir"},
    {"pregunta": "Traduce 'ad epistulam scribendam' (gerundivo).", "respuesta_correcta": "para escribir la carta"},
    {"pregunta": "El supino y el infinitivo tienen usos de finalidad. ¿Cuál es la diferencia?", "respuesta_correcta": "el supino en -um se usa solo con verbos de movimiento"},
]

# Unimos todos los ejercicios en una sola lista para el programa
todos_los_ejercicios = ejercicios_infinitivo + ejercicios_gerundio + ejercicios_gerundivo + ejercicios_supino + ejercicios_diferenciacion

def ejecutar_ejercicios():
    """Bucle principal del programa interactivo."""
    print("--- TUTOR INTERACTIVO DE LATÍN ---")
    print("---------------------------------")
    print("¡Bienvenido! Te haré 100 preguntas sobre el infinitivo, gerundio, gerundivo y supino.")
    
    # Crea una lista de 100 ejercicios, repitiendo los definidos si es necesario
    lista_ejercicios = todos_los_ejercicios * (100 // len(todos_los_ejercicios) + 1)
    random.shuffle(lista_ejercicios)
    
    for i in range(100):
        ejercicio_actual = lista_ejercicios[i]
        
        print(f"\n--- EJERCICIO {i+1}/100 ---")
        print(ejercicio_actual['pregunta'])
        
        while True:
            respuesta_usuario = input("Tu respuesta: ").strip()
            
            # Normalizar la respuesta para que sea menos estricta
            respuesta_normalizada = respuesta_usuario.lower().strip()
            respuesta_correcta_normalizada = ejercicio_actual['respuesta_correcta'].lower().strip()

            if respuesta_normalizada in respuesta_correcta_normalizada.split(" o "):
                print("\n¡Correcto! �")
                break
            else:
                print(f"\nRespuesta incorrecta. La respuesta correcta es: '{ejercicio_actual['respuesta_correcta']}'")
                reintentar = input("¿Quieres intentarlo de nuevo? (s/n): ").strip().lower()
                if reintentar != "s":
                    break
        
    print("\n¡Has completado los 100 ejercicios! ¡Valete!")

if __name__ == "__main__":
    ejecutar_ejercicios()
