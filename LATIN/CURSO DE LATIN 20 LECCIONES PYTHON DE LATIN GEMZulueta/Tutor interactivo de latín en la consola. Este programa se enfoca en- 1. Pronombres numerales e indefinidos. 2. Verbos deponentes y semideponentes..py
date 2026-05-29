# -*- coding: utf-8 -*-
"""
Tutor interactivo de latín en la consola.
Este programa se enfoca en:
1. Pronombres numerales e indefinidos.
2. Verbos deponentes y semideponentes.
"""
import random

# --- Datos para los ejercicios ---

# Pronombres numerales e indefinidos
numerales = {
    "unus, a, um": {"tipo": "cardinal", "traduccion": "uno"},
    "duo, duae, duo": {"tipo": "cardinal", "traduccion": "dos"},
    "tres, tres, tria": {"tipo": "cardinal", "traduccion": "tres"},
    "primus, a, um": {"tipo": "ordinal", "traduccion": "primero"},
    "secundus, a, um": {"tipo": "ordinal", "traduccion": "segundo"},
    "tertius, a, um": {"tipo": "ordinal", "traduccion": "tercero"},
    "singuli, ae, a": {"tipo": "distributivo", "traduccion": "uno cada uno"},
    "bis": {"tipo": "adverbio numeral", "traduccion": "dos veces"}
}

indefinidos = {
    "aliquis, aliqua, aliquid": {"traduccion": "alguien, algo (connotación positiva)"},
    "quidam, quaedam, quiddam": {"traduccion": "cierto, una persona (identidad conocida pero no especificada)"},
    "quisque, quaeque, quidque": {"traduccion": "cada uno, cada cosa"},
    "nemo": {"traduccion": "nadie"},
    "nihil": {"traduccion": "nada"},
    "uterque, utraque, utrumque": {"traduccion": "uno y otro, ambos"}
}

# Verbos deponentes y semideponentes
deponentes = {
    "loquor, loqui, locutus sum": {"traduccion": "hablar", "conjugacion": "Tiene forma pasiva, pero significado activo."},
    "hortor, hortari, hortatus sum": {"traduccion": "exhortar", "conjugacion": "Tiene forma pasiva, pero significado activo."},
    "sequor, sequi, secutus sum": {"traduccion": "seguir", "conjugacion": "Tiene forma pasiva, pero significado activo."},
    "utror, uti, usus sum": {"traduccion": "usar", "conjugacion": "Tiene forma pasiva, pero significado activo."}
}

semideponentes = {
    "audeo, audere, ausus sum": {"traduccion": "osar, atreverse", "conjugacion": "Presente y temas de infectum son activos, pero el tema de perfectum es pasivo."},
    "soleo, solere, solitus sum": {"traduccion": "soler", "conjugacion": "Presente y temas de infectum son activos, pero el tema de perfectum es pasivo."},
    "gaudeo, gaudere, gavisus sum": {"traduccion": "alegrarse", "conjugacion": "Presente y temas de infectum son activos, pero el tema de perfectum es pasivo."}
}

# --- Funciones para generar ejercicios ---

def generar_ejercicio_numerales_indefinidos():
    """Genera un ejercicio sobre numerales o indefinidos."""
    tipo_pronombre = random.choice(["numeral", "indefinido"])
    
    if tipo_pronombre == "numeral":
        pronombre, datos = random.choice(list(numerales.items()))
        pregunta = f"¿Cómo se traduce el pronombre/adverbio numeral '{pronombre}'?"
        respuesta_correcta = datos["traduccion"]
        explicacion = f"'{pronombre}' es un numeral de tipo '{datos['tipo']}' y significa '{datos['traduccion']}'."
        ejemplo = f"Ejemplo: 'Unus homo venit' (Un solo hombre vino)."
    else: # indefinido
        pronombre, datos = random.choice(list(indefinidos.items()))
        pregunta = f"¿Cómo se traduce el pronombre indefinido '{pronombre}'?"
        respuesta_correcta = datos["traduccion"]
        explicacion = f"'{pronombre}' significa '{datos['traduccion']}'. Se utiliza para referirse a una persona o cosa sin especificar su identidad."
        ejemplo = f"Ejemplo: 'Aliqua mulier me vocavit' (Alguna mujer me llamó)."
        
    return pregunta, respuesta_correcta, explicacion, ejemplo

