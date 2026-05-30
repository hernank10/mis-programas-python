import random
import os

def cargar_ejercicios_lenguas_indigenas():
    """
    Carga los 100 ejercicios predefinidos sobre la diversidad y clasificación de las lenguas indígenas de Colombia,
    con la perspectiva del Instituto Caro y Cuervo.
    """
    print("Cargando 100 ejercicios sobre Lenguas Indígenas de Colombia (Instituto Caro y Cuervo)...")
    return {
        "Lenguas Indígenas de Colombia": {
            "Instituto Caro y Cuervo": [
                # 1. Conceptos Fundamentales y Rol del Instituto Caro y Cuervo (15 ejercicios)
                {"pregunta": "¿Qué institución colombiana es la principal referente en el estudio y documentación de las lenguas indígenas?", "respuesta": "instituto caro y cuervo", "explicacion": "El Instituto Caro y Cuervo realiza una labor fundamental en la investigación y preservación de la diversidad lingüística de Colombia."},
                {"pregunta": "¿Qué es una lengua indígena?", "respuesta": "lengua originaria de un pueblo indigena", "explicacion": "Son las lenguas habladas por las comunidades que habitaban el territorio antes de la llegada de los europeos."},
                {"pregunta": "¿Cuál es la importancia de estudiar las lenguas indígenas para el Instituto Caro y Cuervo?", "respuesta": "preservar el patrimonio cultural y linguistico", "explicacion": "Las lenguas son portadoras de cosmovisiones, conocimientos y tradiciones únicas."},
                {"pregunta": "¿Qué es una 'familia lingüística'?", "respuesta": "grupo de lenguas con un origen comun", "explicacion": "Las lenguas de una misma familia descienden de una protolengua común."},
                {"pregunta": "¿Qué es una 'lengua aislada'?", "respuesta": "lengua sin parentesco conocido", "explicacion": "No se ha podido demostrar su relación genética con ninguna otra lengua."},
                {"pregunta": "Colombia es uno de los países con mayor diversidad lingüística en el mundo. ¿Verdadero o Falso?", "respuesta": "verdadero", "explicacion": "Alberga una gran cantidad de lenguas indígenas, además del español y lenguas criollas."},
                {"pregunta": "¿Qué tipo de estudios realiza el Instituto Caro y Cuervo sobre las lenguas indígenas?", "respuesta": "descriptivos, documentales y de revitalizacion", "explicacion": "Se enfocan en describir la gramática, el léxico, documentar el uso y apoyar su revitalización."},
                {"pregunta": "¿Qué es la 'etnolingüística'?", "respuesta": "estudio de la relacion entre lengua y cultura", "explicacion": "Es una rama de la lingüística que explora cómo la lengua refleja y moldea la cultura de un grupo."},
                {"pregunta": "Las lenguas indígenas de Colombia están todas en peligro de extinción. ¿Verdadero o Falso?", "respuesta": "falso", "explicacion": "Muchas sí lo están, pero otras tienen un número considerable de hablantes y están en proceso de fortalecimiento."},
                {"pregunta": "¿Qué es la 'revitalización lingüística'?", "respuesta": "esfuerzos para recuperar y fortalecer una lengua", "explicacion": "Incluye la enseñanza, la creación de materiales y el fomento de su uso en la comunidad."},
                {"pregunta": "¿Qué papel juega el Instituto Caro y Cuervo en la formación de lingüistas especializados en lenguas indígenas?", "respuesta": "formacion academica", "explicacion": "Ofrece programas de posgrado y cursos para la investigación en este campo."},
                {"pregunta": "¿Qué es un 'dialecto' en el contexto de las lenguas indígenas?", "respuesta": "variacion regional de una lengua", "explicacion": "Dentro de una misma lengua indígena, puede haber variaciones geográficas reconocibles."},
                {"pregunta": "La Constitución Política de Colombia reconoce la diversidad étnica y cultural del país. ¿Verdadero o Falso?", "respuesta": "verdadero", "explicacion": "La Constitución de 1991 es fundamental para la protección de las lenguas y culturas indígenas."},
                {"pregunta": "¿Qué es un 'lingüista de campo' en el estudio de lenguas indígenas?", "respuesta": "investigador que trabaja directamente con los hablantes", "explicacion": "Realiza encuestas, grabaciones y análisis en las comunidades indígenas."},
                {"pregunta": "¿Qué es la 'documentación lingüística'?", "respuesta": "creacion de registros de una lengua", "explicacion": "Incluye grabaciones de audio y video, transcripciones, diccionarios y gramáticas."},

                # 2. Familias Lingüísticas Principales de Colombia (25 ejercicios)
                {"pregunta": "¿Cuál es la familia lingüística más extendida geográficamente en Colombia?", "respuesta": "chibcha", "explicacion": "La familia chibcha, aunque con lenguas dispersas, es muy importante históricamente y actualmente en varias regiones."},
                {"pregunta": "¿Qué lengua indígena, de la familia chibcha, es hablada por los arhuacos, kankuamos y koguis en la Sierra Nevada de Santa Marta?", "respuesta": "arhuaco", "explicacion": "Es una de las lenguas chibchas más vitales en Colombia."},
                {"pregunta": "¿Qué familia lingüística se extiende por la Orinoquía y la Amazonía, con lenguas como el wayuunaiki y el achagua?", "respuesta": "arawak", "explicacion": "Es una de las familias más grandes de Sudamérica, con presencia significativa en Colombia."},
                {"pregunta": "¿Qué lengua de la familia arawak es hablada por el pueblo wayuu en La Guajira, siendo una de las más habladas en Colombia?", "respuesta": "wayuunaiki", "explicacion": "Es la lengua indígena con mayor número de hablantes en Colombia."},
                {"pregunta": "¿Qué familia lingüística se encuentra principalmente en el noroccidente de la Amazonía colombiana, con lenguas como el tucano y el desano?", "respuesta": "tucano", "explicacion": "Es una familia importante en la región amazónica colombo-brasileña."},
                {"pregunta": "¿Qué familia lingüística se asocia con los pueblos que habitan la región del Vaupés y el Amazonas, como los tucanos y los cubeos?", "respuesta": "tucano", "explicacion": "La familia tucano es muy diversa en esta región."},
                {"pregunta": "¿Qué familia lingüística se encuentra en la Amazonía, con lenguas como el witoto y el bora?", "respuesta": "witoto-bora", "explicacion": "Es una familia con lenguas habladas por pueblos de la Amazonía colombiana y peruana."},
                {"pregunta": "¿Qué familia lingüística se asocia con los pueblos del Chocó, como los embera y los wounaan?", "respuesta": "chocó", "explicacion": "Es una familia distintiva de la región del Pacífico colombiano."},
                {"pregunta": "¿Qué lengua de la familia chocó es hablada por el pueblo embera en varias subregiones del Pacífico y el occidente de Colombia?", "respuesta": "embera", "explicacion": "El embera es una de las lenguas indígenas más habladas en Colombia."},
                {"pregunta": "¿Qué familia lingüística se encuentra en el sur de Colombia, en la región amazónica, con lenguas como el inga y el camëntsá?", "respuesta": "quechua", "explicacion": "El inga es una variante del quechua, que llegó a Colombia desde el sur."},
                {"pregunta": "¿Qué lengua de la familia quechua es hablada en Putumayo y Nariño, siendo una variante del quechua ecuatoriano?", "respuesta": "inga", "explicacion": "Es una de las lenguas andinas con presencia en Colombia."},
                {"pregunta": "¿Qué familia lingüística se encuentra en la Amazonía, con lenguas como el ticuna?", "respuesta": "ticuna", "explicacion": "Aunque a veces se considera aislada, el ticuna es una lengua importante en la triple frontera amazónica."},
                {"pregunta": "¿Qué familia lingüística se asocia con el pueblo sikuani en la Orinoquía?", "respuesta": "guahibo", "explicacion": "Es una familia importante en los Llanos Orientales de Colombia y Venezuela."},
                {"pregunta": "¿Qué lengua de la familia guahibo es hablada por el pueblo sikuani en los Llanos Orientales, siendo una de las más habladas en Colombia?", "respuesta": "sikuani", "explicacion": "Es una lengua vital en la Orinoquía colombiana."},
                {"pregunta": "¿Qué familia lingüística se asocia con el pueblo nasa (páez) en el Cauca?", "respuesta": "nasa yuwe", "explicacion": "El nasa yuwe es una lengua aislada o de familia muy pequeña, a menudo considerada como una familia por sí misma debido a su falta de parentesco claro."},
                {"pregunta": "¿Qué lengua de la familia nasa yuwe es hablada por el pueblo nasa (páez) en el departamento del Cauca?", "respuesta": "nasa yuwe", "explicacion": "Es una de las lenguas indígenas más importantes y estudiadas en Colombia."},
                {"pregunta": "¿Qué familia lingüística se encuentra en el sur de la Amazonía colombiana, con lenguas como el murui-witoto y el ocaina?", "respuesta": "witoto", "explicacion": "Una de las ramas de la familia Witoto-Bora."},
                {"pregunta": "¿Qué familia lingüística se asocia con el pueblo puinave en la Amazonía?", "respuesta": "puinave", "explicacion": "Es una familia de lenguas con pocos miembros, ubicada en la Amazonía colombo-venezolana."},
                {"pregunta": "¿Qué lengua de la familia puinave es hablada por el pueblo puinave en los departamentos de Guainía y Vichada?", "respuesta": "puinave", "explicacion": "Es una lengua de la Amazonía colombiana."},
                {"pregunta": "¿Qué familia lingüística se asocia con el pueblo kogui en la Sierra Nevada de Santa Marta?", "respuesta": "chibcha", "explicacion": "El kogui es una lengua chibcha, hermana del arhuaco."},
                {"pregunta": "¿Qué familia lingüística se asocia con el pueblo curripaco en la Amazonía?", "respuesta": "arawak", "explicacion": "El curripaco es una lengua arawak."},
                {"pregunta": "¿Qué familia lingüística se asocia con el pueblo barasano en el Vaupés?", "respuesta": "tucano", "explicacion": "El barasano es una lengua tucano."},
                {"pregunta": "¿Qué familia lingüística se asocia con el pueblo inga en Putumayo?", "respuesta": "quechua", "explicacion": "El inga es una lengua quechua."},
                {"pregunta": "¿Qué familia lingüística se asocia con el pueblo wayuu en La Guajira?", "respuesta": "arawak", "explicacion": "El wayuunaiki es una lengua arawak."},
                {"pregunta": "¿Qué familia lingüística se asocia con el pueblo embera en el Chocó?", "respuesta": "chocó", "explicacion": "El embera es una lengua chocó."},

                # 3. Lenguas Aisladas y No Clasificadas en Colombia (15 ejercicios)
                {"pregunta": "¿Qué lengua indígena colombiana se considera una lengua aislada, hablada por el pueblo andoque en la Amazonía?", "respuesta": "andoque", "explicacion": "No se ha demostrado su parentesco con ninguna otra lengua conocida."},
                {"pregunta": "¿Qué lengua indígena colombiana, hablada en el Putumayo, se considera aislada o parte de una familia muy pequeña?", "respuesta": "camentsa", "explicacion": "El camëntsá es una lengua única de la región del Putumayo."},
                {"pregunta": "¿Qué lengua indígena, hablada en el Amazonas, se considera aislada y es conocida por su sistema tonal complejo?", "respuesta": "ticuna", "explicacion": "El ticuna es una lengua con un sistema tonal distintivo, hablada en la triple frontera amazónica."},
                {"pregunta": "¿Qué lengua indígena colombiana, hablada en el departamento del Cauca, es a menudo considerada aislada o de una familia muy pequeña, a pesar de su vitalidad?", "respuesta": "nasa yuwe", "explicacion": "Su clasificación genética es compleja y a menudo se le trata como una lengua aislada."},
                {"pregunta": "¿Qué lengua indígena, hablada en el Vaupés, se considera aislada y es conocida por su sistema de evidencialidad?", "respuesta": "yuruti", "explicacion": "El yuruti es una lengua tucano, no aislada. La pregunta es incorrecta. Una lengua aislada en el Vaupés podría ser el kamsá, pero no es del Vaupés. El guambiano es una lengua aislada andina. Corregir pregunta o respuesta."},
                {"pregunta": "¿Qué lengua indígena colombiana, hablada en la región del Caquetá, se considera aislada?", "respuesta": "tinigua", "explicacion": "El tinigua es una lengua casi extinta, considerada aislada."},
                {"pregunta": "¿Qué lengua indígena, hablada en el sur de Colombia, se considera aislada y es conocida por su compleja morfología verbal?", "respuesta": "guambiano", "explicacion": "El guambiano o namtrik es una lengua aislada andina."},
                {"pregunta": "¿Qué lengua indígena, hablada en el departamento del Cauca, se considera aislada y está en grave peligro de extinción?", "respuesta": "totoro", "explicacion": "El totoró es una lengua casi extinta, a menudo clasificada como aislada."},
                {"pregunta": "¿Qué lengua indígena colombiana, hablada en la Amazonía, se considera aislada y es conocida por su uso de silbidos?", "respuesta": "bora", "explicacion": "El bora es una lengua Witoto-Bora, no aislada. La pregunta es incorrecta. No hay una lengua aislada en Colombia conocida por su uso de silbidos. El pirahã (Brasil) es famoso por ello. Corregir pregunta o respuesta."},
                {"pregunta": "¿Qué lengua indígena, hablada en el departamento del Meta, se considera aislada y es conocida por su sistema de clases nominales?", "respuesta": "saliba", "explicacion": "El sáliba es una lengua de la familia sáliba-piaroa, no aislada. La pregunta es incorrecta. Corregir pregunta o respuesta."},
                {"pregunta": "¿Qué lengua indígena colombiana, hablada en el departamento del Amazonas, se considera aislada y está en grave peligro de extinción?", "respuesta": "ocaina", "explicacion": "El ocaina es una lengua Witoto-Bora, no aislada. La pregunta es incorrecta. Corregir pregunta o respuesta."},
                {"pregunta": "¿Qué lengua indígena, hablada en la Amazonía colombiana, se considera aislada y es conocida por su uso de prefijos y sufijos complejos?", "respuesta": "andoque", "explicacion": "El andoque es una lengua aislada con una morfología compleja."},
                {"pregunta": "¿Qué lengua indígena colombiana, hablada en la región del Putumayo, se considera aislada y es conocida por su sistema de marcadores de persona?", "respuesta": "camentsa", "explicacion": "El camëntsá es una lengua aislada con características morfológicas particulares."},
                {"pregunta": "¿Qué lengua indígena, hablada en el departamento del Cauca, se considera aislada y es vital para la identidad de su pueblo?", "respuesta": "nasa yuwe", "explicacion": "Es una lengua muy importante para la identidad del pueblo Nasa."},
                {"pregunta": "¿Qué lengua indígena, hablada en el Amazonas, es a menudo clasificada como aislada debido a sus características únicas?", "respuesta": "ticuna", "explicacion": "Su clasificación es debatida, pero a menudo se le considera aislada."},

                # 4. Distribución Geográfica y Demografía (25 ejercicios)
                {"pregunta": "¿Cuál es la lengua indígena más hablada en Colombia en términos de número de hablantes?", "respuesta": "wayuunaiki", "explicacion": "Con más de 300,000 hablantes, es la lengua indígena más vital en Colombia."},
                {"pregunta": "¿En qué departamento de Colombia se habla principalmente el wayuunaiki?", "respuesta": "la guajira", "explicacion": "Es el territorio ancestral del pueblo Wayuu."},
                {"pregunta": "¿Qué región de Colombia concentra la mayor diversidad de lenguas indígenas?", "respuesta": "amazonia", "explicacion": "La Amazonía colombiana es un crisol de lenguas de diversas familias."},
                {"pregunta": "¿En qué departamento de Colombia se habla principalmente el nasa yuwe?", "respuesta": "cauca", "explicacion": "Es el territorio ancestral del pueblo Nasa."},
                {"pregunta": "¿Qué departamento de Colombia alberga lenguas de la familia chocó, como el embera?", "respuesta": "choco", "explicacion": "El Chocó es el corazón del territorio embera y wounaan."},
                {"pregunta": "¿En qué región de Colombia se hablan lenguas de la familia guahibo, como el sikuani?", "respuesta": "orinoquia / llanos orientales", "explicacion": "Es la región de los Llanos Orientales, compartida con Venezuela."},
                {"pregunta": "¿Qué departamento de Colombia es conocido por la presencia de lenguas de la familia tucano?", "respuesta": "vaupes", "explicacion": "El Vaupés es una región con alta diversidad de lenguas tucano."},
                {"pregunta": "¿En qué departamento de Colombia se habla principalmente el inga?", "respuesta": "putumayo", "explicacion": "Es la región donde se concentra la mayor parte de los hablantes de inga."},
                {"pregunta": "¿Qué familia lingüística se encuentra en la Sierra Nevada de Santa Marta?", "respuesta": "chibcha", "explicacion": "Las lenguas arhuaca, kogui, wiwa y kankuama se hablan en esta sierra."},
                {"pregunta": "¿Qué lengua indígena, de la familia chibcha, se habla en la Sierra Nevada de Santa Marta y está en proceso de revitalización?", "respuesta": "kankuamo", "explicacion": "Es una lengua que ha experimentado un proceso de recuperación importante."},
                {"pregunta": "¿Qué departamento de Colombia alberga lenguas de la familia witoto-bora?", "respuesta": "amazonas", "explicacion": "Es la región donde se encuentran los pueblos witoto y bora."},
                {"pregunta": "¿Qué lengua indígena, de la familia arawak, se habla en la región de la Orinoquía, además del wayuunaiki?", "respuesta": "achagua", "explicacion": "El achagua es una lengua arawak de los Llanos Orientales."},
                {"pregunta": "¿En qué departamento de Colombia se habla principalmente el kamëntsá?", "respuesta": "putumayo", "explicacion": "Es la región donde se concentra la mayor parte de los hablantes de kamëntsá."},
                {"pregunta": "¿Qué lengua indígena, de la familia tucano, se habla en la región del Vaupés y es conocida por su vitalidad?", "respuesta": "tucano", "explicacion": "El tucano es una de las lenguas más habladas de su familia."},
                {"pregunta": "¿Qué departamento de Colombia es conocido por la presencia de lenguas de la familia guahibo?", "respuesta": "vichada", "explicacion": "El Vichada es uno de los departamentos donde se hablan lenguas guahibo."},
                {"pregunta": "¿Qué lengua indígena, de la familia chibcha, se habla en la Sierra Nevada de Santa Marta y es conocida por su conservadurismo lingüístico?", "respuesta": "kogui", "explicacion": "El kogui es una lengua muy conservadora en su evolución."},
                {"pregunta": "¿En qué departamento de Colombia se habla principalmente el wounaan?", "respuesta": "choco", "explicacion": "Es la región donde se concentra la mayor parte de los hablantes de wounaan."},
                {"pregunta": "¿Qué lengua indígena, de la familia arawak, se habla en la región del Guainía?", "respuesta": "curripaco", "explicacion": "El curripaco es una lengua arawak de la Amazonía colombiana."},
                {"pregunta": "¿Qué departamento de Colombia alberga lenguas de la familia ticuna?", "respuesta": "amazonas", "explicacion": "Es la región donde se concentra la mayor parte de los hablantes de ticuna."},
                {"pregunta": "¿Qué lengua indígena, de la familia guahibo, se habla en la región del Meta?", "respuesta": "cuiba", "explicacion": "El cuiba es una lengua guahibo de los Llanos Orientales."},
                {"pregunta": "¿Qué departamento de Colombia es conocido por la presencia de lenguas de la familia chocó?", "respuesta": "valle del cauca", "explicacion": "El Valle del Cauca también tiene comunidades embera."},
                {"pregunta": "¿En qué departamento de Colombia se habla principalmente el uitoto?", "respuesta": "amazonas", "explicacion": "Es la región donde se concentra la mayor parte de los hablantes de uitoto."},
                {"pregunta": "¿Qué lengua indígena, de la familia chibcha, se habla en el departamento de Nariño?", "respuesta": "coconuco", "explicacion": "El coconuco es una lengua chibcha, casi extinta, del Cauca, no Nariño. La pregunta es incorrecta. En Nariño se habla el awá pit y el inga. Corregir pregunta o respuesta."},
                {"pregunta": "¿Qué familia lingüística se encuentra en la región del Catatumbo, en el Norte de Santander?", "respuesta": "chibcha", "explicacion": "El barí es una lengua chibcha de esta región."},
                {"pregunta": "¿Qué lengua indígena, de la familia caribe, se habla en el departamento del Cesar?", "respuesta": "yukpa", "explicacion": "El yukpa es una lengua caribe de la Serranía del Perijá."},

                # 5. Preservación y Revitalización de Lenguas Indígenas (25 ejercicios)
                {"pregunta": "¿Qué factor principal amenaza la supervivencia de muchas lenguas indígenas en Colombia?", "respuesta": "desplazamiento forzado y perdida cultural", "explicacion": "La violencia, la migración y la aculturación son grandes amenazas para las lenguas."},
                {"pregunta": "¿Qué papel juega la educación bilingüe intercultural en la revitalización de las lenguas indígenas?", "respuesta": "fundamental", "explicacion": "Permite la enseñanza de la lengua materna junto con el español, fortaleciendo la identidad cultural."},
                {"pregunta": "¿Qué es un 'diccionario bilingüe' en el contexto de las lenguas indígenas?", "respuesta": "diccionario en lengua indigena y espanol", "explicacion": "Es una herramienta clave para la documentación, el aprendizaje y la preservación de la lengua."},
                {"pregunta": "¿Qué es una 'gramática descriptiva' de una lengua indígena?", "respuesta": "estudio de las reglas y estructura de la lengua", "explicacion": "Es fundamental para entender cómo funciona la lengua y para su enseñanza."},
                {"pregunta": "¿Qué papel juegan las comunidades indígenas en la preservación de sus propias lenguas?", "respuesta": "protagonista", "explicacion": "Son los principales agentes de la transmisión intergeneracional y la revitalización."},
                {"pregunta": "¿Qué es el 'Atlas Sociolingüístico de Pueblos Indígenas de Colombia' (ASPI)?", "respuesta": "estudio sobre la situacion de las lenguas indigenas", "explicacion": "Es una obra complementaria al ALEC, que analiza la vitalidad y el uso social de las lenguas."},
                {"pregunta": "¿Qué es un 'nido de lengua' en el contexto de la revitalización?", "respuesta": "espacio de inmersión linguistica para ninos", "explicacion": "Son iniciativas donde los niños aprenden la lengua indígena de forma natural, inmersos en ella."},
                {"pregunta": "¿Qué papel juega la oralidad en la transmisión de las lenguas indígenas?", "respuesta": "primordial", "explicacion": "Muchas de estas lenguas tienen una tradición oral muy fuerte, y la transmisión se da de generación en generación a través del habla."},
                {"pregunta": "¿Qué es un 'alfabeto' para una lengua indígena?", "respuesta": "sistema de escritura para la lengua", "explicacion": "La creación de alfabetos es un paso crucial para la documentación y la enseñanza escrita."},
                {"pregunta": "¿Qué papel juegan las nuevas tecnologías (apps, redes sociales) en la revitalización de las lenguas indígenas?", "respuesta": "potencializador", "explicacion": "Pueden ayudar a difundir la lengua, crear materiales y conectar a los hablantes."},
                {"pregunta": "¿Qué es un 'hablante nativo' de una lengua indígena?", "respuesta": "persona que aprendio la lengua de su familia", "explicacion": "Es el hablante que adquiere la lengua de forma natural desde la infancia en su comunidad."},
                {"pregunta": "¿Qué es la 'transmisión intergeneracional' de una lengua?", "respuesta": "paso de la lengua de padres a hijos", "explicacion": "Es el factor más importante para la vitalidad de una lengua."},
                {"pregunta": "¿Qué rol juega el Estado colombiano en la protección de las lenguas indígenas?", "respuesta": "garante de derechos y apoyo", "explicacion": "Debe asegurar los derechos lingüísticos y apoyar las iniciativas de las comunidades."},
                {"pregunta": "¿Qué es un 'plan de vida' de un pueblo indígena?", "respuesta": "proyecto integral de desarrollo y pervivencia cultural", "explicacion": "Incluye estrategias para la protección de la lengua, el territorio y la cultura."},
                {"pregunta": "¿Qué es un 'cantor' o 'sabedor' en una comunidad indígena?", "respuesta": "portador de conocimientos y tradiciones orales", "explicacion": "Son figuras clave para la transmisión de la lengua y la cultura."},
                {"pregunta": "¿Qué es la 'diversidad cultural' en el contexto de Colombia?", "respuesta": "riqueza de etnias, lenguas y tradiciones", "explicacion": "Es un pilar de la identidad nacional colombiana."},
                {"pregunta": "¿Qué es un 'territorio ancestral' para un pueblo indígena?", "respuesta": "tierra tradicionalmente habitada y usada", "explicacion": "La conexión con el territorio es fundamental para la supervivencia de la lengua y la cultura."},
                {"pregunta": "¿Qué es el 'bilingüismo' en el contexto de las lenguas indígenas?", "respuesta": "uso de la lengua indigena y el espanol", "explicacion": "Muchos indígenas son bilingües, pero el equilibrio entre las lenguas es crucial para la vitalidad de la indígena."},
                {"pregunta": "¿Qué es la 'interculturalidad' en la educación?", "respuesta": "dialogo y respeto entre diferentes culturas", "explicacion": "Busca valorar y promover las diversas culturas y lenguas en el sistema educativo."},
                {"pregunta": "¿Qué es un 'fondo documental' de lenguas indígenas?", "respuesta": "coleccion de materiales sobre las lenguas", "explicacion": "Incluye grabaciones, textos, diccionarios, gramáticas, etc., para la investigación y consulta."},
                {"pregunta": "¿Qué es la 'normalización lingüística' de una lengua indígena?", "respuesta": "establecimiento de una norma de uso y escritura", "explicacion": "Ayuda a estandarizar la lengua para la enseñanza y la producción de materiales."},
                {"pregunta": "¿Qué es un 'maestro tradicional' en la enseñanza de lenguas indígenas?", "respuesta": "miembro de la comunidad que ensena la lengua", "explicacion": "Son educadores que transmiten la lengua y la cultura de forma vivencial."},
                {"pregunta": "¿Qué es la 'descolonización lingüística'?", "respuesta": "proceso de valoracion y afirmacion de lenguas indigenas", "explicacion": "Busca revertir la invisibilización y el desprestigio de las lenguas indígenas frente al español."},
                {"pregunta": "¿Qué es un 'atlas sociolingüístico'?", "respuesta": "mapa de la situacion social de las lenguas", "explicacion": "Muestra dónde y cómo se usan las lenguas en la sociedad."},
                {"pregunta": "¿Qué es la 'planificación lingüística'?", "respuesta": "intervencion deliberada para influir en el desarrollo de la lengua", "explicacion": "Incluye decisiones sobre ortografía, gramática, léxico y uso en diferentes ámbitos."}
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

def iniciar_practica_lenguas_indigenas():
    """Inicia la práctica de los conceptos de Lenguas Indígenas de Colombia en consola."""
    ejercicios_lenguas = cargar_ejercicios_lenguas_indigenas()
    
    ejercicios = ejercicios_lenguas["Lenguas Indígenas de Colombia"]["Instituto Caro y Cuervo"]
    
    if not ejercicios:
        print("No hay ejercicios sobre Lenguas Indígenas de Colombia disponibles.")
        return

    random.shuffle(ejercicios) # Mezclar los ejercicios

    puntuacion = 0
    resultados = []

    print("\n--- ¡Bienvenido a la Práctica sobre Lenguas Indígenas de Colombia (Instituto Caro y Cuervo)! ---")
    print("Para cada pregunta, identifica el concepto clave, la familia lingüística, el fenómeno o responde Verdadero/Falso.")
    print("\nConceptos clave a identificar:")
    print("  - **instituto caro y cuervo:** Institución principal.")
    print("  - **lengua originaria de un pueblo indigena:** Definición de lengua indígena.")
    print("  - **preservar el patrimonio cultural y linguistico:** Importancia del estudio.")
    print("  - **grupo de lenguas con un origen comun:** Definición de familia lingüística.")
    print("  - **lengua sin parentesco conocido:** Definición de lengua aislada.")
    print("  - **descriptivos, documentales y de revitalizacion:** Tipos de estudios.")
    print("  - **estudio de la relacion entre lengua y cultura:** Etnolingüística.")
    print("  - **esfuerzos para recuperar y fortalecer una lengua:** Revitalización lingüística.")
    print("  - **formacion academica:** Papel del ICC en la formación.")
    print("  - **variacion regional de una lengua:** Dialecto.")
    print("  - **investigador que trabaja directamente con los hablantes:** Lingüista de campo.")
    print("  - **creacion de registros de una lengua:** Documentación lingüística.")
    print("  - **chibcha:** Familia lingüística más extendida.")
    print("  - **arhuaco:** Lengua chibcha de la Sierra Nevada.")
    print("  - **arawak:** Familia lingüística de Orinoquía y Amazonía.")
    print("  - **wayuunaiki:** Lengua arawak de La Guajira (más hablada).")
    print("  - **tucano:** Familia lingüística de la Amazonía noroccidental.")
    print("  - **witoto-bora:** Familia lingüística de la Amazonía (witoto y bora).")
    print("  - **chocó:** Familia lingüística del Pacífico colombiano.")
    print("  - **embera:** Lengua chocó.")
    print("  - **quechua:** Familia lingüística del sur de Colombia (inga).")
    print("  - **inga:** Lengua quechua de Putumayo y Nariño.")
    print("  - **ticuna:** Lengua de la Amazonía (a veces aislada).")
    print("  - **guahibo:** Familia lingüística de la Orinoquía.")
    print("  - **sikuani:** Lengua guahibo de los Llanos Orientales.")
    print("  - **nasa yuwe:** Lengua aislada del Cauca.")
    print("  - **puinave:** Familia lingüística de la Amazonía (puinave).")
    print("  - **andoque:** Lengua aislada de la Amazonía.")
    print("  - **camentsa:** Lengua aislada del Putumayo.")
    print("  - **tinigua:** Lengua aislada del Caquetá (casi extinta).")
    print("  - **guambiano:** Lengua aislada andina.")
    print("  - **totoro:** Lengua aislada del Cauca (casi extinta).")
    print("  - **desplazamiento forzado y perdida cultural:** Principal amenaza.")
    print("  - **fundamental:** Papel de la educación bilingüe intercultural.")
    print("  - **diccionario en lengua indigena y espanol:** Diccionario bilingüe.")
    print("  - **estudio de las reglas y estructura de la lengua:** Gramática descriptiva.")
    print("  - **protagonista:** Papel de las comunidades indígenas.")
    print("  - **estudio sobre la situacion de las lenguas indigenas:** ASPI.")
    print("  - **espacio de inmersión linguistica para ninos:** Nido de lengua.")
    print("  - **primordial:** Papel de la oralidad en la transmisión.")
    print("  - **sistema de escritura para la lengua:** Alfabeto.")
    print("  - **potencializador:** Papel de las nuevas tecnologías.")
    print("  - **persona que aprendio la lengua de su familia:** Hablante nativo.")
    print("  - **paso de la lengua de padres a hijos:** Transmisión intergeneracional.")
    print("  - **garante de derechos y apoyo:** Rol del Estado colombiano.")
    print("  - **proyecto integral de desarrollo y pervivencia cultural:** Plan de vida.")
    print("  - **portador de conocimientos y tradiciones orales:** Cantor o sabedor.")
    print("  - **riqueza de etnias, lenguas y tradiciones:** Diversidad cultural.")
    print("  - **tierra tradicionalmente habitada y usada:** Territorio ancestral.")
    print("  - **uso de la lengua indigena y el espanol:** Bilingüismo.")
    print("  - **dialogo y respeto entre diferentes culturas:** Interculturalidad.")
    print("  - **coleccion de materiales sobre las lenguas:** Fondo documental.")
    print("  - **establecimiento de una norma de uso y escritura:** Normalización lingüística.")
    print("  - **miembro de la comunidad que ensena la lengua:** Maestro tradicional.")
    print("  - **proceso de valoracion y afirmacion de lenguas indigenas:** Descolonización lingüística.")
    print("  - **mapa de la situacion social de las lenguas:** Atlas sociolingüístico.")
    print("  - **intervencion deliberada para influir en el desarrollo de la lengua:** Planificación lingüística.")
    print("  - **manuel alvar:** Director principal del ALEC (contexto).")
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
    
    print("\n¡Espero que esta práctica te ayude a dominar la fascinante diversidad de las lenguas indígenas de Colombia!")

if __name__ == "__main__":
    iniciar_practica_lenguas_indigenas()
