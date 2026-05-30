# -*- coding: utf-8 -*-
"""
Tutor interactivo de latín en la consola.
Este programa se enfoca en:
1. Formas nominales del verbo: El participio.
2. Sintaxis del participio.
3. Verbos irregulares: 'fero' y 'eo'.
"""
import random

# --- Datos para los ejercicios ---

ejercicios = [
    # Participio Presente
    {"tema": "Participio Presente",
     "pregunta": "¿Cómo se forma el participio de presente del verbo 'laudare' (alabar)?",
     "respuesta_correcta": "laudans, laudantis",
     "explicacion": "El participio de presente se forma con el tema de presente + '-ns' o '-ntis'. Significa 'alabando' y se declina como un adjetivo de una terminación de la tercera declinación.",
     "ejemplo": "Vir laudans (el hombre que alaba)."},
    {"tema": "Participio Presente",
     "pregunta": "Traduce 'el niño que corre' usando el participio de presente del verbo 'currere'.",
     "respuesta_correcta": "puer currens",
     "explicacion": "El participio de presente 'currens' (corriendo) concuerda con 'puer' en caso (nominativo) y número (singular).",
     "ejemplo": "Puellae currentes (las niñas que corren)."},
    
    # Participio Perfecto
    {"tema": "Participio Perfecto",
     "pregunta": "¿Cómo se forma el participio de perfecto del verbo 'amare' (amar)?",
     "respuesta_correcta": "amatus, a, um",
     "explicacion": "El participio de perfecto se forma a partir del supino (4ª forma principal) + '-us, -a, -um'. Significa 'amado' y se declina como un adjetivo de la primera clase.",
     "ejemplo": "Res amata (la cosa amada)."},
    {"tema": "Participio Perfecto",
     "pregunta": "Traduce 'la ciudad tomada' usando el participio de perfecto del verbo 'capere'.",
     "respuesta_correcta": "urbs capta",
     "explicacion": "El participio 'capta' (tomada) es el participio de perfecto femenino de 'capere' y concuerda con 'urbs' en género, número y caso.",
     "ejemplo": "Hostis victus (el enemigo vencido)."},

    # Participio Futuro
    {"tema": "Participio Futuro",
     "pregunta": "¿Cómo se forma el participio de futuro del verbo 'legere' (leer)?",
     "respuesta_correcta": "lecturus, a, um",
     "explicacion": "El participio de futuro se forma a partir del tema de supino + '-urus, -ura, -urum'. Se traduce como 'que va a leer' o 'dispuesto a leer'.",
     "ejemplo": "Puer lecturus (el niño que va a leer)."},
    {"tema": "Participio Futuro",
     "pregunta": "Traduce 'el soldado que va a luchar' usando el participio de futuro de 'pugnare'.",
     "respuesta_correcta": "miles pugnaturus",
     "explicacion": "El participio 'pugnaturus' concuerda con 'miles' en género y número. Se usa para expresar una acción futura.",
     "ejemplo": "Femina cantatura (la mujer que va a cantar)."},

    # Verbo irregular 'fero'
    {"tema": "Verbos Irregulares: Fero",
     "pregunta": "¿Cuáles son las 4 formas principales del verbo 'fero' (llevar, soportar)?",
     "respuesta_correcta": "fero, ferre, tuli, latum",
     "explicacion": "El verbo 'fero' tiene una conjugación muy irregular. Es fundamental aprender sus formas principales de memoria para conjugar sus tiempos.",
     "ejemplo": "Fero librum (llevo un libro)."},
    {"tema": "Verbos Irregulares: Fero",
     "pregunta": "Traduce la forma verbal 'tulit'.",
     "respuesta_correcta": "él/ella llevó o él/ella ha llevado",
     "explicacion": "'Tulit' es la tercera persona del singular del pretérito perfecto de 'fero', a partir de la forma 'tuli'.",
     "ejemplo": "Puer librum tulit (el niño llevó el libro)."},
    {"tema": "Verbos Irregulares: Fero",
     "pregunta": "Conjuga 'fero' en presente de indicativo, tercera persona del plural.",
     "respuesta_correcta": "ferunt",
     "explicacion": "A diferencia de los verbos de la tercera conjugación, 'fero' no añade una vocal temática 'i' antes de la desinencia 'nt'.",
     "ejemplo": "Homines bella ferunt (los hombres soportan las guerras)."},
    
    # Verbo irregular 'eo'
    {"tema": "Verbos Irregulares: Eo",
     "pregunta": "¿Cuáles son las 4 formas principales del verbo 'eo' (ir)?",
     "respuesta_correcta": "eo, ire, ii o ivi, itum",
     "explicacion": "El verbo 'eo' también es irregular. Su conjugación presenta temas diferentes para el presente y el perfecto.",
     "ejemplo": "Eo ad urbem (voy a la ciudad)."},
    {"tema": "Verbos Irregulares: Eo",
     "pregunta": "Traduce 'ibant'.",
     "respuesta_correcta": "ellos/ellas iban",
     "explicacion": "'Ibant' es el imperfecto de indicativo de 'eo', a partir de la raíz 'i' + la desinencia 'bant'.",
     "ejemplo": "Ad ludum ibant (iban a la escuela)."},
    {"tema": "Verbos Irregulares: Eo",
     "pregunta": "Conjuga 'eo' en futuro simple, segunda persona del singular.",
     "respuesta_correcta": "ibis",
     "explicacion": "El futuro simple de 'eo' se forma añadiendo las desinencias de futuro a la raíz 'i-'.",
     "ejemplo": "Cras ad forum ibis (mañana irás al foro)."},
]

def ejecutar_ejercicios():
    """Bucle principal del programa interactivo."""
    print("--- TUTOR INTERACTIVO DE LATÍN ---")
    print("---------------------------------")
    print("¡Bienvenido! Te haré 100 preguntas sobre participios y verbos irregulares 'fero' y 'eo'.")
    
    # Crea una lista de 100 ejercicios, repitiendo los definidos si es necesario
    lista_ejercicios = ejercicios * (100 // len(ejercicios) + 1)
    random.shuffle(lista_ejercicios)
    
    for i in range(100):
        ejercicio_actual = lista_ejercicios[i]
        
        print(f"\n--- EJERCICIO {i+1}/100 ---")
        print(f"Tema: {ejercicio_actual['tema']}")
        print(ejercicio_actual['pregunta'])
        
        while True:
            respuesta_usuario = input("Tu respuesta: ").strip()
            
            # Normalizar la respuesta para que sea menos estricta
            respuesta_normalizada = respuesta_usuario.lower().strip()
            respuesta_correcta_normalizada = ejercicio_actual['respuesta_correcta'].lower().strip()

            if respuesta_normalizada == respuesta_correcta_normalizada:
                print("\n¡Correcto! 😊")
                print(f"Retroalimentación: {ejercicio_actual['explicacion']}")
                print(f"Ejemplo: {ejercicio_actual['ejemplo']}")
                break
            else:
                print(f"\nRespuesta incorrecta. La respuesta correcta es: '{ejercicio_actual['respuesta_correcta']}'")
                print(f"Retroalimentación: {ejercicio_actual['explicacion']}")
                print(f"Ejemplo: {ejercicio_actual['ejemplo']}")
                reintentar = input("¿Quieres intentarlo de nuevo? (s/n): ").strip().lower()
                if reintentar != "s":
                    break
        
    print("\n¡Has completado los 100 ejercicios! ¡Valete!")

if __name__ == "__main__":
    ejecutar_ejercicios()
