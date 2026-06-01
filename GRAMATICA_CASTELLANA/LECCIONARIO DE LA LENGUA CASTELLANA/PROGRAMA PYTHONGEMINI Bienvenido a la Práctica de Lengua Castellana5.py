import random
import os
import json

# --- Persistencia de Datos (Guardar/Cargar ejercicios) ---
DATA_FILE = 'ejercicios_castellano_data.json'

def cargar_ejercicios():
    """Carga los ejercicios desde un archivo JSON. Si no existe o está vacío, usa los predefinidos."""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if data: # Asegurarse de que el archivo no esté vacío
                    print(f"Ejercicios cargados desde {DATA_FILE}")
                    return data
        except json.JSONDecodeError:
            print(f"Error: El archivo {DATA_FILE} está corrupto o vacío. Usando datos predefinidos.")
        except Exception as e:
            print(f"Error al cargar el archivo {DATA_FILE}: {e}. Usando datos predefinidos.")
    print("No se encontró el archivo de datos o estaba vacío/corrupto. Cargando 100 ejercicios predefinidos.")
    
    # --- 100 EJERCICIOS PREDEFINIDOS ---
    return {
        "Ortografía": {
            "Básico": {
                "Uso correcto de tildes": [
                    {"pregunta": "¿Dónde va la tilde en 'cajon'?", "tipo": "Uso correcto de tildes", "respuesta": "cajón", "explicacion": "Es aguda y termina en 'n'."},
                    {"pregunta": "¿Dónde va la tilde en 'arbol'?", "tipo": "Uso correcto de tildes", "respuesta": "árbol", "explicacion": "Es grave y termina en 'l'."},
                    {"pregunta": "¿Necesita tilde 'examen'?", "tipo": "Uso correcto de tildes", "respuesta": "no", "explicacion": "Es grave y termina en 'n'."},
                    {"pregunta": "¿Cuál es la forma correcta: 'solo' (adverbio) o 'sólo' (adverbio)?", "tipo": "Uso correcto de tildes", "respuesta": "solo", "explicacion": "La RAE recomienda no tildar el adverbio 'solo' incluso cuando puede haber ambigüedad."},
                    {"pregunta": "Pon la tilde en 'farmacia' si es necesario.", "tipo": "Uso correcto de tildes", "respuesta": "farmacia", "explicacion": "Es grave y termina en vocal, no lleva tilde."},
                    {"pregunta": "Pon la tilde en 'te' (pronombre) si es necesario.", "tipo": "Uso correcto de tildes", "respuesta": "te", "explicacion": "'Te' (pronombre) no lleva tilde diacrítica."},
                    {"pregunta": "Pon la tilde en 'si' (adverbio de afirmación) si es necesario.", "tipo": "Uso correcto de tildes", "respuesta": "sí", "explicacion": "'Sí' (adverbio de afirmación) lleva tilde diacrítica."},
                    {"pregunta": "Corrige la tilde en 'telefono'.", "tipo": "Uso correcto de tildes", "respuesta": "teléfono", "explicacion": "Es una palabra esdrújula, siempre lleva tilde."},
                    {"pregunta": "¿Necesita tilde 'camion'?", "tipo": "Uso correcto de tildes", "respuesta": "camión", "explicacion": "Es aguda y termina en 'n'."},
                    {"pregunta": "Pon la tilde en 'aun' (equivalente a 'todavía') si es necesario.", "tipo": "Uso correcto de tildes", "respuesta": "aún", "explicacion": "Lleva tilde diacrítica cuando significa 'todavía'."},
                ],
                "Detectar errores": [
                    {"pregunta": "Detecta el error: 'Ella trajo su paraguas de vajo del brazo.'", "tipo": "Detectar errores", "respuesta": {"palabra_erronea": "vajo", "correccion": "bajo"}, "explicacion": "Bajo se escribe con 'b'."},
                    {"pregunta": "Detecta el error: 'Los niños juegaron en el parque.'", "tipo": "Detectar errores", "respuesta": {"palabra_erronea": "juegaron", "correccion": "jugaron"}, "explicacion": "La forma correcta del verbo 'jugar' en pretérito es 'jugaron'."},
                    {"pregunta": "Detecta el error: 'Haí mucha gente en la calle.'", "tipo": "Detectar errores", "respuesta": {"palabra_erronea": "Haí", "correccion": "Hay"}, "explicacion": "'Hay' (del verbo haber) se escribe con 'h' e 'y'."},
                    {"pregunta": "Detecta el error: 'La casa es mui grande.'", "tipo": "Detectar errores", "respuesta": {"palabra_erronea": "mui", "correccion": "muy"}, "explicacion": "La palabra correcta es 'muy'."},
                    {"pregunta": "Detecta el error: 'El libro está en la mesa, ay.'", "tipo": "Detectar errores", "respuesta": {"palabra_erronea": "ay", "correccion": "ahí"}, "explicacion": "'Ahí' indica lugar."},
                    {"pregunta": "Detecta el error: 'Fuimos a ver el avion.'", "tipo": "Detectar errores", "respuesta": {"palabra_erronea": "avion", "correccion": "avión"}, "explicacion": "'Avión' lleva tilde por ser aguda terminada en 'n'."},
                    {"pregunta": "Detecta el error: 'Tengo cazo de agua.'", "tipo": "Detectar errores", "respuesta": {"palabra_erronea": "cazo", "correccion": "caso"}, "explicacion": "Se refiere a un 'caso' o situación, no a un 'cazo' de cocina."},
                    {"pregunta": "Detecta el error: 'Los chicos está felices.'", "tipo": "Detectar errores", "respuesta": {"palabra_erronea": "está", "correccion": "están"}, "explicacion": "Concordancia de número entre sujeto y verbo."},
                    {"pregunta": "Detecta el error: 'El vaso de cristal se calló.'", "tipo": "Detectar errores", "respuesta": {"palabra_erronea": "calló", "correccion": "cayó"}, "explicacion": "'Cayó' (del verbo caer) y 'calló' (del verbo callar)."},
                    {"pregunta": "Detecta el error: 'Me gusta mucho la sensacion de libertad.'", "tipo": "Detectar errores", "respuesta": {"palabra_erronea": "sensacion", "correccion": "sensación"}, "explicacion": "'Sensación' lleva tilde en la 'o'."},
                ],
            },
            "Intermedio": {
                "Completar oraciones": [
                    {"pregunta": "El sol brilla ___ el día.", "tipo": "Completar oraciones", "respuesta": ["por"], "explicacion": "'Por' indica duración."},
                    {"pregunta": "María y Pedro ___ a la fiesta anoche.", "tipo": "Completar oraciones", "respuesta": ["fueron"], "explicacion": "Forma verbal correcta de 'ir' en pretérito perfecto simple."},
                    {"pregunta": "Si no ___ a tiempo, perderemos el tren.", "tipo": "Completar oraciones", "respuesta": ["llegamos"], "explicacion": "Verbo 'llegar' conjugado en presente de subjuntivo."},
                    {"pregunta": "___ es importante leer y ___ bien.", "tipo": "Completar oraciones", "respuesta": ["Es", "escribir"], "explicacion": "'Es' (verbo ser) y 'escribir' (verbo infinitivo)."},
                    {"pregunta": "La casa ___ el tejado rojo es la mía.", "tipo": "Completar oraciones", "respuesta": ["con"], "explicacion": "'Con' indica compañía o característica."},
                    {"pregunta": "No sé si ___ a la montaña o a la playa.", "tipo": "Completar oraciones", "respuesta": ["ir"], "explicacion": "Infinitivo después de 'saber si'."},
                    {"pregunta": "Aunque ___ cansado, terminó el trabajo.", "tipo": "Completar oraciones", "respuesta": ["estaba"], "explicacion": "Verbo 'estar' en pretérito imperfecto."},
                    {"pregunta": "Él siempre ___ la verdad, ___ que le cueste.", "tipo": "Completar oraciones", "respuesta": ["dice", "aunque"], "explicacion": "'Dice' del verbo decir, 'aunque' es una conjunción concesiva."},
                    {"pregunta": "Los libros ___ la mesa son míos.", "tipo": "Completar oraciones", "respuesta": ["sobre"], "explicacion": "'Sobre' indica posición."},
                    {"pregunta": "Me gusta el café ___ leche.", "tipo": "Completar oraciones", "respuesta": ["con"], "explicacion": "'Con' indica acompañamiento."},
                ]
            }
        },
        "Morfología": {
            "Básico": {
                "Clasificación de palabras": [
                    {"pregunta": "Clasifica 'hermoso': ¿sustantivo, verbo o adjetivo?", "tipo": "Clasificación de palabras", "opciones": ["Sustantivo", "Verbo", "Adjetivo"], "respuesta": "Adjetivo", "explicacion": "Describe una cualidad del sustantivo."},
                    {"pregunta": "¿Qué tipo de palabra es 'correr'?", "tipo": "Clasificación de palabras", "opciones": ["Sustantivo", "Verbo", "Adverbio"], "respuesta": "Verbo", "explicacion": "Indica una acción."},
                    {"pregunta": "Clasifica 'mesa': ¿sustantivo o adjetivo?", "tipo": "Clasificación de palabras", "opciones": ["Sustantivo", "Adjetivo"], "respuesta": "Sustantivo", "explicacion": "Nombra un objeto."},
                    {"pregunta": "¿Qué categoría gramatical tiene 'pero'?", "tipo": "Clasificación de palabras", "opciones": ["Preposición", "Conjunción", "Adverbio"], "respuesta": "Conjunción", "explicacion": "Une palabras o proposiciones."},
                    {"pregunta": "En 'el coche rojo', ¿qué tipo de palabra es 'el'?", "tipo": "Clasificación de palabras", "opciones": ["Sustantivo", "Artículo", "Adjetivo"], "respuesta": "Artículo", "explicacion": "Precede al sustantivo y lo determina."},
                    {"pregunta": "¿Qué es 'aquí' en 'Ven aquí'?", "tipo": "Clasificación de palabras", "opciones": ["Sustantivo", "Verbo", "Adverbio de lugar"], "respuesta": "Adverbio de lugar", "explicacion": "Indica el lugar de la acción."},
                    {"pregunta": "Clasifica 'ellos': ¿sustantivo o pronombre?", "tipo": "Clasificación de palabras", "opciones": ["Sustantivo", "Pronombre"], "respuesta": "Pronombre", "explicacion": "Sustituye a un sustantivo o grupo nominal."},
                    {"pregunta": "¿Qué tipo de palabra es 'entre' en 'entre tú y yo'?", "tipo": "Clasificación de palabras", "opciones": ["Verbo", "Preposición", "Adverbio"], "respuesta": "Preposición", "explicacion": "Relaciona elementos de la oración."},
                    {"pregunta": "¿Cuál es la clase de palabra de 'cantar'?", "tipo": "Clasificación de palabras", "opciones": ["Sustantivo", "Adjetivo", "Verbo en infinitivo"], "respuesta": "Verbo en infinitivo", "explicacion": "Es la forma no personal del verbo."},
                    {"pregunta": "En la frase 'La casa es vieja', ¿qué tipo de palabra es 'vieja'?", "tipo": "Clasificación de palabras", "opciones": ["Adverbio", "Adjetivo", "Sustantivo"], "respuesta": "Adjetivo", "explicacion": "Describe una cualidad de la casa."},
                ],
                "Reescribir frases": [
                    {"pregunta": "Reescribe en voz pasiva: 'El jardinero plantó un árbol.'", "tipo": "Reescribir frases", "respuesta": "Un árbol fue plantado por el jardinero.", "explicacion": "El objeto directo de la activa pasa a ser sujeto paciente en la pasiva."},
                    {"pregunta": "Reescribe usando el pretérito perfecto compuesto: 'Ayer fui al cine.'", "tipo": "Reescribir frases", "respuesta": "Hoy he ido al cine.", "explicacion": "'He ido' es el pretérito perfecto compuesto de 'ir'."},
                    {"pregunta": "Reescribe de forma más formal: 'Me gustaría que me echaras una mano.'", "tipo": "Reescribir frases", "respuesta": "Le agradecería su colaboración.", "explicacion": "Se utiliza un lenguaje más cortés y verbos más formales."},
                    {"pregunta": "Reescribe como pregunta: 'Él vive en Madrid.'", "tipo": "Reescribir frases", "respuesta": "¿Vive él en Madrid?", "explicacion": "Se invierte el sujeto y el verbo para formar la pregunta."},
                    {"pregunta": "Reescribe en plural: 'La flor es hermosa.'", "tipo": "Reescribir frases", "respuesta": "Las flores son hermosas.", "explicacion": "Se cambian los sustantivos y adjetivos a su forma plural y se ajusta el verbo."},
                    {"pregunta": "Reescribe usando un adverbio de modo: 'Corrió rápido.'", "tipo": "Reescribir frases", "respuesta": "Corrió rápidamente.", "explicacion": "Se sustituye el adjetivo por el adverbio derivado."},
                    {"pregunta": "Reescribe la oración usando 'para': 'Estudio porque quiero aprender.'", "tipo": "Reescribir frases", "respuesta": "Estudio para aprender.", "explicacion": "Se utiliza 'para' para expresar finalidad."},
                    {"pregunta": "Reescribe la oración comenzando con el complemento: 'La cena la preparó mi madre.'", "tipo": "Reescribir frases", "respuesta": "Mi madre preparó la cena.", "explicacion": "Se invierte el orden del sujeto y el complemento."},
                    {"pregunta": "Reescribe la oración eliminando la repetición: 'Compré pan y queso, y luego comí pan y queso.'", "tipo": "Reescribir frases", "respuesta": "Compré pan y queso, y luego los comí.", "explicacion": "Se usa un pronombre para evitar la repetición innecesaria."},
                    {"pregunta": "Reescribe la oración haciendo énfasis en la acción: 'El accidente fue causado por la velocidad excesiva.'", "tipo": "Reescribir frases", "respuesta": "La velocidad excesiva causó el accidente.", "explicacion": "Se cambia la voz pasiva a activa para resaltar al agente de la acción."},
                ]
            },
            "Intermedio": {
                "Conjugación verbal": [
                    {"pregunta": "Conjuga el verbo 'hablar' en presente de indicativo, segunda persona singular (tú).", "tipo": "Conjugación verbal", "respuesta": "hablas", "explicacion": "La conjugación regular es 'tú hablas'."},
                    {"pregunta": "Conjuga el verbo 'comer' en pretérito perfecto simple, tercera persona plural (ellos).", "tipo": "Conjugación verbal", "respuesta": "comieron", "explicacion": "La conjugación regular es 'ellos comieron'."},
                    {"pregunta": "Conjuga el verbo 'vivir' en futuro simple, primera persona singular (yo).", "tipo": "Conjugación verbal", "respuesta": "viviré", "explicacion": "La conjugación regular es 'yo viviré'."},
                    {"pregunta": "Conjuga el verbo 'ser' en presente de subjuntivo, tercera persona singular (él/ella/usted).", "tipo": "Conjugación verbal", "respuesta": "sea", "explicacion": "La conjugación de 'ser' en subjuntivo es irregular."},
                    {"pregunta": "Conjuga el verbo 'ir' en pretérito imperfecto de indicativo, nosotros.", "tipo": "Conjugación verbal", "respuesta": "íbamos", "explicacion": "La conjugación es 'nosotros íbamos'."},
                    {"pregunta": "Conjuga el verbo 'hacer' en imperativo, segunda persona singular (tú).", "tipo": "Conjugación verbal", "respuesta": "haz", "explicacion": "El imperativo de 'hacer' es irregular."},
                    {"pregunta": "Conjuga el verbo 'escribir' en condicional simple, yo.", "tipo": "Conjugación verbal", "respuesta": "escribiría", "explicacion": "La conjugación es 'yo escribiría'."},
                    {"pregunta": "Conjuga el verbo 'tener' en pretérito pluscuamperfecto de indicativo, ellos.", "tipo": "Conjugación verbal", "respuesta": "habían tenido", "explicacion": "Verbo auxiliar 'haber' en pretérito imperfecto + participio."},
                    {"pregunta": "Conjuga el verbo 'decir' en presente de indicativo, yo.", "tipo": "Conjugación verbal", "respuesta": "digo", "explicacion": "Es un verbo irregular en esta persona."},
                    {"pregunta": "Conjuga el verbo 'salir' en presente de subjuntivo, tú.", "tipo": "Conjugación verbal", "respuesta": "salgas", "explicacion": "La conjugación es 'tú salgas'."},
                ]
            }
        },
        "Sintaxis": {
            "Básico": {
                "Selección múltiple": [ # Un ejemplo de selección múltiple en Sintaxis para diversificar
                    {"pregunta": "¿Qué función sintáctica tiene 'en la mesa' en 'El libro está en la mesa'?", "tipo": "Selección múltiple", "opciones": ["Sujeto", "Complemento Directo", "Complemento Circunstancial de Lugar", "Predicado"], "respuesta": "Complemento Circunstancial de Lugar", "explicacion": "Indica el lugar donde se encuentra el libro."},
                    {"pregunta": "¿Cuál de estas oraciones es unimembre?", "tipo": "Selección múltiple", "opciones": ["Ella canta.", "Hace frío.", "Yo estudio.", "Ellos corren."], "respuesta": "Hace frío.", "explicacion": "Las oraciones unimembres no pueden dividirse en sujeto y predicado."},
                    {"pregunta": "¿En qué oración 'se' es un pronombre personal reflexivo?", "tipo": "Selección múltiple", "opciones": ["Se come bien aquí.", "Ella se peina.", "Se lo di.", "Se vende casa."], "respuesta": "Ella se peina.", "explicacion": "'Se' se refiere a la misma persona que realiza la acción."},
                    {"pregunta": "¿Qué tipo de oración es '¡Ojalá llueva pronto!'?", "tipo": "Selección múltiple", "opciones": ["Enunciativa", "Interrogativa", "Desiderativa", "Imperativa"], "respuesta": "Desiderativa", "explicacion": "Expresa un deseo."},
                    {"pregunta": "¿Qué elemento es el núcleo del predicado verbal?", "tipo": "Selección múltiple", "opciones": ["El sustantivo", "El adjetivo", "El verbo", "El adverbio"], "respuesta": "El verbo", "explicacion": "El verbo es el elemento principal del predicado verbal."},
                    {"pregunta": "¿Cuál de estas oraciones es dubitativa?", "tipo": "Selección múltiple", "opciones": ["Quizás venga mañana.", "Ven aquí.", "No lo sé.", "Qué bien."], "respuesta": "Quizás venga mañana.", "explicacion": "Expresa duda o posibilidad."},
                    {"pregunta": "¿En qué oración el sujeto es tácito u omitido?", "tipo": "Selección múltiple", "opciones": ["Ellos estudian.", "Corro por el parque.", "Los pájaros cantan.", "María lee un libro."], "respuesta": "Corro por el parque.", "explicacion": "El sujeto 'yo' está omitido."},
                    {"pregunta": "¿Cuál es la función sintáctica de 'mañana' en 'Nos vemos mañana'?", "tipo": "Selección múltiple", "opciones": ["Sujeto", "Complemento Directo", "Complemento Circunstancial de Tiempo", "Atributo"], "respuesta": "Complemento Circunstancial de Tiempo", "explicacion": "Indica el momento de la acción."},
                    {"pregunta": "¿Qué tipo de predicado tiene la oración 'Él parece cansado'?", "tipo": "Selección múltiple", "opciones": ["Nominal", "Verbal", "Mixto", "Simple"], "respuesta": "Nominal", "explicacion": "Usa un verbo copulativo (parecer) y un atributo."},
                    {"pregunta": "¿Cuál de las siguientes es una oración exclamativa?", "tipo": "Selección múltiple", "opciones": ["¿Qué hora es?", "Ven aquí.", "¡Qué día tan bonito!", "No lo sé."], "respuesta": "¡Qué día tan bonito!", "explicacion": "Expresa una emoción intensa y lleva signos de exclamación."},
                ],
                "Ordenar oraciones": [
                    {"pregunta": "Ordena las palabras: 'libro / Juan / el / lee.'", "tipo": "Ordenar oraciones", "respuesta": "Juan lee el libro.", "explicacion": "Sujeto + Verbo + Objeto Directo."},
                    {"pregunta": "Ordena las palabras: 'la / parque / en / los / juegan / niños.'", "tipo": "Ordenar oraciones", "respuesta": "Los niños juegan en el parque.", "explicacion": "Sujeto + Verbo + Complemento de Lugar."},
                    {"pregunta": "Ordena las palabras: 'comió / El / perro / su / comida.'", "tipo": "Ordenar oraciones", "respuesta": "El perro comió su comida.", "explicacion": "Sujeto + Verbo + Posesivo + Sustantivo."},
                    {"pregunta": "Ordena las palabras: 'mucho / me / la / música / gusta.'", "tipo": "Ordenar oraciones", "respuesta": "Me gusta mucho la música.", "explicacion": "Objeto Indirecto + Verbo + Adverbio + Sujeto."},
                    {"pregunta": "Ordena las palabras: 'hermana / mi / es / alta / muy.'", "tipo": "Ordenar oraciones", "respuesta": "Mi hermana es muy alta.", "explicacion": "Posesivo + Sujeto + Verbo + Adverbio + Adjetivo."},
                    {"pregunta": "Ordena las palabras: 'ayer / compré / un / coche / nuevo.'", "tipo": "Ordenar oraciones", "respuesta": "Ayer compré un coche nuevo.", "explicacion": "Adverbio de tiempo + Verbo + Artículo + Sustantivo + Adjetivo."},
                    {"pregunta": "Ordena las palabras: 'rápidamente / corre / el / niño.'", "tipo": "Ordenar oraciones", "respuesta": "El niño corre rápidamente.", "explicacion": "Sujeto + Verbo + Adverbio de Modo."},
                    {"pregunta": "Ordena las palabras: 'ellos / trabajan / duro / siempre.'", "tipo": "Ordenar oraciones", "respuesta": "Ellos siempre trabajan duro.", "explicacion": "Sujeto + Adverbio de Frecuencia + Verbo + Adverbio de Modo."},
                    {"pregunta": "Ordena las palabras: 'para / la / escuela / mañana / va / ella.'", "tipo": "Ordenar oraciones", "respuesta": "Ella va para la escuela mañana.", "explicacion": "Sujeto + Verbo + Preposición + Artículo + Sustantivo + Adverbio de Tiempo."},
                    {"pregunta": "Ordena las palabras: 'un / café / quiero / con / leche.'", "tipo": "Ordenar oraciones", "respuesta": "Quiero un café con leche.", "explicacion": "Verbo + Artículo + Sustantivo + Preposición + Sustantivo."},
                ],
                "Identificación de funciones sintácticas": [
                    {"pregunta": "En 'Mi perro juega en el jardín', identifica el **sujeto**.", "tipo": "Identificación de funciones sintácticas", "respuesta": "Mi perro", "explicacion": "Es quien realiza la acción de jugar."},
                    {"pregunta": "En 'Ellos compran libros', identifica el **objeto directo**.", "tipo": "Identificación de funciones sintácticas", "respuesta": "libros", "explicacion": "Es lo que es comprado por ellos."},
                    {"pregunta": "En 'Juan dio un regalo a María', identifica el **objeto indirecto**.", "tipo": "Identificación de funciones sintácticas", "respuesta": "a María", "explicacion": "Es quien recibe el regalo (beneficiario)."},
                    {"pregunta": "En 'Mi casa es grande', identifica el **atributo**.", "tipo": "Identificación de funciones sintácticas", "respuesta": "grande", "explicacion": "Es una cualidad del sujeto unida por un verbo copulativo ('ser', 'estar', 'parecer')."},
                    {"pregunta": "En 'Ella canta muy bien', identifica el **complemento circunstancial de modo**.", "tipo": "Identificación de funciones sintácticas", "respuesta": "muy bien", "explicacion": "Indica cómo canta ella."},
                    {"pregunta": "En 'Los alumnos fueron evaluados por el profesor', identifica el **complemento agente**.", "tipo": "Identificación de funciones sintácticas", "respuesta": "por el profesor", "explicacion": "Realiza la acción en una oración pasiva."},
                    {"pregunta": "En 'Salimos de casa temprano', identifica el **complemento circunstancial de tiempo**.", "tipo": "Identificación de funciones sintácticas", "respuesta": "temprano", "explicacion": "Indica cuándo salimos."},
                    {"pregunta": "En 'Compraron el pan con dinero', identifica el **complemento circunstancial de instrumento**.", "tipo": "Identificación de funciones sintácticas", "respuesta": "con dinero", "explicacion": "Indica el medio con el que se realizó la acción."},
                    {"pregunta": "En 'Ella puso la mesa rápidamente', identifica el **predicado**.", "tipo": "Identificación de funciones sintácticas", "respuesta": "puso la mesa rápidamente", "explicacion": "Es la parte de la oración que contiene el verbo y lo que se dice del sujeto."},
                    {"pregunta": "En 'Estudiamos para el examen', identifica el **complemento circunstancial de finalidad**.", "tipo": "Identificación de funciones sintácticas", "respuesta": "para el examen", "explicacion": "Indica la razón o propósito de la acción."},
                ]
            },
            "Intermedio": {
                "Transformación de oraciones": [
                    {"pregunta": "Transforma a interrogativa: 'Él vendrá mañana.'", "tipo": "Transformación de oraciones", "respuesta": "¿Vendrá él mañana?", "explicacion": "Se invierte el sujeto y el verbo y se añaden los signos de interrogación."},
                    {"pregunta": "Transforma a exclamativa: 'Qué día tan bonito es hoy.'", "tipo": "Transformación de oraciones", "respuesta": "¡Qué día tan bonito es hoy!", "explicacion": "Se añaden los signos de exclamación para expresar una emoción."},
                    {"pregunta": "Transforma a negativa: 'Ella tiene un perro.'", "tipo": "Transformación de oraciones", "respuesta": "Ella no tiene un perro.", "explicacion": "Se añade el adverbio de negación 'no' antes del verbo."},
                    {"pregunta": "Transforma a afirmativa: 'No quiero comer.'", "tipo": "Transformación de oraciones", "respuesta": "Quiero comer.", "explicacion": "Se elimina el adverbio de negación."},
                    {"pregunta": "Transforma a impersonal: 'La gente dice que lloverá.'", "tipo": "Transformación de oraciones", "respuesta": "Se dice que lloverá.", "explicacion": "Se utiliza la construcción con 'se' para indicar que el agente es indeterminado."},
                    {"pregunta": "Transforma a pasiva perifrástica: 'El viento movió las hojas.'", "tipo": "Transformación de oraciones", "respuesta": "Las hojas fueron movidas por el viento.", "explicacion": "Se construye con el verbo 'ser' y el participio del verbo principal."},
                    {"pregunta": "Transforma a oración compuesta por coordinación: 'Estudio. Aprendo.'", "tipo": "Transformación de oraciones", "respuesta": "Estudio y aprendo.", "explicacion": "Se unen las oraciones simples con una conjunción coordinante."},
                    {"pregunta": "Transforma a oración subordinada de relativo: 'Compré el libro. El libro es interesante.'", "tipo": "Transformación de oraciones", "respuesta": "Compré el libro que es interesante.", "explicacion": "Se usa un pronombre relativo para unir las dos oraciones."},
                    {"pregunta": "Transforma a estilo indirecto: Juan dijo: 'Estoy cansado.'", "tipo": "Transformación de oraciones", "respuesta": "Juan dijo que estaba cansado.", "explicacion": "Se introduce la proposición subordinada con 'que' y se ajustan tiempos verbales y pronombres."},
                    {"pregunta": "Transforma a voz pasiva con 'se': 'Venden casas aquí.'", "tipo": "Transformación de oraciones", "respuesta": "Se venden casas aquí.", "explicacion": "Se utiliza la partícula 'se' para formar la pasiva refleja."},
                ]
            }
        }
    }


