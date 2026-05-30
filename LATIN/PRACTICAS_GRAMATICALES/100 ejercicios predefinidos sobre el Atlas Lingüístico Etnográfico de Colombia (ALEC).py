import random
import os

def cargar_ejercicios_alec():
    """
    Carga los 100 ejercicios predefinidos sobre el Atlas Lingüístico Etnográfico de Colombia (ALEC).
    """
    print("Cargando 100 ejercicios sobre el Atlas Lingüístico Etnográfico de Colombia (ALEC)...")
    return {
        "Atlas Linguistico Etnografico de Colombia": {
            "Instituto Caro y Cuervo": [
                # 1. Conceptos Fundamentales del ALEC (20 ejercicios)
                {"pregunta": "¿Qué significa la sigla ALEC?", "respuesta": "atlas linguistico etnografico de colombia", "explicacion": "Es el nombre completo de la obra dialectológica más importante de Colombia."},
                {"pregunta": "¿Qué institución fue la responsable principal de la creación del ALEC?", "respuesta": "instituto caro y cuervo", "explicacion": "El Instituto Caro y Cuervo, con sede en Bogotá, es el centro de investigación lingüística y literaria de Colombia."},
                {"pregunta": "¿Cuál es el objetivo principal de un atlas lingüístico como el ALEC?", "respuesta": "registrar la variacion dialectal", "explicacion": "Busca documentar las diferencias fonéticas, morfosintácticas y léxicas del habla en un territorio."},
                {"pregunta": "El ALEC se enfoca exclusivamente en el español de Colombia. ¿Verdadero o Falso?", "respuesta": "verdadero", "explicacion": "Su ámbito de estudio es el territorio colombiano y las variedades del español habladas en él."},
                {"pregunta": "¿Qué tipo de mapas utiliza el ALEC para representar la distribución geográfica de los fenómenos lingüísticos?", "respuesta": "isoglosas", "explicacion": "Las isoglosas son líneas que delimitan áreas geográficas con rasgos lingüísticos comunes."},
                {"pregunta": "El ALEC es una obra sincrónica, es decir, describe la lengua en un momento dado. ¿Verdadero o Falso?", "respuesta": "verdadero", "explicacion": "Aunque la dialectología tiene una base histórica, el atlas documenta el estado de la lengua en el momento de la encuesta."},
                {"pregunta": "¿Qué disciplina lingüística es la base de la metodología de un atlas lingüístico?", "respuesta": "dialectologia", "explicacion": "La dialectología estudia la variación geográfica de las lenguas."},
                {"pregunta": "El ALEC incluye solo información fonética. ¿Verdadero o Falso?", "respuesta": "falso", "explicacion": "Abarca fonética, morfología, sintaxis y léxico, además de aspectos etnográficos."},
                {"pregunta": "¿Qué significa el componente 'etnográfico' en el título del ALEC?", "respuesta": "relacion con la cultura y costumbres", "explicacion": "El ALEC no solo registra palabras, sino también su relación con la vida, las costumbres y la cultura de los hablantes."},
                {"pregunta": "¿Cuántos tomos principales tiene la publicación del ALEC?", "respuesta": "seis", "explicacion": "El ALEC se publicó en seis grandes tomos, más un tomo introductorio y un índice."},
                {"pregunta": "El ALEC fue el primer atlas lingüístico de América Latina. ¿Verdadero o Falso?", "respuesta": "falso", "explicacion": "Hubo otros intentos o atlas parciales antes, pero el ALEC es uno de los más completos y sistemáticos."},
                {"pregunta": "¿Qué tipo de datos se recolectaron para el ALEC: solo de hablantes cultos o de todos los niveles sociales?", "respuesta": "todos los niveles sociales", "explicacion": "Se buscó una representación de la diversidad de hablantes, aunque con un foco en hablantes rurales y mayores."},
                {"pregunta": "El ALEC es una obra descriptiva. ¿Verdadero o Falso?", "respuesta": "verdadero", "explicacion": "Su objetivo es describir el uso real de la lengua, no prescribir cómo se debe hablar."},
                {"pregunta": "¿Qué es un 'punto de encuesta' en la metodología del ALEC?", "respuesta": "localidad donde se recolectan datos", "explicacion": "Son los lugares específicos donde los encuestadores recopilaron la información lingüística."},
                {"pregunta": "¿Qué importancia tiene el ALEC para el estudio del español americano?", "respuesta": "fundamental", "explicacion": "Es una fuente primaria invaluable para entender la diversidad y evolución del español en América."},
                {"pregunta": "¿Qué tipo de preguntas se hacían a los informantes para obtener los datos lingüísticos?", "respuesta": "preguntas indirectas", "explicacion": "Se evitaban preguntas directas sobre la palabra para no influir en la respuesta, usando descripciones o situaciones."},
                {"pregunta": "El ALEC se basa en el estudio de textos escritos. ¿Verdadero o Falso?", "respuesta": "falso", "explicacion": "Se basa en el habla oral, recolectada directamente de los informantes."},
                {"pregunta": "¿Qué es un 'cuestionario' en el contexto del ALEC?", "respuesta": "lista de preguntas para la encuesta", "explicacion": "Un conjunto estandarizado de preguntas para obtener datos comparables en diferentes puntos."},
                {"pregunta": "El ALEC es un proyecto terminado y no se ha actualizado. ¿Verdadero o Falso?", "respuesta": "falso", "explicacion": "Aunque la publicación principal terminó, el Instituto Caro y Cuervo sigue investigando y publicando sobre dialectología colombiana."},
                {"pregunta": "¿Qué concepto se refiere a las variaciones de una lengua según la región geográfica?", "respuesta": "dialecto", "explicacion": "El ALEC documenta los dialectos del español en Colombia."},

                # 2. Fenómenos Fonéticos Regionales en Colombia (20 ejercicios)
                {"pregunta": "¿Qué fenómeno fonético, muy extendido en Colombia, implica la pronunciación de la 'c' (ante e, i) y la 'z' como 's'?", "respuesta": "seseo", "explicacion": "El seseo es la norma en todo el español de América, incluyendo Colombia, donde no existe la distinción /θ/."},
                {"pregunta": "¿Qué fenómeno fonético, común en algunas zonas de Colombia, implica la pronunciación de 'll' como 'y'?", "respuesta": "yeismo", "explicacion": "El yeísmo es la neutralización de la distinción entre /ʎ/ (ll) y /ʝ/ (y), muy extendido en casi toda Colombia."},
                {"pregunta": "¿Qué fenómeno fonético, característico de la costa caribe colombiana, implica la aspiración o pérdida de la -s final de sílaba?", "respuesta": "aspiracion de -s", "explicacion": "La /s/ se aspira a una /h/ o se pierde en esa posición (ej. 'costa' > 'cohta'), un rasgo del español caribeño."},
                {"pregunta": "¿Qué fenómeno fonético se refiere a la neutralización de /l/ y /r/ en posición implosiva (ej. 'arma' > 'alma')?", "respuesta": "lambdacismo y rotacismo", "explicacion": "El lambdacismo es la pronunciación de /r/ como /l/, y el rotacismo es la de /l/ como /r/. Ambos se dan en algunas zonas costeras de Colombia."},
                {"pregunta": "¿Qué dialecto colombiano se caracteriza por un ritmo lento y una entonación particular, a menudo asociado con el seseo y el yeísmo?", "respuesta": "cundiboyacense", "explicacion": "El español del altiplano cundiboyacense (incluyendo Bogotá) tiene características fonéticas distintivas."},
                {"pregunta": "¿Qué fenómeno fonético se refiere a la pronunciación de la 's' como 'c' o 'z' (interdental fricativa sorda), que no se da en Colombia?", "respuesta": "ceceo", "explicacion": "El ceceo es característico de algunas zonas de Andalucía, pero no del español de Colombia."},
                {"pregunta": "¿Qué dialecto colombiano se caracteriza por la pronunciación fuerte de la 'rr' y la 'ch'?", "respuesta": "paisa", "explicacion": "El dialecto paisa (Antioquia, Eje Cafetero) tiene una fonética muy marcada."},
                {"pregunta": "¿Qué fenómeno fonético implica la omisión de la 'd' intervocálica (ej. 'cantado' > 'cantao'), común en varias regiones de Colombia?", "respuesta": "elision de d intervocálica", "explicacion": "Es una relajación fonética extendida en el español coloquial de muchas zonas."},
                {"pregunta": "¿Qué fenómeno fonético se refiere a la pérdida de la 'j' o 'g' (fricativa velar sorda) en posición final de sílaba (ej. 'reloj' > 'relo')?", "respuesta": "relajacion de j", "explicacion": "Común en algunas zonas de Colombia y otros países americanos."},
                {"pregunta": "¿Qué dialecto colombiano se caracteriza por la entonación 'cantadita' y la aspiración de la 's'?", "respuesta": "costeño", "explicacion": "El dialecto costeño (Caribe colombiano) tiene rasgos fonéticos muy distintivos."},
                {"pregunta": "¿Qué fenómeno fonético implica la pronunciación de la 'n' final de sílaba como una 'm' bilabial (ej. 'pan' > 'pam')?", "respuesta": "bilabializacion de n", "explicacion": "Es un rasgo de algunas variedades dialectales, como el costeño."},
                {"pregunta": "¿Qué fenómeno fonético se refiere a la pronunciación de la 's' final de sílaba como una 'j' aspirada (ej. 'los' > 'loh')?", "respuesta": "aspiracion de s", "explicacion": "Es la aspiración de la /s/ final de sílaba, común en el Caribe y otras zonas cálidas."},
                {"pregunta": "¿Qué dialecto colombiano se caracteriza por la pronunciación de la 'r' vibrante simple como una 'rr' vibrante múltiple (ej. 'pero' > 'perro')?", "respuesta": "pastuso", "explicacion": "El dialecto pastuso (Nariño) tiene este rasgo distintivo."},
                {"pregunta": "¿Qué fenómeno fonético se refiere a la pérdida de la 'r' final de infinitivo (ej. 'comer' > 'comé')?", "respuesta": "apocope de r", "explicacion": "Común en algunas variedades dialectales, especialmente en el habla popular."},
                {"pregunta": "¿Qué fenómeno fonético se refiere a la pronunciación de la 'ch' como 'sh' (ej. 'muchacho' > 'mushasho')?", "respuesta": "africacion de ch", "explicacion": "Es un rasgo de algunas variedades dialectales, especialmente en el habla rural o popular de algunas zonas."},
                {"pregunta": "¿Qué dialecto colombiano es conocido por su 'cantadito' peculiar y el uso del voseo?", "respuesta": "santandereano", "explicacion": "El santandereano tiene una entonación y voseo distintivos."},
                {"pregunta": "¿Qué fenómeno fonético se refiere a la pronunciación de la 'd' final de palabra como 'z' (ej. 'verdad' > 'verdaz')?", "respuesta": "asibilacion de d", "explicacion": "Es un rasgo de algunas variedades dialectales, especialmente en el habla popular."},
                {"pregunta": "¿Qué fenómeno fonético se refiere a la pérdida de la 'b' o 'v' intervocálica (ej. 'saber' > 'saer')?", "respuesta": "elision de b/v intervocálica", "explicacion": "Es una relajación fonética común en el español coloquial de muchas zonas."},
                {"pregunta": "¿Qué dialecto colombiano es conocido por su entonación neutra y la ausencia de aspiración de la 's'?", "respuesta": "rolo", "explicacion": "El dialecto rolo o bogotano se percibe a menudo como el más 'neutro' o estándar en Colombia."},
                {"pregunta": "¿Qué fenómeno fonético se refiere a la vocalización de la 'l' o 'r' en posición implosiva a 'i' (ej. 'sol' > 'soi')?", "respuesta": "vocalizacion de l/r", "explicacion": "Es un rasgo de algunas variedades dialectales, especialmente en el habla popular."},

                # 3. Morfosintaxis Regional en Colombia (20 ejercicios)
                {"pregunta": "¿Qué fenómeno pronominal, muy extendido en Colombia, implica el uso de 'vos' en lugar de 'tú' o 'usted' para la segunda persona del singular?", "respuesta": "voseo", "explicacion": "El voseo es un rasgo morfosintáctico distintivo de gran parte de Colombia, con diferentes conjugaciones verbales según la región."},
                {"pregunta": "¿Qué tipo de voseo es el más común en la zona andina de Colombia (ej. 'vos comés', 'vos tenés')?", "respuesta": "voseo verbal", "explicacion": "Se utiliza 'vos' como pronombre sujeto y un verbo con terminación en '-és' o '-ís' para el presente de indicativo."},
                {"pregunta": "¿Qué forma de tratamiento se utiliza en Colombia para la segunda persona del plural, a diferencia de 'vosotros' en España?", "respuesta": "ustedes", "explicacion": "El uso de 'ustedes' para la segunda persona del plural es universal en América, incluyendo Colombia."},
                {"pregunta": "En Colombia, el uso del artículo con nombres propios de persona (ej. 'la María', 'el Juan') es un rasgo dialectal. ¿Verdadero o Falso?", "respuesta": "verdadero", "explicacion": "Es común en el habla coloquial de muchas regiones de Colombia, aunque no es normativo en el español estándar."},
                {"pregunta": "¿Qué fenómeno morfosintáctico se refiere al uso de diminutivos (ej. 'casita', 'ahorita') con gran frecuencia en Colombia?", "respuesta": "diminutivos", "explicacion": "El uso abundante de diminutivos es una característica del español colombiano, a menudo para expresar afecto o cortesía."},
                {"pregunta": "¿Qué fenómeno se refiere al uso de 'le' como objeto directo para personas masculinas (ej. 'le vi')?", "respuesta": "leismo", "explicacion": "El leísmo es el uso de 'le' en lugar de 'lo' para el objeto directo, común en algunas zonas de Colombia."},
                {"pregunta": "¿Qué fenómeno se refiere al uso de 'la' como objeto indirecto para personas femeninas (ej. 'la di un regalo')?", "respuesta": "laismo", "explicacion": "El laísmo es el uso de 'la' en lugar de 'le' para el objeto indirecto femenino, menos común en Colombia que en España."},
                {"pregunta": "¿Qué fenómeno se refiere al uso de 'lo' como objeto indirecto para personas masculinas (ej. 'lo di un regalo')?", "respuesta": "loismo", "explicacion": "El loísmo es el uso de 'lo' en lugar de 'le' para el objeto indirecto masculino, también menos común en Colombia."},
                {"pregunta": "¿Qué fenómeno morfosintáctico implica la omisión del pronombre sujeto cuando es obvio por el contexto (ej. 'Comemos mucho')?", "respuesta": "sujeto elíptico", "explicacion": "Es una característica general del español, pero su uso puede variar en frecuencia regionalmente."},
                {"pregunta": "¿Qué tipo de oraciones impersonales con 'se' son muy comunes en Colombia (ej. 'Aquí se come bien')?", "respuesta": "impersonales con se", "explicacion": "Estas construcciones son muy productivas en el español colombiano para expresar acciones sin un sujeto específico."},
                {"pregunta": "¿Qué fenómeno morfosintáctico se refiere al uso de la preposición 'en' en lugar de 'a' con verbos de movimiento (ej. 'voy en la casa')?", "respuesta": "uso de 'en' por 'a'", "explicacion": "Es un rasgo dialectal en algunas zonas de Colombia."},
                {"pregunta": "¿Qué fenómeno morfosintáctico se refiere al uso de la doble negación (ej. 'No vino nadie')?", "respuesta": "doble negacion", "explicacion": "Es un rasgo estándar del español y se mantiene en Colombia."},
                {"pregunta": "¿Qué fenómeno morfosintáctico implica el uso del pretérito perfecto simple (ej. 'comí') en lugar del compuesto (ej. 'he comido') para acciones recientes en el pasado?", "respuesta": "preferencia por preterito simple", "explicacion": "En gran parte de América, incluyendo Colombia, el pretérito simple es el uso preferido para acciones pasadas, incluso recientes, a diferencia de España."},
                {"pregunta": "¿Qué fenómeno morfosintáctico se refiere al uso del infinitivo personal (ej. 'al yo llegar')?", "respuesta": "infinitivo personal", "explicacion": "Es un rasgo propio del gallego-portugués y no es estándar en el español colombiano."},
                {"pregunta": "¿Qué fenómeno morfosintáctico se refiere a la colocación de los pronombres clíticos antes del verbo en imperativo negativo (ej. 'no me digas')?", "respuesta": "proclisis en imperativo negativo", "explicacion": "Es la norma en español y se mantiene en Colombia."},
                {"pregunta": "¿Qué fenómeno morfosintáctico se refiere al uso de 'qué' como adverbio de cantidad (ej. '¡Qué bonito!')?", "respuesta": "que adverbial", "explicacion": "Es un uso estándar del español y se mantiene en Colombia."},
                {"pregunta": "¿Qué fenómeno morfosintáctico se refiere al uso de 'lo' neutro (ej. 'lo bueno')?", "respuesta": "lo neutro", "explicacion": "Es un uso estándar del español y se mantiene en Colombia."},
                {"pregunta": "¿Qué fenómeno morfosintáctico se refiere a la formación de adverbios en '-mente' (ej. 'rápidamente')?", "respuesta": "adverbios en -mente", "explicacion": "Es un proceso de formación de palabras estándar en español y se mantiene en Colombia."},
                {"pregunta": "¿Qué fenómeno morfosintáctico se refiere al uso de la construcción 'ir a + infinitivo' para el futuro (ej. 'voy a comer')?", "respuesta": "perifrasis de futuro", "explicacion": "Es la forma más común de expresar el futuro en el español coloquial de Colombia y otros países."},
                {"pregunta": "¿Qué fenómeno morfosintáctico se refiere al uso de 'estar + gerundio' para acciones en progreso (ej. 'estoy comiendo')?", "respuesta": "perifrasis de gerundio", "explicacion": "Es una construcción estándar del español y se mantiene en Colombia."},

                # 4. Léxico Regional y Americanismos en Colombia (20 ejercicios)
                {"pregunta": "¿Qué tipo de palabras son 'papa', 'maíz', 'cacao', provenientes de lenguas indígenas americanas?", "respuesta": "americanismos / indigenismos", "explicacion": "Son palabras de origen indígena que se incorporaron al español tras la Conquista y son comunes en el léxico colombiano."},
                {"pregunta": "¿Qué palabra colombiana se usa para referirse a un 'autobús'?", "respuesta": "buseta", "explicacion": "Es un colombianismo muy extendido."},
                {"pregunta": "¿Qué palabra colombiana se usa para referirse a una 'tienda pequeña' o 'colmado'?", "respuesta": "tienda / miscelanea", "explicacion": "El ALEC documenta estas variaciones léxicas regionales."},
                {"pregunta": "¿Qué palabra colombiana se usa para referirse a un 'niño' o 'joven'?", "respuesta": "pelao / chino", "explicacion": "Son ejemplos de colombianismos para referirse a personas jóvenes."},
                {"pregunta": "¿Qué palabra colombiana se usa para referirse a una 'persona de Bogotá'?", "respuesta": "rolo", "explicacion": "Es un gentilicio coloquial para los habitantes de Bogotá."},
                {"pregunta": "¿Qué palabra colombiana se usa para referirse a una 'fiesta' o 'reunión social'?", "respuesta": "rumba", "explicacion": "Es un colombianismo extendido para referirse a una celebración."},
                {"pregunta": "¿Qué palabra colombiana se usa para referirse a 'dinero'?", "respuesta": "plata", "explicacion": "Es un americanismo muy común en Colombia y otros países."},
                {"pregunta": "¿Qué palabra colombiana se usa para referirse a un 'trabajo' o 'empleo'?", "respuesta": "camello", "explicacion": "Es un colombianismo coloquial para 'trabajo duro'."},
                {"pregunta": "¿Qué palabra colombiana se usa para referirse a 'estar de acuerdo' o 'entender'?", "respuesta": "pillar", "explicacion": "Es un colombianismo coloquial con ese significado."},
                {"pregunta": "¿Qué palabra colombiana se usa para referirse a una 'bebida alcohólica' (especialmente aguardiente)?", "respuesta": "guaro", "explicacion": "Es un colombianismo muy popular."},
                {"pregunta": "¿Qué palabra colombiana se usa para referirse a 'comida' en general?", "respuesta": "comida / rancho", "explicacion": "Rancho es más coloquial y rural."},
                {"pregunta": "¿Qué palabra colombiana se usa para referirse a 'perezoso'?", "respuesta": "gomelo", "explicacion": "Gomelo se refiere a una persona superficial o presumida, no perezosa. La respuesta correcta sería 'flojo' o 'vago'."},
                {"pregunta": "¿Qué palabra colombiana se usa para referirse a 'amigo' o 'compañero'?", "respuesta": "parcero", "explicacion": "Es un colombianismo muy común, especialmente entre jóvenes."},
                {"pregunta": "¿Qué palabra colombiana se usa para referirse a 'desorden' o 'caos'?", "respuesta": "despelote", "explicacion": "Es un colombianismo coloquial."},
                {"pregunta": "¿Qué palabra colombiana se usa para referirse a 'dar un abrazo'?", "respuesta": "abrazar / apapachar", "explicacion": "Apapachar es un mexicanismo, no un colombianismo común. La respuesta correcta es 'abrazar'."},
                {"pregunta": "¿Qué palabra colombiana se usa para referirse a 'persona astuta' o 'lista'?", "respuesta": "avispado", "explicacion": "Es un colombianismo con ese significado."},
                {"pregunta": "¿Qué palabra colombiana se usa para referirse a 'algo fácil'?", "respuesta": "papaya", "explicacion": "Es un colombianismo coloquial (ej. 'es una papaya' = es muy fácil)."},
                {"pregunta": "¿Qué palabra colombiana se usa para referirse a 'estar enojado'?", "respuesta": "estar bravo", "explicacion": "Es un uso común en Colombia."},
                {"pregunta": "¿Qué palabra colombiana se usa para referirse a 'un tipo de café suave'?", "respuesta": "tinto", "explicacion": "En Colombia, 'tinto' se refiere al café negro, sin leche."},
                {"pregunta": "¿Qué palabra colombiana se usa para referirse a 'una pequeña porción de comida'?", "respuesta": "pasaboca / pasabocas", "explicacion": "Es el término común para 'aperitivo' o 'bocadillo'."},

                # 5. Metodología y Recopilación de Datos del ALEC (20 ejercicios)
                {"pregunta": "¿Quién fue el director principal del ALEC?", "respuesta": "manuel alvar", "explicacion": "Manuel Alvar, filólogo español, dirigió el proyecto ALEC."},
                {"pregunta": "¿Qué tipo de informantes se priorizaron en las encuestas del ALEC: jóvenes o mayores?", "respuesta": "mayores", "explicacion": "Se buscaba el habla más tradicional y menos influida por los medios de comunicación."},
                {"pregunta": "¿Qué tipo de informantes se priorizaron en las encuestas del ALEC: urbanos o rurales?", "respuesta": "rurales", "explicacion": "Las zonas rurales suelen conservar mejor los rasgos dialectales tradicionales."},
                {"pregunta": "¿Cómo se llama el método de recolección de datos en el ALEC, donde el encuestador visita las localidades?", "respuesta": "encuesta directa", "explicacion": "Los datos se obtuvieron mediante entrevistas directas con los hablantes en sus lugares de origen."},
                {"pregunta": "¿Qué herramienta se utilizaba para registrar las respuestas de los informantes en el campo?", "respuesta": "cuestionario y grabadora", "explicacion": "Se usaban cuestionarios estandarizados y, en etapas posteriores, grabadoras de audio."},
                {"pregunta": "¿Qué es un 'corpus' lingüístico en el contexto del ALEC?", "respuesta": "conjunto de datos linguisticos", "explicacion": "El ALEC generó un vasto corpus de datos orales sobre el español colombiano."},
                {"pregunta": "¿Qué importancia tuvo la geografía en la selección de los puntos de encuesta del ALEC?", "respuesta": "primordial", "explicacion": "Se buscó una distribución geográfica representativa de las diferentes regiones colombianas."},
                {"pregunta": "¿Qué tipo de mapas se utilizan en el ALEC para visualizar la distribución de los fenómenos?", "respuesta": "mapas linguisticos", "explicacion": "Son mapas temáticos que muestran la distribución geográfica de los rasgos lingüísticos."},
                {"pregunta": "¿Qué es un 'informante' en la metodología del ALEC?", "respuesta": "persona que proporciona datos linguisticos", "explicacion": "Son los hablantes nativos entrevistados para obtener la información."},
                {"pregunta": "¿Qué se buscaba evitar con las 'preguntas indirectas' en las encuestas del ALEC?", "respuesta": "influir en la respuesta del informante", "explicacion": "Se quería obtener el uso natural y espontáneo de la lengua, sin sesgos."},
                {"pregunta": "¿Qué concepto se refiere a la transcripción fonética de los datos orales en el ALEC?", "respuesta": "transcripcion fonetica", "explicacion": "Los sonidos se representaban con símbolos fonéticos para mayor precisión."},
                {"pregunta": "El ALEC documenta solo el español estándar de Colombia. ¿Verdadero o Falso?", "respuesta": "falso", "explicacion": "Documenta las variedades dialectales, que son las que se desvían del estándar."},
                {"pregunta": "¿Qué tipo de datos etnográficos se recolectaron junto con los lingüísticos en el ALEC?", "respuesta": "cultura material, costumbres, oficios", "explicacion": "Se registraba información sobre la vida cotidiana, herramientas, agricultura, etc., para contextualizar el léxico."},
                {"pregunta": "¿Qué importancia tiene la 'comparación' en el análisis de los datos del ALEC?", "respuesta": "fundamental", "explicacion": "Al comparar las respuestas de diferentes puntos, se identifican las isoglosas y las áreas dialectales."},
                {"pregunta": "¿Qué se buscaba documentar al incluir preguntas sobre 'nombres de animales' o 'partes del arado'?", "respuesta": "lexico rural y especializado", "explicacion": "El ALEC se interesó por el léxico específico de la vida rural y tradicional."},
                {"pregunta": "¿Qué es una 'red de puntos' en la metodología de un atlas lingüístico?", "respuesta": "distribucion de localidades de encuesta", "explicacion": "Es el conjunto de puntos geográficos seleccionados para la recolección de datos."},
                {"pregunta": "¿Qué papel jugó la tecnología de la época (ej. grabadoras) en la elaboración del ALEC?", "respuesta": "facilitador de la recoleccion", "explicacion": "Permitió registrar el habla de forma más fiel y precisa."},
                {"pregunta": "¿Qué tipo de información se presenta en las 'láminas' del ALEC?", "respuesta": "mapas y comentarios", "explicacion": "Cada lámina muestra un mapa con la distribución de un fenómeno y un comentario explicativo."},
                {"pregunta": "¿Qué es la 'geografía lingüística'?", "respuesta": "estudio de la distribucion geografica de la lengua", "explicacion": "Es la disciplina que se encarga de cartografiar y analizar las variaciones lingüísticas en el espacio."},
                {"pregunta": "¿Qué importancia tiene el ALEC para la preservación del patrimonio lingüístico de Colombia?", "respuesta": "invaluable", "explicacion": "Documenta formas de hablar que podrían estar en riesgo de desaparecer, sirviendo como un registro histórico."},
            ]
        }
    }

