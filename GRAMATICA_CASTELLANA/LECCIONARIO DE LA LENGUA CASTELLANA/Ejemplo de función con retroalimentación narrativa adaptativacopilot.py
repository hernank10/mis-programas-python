def cargar_ejercicios_composicion_morfologica():
    return [
        {
            "pregunta": "¿Qué tipo de composición se observa en la palabra 'abrebotellas'?",
            "opciones": ["Composición perfecta", "Parasíntesis", "Derivación morfológica"],
            "respuesta": "Composición perfecta"
        },
        {
            "pregunta": "¿Qué tipo de formación es 'sacapuntas'?",
            "opciones": ["Composición perfecta", "Composición imperfecta", "Gentilicio"],
            "respuesta": "Composición perfecta"
        },
        {
            "pregunta": "¿Qué tipo de palabra es 'ferrocarril'?",
            "opciones": ["Composición culta", "Composición vulgar", "Derivación nominal"],
            "respuesta": "Composición culta"
        },
        {
            "pregunta": "¿La palabra 'rompecabezas' representa qué tipo de estructura?",
            "opciones": ["Composición perfecta", "Parasíntesis verbal", "Derivación adjetival"],
            "respuesta": "Composición perfecta"
        },
        {
            "pregunta": "¿Qué tipo de formación presenta 'agroindustria'?",
            "opciones": ["Composición culta", "Parasíntesis", "Compuesta con interfijo"],
            "respuesta": "Composición culta"
        },
        {
            "pregunta": "¿La palabra 'enloquecer' se forma por…?",
            "opciones": ["Parasíntesis (prefijo + base + sufijo)", "Composición culta", "Flexión verbal"],
            "respuesta": "Parasíntesis (prefijo + base + sufijo)"
        },
        {
            "pregunta": "¿Qué tipo de composición hay en 'bienvenido'?",
            "opciones": ["Parasíntesis verbal", "Composición imperfecta", "Composición perfecta"],
            "respuesta": "Parasíntesis verbal"
        },
        {
            "pregunta": "¿'telaraña' corresponde a qué tipo de formación?",
            "opciones": ["Composición imperfecta", "Composición culta", "Derivación sustantiva"],
            "respuesta": "Composición imperfecta"
        },
        {
            "pregunta": "¿'automóvil' es ejemplo de…?",
            "opciones": ["Composición culta", "Compuesta vulgar", "Derivación verbal"],
            "respuesta": "Composición culta"
        },
        {
            "pregunta": "¿La estructura de 'malhumor' muestra…?",
            "opciones": ["Composición imperfecta", "Parasíntesis", "Composición culta"],
            "respuesta": "Composición imperfecta"
        }
        # Puedes extender hasta 100 combinando tipo, estructura, función gramatical y contexto
    ]


import random

def practicar_composicion_morfologica():
    ejercicios = cargar_ejercicios_composicion_morfologica()
    ejercicio = random.choice(ejercicios)
    print("\n⚒️ Tipos de composición morfológica en castellano")
    print(f"❓ {ejercicio['pregunta']}")
    for i, op in enumerate(ejercicio["opciones"], 1):
        print(f"{i}. {op}")
    entrada = input("Tu respuesta (número): ")
    try:
        seleccion = ejercicio["opciones"][int(entrada)-1]
        if seleccion == ejercicio["respuesta"]:
            print("✅ ¡Correcto!")
        else:
            print(f"❌ Incorrecto. Respuesta esperada: {ejercicio['respuesta']}")
    except:
        print("❌ Entrada inválida.")
