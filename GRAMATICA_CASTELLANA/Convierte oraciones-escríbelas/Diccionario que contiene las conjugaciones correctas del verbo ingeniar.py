# Diccionario que contiene las conjugaciones correctas del verbo "ingeniar"
conjugaciones = {
    "presente_indicativo": {
        "yo": "ingenio", "tú": "ingenias", "él/ella": "ingenia",
        "nosotros": "ingeniamos", "vosotros": "ingeniáis", "ellos/ellas": "ingenian"
    },
    "pretérito_perfecto_simple": {
        "yo": "ingenié", "tú": "ingeniaste", "él/ella": "ingenió",
        "nosotros": "ingeniamos", "vosotros": "ingeniasteis", "ellos/ellas": "ingeniaron"
    },
    "futuro_indicativo": {
        "yo": "ingeniaré", "tú": "ingeniarás", "él/ella": "ingeniará",
        "nosotros": "ingeniaremos", "vosotros": "ingeniaréis", "ellos/ellas": "ingeniarán"
    },
    "presente_subjuntivo": {
        "yo": "ingenie", "tú": "ingenies", "él/ella": "ingenie",
        "nosotros": "ingeniemos", "vosotros": "ingeniéis", "ellos/ellas": "ingenien"
    },
    "imperfecto_subjuntivo": {
        "yo": ["ingeniara", "ingeniase"], "tú": ["ingeniaras", "ingeniases"], 
        "él/ella": ["ingeniara", "ingeniase"], "nosotros": ["ingeniáramos", "ingeniásemos"],
        "vosotros": ["ingeniarais", "ingeniaseis"], "ellos/ellas": ["ingeniaran", "ingeniasen"]
    }
}

# Función que verifica si la conjugación es correcta
def verificar_conjugacion(tiempo_modo, persona, numero, conjugacion):
    # Combinar persona y número
    clave_persona = persona if numero == "singular" else persona.replace("yo", "nosotros").replace("tú", "vosotros").replace("él/ella", "ellos/ellas")
    
    # Recuperar las conjugaciones correctas para el tiempo y modo dado
    conjugacion_correcta = conjugaciones[tiempo_modo].get(clave_persona, "")
    
    # Verificar si la conjugación es correcta
    if isinstance(conjugacion_correcta, list):
        return conjugacion in conjugacion_correcta
    else:
        return conjugacion == conjugacion_correcta

# Ejemplos de uso
print(verificar_conjugacion("presente_indicativo", "yo", "singular", "ingenio"))  # True
print(verificar_conjugacion("imperfecto_subjuntivo", "tú", "singular", "ingeniaras"))  # True
print(verificar_conjugacion("futuro_indicativo", "ellos/ellas", "plural", "ingeniarán"))  # True
print(verificar_conjugacion("presente_indicativo", "yo", "singular", "ingenias"))  # False
