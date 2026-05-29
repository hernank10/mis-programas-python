# -*- coding: utf-8 -*-
"""
Tutor interactivo de latín en la consola.
Este programa se enfoca en:
1. Adjetivo de la 2ª clase
2. El comparativo
3. Morfología del infinitivo
4. Sintaxis del infinitivo
"""
import random

# --- Datos para los ejercicios ---

# Adjetivos de la 2ª clase (temas en -i)
adjetivos_2a = {
    "fortis": {"genero": "fuerte (m/f)", "neutro": "forte", "espanol": "fuerte"},
    "gravis": {"genero": "grave (m/f)", "neutro": "grave", "espanol": "grave"},
    "omnis": {"genero": "todo (m/f)", "neutro": "omne", "espanol": "todo"},
    "celer": {"genero": "rápido (m)", "feminino": "celeris", "neutro": "celere", "espanol": "rápido"},
}

# Ejemplos para comparativos
adjetivos_comparativo = {
    "altus, -a, -um": {"raiz": "alt", "espanol": "alto", "comparativo_m_f": "altior", "comparativo_n": "altius"},
    "pulcher, -chra, -chrum": {"raiz": "pulchr", "espanol": "hermoso", "comparativo_m_f": "pulchrior", "comparativo_n": "pulchrius"},
    "brevis, -e": {"raiz": "brev", "espanol": "breve", "comparativo_m_f": "brevior", "comparativo_n": "brevius"},
}

# Desinencias del comparativo
desinencias_comp = {
    "nom_s_m_f": "ior", "nom_s_n": "ius",
    "gen_s_m_f": "ioris", "gen_s_n": "ioris",
    "dat_s_m_f": "iori", "dat_s_n": "iori",
    "acu_s_m_f": "iorem", "acu_s_n": "ius",
    "abl_s_m_f": "iore", "abl_s_n": "iore",
    "nom_p_m_f": "iores", "nom_p_n": "iora",
    "gen_p_m_f": "iorum", "gen_p_n": "iorum",
    "dat_p_m_f": "ioribus", "dat_p_n": "ioribus",
    "acu_p_m_f": "iores", "acu_p_n": "iora",
    "abl_p_m_f": "ioribus", "abl_p_n": "ioribus",
}

# Verbos para infinitivos (presente, perfecto, futuro - activo y pasivo)
verbos_infinitivo = {
    "amare": {"conjugacion": 1, "raiz_presente": "ama", "raiz_perfecto": "amav", "espanol": "amar"},
    "monere": {"conjugacion": 2, "raiz_presente": "mone", "raiz_perfecto": "monu", "espanol": "amonestar"},
    "regere": {"conjugacion": 3, "raiz_presente": "reg", "raiz_perfecto": "rex", "espanol": "regir"},
    "audire": {"conjugacion": 4, "raiz_presente": "audi", "raiz_perfecto": "audiv", "espanol": "oír"},
    "ducere": {"conjugacion": 3, "raiz_presente": "duc", "raiz_perfecto": "dux", "espanol": "conducir"},
}

# Sintaxis del infinitivo
sintaxis_infinitivo = [
    {"ejemplo": "Volo ire.", "espanol": "Quiero ir.", "funcion": "Sujeto de 'volo'", "explicacion": "El infinitivo 'ire' funciona como sujeto de un verbo personal."},
    {"ejemplo": "Difficile est docere.", "espanol": "Es difícil enseñar.", "funcion": "Sujeto de 'est'", "explicacion": "El infinitivo 'docere' es el sujeto de la oración."},
    {"ejemplo": "Gaudet me videre.", "espanol": "Se alegra de verme.", "funcion": "Complemento de 'gaudet'", "explicacion": "El infinitivo 'videre' actúa como complemento del verbo 'gaudet' (verbo de sentimiento)."},
    {"ejemplo": "Scio te venire.", "espanol": "Sé que vienes.", "funcion": "Objeto de 'scio'", "explicacion": "El infinitivo 'venire' está en una oración de infinitivo con el verbo de pensamiento 'scio', y funciona como objeto directo."},
    {"ejemplo": "Paratus sum pugnare.", "espanol": "Estoy preparado para luchar.", "funcion": "Complemento de 'paratus'", "explicacion": "El infinitivo 'pugnare' complementa a un adjetivo ('paratus')."}
]


