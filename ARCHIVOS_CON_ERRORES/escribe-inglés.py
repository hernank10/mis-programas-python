def mostrar_consejos(idioma):
    consejos_es = [
        "1. Aprende las reglas básicas de la gramática inglesa: Familiarízate con los tiempos verbales, la estructura de las oraciones, y el uso correcto de los pronombres.", 
        "2. Usa el verbo to be correctamente: Es uno de los verbos más importantes y tiene muchas funciones en inglés. ",
        "3. Domina el uso de los artículos: A - an y the son esenciales en inglés- y su uso correcto es clave. ",
        "4. Conoce la diferencia entre los tiempos verbales: Aprende cuándo usar el presente simple, el pasado simple, el presente perfecto, y otros tiempos. ",
        "5. Evita traducir literalmente: El inglés y el español tienen estructuras diferentes, y la traducción literal puede llevar a errores. ",
        "6. Aprende las preposiciones comunes: In - on, at, y for son algunas de las preposiciones más comunes en inglés. ",
        "7. Usa los verbos modales correctamente: Can, could, may, might, must, etc., son esenciales para expresar permisos, obligaciones y posibilidades. ",
        "8. Domina el uso de las contracciones: Can't, won't, I'm, you're, son comunes en el habla y la escritura informal. ",
        "9. Conoce la diferencia entre who y whom: Who se usa para el sujeto, y whom para el objeto en una oración. ",
        "10. Usa correctamente los adjetivos y adverbios: Recuerda que los adjetivos modifican sustantivos y los adverbios modifican verbos, adjetivos o adverbios. ",
        "11. Practica el orden de las palabras en las oraciones: El inglés tiene un orden de palabras más rígido que el español, generalmente sujeto-verbo-objeto. ",
        "12. Evita el uso excesivo de very: Busca sinónimos más específicos como extremely,incredibly,terribly." ,
        "13. Usa correctamente los pronombres reflexivos: Myself, yourself, himself, etc., se usan para acciones que recaen sobre el sujeto. ",
        "14. Domina los falsos amigos: Palabras que se parecen en inglés y español pero tienen significados diferentes, como actual real y actual current. ",
        "15. Aprende la diferencia entre say y tell: Say se usa para expresar lo que alguien dijo, mientras que tell se usa para comunicar algo a alguien. ",
        "16. Usa correctamente los tiempos perfectos: El presente perfecto I have eaten se usa para acciones que tienen relevancia en el presente. ",
        "17. Domina el uso de las preposiciones de tiempo: In, on, y at se usan en diferentes contextos de tiempo. ",
        "18. Usa correctamente much y many: Much se usa con incontables, y many con contables. ",
        "19. Conoce la diferencia entre few y a few: Few indica una cantidad insuficiente, y a few indica una cantidad suficiente pero pequeña. ",
        "20. Domina las preguntas indirectas: Cambia el orden de palabras y elimina el auxiliar para formar preguntas indirectas.", 
        "21. Aprende las frases verbales (phrasal verbs): Son comunes en inglés y pueden cambiar completamente el significado de un verbo. ",
        "22. Conoce la diferencia entre to y too: To es una preposición, mientras que too significa también o demasiado. ",
        "23. Usa correctamente make y do: Make se refiere a crear o producir algo, y do se refiere a realizar una acción o tarea. ",
        "24. Domina el uso de there is y there are: Se usan para indicar la existencia de algo, dependiendo si es singular o plural. ",
        "25. Aprende la diferencia entre advice y advise: Advice es un sustantivo, y advise es un verbo. ",
        "26. Evita el uso excesivo de pronombres personales: En inglés es común omitir el sujeto cuando se sobreentiende en la oración. ",
        "27. Conoce la diferencia entre who's y whose: Who's es la contracción de who is, y whose indica posesión. ",
        "28. Usa correctamente since y for: Since indica el inicio de un período de tiempo, y for indica la duración. ",
        "29. Domina el uso de either y neither: Either se usa para cualquiera de dos opciones, y neither para negar ambas. ",
        "30. Aprende la diferencia entre hear y listen: Hear es involuntario, y listen es una acción intencional. ",
        "31. Usa correctamente borrow y lend: Borrow significa tomar prestado, y lend significa prestar. ",
        "32. Domina el uso de who y which: Who se usa para personas, y which para cosas o animales. ",
        "33. Aprende la diferencia entre good y well: Good es un adjetivo, y well es un adverbio. ",
        "34. Usa correctamente bring y take: Bring implica llevar algo hacia un lugar, y take implica llevar algo desde un lugar. ",
        "35. Domina el uso de affect y effect: Affect es un verbo, y effect es un sustantivo. ",
        "36. Conoce la diferencia entre lie y lay: Lie significa recostarse, y lay significa colocar algo en un lugar. ",
        "37. Usa correctamente between y among: Between se usa para dos elementos, y among para más de dos. ",
        "38. Domina las expresiones de cantidad: A lot of, plenty of, a few, some, y cómo usarlas correctamente. ",
        "39. Aprende la diferencia entre farther y further: Farther se refiere a distancia física, y further a distancia metafórica o adicional.", 
        "40. Usa correctamente less y fewer: Less se usa con incontables, y fewer con contables. ",
        "41. Domina las oraciones condicionales: If se usa para expresar condiciones en diferentes tiempos. ",
        "42. Conoce la diferencia entre practice y practise: En inglés británico, practice es un sustantivo y practise es un verbo. ",
        "43. Aprende a usar correctamente los gerundios: Muchos verbos en inglés requieren el gerundio (-ing) después de ellos. ",
        "44. Evita la confusión entre then y than: Then indica tiempo, y than se usa para comparaciones. ",
        "45. Usa correctamente fewer y less: Fewer se usa con sustantivos contables, y less con incontables. ",
        "46. Domina el uso del verbo to get: Tiene muchos significados según el contexto (obtain,become,arrive, etc.). ",
        "47. Conoce la diferencia entre rise y raise: Rise es intransitivo, y raise es transitivo. ",
        "48. Usa correctamente since y because: Since puede indicar tiempo o causa, mientras que because solo indica causa. ",
        "49. Domina el uso de las preguntas de sí o no: Do you like...? Have you been...? Are you going...?" ,
        "50. Aprende la diferencia entre each y every: Each se refiere a individuos en un grupo, y every se refiere a todos en un grupo. ",
        "51. Conoce la diferencia entre any y some: Some se usa en afirmaciones y any en preguntas y negaciones. ",
        "52. Domina las estructuras negativas: Don't, isn't, can't, won't, etc. ",
        "53. Usa correctamente in y into: In indica dentro de algo, y into indica movimiento hacia dentro. ",
        "54. Aprende la diferencia entre other y another: Another se usa con singular, y other con plural o singular. ",
        "55. Conoce la diferencia entre to y for: To se usa para destino o propósito, y for para beneficio o duración. ",
        "56. Domina el uso del presente continuo: I am going, He is working, para acciones que están ocurriendo ahora. ",
        "57. Usa correctamente can y may:Can para capacidad, y may para permiso. ",
        "58. Aprende a usar las frases hechas y modismos: It's raining cats and dogs, break the ice, etc. ",
        "59. Conoce la diferencia entre quiet y quite: Quiet significa silencio, y quite significa bastante. ",
        "60. Domina el uso de used to: Para acciones habituales en el pasado que ya no ocurren. ",
        "61. Usa correctamente must y have to: Ambos indican obligación, pero must es más fuerte. ",
        "62. Aprende la diferencia entre no y not: No se usa para negaciones absolutas, y not para negaciones de verbos. ",
        "63. Domina el uso de will y going to: Will para decisiones inmediatas y going to para planes. ",
        "64. Conoce la diferencia entre by y until: By se usa para indicar un límite de tiempo, y until para la duración hasta un punto. ",
        "65. Usa correctamente whose y who's: Whose indica posesión, y who's es la contracción de who is." ,
        "66. Aprende a usar there,their, y they're: There indica lugar, their indica posesión, y they're es they are." ,
        "67. Domina el uso de rather y prefer: Ambos se usan para expresar preferencias, pero rather suele ir seguido de than." ,
        "68. Usa correctamente say y tell: Say se usa sin objeto directo, y tell se usa con objeto directo. ",
        "69. Conoce la diferencia entre begin y start: Begin es más formal que start, aunque a menudo son intercambiables. ",
        "70. Aprende la diferencia entre lose y loose: Lose es perder, y loose es suelto. ",
        "71. Usa correctamente give y take: Give es dar, y take es tomar. ",
        "72. Domina el uso del infinitivo y el gerundio: Algunos verbos van seguidos de infinitivo (to go) y otros de gerundio (going). ",
        "73. Conoce la diferencia entre lay y lie: Lay es colocar algo, y lie es reclinarse. ",
        "74. Usa correctamente hard y hardly: Hard es difícil, y hardly significa apenas. ",
        "75. Domina el uso de for y since: For se usa con duración, y since con un punto en el tiempo. ",
        "76. Aprende la diferencia entre bring y take: Bring es llevar hacia un lugar, y take es llevar desde un lugar. ",
        "77. Conoce la diferencia entre leave y let: Leave es irse o dejar, y let es permitir. ",
        "78. Usa correctamente do y make: Do se usa para acciones y make para crear o construir algo. ",
        "79. Domina el uso de find y found: Find es encontrar, y found es el pasado de find y también significa fundar. ",
        "80. Conoce la diferencia entre lie y lay: Lie es recostarse y lay es poner algo. ",
        "81. Aprende a usar correctamente like y as: Like se usa para comparaciones, y as para funciones o roles. ",
        "82. Usa correctamente few y a few: Few indica insuficiencia, y a few una pequeña cantidad suficiente. ",
        "83. Domina el uso de just, already, y yet: Just indica algo reciente, already algo que ya ha sucedido, y yet algo que aún no ha sucedido. ",
        "84. Conoce la diferencia entre hear y listen: Hear es percibir un sonido, y listen es prestar atención a un sonido. ",
        "85. Usa correctamente good y well: Good es un adjetivo y well un adverbio. ",
        "86. Domina el uso de as y like: As se usa para comparar acciones, y like para comparar cosas o personas. ",
        "87. Conoce la diferencia entre each y every: Each se refiere a individuos en un grupo, y every al grupo en su totalidad.",
        "88. Usa correctamente such y so: Such se usa antes de un sustantivo, y so antes de un adjetivo o adverbio. ",
        "89. Domina el uso de los adverbios de frecuencia: Always, often, sometimes,rarely,never." ,
        "90. Aprende la diferencia entre by y until: By indica un plazo, y until el final de un período de tiempo. ",
        "91. Usa correctamente few y little: Few se usa con contables, y little con incontables. ",
        "92. Conoce la diferencia entre ago y before: Ago se usa con un tiempo específico en el pasado, y before para una referencia temporal anterior.", 
        "93. Domina el uso de if y whether: If se usa en condicionales y whether en decisiones o alternativas. ",
        "94. Aprende a usar correctamente must y have to: Ambos indican obligación, pero must es más personal. ",
        "95. Conoce la diferencia entre either y neither: Either es cualquiera de dos, y neither es ninguno de los dos. ",
        "96. Usa correctamente still, yet, y already: Still indica continuidad, yet indica algo que no ha ocurrido, y already algo que ya ha ocurrido.", 
        "97. Domina el uso de because y because of: Because introduce una oración, y because of un sustantivo. ",
        "98. Conoce la diferencia entre alone y lonely: Alone es estar solo físicamente, y lonely es sentirse solo emocionalmente. ",
        "99. Usa correctamente who, whom, y whose: Who se usa para sujetos, whom para objetos, y whose para posesión. ",
        "100. Practica, practica, practica: La mejor manera de mejorar tu escritura en inglés es practicando regularmente y pidiendo retroalimentación.",
        "101. Usa un lenguaje preciso y específico.",
        "102. Revisa la coherencia en el uso de los títulos y subtítulos.",
        "103. Asegúrate de que el texto fluya naturalmente de una idea a otra.",

    consejos_en = [
        "1. Use simple sentences.",

        "1. Avoid run-on sentences: Break long sentences into shorter ones for clarity.",
        "2. Use active voice: Prefer /The team completed the project/ over /The project was completed by the team./",
        "3. Vary sentence structure: Mix simple, compound, and complex sentences.",
        "4. Use correct verb tense: Be consistent with past, present, and future tenses.",
        "5. Avoid unnecessary repetition: Don’t repeat the same ideas or words too often.",
        "6. Use parallel structure: Keep sentence elements in a balanced form, e.g., /She likes dancing, singing, and playing./",
        "7. Be concise: Remove unnecessary words.",
        "8. Use transition words: Connect ideas with words like /however,/ /therefore,/ and /moreover./",
        "9. Check subject-verb agreement: Make sure your subject and verb match in number.",
        "10. Avoid vague pronouns: Ensure that pronouns clearly refer to specific nouns.",
        "11. Use appropriate punctuation: Know when to use commas, periods, semicolons, etc.",
        "12. Learn the difference between /a/ and /the/: /A/ is for general nouns, /the/ is for specific nouns.",
        "13. Use the correct prepositions: Learn when to use /in,/ /on,/ /at,/ etc.",
        "14. Avoid overuse of adjectives and adverbs: Too many can clutter your writing.",
        "15. Use /who/ for people and /which/ for things: Use /who/ for people, /which/ for objects, and /that/ for both.",
        "16. Be aware of homophones: Know the difference between words like /their/ and /there./",
        "17. Use conjunctions properly: /And,/ /but,/ /or/ can connect ideas logically.",
        "18. Know when to use /fewer/ and /less/: /Fewer/ is for countable items, /less/ for uncountable.",
        "19. Use /who/ and /whom/ correctly: /Who/ is the subject, /whom/ is the object.",
        "20. Avoid sentence fragments: Every sentence needs a subject and a verb.",
        "21. Learn the difference between /affect/ and /effect/: /Affect/ is a verb, /effect/ is a noun.",
        "22. Use /its/ and /it’s/ correctly: /Its/ shows possession, /it’s/ means /it is/.",
        "23. Practice proper capitalization: Capitalize the first word of a sentence, proper nouns, etc.",
        "24. Use /to,/ /too,/ and /two/ correctly: /To/ is a preposition, /too/ means /also,/ /two/ is a number.",
        "25. Understand the difference between /then/ and /than/: /Then/ relates to time, /than/ is used for comparisons.",
        "26. Avoid double negatives: Instead of /I don’t have no money,/ say /I don’t have any money./",
        "27. Use /complement/ and /compliment/ correctly: /Complement/ means to complete, /compliment/ means to praise."
        "28. Know when to use /which/ and /that/: /Which/ introduces non-essential clauses, /that/ introduces essential clauses.",
        "29. Use /who’s/ and /whose/ correctly: /Who’s/ is /who is,/ /whose/ shows possession.",
        "30. Avoid wordiness: Keep your writing tight and focused.",
        "31. Use /good/ and /well/ correctly: /Good/ is an adjective, /well/ is an adverb.",
        "32. Understand the difference between /may/ and /might/: /May/ is more likely, /might/ is less certain.",
        "33. Avoid cliches: Use fresh, original language.",
        "34. Use /I/ and /me/ correctly: /I/ is the subject, /me/ is the object.",
        "35. Know when to use /further/ and /farther/: /Further/ refers to metaphorical distance, /farthe/ to physical distance.",
        "36. Use /who/ and /that/ correctly: /Who/ for people, /that/ for things.",
        "37. Learn the difference between /bring/ and /take/: /Bring/ is toward the speaker, /take/ is away.",
        "38. Use /whether/ and /if/ correctly: /Whether/ introduces alternatives, /if/ introduces conditions.",
        "39. Understand the difference between /lay/ and /lie/: /Lay/ requires an object, /lie/ does not.",
        "40. Use /that/ and /which/ correctly: /That/ is used for defining clauses, /which/ for non-defining.",
        "41. Avoid passive voice: Prefer active voice for stronger writing.",
        "42. Use /whoever/ and /whomever/ correctly: /Whoever/ is the subject, /whomever/ is the object.",
        "43. Know the difference between /imply/ and /infer/: /Imply/ is to suggest, /infer/ is to deduce.",
        "44. Use /each/ and /every/ correctly: /Each/ refers to individuals, /every/ to the group as a whole.",
        "45. Avoid misplaced modifiers: Place descriptive words close to what they describe.",
        "45. Learn the difference between /between/ and /among/: /Between/ is for two items, /among/ is for three or more.",
        "47. Use /a/ and /an/ correctly: /A/ before consonant sounds, /an/ before vowel sounds.",
        "48. Understand the difference between /principle/ and /principal/: /Principle/ is a rule, /principal/ is a person or main idea.",
        "49. Use /since/ and /because/ correctly: /Since/ relates to time, /because/ to reason.",
        "50. Avoid overusing /very/ and /really/: Find stronger words instead.",
        "51. Use /who/ and /that/ correctly: /Who/ for people, /that/ for things.",
        "52. Know the difference between /stationary/ and /stationery/: /Stationary/ means not moving, /stationery/ is writing paper.",
        "53. Use /your/ and /you’re/ correctly: /Your/ shows possession, /you’re/ is /you are/.",
        "54. Learn the difference between /farther/ and /further/: /Farther/ for physical distance, /further/ for metaphorical.",
        "55. Use /past/ and /passed/ correctly: /Past/ refers to time, /passed/ is the past tense of /pass/.",
        "56. Understand the difference between /desert/ and /dessert/: /Desert/ is a dry place, /dessert/ is a sweet treat.",
        "57. Avoid dangling participles: Ensure your introductory phrases clearly relate to the subject.",
        "58. Use /affect/ and /effec/ correctly: /Affect/ is usually a verb, /effect/ is usually a noun.",
        "59. Know the difference between /quiet/ and /quite/: /Quiet/ means silent, /quite/ means fairly or very.",
        "60. Master the use of /used to/: For habitual actions in the past that no longer occur.",
        "61. Use /must/ and /have to/ correctly: Both indicate obligation, but /must/ is stronger.",
        "62. Learn the difference between /no/ and /not/: /No/ is for absolute negations, /not/ for verb negations.",
        "63. Master the use of /will/ and /going to/: /Will/ for immediate decisions, /going to/ for plans.",
        "64. Know the difference between /by/ and /until/: /By/ is for a deadline, /until/ is for the duration up to a point.",
        "65. Use /whose/ and /who’s/ correctly: /Whose/ indicates possession, /who’s/ is the contraction of /who is/.",
        "66. Learn to use /there,/ /their,/ and /they’re/ correctly: /There/ indicates place, /their/ indicates possession, and /they’re/ is /they are/.",
        "67. Master the use of /rather/ and /prefer/: Both express preferences, but /rather/ often follows /than/.",
        "68. Use /say/ and /tell/ correctly: /Say/ is used without a direct object, and /tell/ with a direct object.",
        "69. Know the difference between /begin/ and /start/: /Begin/ is more formal than /start,/ though often interchangeable.",
        "70. Learn the difference between /lose/ and /loose/: /lose/ means to misplace, /loose/ means not tight.",
        "71. Use /give/ and /take/ correctly: /Give/ is to provide, and /take/ is to receive.",
        "72. Master the use of infinitives and gerunds: Some verbs are followed by an infinitive (to go) and others by a gerund (going).",
        "73. Know the difference between /lay/ and /lie/: /Lay/ is to place something, and /lie/ is to recline.",
        "74. Use /bring/ and /take/ correctly: /Bring/ to move something closer to the speaker, and /take/ to move it away.",
        "75. Learn the difference between /accept/ and /except/: /Accept/ means to receive, and /except/ means to exclude.",
        "76. Master the use of /while/ and /during/: /While/ is used with a verb, and /during/ with a noun.",
        "77. Know the difference between /advice/ and /advise/: /Advice/ is a noun, and /advise/ is a verb.",
        "78. Use /can/ and /may/ correctly: /Can/ indicates ability, and /may/ indicates permission.",
        "79. Learn the difference between /borrow/ and /lend/: /Borrow/ is to take and return, and /lend/ is to give for temporary use.",
        "80. Master the use of /would/ and /used to/: /Would/ is for past habits, and /used to/ for past states.",
        "81. Use /due to/ and /because of/ correctly: /Due to/ is for nouns, and /because of/ is for verbs.",
        "83. Learn the difference between /either/ and /neither/: /Either/ means one or the other, and /neither/ means none.",
        "84. Master the use of /between/ and /among/: /Between/ is for two items, and /among/ is for three or more.",
        "85. Know the difference between /despite/ and /in spite of/: Both mean the same but are used differently in a sentence.",
        "86. Use /farther/ and /further/ correctly: /Farther/ is for physical distance, and /further/ for metaphorical.",
        "87. Learn the difference between /in/ and /into/: /In/ indicates location, and /into/ indicates movement.",
        "88. Master the use of /who/ and /whom/: /Who is the subject, and /whom/ is the object.",
        "89. Use /affect/ and /effect/ correctly: /Affect/ is typically a verb, and /effect/ a noun.",
        "90. Know the difference between /everyday/ and /every day/: /Everyday/ is an adjective meaning ordinary, and /every day/ means each day.",
        "91. Learn the difference between /by/ and /with/: /By/ indicates the agent, and /with/ indicates the instrument.",
        "92. Master the use of /good/ and /well/: /Good/ is an adjective, and /well/ is an adverb.",
        "93. Use /beside/ and /besides/ correctly: /Beside/ means next to, and /besides/ means in addition to.",
        "94. Learn the difference between /raise/ and /rise/: /Raise/ requires an object, and /rise/ does not.",
        "95. Master the use of /bring/ and /take/: /Bring/ is to move something towards the speaker, and /take/ away.",
        "96. Use /its/ and /it’s/ correctly: /Its/ shows possession, and /it’s/ is /it is/.",
        "97. Know the difference between /stationary/ and /stationery/: /Stationary/ means not moving, and /stationery/ means writing paper.",
        "98. Learn the difference between /lose/ and /loose/: /Lose/ means to misplace, and /loose/ means not tight.",
        "99. Master the use of /between/ and /among/: /Between/ for two, and /among/ for more.",
        "99. Use /who’s/ and /whose/ correctly: /Who’s/ is /who is,/ and /whose/ shows possession.",
        "100. Learn the difference between /there,/ /their,/ and /they’re/: /There/ refers to a place, /their/ shows possession, and /they’re/ is /they are/.",
        "101. Ensure the text flows naturally from one idea to another.",
        "100. Review and edit the text.",
    ]

    if idioma == 'es':
        return consejos_es
    elif idioma == 'en':
        return consejos_en
    else:
        return []

def menu():
    print("Menu:")
    print("1. Escribir y repetir los consejos en español")
    print("2. Write and repeat the tips in English")
    print("3. Salir / Exit")

def escribir_consejos(consejos):
    for consejo in consejos:
        print("\nConsejo:")
        print(consejo)
        input_text = input("Escribe el consejo exactamente como aparece:\n")
        if input_text == consejo:
            print("¡Correcto!")
        else:
            print(f"Incorrecto. El consejo correcto es:\n{consejo}")

def main():
    while True:
        menu()
        opcion = input("Seleccione una opción (1, 2, 3): ")

        if opcion == '1':
            consejos = mostrar_consejos('es')
            escribir_consejos(consejos)
        elif opcion == '2':
            consejos = mostrar_consejos('en')
            escribir_consejos(consejos)
        elif opcion == '3':
            print("Gracias por usar el programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione 1, 2 o 3.")

if __name__ == "__main__":
    main()
