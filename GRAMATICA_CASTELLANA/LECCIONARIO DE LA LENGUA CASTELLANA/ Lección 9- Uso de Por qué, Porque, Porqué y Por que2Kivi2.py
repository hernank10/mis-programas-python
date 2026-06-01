# main.py

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.radiobutton import RadioButton
from kivy.properties import ObjectProperty, NumericProperty, StringProperty, BooleanProperty
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.clock import Clock # Para programar eventos si fuera necesario

import random

# --- Datos de las Lecciones (Reutilizamos la estructura de diccionarios de Python) ---

# Enum-like structure for QuestionType
class QuestionType:
    MULTIPLE_CHOICE = "multiple_choice"
    FILL_IN_THE_BLANK = "fill_in_the_blank"
    TRANSFORMATION = "transformation"
    RULE_EXAMPLE = "rule_example"

# Definición de las preguntas para cada lección
lesson1_questions = [
    {
        "id": "L1Q1",
        "text": "El presidente de [Colombia/colombia] visitó ayer Bogotá.",
        "type": QuestionType.MULTIPLE_CHOICE,
        "options": ["Colombia", "colombia"],
        "correct_answer": "Colombia",
        "feedback_explanation": "Los nombres de países y ciudades (sustantivos propios) siempre se escriben con mayúscula inicial."
    },
    {
        "id": "L1Q2",
        "text": "Después de un punto, siempre se escribe con ___.",
        "type": QuestionType.FILL_IN_THE_BLANK,
        "correct_answer": "mayúscula",
        "feedback_explanation": "La primera palabra después de un punto y seguido o un punto y aparte siempre comienza con mayúscula."
    },
    {
        "id": "L1Q3",
        "text": "Mi perro se llama [Max/max].",
        "type": QuestionType.MULTIPLE_CHOICE,
        "options": ["Max", "max"],
        "correct_answer": "Max",
        "feedback_explanation": "Los nombres propios de personas o animales se escriben con mayúscula inicial."
    },
    {
        "id": "L1Q4",
        "text": "El río [Magdalena/magdalena] es muy largo.",
        "type": QuestionType.MULTIPLE_CHOICE,
        "options": ["Magdalena", "magdalena"],
        "correct_answer": "Magdalena",
        "feedback_explanation": "Los nombres propios geográficos (ríos, montañas, etc.) llevan mayúscula inicial."
    },
    {
        "id": "L1Q5",
        "text": "Ella [iba/iva] todos los días al parque.",
        "type": QuestionType.MULTIPLE_CHOICE,
        "options": ["iba", "iva"],
        "correct_answer": "iba",
        "feedback_explanation": "El pretérito imperfecto de 'ir' se escribe con 'b'."
    },
    {
        "id": "L1Q6",
        "text": "Es un [tubo/tuvo] de metal.",
        "type": QuestionType.MULTIPLE_CHOICE,
        "options": ["tubo", "tuvo"],
        "correct_answer": "tubo",
        "feedback_explanation": "'Tubo' es el objeto cilíndrico. 'Tuvo' es del verbo 'tener'."
    },
    {
        "id": "L1Q7",
        "text": "Se escribe con B antes de L o ___ (ej: blanco, brazo).",
        "type": QuestionType.FILL_IN_THE_BLANK,
        "correct_answer": "R",
        "feedback_explanation": "Las sílabas 'bla, ble, bli, blo, blu' y 'bra, bre, bri, bro, bru' siempre llevan 'b'."
    },
    {
        "id": "L1Q8",
        "text": "La [casa/caza] es muy grande.",
        "type": QuestionType.MULTIPLE_CHOICE,
        "options": ["casa", "caza"],
        "correct_answer": "casa",
        "feedback_explanation": "'Casa' es una vivienda. 'Caza' es la acción de cazar."
    },
    {
        "id": "L1Q9",
        "text": "Me gusta la [cereza/seresa].",
        "type": QuestionType.MULTIPLE_CHOICE,
        "options": ["cereza", "seresa"],
        "correct_answer": "cereza",
        "feedback_explanation": "Después de 'a', 'o', 'u' se usa 'z' (zapato, pozo, azul); antes de 'e', 'i' se usa 'c' (cena, cine)."
    },
    {
        "id": "L1Q10",
        "text": "Las palabras terminadas en '-ción' (cuando vienen de verbos terminados en '-ar') se escriben con ___.",
        "type": QuestionType.FILL_IN_THE_BLANK,
        "correct_answer": "c",
        "feedback_explanation": "Ejemplo: 'canción' (de cantar), 'oración' (de orar)."
    }
]