# --- Funciones para generar ejercicios ---

def generar_ejercicio_adjetivo_2a():
    """Genera un ejercicio sobre la 2ª clase de adjetivos."""
    adjetivo, datos = random.choice(list(adjetivos_2a.items()))
    pregunta_tipo = random.choice(["genero", "neutro"])
    
    if pregunta_tipo == "genero":
        pregunta = f"Escribe la forma del adjetivo '{adjetivo}' ({datos['espanol']}) para el género masculino/femenino."
        respuesta_correcta = datos['genero']
    else:
        pregunta = f"Escribe la forma del adjetivo '{adjetivo}' ({datos['espanol']}) para el género neutro."
        respuesta_correcta = datos['neutro']
    
    explicacion = f"Los adjetivos de la segunda clase (o temas en -i-) se caracterizan por tener un nominativo singular en '-is' (m/f) y '-e' (n), o en '-er' (m), '-ris' (f) y '-re' (n)."
    ejemplo = f"Ejemplo: El nominativo singular de 'omnis' es 'omnis' para m/f y 'omne' para neutro."
    return pregunta, respuesta_correcta, explicacion, ejemplo


def generar_ejercicio_comparativo():
    """Genera un ejercicio sobre el comparativo."""
    adjetivo, datos = random.choice(list(adjetivos_comparativo.items()))
    pregunta_tipo = random.choice(["formar", "declinar"])
    
    if pregunta_tipo == "formar":
        genero = random.choice(["m/f", "n"])
        if genero == "m/f":
            pregunta = f"Forma el comparativo para el género masculino/femenino del adjetivo '{adjetivo}' ({datos['espanol']})."
            respuesta_correcta = datos['comparativo_m_f']
        else:
            pregunta = f"Forma el comparativo para el género neutro del adjetivo '{adjetivo}' ({datos['espanol']})."
            respuesta_correcta = datos['comparativo_n']
        
        explicacion = f"El comparativo de superioridad se forma añadiendo a la raíz del adjetivo la terminación '-ior' para m/f y '-ius' para neutro."
        ejemplo = f"Ejemplo: La raíz de 'altus' es 'alt-', por lo que el comparativo es 'altior'/'altius'."
    else:
        caso, forma_comp = random.choice(list(desinencias_comp.items()))
        raiz = datos['raiz']
        
        pregunta = f"Escribe la forma del comparativo '{datos['comparativo_m_f']}' en {caso.replace('_', ' ')}."
        respuesta_correcta = raiz + forma_comp
        explicacion = f"El comparativo se declina por la tercera declinación, pero con sus propias desinencias. Todos los géneros tienen '-iorum' en el genitivo plural y '-ioribus' en dativo/ablativo plural."
        ejemplo = f"Ejemplo: El nominativo singular masculino/femenino de 'altior' es 'altior'."
        
    return pregunta, respuesta_correcta, explicacion, ejemplo

