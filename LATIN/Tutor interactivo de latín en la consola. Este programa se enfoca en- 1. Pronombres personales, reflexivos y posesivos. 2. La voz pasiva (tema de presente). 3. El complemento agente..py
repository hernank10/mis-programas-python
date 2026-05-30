# -*- coding: utf-8 -*-
"""
Tutor interactivo de latín en la consola.
Este programa se enfoca en:
1. Pronombres personales, reflexivos y posesivos.
2. La voz pasiva (tema de presente).
3. El complemento agente.
"""
import random

# --- Datos para los ejercicios ---

# Pronombres
pronombres = {
    "personales": {
        "ego": {"espanol": "yo", "declinacion": {"nom": "ego", "gen": "mei", "dat": "mihi", "acu": "me", "abl": "me"}},
        "tu": {"espanol": "tú", "declinacion": {"nom": "tu", "gen": "tui", "dat": "tibi", "acu": "te", "abl": "te"}},
        "nos": {"espanol": "nosotros", "declinacion": {"nom": "nos", "gen": "nostri", "dat": "nobis", "acu": "nos", "abl": "nobis"}},
        "vos": {"espanol": "vosotros", "declinacion": {"nom": "vos", "gen": "vestri", "dat": "vobis", "acu": "vos", "abl": "vobis"}}
    },
    "reflexivos": {
        "se": {"espanol": "se", "declinacion": {"gen": "sui", "dat": "sibi", "acu": "se", "abl": "se"}},
    },
    "posesivos": {
        "meus, mea, meum": {"espanol": "mi", "ejemplo": "Meus amicus (Mi amigo)."},
        "tuus, tua, tuum": {"espanol": "tu", "ejemplo": "Tu liber (Tu libro)."},
        "noster, nostra, nostrum": {"espanol": "nuestro", "ejemplo": "Noster pater (Nuestro padre)."},
        "vester, vestra, vestrum": {"espanol": "vuestro", "ejemplo": "Vester frater (Vuestro hermano)."},
        "suus, sua, suum": {"espanol": "su", "ejemplo": "Suus filius (Su hijo)."}
    }
}

# Verbos para voz pasiva (solo tema de presente)
verbos_pasivos_presente = {
    "amo, amare, amavi, amatum": {"tema_presente": "am", "conjugacion": 1, "espanol": "amar"},
    "moneo, monere, monui, monitum": {"tema_presente": "mon", "conjugacion": 2, "espanol": "amonestar"},
    "rego, regere, rexi, rectum": {"tema_presente": "reg", "conjugacion": 3, "espanol": "regir"},
    "audio, audire, audivi, auditum": {"tema_presente": "audi", "conjugacion": 4, "espanol": "oír"}
}

# Ejemplos de complemento agente
complemento_agente = [
    {"oracion_activa": "Caesar milites laudat.", "espanol_activa": "César alaba a los soldados.", "oracion_pasiva": "Milites a Caesare laudantur.", "espanol_pasiva": "Los soldados son alabados por César.", "explicacion": "El agente 'Caesar' se convierte en 'a Caesare' (ablativo con 'a/ab') en la oración pasiva."},
    {"oracion_activa": "Servi dominum timent.", "espanol_activa": "Los esclavos temen al amo.", "oracion_pasiva": "Dominus a servis timetur.", "espanol_pasiva": "El amo es temido por los esclavos.", "explicacion": "El agente 'servi' se convierte en 'a servis' (ablativo con 'a/ab') en la oración pasiva."},
    {"oracion_activa": "Poeta carmen scribit.", "espanol_activa": "El poeta escribe el poema.", "oracion_pasiva": "Carmen a poeta scribitur.", "espanol_pasiva": "El poema es escrito por el poeta.", "explicacion": "El agente 'poeta' se convierte en 'a poeta' (ablativo con 'a/ab') en la oración pasiva."},
]

# --- Funciones para generar ejercicios ---