lesson2_questions = [
    {
        "id": "L2Q1",
        "text": "¿Lleva tilde la palabra 'CANCION'?",
        "type": QuestionType.MULTIPLE_CHOICE,
        "options": ["Sí, canción", "No, cancion"],
        "correct_answer": "Sí, canción",
        "feedback_explanation": "Las palabras agudas que terminan en 'n', 's' o vocal llevan tilde."
    },
    {
        "id": "L2Q2",
        "text": "El niño comió un bombón en el parque. (Escribe la palabra con tilde correctamente)",
        "type": QuestionType.FILL_IN_THE_BLANK,
        "correct_answer": "bombón",
        "feedback_explanation": "Bombón es aguda y termina en 'n', por lo tanto lleva tilde."
    },
    {
        "id": "L2Q3",
        "text": "¿Cómo se clasifica la palabra 'ÁRBOL'?",
        "type": QuestionType.MULTIPLE_CHOICE,
        "options": ["Aguda", "Grave", "Esdrújula"],
        "correct_answer": "Grave",
        "feedback_explanation": "Árbol es una palabra grave (llana) que termina en 'l' (no en n, s o vocal), por eso lleva tilde."
    },
    {
        "id": "L2Q4",
        "text": "Mi padre es un buen [CANCER/CARACTER]. (Elige la opción correcta para 'personalidad')",
        "type": QuestionType.MULTIPLE_CHOICE,
        "options": ["carácter", "caracter"],
        "correct_answer": "carácter",
        "feedback_explanation": "Carácter es una palabra grave que termina en 'r', por lo tanto lleva tilde."
    },
    {
        "id": "L2Q5",
        "text": "La palabra 'MATEMÁTICAS' es una palabra...",
        "type": QuestionType.MULTIPLE_CHOICE,
        "options": ["Aguda", "Grave", "Esdrújula"],
        "correct_answer": "Esdrújula",
        "feedback_explanation": "Todas las palabras esdrújulas y sobresdrújulas siempre llevan tilde."
    },
    {
        "id": "L2Q6",
        "text": "El [ULTIMO/ÚLTIMO] día de clase.",
        "type": QuestionType.MULTIPLE_CHOICE,
        "options": ["ultimo", "último"],
        "correct_answer": "último",
        "feedback_explanation": "Último es una palabra esdrújula y siempre lleva tilde."
    },
    {
        "id": "L2Q7",
        "text": "La palabra 'PAIS' forma un hiato. ¿Lleva tilde?",
        "type": QuestionType.MULTIPLE_CHOICE,
        "options": ["Sí, país", "No, pais"],
        "correct_answer": "Sí, país",
        "feedback_explanation": "Las vocales débiles (i, u) llevan tilde cuando forman hiato con una vocal fuerte (a, e, o), rompiendo el diptongo."
    },
    {
        "id": "L2Q8",
        "text": "La palabra 'CIUDAD' tiene un diptongo. ¿Lleva tilde?",
        "type": QuestionType.MULTIPLE_CHOICE,
        "options": ["Sí, ciudad", "No, ciudad"],
        "correct_answer": "No, ciudad",
        "feedback_explanation": "Ciudad es una palabra aguda que termina en 'd', por lo tanto no lleva tilde. El diptongo no se rompe."
    },
    {
        "id": "L2Q9",
        "text": "[EL/ÉL] es mi hermano. (Elige la opción correcta)",
        "type": QuestionType.MULTIPLE_CHOICE,
        "options": ["El", "Él"],
        "correct_answer": "Él",
        "feedback_explanation": "'Él' con tilde es pronombre personal. 'El' sin tilde es artículo."
    },
    {
        "id": "L2Q10",
        "text": "[TE/TÉ] gusta el té verde. (Escribe la palabra con tilde correctamente que significa 'bebida')",
        "type": QuestionType.FILL_IN_THE_BLANK,
        "correct_answer": "té",
        "feedback_explanation": "'Té' con tilde se refiere a la bebida. 'Te' sin tilde es pronombre personal."
    }
]

lesson3_questions = [
    {
        "id": "L3Q1",
        "text": "Transforma la siguiente frase a voz pasiva: 'El perro mordió al cartero.'",
        "type": QuestionType.TRANSFORMATION,
        "correct_answer": "El cartero fue mordido por el perro.",
        "feedback_explanation": "La voz pasiva se forma con el verbo 'ser' conjugado + el participio pasado del verbo principal + 'por' + el agente. Mantén la concordancia."
    },
    {
        "id": "L3Q2",
        "text": "Transforma la siguiente frase a singular: 'Las casas son grandes.'",
        "type": QuestionType.TRANSFORMATION,
        "correct_answer": "La casa es grande.",
        "feedback_explanation": "Debes cambiar el sustantivo y el verbo a su forma singular, manteniendo la concordancia."
    },
    {
        "id": "L3Q3",
        "text": "Transforma la siguiente frase al futuro simple: 'Ellos comen manzanas.'",
        "type": QuestionType.TRANSFORMATION,
        "correct_answer": "Ellos comerán manzanas.",
        "feedback_explanation": "El futuro simple de los verbos -er e -ir se forma añadiendo -erán o -irán a la raíz."
    },
    {
        "id": "L3Q4",
        "text": "Transforma la siguiente frase a forma negativa: 'Ella tiene un coche.'",
        "type": QuestionType.TRANSFORMATION,
        "correct_answer": "Ella no tiene un coche.",
        "feedback_explanation": "Para formar la negación en español, simplemente coloca 'no' antes del verbo conjugado."
    },
    {
        "id": "L3Q5",
        "text": "Transforma la siguiente frase de género masculino a femenino: 'El actor es famoso.'",
        "type": QuestionType.TRANSFORMATION,
        "correct_answer": "La actriz es famosa.",
        "feedback_explanation": "Cambia el artículo y el sustantivo a su forma femenina, y asegúrate de que el adjetivo concuerde en género."
    },
    {
        "id": "L3Q6",
        "text": "Transforma la siguiente frase del presente al pretérito perfecto simple: 'Yo leo un libro.'",
        "type": QuestionType.TRANSFORMATION,
        "correct_answer": "Yo leí un libro.",
        "feedback_explanation": "El pretérito perfecto simple se usa para acciones terminadas en un punto específico del pasado."
    },
    {
        "id": "L3Q7",
        "text": "Transforma la siguiente frase del presente al futuro simple: 'Ellos viajan mañana.'",
        "type": QuestionType.TRANSFORMATION,
        "correct_answer": "Ellos viajarán mañana.",
        "feedback_explanation": "El futuro simple se usa para acciones que ocurrirán después del momento presente."
    },
    {
        "id": "L3Q8",
        "text": "Transforma la siguiente frase del pretérito perfecto simple al presente: 'Nosotros comimos pizza.'",
        "type": QuestionType.TRANSFORMATION,
        "correct_answer": "Nosotros comemos pizza.",
        "feedback_explanation": "El presente se usa para acciones que ocurren ahora o son habituales."
    },
    {
        "id": "L3Q9",
        "text": "Transforma la siguiente frase del presente al pretérito imperfecto: 'Ella canta en el coro.'",
        "type": QuestionType.TRANSFORMATION,
        "correct_answer": "Ella cantaba en el coro.",
        "feedback_explanation": "El pretérito imperfecto se usa para describir acciones habituales o en progreso en el pasado."
    },
    {
        "id": "L3Q10",
        "text": "Transforma la siguiente frase del pretérito imperfecto al futuro simple: 'Tú estudiabas mucho.'",
        "type": QuestionType.TRANSFORMATION,
        "correct_answer": "Tú estudiarás mucho.",
        "feedback_explanation": "Asegúrate de conjugar el verbo 'estudiar' en la segunda persona del singular del futuro simple."
    }
]

