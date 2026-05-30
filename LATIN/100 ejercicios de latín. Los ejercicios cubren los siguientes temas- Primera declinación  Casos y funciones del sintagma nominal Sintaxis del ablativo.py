# -*- coding: utf-8 -*-
"""
Programa de consola en Python para generar 100 ejercicios de latín.
Los ejercicios cubren los siguientes temas:
1. Primera declinación
2. Casos y funciones del sintagma nominal
3. Sintaxis del ablativo
4. Paradigma del tema presente de sum, 1ª y 2ª conjugaciones
5. La oración simple
6. Hiperbatón
7. Evolución de las consonantes del latín al castellano
"""

import random

# --- Datos para los ejercicios ---

# Sustantivos de la primera declinación
sustantivos_1a = ["puella", "rosa", "via", "insula", "agricola", "poeta", "familia", "silva"]

# Verbos de la primera y segunda conjugación en presente de indicativo
verbos_1a = [("amare", "amar"), ("laudare", "alabar"), ("pugnare", "luchar"), ("cantare", "cantar")]
verbos_2a = [("videre", "ver"), ("habere", "tener"), ("tenere", "sostener"), ("monere", "advertir")]
verbo_sum = [("sum", "ser")]

# Frases para analizar
frases_simples = [
    ("Puella rosam pulchram videt.", "La niña ve la rosa hermosa."),
    ("Familia in insula habitat.", "La familia vive en la isla."),
    ("Poetae agricolas laudant.", "Los poetas alaban a los agricultores."),
    ("Rosae in silvis sunt.", "Las rosas están en los bosques."),
    ("Agricola viam longam monstrat.", "El agricultor muestra el camino largo.")
]

# Palabras para la evolución fonética
evolucion_fonetica = {
    "FILIA": "hija",
    "FACERE": "hacer",
    "FORMICA": "hormiga",
    "LUPUS": "lobo",
    "OCULUS": "ojo",
    "APICULA": "abeja",
    "FRATRE": "fraile",
    "PLUVIA": "lluvia",
    "FLAMMA": "llama",
    "CLAVEM": "llave"
}

# --- Funciones para generar ejercicios ---

def generar_1a_declinacion():
    """Genera un ejercicio sobre la primera declinación."""
    sustantivo = random.choice(sustantivos_1a)
    ejercicios = [
        f"Declina el sustantivo '{sustantivo}' (singular y plural).",
        f"Identifica el caso, número y función de '{sustantivo}e'.",
        f"¿Cuál es el genitivo singular de '{sustantivo}'? ¿Y su dativo plural?",
        f"Traduce la forma latina para 'a la {sustantivo}'.",
        f"Traduce la forma latina para 'de las {sustantivo}s'."
    ]
    return random.choice(ejercicios)

def generar_casos_funciones():
    """Genera un ejercicio sobre casos y funciones."""
    frase_latina, frase_espanol = random.choice(frases_simples)
    analisis = random.choice(["sujeto", "objeto directo", "complemento circunstancial"])
    if analisis == "sujeto":
        # Extrae el sujeto de la frase
        sujeto_latino = frase_latina.split()[0].replace('.', '')
        return f"En la oración '{frase_latina}', identifica el caso y la función de '{sujeto_latino}'."
    elif analisis == "objeto directo":
        # Extrae el objeto directo
        od_latino = frase_latina.split()[1].replace('.', '')
        return f"En la oración '{frase_latina}', identifica el caso y la función de '{od_latino}'."
    else:
        # Extrae el complemento circunstancial (si existe)
        cc_latino = " ".join(frase_latina.split()[-2:]).replace('.', '')
        if "in" in cc_latino:
            return f"En la oración '{frase_latina}', identifica el caso y la función de '{cc_latino}'."
        else:
            return f"Traduce al latín: '{frase_espanol}'. Identifica el caso del sintagma nominal."

