# Diccionario que contiene las conjugaciones correctas de verbos científicos en inglés y español
conjugaciones_verbos = {
    "analyze": {
        "present": {
            "I": "analyze", "you": "analyze", "he/she/it": "analyzes",
            "we": "analyze", "you (plural)": "analyze", "they": "analyze"
        },
        "past": {
            "I": "analyzed", "you": "analyzed", "he/she/it": "analyzed",
            "we": "analyzed", "you (plural)": "analyzed", "they": "analyzed"
        }
    },
    "analizar": {
        "presente": {
            "yo": "analizo", "tú": "analizas", "él/ella": "analiza",
            "nosotros": "analizamos", "vosotros": "analizáis", "ellos/ellas": "analizan"
        },
        "pretérito": {
            "yo": "analicé", "tú": "analizaste", "él/ella": "analizó",
            "nosotros": "analizamos", "vosotros": "analizasteis", "ellos/ellas": "analizaron"
        }
    },
    "synthesize": {
        "present": {
            "I": "synthesize", "you": "synthesize", "he/she/it": "synthesizes",
            "we": "synthesize", "you (plural)": "synthesize", "they": "synthesize"
        },
        "past": {
            "I": "synthesized", "you": "synthesized", "he/she/it": "synthesized",
            "we": "synthesized", "you (plural)": "synthesized", "they": "synthesized"
        }
    },
    "sintetizar": {
        "presente": {
            "yo": "sintetizo", "tú": "sintetizas", "él/ella": "sintetiza",
            "nosotros": "sintetizamos", "vosotros": "sintetizáis", "ellos/ellas": "sintetizan"
        },
        "pretérito": {
            "yo": "sinteticé", "tú": "sintetizaste", "él/ella": "sintetizó",
            "nosotros": "sintetizamos", "vosotros": "sintetizasteis", "ellos/ellas": "sintetizaron"
        }
    },
    "hypothesize": {
        "present": {
            "I": "hypothesize", "you": "hypothesize", "he/she/it": "hypothesizes",
            "we": "hypothesize", "you (plural)": "hypothesize", "they": "hypothesize"
        },
        "past": {
            "I": "hypothesized", "you": "hypothesized", "he/she/it": "hypothesized",
            "we": "hypothesized", "you (plural)": "hypothesized", "they": "hypothesized"
        }
    },
    "hipotetizar": {
        "presente": {
            "yo": "hipotetizo", "tú": "hipotetizas", "él/ella": "hipotetiza",
            "nosotros": "hipotetizamos", "vosotros": "hipotetizáis", "ellos/ellas": "hipotetizan"
        },
        "pretérito": {
            "yo": "hipoteticé", "tú": "hipotetizaste", "él/ella": "hipotetizó",
            "nosotros": "hipotetizamos", "vosotros": "hipotetizasteis", "ellos/ellas": "hipotetizaron"
        }
    },
    # Añadir más verbos científicos aquí...
}

# Función que verifica si la conjugación es correcta
def verificar_conjugacion(verbo, tiempo, persona, numero, conjugacion):
    # Recuperar las conjugaciones correctas para el verbo y tiempo dado
    conjugacion_correcta = conjugaciones_verbos[verbo][tiempo].get(persona, "")
    
    # Verificar si la conjugación es correcta
    return conjugacion == conjugacion_correcta

# Función principal que interactúa con el usuario
def solicitar_conjugacion():
    # Solicitar el verbo
    verbo = input("Ingresa el verbo científico (en inglés o español): ").strip().lower()
    
    # Solicitar el tiempo (presente o pasado)
    tiempo = input("Ingresa el tiempo verbal ('present' para inglés o 'presente' para español, 'past' para inglés o 'pretérito' para español): ").strip().lower()
    
    # Solicitar persona y número
    persona = input("Ingresa la persona (yo/I, tú/you, él/ella/he/she/it, nosotros/we, vosotros/you (plural), ellos/ellas/they): ").strip().lower()
    
    # Solicitar la conjugación del usuario
    conjugacion = input(f"Escribe la conjugación de '{verbo}' en '{tiempo}' para '{persona}': ").strip().lower()
    
    # Verificar la conjugación
    if verificar_conjugacion(verbo, tiempo, persona, "singular" if persona in ["yo", "i", "tú", "you", "él/ella", "he/she/it"] else "plural", conjugacion):
        print("¡Correcto!")
    else:
        print("Incorrecto. Revisa la conjugación correcta.")

# Ejecutar la función principal
solicitar_conjugacion()