def generar_ejercicio_morfologia_infinitivo():
    """Genera un ejercicio sobre la morfología del infinitivo."""
    verbo, datos = random.choice(list(verbos_infinitivo.items()))
    tiempo_voz = random.choice(["presente_activo", "presente_pasivo", "perfecto_activo", "perfecto_pasivo", "futuro_activo"])
    
    raiz_presente = datos['raiz_presente']
    raiz_perfecto = datos['raiz_perfecto']
    espanol = datos['espanol']
    
    if tiempo_voz == "presente_activo":
        if datos['conjugacion'] == 1:
            infinitivo = raiz_presente + "re"
        elif datos['conjugacion'] == 2:
            infinitivo = raiz_presente + "re"
        elif datos['conjugacion'] == 3:
            infinitivo = raiz_presente + "ere"
        else: # 4ª
            infinitivo = raiz_presente + "re"
    elif tiempo_voz == "presente_pasivo":
        if datos['conjugacion'] in [1, 2, 4]:
            infinitivo = raiz_presente + "ri"
        else: # 3ª
            infinitivo = raiz_presente + "i"
    elif tiempo_voz == "perfecto_activo":
        infinitivo = raiz_perfecto + "isse"
    elif tiempo_voz == "perfecto_pasivo":
        # Se forma con el supino y 'esse'
        # No se incluye el supino en este ejercicio para simplificar
        infinitivo = f"Forma con participio de perfecto + esse (ej: 'amatum esse')"
        respuesta_correcta = "amatum esse" # Ejemplo para simplificar
        pregunta = f"¿Cómo se forma el infinitivo perfecto pasivo? Da un ejemplo con 'amare'."
        explicacion = "El infinitivo perfecto pasivo se forma con el supino (amatus, -a, -um) en acusativo neutro y el infinitivo del verbo 'ser' ('esse')."
        return pregunta, respuesta_correcta, explicacion, "Ejemplo: amatum esse."
    else: # futuro_activo
        # Se forma con el participio de futuro y 'esse'
        infinitivo = f"Forma con participio de futuro + esse (ej: 'amaturum esse')"
        respuesta_correcta = "amaturum esse"
        pregunta = f"¿Cómo se forma el infinitivo futuro activo? Da un ejemplo con 'amare'."
        explicacion = "El infinitivo futuro activo se forma con el participio de futuro (amaturus, -a, -um) en acusativo neutro y el infinitivo del verbo 'ser' ('esse')."
        return pregunta, respuesta_correcta, explicacion, "Ejemplo: amaturum esse."
        
    pregunta = f"Escribe el infinitivo {tiempo_voz.replace('_', ' ')} del verbo '{verbo}' ({espanol})."
    respuesta_correcta = infinitivo
    explicacion = f"La morfología del infinitivo depende del tiempo y la voz. Se forman a partir de la raíz de presente o de perfecto del verbo."
    ejemplo = f"Ejemplo: El infinitivo de 'amare' para presente activo es 'amare'."
    return pregunta, respuesta_correcta, explicacion, ejemplo

def generar_ejercicio_sintaxis_infinitivo():
    """Genera un ejercicio sobre la sintaxis del infinitivo."""
    ejercicio = random.choice(sintaxis_infinitivo)
    pregunta = f"En la oración '{ejercicio['ejemplo']}' ('{ejercicio['espanol']}'), ¿cuál es la función del infinitivo?"
    respuesta_correcta = ejercicio['funcion']
    explicacion = ejercicio['explicacion']
    ejemplo = f"Ejemplo: En 'Volumus pugnare', 'pugnare' es el sujeto de 'volumus'."
    return pregunta, respuesta_correcta, explicacion, ejemplo


def obtener_ejercicio_aleatorio():
    """Selecciona un generador de ejercicios al azar."""
    generadores = [
        generar_ejercicio_adjetivo_2a,
        generar_ejercicio_comparativo,
        generar_ejercicio_morfologia_infinitivo,
        generar_ejercicio_sintaxis_infinitivo
    ]
    return random.choice(generadores)()


def ejecutar_ejercicios():
    """Bucle principal del programa interactivo."""
    print("--- TUTOR INTERACTIVO DE LATÍN ---")
    print("---------------------------------")
    print("¡Bienvenido! Te haré 100 preguntas sobre adjetivos, comparativos e infinitivos.")
    
    for i in range(1, 101):
        pregunta, respuesta_correcta, explicacion, ejemplo = obtener_ejercicio_aleatorio()
        
        print(f"\n--- EJERCICIO {i}/100 ---")
        print(pregunta)
        
        while True:
            respuesta_usuario = input("Tu respuesta: ").strip().lower()
            
            if respuesta_usuario == respuesta_correcta.lower():
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
