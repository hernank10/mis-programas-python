import random

def cargar_ejercicios_derivacion_morfologica():
    """
    Carga los 100 ejercicios predefinidos de derivación morfológica en castellano
    directamente en el código.
    """
    print("Cargando 100 ejercicios de Derivación Morfológica y su Estructura Gramatical directamente...")
    return {
        "Morfología": {
            "Avanzado": {
                "Derivación Morfológica y Estructura": [
                    {"pregunta": "Analiza la derivación de 'panadero'.", "respuesta": "derivación, sufijación", "explicacion": "'Panadero' se forma añadiendo el sufijo '-adero' (profesión) a 'pan' (raíz)."},
                    {"pregunta": "Analiza la derivación de 'releer'.", "respuesta": "derivación, prefijación", "explicacion": "'Releer' se forma añadiendo el prefijo 're-' (repetición) a 'leer' (raíz)."},
                    {"pregunta": "Analiza la derivación de 'deshacer'.", "respuesta": "derivación, prefijación", "explicacion": "'Deshacer' se forma añadiendo el prefijo 'des-' (negación/inversión) a 'hacer' (raíz)."},
                    {"pregunta": "Analiza la derivación de 'arboleda'.", "respuesta": "derivación, sufijación", "explicacion": "'Arboleda' se forma añadiendo el sufijo '-eda' (lugar poblado) a 'árbol' (raíz)."},
                    {"pregunta": "Analiza la derivación de 'ilegal'.", "respuesta": "derivación, prefijación", "explicacion": "'Ilegal' se forma añadiendo el prefijo 'i-' (negación) a 'legal' (raíz)."},
                    {"pregunta": "Analiza la derivación de 'belleza'.", "respuesta": "derivación, sufijación", "explicacion": "'Belleza' se forma añadiendo el sufijo '-eza' (cualidad) a 'bello' (raíz)."},
                    {"pregunta": "Analiza la derivación de 'cantante'.", "respuesta": "derivación, sufijación", "explicacion": "'Cantante' se forma añadiendo el sufijo '-ante' (agente) a 'cantar' (raíz verbal)."},
                    {"pregunta": "Analiza la derivación de 'submarino'.", "respuesta": "derivación, prefijación", "explicacion": "'Submarino' se forma añadiendo el prefijo 'sub-' (debajo) a 'marino' (raíz)."},
                    {"pregunta": "Analiza la derivación de 'prever'.", "respuesta": "derivación, prefijación", "explicacion": "'Prever' se forma añadiendo el prefijo 'pre-' (anterioridad) a 'ver' (raíz)."},
                    {"pregunta": "Analiza la derivación de 'rojizo'.", "respuesta": "derivación, sufijación", "explicacion": "'Rojizo' se forma añadiendo el sufijo '-izo' (tendencia/semejanza) a 'rojo' (raíz)."},
                    {"pregunta": "Analiza la derivación de 'librería'.", "respuesta": "derivación, sufijación", "explicacion": "'Librería' se forma añadiendo el sufijo '-ería' (lugar) a 'libro' (raíz)."},
                    {"pregunta": "Analiza la derivación de 'incapaz'.", "respuesta": "derivación, prefijación", "explicacion": "'Incapaz' se forma añadiendo el prefijo 'in-' (negación) a 'capaz' (raíz)."},
                    {"pregunta": "Analiza la derivación de 'bondad'.", "respuesta": "derivación, sufijación", "explicacion": "'Bondad' se forma añadiendo el sufijo '-dad' (cualidad) a 'bueno' (raíz adaptada)."},
                    {"pregunta": "Analiza la derivación de 'jardinero'.", "respuesta": "derivación, sufijación", "explicacion": "'Jardinero' se forma añadiendo el sufijo '-ero' (profesión) a 'jardín' (raíz)."},
                    {"pregunta": "Analiza la derivación de 'anticuerpo'.", "respuesta": "derivación, prefijación", "explicacion": "'Anticuerpo' se forma añadiendo el prefijo 'anti-' (contra) a 'cuerpo' (raíz)."},
                    {"pregunta": "Analiza la derivación de 'blanquear'.", "respuesta": "derivación, sufijación", "explicacion": "'Blanquear' se forma añadiendo el sufijo '-ear' (acción) a 'blanco' (raíz)."},
                    {"pregunta": "Analiza la derivación de 'terremoto'.", "respuesta": "composición", "explicacion": "'Terremoto' se forma uniendo 'tierra' y 'moto' (del latín 'motus' = movimiento). Es una palabra compuesta."},
                    {"pregunta": "Analiza la derivación de 'microondas'.", "respuesta": "composición", "explicacion": "'Microondas' se forma uniendo 'micro' y 'ondas'. Es una palabra compuesta."},
                    {"pregunta": "Analiza la derivación de 'parasol'.", "respuesta": "composición", "explicacion": "'Parasol' se forma uniendo 'para' (del verbo parar) y 'sol'. Es una palabra compuesta."},
                    {"pregunta": "Analiza la derivación de 'paraguas'.", "respuesta": "composición", "explicacion": "'Paraguas' se forma uniendo 'para' (del verbo parar) y 'aguas'. Es una palabra compuesta."},
                    {"pregunta": "Analiza la derivación de 'sacapuntas'.", "respuesta": "composición", "explicacion": "'Sacapuntas' se forma uniendo 'saca' (del verbo sacar) y 'puntas'. Es una palabra compuesta."},
                    {"pregunta": "Analiza la derivación de 'abrelatas'.", "respuesta": "composición", "explicacion": "'Abrelatas' se forma uniendo 'abre' (del verbo abrir) y 'latas'. Es una palabra compuesta."},
                    {"pregunta": "Analiza la derivación de 'cortacésped'.", "respuesta": "composición", "explicacion": "'Cortacésped' se forma uniendo 'corta' (del verbo cortar) y 'césped'. Es una palabra compuesta."},
                    {"pregunta": "Analiza la derivación de 'maldecir'.", "respuesta": "derivación, prefijación", "explicacion": "'Maldecir' se forma añadiendo el prefijo 'mal-' (mal, negación) a 'decir' (raíz)."},
                    {"pregunta": "Analiza la derivación de 'bienestar'.", "respuesta": "composición", "explicacion": "'Bienestar' se forma uniendo 'bien' y 'estar'. Es una palabra compuesta."},
                    {"pregunta": "Analiza la derivación de 'guardarropa'.", "respuesta": "composición", "explicacion": "'Guardarropa' se forma uniendo 'guarda' (del verbo guardar) y 'ropa'. Es una palabra compuesta."},
                    {"pregunta": "Analiza la derivación de 'rompecabezas'.", "respuesta": "composición", "explicacion": "'Rompecabezas' se forma uniendo 'rompe' (del verbo romper) y 'cabezas'. Es una palabra compuesta."},
                    {"pregunta": "Analiza la derivación de 'pisapapeles'.", "respuesta": "composición", "explicacion": "'Pisapapeles' se forma uniendo 'pisa' (del verbo pisar) y 'papeles'. Es una palabra compuesta."},
                    {"pregunta": "Analiza la derivación de 'cubrecama'.", "respuesta": "composición", "explicacion": "'Cubrecama' se forma uniendo 'cubre' (del verbo cubrir) y 'cama'. Es una palabra compuesta."},
                    {"pregunta": "Analiza la derivación de 'lavavajillas'.", "respuesta": "composición", "explicacion": "'Lavavajillas' se forma uniendo 'lava' (del verbo lavar) y 'vajillas'. Es una palabra compuesta."},
                    {"pregunta": "Analiza la derivación de 'limpiabotas'.", "respuesta": "composición", "explicacion": "'Limpiabotas' se forma uniendo 'limpia' (del verbo limpiar) y 'botas'. Es una palabra compuesta."},
                    {"pregunta": "Analiza la derivación de 'correcaminos'.", "respuesta": "composición", "explicacion": "'Correcaminos' se forma uniendo 'corre' (del verbo correr) y 'caminos'. Es una palabra compuesta."},
                    {"pregunta": "Analiza la derivación de 'tragaperras'.", "respuesta": "composición", "explicacion": "'Tragaperras' se forma uniendo 'traga' (del verbo tragar) y 'perras'. Es una palabra compuesta."},
                    {"pregunta": "Analiza la derivación de 'hazmerreír'.", "respuesta": "composición", "explicacion": "'Hazmerreír' se forma uniendo 'haz' (del verbo hacer), 'me' y 'reír'. Es una palabra compuesta con pronombre enclítico."},
                    {"pregunta": "Analiza la derivación de 'pasodoble'.", "respuesta": "composición", "explicacion": "'Pasodoble' se forma uniendo 'paso' y 'doble'. Es una palabra compuesta."},
                    {"pregunta": "Analiza la derivación de 'milhojas'.", "respuesta": "composición", "explicacion": "'Milhojas' se forma uniendo 'mil' y 'hojas'. Es una palabra compuesta."},
                    {"pregunta": "Analiza la derivación de 'dieciséis'.", "respuesta": "composición", "explicacion": "'Dieciséis' se forma uniendo 'diez' y 'seis'. Es una palabra compuesta."},
                    {"pregunta": "Analiza la derivación de 'sietemesino'.", "respuesta": "composición", "explicacion": "'Sietemesino' se forma uniendo 'siete' y 'mesino'. Es una palabra compuesta."},
                    {"pregunta": "Analiza la derivación de 'medianoche'.", "respuesta": "composición", "explicacion": "'Medianoche' se forma uniendo 'media' y 'noche'. Es una palabra compuesta."},
                    {"pregunta": "Analiza la derivación de 'aguardiente'.", "respuesta": "composición", "explicacion": "'Aguardiente' se forma uniendo 'agua' y 'ardiente'. Es una palabra compuesta."},
                    {"pregunta": "Analiza la derivación de 'sabelotodo'.", "respuesta": "composición", "explicacion": "'Sabelotodo' se forma uniendo 'sabe' (del verbo saber), 'lo' y 'todo'. Es una palabra compuesta con pronombre."},
                    {"pregunta": "Analiza la derivación de 'malhumor'.", "respuesta": "composición", "explicacion": "'Malhumor' se forma uniendo 'mal' y 'humor'. Es una palabra compuesta."},
                    {"pregunta": "Analiza la derivación de 'altavoz'.", "respuesta": "composición", "explicacion": "'Altavoz' se forma uniendo 'alto' y 'voz'. Es una palabra compuesta."},
                    {"pregunta": "Analiza la derivación de 'agridulce'.", "respuesta": "composición", "explicacion": "'Agridulce' se forma uniendo 'agrio' y 'dulce'. Es una palabra compuesta."},
                    {"pregunta": "Analiza la derivación de 'pelirojo'.", "respuesta": "composición", "explicacion": "'Pelirojo' se forma uniendo 'pelo' (con apócope) y 'rojo'. Es una palabra compuesta."},
                    {"pregunta": "Analiza la derivación de 'manirroto'.", "respuesta": "composición", "explicacion": "'Manirroto' se forma uniendo 'mano' y 'roto'. Es una palabra compuesta."},
                    {"pregunta": "Analiza la derivación de 'sacacorchos'.", "respuesta": "composición", "explicacion": "'Sacacorchos' se forma uniendo 'saca' (del verbo sacar) y 'corchos'. Es una palabra compuesta."},
                    {"pregunta": "Analiza la derivación de 'lavacoches'.", "respuesta": "composición", "explicacion": "'Lavacoches' se forma uniendo 'lava' (del verbo lavar) y 'coches'. Es una palabra compuesta."},
                    {"pregunta": "Analiza la derivación de 'cazafantasmas'.", "respuesta": "composición", "explicacion": "'Cazafantasmas' se forma uniendo 'caza' (del verbo cazar) y 'fantasmas'. Es una palabra compuesta."},
                    {"pregunta": "Analiza la derivación de 'ciempiés'.", "respuesta": "composición", "explicacion": "'Ciempiés' se forma uniendo 'cien' y 'pies'. Es una palabra compuesta."},
                    {"pregunta": "Analiza la derivación de 'malpensado'.", "respuesta": "composición", "explicacion": "'Malpensado' se forma uniendo 'mal' y 'pensado'. Es una palabra compuesta."},
                    {"pregunta": "Analiza la derivación de 'altibajo'.", "respuesta": "composición", "explicacion": "'Altibajo' se forma uniendo 'alto' y 'bajo'. Es una palabra compuesta."},
                    {"pregunta": "Analiza la derivación de 'malvivir'.", "respuesta": "derivación, prefijación", "explicacion": "'Malvivir' se forma añadiendo el prefijo 'mal-' (mal) a 'vivir' (raíz)."},
                    {"pregunta": "Analiza la derivación de 'contradecir'.", "respuesta": "derivación, prefijación", "explicacion": "'Contradecir' se forma añadiendo el prefijo 'contra-' (oposición) a 'decir' (raíz)."},
                    {"pregunta": "Analiza la derivación de 'exalcalde'.", "respuesta": "derivación, prefijación", "explicacion": "'Exalcalde' se forma añadiendo el prefijo 'ex-' (antiguo) a 'alcalde' (raíz)."},
                    {"pregunta": "Analiza la derivación de 'remodelar'.", "respuesta": "derivación, prefijación", "explicacion": "'Remodelar' se forma añadiendo el prefijo 're-' (repetición/intensificación) a 'modelar' (raíz)."},
                    {"pregunta": "Analiza la derivación de 'posguerra'.", "respuesta": "derivación, prefijación", "explicacion": "'Posguerra' se forma añadiendo el prefijo 'pos-' (después) a 'guerra' (raíz)."},
                    {"pregunta": "Analiza la derivación de 'ultrasonido'.", "respuesta": "derivación, prefijación", "explicacion": "'Ultrasonido' se forma añadiendo el prefijo 'ultra-' (más allá) a 'sonido' (raíz)."},
                    {"pregunta": "Analiza la derivación de 'subcampeón'.", "respuesta": "derivación, prefijación", "explicacion": "'Subcampeón' se forma añadiendo el prefijo 'sub-' (inferioridad) a 'campeón' (raíz)."},
                    {"pregunta": "Analiza la derivación de 'bicicleta'.", "respuesta": "derivación, prefijación", "explicacion": "'Bicicleta' se forma añadiendo el prefijo 'bi-' (dos) a 'cicleta' (raíz)."},
                    {"pregunta": "Analiza la derivación de 'monocromo'.", "respuesta": "derivación, prefijación", "explicacion": "'Monocromo' se forma añadiendo el prefijo 'mono-' (uno) a 'cromo' (raíz)."},
                    {"pregunta": "Analiza la derivación de 'televisión'.", "respuesta": "composición", "explicacion": "'Televisión' se forma uniendo 'tele-' (distancia) y 'visión'. Es una palabra compuesta, a menudo tratada como prefijación por su origen griego."},
                    {"pregunta": "Analiza la derivación de 'automóvil'.", "respuesta": "composición", "explicacion": "'Automóvil' se forma uniendo 'auto-' (propio/por sí mismo) y 'móvil'. Es una palabra compuesta, a menudo tratada como prefijación por su origen griego."},
                    {"pregunta": "Analiza la derivación de 'fotografía'.", "respuesta": "composición", "explicacion": "'Fotografía' se forma uniendo 'foto-' (luz) y 'grafía' (escritura). Es una palabra compuesta de origen griego."},
                    {"pregunta": "Analiza la derivación de 'teléfono'.", "respuesta": "composición", "explicacion": "'Teléfono' se forma uniendo 'tele-' (distancia) y 'fono' (sonido). Es una palabra compuesta de origen griego."},
                    {"pregunta": "Analiza la derivación de 'biología'.", "respuesta": "composición", "explicacion": "'Biología' se forma uniendo 'bio-' (vida) y 'logía' (ciencia). Es una palabra compuesta de origen griego."},
                    {"pregunta": "Analiza la derivación de 'geología'.", "respuesta": "composición", "explicacion": "'Geología' se forma uniendo 'geo-' (tierra) y 'logía' (ciencia). Es una palabra compuesta de origen griego."},
                    {"pregunta": "Analiza la derivación de 'cronómetro'.", "respuesta": "composición", "explicacion": "'Cronómetro' se forma uniendo 'crono-' (tiempo) y 'metro' (medida). Es una palabra compuesta de origen griego."},
                    {"pregunta": "Analiza la derivación de 'hidroterapia'.", "respuesta": "composición", "explicacion": "'Hidroterapia' se forma uniendo 'hidro-' (agua) y 'terapia'. Es una palabra compuesta de origen griego."},
                    {"pregunta": "Analiza la derivación de 'neumático'.", "respuesta": "derivación, sufijación", "explicacion": "'Neumático' se forma añadiendo el sufijo '-ático' (relativo a) a 'neuma' (raíz)."},
                    {"pregunta": "Analiza la derivación de 'carnicero'.", "respuesta": "derivación, sufijación", "explicacion": "'Carnicero' se forma añadiendo el sufijo '-ero' (profesión) a 'carne' (raíz)."},
                    {"pregunta": "Analiza la derivación de 'lavadero'.", "respuesta": "derivación, sufijación", "explicacion": "'Lavadero' se forma añadiendo el sufijo '-dero' (lugar/instrumento) a 'lavar' (raíz verbal)."},
                    {"pregunta": "Analiza la derivación de 'limpieza'.", "respuesta": "derivación, sufijación", "explicacion": "'Limpieza' se forma añadiendo el sufijo '-eza' (cualidad) a 'limpio' (raíz)."},
                    {"pregunta": "Analiza la derivación de 'profesorado'.", "respuesta": "derivación, sufijación", "explicacion": "'Profesorado' se forma añadiendo el sufijo '-ado' (conjunto) a 'profesor' (raíz)."},
                    {"pregunta": "Analiza la derivación de 'arbolado'.", "respuesta": "derivación, sufijación", "explicacion": "'Arbolado' se forma añadiendo el sufijo '-ado' (conjunto) a 'árbol' (raíz)."},
                    {"pregunta": "Analiza la derivación de 'caserío'.", "respuesta": "derivación, sufijación", "explicacion": "'Caserío' se forma añadiendo el sufijo '-erío' (conjunto) a 'casa' (raíz)."},
                    {"pregunta": "Analiza la derivación de 'florido'.", "respuesta": "derivación, sufijación", "explicacion": "'Florido' se forma añadiendo el sufijo '-ido' (abundancia) a 'flor' (raíz)."},
                    {"pregunta": "Analiza la derivación de 'humareda'.", "respuesta": "derivación, sufijación", "explicacion": "'Humareda' se forma añadiendo el sufijo '-eda' (abundancia) a 'humo' (raíz)."},
                    {"pregunta": "Analiza la derivación de 'polvareda'.", "respuesta": "derivación, sufijación", "explicacion": "'Polvareda' se forma añadiendo el sufijo '-areda' (abundancia) a 'polvo' (raíz)."},
                    {"pregunta": "Analiza la derivación de 'lavarropas'.", "respuesta": "composición", "explicacion": "'Lavarropas' se forma uniendo 'lava' (del verbo lavar) y 'ropas'. Es una palabra compuesta."},
                    {"pregunta": "Analiza la derivación de 'parabrisas'.", "respuesta": "composición", "explicacion": "'Parabrisas' se forma uniendo 'para' (del verbo parar) y 'brisas'. Es una palabra compuesta."},
                    {"pregunta": "Analiza la derivación de 'portapapeles'.", "respuesta": "composición", "explicacion": "'Portapapeles' se forma uniendo 'porta' (del verbo portar) y 'papeles'. Es una palabra compuesta."},
                    {"pregunta": "Analiza la derivación de 'ciempiés'.", "respuesta": "composición", "explicacion": "'Ciempiés' se forma uniendo 'cien' y 'pies'. Es una palabra compuesta."},
                    {"pregunta": "Analiza la derivación de 'largavista'.", "respuesta": "composición", "explicacion": "'Largavista' se forma uniendo 'larga' y 'vista'. Es una palabra compuesta."},
                    {"pregunta": "Analiza la derivación de 'sordomudo'.", "respuesta": "composición", "explicacion": "'Sordomudo' se forma uniendo 'sordo' y 'mudo'. Es una palabra compuesta."},
                    {"pregunta": "Analiza la derivación de 'aguardiente'.", "respuesta": "composición", "explicacion": "'Aguardiente' se forma uniendo 'agua' y 'ardiente'. Es una palabra compuesta."},
                    {"pregunta": "Analiza la derivación de 'malgastar'.", "respuesta": "derivación, prefijación", "explicacion": "'Malgastar' se forma añadiendo el prefijo 'mal-' (mal) a 'gastar' (raíz)."},
                    {"pregunta": "Analiza la derivación de 'supermercado'.", "respuesta": "derivación, prefijación", "explicacion": "'Supermercado' se forma añadiendo el prefijo 'super-' (superioridad) a 'mercado' (raíz)."},
                    {"pregunta": "Analiza la derivación de 'extraordinario'.", "respuesta": "derivación, prefijación", "explicacion": "'Extraordinario' se forma añadiendo el prefijo 'extra-' (fuera de) a 'ordinario' (raíz)."},
                    {"pregunta": "Analiza la derivación de 'desaparecer'.", "respuesta": "derivación, prefijación", "explicacion": "'Desaparecer' se forma añadiendo el prefijo 'des-' (negación) a 'aparecer' (raíz)."},
                    {"pregunta": "Analiza la derivación de 'prejuicio'.", "respuesta": "derivación, prefijación", "explicacion": "'Prejuicio' se forma añadiendo el prefijo 'pre-' (anterioridad) a 'juicio' (raíz)."},
                    {"pregunta": "Analiza la derivación de 'reposición'.", "respuesta": "derivación, prefijación", "explicacion": "'Reposición' se forma añadiendo el prefijo 're-' (repetición) a 'posición' (raíz)."},
                    {"pregunta": "Analiza la derivación de 'antediluviano'.", "respuesta": "derivación, prefijación", "explicacion": "'Antediluviano' se forma añadiendo el prefijo 'ante-' (anterioridad) a 'diluviano' (raíz)."},
                    {"pregunta": "Analiza la derivación de 'convivir'.", "respuesta": "derivación, prefijación", "explicacion": "'Convivir' se forma añadiendo el prefijo 'con-' (compañía) a 'vivir' (raíz)."},
                    {"pregunta": "Analiza la derivación de 'bilingüe'.", "respuesta": "derivación, prefijación", "explicacion": "'Bilingüe' se forma añadiendo el prefijo 'bi-' (dos) a 'lingüe' (raíz)."},
                    {"pregunta": "Analiza la derivación de 'monopatín'.", "respuesta": "derivación, prefijación", "explicacion": "'Monopatín' se forma añadiendo el prefijo 'mono-' (uno) a 'patín' (raíz)."},
                    {"pregunta": "Analiza la derivación de 'polideportivo'.", "respuesta": "derivación, prefijación", "explicacion": "'Polideportivo' se forma añadiendo el prefijo 'poli-' (muchos) a 'deportivo' (raíz)."},
                    {"pregunta": "Analiza la derivación de 'semicírculo'.", "respuesta": "derivación, prefijación", "explicacion": "'Semicírculo' se forma añadiendo el prefijo 'semi-' (medio) a 'círculo' (raíz)."},
                    {"pregunta": "Analiza la derivación de 'ultramar'.", "respuesta": "derivación, prefijación", "explicacion": "'Ultramar' se forma añadiendo el prefijo 'ultra-' (más allá) a 'mar' (raíz)."},
                    {"pregunta": "Analiza la derivación de 'exclamar'.", "respuesta": "derivación, prefijación", "explicacion": "'Exclamar' se forma añadiendo el prefijo 'ex-' (hacia fuera) a 'clamar' (raíz)."},
                    {"pregunta": "Analiza la derivación de 'infraestructura'.", "respuesta": "derivación, prefijación", "explicacion": "'Infraestructura' se forma añadiendo el prefijo 'infra-' (debajo) a 'estructura' (raíz)."},
                    {"pregunta": "Analiza la derivación de 'intercambio'.", "respuesta": "derivación, prefijación", "explicacion": "'Intercambio' se forma añadiendo el prefijo 'inter-' (entre) a 'cambio' (raíz)."},
                    {"pregunta": "Analiza la derivación de 'postdata'.", "respuesta": "derivación, prefijación", "explicacion": "'Postdata' se forma añadiendo el prefijo 'post-' (después) a 'data' (raíz)."},
                    {"pregunta": "Analiza la derivación de 'anormal'.", "respuesta": "derivación, prefijación", "explicacion": "'Anormal' se forma añadiendo el prefijo 'a-' (negación) a 'normal' (raíz)."},
                    {"pregunta": "Analiza la derivación de 'automático'.", "respuesta": "composición", "explicacion": "'Automático' se forma uniendo 'auto-' (propio) y 'mático' (relacionado con el movimiento)."},
                    {"pregunta": "Analiza la derivación de 'geografía'.", "respuesta": "composición", "explicacion": "'Geografía' se forma uniendo 'geo-' (tierra) y '-grafía' (descripción)."},
                    {"pregunta": "Analiza la derivación de 'termómetro'.", "respuesta": "composición", "explicacion": "'Termómetro' se forma uniendo 'termo-' (calor) y '-metro' (medida)."},
                    {"pregunta": "Analiza la derivación de 'hidrofobia'.", "respuesta": "composición", "explicacion": "'Hidrofobia' se forma uniendo 'hidro-' (agua) y '-fobia' (miedo)."},
                    {"pregunta": "Analiza la derivación de 'cabeza'.", "respuesta": "palabra simple", "explicacion": "'Cabeza' es una palabra simple, sin derivación ni composición evidentes."},
                    {"pregunta": "Analiza la derivación de 'sol'.", "respuesta": "palabra simple", "explicacion": "'Sol' es una palabra simple, sin derivación ni composición evidentes."},
                    {"pregunta": "Analiza la derivación de 'mar'.", "respuesta": "palabra simple", "explicacion": "'Mar' es una palabra simple, sin derivación ni composición evidentes."},
                    {"pregunta": "Analiza la derivación de 'flor'.", "respuesta": "palabra simple", "explicacion": "'Flor' es una palabra simple, sin derivación ni composición evidentes."},
                    {"pregunta": "Analiza la derivación de 'libro'.", "respuesta": "palabra simple", "explicacion": "'Libro' es una palabra simple, sin derivación ni composición evidentes."},
                    {"pregunta": "Analiza la derivación de 'casa'.", "respuesta": "palabra simple", "explicacion": "'Casa' es una palabra simple, sin derivación ni composición evidentes."},
                    {"pregunta": "Analiza la derivación de 'comer'.", "respuesta": "palabra simple", "explicacion": "'Comer' es una palabra simple, un verbo sin prefijos o sufijos derivativos."},
                    {"pregunta": "Analiza la derivación de 'grande'.", "respuesta": "palabra simple", "explicacion": "'Grande' es una palabra simple, un adjetivo sin prefijos o sufijos derivativos."},
                    {"pregunta": "Analiza la derivación de 'perro'.", "respuesta": "palabra simple", "explicacion": "'Perro' es una palabra simple, sin derivación ni composición evidentes."},
                    {"pregunta": "Analiza la derivación de 'azul'.", "respuesta": "palabra simple", "explicacion": "'Azul' es una palabra simple, sin derivación ni composición evidentes."},
                    {"pregunta": "Analiza la derivación de 'verde'.", "respuesta": "palabra simple", "explicacion": "'Verde' es una palabra simple, sin derivación ni composición evidentes."},
                    {"pregunta": "Analiza la derivación de 'blanco'.", "respuesta": "palabra simple", "explicacion": "'Blanco' es una palabra simple, sin derivación ni composición evidentes."},
                    {"pregunta": "Analiza la derivación de 'negro'.", "respuesta": "palabra simple", "explicacion": "'Negro' es una palabra simple, sin derivación ni composición evidentes."},
                    {"pregunta": "Analiza la derivación de 'rápido'.", "respuesta": "palabra simple", "explicacion": "'Rápido' es una palabra simple, sin derivación ni composición evidentes."},
                    {"pregunta": "Analiza la derivación de 'lento'.", "respuesta": "palabra simple", "explicacion": "'Lento' es una palabra simple, sin derivación ni composición evidentes."},
                    {"pregunta": "Analiza la derivación de 'feliz'.", "respuesta": "palabra simple", "explicacion": "'Feliz' es una palabra simple, sin derivación ni composición evidentes."},
                    {"pregunta": "Analiza la derivación de 'triste'.", "respuesta": "palabra simple", "explicacion": "'Triste' es una palabra simple, sin derivación ni composición evidentes."},
                    {"pregunta": "Analiza la derivación de 'dormir'.", "respuesta": "palabra simple", "explicacion": "'Dormir' es una palabra simple, un verbo sin afijos derivativos."},
                    {"pregunta": "Analiza la derivación de 'vivir'.", "respuesta": "palabra simple", "explicacion": "'Vivir' es una palabra simple, un verbo sin afijos derivativos."},
                    {"pregunta": "Analiza la derivación de 'leer'.", "respuesta": "palabra simple", "explicacion": "'Leer' es una palabra simple, un verbo sin afijos derivativos."},
                    {"pregunta": "Analiza la derivación de 'escribir'.", "respuesta": "palabra simple", "explicacion": "'Escribir' es una palabra simple, un verbo sin afijos derivativos."},
                    {"pregunta": "Analiza la derivación de 'cantar'.", "respuesta": "palabra simple", "explicacion": "'Cantar' es una palabra simple, un verbo sin afijos derivativos."},
                    {"pregunta": "Analiza la derivación de 'jugar'.", "respuesta": "palabra simple", "explicacion": "'Jugar' es una palabra simple, un verbo sin afijos derivativos."},
                    {"pregunta": "Analiza la derivación de 'lavar'.", "respuesta": "palabra simple", "explicacion": "'Lavar' es una palabra simple, un verbo sin afijos derivativos."},
                    {"pregunta": "Analiza la derivación de 'limpiar'.", "respuesta": "palabra simple", "explicacion": "'Limpiar' es una palabra simple, un verbo sin afijos derivativos."},
                    {"pregunta": "Analiza la derivación de 'cocinar'.", "respuesta": "palabra simple", "explicacion": "'Cocinar' es una palabra simple, un verbo sin afijos derivativos."},
                    {"pregunta": "Analiza la derivación de 'trabajar'.", "respuesta": "palabra simple", "explicacion": "'Trabajar' es una palabra simple, un verbo sin afijos derivativos."},
                    {"pregunta": "Analiza la derivación de 'ayudar'.", "respuesta": "palabra simple", "explicacion": "'Ayudar' es una palabra simple, un verbo sin afijos derivativos."},
                    {"pregunta": "Analiza la derivación de 'pensar'.", "respuesta": "palabra simple", "explicacion": "'Pensar' es una palabra simple, un verbo sin afijos derivativos."},
                    {"pregunta": "Analiza la derivación de 'hablar'.", "respuesta": "palabra simple", "explicacion": "'Hablar' es una palabra simple, un verbo sin afijos derivativos."},
                    {"pregunta": "Analiza la derivación de 'escuchar'.", "respuesta": "palabra simple", "explicacion": "'Escuchar' es una palabra simple, un verbo sin afijos derivativos."},
                    {"pregunta": "Analiza la derivación de 'ver'.", "respuesta": "palabra simple", "explicacion": "'Ver' es una palabra simple, un verbo sin afijos derivativos."},
                    {"pregunta": "Analiza la derivación de 'dar'.", "respuesta": "palabra simple", "explicacion": "'Dar' es una palabra simple, un verbo sin afijos derivativos."},
                    {"pregunta": "Analiza la derivación de 'tener'.", "respuesta": "palabra simple", "explicacion": "'Tener' es una palabra simple, un verbo sin afijos derivativos."},
                    {"pregunta": "Analiza la derivación de 'venir'.", "respuesta": "palabra simple", "explicacion": "'Venir' es una palabra simple, un verbo sin afijos derivativos."},
                    {"pregunta": "Analiza la derivación de 'ir'.", "respuesta": "palabra simple", "explicacion": "'Ir' es una palabra simple, un verbo sin afijos derivativos."},
                    {"pregunta": "Analiza la derivación de 'ser'.", "respuesta": "palabra simple", "explicacion": "'Ser' es una palabra simple, un verbo sin afijos derivativos."},
                    {"pregunta": "Analiza la derivación de 'estar'.", "respuesta": "palabra simple", "explicacion": "'Estar' es una palabra simple, un verbo sin afijos derivativos."}
                ]
            }
        }
    }

