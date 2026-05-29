import time

# Lista de reglas con ejemplos y oraciones
rules = [
    {
        "rule": "La letra g se usa antes de las vocales e e i.",
        "examples": {
            "gente": "La gente estaba feliz.",
            "gesto": "Su gesto fue amable.",
            "girar": "Vamos a girar a la izquierda.",
            "gigante": "El árbol es gigante.",
            "germen": "El germen causó la enfermedad.",
            "general": "El general dio la orden.",
            "género": "Me gusta ese género musical.",
            "geografía": "Estudiaremos la geografía del país.",
            "geometría": "La geometría es una rama de las matemáticas.",
            "gimnasia": "Ella practica gimnasia todos los días."
        }
    },
    {
        "rule": "Terminaciones -gen, -gélico, -gético, -genario.",
        "examples": {
            "origen": "El origen de la historia es antiguo.",
            "imagen": "Esa imagen es muy clara.",
            "oxígeno": "El oxígeno es esencial para la vida.",
            "vigésimo": "Hoy es su vigésimo cumpleaños.",
            "energúmeno": "Se comportó como un energúmeno.",
            "diabético": "Él es diabético desde hace años.",
            "angélico": "Tiene un rostro angélico.",
            "energético": "Necesito un alimento energético.",
            "sexagenario": "Es un hombre sexagenario.",
            "octogenario": "Ella es una mujer octogenaria."
        }
    },
    {
        "rule": "Terminaciones -gia, -gio, -gión.",
        "examples": {
            "magia": "La magia del espectáculo me fascinó.",
            "geología": "Estudiaremos la geología del terreno.",
            "teología": "Se especializó en teología.",
            "energía": "La energía solar es limpia.",
            "liturgia": "La liturgia de la misa fue solemne.",
            "litigio": "El litigio duró varios años.",
            "prestigio": "Esa universidad tiene mucho prestigio.",
            "religión": "Cada uno tiene su religión.",
            "región": "Esa región es muy montañosa.",
            "legislador": "El legislador propuso una nueva ley."
        }
    },
    {
        "rule": "Sufijos -logía y -gógico.",
        "examples": {
            "biología": "La biología estudia los seres vivos.",
            "psicología": "Ella estudia psicología.",
            "tecnología": "La tecnología avanza rápidamente.",
            "arqueología": "La arqueología descubre el pasado.",
            "ecología": "La ecología es importante para el medio ambiente.",
            "dermatología": "La dermatología trata enfermedades de la piel.",
            "pedagógico": "El método pedagógico es eficaz.",
            "demagógico": "El discurso fue demagógico.",
            "teológico": "Es un tratado teológico.",
            "filosófico": "Me gusta leer textos filosóficos."
        }
    },
    {
        "rule": "Palabras que empiezan con geo-, gest-, gen-.",
        "examples": {
            "geografía": "La geografía de la región es variada.",
            "geometría": "La geometría nos ayuda a entender el espacio.",
            "geología": "La geología estudia la tierra.",
            "gestión": "La gestión del proyecto fue excelente.",
            "gesticular": "Suele gesticular mucho cuando habla.",
            "gesto": "Ese gesto fue muy amable.",
            "general": "El general dirigió la operación.",
            "generación": "Cada generación tiene sus retos.",
            "genético": "El estudio genético reveló nueva información.",
            "gentil": "El anfitrión fue muy gentil."
        }
    },
    {
        "rule": "La letra j se usa antes de las vocales a, o, u.",
        "examples": {
            "jamón": "Me gusta el jamón serrano.",
            "jarra": "Llenó la jarra de agua.",
            "jarrón": "El jarrón se rompió.",
            "joven": "El joven es muy talentoso.",
            "jornada": "La jornada laboral fue intensa.",
            "jugar": "Vamos a jugar al fútbol.",
            "júbilo": "El júbilo llenó el estadio.",
            "juicio": "El juicio fue justo.",
            "juntar": "Vamos a juntar las piezas.",
            "justicia": "La justicia prevaleció."
        }
    },
    {
        "rule": "Terminaciones -aje, -eje.",
        "examples": {
            "viaje": "El viaje fue largo pero divertido.",
            "traje": "Me puse un traje para la boda.",
            "lenguaje": "El lenguaje es la base de la comunicación.",
            "coraje": "Necesitó mucho coraje para hacerlo.",
            "drenaje": "El drenaje de la ciudad es eficiente.",
            "mensaje": "Le dejé un mensaje en su teléfono.",
            "garaje": "El coche está en el garaje.",
            "personaje": "Es un personaje muy interesante.",
            "paisaje": "El paisaje era impresionante.",
            "pasaje": "Compré un pasaje para el tren."
        }
    },
    {
        "rule": "Verbos terminados en -jar, -jear.",
        "examples": {
            "trabajar": "Necesito trabajar más horas.",
            "teclear": "Sabe teclear muy rápido.",
            "dibujar": "Le gusta dibujar paisajes.",
            "viajar": "Quiero viajar por el mundo.",
            "empujar": "Tuvo que empujar la puerta.",
            "dejar": "No puedo dejar de pensar en eso.",
            "alojar": "Nos vamos a alojar en un hotel.",
            "manejar": "Él sabe manejar muy bien.",
            "reflejar": "El espejo puede reflejar la luz.",
            "festejar": "Vamos a festejar tu cumpleaños."
        }
    },
    {
        "rule": "Formas verbales que terminan en -je, -ja, -jo, -ju.",
        "examples": {
            "dije": "Le dije la verdad.",
            "trajiste": "¿Qué trajiste para la cena?",
            "condujo": "Ella condujo hasta el centro.",
            "dejé": "Dejé las llaves en la mesa.",
            "reflejé": "Me reflejé en el espejo.",
            "empujé": "Empujé la puerta con fuerza.",
            "corregí": "Corregí todos los errores.",
            "fijé": "Fijé la lámpara en el techo.",
            "tejer": "Mi abuela sabe tejer.",
            "dibujó": "Él dibujó un hermoso paisaje."
        }
    },
    {
        "rule": "Palabras que empiezan con eje-, aje-, adje-.",
        "examples": {
            "ejemplo": "Me dio un buen ejemplo.",
            "ejercer": "Ella va a ejercer su derecho a votar.",
            "ejecución": "La ejecución del plan fue perfecta.",
            "ajeno": "No te metas en asuntos ajenos.",
            "ajedrez": "Me gusta jugar al ajedrez.",
            "ajedrecista": "El ajedrecista ganó la partida.",
            "ajustar": "Tenemos que ajustar el presupuesto.",
            "ajuste": "Hicieron un ajuste en la máquina.",
            "adjetivo": "El adjetivo describe al sustantivo.",
            "adjetivar": "No se debe adjetivar en exceso."
        }
    }
]

def main():
    print("Bienvenido al programa para memorizar las reglas del uso de la G y la J en español.")
    time.sleep(1)

    for idx, rule in enumerate(rules):
        print(f"\nRegla {idx + 1}: {rule['rule']}")
        time.sleep(1)

        for word, sentence in rule['examples'].items():
            print(f"\nOración: {sentence}")
            user_input = input("Escribe la palabra correcta o la oración completa: ").strip()
            
            if user_input.lower() == word.lower() or user_input.lower() == sentence.lower():
                print("¡Correcto!")
            else:
                print(f"Incorrecto. La palabra correcta es: {word}")
                print(f"La oración correcta es: {sentence}")

        time.sleep(2)

if __name__ == "__main__":
    main()
