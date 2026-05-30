import random

# Diccionario con las lecciones de gramática en inglés.
ENGLISH_LESSONS = {
    "Lección 1: Pronombres personales": {
        "teoría": "Los pronombres personales se usan para reemplazar a los sustantivos (yo, tú, él, etc.).",
        "ejemplo": "She is a doctor. (Ella es una doctora).",
        "pregunta": "¿Qué pronombre personal se usa para hablar de una cosa?",
        "opciones": ["I", "He", "It"],
        "respuesta_correcta": "It"
    },
    "Lección 2: Presente simple (afirmativo)": {
        "teoría": "Se usa para acciones habituales, hechos o rutinas. Se añade 's' o 'es' al verbo en tercera persona del singular (he, she, it).",
        "ejemplo": "He plays football. (Él juega fútbol).",
        "pregunta": "La forma correcta del verbo 'drink' para 'she' es:",
        "opciones": ["drink", "drinks", "drinking"],
        "respuesta_correcta": "drinks"
    },
    "Lección 3: 'to be' (afirmativo)": {
        "teoría": "El verbo 'to be' significa 'ser' o 'estar'. Se conjuga de forma irregular: am, is, are.",
        "ejemplo": "I am happy. She is a student. We are friends.",
        "pregunta": "La forma correcta de 'to be' para 'they' es:",
        "opciones": ["am", "is", "are"],
        "respuesta_correcta": "are"
    },
    "Lección 4: Adjetivos posesivos": {
        "teoría": "Indican posesión o pertenencia. Se colocan antes del sustantivo: my, your, his, her, its, our, their.",
        "ejemplo": "This is my book. (Este es mi libro).",
        "pregunta": "¿Cuál es el adjetivo posesivo para 'we'?",
        "opciones": ["our", "they", "its"],
        "respuesta_correcta": "our"
    },
    "Lección 5: Presente continuo": {
        "teoría": "Se usa para acciones que están ocurriendo en el momento. Se forma con 'to be' + el verbo principal con '-ing'.",
        "ejemplo": "I am studying. (Estoy estudiando).",
        "pregunta": "La forma correcta para 'she' de 'listen' es:",
        "opciones": ["she listening", "she is listening", "she listens"],
        "respuesta_correcta": "she is listening"
    },
    "Lección 6: Sustantivos (singular y plural)": {
        "teoría": "La mayoría de los sustantivos forman el plural añadiendo 's'. Algunos tienen plurales irregulares (man -> men).",
        "ejemplo": "one dog, two dogs. one man, two men.",
        "pregunta": "El plural de 'child' es:",
        "opciones": ["childs", "children", "childen"],
        "respuesta_correcta": "children"
    },
    "Lección 7: Uso de 'do' y 'does'": {
        "teoría": "'Do' y 'does' se usan como auxiliares en oraciones interrogativas y negativas en presente simple.",
        "ejemplo": "Do you like coffee? She does not like coffee.",
        "pregunta": "La forma correcta para 'he' de 'like' es:",
        "opciones": ["Does he like...?", "Do he like...?", "Does he likes...?"],
        "respuesta_correcta": "Does he like...?"
    },
    "Lección 8: Pasado simple": {
        "teoría": "Se usa para acciones que ocurrieron en el pasado y están terminadas. Se añade '-ed' a los verbos regulares. Los verbos irregulares tienen formas especiales.",
        "ejemplo": "I walked yesterday. She ate a pizza.",
        "pregunta": "La forma en pasado de 'go' es:",
        "opciones": ["goed", "went", "gone"],
        "respuesta_correcta": "went"
    },
    "Lección 9: Futuro simple ('will')": {
        "teoría": "Se usa para predecir el futuro o para decisiones espontáneas. Se forma con 'will' + el verbo en su forma base.",
        "ejemplo": "I will go to the party. (Iré a la fiesta).",
        "pregunta": "La forma negativa de 'will' es:",
        "opciones": ["will not", "won't", "ambas son correctas"],
        "respuesta_correcta": "ambas son correctas"
    },
    "Lección 10: Adverbios de frecuencia": {
        "teoría": "Indican con qué frecuencia se realiza una acción: always, often, sometimes, never. Se colocan antes del verbo principal o después del verbo 'to be'.",
        "ejemplo": "I always eat breakfast. He is often late.",
        "pregunta": "En la frase 'She never plays football', 'never' es un...",
        "opciones": ["adjetivo", "verbo", "adverbio"],
        "respuesta_correcta": "adverbio"
    },
    "Lección 11: Preposiciones de tiempo": {
        "teoría": "Se usan para indicar el momento en que ocurre algo: 'in' (meses, años, estaciones), 'on' (días, fechas), 'at' (horas, momentos específicos).",
        "ejemplo": "in July, on Monday, at 3 p.m.",
        "pregunta": "La preposición correcta para 'the morning' es:",
        "opciones": ["at", "on", "in"],
        "respuesta_correcta": "in"
    },
    "Lección 12: Preposiciones de lugar": {
        "teoría": "Se usan para indicar la ubicación de algo: 'in' (dentro), 'on' (sobre), 'at' (en un punto específico).",
        "ejemplo": "in the box, on the table, at the park.",
        "pregunta": "La preposición correcta para 'the chair' es:",
        "opciones": ["at", "on", "in"],
        "respuesta_correcta": "on"
    },
    "Lección 13: La 's' en tercera persona": {
        "teoría": "En presente simple, se añade 's' a los verbos para he, she, it. Si el verbo termina en -sh, -ch, -x, -ss, -z, -o, se añade '-es'.",
        "ejemplo": "he watches TV, she goes to school, it washes clothes",
        "pregunta": "La forma correcta del verbo 'teach' para 'she' es:",
        "opciones": ["teach", "teaches", "teachies"],
        "respuesta_correcta": "teaches"
    },
    "Lección 14: Verbos modales ('can', 'could')": {
        "teoría": "'Can' (poder) expresa habilidad o posibilidad. 'Could' es el pasado de 'can' y se usa para expresar habilidad en el pasado o peticiones educadas.",
        "ejemplo": "I can swim. (Puedo nadar). He could run fast when he was young.",
        "pregunta": "La forma correcta para decir 'Él pudo hablar' es:",
        "opciones": ["He can spoke", "He could speak", "He could spoke"],
        "respuesta_correcta": "He could speak"
    },
    "Lección 15: Verbos modales ('should', 'must')": {
        "teoría": "'Should' (debería) se usa para dar un consejo. 'Must' (debe) se usa para expresar una obligación o una deducción lógica.",
        "ejemplo": "You should study more. You must be tired after that long trip.",
        "pregunta": "La forma correcta para decir 'Tú debes ir al doctor' es:",
        "opciones": ["You should go to the doctor", "You must go to the doctor", "You can go to the doctor"],
        "respuesta_correcta": "You must go to the doctor"
    },
    "Lección 16: 'a' y 'an' (artículos indefinidos)": {
        "teoría": "Se usa 'a' antes de sustantivos que comienzan con sonido de consonante. Se usa 'an' antes de sustantivos que comienzan con sonido de vocal.",
        "ejemplo": "a cat, an apple, an hour (la 'h' no suena).",
        "pregunta": "El artículo correcto para 'university' es:",
        "opciones": ["a", "an"],
        "respuesta_correcta": "a"
    },
    "Lección 17: 'the' (artículo definido)": {
        "teoría": "Se usa 'the' para referirse a algo específico o que ya ha sido mencionado.",
        "ejemplo": "The sun is hot. I have a dog. The dog is brown.",
        "pregunta": "El artículo correcto para 'Mount Everest' es:",
        "opciones": ["a", "the", "ninguno"],
        "respuesta_correcta": "ninguno"
    },
    "Lección 18: Adverbios de modo": {
        "teoría": "Expresan cómo se realiza una acción. Muchos terminan en '-ly' (ej. quickly, carefully).",
        "ejemplo": "He drives slowly. (Él conduce lentamente).",
        "pregunta": "La forma de 'bad' como adverbio es:",
        "opciones": ["badly", "badly", "badly"],
        "respuesta_correcta": "badly"
    },
    "Lección 19: El comparativo": {
        "teoría": "Se usa para comparar dos cosas. Para adjetivos cortos, se añade '-er' y 'than'. Para adjetivos largos, se usa 'more' y 'than'.",
        "ejemplo": "He is taller than me. This car is more expensive than that one.",
        "pregunta": "La forma comparativa de 'fast' es:",
        "opciones": ["faster", "more fast", "fastest"],
        "respuesta_correcta": "faster"
    },
    "Lección 20: El superlativo": {
        "teoría": "Se usa para comparar una cosa con un grupo. Para adjetivos cortos, se añade '-est' y 'the'. Para adjetivos largos, se usa 'the most'.",
        "ejemplo": "He is the tallest in the class. This is the most beautiful painting.",
        "pregunta": "La forma superlativa de 'small' es:",
        "opciones": ["smallest", "more small", "most small"],
        "respuesta_correcta": "smallest"
    }
}

# Diccionario con las lecciones de gramática en castellano.
SPANISH_LESSONS = {
    "Lección 101: Acentuación de palabras agudas": {
        "teoría": "Las palabras agudas son las que tienen la sílaba tónica en el último lugar. Se acentúan cuando terminan en vocal, 'n' o 's'.",
        "ejemplo": "camión, mamá, café",
        "pregunta": "¿Cuál de las siguientes palabras es aguda y lleva tilde?",
        "opciones": ["papel", "corazón", "comer"],
        "respuesta_correcta": "corazón"
    },
    "Lección 102: Acentuación de palabras llanas": {
        "teoría": "Las palabras llanas o graves tienen la sílaba tónica en el penúltimo lugar. Se acentúan cuando NO terminan en vocal, 'n' o 's'.",
        "ejemplo": "árbol, lápiz, cóndor",
        "pregunta": "¿Cuál de las siguientes palabras es llana y no lleva tilde?",
        "opciones": ["fácil", "coche", "difícil"],
        "respuesta_correcta": "coche"
    },
    "Lección 103: Acentuación de palabras esdrújulas": {
        "teoría": "Las palabras esdrújulas tienen la sílaba tónica en el antepenúltimo lugar. Todas las palabras esdrújulas siempre llevan tilde.",
        "ejemplo": "médico, teléfono, brújula",
        "pregunta": "¿Cuál de las siguientes palabras es esdrújula?",
        "opciones": ["canción", "rápido", "mesa"],
        "respuesta_correcta": "rápido"
    },
    "Lección 104: El punto y la coma": {
        "teoría": "El punto (.) se usa para indicar el final de una oración. La coma (,) se usa para indicar una pausa breve en la oración.",
        "ejemplo": "El coche es azul. La casa, grande.",
        "pregunta": "En la frase 'El niño, que es rubio, juega', ¿qué separa la coma?",
        "opciones": ["una enumeración", "un vocativo", "una aclaración"],
        "respuesta_correcta": "una aclaración"
    },
    "Lección 105: El sujeto y el predicado": {
        "teoría": "El sujeto es quien realiza la acción. El predicado es lo que se dice del sujeto.",
        "ejemplo": "El perro (sujeto) come (predicado).",
        "pregunta": "En la frase 'La niña canta una canción', ¿quién es el sujeto?",
        "opciones": ["La niña", "canta", "una canción"],
        "respuesta_correcta": "La niña"
    },
    "Lección 106: El sustantivo": {
        "teoría": "El sustantivo es una palabra que nombra a personas, animales, cosas o lugares.",
        "ejemplo": "perro, mesa, Juan, Madrid",
        "pregunta": "¿Cuál es el sustantivo en la frase 'Mi casa es grande'?",
        "opciones": ["Mi", "casa", "grande"],
        "respuesta_correcta": "casa"
    },
    "Lección 107: El adjetivo": {
        "teoría": "El adjetivo es una palabra que describe o califica al sustantivo. Siempre concuerda en género y número con el sustantivo.",
        "ejemplo": "coche rojo, flores bonitas",
        "pregunta": "En la frase 'El libro viejo', ¿cuál es el adjetivo?",
        "opciones": ["El", "libro", "viejo"],
        "respuesta_correcta": "viejo"
    },
    "Lección 108: El verbo": {
        "teoría": "El verbo es la palabra que expresa una acción, un estado o un proceso.",
        "ejemplo": "correr, dormir, ser",
        "pregunta": "¿Cuál es el verbo en la frase 'El niño juega en el parque'?",
        "opciones": ["niño", "juega", "parque"],
        "respuesta_correcta": "juega"
    },
    "Lección 109: El artículo": {
        "teoría": "El artículo es la palabra que acompaña al sustantivo para especificarlo o no. Pueden ser 'el', 'la', 'los', 'las' (determinados) o 'un', 'una', 'unos', 'unas' (indeterminados).",
        "ejemplo": "la casa, un libro",
        "pregunta": "¿Qué tipo de artículo es 'los'?",
        "opciones": ["determinado", "indeterminado", "posesivo"],
        "respuesta_correcta": "determinado"
    },
    "Lección 110: El diptongo": {
        "teoría": "Es la unión de dos vocales en una misma sílaba (una vocal abierta y una cerrada, o dos vocales cerradas).",
        "ejemplo": "cielo, pausa, ciudad",
        "pregunta": "La palabra 'cuidado' tiene:",
        "opciones": ["hiato", "diptongo", "triptongo"],
        "respuesta_correcta": "diptongo"
    },
    "Lección 111: El hiato": {
        "teoría": "Es la separación de dos vocales en sílabas distintas (dos vocales abiertas, o una vocal abierta y una cerrada tónica).",
        "ejemplo": "ma-e-stro, ca-í-da, po-e-ma",
        "pregunta": "La palabra 'país' tiene:",
        "opciones": ["hiato", "diptongo", "triptongo"],
        "respuesta_correcta": "hiato"
    },
    "Lección 112: El triptongo": {
        "teoría": "Es la unión de tres vocales en una misma sílaba (cerrada + abierta + cerrada).",
        "ejemplo": "miau, Uruguay, buey",
        "pregunta": "La palabra 'buey' tiene:",
        "opciones": ["hiato", "diptongo", "triptongo"],
        "respuesta_correcta": "triptongo"
    },
    "Lección 113: Pronombres personales": {
        "teoría": "Son palabras que reemplazan a los sustantivos y se refieren a las personas que intervienen en la comunicación (yo, tú, él, ella, nosotros, nosotras, ustedes, ellos, ellas).",
        "ejemplo": "Ella es mi hermana.",
        "pregunta": "¿Qué pronombre usarías para referirte a 'Pedro y María'?",
        "opciones": ["tú", "nosotros", "ellos"],
        "respuesta_correcta": "ellos"
    },
    "Lección 114: Verbos regulares": {
        "teoría": "Son los que mantienen la misma raíz en todas sus conjugaciones y siguen las terminaciones del verbo modelo.",
        "ejemplo": "Cantar: yo canto, tú cantas, él canta.",
        "pregunta": "¿Cuál de los siguientes verbos es regular?",
        "opciones": ["ser", "ir", "hablar"],
        "respuesta_correcta": "hablar"
    },
    "Lección 115: Verbos irregulares": {
        "teoría": "Son los que no siguen las reglas de conjugación, cambiando la raíz o la terminación.",
        "ejemplo": "Ser: yo soy, tú eres, él es.",
        "pregunta": "¿Cuál de los siguientes verbos es irregular?",
        "opciones": ["correr", "comer", "tener"],
        "respuesta_correcta": "tener"
    },
    "Lección 116: El pretérito perfecto simple": {
        "teoría": "Se usa para acciones que ya ocurrieron y terminaron en el pasado.",
        "ejemplo": "Ayer comí una pizza.",
        "pregunta": "La forma correcta del verbo 'viajar' en pretérito perfecto simple para 'yo' es:",
        "opciones": ["viajo", "viajé", "viajaba"],
        "respuesta_correcta": "viajé"
    },
    "Lección 117: El gerundio": {
        "teoría": "Es una forma verbal que indica una acción en progreso. Termina en '-ando' o '-iendo'.",
        "ejemplo": "Estoy comiendo.",
        "pregunta": "La forma correcta para 'ellos' de 'estudiar' es:",
        "opciones": ["estudian", "estudiando", "estudiaban"],
        "respuesta_correcta": "estudiando"
    },
    "Lección 118: El infinitivo": {
        "teoría": "Es la forma no conjugada del verbo. Siempre termina en '-ar', '-er' o '-ir'.",
        "ejemplo": "cantar, comer, vivir",
        "pregunta": "¿Cuál es el infinitivo del verbo 'leyó'?",
        "opciones": ["leer", "leía", "leído"],
        "respuesta_correcta": "leer"
    },
    "Lección 119: Palabras agudas sin tilde": {
        "teoría": "No llevan tilde si no terminan en vocal, 'n' o 's'.",
        "ejemplo": "papel, reloj, amor",
        "pregunta": "¿Cuál de las siguientes palabras es aguda y no lleva tilde?",
        "opciones": ["sofá", "calor", "camión"],
        "respuesta_correcta": "calor"
    },
    "Lección 120: Palabras llanas con tilde": {
        "teoría": "Llevan tilde si no terminan en vocal, 'n' o 's'.",
        "ejemplo": "lápiz, álbum, fútbol",
        "pregunta": "¿Cuál de las siguientes palabras es llana y lleva tilde?",
        "opciones": ["canto", "cantar", "cántaro"],
        "respuesta_correcta": "cántaro"
    }
}