lesson4_questions = [
    {
        "id": "L4Q1",
        "text": "Las palabras agudas llevan tilde cuando terminan en N, S o ___.",
        "type": QuestionType.FILL_IN_THE_BLANK,
        "correct_answer": "vocal",
        "feedback_explanation": "Ejemplo: 'canción', 'además', 'café'."
    },
    {
        "id": "L4Q2",
        "text": "El subjuntivo se usa para expresar deseos, dudas o ___.",
        "type": QuestionType.FILL_IN_THE_BLANK,
        "correct_answer": "emociones",
        "feedback_explanation": "El modo subjuntivo es clave para expresar subjetividad, irrealidad, deseos, dudas, emociones, etc."
    },
    {
        "id": "L4Q3",
        "text": "Cuando dos vocales fuertes (a, e, o) están juntas, forman un ___.",
        "type": QuestionType.FILL_IN_THE_BLANK,
        "correct_answer": "hiato",
        "feedback_explanation": "Un hiato ocurre cuando dos vocales fuertes están juntas o una vocal fuerte y una débil tónica."
    },
    {
        "id": "L4Q4",
        "text": "Los adjetivos deben concordar en género y ___ con el sustantivo que modifican.",
        "type": QuestionType.FILL_IN_THE_BLANK,
        "correct_answer": "número",
        "feedback_explanation": "Si el sustantivo es femenino plural, el adjetivo también debe serlo (ej. 'las casas grandes')."
    },
    {
        "id": "L4Q5",
        "text": "Se utiliza 'qué' con tilde para preguntas o ___.",
        "type": QuestionType.FILL_IN_THE_BLANK,
        "correct_answer": "exclamaciones",
        "feedback_explanation": "Los pronombres y adverbios interrogativos y exclamativos (qué, quién, cómo, cuándo, dónde, etc.) llevan tilde."
    }
]

lesson5_questions = [
    {
        "id": "L5Q1",
        "text": "La regla es: Las palabras graves (llanas) llevan tilde cuando NO terminan en N, S o vocal. Escribe un ejemplo de una palabra grave con tilde.",
        "type": QuestionType.RULE_EXAMPLE,
        "correct_answer": "árbol", # Referencia para la UI, la validación es con example_check_func
        "feedback_explanation": "Otros ejemplos: 'difícil', 'ángel', 'césped'.",
        "example_check_func": lambda ans: ans.lower().strip() in ["árbol", "difícil", "ángel", "césped"]
    },
    {
        "id": "L5Q2",
        "text": "La regla es: El verbo 'ir' en pretérito imperfecto de indicativo se escribe con 'b'. Escribe la conjugación para 'yo'.",
        "type": QuestionType.RULE_EXAMPLE,
        "correct_answer": "iba",
        "feedback_explanation": "La conjugación es 'yo iba, tú ibas, él/ella/usted iba, nosotros/as íbamos, vosotros/as ibais, ellos/as/ustedes iban'."
    },
    {
        "id": "L5Q3",
        "text": "La regla es: Se usa 'porque' (junto) para la conjunción causal (para responder '¿por qué?'). Escribe una frase de respuesta usando 'porque'.",
        "type": QuestionType.RULE_EXAMPLE,
        "correct_answer": "Porque tengo frío.",
        "feedback_explanation": "Ejemplo: 'No voy al parque porque tengo que estudiar.' Es la forma para dar una razón.",
        "example_check_func": lambda ans: "porque" in ans.lower() and len(ans.split()) > 2
    },
    {
        "id": "L5Q4",
        "text": "La regla es: El pretérito pluscuamperfecto se forma con el imperfecto de 'haber' + el participio del verbo principal. Escribe una frase usando el pluscuamperfecto con 'nosotros' del verbo 'comer'.",
        "type": QuestionType.RULE_EXAMPLE,
        "correct_answer": "Habíamos comido.",
        "feedback_explanation": "Ejemplo: 'Cuando llegó, ya habíamos comido.'",
        "example_check_func": lambda ans: "habíamos" in ans.lower() and "comido" in ans.lower()
    },
    {
        "id": "L5Q5",
        "text": "La regla es: El gerundio de los verbos terminados en -er/-ir se forma con -iendo. Escribe el gerundio del verbo 'dormir'.",
        "type": QuestionType.RULE_EXAMPLE,
        "correct_answer": "durmiendo",
        "feedback_explanation": "Recuerda que 'dormir' es irregular en el gerundio (oír -> oyendo, leer -> leyendo, etc.)."
    }
]

