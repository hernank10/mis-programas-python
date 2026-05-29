import tkinter as tk
from tkinter import messagebox
import random

# Este es el diccionario principal que contiene TODAS las lecciones.
# Aquí es donde agregarías tus 100 lecciones o más.
GRAMMAR_LESSONS = {
    "Lección 1: El Verbo 'To Be'": {
        "teoría": """El verbo 'to be' (ser/estar) es uno de los más importantes en inglés.
Se conjuga de la siguiente manera:
- I am (Yo soy/estoy)
- You are (Tú eres/estás)
- He/She/It is (Él/Ella/Eso es/está)
- We are (Nosotros somos/estamos)
- They are (Ellos son/están)""",
        "ejemplo": "He is a student. (Él es un estudiante.)",
        "pregunta": "¿Cuál es la forma correcta del verbo 'to be' para 'we'?",
        "opciones": ["is", "am", "are"],
        "respuesta_correcta": "are"
    },
    "Lección 2: Plurales Regulares": {
        "teoría": """Para la mayoría de los sustantivos, se forma el plural agregando una 's' al final.
Ejemplos:
- cat -> cats
- car -> cars
- book -> books""",
        "ejemplo": "I have two books. (Yo tengo dos libros.)",
        "pregunta": "El plural de 'dog' es:",
        "opciones": ["doges", "dog", "dogs"],
        "respuesta_correcta": "dogs"
    },
    "Lección 3: Presente Simple (Afirmativo)": {
        "teoría": """Se usa para hablar de hábitos, verdades generales o hechos.
Para los sujetos 'I, you, we, they', se usa la forma base del verbo.
Para los sujetos 'he, she, it', se agrega una 's' al final del verbo.
Ejemplos:
- I work.
- She works.""",
        "ejemplo": "He reads a lot. (Él lee mucho.)",
        "pregunta": "¿Cuál es la forma correcta de 'to play' para 'we'?",
        "opciones": ["plays", "play", "to playing"],
        "respuesta_correcta": "play"
    },
    # --- AQUÍ EMPEZARÍAS A AGREGAR LAS NUEVAS LECCIONES ---
    "Lección 4: Preposiciones de Tiempo (in, on, at)": {
        "teoría": """Las preposiciones de tiempo se usan para indicar cuándo ocurre algo.
- 'at' se usa para horas y momentos específicos (at 3 PM, at noon).
- 'on' se usa para días y fechas (on Monday, on October 25th).
- 'in' se usa para meses, años, estaciones y períodos de tiempo más largos (in July, in 2024, in the morning).""",
        "ejemplo": "The meeting is at 10 AM on Monday.",
        "pregunta": "¿Qué preposición es correcta para 'the summer'?",
        "opciones": ["on", "at", "in"],
        "respuesta_correcta": "in"
    },
    "Lección 5: Pasado Simple": {
        "teoría": """El pasado simple se usa para acciones que ocurrieron y terminaron en el pasado.
Para verbos regulares, se agrega '-ed' a la forma base.
Ejemplos:
- walk -> walked
- play -> played
- visit -> visited
Para verbos irregulares, la forma cambia completamente.""",
        "ejemplo": "I walked to school yesterday. (Yo caminé a la escuela ayer.)",
        "pregunta": "El pasado simple de 'talk' es:",
        "opciones": ["talks", "talked", "talken"],
        "respuesta_correcta": "talked"
    },
    # --- LECCIÓN AGREGADA PARA ESTA RESPUESTA ---
    "Lección 6: El Verbo Modal 'should'": {
        "teoría": """El verbo modal 'should' se utiliza para dar consejos, sugerencias o para indicar una obligación no muy estricta.
Ejemplos:
- You should study for the test. (Deberías estudiar para el examen.)
- We should leave now. (Deberíamos irnos ahora.)""",
        "ejemplo": "She should eat more vegetables. (Ella debería comer más verduras.)",
        "pregunta": "Selecciona la oración que usa 'should' correctamente:",
        "opciones": ["He should to go.", "They should goes.", "You should go."],
        "respuesta_correcta": "You should go."
    },
    "Lección 7: Presente Continuo": {
        "teoría": """El presente continuo (o progresivo) se usa para acciones que están ocurriendo en el momento del habla. Se forma con el verbo 'to be' + verbo con '-ing'.
Ejemplos:
- I am eating. (Estoy comiendo.)
- She is running. (Ella está corriendo.)""",
        "ejemplo": "They are watching a movie. (Ellos están viendo una película.)",
        "pregunta": "La forma correcta de 'to sleep' en presente continuo para 'he' es:",
        "opciones": ["He is sleeping.", "He are sleeping.", "He sleeping."],
        "respuesta_correcta": "He is sleeping."
    },
    "Lección 8: Artículos (a, an)": {
        "teoría": """'A' y 'an' son artículos indefinidos.
- Se usa 'a' antes de sustantivos que comienzan con un sonido de consonante.
- Se usa 'an' antes de sustantivos que comienzan con un sonido de vocal.""",
        "ejemplo": "I have a car and an apple. (Tengo un coche y una manzana.)",
        "pregunta": "¿Qué artículo es correcto para 'umbrella'?",
        "opciones": ["a", "an", "the"],
        "respuesta_correcta": "an"
    },
    "Lección 9: El Futuro con 'will'": {
        "teoría": """El futuro simple con 'will' se usa para predicciones, promesas y decisiones espontáneas. Se forma con 'will' + la forma base del verbo.
Ejemplos:
- I will help you. (Te ayudaré.)
- It will rain tomorrow. (Lloverá mañana.)""",
        "ejemplo": "They will travel next year. (Ellos viajarán el próximo año.)",
        "pregunta": "Selecciona la oración que usa 'will' correctamente:",
        "opciones": ["She will to go.", "We will go.", "He wills go."],
        "respuesta_correcta": "We will go."
    },
    "Lección 10: Adjetivos Posesivos": {
        "teoría": """Los adjetivos posesivos se usan para mostrar a quién pertenece algo.
Ejemplos: my (mi), your (tu), his (su de él), her (su de ella), our (nuestro), their (su de ellos).
Siempre van antes del sustantivo que poseen.""",
        "ejemplo": "This is my book. (Este es mi libro.)",
        "pregunta": "El adjetivo posesivo para 'she' es:",
        "opciones": ["his", "her", "its"],
        "respuesta_correcta": "her"
    },
    "Lección 11: Pasado Continuo": {
        "teoría": """El pasado continuo se usa para acciones que estaban en progreso en un momento específico del pasado. Se forma con el pasado de 'to be' (was/were) + verbo con '-ing'.
Ejemplos:
- I was studying at 8 PM. (Yo estaba estudiando a las 8 PM.)""",
        "ejemplo": "They were playing football. (Ellos estaban jugando al fútbol.)",
        "pregunta": "La forma correcta de 'to talk' en pasado continuo para 'we' es:",
        "opciones": ["we was talking", "we were talking", "we talking"],
        "respuesta_correcta": "we were talking"
    },
    "Lección 12: Comparativos": {
        "teoría": """Se usan para comparar dos cosas.
- Adjetivos cortos: adjetivo + '-er' + 'than' (taller than).
- Adjetivos largos: 'more' + adjetivo + 'than' (more beautiful than).""",
        "ejemplo": "He is taller than his brother. (Él es más alto que su hermano.)",
        "pregunta": "El comparativo de 'expensive' es:",
        "opciones": ["expensiver", "more expensive", "the most expensive"],
        "respuesta_correcta": "more expensive"
    },
    "Lección 13: Superlativos": {
        "teoría": """Se usan para comparar una cosa con un grupo.
- Adjetivos cortos: 'the' + adjetivo + '-est' (the tallest).
- Adjetivos largos: 'the most' + adjetivo (the most beautiful).""",
        "ejemplo": "She is the fastest runner. (Ella es la corredora más rápida.)",
        "pregunta": "El superlativo de 'big' es:",
        "opciones": ["the biger", "the most big", "the biggest"],
        "respuesta_correcta": "the biggest"
    },
    "Lección 14: Adverbios de Frecuencia": {
        "teoría": """Adverbios como 'always', 'usually', 'often', 'sometimes' y 'never' indican con qué frecuencia ocurre algo.
Generalmente se colocan antes del verbo principal, pero después del verbo 'to be'.
Ejemplos:
- I always eat breakfast.
- He is always on time.""",
        "ejemplo": "We often go to the park. (A menudo vamos al parque.)",
        "pregunta": "Selecciona la oración correcta:",
        "opciones": ["She never is late.", "She is never late.", "She is late never."],
        "respuesta_correcta": "She is never late."
    },
    "Lección 15: Presente Perfecto": {
        "teoría": """El presente perfecto se usa para acciones que comenzaron en el pasado y continúan en el presente, o para experiencias pasadas. Se forma con 'have/has' + participio pasado del verbo.
Ejemplos:
- I have lived here for ten years.
- She has visited Paris.""",
        "ejemplo": "I have seen that movie. (He visto esa película.)",
        "pregunta": "La forma correcta de 'to eat' en presente perfecto para 'he' es:",
        "opciones": ["he has eat", "he have eaten", "he has eaten"],
        "respuesta_correcta": "he has eaten"
    },
    "Lección 16: Preposiciones de Lugar (in, on, at)": {
        "teoría": """'In' se usa para lugares grandes (países, ciudades), 'on' para superficies y 'at' para puntos específicos o direcciones.
Ejemplos:
- in a box (dentro de una caja)
- on the table (sobre la mesa)
- at the station (en la estación)""",
        "ejemplo": "The keys are on the table. (Las llaves están en la mesa.)",
        "pregunta": "La preposición correcta para 'the garden' es:",
        "opciones": ["on", "at", "in"],
        "respuesta_correcta": "in"
    },
    "Lección 17: 'Some' y 'Any'": {
        "teoría": """'Some' se usa en oraciones afirmativas con sustantivos contables y no contables.
'Any' se usa en oraciones negativas e interrogativas.""",
        "ejemplo": "I have some money, but I don't have any coins.",
        "pregunta": "La palabra correcta para 'Do you have _____ questions?' es:",
        "opciones": ["some", "any", "a"],
        "respuesta_correcta": "any"
    },
    "Lección 18: 'Much' y 'Many'": {
        "teoría": """'Much' se usa con sustantivos no contables (much money).
'Many' se usa con sustantivos contables en plural (many books).""",
        "ejemplo": "I don't have much time, but I have many friends.",
        "pregunta": "¿Qué palabra es correcta para 'I don't drink _____ coffee?'",
        "opciones": ["many", "a", "much"],
        "respuesta_correcta": "much"
    },
    "Lección 19: Presente Simple Interrogativo": {
        "teoría": """Para formar preguntas en presente simple, usamos 'do' o 'does' al principio de la oración.
- 'Do' para I, you, we, they.
- 'Does' para he, she, it.""",
        "ejemplo": "Do you like coffee? (¿Te gusta el café?)",
        "pregunta": "Selecciona la forma correcta para 'she':",
        "opciones": ["Does she like?", "Do she like?", "Does she likes?"],
        "respuesta_correcta": "Does she like?"
    },
    "Lección 20: Pretérito Perfecto Continuo": {
        "teoría": """Se usa para acciones que comenzaron en el pasado, han estado ocurriendo por un tiempo y sus resultados son visibles ahora. Se forma con 'have/has been' + verbo con '-ing'.
Ejemplo:
- I have been studying all night. (He estado estudiando toda la noche.)""",
        "ejemplo": "She has been working since 8 AM. (Ella ha estado trabajando desde las 8 AM.)",
        "pregunta": "La forma correcta de 'to wait' en presente perfecto continuo para 'we' es:",
        "opciones": ["we have been waited", "we have been waiting", "we has been waiting"],
        "respuesta_correcta": "we have been waiting"
    },
    "Lección 21: Los Pronombres Personales (Sujeto)": {
        "teoría": """Los pronombres personales de sujeto reemplazan a los sustantivos que realizan la acción en una oración.
- I, you, he, she, it, we, they.""",
        "ejemplo": "She is a doctor. (Ella es una doctora.)",
        "pregunta": "¿Qué pronombre reemplaza a 'The cats'?",
        "opciones": ["it", "they", "we"],
        "respuesta_correcta": "they"
    },
    "Lección 22: Los Pronombres Objeto": {
        "teoría": """Los pronombres objeto reemplazan a los sustantivos que reciben la acción en una oración.
- me, you, him, her, it, us, them.""",
        "ejemplo": "She gave the book to him. (Ella le dio el libro a él.)",
        "pregunta": "El pronombre objeto para 'the children' es:",
        "opciones": ["him", "them", "us"],
        "respuesta_correcta": "them"
    },
    "Lección 23: Los Pronombres Demostrativos": {
        "teoría": """Se usan para señalar cosas o personas.
- 'this' (esto/este) y 'these' (estos) para cosas cercanas.
- 'that' (eso/ese) y 'those' (esos) para cosas lejanas.""",
        "ejemplo": "This is my house. (Esta es mi casa.)",
        "pregunta": "¿Qué pronombre es correcto para 'flowers' (lejos)?",
        "opciones": ["this", "those", "that"],
        "respuesta_correcta": "those"
    },
    "Lección 24: Preposiciones de Movimiento": {
        "teoría": """Se usan para indicar dirección.
- 'to' para un destino (to school).
- 'from' para un origen (from home).
- 'into' para entrar en algo (into the room).""",
        "ejemplo": "He went to the store. (Él fue a la tienda.)",
        "pregunta": "¿Qué preposición es correcta para 'go _____ the house'?",
        "opciones": ["on", "into", "at"],
        "respuesta_correcta": "into"
    },
    "Lección 25: Pasado Simple Negativo": {
        "teoría": """Se forma con 'did not' (o 'didn't') + la forma base del verbo.
Ejemplos:
- I did not go.
- She didn't like it.""",
        "ejemplo": "They didn't see the movie. (Ellos no vieron la película.)",
        "pregunta": "La forma correcta de 'to eat' en pasado simple negativo para 'he' es:",
        "opciones": ["he didn't ate", "he didn't eat", "he no eat"],
        "respuesta_correcta": "he didn't eat"
    },
    "Lección 26: Pasado Simple Interrogativo": {
        "teoría": """Se forma con 'did' + sujeto + forma base del verbo.
Ejemplo:
- Did you call me? (¿Me llamaste?)""",
        "ejemplo": "Did she finish her homework? (¿Ella terminó su tarea?)",
        "pregunta": "La forma correcta para 'they' es:",
        "opciones": ["Did they went?", "Did they go?", "Did they going?"],
        "respuesta_correcta": "Did they go?"
    },
    "Lección 27: Presente Simple Negativo": {
        "teoría": """Se forma con 'do not' (don't) o 'does not' (doesn't) + la forma base del verbo.
- 'Don't' para I, you, we, they.
- 'Doesn't' para he, she, it.""",
        "ejemplo": "She doesn't like coffee. (A ella no le gusta el café.)",
        "pregunta": "La forma correcta de 'to read' para 'we' es:",
        "opciones": ["we doesn't read", "we don't read", "we not read"],
        "respuesta_correcta": "we don't read"
    },
    "Lección 28: Verbos Modales 'can' y 'could' (Negativo)": {
        "teoría": """Se usa 'cannot' (can't) o 'could not' (couldn't) para negar habilidad.
Ejemplos:
- I can't swim. (No puedo nadar.)
- We couldn't hear him. (No podíamos escucharlo.)""",
        "ejemplo": "He can't speak Spanish. (Él no puede hablar español.)",
        "pregunta": "La forma negativa correcta para 'you can go' es:",
        "opciones": ["you cannot go", "you not can go", "you can not to go"],
        "respuesta_correcta": "you cannot go"
    },
    "Lección 29: El Primer Condicional": {
        "teoría": """Se usa para situaciones reales o posibles en el futuro.
Estructura: 'If' + presente simple, 'will' + verbo base.
Ejemplo:
- If it rains, I will stay home. (Si llueve, me quedaré en casa.)""",
        "ejemplo": "If you study, you will pass the exam.",
        "pregunta": "La oración que usa el primer condicional correctamente es:",
        "opciones": ["If I will go, I will call you.", "If I go, I will call you.", "If I go, I call you."],
        "respuesta_correcta": "If I go, I will call you."
    },
    "Lección 30: El Segundo Condicional": {
        "teoría": """Se usa para situaciones hipotéticas o irreales en el presente o futuro.
Estructura: 'If' + pasado simple, 'would' + verbo base.
Ejemplo:
- If I had a million dollars, I would travel the world.""",
        "ejemplo": "If I were you, I would take the job.",
        "pregunta": "La oración que usa el segundo condicional correctamente es:",
        "opciones": ["If I have money, I would buy a car.", "If I had money, I would buy a car.", "If I had money, I will buy a car."],
        "respuesta_correcta": "If I had money, I would buy a car."
    },
    "Lección 31: El Tercer Condicional": {
        "teoría": """Se usa para situaciones hipotéticas en el pasado, a menudo para expresar arrepentimiento.
Estructura: 'If' + pasado perfecto, 'would have' + participio pasado.
Ejemplo:
- If I had studied, I would have passed the exam.""",
        "ejemplo": "If she had left earlier, she wouldn't have missed the bus.",
        "pregunta": "La oración que usa el tercer condicional correctamente es:",
        "opciones": ["If I would have known, I had called you.", "If I would have known, I would have called you.", "If I had known, I would have called you."],
        "respuesta_correcta": "If I had known, I would have called you."
    },
    "Lección 32: 'Used to'": {
        "teoría": """'Used to' se usa para hablar de hábitos o estados en el pasado que ya no son verdaderos.
Ejemplo:
- I used to live in Paris. (Yo solía vivir en París.)""",
        "ejemplo": "She used to play the piano. (Ella solía tocar el piano.)",
        "pregunta": "Selecciona la forma negativa correcta:",
        "opciones": ["I didn't used to smoke.", "I didn't use to smoke.", "I not used to smoke."],
        "respuesta_correcta": "I didn't use to smoke."
    },
    "Lección 33: 'Going to' para Futuro": {
        "teoría": """'Going to' se usa para planes futuros, intenciones y predicciones basadas en evidencia presente. Se forma con 'to be' + 'going to' + verbo base.
Ejemplo:
- I am going to visit my friends. (Voy a visitar a mis amigos.)""",
        "ejemplo": "It's going to rain. (Va a llover.)",
        "pregunta": "La forma correcta de 'to buy' para 'they' es:",
        "opciones": ["they are going buy", "they go to buy", "they are going to buy"],
        "respuesta_correcta": "they are going to buy"
    },
    "Lección 34: El Imperativo": {
        "teoría": """Se usa para dar órdenes, instrucciones o sugerencias. La forma es el verbo base, sin sujeto.
Ejemplo:
- Be quiet! (¡Cállate!)
- Open the door. (Abre la puerta.)""",
        "ejemplo": "Please, pass me the salt. (Por favor, pásame la sal.)",
        "pregunta": "Selecciona la oración imperativa correcta:",
        "opciones": ["You stop talking.", "Stop talking.", "Stops talking."],
        "respuesta_correcta": "Stop talking."
    },
    "Lección 35: Pronombres Reflexivos": {
        "teoría": """Se usan cuando el sujeto y el objeto de una oración son la misma persona o cosa.
- myself, yourself, himself, herself, itself, ourselves, yourselves, themselves.""",
        "ejemplo": "He hurt himself. (Él se lastimó a sí mismo.)",
        "pregunta": "¿Qué pronombre reflexivo es correcto para 'we'?",
        "opciones": ["themselves", "ourselves", "yourself"],
        "respuesta_correcta": "ourselves"
    },
    "Lección 36: Adjetivos y Adverbios": {
        "teoría": """Los adjetivos describen sustantivos. Los adverbios describen verbos, adjetivos u otros adverbios.
La mayoría de los adverbios se forman agregando '-ly' a un adjetivo.
Ejemplos:
- She is a fast runner. (adjetivo)
- She runs fast. (adverbio, irregular)
- He is a slow driver. (adjetivo)
- He drives slowly. (adverbio)""",
        "ejemplo": "He sings beautifully. (Él canta bellamente.)",
        "pregunta": "El adverbio de 'quick' es:",
        "opciones": ["quick", "quickly", "quicklier"],
        "respuesta_correcta": "quickly"
    },
    "Lección 37: Pasado Perfecto": {
        "teoría": """El pasado perfecto se usa para una acción que ocurrió antes de otra acción en el pasado. Se forma con 'had' + participio pasado.
Ejemplo:
- I had already eaten when she arrived.""",
        "ejemplo": "She had finished her homework before she went out. (Ella había terminado su tarea antes de salir.)",
        "pregunta": "La forma correcta de 'to leave' para 'we' es:",
        "opciones": ["we had leaved", "we have left", "we had left"],
        "respuesta_correcta": "we had left"
    },
    "Lección 38: Pasivo (Presente Simple)": {
        "teoría": """Se usa para enfocar la acción en el objeto, no en el sujeto. Se forma con el verbo 'to be' en presente + participio pasado.
Ejemplo:
- The book is written by him. (El libro es escrito por él.)""",
        "ejemplo": "English is spoken all over the world. (El inglés es hablado en todo el mundo.)",
        "pregunta": "La forma pasiva correcta de 'They make cars' es:",
        "opciones": ["Cars are made by them.", "Cars is made by them.", "Cars are make by them."],
        "respuesta_correcta": "Cars are made by them."
    },
    "Lección 39: Pasivo (Pasado Simple)": {
        "teoría": """Se forma con el verbo 'to be' en pasado (was/were) + participio pasado.
Ejemplo:
- The car was repaired. (El coche fue reparado.)""",
        "ejemplo": "The house was built in 1990. (La casa fue construida en 1990.)",
        "pregunta": "La forma pasiva correcta de 'She wrote the letter' es:",
        "opciones": ["The letter was wrote by her.", "The letter was written by her.", "The letter were written by her."],
        "respuesta_correcta": "The letter was written by her."
    },
    "Lección 40: Los Gerundios e Infinitivos": {
        "teoría": """El gerundio es la forma del verbo que termina en '-ing' y funciona como un sustantivo. El infinitivo es 'to' + el verbo base.
Ejemplos:
- I like swimming. (gerundio)
- I want to swim. (infinitivo)""",
        "ejemplo": "She enjoys reading. (Ella disfruta leyendo.)",
        "pregunta": "La forma correcta de 'to learn' en 'I decided _____ English' es:",
        "opciones": ["learning", "to learn", "learn"],
        "respuesta_correcta": "to learn"
    },
    "Lección 41: 'Since' y 'For'": {
        "teoría": """Se usan para indicar duración de tiempo.
- 'For' se usa para un periodo de tiempo (for two hours).
- 'Since' se usa para un punto de inicio en el pasado (since Monday).""",
        "ejemplo": "He has been here since 9 AM. (Ha estado aquí desde las 9 AM.)",
        "pregunta": "¿Qué palabra es correcta para 'I have lived here _____ ten years'?",
        "opciones": ["since", "for", "in"],
        "respuesta_correcta": "for"
    },
    "Lección 42: Sustantivos Contables y No Contables": {
        "teoría": """Los sustantivos contables se pueden contar y tienen forma plural. Los no contables no se pueden contar y no tienen forma plural.
Ejemplos:
- Contable: apple, books, cars.
- No contable: water, money, information.""",
        "ejemplo": "She has many books and much information.",
        "pregunta": "¿Cuál de los siguientes es un sustantivo no contable?",
        "opciones": ["chair", "table", "water"],
        "respuesta_correcta": "water"
    },
    "Lección 43: 'Little' y 'Few'": {
        "teoría": """'Little' se usa con sustantivos no contables (little water).
'Few' se usa con sustantivos contables en plural (few books).""",
        "ejemplo": "I have little time and few friends.",
        "pregunta": "¿Qué palabra es correcta para 'She has very _____ money.'?",
        "opciones": ["few", "little", "many"],
        "respuesta_correcta": "little"
    },
    "Lección 44: 'So' y 'Because'": {
        "teoría": """'So' (entonces/por lo tanto) se usa para expresar un resultado o efecto.
'Because' (porque) se usa para dar una razón.
Ejemplos:
- It was cold, so I wore a jacket. (Era frío, por lo tanto, usé una chaqueta.)
- I wore a jacket because it was cold. (Usé una chaqueta porque era frío.)""",
        "ejemplo": "I was hungry, so I ate a sandwich.",
        "pregunta": "La palabra correcta para 'He was late _____ the bus was delayed' es:",
        "opciones": ["so", "because", "but"],
        "respuesta_correcta": "because"
    },
    "Lección 45: Preguntas con 'Wh'": {
        "teoría": """Se usan para obtener información específica.
- who (quién), what (qué), when (cuándo), where (dónde), why (por qué), how (cómo).
Generalmente van al principio de la pregunta.""",
        "ejemplo": "Where are you from? (¿De dónde eres?)",
        "pregunta": "¿Qué palabra es correcta para '_____ did you go?' para preguntar por un lugar?",
        "opciones": ["What", "When", "Where"],
        "respuesta_correcta": "Where"
    },
    "Lección 46: Voz Pasiva (Futuro Simple)": {
        "teoría": """Se forma con 'will be' + participio pasado.
Ejemplo:
- The work will be finished tomorrow. (El trabajo será terminado mañana.)""",
        "ejemplo": "The new hospital will be built next year. (El nuevo hospital será construido el próximo año.)",
        "pregunta": "La forma pasiva correcta de 'They will send the email' es:",
        "opciones": ["The email will be sended.", "The email will be sent.", "The email is going to be sent."],
        "respuesta_correcta": "The email will be sent."
    },
    "Lección 47: 'Have to' y 'Must'": {
        "teoría": """Ambos se usan para expresar obligación, pero tienen una diferencia sutil.
- 'Must' expresa una obligación personal o fuerte (I must go).
- 'Have to' expresa una obligación externa o una regla (I have to wear a uniform).""",
        "ejemplo": "You must be quiet in the library. (Debes estar en silencio en la biblioteca.)",
        "pregunta": "Selecciona la oración correcta:",
        "opciones": ["I must to go.", "She has to study.", "You must studying."],
        "respuesta_correcta": "She has to study."
    },
    "Lección 48: Preposiciones de Causa y Efecto": {
        "teoría": """Se usan para conectar una causa con su resultado.
- 'because of' (debido a) y 'due to' (debido a) seguidos por un sustantivo.
Ejemplos:
- We stayed home because of the rain.""",
        "ejemplo": "The game was canceled due to bad weather. (El juego fue cancelado debido al mal tiempo.)",
        "pregunta": "La palabra correcta para 'He couldn't sleep _____ the noise' es:",
        "opciones": ["so", "because of", "due to"],
        "respuesta_correcta": "because of"
    },
    "Lección 49: 'Can', 'Could' y 'Be able to'": {
        "teoría": """Todos expresan habilidad. 'Be able to' es más formal y se usa cuando 'can' y 'could' no tienen una forma verbal para el tiempo verbal.
Ejemplo:
- I will be able to go. (Podré ir.)""",
        "ejemplo": "She could swim when she was five. (Ella podía nadar cuando tenía cinco años.)",
        "pregunta": "La forma correcta de 'to be able to' para 'he' en futuro es:",
        "opciones": ["he can able to", "he will can", "he will be able to"],
        "respuesta_correcta": "he will be able to"
    },
    "Lección 50: Preguntas con 'How'": {
        "teoría": """'How' se usa para preguntar sobre la manera, el estado o la cantidad.
- How (cómo), How much (cuánto), How many (cuántos), How long (cuánto tiempo).""",
        "ejemplo": "How much is this book? (¿Cuánto cuesta este libro?)",
        "pregunta": "La palabra correcta para '_____ friends do you have?' es:",
        "opciones": ["How much", "How", "How many"],
        "respuesta_correcta": "How many"
    },
    "Lección 51: 'Still', 'Yet' y 'Already'": {
        "teoría": """'Still' (aún) indica que una acción continúa.
'Yet' (aún, todavía) se usa en oraciones negativas e interrogativas para algo que no ha sucedido.
'Already' (ya) indica que algo ha sucedido antes de lo esperado.""",
        "ejemplo": "I have already finished my homework. (Ya he terminado mi tarea.)",
        "pregunta": "La palabra correcta para 'Is the food ready _____?' es:",
        "opciones": ["already", "yet", "still"],
        "respuesta_correcta": "yet"
    },
    "Lección 52: 'Both' y 'Either'": {
        "teoría": """'Both' (ambos) se usa para referirse a dos personas o cosas.
'Either' (cualquiera de los dos) se usa para una elección entre dos opciones.""",
        "ejemplo": "Both of them are good students. (Ambos son buenos estudiantes.)",
        "pregunta": "La palabra correcta para 'You can choose _____ chocolate or vanilla' es:",
        "opciones": ["both", "either", "neither"],
        "respuesta_correcta": "either"
    },
    "Lección 53: Voz Pasiva (Presente Perfecto)": {
        "teoría": """Se forma con 'have/has been' + participio pasado.
Ejemplo:
- The letter has been sent. (La carta ha sido enviada.)""",
        "ejemplo": "The house has been painted. (La casa ha sido pintada.)",
        "pregunta": "La forma pasiva correcta de 'They have built a new school' es:",
        "opciones": ["A new school has been built.", "A new school have been built.", "A new school has built."],
        "respuesta_correcta": "A new school has been built."
    },
    "Lección 54: Pronombres Relativos (who, which, that)": {
        "teoría": """Se usan para unir dos oraciones o dar más información sobre un sustantivo.
- 'who' para personas, 'which' para cosas, 'that' para ambos.
Ejemplo:
- This is the man who helped me.""",
        "ejemplo": "This is the book that I bought. (Este es el libro que compré.)",
        "pregunta": "La palabra correcta para 'The woman _____ is a doctor lives here' es:",
        "opciones": ["which", "that", "what"],
        "respuesta_correcta": "that"
    },
    "Lección 55: Infinitivos (con 'to')": {
        "teoría": """Se usa el infinitivo con 'to' después de ciertos verbos, como 'want', 'need', 'plan', 'decide'.
Ejemplo:
- I want to go home. (Quiero ir a casa.)""",
        "ejemplo": "She needs to buy a new car. (Ella necesita comprar un coche nuevo.)",
        "pregunta": "La forma correcta de 'to call' en 'I plan _____ you tomorrow' es:",
        "opciones": ["calling", "to call", "call"],
        "respuesta_correcta": "to call"
    },
    "Lección 56: Gerundios (sin 'to')": {
        "teoría": """Se usa el gerundio después de ciertos verbos, como 'enjoy', 'finish', 'mind', 'avoid'.
Ejemplo:
- I enjoy reading. (Disfruto leyendo.)""",
        "ejemplo": "He finished working. (Él terminó de trabajar.)",
        "pregunta": "La forma correcta de 'to sing' en 'She avoids _____ in public' es:",
        "opciones": ["singing", "to sing", "sing"],
        "respuesta_correcta": "singing"
    },
    "Lección 57: Adjetivos con '-ed' y '-ing'": {
        "teoría": """Los adjetivos con '-ed' describen una emoción sentida por alguien (I am bored).
Los adjetivos con '-ing' describen la causa de la emoción (This movie is boring).""",
        "ejemplo": "The story was interesting. I was interested. (La historia fue interesante. Yo estaba interesado.)",
        "pregunta": "La palabra correcta para 'I am very _____ with the results' es:",
        "opciones": ["satisfied", "satisfying", "satisfies"],
        "respuesta_correcta": "satisfied"
    },
    "Lección 58: Preposiciones de Tiempo 'in' y 'on' (días y meses)": {
        "teoría": """'In' para meses y años. 'On' para días específicos y fechas.
Ejemplos:
- I was born in July.
- I was born on July 25th.""",
        "ejemplo": "My birthday is on Friday. (Mi cumpleaños es el viernes.)",
        "pregunta": "La preposición correcta para '_____ 2025' es:",
        "opciones": ["on", "at", "in"],
        "respuesta_correcta": "in"
    },
    "Lección 59: Pasivo (futuro con 'going to')": {
        "teoría": """Se forma con 'to be going to be' + participio pasado.
Ejemplo:
- The report is going to be published tomorrow. (El reporte va a ser publicado mañana.)""",
        "ejemplo": "A new bridge is going to be built. (Un nuevo puente va a ser construido.)",
        "pregunta": "La forma pasiva correcta de 'They are going to close the store' es:",
        "opciones": ["The store is going to close.", "The store is going to be closed.", "The store will be closed."],
        "respuesta_correcta": "The store is going to be closed."
    },
    "Lección 60: 'Another' y 'Other'": {
        "teoría": """'Another' (otro/a) se usa con sustantivos singulares contables.
'Other' (otro/s/a/as) se usa con sustantivos plurales o no contables.""",
        "ejemplo": "I need another cup of coffee. (Necesito otra taza de café.)",
        "pregunta": "La palabra correcta para 'I have _____ friends' es:",
        "opciones": ["another", "other", "a"],
        "respuesta_correcta": "other"
    },
    "Lección 61: 'Neither...nor' y 'Either...or'": {
        "teoría": """'Either...or' (o...o) se usa para una elección entre dos opciones.
'Neither...nor' (ni...ni) se usa para negar dos opciones.
Ejemplo:
- You can either walk or take a bus.
- I like neither coffee nor tea.""",
        "ejemplo": "Neither my brother nor my sister can sing. (Ni mi hermano ni mi hermana pueden cantar.)",
        "pregunta": "La forma correcta para 'He likes _____ chocolate _____ vanilla.' es:",
        "opciones": ["neither, nor", "either, nor", "neither, or"],
        "respuesta_correcta": "neither, nor"
    },
    "Lección 62: Verbos con 'to' y sin 'to'": {
        "teoría": """Algunos verbos como 'make', 'let' y 'help' son seguidos por un verbo sin 'to'.
Ejemplos:
- She made me laugh. (Ella me hizo reír.)
- Let me go. (Déjame ir.)""",
        "ejemplo": "My parents let me go out. (Mis padres me dejaron salir.)",
        "pregunta": "La forma correcta de 'to cry' en 'He made me _____' es:",
        "opciones": ["to cry", "crying", "cry"],
        "respuesta_correcta": "cry"
    },
    "Lección 63: Pasivo (Verbos Modales)": {
        "teoría": """Se forma con verbo modal + 'be' + participio pasado.
Ejemplo:
- The door should be locked. (La puerta debería estar cerrada.)""",
        "ejemplo": "This problem can be solved. (Este problema puede ser resuelto.)",
        "pregunta": "La forma pasiva correcta de 'You must do your homework' es:",
        "opciones": ["Your homework must be doing.", "Your homework must be done.", "Your homework must is done."],
        "respuesta_correcta": "Your homework must be done."
    },
    "Lección 64: 'To' y 'For'": {
        "teoría": """'To' se usa para indicar un destino (I go to the store).
'For' se usa para indicar un propósito o beneficio (This gift is for you).""",
        "ejemplo": "I bought a present for my friend. (Compré un regalo para mi amigo.)",
        "pregunta": "La preposición correcta para 'I gave the book _____ him' es:",
        "opciones": ["for", "to", "at"],
        "respuesta_correcta": "to"
    },
    "Lección 65: Pronombres Recíprocos": {
        "teoría": """Se usan para indicar que dos o más personas están haciendo lo mismo mutuamente.
- 'each other' (el uno al otro) y 'one another' (unos a otros).
Ejemplo:
- They love each other.""",
        "ejemplo": "We gave each other presents. (Nos dimos regalos el uno al otro.)",
        "pregunta": "La forma correcta para 'The students helped _____ with the homework' es:",
        "opciones": ["each other", "one another", "all"],
        "respuesta_correcta": "each other"
    },
    "Lección 66: 'So' y 'Such'": {
        "teoría": """'So' (tan) se usa antes de un adjetivo o adverbio (so beautiful).
'Such' (tan, tal) se usa antes de 'a/an' + adjetivo + sustantivo (such a beautiful day).""",
        "ejemplo": "It was so cold. It was such a cold day. (Hacía tanto frío. Fue un día tan frío.)",
        "pregunta": "La palabra correcta para 'It was _____ an easy test.' es:",
        "opciones": ["so", "such", "too"],
        "respuesta_correcta": "such"
    },
    "Lección 67: 'Too' y 'Enough'": {
        "teoría": """'Too' (demasiado) se usa antes de adjetivos o adverbios y tiene un sentido negativo.
'Enough' (suficiente) se usa después de adjetivos o adverbios, o antes de sustantivos.
Ejemplos:
- It's too hot.
- I am old enough to drive.
- I have enough money.""",
        "ejemplo": "This car is too expensive. (Este coche es demasiado caro.)",
        "pregunta": "La palabra correcta para 'The coat isn't warm _____.' es:",
        "opciones": ["too", "enough", "so"],
        "respuesta_correcta": "enough"
    },
    "Lección 68: Reportado (Presente Simple)": {
        "teoría": """Para reportar lo que alguien dijo, se cambia el tiempo verbal. El presente simple se convierte en pasado simple.
Ejemplo:
- He said, 'I am happy.' -> He said that he was happy.""",
        "ejemplo": "She said she liked to sing. (Ella dijo que le gustaba cantar.)",
        "pregunta": "La forma reportada correcta de 'I work here' es:",
        "opciones": ["He said that he worked there.", "He said that he works here.", "He said that he worked here."],
        "respuesta_correcta": "He said that he worked there."
    },
    "Lección 69: Reportado (Pasado Simple)": {
        "teoría": """El pasado simple se convierte en pasado perfecto.
Ejemplo:
- He said, 'I went to the store.' -> He said that he had gone to the store.""",
        "ejemplo": "She said she had seen a ghost. (Ella dijo que había visto un fantasma.)",
        "pregunta": "La forma reportada correcta de 'I bought a car' es:",
        "opciones": ["He said he bought a car.", "He said he had bought a car.", "He said he was buying a car."],
        "respuesta_correcta": "He said he had bought a car."
    },
    "Lección 70: Preguntas con 'How long'": {
        "teoría": """'How long' se usa para preguntar sobre la duración de una acción.
Ejemplo:
- How long have you been studying? (¿Cuánto tiempo has estado estudiando?)""",
        "ejemplo": "How long does it take to get there? (¿Cuánto tiempo toma llegar allí?)",
        "pregunta": "La pregunta correcta para 'duración' de vivir en un lugar es:",
        "opciones": ["How long did you live here?", "How long you live here?", "How long have you lived here?"],
        "respuesta_correcta": "How long have you lived here?"
    },
    "Lección 71: Adjetivos de Opinión": {
        "teoría": """Cuando se usan varios adjetivos, el de opinión va primero.
Ejemplo:
- a beautiful red dress (un vestido rojo hermoso)
- a wonderful old house (una casa vieja maravillosa)""",
        "ejemplo": "He bought a new blue car. (Él compró un coche nuevo azul.)",
        "pregunta": "La forma correcta de 'a small, beautiful, wooden table' es:",
        "opciones": ["a wooden small beautiful table", "a beautiful small wooden table", "a small wooden beautiful table"],
        "respuesta_correcta": "a beautiful small wooden table"
    },
    "Lección 72: Verbos Estativos y de Acción": {
        "teoría": """Los verbos de acción describen una acción física o mental (run, eat, think).
Los verbos estativos describen un estado o condición (know, love, believe) y no se usan en formas continuas.
Ejemplo:
- I am knowing the answer. (incorrecto)
- I know the answer. (correcto)""",
        "ejemplo": "I love this song. (Amo esta canción.)",
        "pregunta": "El verbo que no se puede usar en presente continuo es:",
        "opciones": ["walking", "running", "loving"],
        "respuesta_correcta": "loving"
    },
    "Lección 73: 'Used to' (Negativo e Interrogativo)": {
        "teoría": """Forma negativa: 'didn't use to'.
Forma interrogativa: 'did... use to'.
Ejemplos:
- I didn't use to like it.
- Did you use to play video games?""",
        "ejemplo": "She didn't use to live here. (Ella no solía vivir aquí.)",
        "pregunta": "La forma interrogativa correcta de 'He used to smoke' es:",
        "opciones": ["Used he to smoke?", "Did he used to smoke?", "Did he use to smoke?"],
        "respuesta_correcta": "Did he use to smoke?"
    },
    "Lección 74: 'Would' (para hábitos pasados)": {
        "teoría": """'Would' se puede usar para hablar de hábitos o acciones repetidas en el pasado, similar a 'used to', pero solo con verbos de acción.
Ejemplo:
- We would go to the beach every summer. (Solíamos ir a la playa cada verano.)""",
        "ejemplo": "My grandfather would tell us stories. (Mi abuelo solía contarnos historias.)",
        "pregunta": "La forma correcta de 'to play' en 'We _____ every weekend' (hábito pasado) es:",
        "opciones": ["used to playing", "would play", "would to play"],
        "respuesta_correcta": "would play"
    },
    "Lección 75: Pasado Perfecto Continuo": {
        "teoría": """Se usa para una acción que estuvo en progreso por un tiempo antes de otra acción en el pasado. Se forma con 'had been' + verbo con '-ing'.
Ejemplo:
- He had been running for an hour when he collapsed.""",
        "ejemplo": "She had been waiting for two hours when he arrived. (Ella había estado esperando por dos horas cuando él llegó.)",
        "pregunta": "La forma correcta de 'to sleep' en pasado perfecto continuo para 'they' es:",
        "opciones": ["they had sleeping", "they have been sleeping", "they had been sleeping"],
        "respuesta_correcta": "they had been sleeping"
    },
    "Lección 76: 'As...as' (Comparación)": {
        "teoría": """Se usa para comparar dos cosas que son iguales. La estructura es 'as' + adjetivo/adverbio + 'as'.
Ejemplo:
- She is as tall as her brother. (Ella es tan alta como su hermano.)""",
        "ejemplo": "He runs as fast as me. (Él corre tan rápido como yo.)",
        "pregunta": "La forma correcta para 'The car is not _____ fast _____ the train' es:",
        "opciones": ["as, as", "so, as", "as, than"],
        "respuesta_correcta": "as, as"
    },
    "Lección 77: Adjetivos Numerales": {
        "teoría": """Se usan para indicar una cantidad exacta (cardinales) o un orden (ordinales).
- Cardinales: one, two, three.
- Ordinales: first, second, third.""",
        "ejemplo": "I have two sisters. This is my first time here. (Tengo dos hermanas. Esta es mi primera vez aquí.)",
        "pregunta": "El número ordinal para 'four' es:",
        "opciones": ["four", "fourth", "fourt"],
        "respuesta_correcta": "fourth"
    },
    "Lección 78: 'So' y 'Neither' (para acuerdos)": {
        "teoría": """'So' + auxiliar + sujeto se usa para estar de acuerdo con una declaración positiva.
'Neither' + auxiliar + sujeto se usa para estar de acuerdo con una declaración negativa.
Ejemplo:
- I like pizza. So do I.
- I don't like coffee. Neither do I.""",
        "ejemplo": "He is a student. So am I. (Él es un estudiante. Yo también.)",
        "pregunta": "La respuesta correcta para 'I didn't go to the party.' es:",
        "opciones": ["So did I.", "Neither did I.", "I did too."],
        "respuesta_correcta": "Neither did I."
    },
    "Lección 79: 'Used to' vs 'Be used to'": {
        "teoría": """'Used to' se refiere a un hábito en el pasado.
'Be used to' (estar acostumbrado a) se refiere a algo que ya es normal.
Se forma con 'to be' + 'used to' + verbo con '-ing'.
Ejemplo:
- I used to live in Spain.
- I am used to living in Spain.""",
        "ejemplo": "She is used to driving on the left. (Ella está acostumbrada a conducir por la izquierda.)",
        "pregunta": "La forma correcta para 'He is used to _____ up early.' es:",
        "opciones": ["get", "getting", "got"],
        "respuesta_correcta": "getting"
    },
    "Lección 80: 'Look', 'Look like', 'Look like a'": {
        "teoría": """'Look' (lucir, verse) se usa con adjetivos.
'Look like' se usa con sustantivos o cláusulas.
Ejemplos:
- He looks happy.
- He looks like his father.
- He looks like a movie star.""",
        "ejemplo": "She looks like her mother. (Ella se parece a su madre.)",
        "pregunta": "La forma correcta para 'It _____ a beautiful day.' es:",
        "opciones": ["looks like", "looks", "look"],
        "respuesta_correcta": "looks like"
    },
    "Lección 81: El Futuro Continuo": {
        "teoría": """Se usa para una acción que estará en progreso en un momento específico en el futuro. Se forma con 'will be' + verbo con '-ing'.
Ejemplo:
- At 3 PM, I will be working. (A las 3 PM, estaré trabajando.)""",
        "ejemplo": "He will be sleeping at midnight. (Él estará durmiendo a medianoche.)",
        "pregunta": "La forma correcta de 'to travel' para 'we' es:",
        "opciones": ["we will traveling", "we will be traveling", "we are traveling"],
        "respuesta_correcta": "we will be traveling"
    },
    "Lección 82: El Futuro Perfecto": {
        "teoría": """Se usa para una acción que se completará antes de un momento específico en el futuro. Se forma con 'will have' + participio pasado.
Ejemplo:
- By next month, I will have finished the project.""",
        "ejemplo": "They will have arrived by 7 PM. (Ellos habrán llegado a las 7 PM.)",
        "pregunta": "La forma correcta de 'to complete' para 'she' es:",
        "opciones": ["she will has completed", "she will have complete", "she will have completed"],
        "respuesta_correcta": "she will have completed"
    },
    "Lección 83: 'Hardly', 'Scarcely', 'Barely'": {
        "teoría": """Estos adverbios tienen un significado de 'apenas' o 'casi no' y se usan para indicar que algo fue difícil de hacer. Se colocan antes del verbo.
Ejemplo:
- I could hardly see anything.""",
        "ejemplo": "She had barely started when the phone rang. (Ella apenas había empezado cuando el teléfono sonó.)",
        "pregunta": "La palabra correcta para 'He could _____ hear me.' es:",
        "opciones": ["very", "easily", "hardly"],
        "respuesta_correcta": "hardly"
    },
    "Lección 84: 'Unless' y 'If'": {
        "teoría": """'Unless' (a menos que) tiene el mismo significado que 'if not'.
Ejemplo:
- You will be late if you don't hurry.
- You will be late unless you hurry.""",
        "ejemplo": "I won't go unless it's a sunny day. (No iré a menos que sea un día soleado.)",
        "pregunta": "La palabra correcta para 'We will fail _____ we study.' es:",
        "opciones": ["if", "unless", "when"],
        "respuesta_correcta": "unless"
    },
    "Lección 85: Verbos Seguidos de Infinitivos": {
        "teoría": """Algunos verbos como 'agree', 'hope', 'promise', 'refuse' son seguidos por un infinitivo.
Ejemplo:
- She agreed to help me. (Ella aceptó ayudarme.)""",
        "ejemplo": "I hope to see you soon. (Espero verte pronto.)",
        "pregunta": "La forma correcta de 'to visit' en 'He promised _____ his family' es:",
        "opciones": ["visiting", "to visit", "visit"],
        "respuesta_correcta": "to visit"
    },
    "Lección 86: Verbos Seguidos de Gerundios": {
        "teoría": """Algunos verbos como 'admit', 'consider', 'deny', 'suggest' son seguidos por un gerundio.
Ejemplo:
- He suggested going to the cinema. (Él sugirió ir al cine.)""",
        "ejemplo": "I considered buying a new car. (Consideré comprar un coche nuevo.)",
        "pregunta": "La forma correcta de 'to talk' en 'She avoided _____ to him' es:",
        "opciones": ["to talk", "talk", "talking"],
        "respuesta_correcta": "talking"
    },
    "Lección 87: Voz Pasiva (Futuro Perfecto)": {
        "teoría": """Se forma con 'will have been' + participio pasado.
Ejemplo:
- The book will have been published by next month. (El libro habrá sido publicado para el próximo mes.)""",
        "ejemplo": "The house will have been sold by Christmas. (La casa habrá sido vendida para Navidad.)",
        "pregunta": "La forma pasiva correcta de 'They will have built the bridge' es:",
        "opciones": ["The bridge will have built.", "The bridge will be built.", "The bridge will have been built."],
        "respuesta_correcta": "The bridge will have been built."
    },
    "Lección 88: 'So that' y 'In order to'": {
        "teoría": """Ambos se usan para expresar un propósito.
- 'So that' + cláusula.
- 'In order to' + verbo base.
Ejemplo:
- I saved money so that I could buy a car.
- I saved money in order to buy a car.""",
        "ejemplo": "He studied hard in order to pass the exam. (Él estudió mucho para pasar el examen.)",
        "pregunta": "La forma correcta para 'She went to the bank _____ withdraw money' es:",
        "opciones": ["so that", "in order to", "so"],
        "respuesta_correcta": "in order to"
    },
    "Lección 89: 'Used to' y 'Would' (Resumen)": {
        "teoría": """'Used to' se usa para hábitos y estados en el pasado.
'Would' solo para hábitos pasados (no estados).
Ejemplo:
- We used to live here.
- We would play here. (No 'we would live here'.)""",
        "ejemplo": "He used to have a cat. (Él solía tener un gato.)",
        "pregunta": "La frase correcta para 'solíamos ser amigos' es:",
        "opciones": ["we would be friends", "we used to be friends", "we would being friends"],
        "respuesta_correcta": "we used to be friends"
    },
    "Lección 90: Discurso Indirecto (Reportado) de preguntas": {
        "teoría": """Se usa una estructura de frase afirmativa después de la palabra 'wh'.
Ejemplo:
- 'Where are you going?' -> He asked me where I was going.""",
        "ejemplo": "She asked what my name was. (Ella preguntó cuál era mi nombre.)",
        "pregunta": "La forma indirecta de 'What is your address?' es:",
        "opciones": ["He asked me what was my address.", "He asked me what my address was.", "He asked me what my address is."],
        "respuesta_correcta": "He asked me what my address was."
    },
    "Lección 91: Voz Pasiva (Futuro Continuo)": {
        "teoría": """Se forma con 'will be being' + participio pasado, pero es una forma poco común.
Ejemplo:
- The car will be being repaired tomorrow morning. (El coche estará siendo reparado mañana por la mañana.)""",
        "ejemplo": "The house will be being painted all next week. (La casa estará siendo pintada toda la próxima semana.)",
        "pregunta": "La forma pasiva correcta de 'They will be delivering the mail' es:",
        "opciones": ["The mail will be delivered.", "The mail will being delivered.", "The mail will be being delivered."],
        "respuesta_correcta": "The mail will be being delivered."
    },
    "Lección 92: 'Shall' (Preguntas y Sugerencias)": {
        "teoría": """'Shall' se usa principalmente para ofrecerse a hacer algo o para hacer sugerencias, generalmente con 'I' o 'we'.
Ejemplo:
- Shall I open the door? (¿Abro la puerta?)
- Shall we dance? (¿Bailamos?)""",
        "ejemplo": "Shall we go to the movies? (¿Vamos al cine?)",
        "pregunta": "La forma correcta para '_____ I help you with that?' es:",
        "opciones": ["will", "shall", "must"],
        "respuesta_correcta": "shall"
    },
    "Lección 93: 'Both' y 'All'": {
        "teoría": """'Both' se usa para dos personas o cosas. 'All' se usa para tres o más.
Ejemplos:
- Both of my parents are doctors.
- All of the students passed the exam.""",
        "ejemplo": "All of them are here. (Todos ellos están aquí.)",
        "pregunta": "La palabra correcta para '_____ of my brothers are tall' (si tienes 3 hermanos) es:",
        "opciones": ["both", "all", "either"],
        "respuesta_correcta": "all"
    },
    "Lección 94: 'Either' y 'None'": {
        "teoría": """'Either' se usa para una elección entre dos.
'None' se usa para referirse a cero de tres o más.
Ejemplo:
- You can either take this road or that one.
- None of the students finished the test.""",
        "ejemplo": "None of the books are interesting. (Ninguno de los libros es interesante.)",
        "pregunta": "La palabra correcta para '_____ of my two bags is clean' es:",
        "opciones": ["None", "Either", "Neither"],
        "respuesta_correcta": "Neither"
    },
    "Lección 95: Los Participios como Adjetivos": {
        "teoría": """Los participios presentes (-ing) y pasados (-ed) de los verbos pueden funcionar como adjetivos.
Ejemplo:
- a boring book (un libro aburrido)
- a bored person (una persona aburrida)""",
        "ejemplo": "I read a surprising story. I was surprised. (Leí una historia sorprendente. Yo estaba sorprendido.)",
        "pregunta": "La forma correcta de 'to tire' en 'He has a very _____ job' es:",
        "opciones": ["tiring", "tired", "tires"],
        "respuesta_correcta": "tiring"
    },
    "Lección 96: El Verbo 'Get'": {
        "teoría": """El verbo 'get' tiene muchos significados. Puede significar 'conseguir', 'recibir', 'llegar', 'ponerse'.
Ejemplo:
- I get a letter.
- We get home late.
- It's getting cold.""",
        "ejemplo": "He got a new job. (Él consiguió un nuevo trabajo.)",
        "pregunta": "La forma correcta de 'get' en 'I didn't _____ the news' es:",
        "opciones": ["got", "gets", "get"],
        "respuesta_correcta": "get"
    },
    "Lección 97: Futuro Perfecto Continuo": {
        "teoría": """Se usa para una acción que estará en progreso hasta un punto en el futuro. Se forma con 'will have been' + verbo con '-ing'.
Ejemplo:
- By noon, she will have been working for six hours. (Para el mediodía, ella habrá estado trabajando por seis horas.)""",
        "ejemplo": "They will have been traveling for a week by Friday. (Ellos habrán estado viajando por una semana para el viernes.)",
        "pregunta": "La forma correcta de 'to sleep' para 'you' en esta lección es:",
        "opciones": ["you will been sleeping", "you will have been sleeping", "you will have been sleep"],
        "respuesta_correcta": "you will have been sleeping"
    },
    "Lección 98: El Segundo Condicional Invertido": {
        "teoría": """Se puede invertir el segundo condicional sin 'if' usando 'were' al principio.
Ejemplo:
- If I were rich, I would buy a house.
- Were I rich, I would buy a house.""",
        "ejemplo": "Were I to win the lottery, I would travel the world. (Si yo ganara la lotería, viajaría por el mundo.)",
        "pregunta": "La forma correcta para 'if I were you' es:",
        "opciones": ["I would be you", "Were I you", "I was you"],
        "respuesta_correcta": "Were I you"
    },
    "Lección 99: El Tercer Condicional Invertido": {
        "teoría": """Se puede invertir el tercer condicional sin 'if' usando 'had' al principio.
Ejemplo:
- If he had left, he would have seen her.
- Had he left, he would have seen her.""",
        "ejemplo": "Had I known, I would have helped you. (Si lo hubiera sabido, te habría ayudado.)",
        "pregunta": "La forma correcta para 'If they had seen me' es:",
        "opciones": ["Had they saw me", "Had they have seen me", "Had they seen me"],
        "respuesta_correcta": "Had they seen me"
    },
    "Lección 100: Estilo Indirecto (Verbos Modales)": {
        "teoría": """Se usan para reportar un consejo, una obligación o una habilidad.
Ejemplo:
- 'You should study.' -> He said that I should study. (El modal no cambia.)
- 'I can swim.' -> He said that he could swim. ('can' cambia a 'could').""",
        "ejemplo": "She said she could sing. (Ella dijo que podía cantar.)",
        "pregunta": "La forma correcta para reportar 'You must be on time.' es:",
        "opciones": ["He said that I must be on time.", "He said that I must been on time.", "He said that I had to be on time."],
        "respuesta_correcta": "He said that I must be on time."
    }
}

