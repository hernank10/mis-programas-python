# -*- coding: utf-8 -*-
"""
Tutor interactivo de latín en la consola.
Genera ejercicios aleatorios y ofrece retroalimentación detallada.
"""
import random

# --- Datos para los ejercicios ---

# Sustantivos de la primera declinación
sustantivos_1a = {
    "puella": {"espanol": "niña", "ejemplo_nom": "Puella videt.", "ejemplo_gen": "Rosa puellae."},
    "rosa": {"espanol": "rosa", "ejemplo_nom": "Rosa est pulchra.", "ejemplo_gen": "Familia rosae."},
    "via": {"espanol": "camino", "ejemplo_nom": "Via longa est.", "ejemplo_gen": "Finis viae."},
    "insula": {"espanol": "isla", "ejemplo_nom": "Insula parva est.", "ejemplo_gen": "Regina insulae."},
    "agricola": {"espanol": "agricultor", "ejemplo_nom": "Agricola laborat.", "ejemplo_gen": "Vita agricolae."}
}

# Verbos de la primera y segunda conjugación en presente de indicativo
verbos_1a = {
    "amare": {"conjugacion": ["amo", "amas", "amat", "amamus", "amatis", "amant"], "espanol": "amar"},
    "laudare": {"conjugacion": ["laudo", "laudas", "laudat", "laudamus", "laudatis", "laudant"], "espanol": "alabar"}
}
verbos_2a = {
    "videre": {"conjugacion": ["video", "vides", "videt", "videmus", "videtis", "vident"], "espanol": "ver"},
    "habere": {"conjugacion": ["habeo", "habes", "habet", "habemus", "habetis", "habent"], "espanol": "tener"}
}
verbo_sum = {
    "sum": {"conjugacion": ["sum", "es", "est", "sumus", "estis", "sunt"], "espanol": "ser/estar"}
}

# Frases para análisis
frases_simples = [
    {"lat": "Puella rosam videt.", "esp": "La niña ve la rosa.", "sujeto": "Puella", "od": "rosam"},
    {"lat": "Agricola in via est.", "esp": "El agricultor está en el camino.", "sujeto": "Agricola", "cc": "in via"},
    {"lat": "Poetae puellam laudant.", "esp": "Los poetas alaban a la niña.", "sujeto": "Poetae", "od": "puellam"}
]

# Palabras para la evolución fonética
evolucion_fonetica = {
    "FILIA": {"castellano": "hija", "explicacion": "La F- inicial latina se aspira y se pierde en castellano, representada por 'h' y luego se omite en la pronunciación moderna."},
    "FACERE": {"castellano": "hacer", "explicacion": "La F- inicial latina se aspira y se convierte en 'h' en castellano, reflejando un cambio fonético común."},
    "PLUVIA": {"castellano": "lluvia", "explicacion": "El grupo consonántico '-PL-' inicial latino evoluciona a '-ll-' en castellano, un proceso de palatalización."},
    "OCULUS": {"castellano": "ojo", "explicacion": "La '-C-' intervocálica latina seguida de 'u' y otra vocal se palataliza y se convierte en 'j' en castellano."}
}

# --- Funciones para generar ejercicios ---

def generar_ejercicio_declinacion():
    """Genera un ejercicio sobre la primera declinación."""
    sustantivo, datos = random.choice(list(sustantivos_1a.items()))
    tipo = random.choice(["genitivo", "dativo"])
    if tipo == "genitivo":
        pregunta = f"¿Cuál es la forma del genitivo singular de '{sustantivo}'? Su significado es 'de la {datos['espanol']}'."
        respuesta_correcta = f"{sustantivo}ae"
        explicacion = "El genitivo singular de la primera declinación se forma con la terminación '-ae'."
        ejemplo = f"Ejemplo: '{sustantivo}ae' significa 'de la {datos['espanol']}'. En la frase '{datos['ejemplo_gen']}', significa 'la rosa de la niña'."
    else: # dativo
        pregunta = f"¿Cuál es la forma del dativo plural de '{sustantivo}'? Su significado es 'a las/los {datos['espanol']}s'."
        respuesta_correcta = f"{sustantivo}is"
        explicacion = "El dativo plural de la primera declinación se forma con la terminación '-is'."
        ejemplo = f"Ejemplo: '{sustantivo}is' significa 'a las niñas'."
    return pregunta, respuesta_correcta, explicacion, ejemplo

def generar_ejercicio_ablativo():
    """Genera un ejercicio sobre la sintaxis del ablativo."""
    pregunta = "¿Qué función sintáctica suele tener el ablativo en latín, especialmente cuando va precedido por la preposición 'cum'?"
    respuesta_correcta = "complemento de compañía"
    explicacion = "El ablativo con la preposición 'cum' ('con') se utiliza para indicar compañía."
    ejemplo = "Ejemplo: En 'cum puella' ('con la niña'), 'puella' está en ablativo y cumple la función de complemento de compañía."
    return pregunta, respuesta_correcta, explicacion, ejemplo