lesson6_questions = [
    {
        "id": "L6Q1",
        "text": "Ella [ser/estar] de Colombia.",
        "type": QuestionType.MULTIPLE_CHOICE,
        "options": ["es", "está"],
        "correct_answer": "es",
        "feedback_explanation": "Usamos 'ser' para origen o nacionalidad (característica permanente)."
    },
    {
        "id": "L6Q2",
        "text": "Yo [ser/estar] cansado hoy.",
        "type": QuestionType.MULTIPLE_CHOICE,
        "options": ["soy", "estoy"],
        "correct_answer": "estoy",
        "feedback_explanation": "Usamos 'estar' para estados temporales o condición física/emocional."
    },
    {
        "id": "L6Q3",
        "text": "La manzana [ser/estar] verde (color).",
        "type": QuestionType.MULTIPLE_CHOICE,
        "options": ["es", "está"],
        "correct_answer": "es",
        "feedback_explanation": "Usamos 'ser' para características inherentes o permanentes (el color natural)."
    },
    {
        "id": "L6Q4",
        "text": "La manzana [ser/estar] verde (no madura).",
        "type": QuestionType.MULTIPLE_CHOICE,
        "options": ["es", "está"],
        "correct_answer": "está",
        "feedback_explanation": "Usamos 'estar' para un estado temporal o condición (madurez de una fruta)."
    },
    {
        "id": "L6Q5",
        "text": "Mi padre [ser/estar] médico.",
        "type": QuestionType.MULTIPLE_CHOICE,
        "options": ["es", "está"],
        "correct_answer": "es",
        "feedback_explanation": "Usamos 'ser' para profesiones u ocupaciones."
    },
    {
        "id": "L6Q6",
        "text": "La reunión [ser/estar] en la sala grande.",
        "type": QuestionType.MULTIPLE_CHOICE,
        "options": ["es", "está"],
        "correct_answer": "es",
        "feedback_explanation": "Aunque parezca ubicación, se usa 'ser' para eventos, reuniones, fiestas, etc., indicando dónde 'tienen lugar'."
    },
    {
        "id": "L6Q7",
        "text": "Yo [ser/estar] en casa ahora.",
        "type": QuestionType.MULTIPLE_CHOICE,
        "options": ["soy", "estoy"],
        "correct_answer": "estoy",
        "feedback_explanation": "Usamos 'estar' para ubicación física."
    },
    {
        "id": "L6Q8",
        "text": "El café [ser/estar] caliente.",
        "type": QuestionType.MULTIPLE_CHOICE,
        "options": ["es", "está"],
        "correct_answer": "está",
        "feedback_explanation": "Usamos 'estar' para describir una condición o estado temporal (temperatura, que puede cambiar)."
    },
    {
        "id": "L6Q9",
        "text": "El libro [ser/estar] interesante.",
        "type": QuestionType.MULTIPLE_CHOICE,
        "options": ["es", "está"],
        "correct_answer": "es",
        "feedback_explanation": "Usamos 'ser' para cualidades intrínsecas o permanentes (una característica del libro)."
    },
    {
        "id": "L6Q10",
        "text": "La puerta [ser/estar] abierta.",
        "type": QuestionType.MULTIPLE_CHOICE,
        "options": ["es", "está"],
        "correct_answer": "está",
        "feedback_explanation": "Usamos 'estar' para un estado resultante de una acción o una condición temporal (la puerta puede cerrarse)."
    }
]

lesson7_questions = [
    {
        "id": "L7Q1",
        "text": "Ayer yo ___ a mis abuelos. (visitar)",
        "type": QuestionType.FILL_IN_THE_BLANK,
        "correct_answer": "visité",
        "feedback_explanation": "Se usa el pretérito perfecto simple para acciones terminadas en un momento específico del pasado ('ayer')."
    },
    {
        "id": "L7Q2",
        "text": "El año pasado, ellos ___ una casa nueva. (comprar)",
        "type": QuestionType.FILL_IN_THE_BLANK,
        "correct_answer": "compraron",
        "feedback_explanation": "Se usa el pretérito perfecto simple para acciones terminadas en un periodo específico del pasado ('el año pasado')."
    },
    {
        "id": "L7Q3",
        "text": "Ella ___ en 1990. (nacer)",
        "type": QuestionType.FILL_IN_THE_BLANK,
        "correct_answer": "nació",
        "feedback_explanation": "Se usa el pretérito perfecto simple para eventos puntuales en el pasado."
    },
    {
        "id": "L7Q4",
        "text": "Cuando ___ niño, siempre ___ en el parque. (ser, jugar)",
        "type": QuestionType.FILL_IN_THE_BLANK,
        "correct_answer": "era, jugaba",
        "feedback_explanation": "Se usa el pretérito imperfecto para describir acciones habituales o repetidas en el pasado ('cuando era niño', 'siempre')."
    },
    {
        "id": "L7Q5",
        "text": "Mientras yo ___, mi hermana ___ música. (leer, escuchar)",
        "type": QuestionType.FILL_IN_THE_BLANK,
        "correct_answer": "leía, escuchaba",
        "feedback_explanation": "Se usa el pretérito imperfecto para describir acciones simultáneas o en progreso en el pasado ('mientras')."
    },
    {
        "id": "L7Q6",
        "text": "La casa ___ un jardín grande y ___ muy bonita. (tener, ser)",
        "type": QuestionType.FILL_IN_THE_BLANK,
        "correct_answer": "tenía, era",
        "feedback_explanation": "Se usa el pretérito imperfecto para descripciones en el pasado (características, estados)."
    },
    {
        "id": "L7Q7",
        "text": "Ayer, [fui/iba] al supermercado y [compré/compraba] pan.",
        "type": QuestionType.MULTIPLE_CHOICE,
        "options": ["fui, compré", "iba, compraba", "fui, compraba", "iba, compré"],
        "correct_answer": "fui, compré",
        "feedback_explanation": "Ambas son acciones terminadas y puntuales en el pasado ('ayer')."
    },
    {
        "id": "L7Q8",
        "text": "Cuando [era/fui] joven, [vivía/viví] en Barcelona.",
        "type": QuestionType.MULTIPLE_CHOICE,
        "options": ["era, vivía", "fui, viví", "era, viví", "fui, vivía"],
        "correct_answer": "era, vivía",
        "feedback_explanation": "'Era' describe una etapa de la vida (imperfecto). 'Vivía' describe una acción habitual o un estado prolongado en el pasado."
    },
    {
        "id": "L7Q9",
        "text": "De repente, [empezó/empezaba] a llover mientras [caminaba/caminó] por la calle.",
        "type": QuestionType.MULTIPLE_CHOICE,
        "options": ["empezó, caminaba", "empezaba, caminó", "empezó, caminó", "empezaba, caminaba"],
        "correct_answer": "empezó, caminaba",
        "feedback_explanation": "'Empezó' es una acción puntual e inesperada (simple). 'Caminaba' es una acción en progreso que fue interrumpida (imperfecto)."
    },
    {
        "id": "L7Q10",
        "text": "Ella [estudió/estudiaba] medicina cuando [conoció/conocía] a su esposo.",
        "type": QuestionType.MULTIPLE_CHOICE,
        "options": ["estudió, conoció", "estudiaba, conocía", "estudiaba, conoció", "estudió, conocía"],
        "correct_answer": "estudiaba, conoció",
        "feedback_explanation": "'Estudiaba' describe una acción en progreso o habitual en el pasado (imperfecto). 'Conoció' es una acción puntual que interrumpió o ocurrió durante la otra (simple)."
    }
]

