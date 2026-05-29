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
        "pregunta": "La palabra correcta es:",
        "opciones": ["Cebra", "Zebra", "Sebra"],
        "respuesta_correcta": "Cebra"
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
        "ejemplo": "Voy a casa. Le di el regalo a mi madre. Vi a mi hermano.",
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
        "teoría": """La conjunción 'y' se convierte en 'e' cuando la palabra que sigue comienza con el sonido 'i' (incluyendo las palabras que comienzan con 'hi').
Ejemplo: 'Padre e hijo'. 'Ciencia e historia'.",
        "pregunta": "La forma correcta para 'lápiz __ impresora' es:",
        "opciones": ["y", "e"],
        "respuesta_correcta": "e"
    },
    "Lección 260: El uso de 'o' y 'u'": {
        "teoría": """La conjunción 'o' se convierte en 'u' cuando la palabra que sigue comienza con el sonido 'o' o 'ho'.
Ejemplo: 'Siete u ocho'. 'Caminas u oyes'.",
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
    }
})


# Se combinan todas las lecciones en un solo diccionario.
ALL_LESSONS = {}
ALL_LESSONS.update(ENGLISH_LESSONS)
ALL_LESSONS.update(SPANISH_LESSONS)


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