def generar_sintaxis_ablativo():
    """Genera un ejercicio sobre la sintaxis del ablativo."""
    ejercicios = [
        "¿Qué función sintáctica cumple el ablativo en la frase 'in horto'? Explica el tipo de ablativo.",
        "Traduce la frase 'Con el poeta y la rosa'. ¿En qué caso se usan los sustantivos?",
        "Escribe una oración en latín donde el ablativo cumpla la función de 'complemento de compañía'.",
        "En la oración 'magna cum cura' ¿qué tipo de ablativo es? Tradúcela.",
        "Identifica y explica el uso del ablativo en la oración 'Agricola via in agris ambulat'."
    ]
    return random.choice(ejercicios)

def generar_verbos():
    """Genera un ejercicio sobre la conjugación verbal."""
    verbo_elegido_1 = random.choice(verbos_1a)
    verbo_elegido_2 = random.choice(verbos_2a)
    verbo_elegido_3 = verbo_sum[0]
    
    ejercicios = [
        f"Conjuga el verbo '{verbo_elegido_1[0]}' (1ª conj.) en presente de indicativo.",
        f"Conjuga el verbo '{verbo_elegido_2[0]}' (2ª conj.) en presente de indicativo.",
        f"Completa la conjugación de 'sum' en presente: 'sum, es, ..., ..., estis, ...'.",
        f"Identifica el verbo y su persona/número en la forma 'laudatis'.",
        f"Traduce al español la forma verbal 'habemus'."
    ]
    return random.choice(ejercicios)

def generar_oracion_simple():
    """Genera un ejercicio sobre la oración simple."""
    frase_latina, frase_espanol = random.choice(frases_simples)
    ejercicios = [
        f"Realiza un análisis sintáctico de la oración '{frase_latina}'.",
        f"Traduce la oración '{frase_latina}' e identifica su sujeto, verbo y objeto directo.",
        f"Crea una oración simple en latín con un verbo de la 2ª conjugación.",
        f"En la oración '{frase_espanol}', traduce y subraya el sujeto.",
        f"¿Qué elementos mínimos necesita una oración simple en latín? Da un ejemplo."
    ]
    return random.choice(ejercicios)

def generar_hiperbaton():
    """Genera un ejercicio sobre hiperbatón."""
    frase_hiperbaton = "Magna pulchra puella est."
    ejercicios = [
        f"Reordena la frase en latín '{frase_hiperbaton}' para entender mejor su significado en español.",
        "Explica qué es el hiperbatón y por qué es común en latín.",
        f"Crea una oración con hiperbatón usando los sustantivos 'silva' y 'puella'."
    ]
    return random.choice(ejercicios)

def generar_evolucion_fonetica():
    """Genera un ejercicio sobre la evolución fonética."""
    latina, espanol = random.choice(list(evolucion_fonetica.items()))
    ejercicios = [
        f"Explica la evolución de la 'F-' inicial en la transición de '{latina}' a '{espanol}'.",
        f"¿Por qué el grupo '-PL-' en latín da lugar a '-ll-' en castellano? Usa '{latina}' como ejemplo.",
        f"¿Qué fenómeno fonético se observa en la evolución de '{latina}' a '{espanol}'?"
    ]
    return random.choice(ejercicios)

# --- Bucle principal para generar los 100 ejercicios ---

print("--- 100 EJERCICIOS DE LATÍN ---")
print("------------------------------\n")

for i in range(1, 101):
    ejercicio_tipo = i % 7
    if ejercicio_tipo == 0 or i <= 15:
        ejercicio = generar_1a_declinacion()
    elif ejercicio_tipo == 1 or i <= 30:
        ejercicio = generar_casos_funciones()
    elif ejercicio_tipo == 2 or i <= 45:
        ejercicio = generar_sintaxis_ablativo()
    elif ejercicio_tipo == 3 or i <= 60:
        ejercicio = generar_verbos()
    elif ejercicio_tipo == 4 or i <= 75:
        ejercicio = generar_oracion_simple()
    elif ejercicio_tipo == 5 or i <= 90:
        ejercicio = generar_hiperbaton()
    else:
        ejercicio = generar_evolucion_fonetica()

    print(f"{i}. {ejercicio}\n")