lesson8_questions = [
    {
        "id": "L8Q1",
        "text": "En la fiesta [hubo/hubieron] mucha gente.",
        "type": QuestionType.MULTIPLE_CHOICE,
        "options": ["hubo", "hubieron"],
        "correct_answer": "hubo",
        "feedback_explanation": "El verbo 'haber' para indicar existencia es impersonal y siempre se usa en singular: 'Hay', 'Había', 'Hubo', 'Habrá'."
    },
    {
        "id": "L8Q2",
        "text": "[Hay/Han] muchos libros en la biblioteca.",
        "type": QuestionType.MULTIPLE_CHOICE,
        "options": ["Hay", "Han"],
        "correct_answer": "Hay",
        "feedback_explanation": "'Hay' es la forma impersonal de 'haber' y se usa para indicar existencia. 'Han' es del verbo 'haber' como auxiliar de tiempos compuestos."
    },
    {
        "id": "L8Q3",
        "text": "En ese lugar no ___ problemas. (haber, en pasado, indicar existencia)",
        "type": QuestionType.FILL_IN_THE_BLANK,
        "correct_answer": "había",
        "feedback_explanation": "Para indicar existencia en pasado (imperf.), se usa 'había'."
    },
    {
        "id": "L8Q4",
        "text": "Ellos ___ comido ya. (haber, en presente)",
        "type": QuestionType.FILL_IN_THE_BLANK,
        "correct_answer": "han",
        "feedback_explanation": "'Han' es la forma del verbo 'haber' que se usa como auxiliar para formar tiempos compuestos (ej. 'han comido', 'han visto')."
    },
    {
        "id": "L8Q5",
        "text": "Yo ___ visto esa película antes. (haber, en presente)",
        "type": QuestionType.FILL_IN_THE_BLANK,
        "correct_answer": "he",
        "feedback_explanation": "'He' es la forma correcta del verbo 'haber' en primera persona singular del presente para formar el pretérito perfecto compuesto."
    },
    {
        "id": "L8Q6",
        "text": "Nosotros ___ estudiado mucho para el examen. (haber, en pretérito pluscuamperfecto)",
        "type": QuestionType.FILL_IN_THE_BLANK,
        "correct_answer": "habíamos",
        "feedback_explanation": "El pretérito pluscuamperfecto se forma con el imperfecto de 'haber' + participio. Para 'nosotros' es 'habíamos'."
    },
    {
        "id": "L8Q7",
        "text": "[Hace/Hacen] dos años que no la veo.",
        "type": QuestionType.MULTIPLE_CHOICE,
        "options": ["Hace", "Hacen"],
        "correct_answer": "Hace",
        "feedback_explanation": "Para expresar duración de tiempo, el verbo 'hacer' en estas construcciones es siempre impersonal y se usa en singular: 'Hace'."
    },
    {
        "id": "L8Q8",
        "text": "[Hizo/Hacía] mucho calor cuando estuvimos de vacaciones.",
        "type": QuestionType.MULTIPLE_CHOICE,
        "options": ["Hizo", "Hacía"],
        "correct_answer": "Hacía",
        "feedback_explanation": "Para describir condiciones climáticas en el pasado (que son duraderas o habituales), se usa el imperfecto de 'hacer'."
    },
    {
        "id": "L8Q9",
        "text": "___ diez minutos que salió. (Hacer, en presente)",
        "type": QuestionType.FILL_IN_THE_BLANK,
        "correct_answer": "Hace",
        "feedback_explanation": "Para indicar un punto de partida en el pasado, se usa 'hace' seguido del tiempo transcurrido."
    },
    {
        "id": "L8Q10",
        "text": "Siempre ___ frío en invierno en esa ciudad. (hacer, en imperfecto)",
        "type": QuestionType.FILL_IN_THE_BLANK,
        "correct_answer": "hacía",
        "feedback_explanation": "Para describir condiciones habituales o repetidas en el pasado, se usa el imperfecto de 'hacer'."
    }
]