def generar_ejercicio_deponentes_semideponentes():
    """Genera un ejercicio sobre verbos deponentes o semideponentes."""
    tipo_verbo = random.choice(["deponente", "semideponente"])
    
    if tipo_verbo == "deponente":
        verbo, datos = random.choice(list(deponentes.items()))
        partes = verbo.split(", ")
        pregunta = f"El verbo deponente '{partes[0]}' ({datos['traduccion']}) tiene forma pasiva pero significado activo. ¿Cómo se traduce su pretérito perfecto '{partes[2]}'? "
        respuesta_correcta = f"he {datos['traduccion'].split()[-1]}o"
        explicacion = f"Los verbos deponentes se conjugan como pasivos, pero se traducen como activos. '{partes[2]}' significa '{respuesta_correcta}'."
        ejemplo = f"Ejemplo: 'Locutus sum' (he hablado)."
    else: # semideponente
        verbo, datos = random.choice(list(semideponentes.items()))
        partes = verbo.split(", ")
        pregunta = f"El verbo semideponente '{partes[0]}' ({datos['traduccion']}) ¿tiene forma activa o pasiva en el presente?"
        respuesta_correcta = "activa"
        explicacion = f"Los verbos semideponentes, como '{partes[0]}', se conjugan en forma activa en el tema de infectum (presente, imperfecto, futuro imperfecto), pero en forma pasiva en el tema de perfectum (perfecto, pluscuamperfecto, futuro perfecto)."
        ejemplo = f"Ejemplo: 'Gaudeo' (me alegro) es una forma activa, mientras que 'gavisus sum' (me he alegrado) es una forma pasiva."
        
    return pregunta, respuesta_correcta, explicacion, ejemplo

def ejecutar_ejercicios():
    """Bucle principal del programa interactivo."""
    print("--- TUTOR INTERACTIVO DE LATÍN ---")
    print("---------------------------------")
    print("¡Bienvenido! Te haré 100 preguntas sobre numerales, indefinidos y verbos deponentes/semideponentes.")
    
    for i in range(1, 101):
        # Seleccionar un tipo de ejercicio al azar
        generador = random.choice([generar_ejercicio_numerales_indefinidos, generar_ejercicio_deponentes_semideponentes])
        pregunta, respuesta_correcta, explicacion, ejemplo = generador()
        
        print(f"\n--- EJERCICIO {i}/100 ---")
        print(pregunta)
        
        while True:
            respuesta_usuario = input("Tu respuesta: ").strip()
            
            # Normalizar la respuesta para que sea más flexible
            respuesta_normalizada = respuesta_usuario.lower().replace("la forma ", "").replace("forma ", "").replace(" el ", "").replace("la ", "").replace("del ", "").replace("de ", "").replace(" ", "")
            respuesta_correcta_normalizada = respuesta_correcta.lower().replace(" ", "")

            if respuesta_normalizada == respuesta_correcta_normalizada:
                print("\n¡Correcto! 😊")
                print(f"Retroalimentación: {explicacion}")
                print(f"Ejemplo: {ejemplo}")
                break
            else:
                print(f"\nRespuesta incorrecta. La respuesta correcta es: '{respuesta_correcta}'")
                print(f"Retroalimentación: {explicacion}")
                print(f"Ejemplo: {ejemplo}")
                reintentar = input("¿Quieres intentarlo de nuevo? (s/n): ").strip().lower()
                if reintentar != "s":
                    break
        
    print("\n¡Has completado los 100 ejercicios! ¡Valete!")

if __name__ == "__main__":
    ejecutar_ejercicios()