def normalizar_respuesta(respuesta):
    """Normaliza una respuesta para comparación (quitar espacios, minúsculas, eliminar tildes, ordenar las partes)."""
    if isinstance(respuesta, str):
        # Eliminar tildes y convertir a minúsculas
        respuesta = respuesta.lower().replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')
        # Dividir por comas, limpiar espacios y ordenar las partes para mayor flexibilidad
        partes = [p.strip() for p in respuesta.split(',') if p.strip()]
        return ', '.join(sorted(partes))
    return respuesta

def comparar_respuestas(respuesta_usuario, respuesta_correcta):
    """Compara la respuesta del usuario con la respuesta correcta después de normalizar."""
    return normalizar_respuesta(respuesta_usuario) == normalizar_respuesta(respuesta_correcta)

def iniciar_practica_derivacion_morfologica():
    """Inicia la práctica de derivación morfológica en castellano en consola."""
    ejercicios_castellano = cargar_ejercicios_derivacion_morfologica()
    
    # Accedemos directamente a los ejercicios de derivación morfológica
    ejercicios_derivacion = ejercicios_castellano["Morfología"]["Avanzado"]["Derivación Morfológica y Estructura"]
    
    if not ejercicios_derivacion:
        print("No hay ejercicios de derivación morfológica disponibles.")
        return

    random.shuffle(ejercicios_derivacion) # Mezclar los ejercicios

    puntuacion = 0
    resultados = []

    print("\n--- ¡Bienvenido a la Práctica de Derivación Morfológica en Lengua Castellana! ---")
    print("Para cada palabra, indica el tipo de proceso morfológico que la ha formado.")
    print("Tipos de derivación: 'derivación, prefijación', 'derivación, sufijación', 'composición'.")
    print("Si no presenta derivación, indica: 'palabra simple'.")
    print(f"Tienes {len(ejercicios_derivacion)} ejercicios para practicar.\n")

    for i, ejercicio in enumerate(ejercicios_derivacion):
        print(f"\n--- Ejercicio {i + 1} de {len(ejercicios_derivacion)} ---")
        print(f"Palabra: '{ejercicio['pregunta']}'")
        
        respuesta_usuario = input("Tu respuesta (ej: derivación, sufijación): ").strip()

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
    print(f"Has obtenido {puntuacion} de {len(ejercicios_derivacion)} respuestas correctas.")
    print("\n--- Resumen de Resultados ---")
    for res in resultados:
        estado = "✅ CORRECTO" if res['correcta'] else "❌ INCORRECTO"
        print(f"\nPalabra: '{res['pregunta']}'")
        print(f"Tu respuesta: {res['tu_respuesta']}")
        print(f"Respuesta correcta: **{res['respuesta_correcta']}**")
        print(f"Estado: {estado}")
        print(f"Explicación: {res['explicacion']}")
    
    print("\n¡Gracias por practicar!")

if __name__ == "__main__":
    iniciar_practica_derivacion_morfologica()