lesson9_questions = [
    {
        "id": "L9Q1",
        "text": "¿___ no viniste ayer?",
        "type": QuestionType.FILL_IN_THE_BLANK,
        "correct_answer": "Por qué",
        "feedback_explanation": "'Por qué' (separado y con tilde) se usa para preguntas directas o indirectas."
    },
    {
        "id": "L9Q2",
        "text": "No fui a la fiesta ___ estaba enfermo.",
        "type": QuestionType.FILL_IN_THE_BLANK,
        "correct_answer": "porque",
        "feedback_explanation": "'Porque' (junto y sin tilde) es una conjunción causal, se usa para responder a una pregunta o dar una razón."
    },
    {
        "id": "L9Q3",
        "text": "No entiendo el ___ de tu decisión.",
        "type": QuestionType.FILL_IN_THE_BLANK,
        "correct_answer": "porqué",
        "feedback_explanation": "'Porqué' (junto y con tilde) es un sustantivo (sinónimo de 'motivo' o 'razón') y suele ir precedido de un artículo o determinante."
    },
    {
        "id": "L9Q4",
        "text": "Esta es la razón ___ te llamé.",
        "type": QuestionType.FILL_IN_THE_BLANK,
        "correct_answer": "por que",
        "feedback_explanation": "'Por que' (separado y sin tilde) se usa cuando 'que' es un pronombre relativo (equivalente a 'por el cual', 'por la cual', etc.) o una preposición + conjunción."
    },
    {
        "id": "L9Q5",
        "text": "Me pregunto ___ no me contestas.",
        "type": QuestionType.FILL_IN_THE_BLANK,
        "correct_answer": "por qué",
        "feedback_explanation": "'Por qué' se usa en preguntas indirectas."
    },
    {
        "id": "L9Q6",
        "text": "Lo hizo ___ quiso.",
        "type": QuestionType.FILL_IN_THE_BLANK,
        "correct_answer": "porque",
        "feedback_explanation": "'Porque' introduce la causa o razón de algo."
    },
    {
        "id": "L9Q7",
        "text": "No sé el ___ de su comportamiento.",
        "type": QuestionType.FILL_IN_THE_BLANK,
        "correct_answer": "porqué",
        "feedback_explanation": "Aquí 'porqué' funciona como sustantivo, significando 'la razón' o 'el motivo'."
    },
    {
        "id": "L9Q8",
        "text": "Los caminos ___ pasamos eran peligrosos.",
        "type": QuestionType.FILL_IN_THE_BLANK,
        "correct_answer": "por que",
        "feedback_explanation": "Se puede reemplazar por 'por los cuales': 'Los caminos por los cuales pasamos eran peligrosos'."
    },
    {
        "id": "L9Q9",
        "text": "Estudia ___ quieres aprobar el examen.",
        "type": QuestionType.FILL_IN_THE_BLANK,
        "correct_answer": "porque",
        "feedback_explanation": "'Porque' es la respuesta a la pregunta implícita '¿por qué estudias?'."
    },
    {
        "id": "L9Q10",
        "text": "Ese es el motivo ___ te pedí ayuda.",
        "type": QuestionType.FILL_IN_THE_BLANK,
        "correct_answer": "por que",
        "feedback_explanation": "Se puede reemplazar por 'por el cual': 'Ese es el motivo por el cual te pedí ayuda'."
    }
]

lesson10_questions = [
    {
        "id": "L10Q1",
        "text": "___ si lo entiendes. (expresión para pedir que alguien compruebe)",
        "type": QuestionType.FILL_IN_THE_BLANK,
        "correct_answer": "A ver",
        "feedback_explanation": "'A ver' (preposición 'a' + verbo 'ver') se usa para pedir que se vea o se compruebe algo, o como exclamación de expectación."
    },
    {
        "id": "L10Q2",
        "text": "Va a ___ mucha gente en la fiesta. (verbo auxiliar de existencia)",
        "type": QuestionType.FILL_IN_THE_BLANK,
        "correct_answer": "haber",
        "feedback_explanation": "'Haber' (verbo) se usa para indicar existencia (hay, había, habrá) o como auxiliar en tiempos compuestos (ha hecho, hemos comido)."
    },
    {
        "id": "L10Q3",
        "text": "[A ver/Haber] si llegamos a tiempo.",
        "type": QuestionType.MULTIPLE_CHOICE,
        "options": ["A ver", "Haber"],
        "correct_answer": "A ver",
        "feedback_explanation": "'A ver' se usa para expresar expectación o para comprobar algo."
    },
    {
        "id": "L10Q4",
        "text": "Debe ___ estudiado más. (verbo auxiliar)",
        "type": QuestionType.FILL_IN_THE_BLANK,
        "correct_answer": "haber",
        "feedback_explanation": "En este caso, 'haber' funciona como un verbo auxiliar en una perífrasis verbal ('deber de haber + participio')."
    },
    {
        "id": "L10Q5",
        "text": "Vamos a ___ la película que te dije.",
        "type": QuestionType.FILL_IN_THE_BLANK,
        "correct_answer": "ver", # Aquí el "a" ya está implícito en la frase
        "feedback_explanation": "Aunque la frase usa 'a', la palabra que falta es el verbo 'ver'. La confusión es común con 'a ver'."
    },
    {
        "id": "L10Q6",
        "text": "¿Qué te parece esta idea? [A ver/Haber].",
        "type": QuestionType.MULTIPLE_CHOICE,
        "options": ["A ver", "Haber"],
        "correct_answer": "A ver",
        "feedback_explanation": "Se utiliza 'a ver' como interjección para solicitar la atención del interlocutor."
    },
    {
        "id": "L10Q7",
        "text": "Podría ___ un problema si no actuamos.",
        "type": QuestionType.FILL_IN_THE_BLANK,
        "correct_answer": "haber",
        "feedback_explanation": "Aquí 'haber' indica la posibilidad de existencia de un problema."
    },
    {
        "id": "L10Q8",
        "text": "Ellos se fueron sin ___ despedido. (verbo auxiliar)",
        "type": QuestionType.FILL_IN_THE_BLANK,
        "correct_answer": "haber",
        "feedback_explanation": "Se usa 'haber' en infinitivo después de preposiciones (sin, por, para, etc.) para formar tiempos compuestos en infinitivo."
    },
    {
        "id": "L10Q9",
        "text": "[A ver/Haber], ¿qué tienes que decir?",
        "type": QuestionType.MULTIPLE_CHOICE,
        "options": ["A ver", "Haber"],
        "correct_answer": "A ver",
        "feedback_explanation": "Es una expresión coloquial para llamar la atención antes de una pregunta o comentario."
    },
    {
        "id": "L10Q10",
        "text": "No debería ___ ocurrido esto. (verbo auxiliar)",
        "type": QuestionType.FILL_IN_THE_BLANK,
        "correct_answer": "haber",
        "feedback_explanation": "Similar al Q4, 'haber' funciona como auxiliar en la perífrasis verbal 'deber de haber + participio'."
    }
]


