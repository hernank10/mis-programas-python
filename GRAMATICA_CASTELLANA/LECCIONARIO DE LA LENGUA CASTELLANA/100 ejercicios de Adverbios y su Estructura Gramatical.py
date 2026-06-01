import random

def cargar_ejercicios_adverbios():
    """
    Carga los 100 ejercicios predefinidos de tipos de adverbios y su estructura gramatical
    directamente en el código.
    """
    print("Cargando 100 ejercicios de Adverbios y su Estructura Gramatical directamente...")
    return {
        "Morfología": {
            "Intermedio": {
                "Adverbios y Estructura": [
                    {"pregunta": "Identifica el adverbio y su tipo en: 'Él camina **lentamente**.'", "respuesta": "lentamente, modo", "explicacion": "'Lentamente' indica la manera en que camina."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'Nos vemos **mañana**.'", "respuesta": "mañana, tiempo", "explicacion": "'Mañana' indica cuándo se verán."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'El libro está **aquí**.'", "respuesta": "aquí, lugar", "explicacion": "'Aquí' indica la ubicación del libro."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'Comió **mucho**.'", "respuesta": "mucho, cantidad", "explicacion": "'Mucho' indica la cantidad que comió."},
                    {"pregunta": "Identifica el adverbio y su tipo en: '**Sí**, quiero ir.'", "respuesta": "sí, afirmación", "explicacion": "'Sí' expresa afirmación."},
                    {"pregunta": "Identifica el adverbio y su tipo en: '**No** iré a la fiesta.'", "respuesta": "no, negación", "explicacion": "'No' expresa negación."},
                    {"pregunta": "Identifica el adverbio y su tipo en: '**Quizás** llueva.'", "respuesta": "quizás, duda", "explicacion": "'Quizás' expresa incertidumbre o duda."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'Ella habla **claramente**.'", "respuesta": "claramente, modo", "explicacion": "'Claramente' indica la manera en que habla."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'Llegó **tarde**.'", "respuesta": "tarde, tiempo", "explicacion": "'Tarde' indica el momento de la llegada."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'Vivo **cerca** de la playa.'", "respuesta": "cerca, lugar", "explicacion": "'Cerca' indica proximidad espacial."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'Estudié **bastante**.'", "respuesta": "bastante, cantidad", "explicacion": "'Bastante' indica una cantidad considerable."},
                    {"pregunta": "Identifica el adverbio y su tipo en: '**También** vino mi hermano.'", "respuesta": "también, afirmación", "explicacion": "'También' añade un elemento afirmativo."},
                    {"pregunta": "Identifica el adverbio y su tipo en: '**Nunca** lo haré.'", "respuesta": "nunca, negación", "explicacion": "'Nunca' indica negación de tiempo."},
                    {"pregunta": "Identifica el adverbio y su tipo en: '**Tal vez** venga.'", "respuesta": "tal vez, duda", "explicacion": "'Tal vez' indica posibilidad."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'Lo hizo **rápidamente**.'", "respuesta": "rápidamente, modo", "explicacion": "'Rápidamente' indica la velocidad de la acción."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'Terminé **hoy**.'", "respuesta": "hoy, tiempo", "explicacion": "'Hoy' indica el día de la finalización."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'Baja **abajo**.'", "respuesta": "abajo, lugar", "explicacion": "'Abajo' indica dirección descendente."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'Casi **siempre** llego a tiempo.'", "respuesta": "siempre, tiempo", "explicacion": "'Siempre' indica una frecuencia constante."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'Hay **menos** gente.'", "respuesta": "menos, cantidad", "explicacion": "'Menos' indica una cantidad reducida."},
                    {"pregunta": "Identifica el adverbio y su tipo en: '**Evidentemente** tiene razón.'", "respuesta": "evidentemente, afirmación", "explicacion": "'Evidentemente' refuerza la certeza."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'Ella **jamás** miente.'", "respuesta": "jamás, negación", "explicacion": "'Jamás' indica una negación absoluta en el tiempo."},
                    {"pregunta": "Identifica el adverbio y su tipo en: '**Acaso** sea verdad.'", "respuesta": "acaso, duda", "explicacion": "'Acaso' expresa una pequeña duda."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'Respondió **cortésmente**.'", "respuesta": "cortésmente, modo", "explicacion": "'Cortésmente' indica la manera educada de responder."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'Fui al cine **ayer**.'", "respuesta": "ayer, tiempo", "explicacion": "'Ayer' indica el día de la acción."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'Está **delante** de la casa.'", "respuesta": "delante, lugar", "explicacion": "'Delante' indica posición frontal."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'Había **demasiado** ruido.'", "respuesta": "demasiado, cantidad", "explicacion": "'Demasiado' indica una cantidad excesiva."},
                    {"pregunta": "Identifica el adverbio y su tipo en: '**Ciertamente** lo haré.'", "respuesta": "ciertamente, afirmación", "explicacion": "'Ciertamente' expresa certeza."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'Él **tampoco** sabe.'", "respuesta": "tampoco, negación", "explicacion": "'Tampoco' indica negación en adición."},
                    {"pregunta": "Identifica el adverbio y su tipo en: '**Posiblemente** viaje.'", "respuesta": "posiblemente, duda", "explicacion": "'Posiblemente' indica una posibilidad."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'Lo hizo **fácilmente**.'", "respuesta": "fácilmente, modo", "explicacion": "'Fácilmente' indica la manera sencilla de hacerlo."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'Ven **pronto**.'", "respuesta": "pronto, tiempo", "explicacion": "'Pronto' indica un tiempo cercano."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'Mira **allá**.'", "respuesta": "allá, lugar", "explicacion": "'Allá' indica un lugar lejano."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'Compró **algo**.'", "respuesta": "algo, cantidad", "explicacion": "'Algo' indica una cantidad indeterminada."},
                    {"pregunta": "Identifica el adverbio y su tipo en: '**Desde luego** que sí.'", "respuesta": "desde luego, afirmación", "explicacion": "Locución adverbial de afirmación."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'No tengo **nada** que decir.'", "respuesta": "nada, negación", "explicacion": "'Nada' expresa ausencia o negación de algo."},
                    {"pregunta": "Identifica el adverbio y su tipo en: '**Seguramente** aprobarás.'", "respuesta": "seguramente, duda", "explicacion": "'Seguramente' indica una alta probabilidad (aunque es de duda, se acerca a la afirmación)."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'Lo logré **difícilmente**.'", "respuesta": "difícilmente, modo", "explicacion": "'Difícilmente' indica una manera con dificultad."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'Te veo **luego**.'", "respuesta": "luego, tiempo", "explicacion": "'Luego' indica un tiempo posterior."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'Sube **arriba**.'", "respuesta": "arriba, lugar", "explicacion": "'Arriba' indica dirección ascendente."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'Estaba **medio** dormido.'", "respuesta": "medio, cantidad", "explicacion": "'Medio' indica una cantidad a la mitad."},
                    {"pregunta": "Identifica el adverbio y su tipo en: '**Exactamente** así fue.'", "respuesta": "exactamente, afirmación", "explicacion": "'Exactamente' expresa precisión y afirmación."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'No tengo **ninguna** duda.'", "respuesta": "ninguna, negación", "explicacion": "'Ninguna' expresa negación o ausencia total."},
                    {"pregunta": "Identifica el adverbio y su tipo en: '**Probablemente** no lo haga.'", "respuesta": "probablemente, duda", "explicacion": "'Probablemente' indica una posibilidad."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'Se comportó **mal**.'", "respuesta": "mal, modo", "explicacion": "'Mal' indica una mala manera de comportarse."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'Llegó **temprano**.'", "respuesta": "temprano, tiempo", "explicacion": "'Temprano' indica un tiempo anticipado."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'Estaba **detrás** del árbol.'", "respuesta": "detrás, lugar", "explicacion": "'Detrás' indica posición posterior."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'Comió **poco**.'", "respuesta": "poco, cantidad", "explicacion": "'Poco' indica una cantidad escasa."},
                    {"pregunta": "Identifica el adverbio y su tipo en: '**Claro** que sí.'", "respuesta": "claro, afirmación", "explicacion": "Expresa una afirmación contundente."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'Ella **apenas** come.'", "respuesta": "apenas, cantidad", "explicacion": "'Apenas' indica una cantidad mínima."},
                    {"pregunta": "Identifica el adverbio y su tipo en: '**Todavía** no ha llegado.'", "respuesta": "todavía, tiempo", "explicacion": "'Todavía' indica una persistencia en el tiempo."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'Se encuentra **fuera**.'", "respuesta": "fuera, lugar", "explicacion": "'Fuera' indica el exterior."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'Corrió **muchísimo**.'", "respuesta": "muchísimo, cantidad", "explicacion": "'Muchísimo' indica una cantidad muy grande."},
                    {"pregunta": "Identifica el adverbio y su tipo en: '**Verdaderamente** lo aprecio.'", "respuesta": "verdaderamente, afirmación", "explicacion": "'Verdaderamente' enfatiza la autenticidad."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'No lo haré **jamás**.'", "respuesta": "jamás, negación", "explicacion": "'Jamás' enfatiza la negación en el tiempo."},
                    {"pregunta": "Identifica el adverbio y su tipo en: '**A lo mejor** viene.'", "respuesta": "a lo mejor, duda", "explicacion": "Locución adverbial que expresa posibilidad."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'Habla **despacio**.'", "respuesta": "despacio, modo", "explicacion": "'Despacio' indica la velocidad lenta."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'Lo haremos **ahora**.'", "respuesta": "ahora, tiempo", "explicacion": "'Ahora' indica el momento presente."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'Los niños están **dentro**.'", "respuesta": "dentro, lugar", "explicacion": "'Dentro' indica el interior."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'Come **bastante** bien.'", "respuesta": "bastante, cantidad", "explicacion": "'Bastante' modifica al adverbio 'bien', indicando grado."},
                    {"pregunta": "Identifica el adverbio y su tipo en: '**Desde luego** que no.'", "respuesta": "desde luego, negación", "explicacion": "Locución adverbial que niega con énfasis."},
                    {"pregunta": "Identifica el adverbio y su tipo en: '**Casi** lo consigo.'", "respuesta": "casi, cantidad", "explicacion": "'Casi' indica una cantidad incompleta."},
                    {"pregunta": "Identifica el adverbio y su tipo en: '**Quizá** se equivoque.'", "respuesta": "quizá, duda", "explicacion": "'Quizá' expresa incertidumbre."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'Actúa **generosamente**.'", "respuesta": "generosamente, modo", "explicacion": "'Generosamente' indica una manera de actuar."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'Me iré **pronto**.'", "respuesta": "pronto, tiempo", "explicacion": "'Pronto' indica un tiempo futuro cercano."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'Vive **lejos**.'", "respuesta": "lejos, lugar", "explicacion": "'Lejos' indica una gran distancia."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'Es **totalmente** cierto.'", "respuesta": "totalmente, cantidad", "explicacion": "'Totalmente' indica la totalidad o el grado máximo."},
                    {"pregunta": "Identifica el adverbio y su tipo en: '**Así** es.'", "respuesta": "así, afirmación", "explicacion": "'Así' puede usarse para afirmar."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'No veo **ningún** problema.'", "respuesta": "ningún, negación", "explicacion": "'Ningún' indica la ausencia total (aunque también es determinante)."},
                    {"pregunta": "Identifica el adverbio y su tipo en: '**Difícilmente** llegará a tiempo.'", "respuesta": "difícilmente, duda", "explicacion": "'Difícilmente' expresa baja probabilidad."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'Lo hizo **perfectamente**.'", "respuesta": "perfectamente, modo", "explicacion": "'Perfectamente' indica una manera impecable."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'Vendrá **después**.'", "respuesta": "después, tiempo", "explicacion": "'Después' indica un tiempo posterior."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'Está **debajo** de la mesa.'", "respuesta": "debajo, lugar", "explicacion": "'Debajo' indica posición inferior."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'Hay **suficiente** comida.'", "respuesta": "suficiente, cantidad", "explicacion": "'Suficiente' indica una cantidad adecuada."},
                    {"pregunta": "Identifica el adverbio y su tipo en: '**Desde luego** que no es así.'", "respuesta": "desde luego, negación", "explicacion": "Locución adverbial de negación."},
                    {"pregunta": "Identifica el adverbio y su tipo en: '**Algo** he comido.'", "respuesta": "algo, cantidad", "explicacion": "'Algo' indica una cantidad pequeña e imprecisa."},
                    {"pregunta": "Identifica el adverbio y su tipo en: '**Seguramente** me equivoqué.'", "respuesta": "seguramente, duda", "explicacion": "'Seguramente' indica una alta probabilidad (casi afirmación de duda)."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'Respiró **profundamente**.'", "respuesta": "profundamente, modo", "explicacion": "'Profundamente' indica la intensidad de la respiración."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'Comeremos **después**.'", "respuesta": "después, tiempo", "explicacion": "'Después' indica un momento posterior."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'La estación está **lejos**.'", "respuesta": "lejos, lugar", "explicacion": "'Lejos' indica distancia."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'Hizo **demasiado** calor.'", "respuesta": "demasiado, cantidad", "explicacion": "'Demasiado' indica una cantidad excesiva de calor."},
                    {"pregunta": "Identifica el adverbio y su tipo en: '**Efectivamente**, es cierto.'", "respuesta": "efectivamente, afirmación", "explicacion": "'Efectivamente' expresa conformidad."},
                    {"pregunta": "Identifica el adverbio y su tipo en: '**Tampoco** quiero ese.'", "respuesta": "tampoco, negación", "explicacion": "'Tampoco' añade una negación."},
                    {"pregunta": "Identifica el adverbio y su tipo en: '**Quizás** me arrepienta.'", "respuesta": "quizás, duda", "explicacion": "'Quizás' expresa incertidumbre."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'Se vistió **elegantemente**.'", "respuesta": "elegantemente, modo", "explicacion": "'Elegantemente' indica la manera de vestir."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'Te llamaré **inmediatamente**.'", "respuesta": "inmediatamente, tiempo", "explicacion": "'Inmediatamente' indica un tiempo sin demora."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'Ponlo **encima** de la mesa.'", "respuesta": "encima, lugar", "explicacion": "'Encima' indica posición superior."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'Hay **muchos** libros.'", "respuesta": "muchos, cantidad", "explicacion": "'Muchos' indica una gran cantidad."},
                    {"pregunta": "Identifica el adverbio y su tipo en: '**Por supuesto** que sí.'", "respuesta": "por supuesto, afirmación", "explicacion": "Locución adverbial de afirmación."},
                    {"pregunta": "Identifica el adverbio y su tipo en: '**Jamás** vuelvas.'", "respuesta": "jamás, negación", "explicacion": "'Jamás' es un adverbio de negación en sentido temporal."},
                    {"pregunta": "Identifica el adverbio y su tipo en: '**Probablemente** no lo logremos.'", "respuesta": "probablemente, duda", "explicacion": "'Probablemente' indica una baja probabilidad."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'Salió **corriendo**.'", "respuesta": "corriendo, modo", "explicacion": "'Corriendo' es un gerundio que funciona como adverbio de modo."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'Llegaré **tarde**.'", "respuesta": "tarde, tiempo", "explicacion": "'Tarde' indica el momento de la llegada."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'El gato está **arriba**.'", "respuesta": "arriba, lugar", "explicacion": "'Arriba' indica posición superior."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'Compró **varios** libros.'", "respuesta": "varios, cantidad", "explicacion": "'Varios' indica una cantidad indefinida."},
                    {"pregunta": "Identifica el adverbio y su tipo en: '**Desde luego**, no es fácil.'", "respuesta": "desde luego, negación", "explicacion": "Locución adverbial de negación."},
                    {"pregunta": "Identifica el adverbio y su tipo en: '**Apenas** se mueve.'", "respuesta": "apenas, modo", "explicacion": "'Apenas' indica que se mueve con dificultad o muy poco."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'Lo supe **siempre**.'", "respuesta": "siempre, tiempo", "explicacion": "'Siempre' indica que lo supo en todo momento."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'Están **adentro**.'", "respuesta": "adentro, lugar", "explicacion": "'Adentro' indica el interior."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'Había **pocos** estudiantes.'", "respuesta": "pocos, cantidad", "explicacion": "'Pocos' indica una cantidad escasa."},
                    {"pregunta": "Identifica el adverbio y su tipo en: '**Así** lo quiero.'", "respuesta": "así, modo", "explicacion": "'Así' indica la manera en que lo quiere."},
                    {"pregunta": "Identifica el adverbio y su tipo en: '**Ni** tú ni yo.'", "respuesta": "ni, negación", "explicacion": "'Ni' es un adverbio de negación cuando está solo o repetido."},
                    {"pregunta": "Identifica el adverbio y su tipo en: '**A lo mejor** no voy.'", "respuesta": "a lo mejor, duda", "explicacion": "Locución adverbial que expresa una posibilidad negativa."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'Lo resolvió **rápidamente**.'", "respuesta": "rápidamente, modo", "explicacion": "'Rápidamente' indica la velocidad de la resolución."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'Me llamó **anoche**.'", "respuesta": "anoche, tiempo", "explicacion": "'Anoche' indica el momento en que llamó."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'El coche está **enfrente**.'", "respuesta": "enfrente, lugar", "explicacion": "'Enfrente' indica posición frontal."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'Casi **nada** de comida.'", "respuesta": "casi, cantidad", "explicacion": "'Casi' modifica a 'nada', indicando proximidad a cero."},
                    {"pregunta": "Identifica el adverbio y su tipo en: '**Por supuesto**, estoy de acuerdo.'", "respuesta": "por supuesto, afirmación", "explicacion": "Locución adverbial de afirmación."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'No lo hizo **nadie**.'", "respuesta": "nadie, negación", "explicacion": "'Nadie' es un pronombre/adverbio de negación."},
                    {"pregunta": "Identifica el adverbio y su tipo en: '**Probablemente** no venga.'", "respuesta": "probablemente, duda", "explicacion": "'Probablemente' indica una posibilidad negativa."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'Se portó **excelentemente**.'", "respuesta": "excelentemente, modo", "explicacion": "'Excelentemente' indica una manera sobresaliente."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'Lo veré **pronto**.'", "respuesta": "pronto, tiempo", "explicacion": "'Pronto' indica un tiempo cercano en el futuro."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'Estás **ahí**.'", "respuesta": "ahí, lugar", "explicacion": "'Ahí' indica un lugar cercano o medianamente lejano."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'Tengo **mucho** trabajo.'", "respuesta": "mucho, cantidad", "explicacion": "'Mucho' indica una gran cantidad."},
                    {"pregunta": "Identifica el adverbio y su tipo en: '**Verdaderamente** es un genio.'", "respuesta": "verdaderamente, afirmación", "explicacion": "'Verdaderamente' enfatiza la autenticidad de la afirmación."},
                    {"pregunta": "Identifica el adverbio y su tipo en: '**Nunca** es suficiente.'", "respuesta": "nunca, negación", "explicacion": "'Nunca' es un adverbio de tiempo que funciona como negación."},
                    {"pregunta": "Identifica el adverbio y su tipo en: '**Quizá** no lo logre.'", "respuesta": "quizá, duda", "explicacion": "'Quizá' expresa incertidumbre sobre el logro."},
                    {"pregunta": "Identifica el adverbio y su tipo en: 'Lo hizo **cuidadosamente**.'", "respuesta": "cuidadosamente, modo", "explicacion": "'Cuidadosamente' indica una manera con precaución."}
                ]
            }
        }
    }

def normalizar_respuesta(respuesta):
    """Normaliza una respuesta para comparación (quitar espacios, minúsculas, eliminar tildes, ordenar)."""
    if isinstance(respuesta, str):
        # Eliminar tildes y convertir a minúsculas
        respuesta = respuesta.lower().replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')
        # Dividir por comas, limpiar espacios y ordenar para respuestas con múltiples partes (ej. 'adverbio, modo')
        partes = [p.strip() for p in respuesta.split(',') if p.strip()]
        return ', '.join(sorted(partes))
    return respuesta

def comparar_respuestas(respuesta_usuario, respuesta_correcta):
    """Compara la respuesta del usuario con la respuesta correcta después de normalizar."""
    return normalizar_respuesta(respuesta_usuario) == normalizar_respuesta(respuesta_correcta)

def iniciar_practica_adverbios():
    """Inicia la práctica de adverbios y su estructura gramatical en consola."""
    ejercicios_castellano = cargar_ejercicios_adverbios()
    
    # Accedemos directamente a los ejercicios de adverbios
    ejercicios_adverbios = ejercicios_castellano["Morfología"]["Intermedio"]["Adverbios y Estructura"]
    
    if not ejercicios_adverbios:
        print("No hay ejercicios de adverbios disponibles.")
        return

    random.shuffle(ejercicios_adverbios) # Mezclar los ejercicios

    puntuacion = 0
    resultados = []

    print("\n--- ¡Bienvenido a la Práctica de Adverbios y su Estructura Gramatical! ---")
    print("Identifica el adverbio en la oración y luego su tipo (ej: 'aquí, lugar').")
    print("Los tipos pueden ser: modo, tiempo, lugar, cantidad, afirmación, negación, duda.")
    print(f"Tienes {len(ejercicios_adverbios)} ejercicios para practicar.\n")

    for i, ejercicio in enumerate(ejercicios_adverbios):
        print(f"\n--- Ejercicio {i + 1} de {len(ejercicios_adverbios)} ---")
        print(f"Pregunta: {ejercicio['pregunta']}")
        
        respuesta_usuario = input("Tu respuesta (ej: adverbio, tipo): ").strip()

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
    print(f"Has obtenido {puntuacion} de {len(ejercicios_adverbios)} respuestas correctas.")
    print("\n--- Resumen de Resultados ---")
    for res in resultados:
        estado = "✅ CORRECTO" if res['correcta'] else "❌ INCORRECTO"
        print(f"\nPregunta: {res['pregunta']}")
        print(f"Tu respuesta: {res['tu_respuesta']}")
        print(f"Respuesta correcta: **{res['respuesta_correcta']}**")
        print(f"Estado: {estado}")
        print(f"Explicación: {res['explicacion']}")
    
    print("\n¡Gracias por practicar!")

if __name__ == "__main__":
    iniciar_practica_adverbios()
