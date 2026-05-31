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

# Función principal que interactúa con el usuario
def solicitar_conjugacion():
    # Solicitar tiempo y modo
    tiempo_modo = input("Ingresa el tiempo y modo (por ejemplo, 'presente_indicativo', 'pretérito_perfecto_simple', etc.): ").strip()
    
    # Solicitar persona
    persona = input("Ingresa la persona (yo, tú, él/ella, nosotros, vosotros, ellos/ellas): ").strip()
    
    # Solicitar número
    numero = input("Ingresa el número (singular o plural): ").strip()
    
    # Solicitar la conjugación del usuario
    conjugacion = input(f"Escribe la conjugación de '{persona}' en '{tiempo_modo}': ").strip()
    
    # Verificar la conjugación
    if verificar_conjugacion(tiempo_modo, persona, numero, conjugacion):
        print("¡Correcto!")
    else:
        print("Incorrecto. La conjugación correcta es:", conjugaciones[tiempo_modo][persona if numero == "singular" else persona.replace("yo", "nosotros").replace("tú", "vosotros").replace("él/ella", "ellos/ellas")])

# Ejecutar la función principal
solicitar_conjugacion()