def normalizar_respuesta(respuesta):
    """Normaliza una respuesta para comparación (quitar espacios, minúsculas, eliminar tildes, etc.)."""
    if isinstance(respuesta, str):
        # Eliminar tildes y convertir a minúsculas
        respuesta = respuesta.lower().replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')
        # Limpiar espacios extra
        respuesta = ' '.join(respuesta.split())
    return respuesta

def comparar_respuestas(respuesta_usuario, respuesta_correcta):
    """Compara la respuesta del usuario con la respuesta correcta después de normalizar."""
    return normalizar_respuesta(respuesta_usuario) == normalizar_respuesta(respuesta_correcta)

def iniciar_practica_alec():
    """Inicia la práctica de los conceptos del Atlas Lingüístico Etnográfico de Colombia (ALEC) en consola."""
    ejercicios_alec = cargar_ejercicios_alec()
    
    ejercicios = ejercicios_alec["Atlas Linguistico Etnografico de Colombia"]["Instituto Caro y Cuervo"]
    
    if not ejercicios:
        print("No hay ejercicios sobre el ALEC disponibles.")
        return

    random.shuffle(ejercicios) # Mezclar los ejercicios

    puntuacion = 0
    resultados = []

    print("\n--- ¡Bienvenido a la Práctica sobre el Atlas Lingüístico Etnográfico de Colombia (ALEC)! ---")
    print("Para cada pregunta, identifica el concepto clave, el fenómeno o responde Verdadero/Falso.")
    print("\nConceptos clave a identificar:")
    print("  - **atlas linguistico etnografico de colombia:** Significado de ALEC.")
    print("  - **instituto caro y cuervo:** Institución responsable.")
    print("  - **registrar la variacion dialectal:** Objetivo principal.")
    print("  - **isoglosas:** Mapas para representar la distribución.")
    print("  - **dialectologia:** Disciplina base.")
    print("  - **relacion con la cultura y costumbres:** Significado de 'etnográfico'.")
    print("  - **seis:** Número de tomos principales.")
    print("  - **todos los niveles sociales:** Tipo de datos recolectados.")
    print("  - **localidad donde se recolectan datos:** Significado de 'punto de encuesta'.")
    print("  - **fundamental:** Importancia del ALEC para el español americano.")
    print("  - **preguntas indirectas:** Tipo de preguntas para obtener datos.")
    print("  - **cuestionario y grabadora:** Herramientas de registro.")
    print("  - **dialecto:** Variación de una lengua según la región.")
    print("  - **seseo:** Pronunciación de 'c'/'z' como 's'.")
    print("  - **yeismo:** Pronunciación de 'll' como 'y'.")
    print("  - **aspiracion de -s:** Aspiración o pérdida de la -s final de sílaba.")
    print("  - **lambdacismo y rotacismo:** Neutralización de /l/ y /r/ implosivas.")
    print("  - **cundiboyacense:** Dialecto con ritmo lento y entonación particular.")
    print("  - **ceceo:** Pronunciación de 's' como 'c'/'z' (no en Colombia).")
    print("  - **paisa:** Dialecto con 'rr' y 'ch' fuertes.")
    print("  - **elision de d intervocálica:** Omisión de la 'd' intervocálica.")
    print("  - **relajacion de j:** Pérdida de la 'j' o 'g' final de sílaba.")
    print("  - **costeño:** Dialecto con entonación 'cantadita' y aspiración de 's'.")
    print("  - **bilabializacion de n:** Pronunciación de 'n' final como 'm'.")
    print("  - **pastuso:** Dialecto con 'r' vibrante simple como 'rr'.")
    print("  - **apocope de r:** Pérdida de la 'r' final de infinitivo.")
    print("  - **africacion de ch:** Pronunciación de 'ch' como 'sh'.")
    print("  - **santandereano:** Dialecto con entonación y voseo distintivos.")
    print("  - **asibilacion de d:** Pronunciación de 'd' final como 'z'.")
    print("  - **elision de b/v intervocálica:** Pérdida de 'b' o 'v' intervocálica.")
    print("  - **rolo:** Dialecto con entonación neutra.")
    print("  - **vocalizacion de l/r:** Vocalización de 'l' o 'r' implosivas a 'i'.")
    print("  - **voseo:** Uso de 'vos' en lugar de 'tú' o 'usted'.")
    print("  - **voseo verbal:** Tipo de voseo en la zona andina.")
    print("  - **ustedes:** Forma de tratamiento para la segunda persona del plural en Colombia.")
    print("  - **diminutivos:** Uso frecuente de 'casita', 'ahorita'.")
    print("  - **leismo:** Uso de 'le' como objeto directo para personas masculinas.")
    print("  - **laismo:** Uso de 'la' como objeto indirecto para personas femeninas.")
    print("  - **loismo:** Uso de 'lo' como objeto indirecto para personas masculinas.")
    print("  - **sujeto elíptico:** Omisión del pronombre sujeto.")
    print("  - **impersonales con se:** Oraciones impersonales con 'se' (ej. 'Aquí se come bien').")
    print("  - **uso de 'en' por 'a':** Uso de 'en' con verbos de movimiento.")
    print("  - **doble negacion:** Uso de 'no' y otro elemento negativo.")
    print("  - **preferencia por preterito simple:** Uso de 'comí' en lugar de 'he comido'.")
    print("  - **proclisis en imperativo negativo:** Pronombres clíticos antes del verbo en imperativo negativo.")
    print("  - **que adverbial:** Uso de 'qué' como adverbio de cantidad.")
    print("  - **lo neutro:** Uso de 'lo' neutro (ej. 'lo bueno').")
    print("  - **adverbios en -mente:** Formación de adverbios en '-mente'.")
    print("  - **perifrasis de futuro:** Uso de 'ir a + infinitivo'.")
    print("  - **perifrasis de gerundio:** Uso de 'estar + gerundio'.")
    print("  - **americanismos / indigenismos:** Palabras de origen indígena.")
    print("  - **buseta:** Palabra colombiana para 'autobús'.")
    print("  - **tienda / miscelanea:** Palabra colombiana para 'tienda pequeña'.")
    print("  - **pelao / chino:** Palabra colombiana para 'niño' o 'joven'.")
    print("  - **rolo:** Palabra colombiana para 'persona de Bogotá'.")
    print("  - **rumba:** Palabra colombiana para 'fiesta'.")
    print("  - **plata:** Palabra colombiana para 'dinero'.")
    print("  - **camello:** Palabra colombiana para 'trabajo'.")
    print("  - **pillar:** Palabra colombiana para 'estar de acuerdo' o 'entender'.")
    print("  - **guaro:** Palabra colombiana para 'bebida alcohólica'.")
    print("  - **comida / rancho:** Palabra colombiana para 'comida'.")
    print("  - **flojo / vago:** Palabra colombiana para 'perezoso'.")
    print("  - **parcero:** Palabra colombiana para 'amigo'.")
    print("  - **despelote:** Palabra colombiana para 'desorden'.")
    print("  - **abrazar:** Palabra colombiana para 'dar un abrazo'.")
    print("  - **avispado:** Palabra colombiana para 'persona astuta'.")
    print("  - **papaya:** Palabra colombiana para 'algo fácil'.")
    print("  - **estar bravo:** Palabra colombiana para 'estar enojado'.")
    print("  - **tinto:** Palabra colombiana para 'tipo de café suave'.")
    print("  - **pasaboca / pasabocas:** Palabra colombiana para 'pequeña porción de comida'.")
    print("  - **manuel alvar:** Director principal del ALEC.")
    print("  - **mayores:** Tipo de informantes priorizados (edad).")
    print("  - **rurales:** Tipo de informantes priorizados (ubicación).")
    print("  - **encuesta directa:** Método de recolección de datos.")
    print("  - **transcripcion fonetica:** Representación de sonidos con símbolos.")
    print("  - **cultura material, costumbres, oficios:** Datos etnográficos recolectados.")
    print("  - **geografia linguistica:** Estudio de la distribución geográfica de la lengua.")
    print("  - **invaluable:** Importancia del ALEC para la preservación del patrimonio.")
    print("  - **verdadero / falso:** Para preguntas dicotómicas.")
    print(f"\nTienes {len(ejercicios)} ejercicios para practicar.\n")

    for i, ejercicio in enumerate(ejercicios):
        print(f"\n--- Ejercicio {i + 1} de {len(ejercicios)} ---")
        print(f"Pregunta: {ejercicio['pregunta']}")
        
        respuesta_usuario = input("Tu respuesta: ").strip()

        es_correcta = comparar_respuestas(respuesta_usuario, ejercicio['respuesta'])

        if es_correcta:
            print("¡Correcto! ✅")
            puntuacion += 1
        else:
            print("Incorrecto. ❌")
        
        print(f"La respuesta correcta era: **{ejercicio['respuesta']}**")
        print(f"Explicación: {ejercicio['explicacion']}")
        
        resultados.append({
            "pregunta": ejercicio['pregunta'],
            "tu_respuesta": respuesta_usuario,
            "correcta": es_correcta,
            "respuesta_correcta": ejercicio['respuesta'],
            "explicacion": ejercicio['explicacion']
        })

    print("\n--- Práctica Terminada ---")
    print(f"Has obtenido {puntuacion} de {len(ejercicios)} respuestas correctas.")
    print("\n--- Resumen de Resultados ---")
    for res in resultados:
        estado = "✅ CORRECTO" if res['correcta'] else "❌ INCORRECTO"
        print(f"\nPregunta: {res['pregunta']}")
        print(f"Tu respuesta: {res['tu_respuesta']}")
        print(f"Respuesta correcta: **{res['respuesta_correcta']}**")
        print(f"Estado: {estado}")
        print(f"Explicación: {res['explicacion']}")
    
    print("\n¡Espero que esta práctica te ayude a dominar la fascinante historia de la lengua castellana según el ALEC!")

if __name__ == "__main__":
    iniciar_practica_alec()