# Se combinan todas las lecciones en un solo diccionario.
ALL_LESSONS = {}
ALL_LESSONS.update(ENGLISH_LESSONS)
ALL_LESSONS.update(SPANISH_LESSONS)

# 100 lecciones adicionales de lengua castellana.
SPANISH_LESSONS.update({
    "Lección 201: Acentuación de palabras agudas": {
        "teoría": """Las palabras agudas son aquellas cuya sílaba tónica es la última.
Se acentúan solo si terminan en vocal, 'n' o 's'.""",
        "ejemplo": "Café, camión, compás.",
        "pregunta": "¿Qué palabra aguda está correctamente acentuada?",
        "opciones": ["Reloj", "Pared", "Ademas"],
        "respuesta_correcta": "Ademas"
    },
    "Lección 202: Acentuación de palabras llanas o graves": {
        "teoría": """Las palabras llanas o graves tienen la sílaba tónica en la penúltima sílaba.
Se acentúan si NO terminan en vocal, 'n' o 's'.""",
        "ejemplo": "Árbol, lápiz, césped.",
        "pregunta": "¿Qué palabra llana está correctamente acentuada?",
        "opciones": ["Silla", "Casa", "Difícil"],
        "respuesta_correcta": "Difícil"
    },
    "Lección 203: Acentuación de palabras esdrújulas y sobresdrújulas": {
        "teoría": """Las palabras esdrújulas tienen la sílaba tónica en la antepenúltima sílaba.
Las sobresdrújulas tienen la sílaba tónica antes de la antepenúltima.
Todas las palabras esdrújulas y sobresdrújulas siempre llevan tilde.""",
        "ejemplo": "Teléfono, brújula, pídete.",
        "pregunta": "¿Qué palabra esdrújula o sobresdrújula NO lleva tilde?",
        "opciones": ["Murciélago", "Económico", "Fácilmente"],
        "respuesta_correcta": "Murciélago"
    },
    "Lección 204: Uso de la coma": {
        "teoría": """La coma se usa para separar los elementos de una enumeración, aislar incisos y aclaraciones, y separar el vocativo del resto de la oración.""",
        "ejemplo": "Compré pan, leche y huevos. Ana, ven aquí.",
        "pregunta": "¿En qué caso es incorrecto usar la coma?",
        "opciones": ["Para separar el sujeto del verbo", "Para separar los elementos de una enumeración", "Para aislar una aclaración"],
        "respuesta_correcta": "Para separar el sujeto del verbo"
    },
    "Lección 205: Uso del punto y coma": {
        "teoría": """El punto y coma se usa para indicar una pausa mayor que la de la coma y menor que la del punto.
Sirve para separar oraciones con una relación estrecha, o los elementos de una enumeración compleja.""",
        "ejemplo": "La camisa era blanca; el pantalón, negro.",
        "pregunta": "El punto y coma es útil para:",
        "opciones": ["Terminar una oración.", "Separar dos oraciones muy relacionadas.", "Introducir una cita."],
        "respuesta_correcta": "Separar dos oraciones muy relacionadas."
    },
    "Lección 206: Los dos puntos": {
        "teoría": """Los dos puntos se usan para introducir una enumeración, una cita textual, o para conectar oraciones que tienen una relación de causa-efecto o resumen.""",
        "ejemplo": "El médico dijo: 'Descanse.'",
        "pregunta": "¿Cuándo se usan los dos puntos?",
        "opciones": ["Para separar la conjunción del verbo.", "Para iniciar una pregunta.", "Para introducir una enumeración."],
        "respuesta_correcta": "Para introducir una enumeración."
    },
    "Lección 207: Uso de la B y la V (reglas básicas)": {
        "teoría": """Se usa 'b' en las terminaciones -aba, -abas, -ábamos, -abais, -aban.
Se usa 'v' en las palabras que contienen el prefijo 'vice-' o 'villa-'.""",
        "ejemplo": "Cantaba, Vicepresidente, Villavicencio.",
        "pregunta": "La palabra correcta es:",
        "opciones": ["Bivir", "Vivir", "Vivir"],
        "respuesta_correcta": "Vivir"
    },
    "Lección 208: Uso de la C, S y Z": {
        "teoría": """La 'c' se usa en el sonido suave antes de 'e' e 'i'.
La 'z' se usa antes de 'a', 'o', 'u' y al final de la palabra.
La 's' se usa en la mayoría de los casos para el sonido de 's'.""",
        "ejemplo": "Cielo, cebra, zapato, voz.",
        "pregunta": "La palabra 'cesta' se escribe con:",
        "opciones": ["C", "S", "Z"],
        "respuesta_correcta": "S"
    },
    "Lección 209: Uso de la G y la J": {
        "teoría": """La 'g' tiene un sonido suave antes de 'a', 'o' y 'u'.
La 'g' tiene un sonido fuerte antes de 'e' e 'i', al igual que la 'j'.""",
        "ejemplo": "Gato, gente, jinete, gira.",
        "pregunta": "La palabra 'girasol' se escribe con:",
        "opciones": ["J", "G"],
        "respuesta_correcta": "G"
    },
    "Lección 210: El Hiato": {
        "teoría": """El hiato es la secuencia de dos vocales que se pronuncian en sílabas separadas.
Las vocales abiertas ('a', 'e', 'o') forman hiatos entre sí.
Una vocal abierta y una vocal cerrada tónica ('í', 'ú') también forman hiato.""",
        "ejemplo": "Pa-ís, ca-o-ba, Ma-rí-a.",
        "pregunta": "La palabra 'poesía' tiene...",
        "opciones": ["Un diptongo.", "Un hiato.", "Un triptongo."],
        "respuesta_correcta": "Un hiato."
    },
    "Lección 211: El Diptongo": {
        "teoría": """El diptongo es la unión de dos vocales en la misma sílaba.
Puede ser una vocal abierta con una cerrada átona, o dos vocales cerradas.""",
        "ejemplo": "Pausa, cuento, ciudad.",
        "pregunta": "La palabra 'ruido' tiene...",
        "opciones": ["Un diptongo.", "Un hiato.", "Un triptongo."],
        "respuesta_correcta": "Un diptongo."
    },
    "Lección 212: El Triptongo": {
        "teoría": """El triptongo es la unión de tres vocales en una misma sílaba: una vocal cerrada, una abierta y otra cerrada.""",
        "ejemplo": "Uruguay, buey, miau.",
        "pregunta": "La palabra 'confiáis' tiene...",
        "opciones": ["Un hiato.", "Un diptongo.", "Un triptongo."],
        "respuesta_correcta": "Un triptongo."
    },
    "Lección 213: Uso de la H (intercalada)": {
        "teoría": """Se usa 'h' intercalada cuando la palabra proviene de una que la llevaba o para separar vocales de distinta sílaba.""",
        "ejemplo": "Prohibir, cohete, alcohol.",
        "pregunta": "La palabra 'a_ora' se escribe con 'h' para:",
        "opciones": ["Separar vocales.", "Indicar una pausa.", "No tiene reglas."],
        "respuesta_correcta": "Separar vocales."
    },
    "Lección 214: El Sujeto y el Predicado": {
        "teoría": """El sujeto es la persona, animal o cosa que realiza la acción del verbo.
El predicado es lo que se dice del sujeto, e incluye el verbo.""",
        "ejemplo": "Juan (sujeto) come una manzana (predicado).",
        "pregunta": "En 'El niño juega en el parque', el predicado es:",
        "opciones": ["El niño", "juega en el parque", "parque"],
        "respuesta_correcta": "juega en el parque"
    },
    "Lección 215: La Concordancia (Género y Número)": {
        "teoría": """Un adjetivo y un sustantivo deben concordar en género (masculino/femenino) y número (singular/plural).""",
        "ejemplo": "Las casas bonitas. El libro rojo.",
        "pregunta": "La forma correcta es:",
        "opciones": ["Los perros grande.", "Las perro grandes.", "Los perros grandes."],
        "respuesta_correcta": "Los perros grandes."
    },
    "Lección 216: Los Pronombres Personales": {
        "teoría": """Son las palabras que sustituyen a los sustantivos para evitar la repetición.
Ejemplos: yo, tú, él, ella, nosotros, ustedes, ellos, ellas.""",
        "ejemplo": "Pedro y Ana van al cine. Ellos van al cine.",
        "pregunta": "En 'Ellos juegan al fútbol', 'ellos' es un...",
        "opciones": ["Adjetivo.", "Pronombre personal.", "Verbo."],
        "respuesta_correcta": "Pronombre personal."
    },
    "Lección 217: La Tilde Diacrítica": {
        "teoría": """Es la tilde que sirve para diferenciar palabras que se escriben igual, pero tienen diferente significado y función gramatical.""",
        "ejemplo": "Tú (pronombre personal) vs. Tu (adjetivo posesivo).",
        "pregunta": "La oración correcta es:",
        "opciones": ["Tu sabes la respuesta.", "Tú sabes la respuesta.", "Tu, sabes la respuesta."],
        "respuesta_correcta": "Tú sabes la respuesta."
    },
    "Lección 218: Verbos Regulares": {
        "teoría": """Los verbos regulares mantienen la misma raíz en todas sus conjugaciones y siguen el mismo patrón de terminación que su modelo de conjugación (-ar, -er, -ir).""",
        "ejemplo": "Cantar: yo canto, tú cantas, él canta.",
        "pregunta": "El verbo 'comer' es...",
        "opciones": ["Irregular.", "Regular.", "Defectivo."],
        "respuesta_correcta": "Regular."
    },
    "Lección 219: Verbos Irregulares": {
        "teoría": """Los verbos irregulares no mantienen la misma raíz o no siguen el patrón de terminación de su conjugación al ser conjugados.""",
        "ejemplo": "Ser: yo soy, tú eres, él es.",
        "pregunta": "El verbo 'ir' es...",
        "opciones": ["Regular.", "Irregular.", "Defectivo."],
        "respuesta_correcta": "Irregular."
    },
    "Lección 220: El Gerundio": {
        "teoría": """El gerundio es una forma verbal que expresa una acción en progreso. Termina en -ando (verbos en -ar) o -iendo (verbos en -er/-ir).""",
        "ejemplo": "Estoy estudiando. Él está corriendo.",
        "pregunta": "La forma correcta para 'Ellos están...' es:",
        "opciones": ["Comieron", "Comiendo", "Comen"],
        "respuesta_correcta": "Comiendo"
    },
    "Lección 221: El Participio": {
        "teoría": """El participio es una forma verbal que indica una acción terminada. Termina en -ado (verbos en -ar) o -ido (verbos en -er/-ir).""",
        "ejemplo": "He cantado. Han comido.",
        "pregunta": "El participio del verbo 'dormir' es:",
        "opciones": ["Dormido", "Durmiendo", "Duermo"],
        "respuesta_correcta": "Dormido"
    },
    "Lección 222: Oraciones Simples y Compuestas": {
        "teoría": """Una oración simple tiene un solo verbo.
Una oración compuesta tiene dos o más verbos, lo que significa que tiene dos o más oraciones (o proposiciones) en ella.""",
        "ejemplo": "La niña juega (simple). El niño juega y la niña canta (compuesta).",
        "pregunta": "La oración 'Caminé toda la noche y no me cansé' es:",
        "opciones": ["Simple", "Compuesta"],
        "respuesta_correcta": "Compuesta"
    },
    "Lección 223: El Adjetivo y sus Grados": {
        "teoría": """El adjetivo expresa cualidades del sustantivo. Tiene tres grados: positivo (grande), comparativo (más grande que) y superlativo (el más grande).""",
        "ejemplo": "Juan es alto. María es más alta que Juan. Pedro es el más alto.",
        "pregunta": "En 'El libro es interesantísimo', el adjetivo está en grado...",
        "opciones": ["Positivo.", "Comparativo.", "Superlativo."],
        "respuesta_correcta": "Superlativo."
    },
    "Lección 224: El Adverbio": {
        "teoría": """El adverbio es una palabra que modifica a un verbo, un adjetivo o a otro adverbio.
Pueden ser de modo (rápidamente), lugar (aquí), tiempo (hoy), etc.""",
        "ejemplo": "Él corre rápidamente. El libro está aquí.",
        "pregunta": "La palabra 'lentamente' es un...",
        "opciones": ["Adjetivo.", "Verbo.", "Adverbio."],
        "respuesta_correcta": "Adverbio."
    },
    "Lección 225: Uso de los signos de exclamación": {
        "teoría": """Se usan para expresar emociones intensas, sorpresa, admiración, ruego o una orden.
Siempre se usan tanto al inicio (¡) como al final de la frase (!).""",
        "ejemplo": "¡Qué golazo! ¡Por favor, ayúdame!",
        "pregunta": "¿Cuándo se usa el signo de exclamación?",
        "opciones": ["Para hacer una pregunta.", "Para expresar una emoción fuerte.", "Para terminar una oración declarativa."],
        "respuesta_correcta": "Para expresar una emoción fuerte."
    },
    "Lección 226: Los Pronombres Posesivos": {
        "teoría": """Indican a quién pertenece algo. Sustituyen a la combinación de adjetivo posesivo + sustantivo.
Ejemplos: mío, tuyo, suyo, nuestro, vuestro, suyo.""",
        "ejemplo": "Mi casa es grande. La mía es grande.",
        "pregunta": "En la frase 'El libro es tuyo', 'tuyo' es un...",
        "opciones": ["Adjetivo posesivo.", "Pronombre posesivo.", "Pronombre personal."],
        "respuesta_correcta": "Pronombre posesivo."
    },
    "Lección 227: Los Pronombres Demostrativos": {
        "teoría": """Indican la distancia de un objeto o ser con respecto al hablante.
Ejemplos: este, ese, aquel, esta, esa, aquella.""",
        "ejemplo": "Este coche es rápido. Ese coche es lento.",
        "pregunta": "En la frase 'Aquel me gusta más', 'aquel' es un...",
        "opciones": ["Adjetivo demostrativo.", "Pronombre demostrativo.", "Verbo."],
        "respuesta_correcta": "Pronombre demostrativo."
    },
    "Lección 228: Uso de la G y la J (continuación)": {
        "teoría": """Se usa la 'j' en las palabras que terminan en -aje y -eje.
Ejemplos: garaje, masaje, coraje.""",
        "ejemplo": "El viaje fue largo.",
        "pregunta": "La terminación -aje se escribe con:",
        "opciones": ["G", "J"],
        "respuesta_correcta": "J"
    },
    "Lección 229: El Prefijo 'Des-'": {
        "teoría": """El prefijo 'des-' indica negación, inversión o privación.
Ejemplos: desordenar, desarmar, deshacer.""",
        "ejemplo": "La palabra 'deshacer' significa lo opuesto a 'hacer'.",
        "pregunta": "La palabra 'despeinar' significa lo opuesto a...",
        "opciones": ["Peinar", "Apretar", "Encontrar"],
        "respuesta_correcta": "Peinar"
    },
    "Lección 230: Palabras homófonas 'ahí', 'hay' y 'ay'": {
        "teoría": """'Ahí' es un adverbio de lugar (allí, en ese lugar).
'Hay' es una forma del verbo haber (existencia).
'Ay' es una interjección (expresa dolor, sorpresa).""",
        "ejemplo": "Ahí está el libro. Hay mucho ruido. ¡Ay, qué dolor!",
        "pregunta": "La frase correcta es:",
        "opciones": ["Hay un perro ahí.", "Ahi un perro hay.", "Ay un perro ahi."],
        "respuesta_correcta": "Hay un perro ahí."
    },
    "Lección 231: La Voz Pasiva": {
        "teoría": """La voz pasiva se usa para enfocar la atención en el objeto de la acción, en vez de en quien la realiza.
Se forma con 'ser' + el participio pasado del verbo.""",
        "ejemplo": "La carta fue escrita por mi padre.",
        "pregunta": "En la oración 'La casa es construida', la voz es...",
        "opciones": ["Activa", "Pasiva"],
        "respuesta_correcta": "Pasiva"
    },
    "Lección 232: Oraciones Coordinadas": {
        "teoría": """Son dos o más oraciones que tienen sentido completo y se unen por una conjunción.
Tipos: copulativas (y), disyuntivas (o), adversativas (pero), distributivas (ora...ora).""",
        "ejemplo": "Estudio y trabajo.",
        "pregunta": "La oración 'No me gusta la leche, pero la tomo' es...",
        "opciones": ["Coordinada adversativa.", "Coordinada copulativa.", "Coordinada disyuntiva."],
        "respuesta_correcta": "Coordinada adversativa."
    },
    "Lección 233: Oraciones Subordinadas": {
        "teoría": """Son oraciones que dependen de otra principal y no tienen sentido completo por sí solas.
Pueden ser sustantivas, adjetivas o adverbiales.""",
        "ejemplo": "Me gusta que vengas a verme.",
        "pregunta": "En 'Me dijo que no vendría', 'que no vendría' es una oración...",
        "opciones": ["Principal.", "Subordinada.", "Coordinada."],
        "respuesta_correcta": "Subordinada."
    },
    "Lección 234: El 'queísmo'": {
        "teoría": """El 'queísmo' es el uso incorrecto de 'que' en lugar de 'de que'.
Ocurre con verbos que exigen la preposición 'de' (ej: 'alegrarse de', 'darse cuenta de').""",
        "ejemplo": "Incorrecto: 'Me alegro que estés bien.' Correcto: 'Me alegro de que estés bien.'",
        "pregunta": "La frase correcta es:",
        "opciones": ["No me di cuenta que te fuiste.", "No me di cuenta de que te fuiste."],
        "respuesta_correcta": "No me di cuenta de que te fuiste."
    },
    "Lección 235: El 'dequeísmo'": {
        "teoría": """El 'dequeísmo' es el uso incorrecto de 'de que' cuando solo se necesita 'que'.
Verifica si puedes sustituir 'de que' por 'eso'.""",
        "ejemplo": "Incorrecto: 'Pienso de que es tarde.' Correcto: 'Pienso que es tarde.'",
        "pregunta": "La frase correcta es:",
        "opciones": ["Le pedí de que me ayudara.", "Le pedí que me ayudara."],
        "respuesta_correcta": "Le pedí que me ayudara."
    },
    "Lección 236: Uso de las mayúsculas": {
        "teoría": """Se usa mayúscula al principio de una oración, en nombres propios y en siglas.""",
        "ejemplo": "Mi nombre es Juan. La ONU es un organismo internacional.",
        "pregunta": "La forma correcta de escribir 'estados unidos' es:",
        "opciones": ["estados unidos", "Estados unidos", "Estados Unidos"],
        "respuesta_correcta": "Estados Unidos"
    },
    "Lección 237: Uso de la H (al inicio de palabra)": {
        "teoría": """Se usa 'h' al inicio de las palabras que empiezan por 'hue', 'hie', 'hui', 'hum'.
Ejemplos: hueso, hielo, huir, humo.""",
        "ejemplo": "El hueso es duro.",
        "pregunta": "La palabra '_uelo' se escribe con 'h'.",
        "opciones": ["Suelo", "Abuelo", "Huelo"],
        "respuesta_correcta": "Huelo"
    },
    "Lección 238: El punto y aparte": {
        "teoría": """El punto y aparte se usa para separar dos párrafos distintos, que desarrollan ideas diferentes, aunque relacionadas.""",
        "ejemplo": "Terminamos un tema. Ahora empezamos uno nuevo.",
        "pregunta": "¿Qué indica el punto y aparte?",
        "opciones": ["El final de una oración.", "El final de un párrafo.", "El final de un texto."],
        "respuesta_correcta": "El final de un párrafo."
    },
    "Lección 239: Los sustantivos": {
        "teoría": """El sustantivo es una clase de palabra que nombra a personas, animales, cosas, lugares, ideas o sentimientos.""",
        "ejemplo": "Casa, perro, felicidad.",
        "pregunta": "En la frase 'El coche rojo', la palabra 'coche' es un...",
        "opciones": ["Adjetivo.", "Verbo.", "Sustantivo."],
        "respuesta_correcta": "Sustantivo."
    },
    "Lección 240: El verbo": {
        "teoría": """El verbo es la palabra que expresa acción, estado, proceso o existencia del sujeto.""",
        "ejemplo": "Correr, estar, existir.",
        "pregunta": "En la frase 'Ella canta muy bien', 'canta' es un...",
        "opciones": ["Sustantivo.", "Verbo.", "Adverbio."],
        "respuesta_correcta": "Verbo."
    },
    "Lección 241: El adjetivo": {
        "teoría": """El adjetivo es la palabra que describe o califica al sustantivo. Debe concordar con él en género y número.""",
        "ejemplo": "Casa grande, perros rápidos.",
        "pregunta": "En la frase 'El cielo azul', 'azul' es un...",
        "opciones": ["Sustantivo.", "Adverbio.", "Adjetivo."],
        "respuesta_correcta": "Adjetivo."
    },
    "Lección 242: Las preposiciones": {
        "teoría": """Las preposiciones son palabras invariables que sirven de nexo para unir palabras o grupos de palabras.
Ejemplos: a, ante, bajo, con, contra, de, desde, en, entre, hacia, hasta, para, por, según, sin, sobre, tras.""",
        "ejemplo": "Voy a la escuela. El libro es para ti.",
        "pregunta": "En la frase 'El libro está sobre la mesa', 'sobre' es una...",
        "opciones": ["Conjunción.", "Preposición.", "Adverbio."],
        "respuesta_correcta": "Preposición."
    },
    "Lección 243: Las conjunciones": {
        "teoría": """Las conjunciones son palabras invariables que unen oraciones o palabras.
Ejemplos: y, e, ni, o, u, pero, mas, sino.""",
        "ejemplo": "Compré pan y leche. No quiero esto, sino aquello.",
        "pregunta": "En la frase 'Leche o jugo', 'o' es una...",
        "opciones": ["Preposición.", "Conjunción.", "Adverbio."],
        "respuesta_correcta": "Conjunción."
    },
    "Lección 244: El artículo": {
        "teoría": """El artículo es la palabra que acompaña al sustantivo para especificarlo o determinarlo.
Ejemplos: el, la, los, las (determinados); un, una, unos, unas (indeterminados).""",
        "ejemplo": "El perro es grande. Una niña canta.",
        "pregunta": "En la frase 'Los niños juegan', 'los' es un...",
        "opciones": ["Sustantivo.", "Adjetivo.", "Artículo."],
        "respuesta_correcta": "Artículo."
    },
    "Lección 245: Reglas de la C, S y Z (continuación)": {
        "teoría": """Se escriben con 'z' las palabras que terminan en -azo (golpe) o -aza.
Ejemplos: portazo, manaza.""",
        "ejemplo": "Dio un cabezazo.",
        "pregunta": "La terminación para 'cuchara...' (aumentativo) es:",
        "opciones": ["-azo", "-aza", "-izo"],
        "respuesta_correcta": "-aza"
    },
    "Lección 246: Uso de la H (en palabras compuestas)": {
        "teoría": """En las palabras compuestas, la 'h' se mantiene si la palabra original la lleva.
Ejemplo: 'malhumor' (de 'humor'), 'bienhechor' (de 'hechor').""",
        "ejemplo": "Se debe escribir 'malhumorado'.",
        "pregunta": "La palabra 'bien__ado' se escribe con 'h'.",
        "opciones": ["Echado", "Hechado", "Hechado"],
        "respuesta_correcta": "Hechado"
    },
    "Lección 247: El 'porqué', 'por qué', 'porque' y 'por que'": {
        "teoría": """'Porqué' (sustantivo) significa 'la causa'.
'Por qué' (interrogativo) para preguntar la razón.
'Porque' (conjunción) para dar una razón.
'Por que' (preposición + relativo) para introducir una oración de relativo.""",
        "ejemplo": "No entiendo el porqué. ¿Por qué no vienes? Vengo porque quiero. La razón por que lo hice...",
        "pregunta": "La forma correcta para 'No sé _____ no me llamas' es:",
        "opciones": ["porque", "por que", "por qué"],
        "respuesta_correcta": "por qué"
    },
    "Lección 248: Uso de la G y la J (continuación)": {
        "teoría": """Se escribe con 'g' antes de 'e' e 'i' las palabras que empiezan por 'geo-'.
Ejemplos: geografía, geología, geometría.""",
        "ejemplo": "La geografía es mi materia favorita.",
        "pregunta": "La palabra 'geo__ía' se escribe con:",
        "opciones": ["J", "G"],
        "respuesta_correcta": "G"
    },
    "Lección 249: El Imperativo": {
        "teoría": """El imperativo es un modo verbal que se usa para dar órdenes, peticiones o mandatos.
No tiene conjugación para la primera persona del singular ('yo').""",
        "ejemplo": "Ven aquí. No corras. Cierra la puerta.",
        "pregunta": "La forma correcta del imperativo para 'tú' del verbo 'hablar' es:",
        "opciones": ["Habla", "Hablo", "Hablas"],
        "respuesta_correcta": "Habla"
    },
    "Lección 250: Los Verbos Defectivos": {
        "teoría": """Son verbos que no tienen una conjugación completa y solo se usan en algunas personas o tiempos.
Ejemplo: 'abolir' solo se conjuga en algunas formas.""",
        "ejemplo": "No existe la forma 'yo abolí' o 'tú aboles'.",
        "pregunta": "El verbo 'atañer' se usa comúnmente en la tercera persona del singular, ¿es un verbo...?",
        "opciones": ["Regular.", "Irregular.", "Defectivo."],
        "respuesta_correcta": "Defectivo."
    },
    "Lección 251: La Apóstrofe": {
        "teoría": """El apóstrofe (') no se usa en español para abreviar palabras, como en inglés. Su uso es muy limitado, principalmente para indicar que se ha omitido una vocal en poesía o dialectos.""",
        "ejemplo": "D'el (de él), p'al (para el).",
        "pregunta": "La frase 'L'hice yo' es incorrecta en español moderno, ¿por qué?",
        "opciones": ["Es un verbo irregular.", "El apóstrofe no se usa para abreviar.", "Es una palabra arcaica."],
        "respuesta_correcta": "El apóstrofe no se usa para abreviar."
    },
    "Lección 252: El infinitivo": {
        "teoría": """El infinitivo es la forma no conjugada del verbo, y termina en -ar, -er o -ir.""",
        "ejemplo": "Amar, temer, partir.",
        "pregunta": "El infinitivo del verbo 'caminaba' es:",
        "opciones": ["Caminar", "Caminando", "Caminó"],
        "respuesta_correcta": "Caminar"
    },
    "Lección 253: El futuro simple": {
        "teoría": """El futuro simple se usa para hablar de acciones que ocurrirán en el futuro.
Las terminaciones son -é, -ás, -á, -emos, -éis, -án, para todas las conjugaciones.""",
        "ejemplo": "Mañana compraré un coche.",
        "pregunta": "La forma correcta del futuro para 'yo salir' es:",
        "opciones": ["Saldré", "Salió", "Saliendo"],
        "respuesta_correcta": "Saldré"
    },
    "Lección 254: El condicional simple": {
        "teoría": """El condicional simple se usa para expresar acciones hipotéticas o deseos.
Las terminaciones son -ía, -ías, -ía, -íamos, -íais, -ían.""",
        "ejemplo": "Me gustaría viajar por el mundo.",
        "pregunta": "La forma correcta del condicional para 'tú poder' es:",
        "opciones": ["Podrías", "Puedes", "Pudiste"],
        "respuesta_correcta": "Podrías"
    },
    "Lección 255: La preposición 'a'": {
        "teoría": """Se usa la preposición 'a' para indicar movimiento hacia un lugar, el complemento indirecto y el complemento directo de persona.""",
        "ejemplo": "Voy a la escuela. Le di el regalo a mi madre. Vi a mi hermano.",
        "pregunta": "En la frase 'Conocí a un amigo', el uso de 'a' es para:",
        "opciones": ["Indicar un lugar.", "Un complemento directo de persona.", "Un complemento indirecto."],
        "respuesta_correcta": "Un complemento directo de persona."
    },
    "Lección 256: El 'sino' y el 'si no'": {
        "teoría": """'Sino' es una conjunción adversativa que se usa después de una oración negativa.
'Si no' es la combinación de la conjunción condicional 'si' y el adverbio de negación 'no'.""",
        "ejemplo": "No quiero té, sino café. Si no estudias, no aprobarás.",
        "pregunta": "La forma correcta para 'No vino ____ quería' es:",
        "opciones": ["sino", "si no"],
        "respuesta_correcta": "si no"
    },
    "Lección 257: El Uso de 'con que', 'con qué' y 'conque'": {
        "teoría": """'Con que' es la preposición 'con' más el pronombre relativo 'que'.
'Con qué' se usa en preguntas.
'Conque' es una conjunción consecutiva.""",
        "ejemplo": "La herramienta con que lo hizo... ¿Con qué lo vas a hacer? Conque no querías venir...",
        "pregunta": "La forma correcta para '¿____ has preparado el pastel?' es:",
        "opciones": ["Conque", "Con qué", "Con que"],
        "respuesta_correcta": "Con qué"
    },
    "Lección 258: Las oraciones impersonales": {
        "teoría": """Son oraciones que carecen de sujeto explícito o implícito.
Pueden ser con verbos de fenómenos naturales (llueve), o con 'se'.""",
        "ejemplo": "Llueve mucho. Se vive bien aquí.",
        "pregunta": "La oración 'Se busca personal' es...",
        "opciones": ["Una oración personal.", "Una oración impersonal.", "Una oración pasiva."],
        "respuesta_correcta": "Una oración impersonal."
    },
    "Lección 259: El uso de 'y' e 'e'": {
        "teoría": """La conjunción 'y' se convierte en 'e' cuando la palabra que sigue comienza con el sonido 'i' (incluyendo las palabras que comienzan con 'hi').""",
        "ejemplo": "Padre e hijo. Ciencia e historia.",
        "pregunta": "La forma correcta para 'lápiz __ impresora' es:",
        "opciones": ["y", "e"],
        "respuesta_correcta": "e"
    },
    "Lección 260: El uso de 'o' y 'u'": {
        "teoría": """La conjunción 'o' se convierte en 'u' cuando la palabra que sigue comienza con el sonido 'o' o 'ho'.""",
        "ejemplo": "Siete u ocho. Caminas u oyes.",
        "pregunta": "La forma correcta para 'leche __ hoy' es:",
        "opciones": ["o", "u"],
        "respuesta_correcta": "u"
    },
    "Lección 261: Los adverbios terminados en '-mente'": {
        "teoría": """Se forman añadiendo '-mente' a la forma femenina del adjetivo. Si el adjetivo tiene tilde, el adverbio también la conserva.""",
        "ejemplo": "Rápida -> Rápidamente. Fácil -> Fácilmente.",
        "pregunta": "La forma correcta del adverbio para 'común' es:",
        "opciones": ["Comúnmente", "Comunmente", "Comúnmente"],
        "respuesta_correcta": "Comúnmente"
    },
    "Lección 262: Las conjunciones 'aunque' y 'incluso'": {
        "teoría": """'Aunque' es una conjunción concesiva que introduce una objeción a lo dicho.
'Incluso' es un adverbio que enfatiza lo dicho, significando 'aun' o 'hasta'.""",
        "ejemplo": "Aunque llovió, salimos. Incluso los niños lo entendieron.",
        "pregunta": "La palabra correcta para '____ sabiendo la respuesta, no la dijo' es:",
        "opciones": ["Aunque", "Incluso"],
        "respuesta_correcta": "Aunque"
    },
    "Lección 263: Uso de los puntos suspensivos": {
        "teoría": """Los puntos suspensivos (...) se usan para indicar una interrupción en la oración, un final incompleto, o para dejar algo a la imaginación.""",
        "ejemplo": "Me gustaría ir, pero...",
        "pregunta": "¿Cuál es el uso incorrecto de los puntos suspensivos?",
        "opciones": ["Para indicar un final incompleto.", "Para separar un sujeto de su verbo.", "Para dejar algo a la imaginación."],
        "respuesta_correcta": "Para separar un sujeto de su verbo."
    },
    "Lección 264: El uso de 'si' y 'sí'": {
        "teoría": """'Si' (sin tilde) es una conjunción condicional.
'Sí' (con tilde) es un adverbio de afirmación o un sustantivo.""",
        "ejemplo": "Si vienes, te espero. Sí, voy a ir. Dijo que sí.",
        "pregunta": "La forma correcta para '____ me preguntas, te digo que ____' es:",
        "opciones": ["Si, si", "Sí, sí", "Si, sí"],
        "respuesta_correcta": "Si, sí"
    },
    "Lección 265: La 'tilde' en los monosílabos": {
        "teoría": """Los monosílabos, palabras de una sola sílaba, no se acentúan, a menos que sea una tilde diacrítica.""",
        "ejemplo": "Fe, sol, fue, vio.",
        "pregunta": "La palabra 'fue'...",
        "opciones": ["Lleva tilde.", "No lleva tilde."],
        "respuesta_correcta": "No lleva tilde."
    },
    "Lección 266: Los verbos en presente de indicativo": {
        "teoría": """Se usa el presente de indicativo para acciones que ocurren en el momento actual, hábitos, o hechos universales.""",
        "ejemplo": "Yo hablo, tú comes, él vive.",
        "pregunta": "La conjugación correcta para 'nosotros comer' es:",
        "opciones": ["Comemos", "Comemos", "Comieron"],
        "respuesta_correcta": "Comemos"
    },
    "Lección 267: Los verbos en pretérito perfecto simple": {
        "teoría": """Se usa para acciones que ocurrieron en el pasado y están completamente terminadas.""",
        "ejemplo": "Ayer fui al cine. Comí en un restaurante.",
        "pregunta": "La conjugación correcta para 'yo hablar' en pretérito perfecto simple es:",
        "opciones": ["Hablé", "Hablaban", "Hablaría"],
        "respuesta_correcta": "Hablé"
    },
    "Lección 268: Los verbos en pretérito imperfecto": {
        "teoría": """Se usa para acciones pasadas no terminadas, hábitos en el pasado o para describir una situación pasada.""",
        "ejemplo": "De niño, jugaba en el parque. Llovía cuando salimos.",
        "pregunta": "La conjugación correcta para 'ellos comer' en pretérito imperfecto es:",
        "opciones": ["Comieron", "Comían", "Comen"],
        "respuesta_correcta": "Comían"
    },
    "Lección 269: Los Verbos en futuro compuesto": {
        "teoría": """Se usa para expresar una acción futura que estará terminada antes de otra acción futura.
Se forma con 'habré' + participio.""",
        "ejemplo": "Para mañana ya habré terminado el trabajo.",
        "pregunta": "La forma correcta para 'tú' de 'haber comido' es:",
        "opciones": ["Habrías comido", "Habrás comido", "Habías comido"],
        "respuesta_correcta": "Habrás comido"
    },
    "Lección 270: Uso de la G y la J (continuación)": {
        "teoría": """Se escriben con 'j' las palabras que terminan en -jero, -jera, -jería.
Ejemplos: pasajero, mensajera, conserjería.""",
        "ejemplo": "La mensajera es mi hermana.",
        "pregunta": "La terminación -jería se escribe con:",
        "opciones": ["G", "J"],
        "respuesta_correcta": "J"
    },
    "Lección 271: El uso de los verbos 'haber' y 'a ver'": {
        "teoría": """'Haber' es un verbo auxiliar o impersonal (hay).
'A ver' es una secuencia de la preposición 'a' y el verbo 'ver'.""",
        "ejemplo": "Hay un libro en la mesa. Vamos a ver la película.",
        "pregunta": "La forma correcta para '____ si viene' es:",
        "opciones": ["Haber", "A ver"],
        "respuesta_correcta": "A ver"
    },
    "Lección 272: Uso de 'halla', 'haya', 'allá' y 'aya'": {
        "teoría": """'Halla' (verbo hallar). 'Haya' (verbo haber). 'Allá' (adverbio de lugar). 'Aya' (sustantivo).""",
        "ejemplo": "Él halla la respuesta. Ojalá haya suerte. Allá iremos. La aya es buena.",
        "pregunta": "La forma correcta para 'No creo que ____ una solución' es:",
        "opciones": ["halla", "haya", "aya"],
        "respuesta_correcta": "haya"
    },
    "Lección 273: Los determinantes": {
        "teoría": """Los determinantes son palabras que acompañan al sustantivo para concretarlo y limitar su significado.""",
        "ejemplo": "El, mi, tres, este, algún.",
        "pregunta": "En la frase 'Tres perros corren', 'tres' es un...",
        "opciones": ["Adjetivo.", "Verbo.", "Determinante numeral."],
        "respuesta_correcta": "Determinante numeral."
    },
    "Lección 274: Los diptongos con tilde": {
        "teoría": """Cuando el diptongo lleva una vocal abierta y una cerrada, la tilde se coloca sobre la vocal abierta, siguiendo las reglas de acentuación.""",
        "ejemplo": "Bailáis, náufrago.",
        "pregunta": "La palabra 'cielo' no lleva tilde porque...",
        "opciones": ["Es una palabra llana y termina en vocal.", "El diptongo no tiene vocal abierta.", "La 'e' es átona."],
        "respuesta_correcta": "Es una palabra llana y termina en vocal."
    },
    "Lección 275: Los hiatos con tilde": {
        "teoría": """Cuando un hiato está formado por una vocal abierta y una cerrada, la vocal cerrada siempre lleva tilde, sin importar las reglas de acentuación.""",
        "ejemplo": "Ma-rí-a, sa-ú-co, bú-ho.",
        "pregunta": "La palabra 'país' lleva tilde porque...",
        "opciones": ["Es una palabra aguda.", "Hay un hiato y la vocal cerrada es tónica.", "Es un diptongo."],
        "respuesta_correcta": "Hay un hiato y la vocal cerrada es tónica."
    },
    "Lección 276: La voz activa": {
        "teoría": """En la voz activa, el sujeto realiza la acción del verbo.
Es la forma más común de construir oraciones en español.""",
        "ejemplo": "El perro persiguió al gato.",
        "pregunta": "La oración 'El libro fue leído por Juan' está en voz...",
        "opciones": ["Activa", "Pasiva"],
        "respuesta_correcta": "Pasiva"
    },
    "Lección 277: Los sustantivos concretos y abstractos": {
        "teoría": """Los sustantivos concretos nombran a seres u objetos que se pueden percibir por los sentidos.
Los sustantivos abstractos nombran ideas, sentimientos o conceptos que no se pueden percibir.""",
        "ejemplo": "Concreto: mesa, lápiz. Abstracto: felicidad, amor.",
        "pregunta": "La palabra 'belleza' es un sustantivo...",
        "opciones": ["Concreto.", "Abstracto."],
        "respuesta_correcta": "Abstracto."
    },
    "Lección 278: Los sustantivos contables y no contables": {
        "teoría": """Los sustantivos contables se pueden contar y tienen forma plural.
Los sustantivos no contables no se pueden contar individualmente.""",
        "ejemplo": "Contable: perro, lápiz. No contable: agua, arena.",
        "pregunta": "La palabra 'arena' es un sustantivo...",
        "opciones": ["Contable.", "No contable."],
        "respuesta_correcta": "No contable."
    },
    "Lección 279: Los diminutivos y aumentativos": {
        "teoría": """Los diminutivos (-ito/-ita, -illo/-illa) expresan tamaño pequeño o cariño.
Los aumentativos (-ón/-ona, -azo/-aza) expresan tamaño grande.""",
        "ejemplo": "Casita, perrazo.",
        "pregunta": "La forma correcta para el diminutivo de 'coche' es:",
        "opciones": ["Cochón", "Cochito", "Cochazo"],
        "respuesta_correcta": "Cochito"
    },
    "Lección 280: Uso de la B y la V (continuación)": {
        "teoría": """Se usa 'v' después de las consonantes 'd' y 'n'.
Ejemplos: adverbio, enviar, invierno.""",
        "ejemplo": "Envié la carta a tiempo.",
        "pregunta": "La forma correcta para 'in__ierno' es:",
        "opciones": ["Invierno", "Inbierno"],
        "respuesta_correcta": "Invierno"
    },
    "Lección 281: Los verbos en modo subjuntivo": {
        "teoría": """El subjuntivo se usa para expresar deseo, duda, posibilidad, o un hecho no real o hipotético.""",
        "ejemplo": "Quizás vaya al cine. Espero que me escuche.",
        "pregunta": "La oración 'Es posible que ____ mañana' requiere el subjuntivo del verbo 'llover'.",
        "opciones": ["llueva", "lloverá", "llovía"],
        "respuesta_correcta": "llueva"
    },
    "Lección 282: El imperativo afirmativo y negativo": {
        "teoría": """El imperativo afirmativo (tú) tiene la misma forma que la tercera persona del singular del presente de indicativo.
El imperativo negativo (tú) se forma con 'no' + la segunda persona del singular del presente de subjuntivo.""",
        "ejemplo": "¡Habla! ¡No hables!",
        "pregunta": "La forma correcta del imperativo negativo para 'tú' del verbo 'correr' es:",
        "opciones": ["No corres.", "No corras.", "No correr."],
        "respuesta_correcta": "No corras."
    },
    "Lección 283: El uso de 'también' y 'tampoco'": {
        "teoría": """'También' es un adverbio de afirmación que significa 'de igual modo'.
'Tampoco' es un adverbio de negación que significa 'ni siquiera' o 'ni'.""",
        "ejemplo": "Yo también voy. Yo tampoco voy.",
        "pregunta": "La forma correcta para 'A mí no me gusta el helado, y a ti ____' es:",
        "opciones": ["también", "tampoco"],
        "respuesta_correcta": "tampoco"
    },
    "Lección 284: La diferencia entre 'haber' y 'a ver'": {
        "teoría": """'Haber' es un verbo auxiliar o impersonal.
'A ver' es una secuencia de la preposición 'a' y el verbo 'ver'.""",
        "ejemplo": "Tiene que haber más gente. Ven a ver la televisión.",
        "pregunta": "La forma correcta para 'No tiene que ____ un problema' es:",
        "opciones": ["haber", "a ver"],
        "respuesta_correcta": "haber"
    },
    "Lección 285: El uso de la 'tilde' en adverbios terminados en '-mente'": {
        "teoría": """Los adverbios terminados en '-mente' conservan la acentuación del adjetivo del que provienen.
Ejemplo: 'fácil' (lleva tilde) -> 'fácilmente' (lleva tilde).""",
        "ejemplo": "Rápidamente, tímidamente.",
        "pregunta": "La palabra 'lógicamente' se escribe con 'tilde' porque...",
        "opciones": ["Es una palabra esdrújula.", "Proviene del adjetivo 'lógica' que la lleva.", "Todas las palabras terminadas en '-mente' la llevan."],
        "respuesta_correcta": "Proviene del adjetivo 'lógica' que la lleva."
    },
    "Lección 286: El uso de 'y' y 'e' (continuación)": {
        "teoría": """La conjunción 'y' no se transforma en 'e' si la palabra que sigue comienza por 'h' y después la 'i'.""",
        "ejemplo": "Tengo hambre y hielo.",
        "pregunta": "La forma correcta para 'mesa __ hierro' es:",
        "opciones": ["y", "e"],
        "respuesta_correcta": "y"
    },
    "Lección 287: Los verbos en pretérito pluscuamperfecto de indicativo": {
        "teoría": """Se usa para hablar de una acción pasada que ocurrió antes que otra acción pasada.
Se forma con 'había' + participio.""",
        "ejemplo": "Cuando llegué, ella ya había comido.",
        "pregunta": "La forma correcta para 'ellos' de 'haber comido' es:",
        "opciones": ["Habrían comido", "Habían comido", "Habrán comido"],
        "respuesta_correcta": "Habían comido"
    },
    "Lección 288: El uso de los verbos 'ir' y 'ser' en pretérito perfecto simple": {
        "teoría": """Los verbos 'ir' y 'ser' tienen la misma conjugación en el pretérito perfecto simple.
'Yo fui', 'tú fuiste', 'él fue', etc. El contexto aclara el significado.""",
        "ejemplo": "Fui al cine. Fui muy feliz.",
        "pregunta": "En la frase 'Ella fue la mejor', el verbo 'fue' corresponde a:",
        "opciones": ["Ir", "Ser"],
        "respuesta_correcta": "Ser"
    },
    "Lección 289: El uso de 'por que', 'porque', 'porqué', 'por qué' (continuación)": {
        "teoría": """'Por que' es la preposición 'por' más la conjunción 'que'.""",
        "ejemplo": "La razón por que lo hice es personal.",
        "pregunta": "La forma correcta para 'No sé el ____ de su decisión' es:",
        "opciones": ["porqué", "por qué"],
        "respuesta_correcta": "porqué"
    },
    "Lección 290: Los pronombres relativos 'quien', 'quienes'": {
        "teoría": """Se usan para referirse a personas.
'Quien' se usa en singular y 'quienes' en plural.""",
        "ejemplo": "El hombre con quien hablé. Los amigos con quienes salí.",
        "pregunta": "La palabra correcta para 'La mujer a ____ llamé es mi madre' es:",
        "opciones": ["quien", "quienes"],
        "respuesta_correcta": "quien"
    },
    "Lección 291: El uso de la 'tilde' en monosílabos (continuación)": {
        "teoría": """La tilde diacrítica se usa para distinguir:
- 'él' (pronombre) de 'el' (artículo).
- 'tú' (pronombre) de 'tu' (posesivo).
- 'mí' (pronombre) de 'mi' (posesivo).""",
        "ejemplo": "El coche es de él. Tu hermano es mi amigo.",
        "pregunta": "La forma correcta para '____ libro es para ____' es:",
        "opciones": ["Tu, mí", "Tú, mí", "Tu, mi"],
        "respuesta_correcta": "Tu, mí"
    },
    "Lección 292: El uso de 'sé' y 'se'": {
        "teoría": """'Sé' (con tilde) es la forma del verbo 'saber' o 'ser'.
'Se' (sin tilde) es un pronombre personal o reflexivo.""",
        "ejemplo": "Sé que vendrás. ¡Sé bueno! Se lo dio a su amigo.",
        "pregunta": "La forma correcta para '____ que tengo que estudiar' es:",
        "opciones": ["Se", "Sé"],
        "respuesta_correcta": "Sé"
    },
    "Lección 293: Los adverbios de negación": {
        "teoría": """Expresan negación. El más común es 'no', pero hay otros como 'nunca', 'jamás', 'tampoco'.""",
        "ejemplo": "No iré. Nunca he estado allí.",
        "pregunta": "El adverbio 'jamás' significa...",
        "opciones": ["A veces.", "Siempre.", "Nunca."],
        "respuesta_correcta": "Nunca."
    },
    "Lección 294: Los adverbios de duda": {
        "teoría": """Expresan duda o posibilidad.
Ejemplos: quizás, tal vez, probablemente, posiblemente.""",
        "ejemplo": "Quizás vayamos al cine.",
        "pregunta": "La palabra 'probablemente' indica:",
        "opciones": ["Certeza.", "Duda.", "Posibilidad."],
        "respuesta_correcta": "Posibilidad."
    },
    "Lección 295: La oración pasiva refleja": {
        "teoría": """Es una forma de oración pasiva con el pronombre 'se' y un verbo en tercera persona.
El sujeto recibe la acción, pero no se menciona quién la realiza.""",
        "ejemplo": "Se venden casas. Se construyó una escuela.",
        "pregunta": "En la frase 'Se habla español', ¿quién habla?",
        "opciones": ["Alguien específico.", "No se especifica.", "Los españoles."],
        "respuesta_correcta": "No se especifica."
    },
    "Lección 296: La tilde en los demostrativos": {
        "teoría": """Los pronombres demostrativos ('este', 'ese', 'aquel') ya no llevan tilde para diferenciarse de los adjetivos, según la RAE.
Sin embargo, su uso es opcional si hay ambigüedad.""",
        "ejemplo": "Compré este libro. Este me gusta.",
        "pregunta": "La frase 'Compraré este' es ambigua. ¿Cuál de las dos opciones resuelve la ambigüedad?",
        "opciones": ["Compraré este libro.", "Compraré éste.", "Compraré ése libro."],
        "respuesta_correcta": "Compraré éste."
    },
    "Lección 297: El uso de 'porque', 'porqué', 'por qué' y 'por que' (repaso)": {
        "teoría": """'Porque' para dar una razón. 'Por qué' para preguntar la razón. 'Porqué' para referirse a la causa. 'Por que' para un caso específico.""",
        "ejemplo": "Llegué tarde porque el bus se averió. ¿Por qué llegaste tarde? Me explicó el porqué de su decisión. La razón por que lo hice...",
        "pregunta": "La forma correcta para 'No vino ____ no quiso' es:",
        "opciones": ["por que", "por qué", "porque"],
        "respuesta_correcta": "porque"
    },
    "Lección 298: Los adverbios de modo": {
        "teoría": """Indican la forma en que se realiza una acción.
Terminan en '-mente' o son palabras como 'bien', 'mal', 'así', etc.""",
        "ejemplo": "Lo hizo muy bien.",
        "pregunta": "La palabra 'lentamente' es un adverbio de...",
        "opciones": ["Lugar.", "Tiempo.", "Modo."],
        "respuesta_correcta": "Modo."
    },
    "Lección 299: Los adverbios de lugar": {
        "teoría": """Indican dónde ocurre una acción.
Ejemplos: aquí, allí, cerca, lejos, encima, debajo.""",
        "ejemplo": "El libro está encima de la mesa.",
        "pregunta": "La palabra 'allí' es un adverbio de...",
        "opciones": ["Lugar.", "Tiempo.", "Modo."],
        "respuesta_correcta": "Lugar."
    },
    "Lección 300: Los adverbios de tiempo": {
        "teoría": """Indican cuándo ocurre una acción.
Ejemplos: hoy, mañana, ayer, ahora, antes, después.""",
        "ejemplo": "Llegaré mañana.",
        "pregunta": "La palabra 'después' es un adverbio de...",
        "opciones": ["Lugar.", "Tiempo.", "Modo."],
        "respuesta_correcta": "Tiempo."
    },
    "Lección 301: Oraciones subordinadas sustantivas": {
        "teoría": """Una oración subordinada sustantiva cumple la función de un sustantivo.
Puede ser el sujeto, el objeto directo o el objeto indirecto de la oración principal.""",
        "ejemplo": "Me gusta que vengas a verme.",
        "pregunta": "En la oración 'Es necesario que vengas pronto', la subordinada 'que vengas pronto' es un...",
        "opciones": ["Sujeto.", "Objeto directo.", "Objeto indirecto."],
        "respuesta_correcta": "Sujeto."
    },
    "Lección 302: Oraciones subordinadas adjetivas": {
        "teoría": """Una oración subordinada adjetiva (o de relativo) modifica a un sustantivo de la oración principal.
Comienzan con un pronombre relativo como 'que', 'quien', 'el cual', 'cuyo'.""",
        "ejemplo": "La casa que compré es grande.",
        "pregunta": "En 'El libro que me prestaste es bueno', la subordinada 'que me prestaste' es un...",
        "opciones": ["Complemento de régimen.", "Objeto directo.", "Complemento del sustantivo."],
        "respuesta_correcta": "Complemento del sustantivo."
    },
    "Lección 303: Oraciones subordinadas adverbiales": {
        "teoría": """Una oración subordinada adverbial funciona como un adverbio en la oración principal.
Pueden ser de lugar, tiempo, modo, causa, consecuencia, etc.""",
        "ejemplo": "Iré cuando termine mi tarea. (subordinada de tiempo)",
        "pregunta": "En 'Lo hizo como le enseñaron', la oración subordinada es de...",
        "opciones": ["Lugar.", "Modo.", "Tiempo."],
        "respuesta_correcta": "Modo."
    },
    "Lección 304: Complemento Directo (CD)": {
        "teoría": """El complemento directo recibe la acción del verbo de manera directa.
Se sustituye por los pronombres 'lo', 'la', 'los', 'las'.""",
        "ejemplo": "Compré un libro. -> Lo compré.",
        "pregunta": "En la oración 'Vi a Juan', el complemento directo es:",
        "opciones": ["Vi", "a Juan", "Juan"],
        "respuesta_correcta": "a Juan"
    },
    "Lección 305: Complemento Indirecto (CI)": {
        "teoría": """El complemento indirecto indica a quién beneficia o perjudica la acción del verbo.
Se sustituye por los pronombres 'le' o 'les'.""",
        "ejemplo": "Le di un regalo a mi madre. -> Le di un regalo.",
        "pregunta": "En la oración 'Compré flores para mi novia', el complemento indirecto es:",
        "opciones": ["flores", "para mi novia", "Compré"],
        "respuesta_correcta": "para mi novia"
    },
    "Lección 306: Complemento de Régimen Verbal": {
        "teoría": """Es un complemento que requiere el verbo para que la oración tenga sentido.
Generalmente se introduce con una preposición que el verbo exige.""",
        "ejemplo": "El libro trata de la vida. (tratar de)",
        "pregunta": "En 'Confío en ti', el complemento de régimen es:",
        "opciones": ["Confío", "en ti", "ti"],
        "respuesta_correcta": "en ti"
    },
    "Lección 307: El Sujeto Tácito (u omitido)": {
        "teoría": """El sujeto tácito es el sujeto que no aparece explícitamente en la oración, pero se puede deducir por la forma verbal.""",
        "ejemplo": "Estudiamos para el examen. (Sujeto: nosotros)",
        "pregunta": "En la oración 'Viajó a París', el sujeto tácito es:",
        "opciones": ["Yo", "Él/ella", "Ustedes"],
        "respuesta_correcta": "Él/ella"
    },
    "Lección 308: Vicios del lenguaje: Barbarismo": {
        "teoría": """El barbarismo es el uso de palabras extranjeras o de construcciones ajenas a la lengua propia.
También puede ser la mala pronunciación o escritura de palabras.""",
        "ejemplo": "Dijo 'bizarro' por 'raro'.",
        "pregunta": "La palabra 'haiga' en lugar de 'haya' es un...",
        "opciones": ["Solecismo.", "Barbarismo.", "Cacofonía."],
        "respuesta_correcta": "Barbarismo."
    },
    "Lección 309: Vicios del lenguaje: Solecismo": {
        "teoría": """El solecismo es una falta de sintaxis, es decir, una construcción incorrecta de la oración.""",
        "ejemplo": "Incorrecto: 'Se alquilan coches para ir.' Correcto: 'Se alquila coche para ir.'",
        "pregunta": "La frase 'Ha llegado la familia de Juan, los cuales se quedarán una semana' es un...",
        "opciones": ["Barbarismo.", "Solecismo.", "Cacofonía."],
        "respuesta_correcta": "Solecismo."
    },
    "Lección 310: Vicios del lenguaje: Anfibología": {
        "teoría": """La anfibología es la falta de claridad en la expresión, lo que provoca que una oración se pueda interpretar de varias maneras.""",
        "ejemplo": "Se vende vestido de novia de seda para señora. (¿El vestido es de seda o la señora?)",
        "pregunta": "La frase 'Vi a Juan paseando a su perro y a su hermano' es un ejemplo de...",
        "opciones": ["Barbarismo.", "Anfibología.", "Cacofonía."],
        "respuesta_correcta": "Anfibología."
    },
    "Lección 311: Figuras retóricas: La Metáfora": {
        "teoría": """La metáfora es una figura literaria que consiste en la identificación de dos elementos: uno real y uno imaginario, sin un nexo comparativo.""",
        "ejemplo": "Tus ojos son dos luceros. (ojos = luceros)",
        "pregunta": "En la frase 'El tiempo es oro', 'oro' es una...",
        "opciones": ["Comparación.", "Metáfora.", "Personificación."],
        "respuesta_correcta": "Metáfora."
    },
    "Lección 312: Figuras retóricas: La Metonimia": {
        "teoría": """La metonimia es la figura retórica que sustituye un término por otro con el que tiene una relación de contigüidad o dependencia.""",
        "ejemplo": "Leí a Góngora. (No leí al autor, leí su obra).",
        "pregunta": "En 'Se tomó una copa', 'copa' es una...",
        "opciones": ["Metáfora.", "Metonimia.", "Hipérbole."],
        "respuesta_correcta": "Metonimia."
    },
    "Lección 313: Figuras retóricas: El Hipérbaton": {
        "teoría": """El hipérbaton es una alteración del orden gramatical de las palabras en una oración.""",
        "ejemplo": "Volverán las oscuras golondrinas en tu balcón sus nidos a colgar. (G. A. Bécquer)",
        "pregunta": "La frase 'Al hombre de su tierra le dolían los ojos' es un ejemplo de...",
        "opciones": ["Metáfora.", "Hipérbaton.", "Comparación."],
        "respuesta_correcta": "Hipérbaton."
    },
    "Lección 314: Figuras retóricas: La Hipérbole": {
        "teoría": """La hipérbole es una exageración con la finalidad de enfatizar una idea o sentimiento.""",
        "ejemplo": "Te lo dije mil veces.",
        "pregunta": "La frase 'Estoy que me muero de sueño' es un ejemplo de...",
        "opciones": ["Metáfora.", "Hipérbole.", "Comparación."],
        "respuesta_correcta": "Hipérbole."
    },
    "Lección 315: Figuras retóricas: El Oxímoron": {
        "teoría": """El oxímoron es la unión de dos palabras con significados opuestos, creando un tercer significado.""",
        "ejemplo": "Silencio atronador.",
        "pregunta": "La expresión 'un secreto a voces' es un...",
        "opciones": ["Hipérbole.", "Antítesis.", "Oxímoron."],
        "respuesta_correcta": "Oxímoron."
    },
    "Lección 316: Uso de los paréntesis ()": {
        "teoría": """Los paréntesis se usan para incluir información adicional o aclaraciones en una oración.""",
        "ejemplo": "La reunión (que duró dos horas) fue muy productiva.",
        "pregunta": "El uso de los paréntesis en la frase 'El rey (que era muy sabio) gobernó durante años' es para...",
        "opciones": ["Una cita textual.", "Una aclaración.", "Una enumeración."],
        "respuesta_correcta": "Una aclaración."
    },
    "Lección 317: Uso de los corchetes []": {
        "teoría": """Los corchetes se usan para incluir información en un texto que ya se encuentra entre paréntesis.""",
        "ejemplo": "La obra de Juan (que escribió en 1990 [con mi ayuda]) fue un éxito.",
        "pregunta": "El uso de los corchetes en la frase anterior es para...",
        "opciones": ["Una aclaración dentro de otra.", "Una enumeración.", "Una cita textual."],
        "respuesta_correcta": "Una aclaración dentro de otra."
    },
    "Lección 318: Uso de la raya o guion largo —": {
        "teoría": """La raya se usa para introducir el diálogo de un personaje o para encerrar una aclaración en un contexto más formal que los paréntesis.""",
        "ejemplo": "— ¿Qué hora es? —preguntó. El perro —que estaba dormido— se levantó.",
        "pregunta": "El uso de la raya en la frase 'Mi amigo —al que vi ayer— me saludó' es para...",
        "opciones": ["Una enumeración.", "Una interrupción.", "Una aclaración."],
        "respuesta_correcta": "Una aclaración."
    },
    "Lección 319: Formación de palabras: Composición": {
        "teoría": """La composición es la unión de dos o más palabras para formar una nueva con un significado distinto.""",
        "ejemplo": "Abrelatas (abre + latas).",
        "pregunta": "La palabra 'paraguas' se ha formado por...",
        "opciones": ["Derivación.", "Composición.", "Parasíntesis."],
        "respuesta_correcta": "Composición."
    },
    "Lección 320: Formación de palabras: Derivación": {
        "teoría": """La derivación es la creación de una nueva palabra añadiendo un prefijo o un sufijo a la raíz de una palabra.""",
        "ejemplo": "Submarino (sub + marino). Panadería (pan + adería).",
        "pregunta": "La palabra 'inútil' se ha formado por...",
        "opciones": ["Composición.", "Derivación.", "Parasíntesis."],
        "respuesta_correcta": "Derivación."
    },
    "Lección 321: Formación de palabras: Parasíntesis": {
        "teoría": """La parasíntesis es la combinación de composición y derivación, o de un prefijo y un sufijo al mismo tiempo.""",
        "ejemplo": "Enriquecer (en + rico + ecer).",
        "pregunta": "La palabra 'envejecer' se ha formado por...",
        "opciones": ["Derivación.", "Parasíntesis.", "Composición."],
        "respuesta_correcta": "Parasíntesis."
    },
    "Lección 322: Uso de mayúsculas en títulos y siglas": {
        "teoría": """Se usa mayúscula al inicio de los títulos de libros, películas y obras de arte.
Las siglas se escriben todas en mayúsculas.""",
        "ejemplo": "El Quijote, La Celestina, ONU.",
        "pregunta": "La forma correcta de escribir 'rae' es:",
        "opciones": ["Rae", "rae", "RAE"],
        "respuesta_correcta": "RAE"
    },
    "Lección 323: Los marcadores del discurso": {
        "teoría": """Los marcadores del discurso son palabras o expresiones que guían al lector o al oyente en la organización del texto.
Ejemplos: en primer lugar, además, en conclusión, por otro lado.""",
        "ejemplo": "En primer lugar, hay que analizar el problema.",
        "pregunta": "El marcador 'por consiguiente' es de tipo...",
        "opciones": ["Adversativo.", "Consecutivo.", "Aditivo."],
        "respuesta_correcta": "Consecutivo."
    },
    "Lección 324: Uso de 'si no' y 'sino' (continuación)": {
        "teoría": """'Si no' (separado) es la conjunción condicional 'si' seguida del adverbio de negación 'no'.
'Sino' (junto) es una conjunción adversativa.""",
        "ejemplo": "Si no vienes, me voy. No era azul, sino verde.",
        "pregunta": "La forma correcta para 'No es él el culpable, ____ su hermano' es:",
        "opciones": ["si no", "sino"],
        "respuesta_correcta": "sino"
    },
    "Lección 325: El laísmo, leísmo y loísmo": {
        "teoría": """Son vicios del lenguaje relacionados con el uso incorrecto de los pronombres de objeto directo e indirecto.
- **Laísmo**: Uso de 'la'/'las' por 'le'/'les'. (Le vi a la chica).
- **Leísmo**: Uso de 'le'/'les' por 'lo'/'los' o 'la'/'las'. (Le vi al chico).
- **Loísmo**: Uso de 'lo'/'los' por 'le'/'les'. (Lo dije a mis padres).""",
        "ejemplo": "Le vi al chico. (Leísmo). Correcto: Lo vi.",
        "pregunta": "La frase 'La dije la verdad a mi amiga' es un ejemplo de...",
        "opciones": ["Laísmo.", "Leísmo.", "Loísmo."],
        "respuesta_correcta": "Laísmo."
    },
    "Lección 326: El Atributo": {
        "teoría": """El atributo es un complemento que califica o describe al sujeto.
Aparece con verbos copulativos (ser, estar, parecer).""",
        "ejemplo": "Mi amigo es alto.",
        "pregunta": "En la oración 'La casa parece nueva', el atributo es:",
        "opciones": ["La casa", "parece", "nueva"],
        "respuesta_correcta": "nueva"
    },
    "Lección 327: El Predicativo": {
        "teoría": """El predicativo es un complemento que se refiere al sujeto o al objeto directo, y a la vez modifica al verbo.
Aparece con verbos predicativos (no copulativos).""",
        "ejemplo": "Llegó cansado. (cansado se refiere a él y a la acción de llegar)",
        "pregunta": "En la oración 'El perro corre contento', el predicativo es:",
        "opciones": ["perro", "corre", "contento"],
        "respuesta_correcta": "contento"
    },
    "Lección 328: El uso de los dos puntos y el guion largo": {
        "teoría": """Se usan dos puntos para introducir una cita textual.
El guion largo puede usarse para introducir un diálogo.""",
        "ejemplo": "El escritor dijo: 'La vida es un sueño'.",
        "pregunta": "Para introducir un diálogo, ¿qué signo de puntuación se usa?",
        "opciones": ["Dos puntos.", "Guion largo.", "Punto y coma."],
        "respuesta_correcta": "Guion largo."
    },
    "Lección 329: Los préstamos lingüísticos": {
        "teoría": """Son palabras de un idioma que son adoptadas por otro.
Se pueden adaptar a la fonética y la ortografía del idioma receptor (ej. 'fútbol' de 'football') o mantener su forma original ('marketing').""",
        "ejemplo": "Email, chef, show.",
        "pregunta": "La palabra 'bacon' es un préstamo lingüístico que significa:",
        "opciones": ["Tocino", "Pan", "Jamón"],
        "respuesta_correcta": "Tocino"
    },
    "Lección 330: El 'deber' y 'deber de'": {
        "teoría": """'Deber' + infinitivo indica una obligación.
'Deber de' + infinitivo indica una suposición o probabilidad.""",
        "ejemplo": "Debes estudiar. (Obligación). Debe de ser tarde. (Suposición).",
        "pregunta": "La forma correcta para 'Ellos ____ de haber llegado' es:",
        "opciones": ["deben", "deben de"],
        "respuesta_correcta": "deben de"
    },
    "Lección 331: El uso de la 'tilde' en adverbios terminados en '-mente' (continuación)": {
        "teoría": """El adverbio conserva la tilde del adjetivo en su forma femenina.
Ejemplo: 'fácil' -> 'fácilmente'.""",
        "ejemplo": "Lentamente, ágilmente.",
        "pregunta": "El adverbio de 'difícil' se escribe:",
        "opciones": ["Dificilmente", "Díficilmente", "Difícilmente"],
        "respuesta_correcta": "Difícilmente"
    },
    "Lección 332: La oración simple: análisis sintáctico": {
        "teoría": """Para analizar una oración simple, se identifica el sujeto y el predicado, y luego los complementos del verbo.""",
        "ejemplo": "La niña come dulces. (Sujeto: La niña, Predicado: come dulces, Objeto directo: dulces).",
        "pregunta": "En la oración 'Mi hermana corre por el parque', el complemento de lugar es:",
        "opciones": ["Mi hermana", "corre", "por el parque"],
        "respuesta_correcta": "por el parque"
    },
    "Lección 333: El uso de los verbos 'ir' y 'ser' en pretérito": {
        "teoría": """Ambos verbos tienen la misma conjugación en el pretérito perfecto simple, por lo que el contexto es clave.""",
        "ejemplo": "Fui a la tienda (ir). Fui feliz (ser).",
        "pregunta": "En la frase 'Ella fue mi mejor amiga', 'fue' es el verbo:",
        "opciones": ["Ir", "Ser"],
        "respuesta_correcta": "Ser"
    },
    "Lección 334: Uso de los verbos 'echar' y 'hechar'": {
        "teoría": """'Echar' (sin h) significa lanzar, tirar o expulsar.
'Hechar' (con h) no existe en español, es un error ortográfico.""",
        "ejemplo": "Échame una mano. (Ayúdame).",
        "pregunta": "La forma correcta para 'No quiero que me ____' es:",
        "opciones": ["eches", "heches"],
        "respuesta_correcta": "eches"
    },
    "Lección 335: Vicios del lenguaje: Anacoluto": {
        "teoría": """Es la ruptura de la sintaxis de una oración. La segunda parte de la frase no concuerda con la primera.""",
        "ejemplo": "La película me parece aburrida, y no me gusta.",
        "pregunta": "La frase 'La gente me ha dicho que tienen que esperar' es un ejemplo de...",
        "opciones": ["Anfibología.", "Barbarismo.", "Anacoluto."],
        "respuesta_correcta": "Anacoluto."
    },
    "Lección 336: Pronombre personal átono 'se' y sus valores": {
        "teoría": """El pronombre 'se' tiene varios valores:
- **Reflexivo**: Se lavó (a sí mismo).
- **Recíproco**: Se saludaron (el uno al otro).
- **Impersonal**: Se vive bien aquí.
- **Pasivo-reflejo**: Se venden coches.""",
        "ejemplo": "Se lo di. (variante de 'le' + 'lo').",
        "pregunta": "En la oración 'Se compran casas usadas', el valor de 'se' es:",
        "opciones": ["Reflexivo.", "Impersonal.", "Pasivo-reflejo."],
        "respuesta_correcta": "Pasivo-reflejo."
    },
    "Lección 337: El uso del punto y seguido": {
        "teoría": """El punto y seguido se usa para separar oraciones que forman parte de un mismo párrafo, pero que tratan ideas diferentes.""",
        "ejemplo": "Compró el coche. Luego fue a casa.",
        "pregunta": "El punto y seguido es para...",
        "opciones": ["Terminar un párrafo.", "Separar oraciones dentro de un párrafo.", "Introducir una cita."],
        "respuesta_correcta": "Separar oraciones dentro de un párrafo."
    },
    "Lección 338: Elipsis verbal": {
        "teoría": """La elipsis es la omisión de un elemento de la oración (usualmente el verbo) porque se entiende por el contexto.""",
        "ejemplo": "Juan come pan y María [come] galletas.",
        "pregunta": "En la frase 'Ella tiene dos gatos, y yo, uno', la palabra 'yo' es el sujeto, y 'uno' es el...",
        "opciones": ["Complemento de régimen.", "Objeto directo.", "Sujeto."],
        "respuesta_correcta": "Objeto directo."
    },
    "Lección 339: La Tilde Diacrítica en interrogativos y exclamativos": {
        "teoría": """Los pronombres, adverbios y adjetivos interrogativos y exclamativos siempre llevan tilde, a diferencia de sus formas relativas.""",
        "ejemplo": "¿Qué hora es? ¡Qué calor! La casa que compré...",
        "pregunta": "En la frase 'Dime ____ quieres', se usa la tilde para preguntar:",
        "opciones": ["que", "qué"],
        "respuesta_correcta": "qué"
    },
    "Lección 340: El uso de 'ha' y 'a'": {
        "teoría": """'Ha' es la forma del verbo 'haber'. 'A' es una preposición.""",
        "ejemplo": "Ha venido. Voy a la casa.",
        "pregunta": "La forma correcta para '____ terminado de estudiar' es:",
        "opciones": ["A", "Ha"],
        "respuesta_correcta": "Ha"
    },
    "Lección 341: Las Oraciones Coordinadas Copulativas": {
        "teoría": """Unen oraciones que expresan adición o suma.
Los nexos son: 'y' (e), 'ni'.""",
        "ejemplo": "Comí y dormí. No come ni duerme.",
        "pregunta": "La oración 'No estudia ni trabaja' es de tipo:",
        "opciones": ["Coordinada adversativa.", "Coordinada copulativa.", "Coordinada disyuntiva."],
        "respuesta_correcta": "Coordinada copulativa."
    },
    "Lección 342: Las Oraciones Coordinadas Adversativas": {
        "teoría": """Unen oraciones que expresan oposición o contraste.
Los nexos son: 'pero', 'mas', 'sino'.""",
        "ejemplo": "Quería ir, pero no pude.",
        "pregunta": "La oración 'No es que no pueda, sino que no quiere' es de tipo:",
        "opciones": ["Coordinada copulativa.", "Coordinada adversativa.", "Coordinada distributiva."],
        "respuesta_correcta": "Coordinada adversativa."
    },
    "Lección 343: Las Oraciones Coordinadas Disyuntivas": {
        "teoría": """Unen oraciones que expresan una opción o una alternativa.
Los nexos son: 'o' (u), 'ora...ora'.""",
        "ejemplo": "Vienes o te quedas.",
        "pregunta": "La oración 'Ora canta, ora baila' es de tipo:",
        "opciones": ["Coordinada disyuntiva.", "Coordinada copulativa.", "Coordinada adversativa."],
        "respuesta_correcta": "Coordinada disyuntiva."
    },
    "Lección 344: Las Oraciones Coordinadas Distributivas": {
        "teoría": """Unen oraciones que expresan una alternancia o una distribución de acciones.
Los nexos son: 'ya...ya', 'bien...bien', 'unos...otros'.""",
        "ejemplo": "Ya ríe, ya llora.",
        "pregunta": "La oración 'Unos ríen, otros lloran' es de tipo:",
        "opciones": ["Coordinada copulativa.", "Coordinada distributiva.", "Coordinada disyuntiva."],
        "respuesta_correcta": "Coordinada distributiva."
    },
    "Lección 345: La Tilde Diacrítica en 'solo'": {
        "teoría": """La palabra 'solo' no lleva tilde, aunque se puede usar para evitar ambigüedad en algunos casos.
Ejemplo: 'Comió solo un dulce'. (Solo, adverbio).
'Vive solo'. (Solo, adjetivo).""",
        "ejemplo": "Camina solo por la calle. (Adverbio: sin compañía, Adjetivo: en soledad).",
        "pregunta": "La RAE recomienda no usar la tilde en 'solo'. ¿Verdadero o Falso?",
        "opciones": ["Verdadero.", "Falso."],
        "respuesta_correcta": "Verdadero."
    },
    "Lección 346: La Tilde Diacrítica en 'aun'": {
        "teoría": """'Aún' (con tilde) es un adverbio de tiempo que significa 'todavía'.
'Aun' (sin tilde) es una conjunción o adverbio que significa 'incluso' o 'hasta'""",
        "ejemplo": "Aún no ha llegado. (Todavía). Aun los niños lo entendieron. (Incluso).",
        "pregunta": "La forma correcta para '____ sin dinero, voy al cine' es:",
        "opciones": ["Aún", "Aun"],
        "respuesta_correcta": "Aun"
    },
    "Lección 347: El uso de 'así mismo', 'asimismo' y 'a sí mismo'": {
        "teoría": """'Asimismo' (junto) es un adverbio que significa 'también' o 'además'.
'A sí mismo' (separado) es una preposición, pronombre y adverbio que significa 'hacia uno mismo'.
'Así mismo' (separado) es una locución adverbial que significa 'de esa misma manera'.""",
        "ejemplo": "Asimismo, es importante... Se lo dijo a sí mismo. Lo hizo así mismo.",
        "pregunta": "La forma correcta para 'No se lo digas, hazlo ____' es:",
        "opciones": ["así mismo", "asimismo", "a sí mismo"],
        "respuesta_correcta": "así mismo"
    },
    "Lección 348: Oraciones impersonales con 'se'": {
        "teoría": """Son oraciones que no tienen un sujeto concreto, y se construyen con el pronombre 'se' seguido de un verbo en tercera persona del singular.""",
        "ejemplo": "Se come bien en este restaurante. Se vive tranquilo aquí.",
        "pregunta": "La oración 'Se vive mejor en verano' es...",
        "opciones": ["Impersonal.", "Pasiva refleja.", "Activa."],
        "respuesta_correcta": "Impersonal."
    },
    "Lección 349: El uso de 'sino que'": {
        "teoría": """Se usa 'sino que' como conjunción adversativa para unir oraciones que expresan oposición, cuando la segunda oración tiene su propio verbo conjugado.""",
        "ejemplo": "No quiere trabajar, sino que quiere vivir de sus padres.",
        "pregunta": "La forma correcta para 'No tengo hambre, ____ sed' es:",
        "opciones": ["sino que", "sino"],
        "respuesta_correcta": "sino"
    },
    "Lección 350: Vicios del lenguaje: Pleonasmo": {
        "teoría": """Es el uso de palabras innecesarias que ya están implícitas en el significado de la frase.
También se le conoce como 'redundancia'.""",
        "ejemplo": "Subir arriba, bajar abajo, entrar adentro.",
        "pregunta": "La frase 'Lo vi con mis propios ojos' es un ejemplo de...",
        "opciones": ["Anfibología.", "Barbarismo.", "Pleonasmo."],
        "respuesta_correcta": "Pleonasmo."
    },
    "Lección 351: Vicios del lenguaje: Cacofonía": {
        "teoría": """Es la repetición de sonidos similares en una oración, que resulta desagradable para el oído.""",
        "ejemplo": "El partido de fútbol es una ocasión de colisión.",
        "pregunta": "La frase 'Teatro, teatro, te he traído una tarea' es un ejemplo de...",
        "opciones": ["Anacoluto.", "Cacofonía.", "Pleonasmo."],
        "respuesta_correcta": "Cacofonía."
    },
    "Lección 352: El Uso de la C y la Z (repaso)": {
        "teoría": """La 'c' se usa en palabras con sonido de 'k' antes de 'a', 'o', 'u', y con sonido de 's' antes de 'e', 'i'.
La 'z' se usa antes de 'a', 'o', 'u' y al final de palabra.""",
        "ejemplo": "Casa, coche, cuento, cena, cine, zapato, zona, zoológico, voz.",
        "pregunta": "La palabra 'cigarro' se escribe con 'c' porque el sonido es de:",
        "opciones": ["K", "S", "Z"],
        "respuesta_correcta": "S"
    },
    "Lección 353: Las palabras homófonas 'ah', 'ha' y 'a'": {
        "teoría": """'Ah' es una interjección.
'Ha' es del verbo haber.
'A' es una preposición.""",
        "ejemplo": "¡Ah, ya entiendo! Ha llovido. Voy a casa.",
        "pregunta": "La forma correcta para '____ hecho la tarea' es:",
        "opciones": ["A", "Ha", "Ah"],
        "respuesta_correcta": "Ha"
    },
    "Lección 354: La Tilde en 'qué', 'quién', 'cuándo', 'cómo' (repaso)": {
        "teoría": """Estas palabras llevan tilde cuando se usan en oraciones interrogativas o exclamativas, ya sean directas o indirectas.""",
        "ejemplo": "¿Qué quieres? No sé qué quieres. ¡Qué bien!",
        "pregunta": "La forma correcta para 'Dime ____ vas a llegar' es:",
        "opciones": ["cuando", "cuándo"],
        "respuesta_correcta": "cuándo"
    },
    "Lección 355: Los verbos reflexivos": {
        "teoría": """Los verbos reflexivos se conjugan con un pronombre personal (me, te, se, nos, os, se) que indica que la acción del verbo recae sobre el propio sujeto.""",
        "ejemplo": "Me lavo (a mí mismo).",
        "pregunta": "El verbo 'peinarse' es...",
        "opciones": ["Regular.", "Irregular.", "Reflexivo."],
        "respuesta_correcta": "Reflexivo."
    },
    "Lección 356: Los verbos recíprocos": {
        "teoría": """Los verbos recíprocos se usan para expresar una acción mutua entre dos o más sujetos.
Se construyen con los pronombres 'nos', 'os', 'se'.""",
        "ejemplo": "Juan y María se aman. (Se aman el uno al otro).",
        "pregunta": "En la oración 'Nos ayudamos', el verbo es...",
        "opciones": ["Reflexivo.", "Recíproco.", "Impersonal."],
        "respuesta_correcta": "Recíproco."
    },
    "Lección 357: Uso de la G y la J (repaso)": {
        "teoría": """Se escribe con 'j' las palabras que tienen el sonido fuerte de la 'g' y terminan en -jero, -jera, -jería.
También se usa 'j' en palabras que empiezan por 'ej-'.""",
        "ejemplo": "Ejemplo, ejercicio.",
        "pregunta": "La palabra 'ejercicio' se escribe con:",
        "opciones": ["G", "J"],
        "respuesta_correcta": "J"
    },
    "Lección 358: El uso de la Y y la LL": {
        "teoría": """La 'y' tiene un sonido de consonante cuando está al inicio de la palabra o entre vocales, y un sonido de vocal al final.
La 'll' es un dígrafo (dos letras) que representa un solo sonido.""",
        "ejemplo": "Yegua, payaso, ley, calle.",
        "pregunta": "La palabra 'pollo' se escribe con:",
        "opciones": ["Y", "LL"],
        "respuesta_correcta": "LL"
    },
    "Lección 359: El uso de la 'r' y la 'rr'": {
        "teoría": """La 'r' tiene un sonido suave al inicio de palabra y entre vocales.
La 'rr' tiene un sonido fuerte, y solo se usa entre vocales.""",
        "ejemplo": "Rosa, cara, perro, carro.",
        "pregunta": "La palabra 'carro' se escribe con 'rr' para:",
        "opciones": ["Indicar un sonido fuerte.", "Indicar un sonido suave.", "Una regla ortográfica sin motivo."],
        "respuesta_correcta": "Indicar un sonido fuerte."
    },
    "Lección 360: Los verbos en modo imperativo (repaso)": {
        "teoría": """El imperativo se usa para dar órdenes o hacer peticiones. Solo se usa en las formas 'tú', 'vosotros', 'usted' y 'ustedes'.""",
        "ejemplo": "Come. Comed. Coma. Coman.",
        "pregunta": "La forma correcta para 'vosotros' del verbo 'beber' es:",
        "opciones": ["Bebéis", "Bebed", "Beban"],
        "respuesta_correcta": "Bebed"
    },
    "Lección 361: Los verbos en modo subjuntivo (continuación)": {
        "teoría": """El subjuntivo se usa para expresar deseo, duda, emoción, posibilidad o una acción hipotética.
Ejemplo: 'Espero que vengas.' 'Tal vez estudie.'""",
        "ejemplo": "Ojalá que llueva.",
        "pregunta": "La frase 'No creo que haga sol' usa el modo...",
        "opciones": ["Indicativo.", "Subjuntivo.", "Imperativo."],
        "respuesta_correcta": "Subjuntivo."
    },
    "Lección 362: El uso de 'y' y 'e' (continuación)": {
        "teoría": """La conjunción 'y' se transforma en 'e' para evitar la cacofonía cuando la siguiente palabra empieza con el sonido /i/ o /hi/.""",
        "ejemplo": "Tengo hambre e impotencia. Es agua e hielo.",
        "pregunta": "La forma correcta para 'la belleza __ la inocencia' es:",
        "opciones": ["y", "e"],
        "respuesta_correcta": "y"
    },
    "Lección 363: El uso de la diéresis (¨)": {
        "teoría": """La diéresis se usa para indicar que la vocal 'u' en las sílabas 'güe' y 'güi' debe pronunciarse.
También se usa en la poesía para deshacer un diptongo.""",
        "ejemplo": "Vergüenza, pingüino, cigüeña. 'Con blando movimiento, rüido' (poesía).",
        "pregunta": "La palabra 'agua' no lleva diéresis porque...",
        "opciones": ["La 'u' no se pronuncia.", "La 'u' se pronuncia.", "Es una palabra llana."],
        "respuesta_correcta": "La 'u' se pronuncia."
    },
    "Lección 364: El uso del guion (-) y la raya (—)": {
        "teoría": """El guion (-) se usa para unir palabras compuestas o para separar las sílabas de una palabra.
La raya (—) se usa para los diálogos, o para incisos más formales.""",
        "ejemplo": "Socio-económico. Teléfono. — ¡Hola! El libro —un gran éxito—...",
        "pregunta": "Para unir dos palabras compuestas, como 'histórico' y 'social', se usa un...",
        "opciones": ["Guion.", "Raya."],
        "respuesta_correcta": "Guion."
    },
    "Lección 365: Los verbos en futuro perfecto": {
        "teoría": """El futuro perfecto se usa para expresar una acción que se habrá completado antes de otra acción futura.
Se forma con 'habré' + participio.""",
        "ejemplo": "Para el 2025, ya habré terminado mis estudios.",
        "pregunta": "La forma correcta para 'ella' del verbo 'haber llegado' es:",
        "opciones": ["Habrá llegado", "Habría llegado", "Ha llegado"],
        "respuesta_correcta": "Habrá llegado"
    },
    "Lección 366: Los verbos en condicional compuesto": {
        "teoría": """El condicional compuesto se usa para expresar una acción que podría haber ocurrido en el pasado pero no ocurrió.
Se forma con 'habría' + participio.""",
        "ejemplo": "Habría ido a la fiesta si me hubieran invitado.",
        "pregunta": "La forma correcta para 'yo' del verbo 'haber hablado' es:",
        "opciones": ["Habría hablado", "Había hablado", "Habré hablado"],
        "respuesta_correcta": "Habría hablado"
    },
    "Lección 367: El uso de 'aun' y 'aún' (repaso)": {
        "teoría": """'Aun' (sin tilde) equivale a 'incluso' o 'hasta'.
'Aún' (con tilde) equivale a 'todavía'.""",
        "ejemplo": "Aun con fiebre, fui a trabajar. Aún no ha llegado el autobús.",
        "pregunta": "La forma correcta para '____ es muy temprano' es:",
        "opciones": ["Aún", "Aun"],
        "respuesta_correcta": "Aún"
    },
    "Lección 368: Los complementos circunstanciales de lugar, tiempo y modo": {
        "teoría": """Indican las circunstancias en las que se realiza la acción del verbo.
- **Lugar**: ¿Dónde?
- **Tiempo**: ¿Cuándo?
- **Modo**: ¿Cómo?""",
        "ejemplo": "Lo hizo en su casa. (lugar) Lo hizo ayer. (tiempo) Lo hizo bien. (modo)",
        "pregunta": "En la frase 'Corrió rápidamente por el parque', 'rápidamente' es un complemento de...",
        "opciones": ["Lugar.", "Tiempo.", "Modo."],
        "respuesta_correcta": "Modo."
    },
    "Lección 369: Los vicios del lenguaje: Ambigüedad": {
        "teoría": """La ambigüedad es un tipo de anfibología.
Ocurre cuando una frase puede ser interpretada de dos o más formas.""",
        "ejemplo": "Ana le prestó a su hermana su libro. (¿El libro de Ana o el de su hermana?).",
        "pregunta": "La frase 'Vi a un hombre con binoculares' es ambigua. ¿Verdadero o Falso?",
        "opciones": ["Verdadero.", "Falso."],
        "respuesta_correcta": "Verdadero."
    },
    "Lección 370: La tilde en los adverbios de interrogación y exclamación (repaso)": {
        "teoría": """Los adverbios 'cómo', 'cuándo', 'dónde' y 'cuánto' llevan tilde en oraciones interrogativas y exclamativas.""",
        "ejemplo": "¿Dónde está? ¡Cuánto me alegro!",
        "pregunta": "En la frase 'No sé ____ vive', se usa la tilde para preguntar:",
        "opciones": ["donde", "dónde"],
        "respuesta_correcta": "dónde"
    },
    "Lección 371: El uso de 'adonde', 'adonde', 'adónde', 'a donde'": {
        "teoría": """'Adonde' (sin tilde) es un pronombre relativo que indica movimiento.
'Adónde' (con tilde) es un adverbio de lugar interrogativo o exclamativo.""",
        "ejemplo": "La casa adonde vamos... ¿Adónde vas?",
        "pregunta": "La forma correcta para 'No sé ____ ir' es:",
        "opciones": ["adonde", "adónde"],
        "respuesta_correcta": "adónde"
    },
    "Lección 372: La 'y' con valor de conjunción copulativa": {
        "teoría": """La conjunción 'y' tiene un valor de adición y se usa para unir dos o más elementos.""",
        "ejemplo": "Comí pan y queso.",
        "pregunta": "En la frase 'Luis y Ana son amigos', el conector 'y' tiene valor de...",
        "opciones": ["Adición.", "Contraste.", "Alternativa."],
        "respuesta_correcta": "Adición."
    },
    "Lección 373: Los verbos en presente de subjuntivo": {
        "teoría": """El presente de subjuntivo se usa para expresar deseos, dudas o emociones en el presente.""",
        "ejemplo": "Espero que vengas. Ojalá que llueva.",
        "pregunta": "La forma correcta para 'yo' del verbo 'hablar' en presente de subjuntivo es:",
        "opciones": ["hable", "hablo", "hablaría"],
        "respuesta_correcta": "hable"
    },
    "Lección 374: Los verbos en pretérito perfecto compuesto de indicativo": {
        "teoría": """Se usa para acciones que ocurrieron en un pasado reciente y tienen relevancia en el presente.
Se forma con 'he' + participio.""",
        "ejemplo": "He comido mucho hoy. (hoy es un pasado reciente)",
        "pregunta": "La forma correcta para 'tú' del verbo 'haber estudiado' es:",
        "opciones": ["Has estudiado", "Habías estudiado", "Estudiaste"],
        "respuesta_correcta": "Has estudiado"
    },
    "Lección 375: Los verbos en pretérito pluscuamperfecto de subjuntivo": {
        "teoría": """Se usa para expresar una acción pasada que es hipotética o no se ha realizado.
Se forma con 'hubiera' o 'hubiese' + participio.""",
        "ejemplo": "Si me lo hubieras dicho, habría ido.",
        "pregunta": "La forma correcta para 'ellos' del verbo 'haber hablado' es:",
        "opciones": ["Hubieran hablado", "Habrían hablado", "Habían hablado"],
        "respuesta_correcta": "Hubieran hablado"
    },
    "Lección 376: El uso de 'y/e' y 'o/u' (continuación)": {
        "teoría": """Se usa 'y' cuando la siguiente palabra empieza con el sonido /i/. Se usa 'e' cuando la siguiente palabra empieza con el sonido /hi/ o /i/.
No se usa 'e' si la palabra siguiente es el prefijo 'hie'. Ejemplos: hierro.""",
        "ejemplo": "Tengo hambre y hielo.",
        "pregunta": "La forma correcta para 'mesa __ hierro' es:",
        "opciones": ["y", "e"],
        "respuesta_correcta": "y"
    },
    "Lección 377: La tilde en 'por qué' y 'porque' (repaso)": {
        "teoría": """'Por qué' (separado y con tilde) para preguntar la causa.
'Porque' (junto y sin tilde) para responder a la causa.""",
        "ejemplo": "¿Por qué no comes? Porque no tengo hambre.",
        "pregunta": "La forma correcta para '____ llegaste tarde' es:",
        "opciones": ["Porqué", "Por qué", "Porque"],
        "respuesta_correcta": "Por qué"
    },
    "Lección 378: El uso de 'sino que' (repaso)": {
        "teoría": """Se usa 'sino' cuando lo que sigue es una palabra o un grupo de palabras sin verbo.
Se usa 'sino que' cuando lo que sigue es una oración con su propio verbo.""",
        "ejemplo": "No quiere un perro, sino un gato. No quiere un perro, sino que quiere un gato.",
        "pregunta": "La forma correcta para 'No estudia, ____ trabaja' es:",
        "opciones": ["sino que", "sino"],
        "respuesta_correcta": "sino que"
    },
    "Lección 379: El uso de la 'tilde' en monosílabos (repaso)": {
        "teoría": """La tilde diacrítica se usa para distinguir los monosílabos que tienen dos funciones gramaticales.
'tú' (pronombre personal) vs. 'tu' (posesivo).""",
        "ejemplo": "Tu coche es nuevo. Tú eres mi amigo.",
        "pregunta": "La forma correcta para 'Dime si ____ vas a ir' es:",
        "opciones": ["tú", "tu"],
        "respuesta_correcta": "tú"
    },
    "Lección 380: El uso de los puntos y aparte (repaso)": {
        "teoría": """El punto y aparte se usa para separar párrafos que tienen ideas principales diferentes.
El punto y seguido se usa para separar oraciones que tienen ideas relacionadas dentro del mismo párrafo.""",
        "ejemplo": "El punto y seguido se usa para separar oraciones. El punto y aparte separa párrafos.",
        "pregunta": "Para cambiar de tema en un texto, se usa un...",
        "opciones": ["Punto y seguido.", "Punto y aparte.", "Punto final."],
        "respuesta_correcta": "Punto y aparte."
    },
    "Lección 381: La tilde en las palabras compuestas": {
        "teoría": """Si una palabra compuesta se escribe con guion, cada componente mantiene su acentuación.
Si se escribe sin guion, sigue las reglas generales de acentuación.""",
        "ejemplo": "Físico-químico. Vigésimoquinto.",
        "pregunta": "La palabra 'decimotercero' es...",
        "opciones": ["Aguda y lleva tilde.", "Llena y no lleva tilde.", "Esdrújula y lleva tilde."],
        "respuesta_correcta": "Llena y no lleva tilde."
    },
    "Lección 382: La tilde en los adverbios terminados en '-mente' (repaso)": {
        "teoría": """Los adverbios terminados en '-mente' conservan la acentuación del adjetivo en su forma femenina, si la tuviera.""",
        "ejemplo": "Ágil -> ágilmente. Lenta -> lentamente.",
        "pregunta": "El adverbio de 'fácil' es:",
        "opciones": ["Facilmente", "Fácilmente", "Facilmente"],
        "respuesta_correcta": "Fácilmente"
    },
    "Lección 383: El uso de la 'b' y la 'v' (repaso)": {
        "teoría": """Se escribe con 'b' las palabras que empiezan por 'bu-', 'bur-', 'bus-'.
Se escribe con 'v' las palabras que empiezan por 'vice-', 'villa-'.""",
        "ejemplo": "Burro, buscar, viceversa, villano.",
        "pregunta": "La palabra correcta es:",
        "opciones": ["bicepresidente", "vicepresidente"],
        "respuesta_correcta": "vicepresidente"
    },
    "Lección 384: El uso de la 'g' y la 'j' (repaso)": {
        "teoría": """Se escribe con 'g' las palabras que empiezan por 'geo-'.
Se escribe con 'j' las palabras que terminan en '-aje' y '-eje'.""",
        "ejemplo": "Geografía, garaje, hereje.",
        "pregunta": "La palabra correcta es:",
        "opciones": ["garaje", "garaje"],
        "respuesta_correcta": "garaje"
    },
    "Lección 385: Los préstamos lingüísticos: anglicismos": {
        "teoría": """Son palabras o giros procedentes del inglés que se usan en otro idioma.
Pueden ser innecesarios ('email' por 'correo electrónico') o necesarios ('software').""",
        "ejemplo": "Sándwich, hobby, fútbol, marketing.",
        "pregunta": "La palabra 'feedback' es un anglicismo que significa:",
        "opciones": ["Alimentación.", "Retroalimentación.", "Regalo."],
        "respuesta_correcta": "Retroalimentación."
    },
    "Lección 386: Los préstamos lingüísticos: galicismos": {
        "teoría": """Son palabras o giros procedentes del francés que se usan en otro idioma.
Ejemplo: 'chef', 'croissant', 'boutique'.""",
        "ejemplo": "El chef preparó la cena.",
        "pregunta": "La palabra 'debut' es un galicismo que significa:",
        "opciones": ["Estreno.", "Baile.", "Fiesta."],
        "respuesta_correcta": "Estreno."
    },
    "Lección 387: Los vicios del lenguaje: neologismo": {
        "teoría": """Un neologismo es el uso de una palabra nueva que aún no ha sido aceptada oficialmente en el idioma.
Se usa para nombrar cosas que no tienen un nombre específico.""",
        "ejemplo": "Tuitear, bloguero.",
        "pregunta": "La palabra 'selfie' es un tipo de...",
        "opciones": ["Barbarismo.", "Neologismo.", "Solecismo."],
        "respuesta_correcta": "Neologismo."
    },
    "Lección 388: Vicios del lenguaje: arcaísmo": {
        "teoría": """El arcaísmo es el uso de una palabra o expresión que ya está en desuso en el idioma.
Ejemplo: 'ansina' por 'así', 'fierro' por 'hierro'.""",
        "ejemplo": "La frase 'mijo, no vayas' es un ejemplo de...",
        "opciones": ["Neologismo.", "Arcaísmo.", "Barbarismo."],
        "respuesta_correcta": "Arcaísmo."
    },
    "Lección 389: El uso de las mayúsculas en las siglas (repaso)": {
        "teoría": """Las siglas de más de cuatro letras solo llevan mayúscula la primera, a menos que sean nombres propios.""",
        "ejemplo": "Unicef, Unesco.",
        "pregunta": "La forma correcta de escribir 'ONU' es:",
        "opciones": ["onu", "Onu", "ONU"],
        "respuesta_correcta": "ONU"
    },
    "Lección 390: La conjunción 'mas' vs. 'más'": {
        "teoría": """'Mas' (sin tilde) es una conjunción adversativa que equivale a 'pero'.
'Más' (con tilde) es un adverbio de cantidad.""",
        "ejemplo": "Quise ayudarte, mas no pude. Quiero más agua.",
        "pregunta": "La forma correcta para 'Estudio, ____ no comprendo' es:",
        "opciones": ["mas", "más"],
        "respuesta_correcta": "mas"
    },
    "Lección 391: La conjunción 'o' vs 'u' (repaso)": {
        "teoría": """La conjunción 'o' se cambia a 'u' para evitar la cacofonía cuando la siguiente palabra empieza con el sonido /o/ o /ho/.""",
        "ejemplo": "Siete u ocho. Perros u osos.",
        "pregunta": "La forma correcta para 'lápiz __ hojalata' es:",
        "opciones": ["o", "u"],
        "respuesta_correcta": "u"
    },
    "Lección 392: El uso de 'y' vs 'e' (repaso)": {
        "teoría": """La conjunción 'y' se cambia a 'e' para evitar la cacofonía cuando la siguiente palabra empieza con el sonido /i/ o /hi/.""",
        "ejemplo": "Padre e hijo.",
        "pregunta": "La forma correcta para 'agua __ hielo' es:",
        "opciones": ["y", "e"],
        "respuesta_correcta": "e"
    },
    "Lección 393: La tilde en 'cómo', 'cuándo' y 'dónde' (repaso)": {
        "teoría": """Estas palabras se acentúan solo si son interrogativas o exclamativas, ya sean directas o indirectas.""",
        "ejemplo": "¿Cómo lo hiciste? No sé cómo lo hiciste.",
        "pregunta": "La forma correcta para 'La casa ____ vives es bonita' es:",
        "opciones": ["donde", "dónde"],
        "respuesta_correcta": "donde"
    },
    "Lección 394: Las oraciones subordinadas de relativo con 'quien' y 'quienes'": {
        "teoría": """Los pronombres 'quien' y 'quienes' se usan para referirse a personas.
'Quien' se usa en singular y 'quienes' en plural.""",
        "ejemplo": "La persona con quien hablé. Los amigos con quienes salí.",
        "pregunta": "La forma correcta para 'El autor a ____ admiras' es:",
        "opciones": ["quien", "quienes"],
        "respuesta_correcta": "quien"
    },
    "Lección 395: El uso de 'ser' y 'estar' (repaso)": {
        "teoría": """**Ser** se usa para cualidades permanentes o inherentes.
**Estar** se usa para estados temporales o ubicaciones.""",
        "ejemplo": "Soy alto. Estoy cansado.",
        "pregunta": "La forma correcta para 'El clima ____ frío hoy' es:",
        "opciones": ["es", "está"],
        "respuesta_correcta": "está"
    },
    "Lección 396: Las oraciones pasivas con 'ser' + participio": {
        "teoría": """La voz pasiva se usa para dar énfasis al objeto o al resultado de la acción, en lugar de a quien la realiza.
Se forma con el verbo 'ser' más el participio del verbo principal.""",
        "ejemplo": "La carta fue escrita por mi padre. (El énfasis está en la carta).",
        "pregunta": "La oración 'El libro fue leído por Juan' está en voz...",
        "opciones": ["Activa", "Pasiva"],
        "respuesta_correcta": "Pasiva"
    },
    "Lección 397: El uso de los puntos suspensivos (repaso)": {
        "teoría": """Indican que una frase o idea queda incompleta, o para expresar duda, temor o sorpresa.""",
        "ejemplo": "Quiero decirte algo, pero...",
        "pregunta": "El uso de los puntos suspensivos es para:",
        "opciones": ["Terminar una frase.", "Indicar una pausa.", "Continuar una idea."],
        "respuesta_correcta": "Indicar una pausa."
    },
    "Lección 398: La tilde en los adverbios terminados en '-mente' (repaso)": {
        "teoría": """Los adverbios que terminan en '-mente' conservan la tilde del adjetivo en su forma femenina, si la tuviera.""",
        "ejemplo": "Rápida -> rápidamente. Tímida -> tímidamente.",
        "pregunta": "El adverbio de 'difícil' se escribe:",
        "opciones": ["Dificilmente", "Díficilmente", "Difícilmente"],
        "respuesta_correcta": "Difícilmente"
    },
    "Lección 399: El uso de los signos de interrogación y exclamación": {
        "teoría": """En español, los signos de interrogación (¿?) y exclamación (¡!) se usan al inicio y al final de la frase.""",
        "ejemplo": "¿Qué hora es? ¡Qué bien!",
        "pregunta": "La forma correcta para 'Que me digas la verdad' en una pregunta es:",
        "opciones": ["¿Qué me digas la verdad?", "Que me digas la verdad.", "Qué me digas la verdad"],
        "respuesta_correcta": "¿Qué me digas la verdad?"
    },
    "Lección 400: El uso de las mayúsculas en los nombres de los meses y los días": {
        "teoría": """En español, los nombres de los días de la semana y de los meses del año se escriben en minúscula.""",
        "ejemplo": "Mañana es martes. Mi cumpleaños es en mayo.",
        "pregunta": "La forma correcta de escribir 'diciembre' es:",
        "opciones": ["Diciembre", "diciembre"],
        "respuesta_correcta": "diciembre"
    }
})


