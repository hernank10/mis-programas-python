# -*- coding: utf-8 -*-
"""
Tutor interactivo de latín en la consola.
Este programa se enfoca en el vocabulario básico.
"""
import random

# --- Datos para los ejercicios de vocabulario ---

ejercicios_vocabulario = [
    # Sustantivos
    {"palabra": "puer", "traduccion": "niño", "tipo": "sustantivo", "explicacion": "puer, pueri (m) -> niño"},
    {"palabra": "puella", "traduccion": "niña", "tipo": "sustantivo", "explicacion": "puella, puellae (f) -> niña"},
    {"palabra": "servus", "traduccion": "esclavo", "tipo": "sustantivo", "explicacion": "servus, servi (m) -> esclavo"},
    {"palabra": "domus", "traduccion": "casa", "tipo": "sustantivo", "explicacion": "domus, domus (f) -> casa"},
    {"palabra": "urbis", "traduccion": "ciudad", "tipo": "sustantivo", "explicacion": "urbs, urbis (f) -> ciudad"},
    {"palabra": "terra", "traduccion": "tierra", "tipo": "sustantivo", "explicacion": "terra, terrae (f) -> tierra"},
    {"palabra": "pater", "traduccion": "padre", "tipo": "sustantivo", "explicacion": "pater, patris (m) -> padre"},
    {"palabra": "mater", "traduccion": "madre", "tipo": "sustantivo", "explicacion": "mater, matris (f) -> madre"},
    {"palabra": "filius", "traduccion": "hijo", "tipo": "sustantivo", "explicacion": "filius, filii (m) -> hijo"},
    {"palabra": "flumen", "traduccion": "río", "tipo": "sustantivo", "explicacion": "flumen, fluminis (n) -> río"},
    {"palabra": "bellum", "traduccion": "guerra", "tipo": "sustantivo", "explicacion": "bellum, belli (n) -> guerra"},
    {"palabra": "liber", "traduccion": "libro", "tipo": "sustantivo", "explicacion": "liber, libri (m) -> libro"},
    {"palabra": "amicus", "traduccion": "amigo", "tipo": "sustantivo", "explicacion": "amicus, amici (m) -> amigo"},

    # Verbos
    {"palabra": "amare", "traduccion": "amar", "tipo": "verbo", "explicacion": "amare -> infinitivo del verbo 'amar'"},
    {"palabra": "videre", "traduccion": "ver", "tipo": "verbo", "explicacion": "videre -> infinitivo del verbo 'ver'"},
    {"palabra": "audire", "traduccion": "oír", "tipo": "verbo", "explicacion": "audire -> infinitivo del verbo 'oír'"},
    {"palabra": "facere", "traduccion": "hacer", "tipo": "verbo", "explicacion": "facere -> infinitivo del verbo 'hacer'"},
    {"palabra": "ducere", "traduccion": "conducir", "tipo": "verbo", "explicacion": "ducere -> infinitivo del verbo 'conducir'"},
    {"palabra": "esse", "traduccion": "ser", "tipo": "verbo", "explicacion": "esse -> infinitivo del verbo 'ser'"},
    {"palabra": "habere", "traduccion": "tener", "tipo": "verbo", "explicacion": "habere -> infinitivo del verbo 'tener'"},
    {"palabra": "venire", "traduccion": "venir", "tipo": "verbo", "explicacion": "venire -> infinitivo del verbo 'venir'"},
    {"palabra": "ire", "traduccion": "ir", "tipo": "verbo", "explicacion": "ire -> infinitivo del verbo 'ir'"},

    # Adjetivos
    {"palabra": "magnus", "traduccion": "grande", "tipo": "adjetivo", "explicacion": "magnus, magna, magnum -> grande"},
    {"palabra": "bonus", "traduccion": "bueno", "tipo": "adjetivo", "explicacion": "bonus, bona, bonum -> bueno"},
    {"palabra": "malus", "traduccion": "malo", "tipo": "adjetivo", "explicacion": "malus, mala, malum -> malo"},
    {"palabra": "pulcher", "traduccion": "hermoso", "tipo": "adjetivo", "explicacion": "pulcher, pulchra, pulchrum -> hermoso"},
    {"palabra": "altus", "traduccion": "alto", "tipo": "adjetivo", "explicacion": "altus, alta, altum -> alto"},

    # Adverbios y conjunciones
    {"palabra": "semper", "traduccion": "siempre", "tipo": "adverbio", "explicacion": "semper -> siempre"},
    {"palabra": "saepe", "traduccion": "a menudo", "tipo": "adverbio", "explicacion": "saepe -> a menudo, frecuentemente"},
    {"palabra": "non", "traduccion": "no", "tipo": "adverbio", "explicacion": "non -> no"},
    {"palabra": "et", "traduccion": "y", "tipo": "conjunción", "explicacion": "et -> y"},
    {"palabra": "sed", "traduccion": "pero", "tipo": "conjunción", "explicacion": "sed -> pero, sino"},
    {"palabra": "aut", "traduccion": "o", "tipo": "conjunción", "explicacion": "aut -> o"},
]

def ejecutar_ejercicios():
    """Bucle principal del programa interactivo."""
    print("--- TUTOR INTERACTIVO DE LATÍN ---")
    print("---------------------------------")
    print("¡Bienvenido! Te haré 100 preguntas de vocabulario básico de latín.")
    print("Simplemente escribe la traducción al español de la palabra que se te presente.")
    
    # Crea una lista de 100 ejercicios, repitiendo los definidos si es necesario
    lista_ejercicios = ejercicios_vocabulario * (100 // len(ejercicios_vocabulario) + 1)
    random.shuffle(lista_ejercicios)
    
    for i in range(100):
        ejercicio_actual = lista_ejercicios[i]
        
        print(f"\n--- EJERCICIO {i+1}/100 ---")
        print(f"Palabra latina: '{ejercicio_actual['palabra']}'")
        
        while True:
            respuesta_usuario = input("Tu traducción: ").strip()
            
            # Normalizar la respuesta para que sea menos estricta
            respuesta_normalizada = respuesta_usuario.lower().strip()
            respuesta_correcta_normalizada = ejercicio_actual['traduccion'].lower().strip()
            
            if respuesta_normalizada == respuesta_correcta_normalizada:
                print("\n¡Correcto! 😊")
                print(f"Retroalimentación: {ejercicio_actual['explicacion']}")
                break
            else:
                print(f"\nRespuesta incorrecta. La traducción correcta es: '{ejercicio_actual['traduccion']}'")
                print(f"Retroalimentación: {ejercicio_actual['explicacion']}")
                reintentar = input("¿Quieres intentarlo de nuevo? (s/n): ").strip().lower()
                if reintentar != "s":
                    break
        
    print("\n¡Has completado los 100 ejercicios! ¡Valete!")

if __name__ == "__main__":
    ejecutar_ejercicios()