# Mapeo de todas las lecciones
all_lessons = {
    1: {"title": "Ortografía Básica 📚", "questions": lesson1_questions},
    2: {"title": "Acentuación ✨", "questions": lesson2_questions},
    3: {"title": "Transformación de Oraciones 🔄", "questions": lesson3_questions},
    4: {"title": "Redacción de Reglas (Completar Huecos) ✍️", "questions": lesson4_questions},
    5: {"title": "Redacción de Reglas (Ejemplo) 🧠", "questions": lesson5_questions},
    6: {"title": "Uso de Ser y Estar 🇪🇸", "questions": lesson6_questions},
    7: {"title": "Pretérito Simple vs. Imperfecto 🕰️", "questions": lesson7_questions},
    8: {"title": "Usos de \"Haber\" y \"Hacer\" 💡", "questions": lesson8_questions},
    9: {"title": "Uso de \"Por qué\", \"Porque\", \"Porqué\" y \"Por que\" ❓", "questions": lesson9_questions},
    10: {"title": "Uso de \"A ver\" vs. \"Haber\" 🧐", "questions": lesson10_questions} # ¡Nueva lección añadida aquí!
}


# --- Lógica del Programa (LessonManager adaptable a Kivy) ---
class LessonManager:
    def __init__(self):
        self.current_lesson_num = None
        self.current_lesson = None
        self.shuffled_questions = []
        self.current_question_index = 0
        self.score = 0
        self.total_possible_score = 0
        self.user_answer = "" # Mantener la respuesta del usuario para el feedback

    def start_lesson(self, lesson_number):
        if lesson_number in all_lessons:
            self.current_lesson_num = lesson_number
            self.current_lesson = all_lessons[lesson_number]
            self.shuffled_questions = random.sample(self.current_lesson["questions"], len(self.current_lesson["questions"]))
            self.current_question_index = 0
            self.score = 0
            self.total_possible_score = len(self.shuffled_questions) * 10
            self.user_answer = ""
            return True
        return False

    def get_current_question(self):
        if self.shuffled_questions and self.current_question_index < len(self.shuffled_questions):
            return self.shuffled_questions[self.current_question_index]
        return None

    def check_answer(self, user_input):
        question = self.get_current_question()
        if not question:
            return False, "Error: No hay pregunta cargada."

        self.user_answer = user_input.strip() # Almacenar la respuesta del usuario

        is_correct = False
        if question["type"] == QuestionType.MULTIPLE_CHOICE or \
           question["type"] == QuestionType.FILL_IN_THE_BLANK or \
           question["type"] == QuestionType.TRANSFORMATION:
            is_correct = (self.user_answer.lower() == question["correct_answer"].lower())
        elif question["type"] == QuestionType.RULE_EXAMPLE:
            # Para RULE_EXAMPLE, usamos la función lambda definida en los datos
            if "example_check_func" in question and callable(question["example_check_func"]):
                is_correct = question["example_check_func"](self.user_answer)
            else:
                # Fallback si no hay función de chequeo específica
                is_correct = (self.user_answer.lower() == question["correct_answer"].lower())

        if is_correct:
            self.score += 10

        return is_correct, question["feedback_explanation"]

    def move_to_next_question(self):
        self.current_question_index += 1
        self.user_answer = "" # Limpiar la respuesta para la siguiente pregunta
        return self.current_question_index < len(self.shuffled_questions)

    def get_lesson_title(self):
        return self.current_lesson["title"] if self.current_lesson else "Lección Desconocida"

    def get_current_question_number(self):
        return self.current_question_index + 1

    def get_total_questions(self):
        return len(self.shuffled_questions)


# --- Kivy UI y Lógica de Navegación ---

# Cargar el archivo .kv
Builder.load_file('castellano_app.kv')

class MainMenuScreen(BoxLayout):
    # Esto es solo un placeholder, la estructura real está en el KV
    pass

class LessonScreen(BoxLayout):
    lesson_manager = ObjectProperty(None) # Referencia al gestor de lecciones
    current_question_text = StringProperty("")
    current_question_number_display = StringProperty("")
    input_type = StringProperty("text") # 'text' for TextInput, 'options' for RadioButtons
    multiple_choice_options = ObjectProperty([]) # Lista de opciones para RadioButtons
    user_input_text = StringProperty("") # Para el TextInput
    selected_option = StringProperty("") # Para RadioButtons

    def on_kv_post_build(self, *args):
        # Esta función se llama después de que el KV ha sido construido.
        # Aquí asignamos la instancia de LessonManager.
        # Esto se hará en CastellanoApp cuando se instancie LessonScreen.
        pass

    def update_question_display(self):
        question = self.lesson_manager.get_current_question()
        if question:
            self.current_question_text = question["text"]
            self.current_question_number_display = f"Pregunta {self.lesson_manager.get_current_question_number()} de {self.lesson_manager.get_total_questions()}"
            self.user_input_text = "" # Limpiar el input para la nueva pregunta
            self.selected_option = "" # Limpiar la selección de radio buttons

            # Eliminar widgets previos de opciones
            self.ids.radio_options_container.clear_widgets()

            if question["type"] == QuestionType.MULTIPLE_CHOICE:
                self.input_type = "options"
                self.ids.user_text_input.opacity = 0 # Ocultar TextInput
                self.ids.user_text_input.disabled = True

                self.ids.radio_options_container.opacity = 1 # Mostrar RadioButtons
                self.ids.radio_options_container.disabled = False
                for option in question["options"]:
                    radio_box = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(40))
                    radio_button = RadioButton(group='options', size_hint_x=None, width=dp(40))
                    radio_label = Label(text=option, text_size=(self.ids.radio_options_container.width - dp(50), None), halign='left', valign='middle')

                    # Enlazar la selección
                    radio_button.bind(active=self.on_radio_button_active)
                    radio_button.option_text = option # Guardar el texto de la opción en el botón

                    radio_box.add_widget(radio_button)
                    radio_box.add_widget(radio_label)
                    self.ids.radio_options_container.add_widget(radio_box)
            else:
                self.input_type = "text"
                self.ids.user_text_input.opacity = 1 # Mostrar TextInput
                self.ids.user_text_input.disabled = False

                self.ids.radio_options_container.opacity = 0 # Ocultar RadioButtons
                self.ids.radio_options_container.disabled = True
        else:
            self.current_question_text = "No hay más preguntas."
            self.current_question_number_display = ""
            self.input_type = "text" # Default
            self.multiple_choice_options = []
            self.ids.user_text_input.opacity = 1
            self.ids.user_text_input.disabled = False
            self.ids.radio_options_container.opacity = 0
            self.ids.radio_options_container.disabled = True

    def on_radio_button_active(self, radio_button, value):
        if value:
            self.selected_option = radio_button.option_text


