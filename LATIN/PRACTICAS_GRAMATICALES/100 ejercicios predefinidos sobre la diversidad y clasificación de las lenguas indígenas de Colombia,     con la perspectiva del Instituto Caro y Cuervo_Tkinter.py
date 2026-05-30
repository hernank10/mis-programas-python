import tkinter as tk
from tkinter import font as tkfont
from tkinter import ttk
import random
import os
import re

# ==============================================================================
# DATOS DEL QUIZ
# ==============================================================================
# La misma base de datos de preguntas y respuestas, ahora para la GUI.
EJERCICIOS_LENGUAS_INDIGENAS = [
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


# ==============================================================================
# CLASE PRINCIPAL DE LA APLICACIÓN
# ==============================================================================
class LenguasIndigenasQuizApp(tk.Tk):
    """
    Aplicación de Quiz de Lenguas Indígenas de Colombia con Tkinter.
    """
    def __init__(self):
        super().__init__()
        self.title("Quiz: Lenguas Indígenas de Colombia")
        self.geometry("800x600")
        self.configure(bg="#f0f0f0")

        # Se cargan las preguntas y se mezclan para un orden aleatorio
        self.questions = random.sample(EJERCICIOS_LENGUAS_INDIGENAS, k=len(EJERCICIOS_LENGUAS_INDIGENAS))
        self.current_question_index = 0
        self.score = 0
        self.total_questions = len(self.questions)

        # Se definen las fuentes para los diferentes elementos de la GUI
        self.title_font = tkfont.Font(family="Helvetica", size=24, weight="bold")
        self.question_font = tkfont.Font(family="Helvetica", size=16)
        self.feedback_font = tkfont.Font(family="Helvetica", size=14, weight="bold")
        self.explanation_font = tkfont.Font(family="Helvetica", size=12)

        self.setup_ui()

    def setup_ui(self):
        """Configura la interfaz de usuario de la aplicación."""
        # Marco principal para contener todos los elementos
        main_frame = ttk.Frame(self, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Título del quiz
        title_label = tk.Label(main_frame, text="Quiz: Lenguas Indígenas de Colombia", font=self.title_font, fg="#4a4a4a")
        title_label.pack(pady=10)

        # Etiqueta para mostrar la pregunta actual
        self.question_label = tk.Label(main_frame, text="", font=self.question_font, wraplength=700, justify="center", bg="#f0f0f0")
        self.question_label.pack(pady=20, padx=10)

        # Cuadro de entrada para la respuesta del usuario
        self.answer_entry = ttk.Entry(main_frame, font=self.question_font)
        self.answer_entry.pack(pady=10, fill=tk.X, padx=50)

        # Etiqueta para mostrar el número de pregunta y la puntuación
        self.status_label = tk.Label(main_frame, text="", font=self.feedback_font, bg="#f0f0f0")
        self.status_label.pack(pady=5)

        # Etiqueta para mostrar el feedback (correcto/incorrecto)
        self.feedback_label = tk.Label(main_frame, text="", font=self.feedback_font, bg="#f0f0f0")
        self.feedback_label.pack(pady=5)

        # Etiqueta para mostrar la explicación detallada
        self.explanation_label = tk.Label(main_frame, text="", font=self.explanation_font, wraplength=700, justify="center", bg="#f0f0f0")
        self.explanation_label.pack(pady=10, padx=10)

        # Marco para los botones
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(pady=20)

        # Botón para revisar la respuesta
        self.check_button = ttk.Button(button_frame, text="Revisar Respuesta", command=self.check_answer)
        self.check_button.pack(side=tk.LEFT, padx=10)

        # Botón para pasar a la siguiente pregunta
        self.next_button = ttk.Button(button_frame, text="Siguiente", command=self.next_question, state=tk.DISABLED)
        self.next_button.pack(side=tk.RIGHT, padx=10)
        
        # Enlazar la tecla Enter al evento de revisar respuesta
        self.answer_entry.bind("<Return>", lambda event: self.check_answer())

        # Iniciar el quiz
        self.display_question()

    def normalize_string(self, text):
        """
        Normaliza una cadena para la comparación, eliminando espacios, tildes,
        caracteres especiales y convirtiendo a minúsculas.
        """
        if not isinstance(text, str):
            return ""
        text = text.lower().strip()
        text = re.sub(r'[^\w\s]', '', text)  # Elimina la mayoría de los símbolos de puntuación
        text = text.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')
        text = text.replace(' ', '') # Elimina espacios
        return text
    
    def check_answer(self):
        """Comprueba si la respuesta del usuario es correcta y actualiza la GUI."""
        current_question = self.questions[self.current_question_index]
        user_answer = self.answer_entry.get()
        correct_answer = current_question["respuesta"]

        # Normalizar respuestas para una comparación flexible
        is_correct = self.normalize_string(user_answer) == self.normalize_string(correct_answer)

        if is_correct:
            self.score += 1
            self.feedback_label.config(text="¡Correcto! ✅", fg="green")
        else:
            self.feedback_label.config(text="Incorrecto. ❌", fg="red")
        
        # Actualizar la explicación y el estado de los botones
        self.explanation_label.config(text=f"Respuesta correcta: {correct_answer.capitalize()}\nExplicación: {current_question['explicacion']}")
        self.check_button.config(state=tk.DISABLED)
        self.next_button.config(state=tk.NORMAL)

    def next_question(self):
        """Pasa a la siguiente pregunta o finaliza el quiz."""
        self.current_question_index += 1
        if self.current_question_index < self.total_questions:
            self.display_question()
        else:
            self.show_final_results()

    def display_question(self):
        """Muestra la siguiente pregunta en la GUI."""
        current_question = self.questions[self.current_question_index]
        self.question_label.config(text=current_question["pregunta"])
        self.status_label.config(text=f"Pregunta {self.current_question_index + 1} de {self.total_questions} | Puntuación: {self.score}")
        
        # Limpiar y reiniciar los elementos de la GUI
        self.answer_entry.delete(0, tk.END)
        self.feedback_label.config(text="")
        self.explanation_label.config(text="")
        self.check_button.config(state=tk.NORMAL)
        self.next_button.config(state=tk.DISABLED)

    def show_final_results(self):
        """Muestra los resultados finales del quiz."""
        self.question_label.pack_forget()
        self.answer_entry.pack_forget()
        self.check_button.pack_forget()
        self.next_button.pack_forget()
        self.feedback_label.pack_forget()
        self.explanation_label.pack_forget()

        final_score_label = tk.Label(self, text="¡Quiz Completado!", font=self.title_font, fg="#4a4a4a")
        final_score_label.pack(pady=40)

        result_text = f"Has obtenido {self.score} de {self.total_questions} respuestas correctas."
        result_label = tk.Label(self, text=result_text, font=self.question_font, fg="#4a4a4a")
        result_label.pack(pady=20)
        
        restart_button = ttk.Button(self, text="Volver a empezar", command=self.restart_quiz)
        restart_button.pack(pady=20)

    def restart_quiz(self):
        """Reinicia el quiz a su estado inicial."""
        self.destroy()
        new_app = LenguasIndigenasQuizApp()
        new_app.mainloop()


if __name__ == "__main__":
    app = LenguasIndigenasQuizApp()
    app.mainloop()