def generar_ejercicio_pronombre():
    """Genera un ejercicio sobre pronombres."""
    tipo = random.choice(["personales", "reflexivos", "posesivos"])
    
    if tipo == "personales":
        pronombre, datos = random.choice(list(pronombres["personales"].items()))
        caso, forma = random.choice(list(datos['declinacion'].items()))
        pregunta = f"Escribe la forma del {caso} de '{pronombre}' ({datos['espanol']})."
        respuesta_correcta = forma
        explicacion = f"Los pronombres personales se declinan para indicar el caso. Por ejemplo, el genitivo de 'ego' es 'mei'."
        ejemplo = f"Ejemplo: El dativo de 'tu' es 'tibi'."
        
    elif tipo == "reflexivos":
        pronombre, datos = random.choice(list(pronombres["reflexivos"].items()))
        caso, forma = random.choice(list(datos['declinacion'].items()))
        pregunta = f"Escribe la forma del {caso} del pronombre reflexivo '{pronombre}' ({datos['espanol']})."
        respuesta_correcta = forma
        explicacion = f"El pronombre reflexivo 'se' se utiliza para referirse al sujeto de la oración en la misma persona y número. Solo tiene formas para genitivo, dativo, acusativo y ablativo."
        ejemplo = f"Ejemplo: El dativo de 'se' es 'sibi'."
        
    else: # posesivos
        pronombre_full, datos = random.choice(list(pronombres["posesivos"].items()))
        pregunta = f"¿Cómo se traduce el pronombre posesivo '{pronombre_full}'?"
        respuesta_correcta = datos["espanol"]
        explicacion = "Los pronombres posesivos concuerdan en género, número y caso con el sustantivo al que acompañan."
        ejemplo = datos["ejemplo"]
        
    return pregunta, respuesta_correcta, explicacion, ejemplo

def generar_ejercicio_voz_pasiva():
    """Genera un ejercicio sobre la voz pasiva en el tema de presente."""
    verbo, datos = random.choice(list(verbos_pasivos_presente.items()))
    
    if datos["conjugacion"] == 1:
        pasiva_forma = datos["tema_presente"] + "or"
        explicacion = "La 1ª conjugación pasiva en presente se forma con el tema de presente + '-o', y las desinencias pasivas."
    elif datos["conjugacion"] == 2:
        pasiva_forma = datos["tema_presente"] + "or"
        explicacion = "La 2ª conjugación pasiva en presente se forma con el tema de presente + '-o', y las desinencias pasivas."
    elif datos["conjugacion"] == 3:
        pasiva_forma = datos["tema_presente"] + "or"
        explicacion = "La 3ª conjugación pasiva en presente se forma con el tema de presente + '-or', y las desinencias pasivas."
    else: # 4ª conjugación
        pasiva_forma = datos["tema_presente"] + "or"
        explicacion = "La 4ª conjugación pasiva en presente se forma con el tema de presente + '-or', y las desinencias pasivas."
        
    pregunta = f"Escribe la 1ª persona del singular del presente de indicativo pasivo de '{verbo}' ({datos['espanol']})."
    respuesta_correcta = pasiva_forma
    ejemplo = f"Ejemplo: La 1ª persona del singular del presente de indicativo pasivo de 'amare' es 'amor'."
    
    return pregunta, respuesta_correcta, explicacion, ejemplo

def generar_ejercicio_complemento_agente():
    """Genera un ejercicio sobre el complemento agente."""
    ejercicio = random.choice(complemento_agente)
    
    pregunta = f"En la oración pasiva '{ejercicio['oracion_pasiva']}' ('{ejercicio['espanol_pasiva']}'), ¿cuál es la forma del complemento agente?"
    respuesta_correcta = ejercicio["oracion_pasiva"].split()[-2:]
    respuesta_correcta = " ".join(respuesta_correcta).strip(".").strip()
    
    explicacion = ejercicio["explicacion"]
    ejemplo = "Ejemplo: En 'Urbs a militibus defenditur', 'a militibus' es el complemento agente."
    
    return pregunta, respuesta_correcta, explicacion, ejemplo

def obtener_ejercicio_aleatorio():
    """Selecciona un generador de ejercicios al azar."""
    generadores = [
        generar_ejercicio_pronombre,
        generar_ejercicio_voz_pasiva,
        generar_ejercicio_complemento_agente
    ]
    return random.choice(generadores)()

def ejecutar_ejercicios():
    """Bucle principal del programa interactivo."""
    print("--- TUTOR INTERACTIVO DE LATÍN ---")
    print("---------------------------------")
    print("¡Bienvenido! Te haré 100 preguntas sobre pronombres, voz pasiva y complemento agente.")
    
    for i in range(1, 101):
        pregunta, respuesta_correcta, explicacion, ejemplo = obtener_ejercicio_aleatorio()
        
        print(f"\n--- EJERCICIO {i}/100 ---")
        print(pregunta)
        
        while True:
            respuesta_usuario = input("Tu respuesta: ").strip()
            
            if respuesta_usuario.lower() == respuesta_correcta.lower():
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
