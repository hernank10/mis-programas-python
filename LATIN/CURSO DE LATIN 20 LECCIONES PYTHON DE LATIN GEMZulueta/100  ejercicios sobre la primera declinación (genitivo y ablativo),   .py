import random

def run_latin_quiz():
    """
    Ejecuta un taller interactivo de Latín en la consola.
    Incluye ejercicios sobre la primera declinación (genitivo y ablativo),
    funciones sintácticas (genitivo y ablativo), complemento circunstancial de lugar,
    significado del verbo sum, segunda conjugación activa (presente e imperfecto de indicativo),
    y evolución del latín al castellano.
    Pide al usuario que escriba una palabra latina y su traducción después de cada ejercicio.
    """
    exercises = [
        # --- Primera Declinación (Genitivo y Ablativo) (20 ejercicios) ---
        {"type": "declension", "topic": "Primera Declinación (Genitivo/Ablativo)", "question": "Proporciona el genitivo singular de 'puella, -ae f.'", "answer": "puellae", "feedback": "El genitivo singular de 'puella' es 'puellae'."},
        {"type": "declension", "topic": "Primera Declinación (Genitivo/Ablativo)", "question": "Proporciona el ablativo singular de 'rosa, -ae f.'", "answer": "rosa", "feedback": "El ablativo singular de 'rosa' es 'rosa'."},
        {"type": "declension", "topic": "Primera Declinación (Genitivo/Ablativo)", "question": "Proporciona el genitivo plural de 'via, -ae f.'", "answer": "viarum", "feedback": "El genitivo plural de 'via' es 'viarum'."},
        {"type": "declension", "topic": "Primera Declinación (Genitivo/Ablativo)", "question": "Proporciona el ablativo plural de 'terra, -ae f.'", "answer": "terris", "feedback": "El ablativo plural de 'terra' es 'terris'."},
        {"type": "declension", "topic": "Primera Declinación (Genitivo/Ablativo)", "question": "Cuál es el genitivo singular de 'filia, -ae f.'?", "answer": "filiae", "feedback": "El genitivo singular de 'filia' es 'filiae'."},
        {"type": "declension", "topic": "Primera Declinación (Genitivo/Ablativo)", "question": "Cuál es el ablativo singular de 'aqua, -ae f.'?", "answer": "aqua", "feedback": "El ablativo singular de 'aqua' es 'aqua'."},
        {"type": "declension", "topic": "Primera Declinación (Genitivo/Ablativo)", "question": "Cuál es el genitivo plural de 'lupa, -ae f.'?", "answer": "luparum", "feedback": "El genitivo plural de 'lupa' es 'luparum'."},
        {"type": "declension", "topic": "Primera Declinación (Genitivo/Ablativo)", "question": "Cuál es el ablativo plural de 'mensa, -ae f.'?", "answer": "mensis", "feedback": "El ablativo plural de 'mensa' es 'mensis'."},
        {"type": "declension", "topic": "Primera Declinación (Genitivo/Ablativo)", "question": "Declina 'silva, -ae f.' en genitivo singular.", "answer": "silvae", "feedback": "Genitivo singular de 'silva' es 'silvae'."},
        {"type": "declension", "topic": "Primera Declinación (Genitivo/Ablativo)", "question": "Declina 'silva, -ae f.' en ablativo singular.", "answer": "silva", "feedback": "Ablativo singular de 'silva' es 'silva'."},
        {"type": "declension", "topic": "Primera Declinación (Genitivo/Ablativo)", "question": "Declina 'vita, -ae f.' en genitivo plural.", "answer": "vitarum", "feedback": "Genitivo plural de 'vita' es 'vitarum'."},
        {"type": "declension", "topic": "Primera Declinación (Genitivo/Ablativo)", "question": "Declina 'vita, -ae f.' en ablativo plural.", "answer": "vitis", "feedback": "Ablativo plural de 'vita' es 'vitis'."},
        {"type": "declension", "topic": "Primera Declinación (Genitivo/Ablativo)", "question": "Proporciona el genitivo singular de 'poeta, -ae m.'", "answer": "poetae", "feedback": "El genitivo singular de 'poeta' es 'poetae'."},
        {"type": "declension", "topic": "Primera Declinación (Genitivo/Ablativo)", "question": "Proporciona el ablativo plural de 'agricola, -ae m.'", "answer": "agricolis", "feedback": "El ablativo plural de 'agricola' es 'agricolis'."},
        {"type": "declension", "topic": "Primera Declinación (Genitivo/Ablativo)", "question": "Declina 'nauta, -ae m.' en genitivo plural.", "answer": "nautarum", "feedback": "Genitivo plural de 'nauta' es 'nautarum'."},
        {"type": "declension", "topic": "Primera Declinación (Genitivo/Ablativo)", "question": "Declina 'nauta, -ae m.' en ablativo singular.", "answer": "nauta", "feedback": "Ablativo singular de 'nauta' es 'nauta'."},
        {"type": "declension", "topic": "Primera Declinación (Genitivo/Ablativo)", "question": "Cuál es el genitivo singular de 'incola, -ae m.'?", "answer": "incolae", "feedback": "El genitivo singular de 'incola' es 'incolae'."},
        {"type": "declension", "topic": "Primera Declinación (Genitivo/Ablativo)", "question": "Cuál es el ablativo plural de 'ancilla, -ae f.'?", "answer": "ancillis", "feedback": "El ablativo plural de 'ancilla' es 'ancillis'."},
        {"type": "declension", "topic": "Primera Declinación (Genitivo/Ablativo)", "question": "Declina 'littera, -ae f.' en genitivo singular.", "answer": "litterae", "feedback": "Genitivo singular de 'littera' es 'litterae'."},
        {"type": "declension", "topic": "Primera Declinación (Genitivo/Ablativo)", "question": "Declina 'littera, -ae f.' en ablativo plural.", "answer": "litteris", "feedback": "Ablativo plural de 'littera' es 'litteris'."},

        # --- Función Sintáctica (Genitivo y Ablativo) (20 ejercicios) ---
        {"type": "syntax", "topic": "Función Sintáctica (Genitivo/Ablativo)", "question": "Identifica la función sintáctica de 'puellae' en 'Liber puellae est.'", "answer": "complemento del nombre", "feedback": "Indica posesión, es un complemento del nombre en genitivo."},
        {"type": "syntax", "topic": "Función Sintáctica (Genitivo/Ablativo)", "question": "Identifica la función sintáctica de 'silva' en 'In silva ambulat.'", "answer": "complemento circunstancial de lugar (dónde)", "feedback": "Indica el lugar donde se realiza la acción, con preposición 'in' y ablativo."},
        {"type": "syntax", "topic": "Función Sintáctica (Genitivo/Ablativo)", "question": "Traduce 'el libro de la niña' ('liber, -bri m.', 'puella, -ae f.').", "answer": "liber puellae", "feedback": "'De la niña' es genitivo."},
        {"type": "syntax", "topic": "Función Sintáctica (Genitivo/Ablativo)", "question": "Traduce 'en la ciudad' ('urbs, urbis f.').", "answer": "in urbe", "feedback": "Lugar 'dónde' con 'in' + ablativo."},
        {"type": "syntax", "topic": "Función Sintáctica (Genitivo/Ablativo)", "question": "Cuál es la función de 'rosarum' en 'Pulchritudo rosarum magna est.'?", "answer": "complemento del nombre", "feedback": "Indica de qué son las rosas, es genitivo plural."},
        {"type": "syntax", "topic": "Función Sintáctica (Genitivo/Ablativo)", "question": "Cuál es la función de 'aqua' en 'Aqua vivit.'", "answer": "complemento circunstancial de medio", "feedback": "Indica el medio por el cual vive, es ablativo sin preposición."},
        {"type": "syntax", "topic": "Función Sintáctica (Genitivo/Ablativo)", "question": "Traduce 'la voz de las mujeres' ('vox, vocis f.', 'femina, -ae f.').", "answer": "vox feminarum", "feedback": "'De las mujeres' es genitivo plural."},
        {"type": "syntax", "topic": "Función Sintáctica (Genitivo/Ablativo)", "question": "Traduce 'con gran cuidado' ('cura, -ae f.', 'magnus, -a, -um').", "answer": "magna cura", "feedback": "Ablativo de modo sin preposición."},
        {"type": "syntax", "topic": "Función Sintáctica (Genitivo/Ablativo)", "question": "Identifica la función sintáctica de 'poetae' en 'Carmina poetae legimus.'", "answer": "complemento del nombre", "feedback": "Indica de quién son los poemas, genitivo singular."},
        {"type": "syntax", "topic": "Función Sintáctica (Genitivo/Ablativo)", "question": "Identifica la función sintáctica de 'gladio' en 'Pugnat gladio.'", "answer": "complemento circunstancial de instrumento", "feedback": "Indica el instrumento, ablativo sin preposición."},
        {"type": "syntax", "topic": "Función Sintáctica (Genitivo/Ablativo)", "question": "Traduce 'el consejo del anciano' ('consilium, -i n.', 'senex, senis m.').", "answer": "consilium senis", "feedback": "'Del anciano' es genitivo singular."},
        {"type": "syntax", "topic": "Función Sintáctica (Genitivo/Ablativo)", "question": "Traduce 'por miedo' ('timor, timoris m.').", "answer": "timore", "feedback": "Ablativo de causa sin preposición."},
        {"type": "syntax", "topic": "Función Sintáctica (Genitivo/Ablativo)", "question": "Cuál es la función de 'urbis' en 'Moenia urbis alta sunt.'?", "answer": "complemento del nombre", "feedback": "Indica de qué son las murallas, genitivo singular."},
        {"type": "syntax", "topic": "Función Sintáctica (Genitivo/Ablativo)", "question": "Cuál es la función de 'celeritate' en 'Venit celeritate.'?", "answer": "complemento circunstancial de modo", "feedback": "Indica el modo, ablativo sin preposición."},
        {"type": "syntax", "topic": "Función Sintáctica (Genitivo/Ablativo)", "question": "Traduce 'la casa del padre' ('domus, -us f.', 'pater, patris m.').", "answer": "domus patris", "feedback": "'Del padre' es genitivo singular."},
        {"type": "syntax", "topic": "Función Sintáctica (Genitivo/Ablativo)", "question": "Traduce 'en la guerra' ('bellum, -i n.').", "answer": "in bello", "feedback": "Lugar 'dónde' con 'in' + ablativo."},
        {"type": "syntax", "topic": "Función Sintáctica (Genitivo/Ablativo)", "question": "Identifica la función sintáctica de 'regis' en 'Potestas regis magna est.'", "answer": "complemento del nombre", "feedback": "Indica de quién es el poder, genitivo singular."},
        {"type": "syntax", "topic": "Función Sintáctica (Genitivo/Ablativo)", "question": "Identifica la función sintáctica de 'manu' en 'Scribit manu.'", "answer": "complemento circunstancial de instrumento", "feedback": "Indica el instrumento, ablativo sin preposición."},
        {"type": "syntax", "topic": "Función Sintáctica (Genitivo/Ablativo)", "question": "Traduce 'el amor a la patria' ('amor, amoris m.', 'patria, -ae f.').", "answer": "amor patriae", "feedback": "'A la patria' es genitivo objetivo."},
        {"type": "syntax", "topic": "Función Sintáctica (Genitivo/Ablativo)", "question": "Traduce 'con gran valentía' ('virtus, virtutis f.', 'magnus, -a, -um').", "answer": "magna virtute", "feedback": "Ablativo de modo sin preposición."},

        # --- Complemento Circunstancial de Lugar (15 ejercicios) ---
        {"type": "locative", "topic": "Complemento Circunstancial de Lugar", "question": "Cómo se dice 'en Roma' (lugar dónde)?", "answer": "roma", "feedback": "Para ciudades pequeñas y singulares de la 1ª y 2ª declinación, se usa el locativo, que coincide con el genitivo singular."},
        {"type": "locative", "topic": "Complemento Circunstancial de Lugar", "question": "Cómo se dice 'a Roma' (lugar adonde)?", "answer": "romam", "feedback": "Acusativo sin preposición para ciudades."},
        {"type": "locative", "topic": "Complemento Circunstancial de Lugar", "question": "Cómo se dice 'desde Roma' (lugar de donde)?", "answer": "roma", "feedback": "Ablativo sin preposición para ciudades."},
        {"type": "locative", "topic": "Complemento Circunstancial de Lugar", "question": "Cómo se dice 'por el camino' (lugar por donde)?", "answer": "via", "feedback": "Ablativo sin preposición para 'lugar por donde'."},
        {"type": "locative", "topic": "Complemento Circunstancial de Lugar", "question": "Traduce 'en el campo' ('ager, agri m.').", "answer": "in agro", "feedback": "Lugar 'dónde' con 'in' + ablativo."},
        {"type": "locative", "topic": "Complemento Circunstancial de Lugar", "question": "Traduce 'hacia la ciudad' ('urbs, urbis f.').", "answer": "ad urbem", "feedback": "Lugar 'adonde' con 'ad' + acusativo."},
        {"type": "locative", "topic": "Complemento Circunstancial de Lugar", "question": "Traduce 'desde el bosque' ('silva, -ae f.').", "answer": "ex silva", "feedback": "Lugar 'de donde' con 'ex' + ablativo."},
        {"type": "locative", "topic": "Complemento Circunstancial de Lugar", "question": "Traduce 'a través de los campos' ('campus, -i m.').", "answer": "per campos", "feedback": "Lugar 'por donde' con 'per' + acusativo."},
        {"type": "locative", "topic": "Complemento Circunstancial de Lugar", "question": "Cómo se dice 'en casa' (lugar dónde)?", "answer": "domi", "feedback": "Locativo de 'domus'."},
        {"type": "locative", "topic": "Complemento Circunstancial de Lugar", "question": "Cómo se dice 'a casa' (lugar adonde)?", "answer": "domum", "feedback": "Acusativo sin preposición para 'domus'."},
        {"type": "locative", "topic": "Complemento Circunstancial de Lugar", "question": "Cómo se dice 'desde casa' (lugar de donde)?", "answer": "domo", "feedback": "Ablativo sin preposición para 'domus'."},
        {"type": "locative", "topic": "Complemento Circunstancial de Lugar", "question": "Traduce 'en Atenas' (lugar dónde).", "answer": "athenis", "feedback": "Locativo para nombres de ciudades plurales de la 1ª declinación."},
        {"type": "locative", "topic": "Complemento Circunstancial de Lugar", "question": "Traduce 'a Atenas' (lugar adonde).", "answer": "athenas", "feedback": "Acusativo sin preposición para ciudades."},
        {"type": "locative", "topic": "Complemento Circunstancial de Lugar", "question": "Traduce 'desde Atenas' (lugar de donde).", "answer": "athenis", "feedback": "Ablativo sin preposición para ciudades."},
        {"type": "locative", "topic": "Complemento Circunstancial de Lugar", "question": "Cómo se dice 'en el jardín' ('hortus, -i m.').", "answer": "in horto", "feedback": "Lugar 'dónde' con 'in' + ablativo."},

        # --- Significado del Verbo Sum (15 ejercicios) ---
        {"type": "sum_verb", "topic": "Verbo Sum", "question": "Traduce 'soy'.", "answer": "sum", "feedback": "1ª persona singular del presente de indicativo de 'sum'."},
        {"type": "sum_verb", "topic": "Verbo Sum", "question": "Traduce 'eres'.", "answer": "es", "feedback": "2ª persona singular del presente de indicativo de 'sum'."},
        {"type": "sum_verb", "topic": "Verbo Sum", "question": "Traduce 'es'.", "answer": "est", "feedback": "3ª persona singular del presente de indicativo de 'sum'."},
        {"type": "sum_verb", "topic": "Verbo Sum", "question": "Traduce 'somos'.", "answer": "sumus", "feedback": "1ª persona plural del presente de indicativo de 'sum'."},
        {"type": "sum_verb", "topic": "Verbo Sum", "question": "Traduce 'sois'.", "answer": "estis", "feedback": "2ª persona plural del presente de indicativo de 'sum'."},
        {"type": "sum_verb", "topic": "Verbo Sum", "question": "Traduce 'son'.", "answer": "sunt", "feedback": "3ª persona plural del presente de indicativo de 'sum'."},
        {"type": "sum_verb", "topic": "Verbo Sum", "question": "Traduce 'era'.", "answer": "eram", "feedback": "1ª persona singular del imperfecto de indicativo de 'sum'."},
        {"type": "sum_verb", "topic": "Verbo Sum", "question": "Traduce 'eras'.", "answer": "eras", "feedback": "2ª persona singular del imperfecto de indicativo de 'sum'."},
        {"type": "sum_verb", "topic": "Verbo Sum", "question": "Traduce 'era' (él/ella).", "answer": "erat", "feedback": "3ª persona singular del imperfecto de indicativo de 'sum'."},
        {"type": "sum_verb", "topic": "Verbo Sum", "question": "Traduce 'éramos'.", "answer": "eramus", "feedback": "1ª persona plural del imperfecto de indicativo de 'sum'."},
        {"type": "sum_verb", "topic": "Verbo Sum", "question": "Traduce 'erais'.", "answer": "eratis", "feedback": "2ª persona plural del imperfecto de indicativo de 'sum'."},
        {"type": "sum_verb", "topic": "Verbo Sum", "question": "Traduce 'eran'.", "answer": "erant", "feedback": "3ª persona plural del imperfecto de indicativo de 'sum'."},
        {"type": "sum_verb", "topic": "Verbo Sum", "question": "Qué significa 'sum'?", "answer": "ser o estar", "feedback": "El verbo 'sum' significa 'ser' o 'estar'."},
        {"type": "sum_verb", "topic": "Verbo Sum", "question": "Qué significa 'est'?", "answer": "es o está", "feedback": "Significa 'es' o 'está'."},
        {"type": "sum_verb", "topic": "Verbo Sum", "question": "Qué significa 'erant'?", "answer": "eran o estaban", "feedback": "Significa 'eran' o 'estaban'."},

        # --- Segunda Conjugación Activa (Presente e Imperfecto de Indicativo) (15 ejercicios) ---
        {"type": "conjugation2", "topic": "Segunda Conjugación (Presente)", "question": "Conjuga 'moneo, monere' en presente de indicativo, 1ª persona singular.", "answer": "moneo", "feedback": "Yo advierto."},
        {"type": "conjugation2", "topic": "Segunda Conjugación (Presente)", "question": "Conjuga 'doceo, docere' en presente de indicativo, 2ª persona singular.", "answer": "doces", "feedback": "Tú enseñas."},
        {"type": "conjugation2", "topic": "Segunda Conjugación (Presente)", "question": "Conjuga 'habeo, habere' en presente de indicativo, 3ª persona singular.", "answer": "habet", "feedback": "Él/ella tiene."},
        {"type": "conjugation2", "topic": "Segunda Conjugación (Presente)", "question": "Conjuga 'video, videre' en presente de indicativo, 1ª persona plural.", "answer": "videmus", "feedback": "Nosotros vemos."},
        {"type": "conjugation2", "topic": "Segunda Conjugación (Presente)", "question": "Conjuga 'teneo, tenere' en presente de indicativo, 2ª persona plural.", "answer": "tenetis", "feedback": "Vosotros tenéis."},
        {"type": "conjugation2", "topic": "Segunda Conjugación (Presente)", "question": "Conjuga 'moveo, movere' en presente de indicativo, 3ª persona plural.", "answer": "movent", "feedback": "Ellos/ellas mueven."},
        {"type": "conjugation2", "topic": "Segunda Conjugación (Imperfecto)", "question": "Conjuga 'moneo, monere' en imperfecto de indicativo, 1ª persona singular.", "answer": "monebam", "feedback": "Yo advertía."},
        {"type": "conjugation2", "topic": "Segunda Conjugación (Imperfecto)", "question": "Conjuga 'doceo, docere' en imperfecto de indicativo, 2ª persona singular.", "answer": "docebas", "feedback": "Tú enseñabas."},
        {"type": "conjugation2", "topic": "Segunda Conjugación (Imperfecto)", "question": "Conjuga 'habeo, habere' en imperfecto de indicativo, 3ª persona singular.", "answer": "habebat", "feedback": "Él/ella tenía."},
        {"type": "conjugation2", "topic": "Segunda Conjugación (Imperfecto)", "question": "Conjuga 'video, videre' en imperfecto de indicativo, 1ª persona plural.", "answer": "videbamus", "feedback": "Nosotros veíamos."},
        {"type": "conjugation2", "topic": "Segunda Conjugación (Imperfecto)", "question": "Conjuga 'teneo, tenere' en imperfecto de indicativo, 2ª persona plural.", "answer": "tenebatis", "feedback": "Vosotros teníais."},
        {"type": "conjugation2", "topic": "Segunda Conjugación (Imperfecto)", "question": "Conjuga 'moveo, movere' en imperfecto de indicativo, 3ª persona plural.", "answer": "movebant", "feedback": "Ellos/ellas movían."},
        {"type": "conjugation2", "topic": "Segunda Conjugación (Presente)", "question": "Traduce 'tienes' al latín (verbo 'habeo, habere').", "answer": "habes", "feedback": "2ª persona singular del presente."},
        {"type": "conjugation2", "topic": "Segunda Conjugación (Imperfecto)", "question": "Traduce 'ellos veían' al latín (verbo 'video, videre').", "answer": "videbant", "feedback": "3ª persona plural del imperfecto."},
        {"type": "conjugation2", "topic": "Primera Conjugación (Presente)", "question": "Cuál es la terminación del presente de indicativo, 1ª persona plural, en la segunda conjugación?", "answer": "-emus", "feedback": "Ej. 'videmus'."},

        # --- Evolución del Latín al Castellano (15 ejercicios) ---
        {"type": "evolution", "topic": "Evolución Latín-Castellano", "question": "Cuál es la evolución en castellano de 'clavem'?", "answer": "llave", "feedback": "El grupo 'cl' inicial se palataliza a 'll'."},
        {"type": "evolution", "topic": "Evolución Latín-Castellano", "question": "Cuál es la evolución en castellano de 'plenum'?", "answer": "lleno", "feedback": "El grupo 'pl' inicial se palataliza a 'll'."},
        {"type": "evolution", "topic": "Evolución Latín-Castellano", "question": "Cuál es la evolución en castellano de 'flammam'?", "answer": "llama", "feedback": "El grupo 'fl' inicial se palataliza a 'll'."},
        {"type": "evolution", "topic": "Evolución Latín-Castellano", "question": "Cuál es la evolución en castellano de 'oculum'?", "answer": "ojo", "feedback": "El grupo 'cl' intervocálico se palataliza a 'j'."},
        {"type": "evolution", "topic": "Evolución Latín-Castellano", "question": "Cuál es la evolución en castellano de 'noctem'?", "answer": "noche", "feedback": "El grupo 'ct' se palataliza a 'ch'."},
        {"type": "evolution", "topic": "Evolución Latín-Castellano", "question": "Cuál es la evolución en castellano de 'factum'?", "answer": "hecho", "feedback": "La 'f' inicial se aspira a 'h', y el grupo 'ct' se palataliza a 'ch'."},
        {"type": "evolution", "topic": "Evolución Latín-Castellano", "question": "Cuál es la evolución en castellano de 'lupum'?", "answer": "lobo", "feedback": "La 'u' breve tónica diptonga a 'o', y la 'p' intervocálica se sonoriza a 'b'."},
        {"type": "evolution", "topic": "Evolución Latín-Castellano", "question": "Cuál es la evolución en castellano de 'vitam'?", "answer": "vida", "feedback": "La 't' intervocálica se sonoriza a 'd'."},
        {"type": "evolution", "topic": "Evolución Latín-Castellano", "question": "Cuál es la evolución en castellano de 'rotam'?", "answer": "rueda", "feedback": "La 'o' breve tónica diptonga a 'ue', y la 't' intervocálica se sonoriza a 'd'."},
        {"type": "evolution", "topic": "Evolución Latín-Castellano", "question": "Cuál es la evolución en castellano de 'ferrum'?", "answer": "hierro", "feedback": "La 'e' breve tónica diptonga a 'ie', y la 'rr' se mantiene."},
        {"type": "evolution", "topic": "Evolución Latín-Castellano", "question": "Cuál es la evolución en castellano de 'aurum'?", "answer": "oro", "feedback": "El diptongo 'au' monoptonga a 'o'."},
        {"type": "evolution", "topic": "Evolución Latín-Castellano", "question": "Cuál es la evolución en castellano de 'causam'?", "answer": "cosa", "feedback": "El diptongo 'au' monoptonga a 'o', y la 's' intervocálica se mantiene."},
        {"type": "evolution", "topic": "Evolución Latín-Castellano", "question": "Cuál es la evolución en castellano de 'lignum'?", "answer": "leño", "feedback": "El grupo 'gn' se palataliza a 'ñ'."},
        {"type": "evolution", "topic": "Evolución Latín-Castellano", "question": "Cuál es la evolución en castellano de 'somnum'?", "answer": "sueño", "feedback": "La 'o' breve tónica diptonga a 'ue', y el grupo 'mn' se palataliza a 'ñ'."},
        {"type": "evolution", "topic": "Evolución Latín-Castellano", "question": "Cuál es la evolución en castellano de 'filium'?", "answer": "hijo", "feedback": "La 'f' inicial se aspira a 'h', y el grupo 'li' se palataliza a 'j'."},

        # --- Ejercicios Adicionales para completar los 100 ---
        # Primera Declinación (Genitivo y Ablativo) - 5 adicionales
        {"type": "declension", "topic": "Primera Declinación (Genitivo/Ablativo)", "question": "Proporciona el genitivo singular de 'magistra, -ae f.'", "answer": "magistrae", "feedback": "El genitivo singular de 'magistra' es 'magistrae'."},
        {"type": "declension", "topic": "Primera Declinación (Genitivo/Ablativo)", "question": "Proporciona el ablativo singular de 'familia, -ae f.'", "answer": "familia", "feedback": "El ablativo singular de 'familia' es 'familia'."},
        {"type": "declension", "topic": "Primera Declinación (Genitivo/Ablativo)", "question": "Proporciona el genitivo plural de 'stella, -ae f.'", "answer": "stellarum", "feedback": "El genitivo plural de 'stella' es 'stellarum'."},
        {"type": "declension", "topic": "Primera Declinación (Genitivo/Ablativo)", "question": "Proporciona el ablativo plural de 'cena, -ae f.'", "answer": "cenis", "feedback": "El ablativo plural de 'cena' es 'cenis'."},
        {"type": "declension", "topic": "Primera Declinación (Genitivo/Ablativo)", "question": "Cuál es el genitivo singular de 'cura, -ae f.'?", "answer": "curae", "feedback": "El genitivo singular de 'cura' es 'curae'."},

        # Función Sintáctica (Genitivo y Ablativo) - 5 adicionales
        {"type": "syntax", "topic": "Función Sintáctica (Genitivo/Ablativo)", "question": "Identifica la función sintáctica de 'militum' en 'Fortitudo militum magna est.'", "answer": "complemento del nombre", "feedback": "Indica de quién es la fortaleza, genitivo plural."},
        {"type": "syntax", "topic": "Función Sintáctica (Genitivo/Ablativo)", "question": "Identifica la función sintáctica de 'tempore' en 'Bello tempore pugnant.'", "answer": "complemento circunstancial de tiempo", "feedback": "Indica el tiempo, ablativo sin preposición."},
        {"type": "syntax", "topic": "Función Sintáctica (Genitivo/Ablativo)", "question": "Traduce 'el miedo a la muerte' ('timor, timoris m.', 'mors, mortis f.').", "answer": "timor mortis", "feedback": "'A la muerte' es genitivo objetivo."},
        {"type": "syntax", "topic": "Función Sintáctica (Genitivo/Ablativo)", "question": "Traduce 'con gran alegría' ('gaudium, -i n.', 'magnus, -a, -um').", "answer": "magno gaudio", "feedback": "Ablativo de modo sin preposición."},
        {"type": "syntax", "topic": "Función Sintáctica (Genitivo/Ablativo)", "question": "Cuál es la función de 'urbium' en 'Ruinae urbium antiquarum.'?", "answer": "complemento del nombre", "feedback": "Indica de qué son las ruinas, genitivo plural."},

        # Complemento Circunstancial de Lugar - 5 adicionales
        {"type": "locative", "topic": "Complemento Circunstancial de Lugar", "question": "Cómo se dice 'en el foro' (lugar dónde)?", "answer": "in foro", "feedback": "Lugar 'dónde' con 'in' + ablativo."},
        {"type": "locative", "topic": "Complemento Circunstancial de Lugar", "question": "Cómo se dice 'a la escuela' (lugar adonde)?", "answer": "ad scholam", "feedback": "Lugar 'adonde' con 'ad' + acusativo."},
        {"type": "locative", "topic": "Complemento Circunstancial de Lugar", "question": "Cómo se dice 'desde la cumbre' ('summus, -a, -um' + 'mons, montis m.').", "answer": "e summo monte", "feedback": "Lugar 'de donde' con 'e/ex' + ablativo."},
        {"type": "locative", "topic": "Complemento Circunstancial de Lugar", "question": "Cómo se dice 'por el río' ('flumen, fluminis n.').", "answer": "per flumen", "feedback": "Lugar 'por donde' con 'per' + acusativo."},
        {"type": "locative", "topic": "Complemento Circunstancial de Lugar", "question": "Traduce 'en el cielo' ('caelum, -i n.').", "answer": "in caelo", "feedback": "Lugar 'dónde' con 'in' + ablativo."},

        # Verbo Sum - 5 adicionales
        {"type": "sum_verb", "topic": "Verbo Sum", "question": "Traduce 'seré'.", "answer": "ero", "feedback": "1ª persona singular del futuro de indicativo de 'sum'."},
        {"type": "sum_verb", "topic": "Verbo Sum", "question": "Traduce 'habrás sido'.", "answer": "fueris", "feedback": "2ª persona singular del futuro perfecto de indicativo de 'sum'."},
        {"type": "sum_verb", "topic": "Verbo Sum", "question": "Qué significa 'fui'?", "answer": "fui o estuve", "feedback": "Perfecto de indicativo de 'sum', 1ª persona singular."},
        {"type": "sum_verb", "topic": "Verbo Sum", "question": "Qué significa 'esse'?", "answer": "ser o estar", "feedback": "Infinitivo de 'sum'."},
        {"type": "sum_verb", "topic": "Verbo Sum", "question": "Traduce 'serán'.", "answer": "erunt", "feedback": "3ª persona plural del futuro de indicativo de 'sum'."},

        # Segunda Conjugación Activa (Presente e Imperfecto) - 5 adicionales
        {"type": "conjugation2", "topic": "Segunda Conjugación (Presente)", "question": "Conjuga 'iubeo, iubere' en presente de indicativo, 3ª persona plural.", "answer": "iubent", "feedback": "Ellos/ellas ordenan."},
        {"type": "conjugation2", "topic": "Segunda Conjugación (Imperfecto)", "question": "Conjuga 'respondeo, respondere' en imperfecto de indicativo, 1ª persona singular.", "answer": "respondebam", "feedback": "Yo respondía."},
        {"type": "conjugation2", "topic": "Segunda Conjugación (Presente)", "question": "Traduce 'él tiene' al latín (verbo 'habeo, habere').", "answer": "habet", "feedback": "3ª persona singular del presente."},
        {"type": "conjugation2", "topic": "Segunda Conjugación (Imperfecto)", "question": "Traduce 'vosotros enseñabais' al latín (verbo 'doceo, docere').", "answer": "docebatis", "feedback": "2ª persona plural del imperfecto."},
        {"type": "conjugation2", "topic": "Primera Conjugación (Presente)", "question": "Cuál es la terminación del presente de indicativo, 3ª persona singular, en la segunda conjugación?", "answer": "-et", "feedback": "Ej. 'habet'."},

        # Evolución del Latín al Castellano - 5 adicionales
        {"type": "evolution", "topic": "Evolución Latín-Castellano", "question": "Cuál es la evolución en castellano de 'caput'?", "answer": "cabo", "feedback": "La 'u' breve tónica diptonga a 'o', y la 'p' intervocálica se sonoriza a 'b'."},
        {"type": "evolution", "topic": "Evolución Latín-Castellano", "question": "Cuál es la evolución en castellano de 'regem'?", "answer": "rey", "feedback": "La 'g' intervocálica se pierde, y la 'e' se mantiene."},
        {"type": "evolution", "topic": "Evolución Latín-Castellano", "question": "Cuál es la evolución en castellano de 'fratrem'?", "answer": "hermano", "feedback": "La 'f' inicial se aspira a 'h', y el grupo 'tr' se mantiene."},
        {"type": "evolution", "topic": "Evolución Latín-Castellano", "question": "Cuál es la evolución en castellano de 'integrum'?", "answer": "entero", "feedback": "La 'i' inicial se convierte en 'e', y la 'g' intervocálica se pierde."},
        {"type": "evolution", "topic": "Evolución Latín-Castellano", "question": "Cuál es la evolución en castellano de 'directum'?", "answer": "derecho", "feedback": "La 'i' inicial se convierte en 'e', y el grupo 'ct' se palataliza a 'ch'."}
    ]

    # Mezcla los ejercicios para que aparezcan en un orden diferente cada vez
    random.shuffle(exercises)

    score = 0
    total_questions = 0

    print("--- ¡Bienvenido al Taller Avanzado de Latín! ---")
    print("Este programa te ayudará a practicar la primera declinación (genitivo y ablativo),")
    print("funciones sintácticas (genitivo y ablativo), complemento circunstancial de lugar,")
    print("el verbo 'sum', segunda conjugación activa (presente e imperfecto),")
    print("y evolución del latín al castellano.")
    print("¡Responde a las preguntas y mejora tus conocimientos!")
    print("---------------------------------------------------\n")

    # Limita a 100 ejercicios si hay más disponibles
    for i, exercise in enumerate(exercises[:100]):
        total_questions += 1
        print(f"--- Ejercicio {i + 1}/{min(len(exercises), 100)} ---")
        print(f"Tema: {exercise['topic']}")
        print(f"Pregunta: {exercise['question']}")
        user_answer = input("Tu respuesta: ").strip().lower() # Normaliza la entrada del usuario

        if user_answer == exercise['answer'].lower():
            print("¡Correcto! ✅")
            score += 1
        else:
            print(f"Incorrecto. ❌ La respuesta correcta era: {exercise['answer']}")
            print(f"Ayuda: {exercise['feedback']}")

        # Solicitar palabra latina y traducción
        print("\n--- ¡Momento de vocabulario! ---")
        latin_word = input("Escribe una palabra en latín (o 'omitir' para saltar): ").strip()
        if latin_word.lower() != 'omitir':
            spanish_translation = input(f"Ahora, escribe la traducción al castellano de '{latin_word}': ").strip()
            print(f"¡Gracias por compartir! Has escrito '{latin_word}' que significa '{spanish_translation}'.")
        else:
            print("Has decidido omitir este paso. ¡No hay problema!")

        print("-" * 30 + "\n")

    print("--- Taller Finalizado ---")
    print(f"Has completado {total_questions} ejercicios.")
    print(f"Tu puntuación final es: {score} de {total_questions} ({score/total_questions:.2%})")
    print("¡Sigue practicando para dominar el Latín!")
    print("------------------------------------------\n")

# Llama a la función para iniciar el taller
run_latin_quiz()