class GrammarApp:
    def __init__(self, master):
        self.master = master
        master.title("Aprendizaje de Gramática de Inglés")
        master.geometry("600x400")
        master.configure(bg="#f0f0f0")

        self.lecciones = list(GRAMMAR_LESSONS.keys())
        self.leccion_actual_index = 0
        self.puntaje = 0

        # UI Elements
        self.title_label = tk.Label(master, text="", font=("Arial", 20, "bold"), bg="#f0f0f0", fg="#333")
        self.title_label.pack(pady=10)

        self.theory_text = tk.Label(master, text="", font=("Arial", 12), justify="left", wraplength=550, bg="#f0f0f0")
        self.theory_text.pack(pady=5)

        self.example_label = tk.Label(master, text="", font=("Arial", 12, "italic"), bg="#f0f0f0")
        self.example_label.pack(pady=5)

        self.question_label = tk.Label(master, text="", font=("Arial", 14), bg="#f0f0f0")
        self.question_label.pack(pady=10)

        self.buttons_frame = tk.Frame(master, bg="#f0f0f0")
        self.buttons_frame.pack(pady=10)
        
        self.option_buttons = []
        for i in range(3):
            btn = tk.Button(self.buttons_frame, text="", command=lambda i=i: self.check_answer(i),
                            font=("Arial", 12), bg="#4CAF50", fg="white", bd=0, padx=20, pady=5)
            self.option_buttons.append(btn)
            btn.pack(side="left", padx=5)

        self.next_button = tk.Button(master, text="Siguiente Lección", command=self.next_lesson,
                                     font=("Arial", 12), bg="#008CBA", fg="white", bd=0, padx=20, pady=5)
        self.next_button.pack(pady=10)

        self.message_box = tk.Label(master, text="", font=("Arial", 12, "bold"), bg="#f0f0f0")
        self.message_box.pack(pady=5)
        
        self.load_lesson()

    def load_lesson(self):
        """Loads the content for the current lesson index."""
        if self.leccion_actual_index < len(self.lecciones):
            leccion_titulo = self.lecciones[self.leccion_actual_index]
            leccion_data = GRAMMAR_LESSONS[leccion_titulo]

            # Update UI with lesson data
            self.title_label.config(text=leccion_titulo)
            self.theory_text.config(text=leccion_data["teoría"])
            self.example_label.config(text=leccion_data["ejemplo"])
            self.question_label.config(text=leccion_data["pregunta"])
            
            # Show options
            opciones = leccion_data["opciones"]
            random.shuffle(opciones)
            for i, btn in enumerate(self.option_buttons):
                btn.config(text=opciones[i], state="normal")
            
            self.next_button.pack_forget()
            self.message_box.config(text="")
        else:
            self.show_end_message()

    def check_answer(self, option_index):
        """Checks if the selected option is correct and provides feedback."""
        leccion_titulo = self.lecciones[self.leccion_actual_index]
        leccion_data = GRAMMAR_LESSONS[leccion_titulo]
        selected_answer = self.option_buttons[option_index]["text"]

        if selected_answer == leccion_data["respuesta_correcta"]:
            self.puntaje += 1
            self.message_box.config(text="¡Correcto! Sigue así.", fg="green")
        else:
            self.message_box.config(text="Incorrecto. La respuesta correcta es '{}'".format(leccion_data["respuesta_correcta"]), fg="red")
        
        # Disable buttons after an answer is selected
        for btn in self.option_buttons:
            btn.config(state="disabled")

        # Agrega un pequeño retraso (1000ms = 1 segundo) antes de pasar a la siguiente lección.
        self.master.after(1000, self.next_lesson)

    def next_lesson(self):
        """Moves to the next lesson."""
        self.leccion_actual_index += 1
        self.load_lesson()

    def show_end_message(self):
        """Displays a message when all lessons are completed."""
        # Clear the current UI elements
        for widget in self.master.winfo_children():
            widget.pack_forget()
        
        # Show end message
        end_label = tk.Label(self.master, text="¡Has completado todas las lecciones!", font=("Arial", 18, "bold"), bg="#f0f0f0")
        end_label.pack(pady=50)
        
        score_label = tk.Label(self.master, text=f"Tu puntuación final es: {self.puntaje}/{len(self.lecciones)}", font=("Arial", 16), bg="#f0f0f0")
        score_label.pack(pady=10)
        
        tk.Button(self.master, text="Reiniciar", command=self.restart_app, font=("Arial", 12), bg="#4CAF50", fg="white", padx=20, pady=5).pack(pady=20)

    def restart_app(self):
        """Restarts the application to the beginning."""
        self.leccion_actual_index = 0
        self.puntaje = 0
        self.master.destroy()
        root = tk.Tk()
        GrammarApp(root)
        root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = GrammarApp(root)
    root.mainloop()
