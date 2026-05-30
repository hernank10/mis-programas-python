EJEMPLOS = {
    # Categoría 1: Comas explicativas (títulos/cargos)
    "Comas explicativas (títulos/cargos)": [
        {
            "base": "La conferencia será impartida por el experto en inteligencia artificial.",
            "inciso": "Dr. Luis Martínez",
            "puntuacion": "comas"
        },
        {
            "base": "La directora del colegio anunció nuevas becas estudiantiles.",
            "inciso": "licenciada Sofía Ramírez",
            "puntuacion": "comas"
        },
    ],
    
    # Categoría 2: Paréntesis (datos técnicos)
    "Paréntesis (datos técnicos)": [
        {
            "base": "El cohete Falcon 9 alcanzó la órbita terrestre.",
            "inciso": "desarrollado por SpaceX",
            "puntuacion": "paréntesis"
        },
    ],
    
    # Categoría 3: Rayas (énfasis)
    "Rayas (interrupciones o énfasis)": [
        {
            "base": "El proyecto aprobado ayer beneficiará a miles de familias.",
            "inciso": "tras meses de negociaciones",
            "puntuacion": "rayas"
        },
    ],
    
    # Categoría 4: Comas (contexto geográfico)
    "Comas explicativas (contexto geográfico o temporal)": [
        {
            "base": "El festival de Viña del Mar atrae a artistas internacionales.",
            "inciso": "evento anual en Chile",
            "puntuacion": "comas"
        },
    ],
    
    # Categoría 5: Paréntesis (siglas)
    "Paréntesis (abreviaturas o siglas)": [
        {
            "base": "La Organización del Tratado del Atlántico Norte promueve la cooperación militar.",
            "inciso": "OTAN",
            "puntuacion": "paréntesis"
        },
    ],
    
    # Categoría 6: Comas (sinónimos)
    "Comas explicativas (sinónimos o aclaraciones)": [
        {
            "base": "El kimchi es un alimento fermentado tradicional.",
            "inciso": "preparado con repollo y especias",
            "puntuacion": "comas"
        },
    ],
    
    # Categoría 7: Ejemplo mixto (comas y rayas)
    "Ejemplos mixtos (combinan signos)": [
        {
            "base": "El puente Golden Gate —símbolo de San Francisco— fue inaugurado en 1937.",
            "inciso": "diseñado por Joseph Strauss",
            "puntuacion": "paréntesis"  # El usuario debe añadir este inciso con paréntesis
        },
    ],
    
    # Categoría 8: Uso excesivo (para evitar)
    "Uso excesivo (para evitar)": [
        {
            "base": "El café colombiano es reconocido mundialmente.",
            "inciso": "cultivado en zonas montañosas, procesado artesanalmente, exportado a 50 países",
            "puntuacion": "comas"  # Incorrecto: tres incisos
        },
    ]
}

EJEMPLOS = {
    "Comas explicativas (títulos/cargos)": [
        {
            "base": "El rector de la UIS tendrá a su cargo el discurso inaugural.",
            "inciso": "doctor Hernán Darío Díaz",
            "puntuacion": "comas"
        },
        # ... más ejemplos
    ],
    "Paréntesis (datos técnicos)": [
        {
            "base": "La empresa Biotech desarrolló una vacuna contra la malaria.",
            "inciso": "fundada en 2010",
            "puntuacion": "paréntesis"
        },
        # ... más ejemplos
    ],
    # ... otras categorías
}