def generar_ejercicio_verbos():
    """Genera un ejercicio sobre la conjugación verbal."""
    verbo_infinitivo, datos = random.choice(list(verbos_1a.items()) + list(verbos_2a.items()))
    persona = random.randint(0, 5)
    personas_letras = ["yo", "tú", "él/ella", "nosotros", "vosotros", "ellos"]
    pregunta = f"¿Cuál es la forma de la {persona+1}ª persona del plural del verbo '{verbo_infinitivo}' en presente de indicativo? Significa '{personas_letras[persona]} {datos['espanol']}'."
    respuesta_correcta = datos['conjugacion'][persona]
    explicacion = f"Los verbos de la {1 if verbo_infinitivo in verbos_1a else 2}ª conjugación tienen desinencias específicas en cada persona. Por ejemplo, en el presente de indicativo, la tercera persona del plural termina en '-nt'."
    ejemplo = f"Ejemplo: La tercera persona del plural de 'amare' es 'amant'."
    return pregunta, respuesta_correcta, explicacion, ejemplo

def generar_ejercicio_sum():
    """Genera un ejercicio sobre la conjugación del verbo 'sum'."""
    pregunta = "¿Cuál es la conjugación completa del verbo 'sum' (ser/estar) en presente de indicativo?"
    respuesta_correcta = "sum, es, est, sumus, estis, sunt"
    explicacion = "El verbo 'sum' es irregular, pero su conjugación en presente es fundamental y debe memorizarse: sum (yo soy), es (tú eres), est (él es), sumus (nosotros somos), estis (vosotros sois), sunt (ellos son)."
    ejemplo = "Ejemplo: 'Puella pulchra est.' ('La niña es hermosa.')."
    return pregunta, respuesta_correcta, explicacion, ejemplo

def generar_ejercicio_oracion():
    """Genera un ejercicio sobre la oración simple."""
    frase = random.choice(frases_simples)
    pregunta = f"Analiza sintácticamente la oración '{frase['lat']}'. Identifica el sujeto y el objeto directo."
    respuesta_correcta = f"Sujeto: {frase['sujeto']}, Objeto directo: {frase['od'] if 'od' in frase else 'No hay'}"
    explicacion = "El sujeto concuerda en número con el verbo y el objeto directo está en caso acusativo."
    ejemplo = f"Ejemplo: En la oración 'Poetae puellam laudant', el sujeto es 'Poetae' (nominativo plural) y el objeto directo es 'puellam' (acusativo singular)."
    return pregunta, respuesta_correcta, explicacion, ejemplo

def generar_ejercicio_hiperbaton():
    """Genera un ejercicio sobre el hiperbatón."""
    pregunta = "En latín, las palabras de una oración no siempre siguen el orden S-V-O. ¿Qué nombre recibe este fenómeno de alteración del orden sintáctico?"
    respuesta_correcta = "hiperbatón"
    explicacion = "El hiperbatón es la figura retórica que consiste en la alteración del orden sintáctico habitual de las palabras en una oración. Es muy común en latín debido a la flexibilidad de sus casos."
    ejemplo = "Ejemplo: La frase 'Magnam in silvam puella ambulat' (La niña camina hacia el gran bosque) tiene las palabras separadas de su orden lógico."
    return pregunta, respuesta_correcta, explicacion, ejemplo

def generar_ejercicio_fonetica():
    """Genera un ejercicio sobre la evolución fonética."""
    latina, datos = random.choice(list(evolucion_fonetica.items()))
    pregunta = f"¿A qué palabra castellana ha evolucionado el vocablo latino '{latina}'? Explica brevemente el cambio fonético."
    respuesta_correcta = datos['castellano']
    explicacion = datos['explicacion']
    ejemplo = f"Ejemplo: La palabra 'FACERE' ha evolucionado a 'hacer'."
    return pregunta, respuesta_correcta, explicacion, ejemplo

def obtener_ejercicio_aleatorio():
    """Selecciona un generador de ejercicios al azar."""
    generadores = [
        generar_ejercicio_declinacion,
        generar_ejercicio_ablativo,
        generar_ejercicio_verbos,
        generar_ejercicio_sum,
        generar_ejercicio_oracion,
        generar_ejercicio_hiperbaton,
        generar_ejercicio_fonetica
    ]
    return random.choice(generadores)()

def ejecutar_ejercicios():
    """Bucle principal del programa interactivo."""
    print("--- TUTOR INTERACTIVO DE LATÍN ---")
    print("-----------------------------------")
    print("¡Bienvenido! Te haré una pregunta de latín. Responde y te daré retroalimentación.")
    
    continuar = "s"
    while continuar.lower() == "s":
        pregunta, respuesta_correcta, explicacion, ejemplo = obtener_ejercicio_aleatorio()
        
        print("\n--- NUEVO EJERCICIO ---")
        print(pregunta)
        
        # Intentos para el mismo ejercicio
        intento = 1
        while True:
            respuesta_usuario = input("Tu respuesta: ").strip().lower()
            
            # Un chequeo básico, pero útil para la interacción
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
                
        continuar = input("\n¿Quieres pasar al siguiente ejercicio? (s/n): ").strip().lower()
    
    print("\n¡Gracias por practicar! ¡Valete!")

if __name__ == "__main__":
    ejecutar_ejercicios()