def run_test(lesson_data):
    """
    Ejecuta un pequeño test de opción múltiple para una lección.

    Args:
        lesson_data (dict): Un diccionario que contiene la pregunta, opciones y
                            la respuesta correcta.
    """
    pregunta = lesson_data.get("pregunta")
    opciones = lesson_data.get("opciones")
    respuesta_correcta = lesson_data.get("respuesta_correcta")

    if not all([pregunta, opciones, respuesta_correcta]):
        print("Datos de lección incompletos. Por favor, revisa el diccionario.")
        return

    print("\n--- Test de la lección ---")
    print(pregunta)
    for i, opcion in enumerate(opciones, 1):
        print(f"{i}. {opcion}")

    try:
        user_input = int(input("Ingresa el número de tu respuesta: "))
        if 1 <= user_input <= len(opciones):
            respuesta_usuario = opciones[user_input - 1]
            if respuesta_usuario == respuesta_correcta:
                print("¡Correcto! ¡Excelente trabajo!\n")
            else:
                print(f"Incorrecto. La respuesta correcta es: {respuesta_correcta}\n")
        else:
            print("Entrada inválida. Por favor, ingresa un número de la lista.\n")
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número.\n")


def main():
    """
    Función principal del programa.
    Permite al usuario seleccionar una lección y ejecutar su test.
    """
    print("¡Bienvenido al programa de lecciones de gramática!")
    print("---------------------------------------------------\n")

    lesson_titles = list(ALL_LESSONS.keys())

    while True:
        # Pide al usuario que elija una lección
        print("Lecciones disponibles:")
        for i, title in enumerate(lesson_titles, 1):
            print(f"{i}. {title}")
        
        print("\n(O puedes escribir 'salir' para terminar el programa)")
        
        try:
            user_choice = input("Selecciona el número de la lección que quieres aprender: ")
            
            if user_choice.lower() == 'salir':
                print("¡Gracias por usar el programa! ¡Hasta la próxima!")
                break
                
            choice_index = int(user_choice) - 1

            if 0 <= choice_index < len(lesson_titles):
                selected_title = lesson_titles[choice_index]
                lesson_data = ALL_LESSONS.get(selected_title)

                print(f"\n--- {selected_title} ---")
                print("Teoría:", lesson_data.get("teoría", "No hay teoría disponible."))
                print("Ejemplo:", lesson_data.get("ejemplo", "No hay ejemplo disponible."))
                
                # Ejecuta el test
                run_test(lesson_data)

            else:
                print("Opción inválida. Por favor, elige un número de la lista.\n")

        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número.\n")
        
        # Pide al usuario que presione enter para continuar
        input("Presiona Enter para continuar...")


if __name__ == "__main__":
    main()