def guardar_ejercicios(data):
    """Guarda los ejercicios en un archivo JSON."""
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False) # ensure_ascii=False para caracteres especiales

# Cargar los ejercicios al inicio del programa
ejercicios_castellano = cargar_ejercicios()

# --- Funciones Auxiliares para Interacción ---

def limpiar_pantalla():
    """Limpia la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_opciones(titulo, opciones):
    """Muestra un menú numerado y pide una selección."""
    print(f"\n--- {titulo} ---")
    for i, opcion in enumerate(opciones):
        print(f"{i + 1}. {opcion}")
    while True:
        try:
            seleccion = input("Selecciona un número: ").strip()
            if seleccion.lower() == 's': # Opción para salir de la selección
                return None
            seleccion = int(seleccion)
            if 1 <= seleccion <= len(opciones):
                return opciones[seleccion - 1]
            else:
                print("Opción no válida. Intenta de nuevo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número.")

def normalizar_respuesta(respuesta):
    """Normaliza una respuesta para comparación (quitar espacios, minúsculas)."""
    if isinstance(respuesta, str):
        return respuesta.strip().lower()
    elif isinstance(respuesta, list):
        return [r.strip().lower() for r in respuesta]
    elif isinstance(respuesta, dict):
        return {k: v.strip().lower() for k, v in respuesta.items()}
    return respuesta

def comparar_respuestas(tipo_ejercicio, respuesta_usuario, respuesta_correcta):
    """Compara la respuesta del usuario con la respuesta correcta."""
    if tipo_ejercicio == "Selección múltiple" or tipo_ejercicio == "Clasificación de palabras":
        # Para seleccion_multiple y clasificacion_de_palabras que usan seleccion_multiple-like
        return normalizar_respuesta(respuesta_usuario) == normalizar_respuesta(respuesta_correcta)
    elif tipo_ejercicio == "Completar oraciones":
        # Divide la respuesta del usuario por comas y normaliza cada parte
        partes_usuario = [s.strip() for s in respuesta_usuario.split(',') if s.strip()]
        partes_correctas = normalizar_respuesta(respuesta_correcta)
        return normalizar_respuesta(partes_usuario) == partes_correctas
    elif tipo_ejercicio == "Detectar errores":
        # Se espera "palabra_erronea,correccion"
        partes = [s.strip() for s in respuesta_usuario.split(',') if s.strip()]
        if len(partes) == 2:
            respuesta_usuario_dict = {"palabra_erronea": partes[0], "correccion": partes[1]}
            return normalizar_respuesta(respuesta_usuario_dict) == normalizar_respuesta(respuesta_correcta)
        return False
    else: # Reescribir frases, Ordenar oraciones, Conjugación verbal, Uso correcto de tildes, Identificación de funciones sintácticas, Transformación de oraciones
        return normalizar_respuesta(respuesta_usuario) == normalizar_respuesta(respuesta_correcta)

# --- Funciones del Modo Práctica ---

def obtener_ejercicios_por_tipo(tipo_deseado):
    """Recopila todos los ejercicios de un tipo específico de todas las áreas y niveles."""
    ejercicios_encontrados = []
    for area in ejercicios_castellano.values():
        for nivel in area.values():
            for tipo, lista_ejer in nivel.items():
                # Normalizar el tipo del diccionario de ejercicios para la comparación
                if normalizar_respuesta(tipo) == normalizar_respuesta(tipo_deseado):
                    ejercicios_encontrados.extend(lista_ejer)
    return ejercicios_encontrados

def iniciar_practica():
    """Permite al usuario seleccionar el modo de práctica."""
    while True:
        limpiar_pantalla()
        print("--- Iniciar Sesión de Práctica ---")
        print("¿Cómo quieres practicar hoy?")
        
        opciones_practica = [
            "Por Tipo de Ejercicio (recomendado)",
            "Por Categoría (Área > Nivel > Tipo)",
            "Volver al Menú Principal"
        ]
        eleccion_modo = mostrar_opciones("Selecciona un Modo de Práctica", opciones_practica)

        if eleccion_modo == "Por Tipo de Ejercicio (recomendado)":
            menu_practica_por_tipo()
        elif eleccion_modo == "Por Categoría (Área > Nivel > Tipo)":
            menu_practica_por_categoria()
        elif eleccion_modo == "Volver al Menú Principal":
            break

def menu_practica_por_tipo():
    """Menú para seleccionar y practicar por tipo de ejercicio."""
    while True:
        limpiar_pantalla()
        print("--- Practicar por Tipo de Ejercicio ---")
        
        # Obtener todos los tipos de ejercicio únicos disponibles en los datos
        tipos_disponibles = set()
        for area_data in ejercicios_castellano.values():
            for nivel_data in area_data.values():
                for tipo_nombre in nivel_data.keys():
                    tipos_disponibles.add(tipo_nombre)
        
        if not tipos_disponibles:
            print("¡No hay ejercicios de ningún tipo disponibles! Por favor, añade ejercicios primero.")
            input("Presiona Enter para continuar...")
            return

        opciones_tipos = sorted(list(tipos_disponibles))
        opciones_tipos.append("Volver al Menú de Práctica") # Opción para salir

        tipo_seleccionado = mostrar_opciones("Selecciona un Tipo de Ejercicio para Practicar (o 's' para salir)", opciones_tipos)

        if tipo_seleccionado is None or tipo_seleccionado == "Volver al Menú de Práctica":
            break
        
        ejercicios_filtrados = obtener_ejercicios_por_tipo(tipo_seleccionado)
        
        if not ejercicios_filtrados:
            print(f"No hay ejercicios del tipo '{tipo_seleccionado}' disponibles.")
            input("Presiona Enter para continuar...")
            continue
        
        realizar_sesion_practica(ejercicios_filtrados, f"Tipo: {tipo_seleccionado}")
        # Después de una sesión, dar la opción de continuar practicando el mismo tipo o volver
        otra_sesion = input("¿Quieres practicar más ejercicios de este tipo? (s/n): ").lower().strip()
        if otra_sesion != 's':
            break # Sale del bucle y vuelve al menú de selección de tipo

def menu_practica_por_categoria():
    """Menú para seleccionar y practicar por categoría (Área > Nivel > Tipo)."""
    while True:
        limpiar_pantalla()
        print("--- Practicar por Categoría (Área > Nivel > Tipo) ---")

        areas = list(ejercicios_castellano.keys())
        if not areas:
            print("¡No hay áreas de ejercicios disponibles! Por favor, añade ejercicios primero.")
            input("Presiona Enter para continuar...")
            return

        area_seleccionada = mostrar_opciones("Selecciona un Área (o 's' para salir)", areas)
        if area_seleccionada is None: continue

        niveles = list(ejercicios_castellano[area_seleccionada].keys())
        if not niveles:
            print(f"No hay niveles en '{area_seleccionada}'.")
            input("Presiona Enter para continuar...")
            continue

        nivel_seleccionado = mostrar_opciones(f"Selecciona un Nivel para {area_seleccionada} (o 's' para salir)", niveles)
        if nivel_seleccionado is None: continue

        tipos_ejercicio = list(ejercicios_castellano[area_seleccionada][nivel_seleccionado].keys())
        if not tipos_ejercicio:
            print(f"No hay tipos de ejercicio en '{area_seleccionada}' > '{nivel_seleccionado}'.")
            input("Presiona Enter para continuar...")
            continue

        tipo_seleccionado = mostrar_opciones(f"Selecciona un Tipo de Ejercicio para {area_seleccionada} > {nivel_seleccionado} (o 's' para salir)", tipos_ejercicio)
        if tipo_seleccionado is None: continue

        ejercicios_filtrados = ejercicios_castellano[area_seleccionada][nivel_seleccionado][tipo_seleccionado]
        if not ejercicios_filtrados:
            print(f"No hay ejercicios en la categoría seleccionada: {area_seleccionada} > {nivel_seleccionado} > {tipo_seleccionado}.")
            input("Presiona Enter para continuar...")
            continue
        
        realizar_sesion_practica(ejercicios_filtrados, f"{area_seleccionada} > {nivel_seleccionado} > {tipo_seleccionado}")
        break # Sale después de completar o salir de la práctica por categoría

def realizar_sesion_practica(ejercicios, titulo_sesion):
    """Ejecuta una sesión de práctica con los ejercicios seleccionados."""
    limpiar_pantalla()
    print(f"\n--- Sesión de Práctica: {titulo_sesion} ---")
    
    ejercicios_para_practicar = list(ejercicios) # Copia la lista
    random.shuffle(ejercicios_para_practicar) # Mezcla los ejercicios
    
    puntuacion = 0
    total_ejercicios = len(ejercicios_para_practicar)

    for i, ejercicio in enumerate(ejercicios_para_practicar):
        limpiar_pantalla()
        print(f"\nEjercicio {i + 1} de {total_ejercicios}")
        print("-" * 30)
        print(f"Pregunta: {ejercicio['pregunta']}")

        respuesta_usuario = ""
        # Adaptar la interfaz de entrada según el tipo de ejercicio
        if ejercicio['tipo'] == "Selección múltiple" or ejercicio['tipo'] == "Clasificación de palabras":
            print("Opciones:")
            for j, opcion in enumerate(ejercicio['opciones']):
                print(f"{j + 1}. {opcion}")
            while True:
                try:
                    eleccion = input("Selecciona tu respuesta (número) o 's' para saltar: ").strip()
                    if eleccion.lower() == 's': # Opción para saltar
                        respuesta_usuario = 'saltar_ejercicio'
                        break
                    eleccion = int(eleccion)
                    if 1 <= eleccion <= len(ejercicio['opciones']):
                        respuesta_usuario = ejercicio['opciones'][eleccion - 1]
                        break
                    else:
                        print("Opción no válida. Intenta de nuevo.")
                except ValueError:
                    print("Entrada inválida. Por favor, ingresa un número.")
        elif ejercicio['tipo'] == "Completar oraciones":
            respuesta_usuario = input("Tu respuesta (separa por comas si hay múltiples espacios o 's' para saltar): ").strip()
        elif ejercicio['tipo'] == "Detectar errores":
            respuesta_usuario = input("Detecta el error y la corrección (ej: palabra_erronea,correccion, o 's' para saltar): ").strip()
        elif ejercicio['tipo'] == "Reescribir frases":
            respuesta_usuario = input("Reescribe la frase correctamente (o 's' para saltar): ").strip()
        elif ejercicio['tipo'] == "Ordenar oraciones":
            respuesta_usuario = input("Ordena la oración (o 's' para saltar): ").strip()
        elif ejercicio['tipo'] == "Conjugación verbal":
            respuesta_usuario = input("Tu conjugación (o 's' para saltar): ").strip()
        elif ejercicio['tipo'] == "Uso correcto de tildes":
            respuesta_usuario = input("Tu respuesta con tildes (o 's' para saltar): ").strip()
        elif ejercicio['tipo'] == "Identificación de funciones sintácticas":
            respuesta_usuario = input("Identifica la función sintáctica (o 's' para saltar): ").strip()
        elif ejercicio['tipo'] == "Transformación de oraciones":
            respuesta_usuario = input("Tu oración transformada (o 's' para saltar): ").strip()
        else: # Tipo no reconocido, fallback a respuesta corta
            print(f"Tipo de ejercicio '{ejercicio['tipo']}' no reconocido, esperando respuesta corta.")
            respuesta_usuario = input("Tu respuesta (o 's' para saltar): ").strip()

        if respuesta_usuario.lower() == 's':
            print("Ejercicio saltado.")
            print(f"Explicación: {ejercicio['explicacion']}")
            input("Presiona Enter para el siguiente ejercicio...")
            continue
            
        es_correcta = comparar_respuestas(ejercicio['tipo'], respuesta_usuario, ejercicio['respuesta'])

        if es_correcta:
            print("¡Correcto! ✅")
            puntuacion += 1
        else:
            print("Incorrecto. ❌")
            if isinstance(ejercicio['respuesta'], dict): # Para detectar_errores
                print(f"Respuesta correcta: Palabra errónea '{ejercicio['respuesta']['palabra_erronea']}', Corrección: '{ejercicio['respuesta']['correccion']}'")
            elif isinstance(ejercicio['respuesta'], list): # Para completar_oraciones
                print(f"Respuesta correcta: {', '.join(ejercicio['respuesta'])}")
            else: # Otros tipos
                print(f"Respuesta correcta: {ejercicio['respuesta']}")
        
        print(f"Explicación: {ejercicio['explicacion']}")
        input("Presiona Enter para el siguiente ejercicio...")
    
    limpiar_pantalla()
    print("\n--- ¡Sesión de Práctica Terminada! ---")
    print(f"Obtuviste {puntuacion} de {total_ejercicios} ejercicios correctos.")
    print("¡Sigue practicando para mejorar! 💪")
    input("Presiona Enter para volver al menú principal...")

# --- Funciones del Modo Editor (sin cambios significativos, solo actualización de tipos válidos) ---

def menu_editor():
    """Menú principal del editor de ejercicios."""
    while True:
        limpiar_pantalla()
        print("--- Editor de Ejercicios ---")
        opciones_editor = [
            "Listar ejercicios",
            "Añadir nuevo ejercicio",
            "Editar ejercicio existente",
            "Eliminar ejercicio",
            "Añadir nueva categoría (Área/Nivel/Tipo)",
            "Volver al Menú Principal"
        ]
        eleccion_editor = mostrar_opciones("Opciones del Editor", opciones_editor)

        if eleccion_editor == "Listar ejercicios":
            listar_ejercicios_menu()
        elif eleccion_editor == "Añadir nuevo ejercicio":
            añadir_ejercicio()
        elif eleccion_editor == "Editar ejercicio existente":
            editar_ejercicio()
        elif eleccion_editor == "Eliminar ejercicio":
            eliminar_ejercicio()
        elif eleccion_editor == "Añadir nueva categoría (Área/Nivel/Tipo)":
            añadir_categoria()
        elif eleccion_editor == "Volver al Menú Principal":
            break

def seleccionar_categoria_editor():
    """Función auxiliar para seleccionar Área, Nivel y Tipo en el editor."""
    areas = list(ejercicios_castellano.keys())
    if not areas:
        print("No hay áreas de ejercicios. Por favor, crea una primero.")
        return None, None, None, None

    area_sel = mostrar_opciones("Selecciona un Área (o 's' para salir)", areas)
    if area_sel is None: return None, None, None, None

    niveles = list(ejercicios_castellano[area_sel].keys())
    if not niveles:
        print(f"No hay niveles en '{area_sel}'.")
        return area_sel, None, None, None

    nivel_sel = mostrar_opciones(f"Selecciona un Nivel para {area_sel} (o 's' para salir)", niveles)
    if nivel_sel is None: return area_sel, None, None, None

    tipos = list(ejercicios_castellano[area_sel][nivel_sel].keys())
    if not tipos:
        print(f"No hay tipos de ejercicio en '{area_sel}' > '{nivel_sel}'.")
        return area_sel, nivel_sel, None, None

    tipo_sel = mostrar_opciones(f"Selecciona un Tipo de Ejercicio para {area_sel} > {nivel_sel} (o 's' para salir)", tipos)
    return area_sel, nivel_sel, tipo_sel, ejercicios_castellano[area_sel][nivel_sel].get(tipo_sel, [])


def listar_ejercicios_menu():
    """Permite al usuario listar ejercicios de una categoría seleccionada."""
    limpiar_pantalla()
    print("--- Listar Ejercicios ---")
    area, nivel, tipo, lista_ejercicios = seleccionar_categoria_editor()

    if not all([area, nivel, tipo]):
        input("Presiona Enter para continuar...")
        return

    if not lista_ejercicios:
        print(f"No hay ejercicios en '{area}' > '{nivel}' > '{tipo}'.")
        input("Presiona Enter para continuar...")
        return

    print(f"\n--- Ejercicios en {area} > {nivel} > {tipo} ---")
    for i, ejer in enumerate(lista_ejercicios):
        print(f"\n{i + 1}.")
        print(f"  Pregunta: {ejer['pregunta']}")
        print(f"  Tipo: {ejer['tipo'].replace('_', ' ').title()}")
        if ejer['tipo'] == "Selección múltiple" or ejer['tipo'] == "Clasificación de palabras":
            print(f"  Opciones: {', '.join(ejer['opciones'])}")
            print(f"  Respuesta Correcta: {ejer['respuesta']}")
        elif ejer['tipo'] == "Completar oraciones":
            print(f"  Respuesta Correcta: {', '.join(ejer['respuesta'])}")
        elif ejer['tipo'] == "Detectar errores":
            print(f"  Palabra Errónea: {ejer['respuesta']['palabra_erronea']}, Corrección: {ejer['respuesta']['correccion']}")
        else: # Reescribir frases, Ordenar oraciones, Conjugación verbal, Uso correcto de tildes, Identificación de funciones sintácticas, Transformación de oraciones
            print(f"  Respuesta Correcta: {ejer['respuesta']}")
        print(f"  Explicación: {ejer['explicacion']}")
    
    input("\nPresiona Enter para continuar...")

def añadir_ejercicio():
    """Permite al usuario añadir un nuevo ejercicio a una categoría existente."""
    limpiar_pantalla()
    print("--- Añadir Nuevo Ejercicio ---")
    
    area, nivel, tipo, lista_ejercicios = seleccionar_categoria_editor()

    if not all([area, nivel, tipo]):
        input("Presiona Enter para continuar...")
        return
    
    print(f"\nAñadiendo ejercicio en: {area} > {nivel} > {tipo}")
    pregunta = input("Ingresa la pregunta del ejercicio: ").strip()
    explicacion = input("Ingresa la explicación del ejercicio: ").strip()

    # Tipos válidos de ejercicios para el editor (asegurarse de que coincidan con la lógica de práctica)
    tipos_validos = [
        "Selección múltiple",
        "Completar oraciones",
        "Detectar errores",
        "Reescribir frases",
        "Ordenar oraciones",
        "Clasificación de palabras",
        "Conjugación verbal",
        "Uso correcto de tildes",
        "Identificación de funciones sintácticas",
        "Transformación de oraciones"
    ]

    tipo_ejercicio = mostrar_opciones("Selecciona el Tipo de Ejercicio", tipos_validos)
    if tipo_ejercicio is None: # Si el usuario decide salir de la selección
        return
    
    respuesta = None
    opciones = []

    if tipo_ejercicio == "Selección múltiple" or tipo_ejercicio == "Clasificación de palabras":
        num_opciones = int(input("¿Cuántas opciones tendrá el ejercicio? "))
        for i in range(num_opciones):
            opciones.append(input(f"Ingresa la opción {i+1}: ").strip())
        respuesta = input("Ingresa la respuesta correcta (tal como aparece en las opciones): ").strip()
        if respuesta not in opciones:
            print("Error: La respuesta correcta debe ser una de las opciones. Volviendo al menú.")
            input("Presiona Enter para continuar...")
            return
    elif tipo_ejercicio == "Completar oraciones":
        respuesta_str = input("Ingresa la/s palabra/s correcta/s (separa por comas si hay varias): ").strip()
        respuesta = [s.strip() for s in respuesta_str.split(',') if s.strip()]
    elif tipo_ejercicio == "Detectar errores":
        palabra_erronea = input("Ingresa la palabra errónea: ").strip()
        correccion = input("Ingresa la corrección de la palabra: ").strip()
        respuesta = {"palabra_erronea": palabra_erronea, "correccion": correccion}
    else: # Otros tipos con respuesta de texto simple: Reescribir frases, Ordenar oraciones, Conjugación verbal, Uso correcto de tildes, Identificación de funciones sintácticas, Transformación de oraciones
        respuesta = input("Ingresa la respuesta correcta: ").strip()

    nuevo_ejercicio = {
        "pregunta": pregunta,
        "tipo": tipo_ejercicio,
        "respuesta": respuesta,
        "explicacion": explicacion
    }
    if opciones:
        nuevo_ejercicio["opciones"] = opciones
    
    ejercicios_castellano[area][nivel][tipo].append(nuevo_ejercicio)
    guardar_ejercicios(ejercicios_castellano)
    print("¡Ejercicio añadido exitosamente!")
    input("Presiona Enter para continuar...")

def editar_ejercicio():
    """Permite al usuario editar un ejercicio existente."""
    limpiar_pantalla()
    print("--- Editar Ejercicio ---")
    area, nivel, tipo, lista_ejercicios = seleccionar_categoria_editor()

    if not all([area, nivel, tipo]):
        input("Presiona Enter para continuar...")
        return
    
    if not lista_ejercicios:
        print(f"No hay ejercicios en '{area}' > '{nivel}' > '{tipo}' para editar.")
        input("Presiona Enter para continuar...")
        return

    print(f"\nEjercicios en {area} > {nivel} > {tipo}:")
    for i, ejer in enumerate(lista_ejercicios):
        print(f"{i + 1}. {ejer['pregunta'][:50]}...") # Mostrar un fragmento de la pregunta

    while True:
        try:
            idx = int(input("Ingresa el número del ejercicio a editar (0 para cancelar): ")) - 1
            if idx == -1:
                print("Edición cancelada.")
                break
            if 0 <= idx < len(lista_ejercicios):
                ejercicio_a_editar = lista_ejercicios[idx]
                print(f"\nEditando ejercicio: {ejercicio_a_editar['pregunta']}")
                print(f"Tipo actual: {ejercicio_a_editar['tipo']}")
                print("Deja en blanco si no quieres cambiar el valor.")

                nueva_pregunta = input(f"Nueva pregunta ({ejercicio_a_editar['pregunta']}): ").strip()
                if nueva_pregunta:
                    ejercicio_a_editar['pregunta'] = nueva_pregunta

                nueva_explicacion = input(f"Nueva explicación ({ejercicio_a_editar['explicacion']}): ").strip()
                if nueva_explicacion:
                    ejercicio_a_editar['explicacion'] = nueva_explicacion
                
                # Edición de respuesta según el tipo de ejercicio
                if ejercicio_a_editar['tipo'] == "Selección múltiple" or ejercicio_a_editar['tipo'] == "Clasificación de palabras":
                    print("\nEditando opciones (ingresa las nuevas opciones una por línea, deja vacío para terminar):")
                    nuevas_opciones = []
                    for i, op in enumerate(ejercicio_a_editar.get('opciones', [])): # Usar .get para evitar error si no hay opciones
                        print(f"Opción actual {i+1}: {op}")
                        nueva_op = input(f"Nueva opción {i+1} (Enter para mantener, o 'FIN' para terminar): ").strip()
                        if nueva_op.lower() == 'fin':
                            break
                        elif nueva_op:
                            nuevas_opciones.append(nueva_op)
                        else:
                            nuevas_opciones.append(op) # Mantener la opción original si no se edita
                    
                    while True: # Permite añadir más opciones después de las existentes
                        mas_opcion = input("Añadir otra opción? (s/n): ").lower().strip()
                        if mas_opcion == 's':
                            nuevas_opciones.append(input("Ingresa la nueva opción: ").strip())
                        else:
                            break
                    
                    if nuevas_opciones: # Si no están vacías
                        ejercicio_a_editar['opciones'] = nuevas_opciones

                    nueva_respuesta_sm = input(f"Nueva respuesta correcta (actual: {ejercicio_a_editar['respuesta']}): ").strip()
                    if nueva_respuesta_sm:
                        if 'opciones' in ejercicio_a_editar and nueva_respuesta_sm not in ejercicio_a_editar['opciones']:
                            print("Advertencia: La nueva respuesta no está entre las opciones actuales. Asegúrate de corregirlo.")
                        ejercicio_a_editar['respuesta'] = nueva_respuesta_sm

                elif ejercicio_a_editar['tipo'] == "Completar oraciones":
                    resp_actual = ", ".join(ejercicio_a_editar['respuesta'])
                    nueva_respuesta_co_str = input(f"Nuevas palabras correctas (separadas por comas, actual: {resp_actual}): ").strip()
                    if nueva_respuesta_co_str:
                        ejercicio_a_editar['respuesta'] = [s.strip() for s in nueva_respuesta_co_str.split(',') if s.strip()]

                elif ejercicio_a_editar['tipo'] == "Detectar errores":
                    palabra_erronea_act = ejercicio_a_editar['respuesta']['palabra_erronea']
                    correccion_act = ejercicio_a_editar['respuesta']['correccion']
                    nueva_palabra_erronea = input(f"Nueva palabra errónea (actual: {palabra_erronea_act}): ").strip()
                    nueva_correccion = input(f"Nueva corrección (actual: {correccion_act}): ").strip()
                    if nueva_palabra_erronea:
                        ejercicio_a_editar['respuesta']['palabra_erronea'] = nueva_palabra_erronea
                    if nueva_correccion:
                        ejercicio_a_editar['respuesta']['correccion'] = nueva_correccion
                else: # Otros tipos de respuesta simple
                    nueva_respuesta = input(f"Nueva respuesta correcta (actual: {ejercicio_a_editar['respuesta']}): ").strip()
                    if nueva_respuesta:
                        ejercicio_a_editar['respuesta'] = nueva_respuesta
                
                guardar_ejercicios(ejercicios_castellano)
                print("¡Ejercicio editado exitosamente!")
                break
            else:
                print("Número de ejercicio no válido.")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número.")
    
    input("Presiona Enter para continuar...")


def eliminar_ejercicio():
    """Permite al usuario eliminar un ejercicio."""
    limpiar_pantalla()
    print("--- Eliminar Ejercicio ---")
    area, nivel, tipo, lista_ejercicios = seleccionar_categoria_editor()

    if not all([area, nivel, tipo]):
        input("Presiona Enter para continuar...")
        return
    
    if not lista_ejercicios:
        print(f"No hay ejercicios en '{area}' > '{nivel}' > '{tipo}' para eliminar.")
        input("Presiona Enter para continuar...")
        return

    print(f"\nEjercicios en {area} > {nivel} > {tipo}:")
    for i, ejer in enumerate(lista_ejercicios):
        print(f"{i + 1}. {ejer['pregunta'][:50]}...")

    while True:
        try:
            idx = int(input("Ingresa el número del ejercicio a eliminar (0 para cancelar): ")) - 1
            if idx == -1:
                print("Eliminación cancelada.")
                break
            if 0 <= idx < len(lista_ejercicios):
                confirmacion = input(f"¿Estás seguro de eliminar '{lista_ejercicios[idx]['pregunta'][:30]}...'? (s/n): ").lower().strip()
                if confirmacion == 's':
                    del ejercicios_castellano[area][nivel][tipo][idx]
                    guardar_ejercicios(ejercicios_castellano)
                    print("¡Ejercicio eliminado exitosamente!")
                else:
                    print("Eliminación cancelada.")
                break
            else:
                print("Número de ejercicio no válido.")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número.")
    
    input("Presiona Enter para continuar...")

def añadir_categoria():
    """Permite al usuario añadir nuevas áreas, niveles o tipos de ejercicio."""
    limpiar_pantalla()
    print("--- Añadir Nueva Categoría ---")
    opciones_cat = ["Área", "Nivel", "Tipo de Ejercicio", "Cancelar"]
    tipo_cat = mostrar_opciones("¿Qué tipo de categoría quieres añadir?", opciones_cat)

    if tipo_cat == "Cancelar" or tipo_cat is None:
        return

    nombre_nueva_categoria = input(f"Ingresa el nombre de la nueva {tipo_cat}: ").strip()
    if not nombre_nueva_categoria:
        print("El nombre no puede estar vacío.")
        input("Presiona Enter para continuar...")
        return

    if tipo_cat == "Área":
        if nombre_nueva_categoria in ejercicios_castellano:
            print(f"El área '{nombre_nueva_categoria}' ya existe.")
        else:
            ejercicios_castellano[nombre_nueva_categoria] = {}
            print(f"Área '{nombre_nueva_categoria}' añadida.")
    elif tipo_cat == "Nivel":
        areas = list(ejercicios_castellano.keys())
        if not areas:
            print("No hay áreas existentes. Por favor, crea un área primero.")
            input("Presiona Enter para continuar...")
            return
        area_parent = mostrar_opciones("Selecciona el Área a la que pertenece este Nivel (o 's' para salir)", areas)
        if area_parent is None:
            print("Operación cancelada.")
            input("Presiona Enter para continuar...")
            return
        if nombre_nueva_categoria in ejercicios_castellano[area_parent]:
            print(f"El nivel '{nombre_nueva_categoria}' ya existe en '{area_parent}'.")
        else:
            ejercicios_castellano[area_parent][nombre_nueva_categoria] = {}
            print(f"Nivel '{nombre_nueva_categoria}' añadido a '{area_parent}'.")
    elif tipo_cat == "Tipo de Ejercicio":
        areas = list(ejercicios_castellano.keys())
        if not areas:
            print("No hay áreas existentes. Por favor, crea un área primero.")
            input("Presiona Enter para continuar...")
            return
        area_parent = mostrar_opciones("Selecciona el Área (o 's' para salir)", areas)
        if area_parent is None:
            print("Operación cancelada.")
            input("Presiona Enter para continuar...")
            return

        niveles = list(ejercicios_castellano[area_parent].keys())
        if not niveles:
            print(f"No hay niveles en '{area_parent}'. Por favor, crea un nivel primero.")
            input("Presiona Enter para continuar...")
            return
        level_parent = mostrar_opciones(f"Selecciona el Nivel para {area_parent} (o 's' para salir)", niveles)
        if level_parent is None:
            print("Operación cancelada.")
            input("Presiona Enter para continuar...")
            return
        if nombre_nueva_categoria in ejercicios_castellano[area_parent][level_parent]:
            print(f"El tipo de ejercicio '{nombre_nueva_categoria}' ya existe en '{area_parent}' > '{level_parent}'.")
        else:
            ejercicios_castellano[area_parent][level_parent][nombre_nueva_categoria] = []
            print(f"Tipo de ejercicio '{nombre_nueva_categoria}' añadido a '{area_parent}' > '{level_parent}'.")
    
    guardar_ejercicios(ejercicios_castellano)
    input("Presiona Enter para continuar...")

# --- Menú Principal del Programa ---

def menu_principal():
    """Muestra el menú principal y gestiona la navegación."""
    while True:
        limpiar_pantalla()
        print("**************************************************")
        print("*** ¡Bienvenido a la Práctica de Lengua Castellana! ***")
        print("**************************************************")
        
        opciones_menu = [
            "Empezar a practicar",
            "Editar ejercicios",
            "Salir"
        ]
        eleccion = mostrar_opciones("Menú Principal", opciones_menu)

        if eleccion == "Empezar a practicar":
            iniciar_practica()
        elif eleccion == "Editar ejercicios":
            menu_editor()
        elif eleccion == "Salir":
            print("\n¡Gracias por practicar! ¡Hasta pronto! 👋")
            break

if __name__ == "__main__":
    menu_principal()