class FeedbackScreen(BoxLayout):
    feedback_text = StringProperty("")
    explanation_text = StringProperty("")
    score_display = StringProperty("")
    is_correct = BooleanProperty(False) # Para controlar el color o ícono

class ResultsScreen(BoxLayout):
    final_score_text = StringProperty("")
    percentage_text = StringProperty("")
    message_text = StringProperty("")


# Clase principal de la aplicación Kivy
class CastellanoApp(App):
    current_view = ObjectProperty(None) # Para cambiar dinámicamente las vistas
    lesson_manager = ObjectProperty(LessonManager()) # Instancia global del gestor

    def build(self):
        # Al iniciar, cargamos la pantalla del menú
        self.main_menu_screen = MainMenuScreen(orientation='vertical')
        self.main_menu_screen.ids.app_ref = self # Permitir que el KV acceda a métodos de la app
        self.current_view = self.main_menu_screen
        return self.current_view

    def start_lesson(self, lesson_number):
        if self.lesson_manager.start_lesson(lesson_number):
            self.lesson_screen = LessonScreen(orientation='vertical')
            self.lesson_screen.lesson_manager = self.lesson_manager # Pasar la referencia
            self.lesson_screen.ids.app_ref = self # Permitir acceso a la app
            self.lesson_screen.ids.lesson_title_label.text = self.lesson_manager.get_lesson_title()
            self.lesson_screen.update_question_display()
            self.root.clear_widgets() # Limpiar la vista actual
            self.root.add_widget(self.lesson_screen) # Añadir la nueva vista
            self.current_view = self.lesson_screen

    def submit_answer(self, user_input):
        # Para preguntas de selección múltiple, el user_input ya viene del RadioButton
        # Para TextInput, viene del TextInput
        # La lógica de update_question_display se encarga de mostrar el input correcto
        # Por lo tanto, el user_input aquí ya es el valor correcto.
        
        # Validación extra: si es de selección múltiple y no ha seleccionado nada
        current_q = self.lesson_manager.get_current_question()
        if current_q and current_q["type"] == QuestionType.MULTIPLE_CHOICE and not self.lesson_screen.selected_option:
            popup = Popup(title='Atención',
                          content=Label(text='Por favor, selecciona una opción.'),
                          size_hint=(0.7, 0.3))
            popup.open()
            return
            
        # Si es de texto y el input está vacío
        if current_q and current_q["type"] != QuestionType.MULTIPLE_CHOICE and not user_input.strip():
            popup = Popup(title='Atención',
                          content=Label(text='Por favor, ingresa una respuesta.'),
                          size_hint=(0.7, 0.3))
            popup.open()
            return

        is_correct, feedback_exp = self.lesson_manager.check_answer(user_input)

        self.feedback_screen = FeedbackScreen(orientation='vertical')
        self.feedback_screen.is_correct = is_correct
        self.feedback_screen.feedback_text = "¡Correcto! ✅" if is_correct else "Incorrecto. ❌"
        self.feedback_screen.explanation_text = feedback_exp
        # Mostrar la respuesta correcta solo si fue incorrecta
        if not is_correct:
            correct_ans_display = self.lesson_manager.get_current_question()["correct_answer"]
            self.feedback_screen.explanation_text = f"La respuesta correcta es: '{correct_ans_display}'\n\n" + feedback_exp

        self.feedback_screen.score_display = f"Puntuación actual: {self.lesson_manager.score} / {self.lesson_manager.get_current_question_number() * 10}"
        self.feedback_screen.ids.app_ref = self
        self.root.clear_widgets()
        self.root.add_widget(self.feedback_screen)
        self.current_view = self.feedback_screen

    def go_to_next_question(self):
        if self.lesson_manager.move_to_next_question():
            # Volver a la pantalla de la lección para la siguiente pregunta
            self.lesson_screen.update_question_display() # Actualizar los widgets de la pantalla de lección
            self.root.clear_widgets()
            self.root.add_widget(self.lesson_screen)
            self.current_view = self.lesson_screen
        else:
            # Ir a la pantalla de resultados
            self.results_screen = ResultsScreen(orientation='vertical')
            final_score_percentage = (self.lesson_manager.score / self.lesson_manager.total_possible_score) * 100 if self.lesson_manager.total_possible_score > 0 else 0
            
            self.results_screen.final_score_text = f"Tu puntuación final es: {self.lesson_manager.score} de {self.lesson_manager.total_possible_score} puntos."
            self.results_screen.percentage_text = f"Porcentaje: {final_score_percentage:.0f}%"

            message = ""
            if final_score_percentage == 100:
                message = "¡Felicidades! ¡Has dominado esta lección a la perfección! ⭐⭐⭐"
            elif final_score_percentage >= 70:
                message = "¡Muy bien! Estás dominando las reglas. ¡Sigue así! 👍"
            else:
                message = "¡Buen intento! Repasa las reglas y vuelve a intentarlo. ¡La práctica te hará un experto! 💪"
            self.results_screen.message_text = message
            self.results_screen.ids.app_ref = self
            self.root.clear_widgets()
            self.root.add_widget(self.results_screen)
            self.current_view = self.results_screen

    def go_to_main_menu(self):
        self.root.clear_widgets()
        self.root.add_widget(self.main_menu_screen)
        self.current_view = self.main_menu_screen

    def exit_application(self):
        App.get_running_app().stop()

if __name__ == '__main__':
    CastellanoApp().run()
