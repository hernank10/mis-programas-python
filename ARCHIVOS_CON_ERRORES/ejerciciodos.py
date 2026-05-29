def mostrar_consejos(idioma):
    consejos_es = [
        "1. Usa oraciones simples.",
        "2. Evita el uso excesivo de la voz pasiva.",
        "3. Revisa y edita el texto.",
            "4. Acentuación: Familiarízate con las palabras agudas, llanas y esdrújulas.",
            "5. Signos de puntuación: Coloca correctamente puntos, comas y otros signos.",
        "1. Aprende las reglas básicas de la gramática inglesa: Familiarízate con los tiempos verbales, la estructura de las oraciones, y el uso correcto de los pronombres.", 
        "2. Usa el verbo /to be/ correctamente: Es uno de los verbos más importantes y tiene muchas funciones en inglés. ",
        "3. Domina el uso de los artículos: /A,/ /an,/ y /the/ son esenciales en inglés, y su uso correcto es clave. ",
        "4. Conoce la diferencia entre los tiempos verbales: Aprende cuándo usar el presente simple, el pasado simple, el presente perfecto, y otros tiempos. ",
        "5. Evita traducir literalmente: El inglés y el español tienen estructuras diferentes, y la traducción literal puede llevar a errores. ",
        "6. Aprende las preposiciones comunes: /In,/ /on,/ /at,/ y /for/ son algunas de las preposiciones más comunes en inglés. ",
        "7. Usa los modales correctamente: /Can,/ /could,/ /may,/ /might,/ /must,/ etc., son esenciales para expresar permisos, obligaciones y posibilidades. ",
        "8. Domina el uso de las contracciones: /Can't,/ /won't,/ /I'm,/ /you're/ son comunes en el habla y la escritura informal. ",
        "9. Conoce la diferencia entre /who/ y /whom/: /Who/ se usa para el sujeto, y /whom/ para el objeto en una oración. ",
        "10. Usa correctamente los adjetivos y adverbios: Recuerda que los adjetivos modifican sustantivos y los adverbios modifican verbos, adjetivos o adverbios. ",
        "11. Practica el orden de las palabras en las oraciones: El inglés tiene un orden de palabras más rígido que el español, generalmente sujeto-verbo-objeto. ",
        "12. Evita el uso excesivo de /very/: Busca sinónimos más específicos como /extremely,/ /incredibly,/ /terribly." ,
        "13. Usa correctamente los pronombres reflexivos: /Myself,/ /yourself,/ /himself,/ etc., se usan para acciones que recaen sobre el sujeto. ",
        "14. Domina los falsos amigos: Palabras que se parecen en inglés y español pero tienen significados diferentes, como /actual/ /real/ y /actual/ current. ",
        "15. Aprende la diferencia entre /say/ y /tell/: /Say/ se usa para expresar lo que alguien dijo, mientras que /tell/ se usa para comunicar algo a alguien. ",
        "16. Usa correctamente los tiempos perfectos: El presente perfecto (/I have eaten/) se usa para acciones que tienen relevancia en el presente. ",
        "17. Domina el uso de las preposiciones de tiempo: /In,/ /on,/ y /at/ se usan en diferentes contextos de tiempo. ",
        "18. Usa correctamente /much/ y /many/: /Much/ se usa con incontables, y /many/ con contables. ",
        "19. Conoce la diferencia entre /few/ y /a few/: /Few/ indica una cantidad insuficiente, y /a few/ indica una cantidad suficiente pero pequeña. ",
        "20. Domina las preguntas indirectas: Cambia el orden de palabras y elimina el auxiliar para formar preguntas indirectas.", 
        "21. Aprende las frases verbales (phrasal verbs): Son comunes en inglés y pueden cambiar completamente el significado de un verbo. ",
        "22. Conoce la diferencia entre /to/ y /too/: /To/ es una preposición, mientras que /too/ significa /también/ o /demasiado. ",
        "23. Usa correctamente /make/ y /do/: /Make/ se refiere a crear o producir algo, y /do/ se refiere a realizar una acción o tarea. ",
        "24. Domina el uso de /there/ is/ y /there are/: Se usan para indicar la existencia de algo, dependiendo si es singular o plural. ",
        "25. Aprende la diferencia entre /advice/ y /advise/: /Advice/ es un sustantivo, y /advise/ es un verbo. ",
        "26. Evita el uso excesivo de pronombres personales: En inglés es común omitir el sujeto cuando se sobreentiende en la oración. ",
        "27. Conoce la diferencia entre /who's/ y /whose/: /Who's/ es la contracción de /who is,/ y /whose/ indica posesión. ",
        "28. Usa correctamente /since/ y /for/: /Since/ indica el inicio de un período de tiempo, y /for/ indica la duración. ",
        "29. Domina el uso de /either/ y /neither/: /Either/ se usa para cualquiera de dos opciones, y /neither/ para negar ambas. ",
        "30. Aprende la diferencia entre /hear/ y /listen/: /Hear/ es involuntario, y /listen/ es una acción intencional. ",
        "31. Usa correctamente /borrow/ y /lend/: /Borrow/ significa tomar prestado, y /lend/ significa prestar. ",
        "32. Domina el uso de /who/ y /which/: /Who/se usa para personas, y /which/ para cosas o animales. ",
        "33. Aprende la diferencia entre /good/ y /well/: /Good/ es un adjetivo, y /well/ es un adverbio. ",
        "34. Usa correctamente /bring/ y /take/: /Bring/ implica llevar algo hacia un lugar, y /take/ implica llevar algo desde un lugar. ",
        "35. Domina el uso de /affect/ y /effect/: /Affect/ es un verbo, y /effect/ es un sustantivo. ",
        "36. Conoce la diferencia entre /lie/ y /lay/: /Lie/ significa recostarse, y /lay/ significa colocar algo en un lugar. ",
        "37. Usa correctamente /between/ y /among/: /Between/ se usa para dos elementos, y /among/ para más de dos. ",
        "38. Domina las expresiones de cantidad: /A lot of,/ /plenty of,/ /a few,/ /some,/ y cómo usarlas correctamente. ",
        "39. Aprende la diferencia entre /farther/ y /further/: /Farther/ se refiere a distancia física, y /further/ a distancia metafórica o adicional.", 
        "40. Usa correctamente /less/ y /fewer/: /Less/ se usa con incontables, y /fewer/ con contables. ",
        "41. Domina las oraciones condicionales: /If/ se usa para expresar condiciones en diferentes tiempos. ",
        "42. Conoce la diferencia entre /practice/ y /practise/: En inglés británico, /practice/ es un sustantivo y /practise/ es un verbo. ",
        "43. Aprende a usar correctamente los gerundios: Muchos verbos en inglés requieren el gerundio (/-ing/) después de ellos. ",
        "44. Evita la confusión entre /then/ y /than/: /Then/ indica tiempo, y /than/ se usa para comparaciones. ",
        "45. Usa correctamente /fewer/ y /less/: /Fewer/ se usa con sustantivos contables, y /less/ con incontables. ",
        "46. Domina el uso del verbo /to get/: Tiene muchos significados según el contexto (/obtain,/ /become,/ /arrive,/ etc.). ",
        "47. Conoce la diferencia entre /rise/ y /raise/: /Rise/ es intransitivo, y /raise/ es transitivo. ",
        "48. Usa correctamente /since/ y /because/: /Since/ puede indicar tiempo o causa, mientras que /because/ solo indica causa. ",
        "49. Domina el uso de las preguntas de sí/no: /Do you like...?/ /Have you been...?/ /Are you going...?" ,
        "50. Aprende la diferencia entre /each/ y /every/: /Each/ se refiere a individuos en un grupo, y /every/ se refiere a todos en un grupo. ",
        "51. Conoce la diferencia entre /any/ y /some/: /Some/ se usa en afirmaciones y /any/ en preguntas y negaciones. ",
        "52. Domina las estructuras negativas: /Don't,/ /isn't,/ /can't,/ /won't,/ etc. ",
        "53. Usa correctamente /in/ y /into/: /In/ indica dentro de algo, y /into/ indica movimiento hacia dentro. ",
        "54. Aprende la diferencia entre /other/ y /another/: /Another/ se usa con singular, y /other/ con plural o singular. ",
        "55. Conoce la diferencia entre /to/ y /for/: /To/ se usa para destino o propósito, y /for/ para beneficio o duración. ",
            "61. Mantén el mismo punto de vista a lo largo del texto.",
            "62. Evita el uso de palabras demasiado técnicas sin explicación.",
            "63. Utiliza un lenguaje formal en documentos académicos y profesionales.",
            "64. Usa la voz pasiva solo cuando sea necesario.",
            "65. Revisa la concordancia entre sustantivos y adjetivos.",
            "66. Asegúrate de que el pronombre se refiera claramente a su antecedente.",
            "67. Usa los adverbios con moderación.",
            "68. Mantén la coherencia en la estructura de las listas.",
            "69. Revisa la consistencia en el uso de tiempos verbales.",
            "70. Evita el uso de palabras rebuscadas o arcaicas.",
            "71. Usa las citas indirectas para parafrasear ideas de otros.",
            "72. Evita las palabras de relleno.",
            "73. Utiliza la negrita para destacar información clave.",
            "74. Usa el subrayado con moderación.",
            "75. No olvides incluir referencias y bibliografía en textos académicos.",
            "76. Asegúrate de que las imágenes y tablas estén bien etiquetadas.",
            "77. Revisa la correcta numeración de páginas y secciones.",
            "78. Evita las oraciones incompletas.",
            "79. Usa las notas al pie de página para aclaraciones importantes.",
            "80. Evita las generalizaciones excesivas.",
            "81. Revisa la coherencia en el uso de comillas simples y dobles.",
            "82. Asegúrate de que las citas textuales estén correctamente formateadas.",
            "83. Usa el paréntesis para incluir información adicional sin interrumpir el flujo del texto.",
            "84. Evita el uso de pronombres ambiguos.",
            "85. Mantén la coherencia en la estructura gramatical de las oraciones.",
            "86. Usa la cursiva para enfatizar palabras o títulos de obras.",
            "87. Revisa la consistencia en el uso de abreviaturas.",
            "88. Evita el uso de verbos débiles como hacer o tener.",
            "89. Usa la segunda persona solo en textos de tono informal.",
            "90. Revisa la coherencia en la numeración de ejemplos y figuras.",
            "91. Evita el uso excesivo de metáforas.",
            "92. Usa el estilo directo en lugar del indirecto cuando sea posible.",
            "93. Asegúrate de que las ideas principales estén claramente resaltadas.",
            "94. Revisa la coherencia en la numeración de capítulos y secciones.",
            "95. Evita las digresiones innecesarias",
            "96. Usa los puntos suspensivos con moderación.",
            "97. Asegúrate de que el título del texto sea claro y conciso.",
            "98. Evita el uso excesivo de oraciones interrogativas en textos formales.",
            "99. Revisa la consistencia en el uso de mayúsculas y minúsculas.",
            "100. Evita el uso de palabras o frases redundantes.",
            "101. Usa un lenguaje preciso y específico.",
            "102. Revisa la coherencia en el uso de los títulos y subtítulos.",
            "103. Asegúrate de que el texto fluya naturalmente de una idea a otra.",

    ]
    
    consejos_en = [
        "1. Use simple sentences.",
        "2. Avoid overusing the passive voice.",
        "3. Accentuation: Familiarize yourself with acute, grave, and proparoxytone words.",
            "4. Punctuation marks: Place periods, commas, and other punctuation marks correctly.",
            "5. Spelling rules: Understand when to use 'b' or 'v', 'c', 'k' or 'q', 'g' or 'j', 'll' or 'y'.",
            "6. Rhetorical figures: Explore stylistic resources to enrich your texts.",
            "7. Avoid unnecessary repetition of words.",
            "8. Use connectors to link ideas.",
            "9. Write paragraphs with a single main idea.",
            "10. Use punctuation correctly.",
            "11. Avoid overly long sentences.",
            "12. Check spelling and grammar.",
            "13. Avoid unnecessary technical jargon.",
            "14. Write in a tone appropriate for your audience.",
            "15. Use examples to clarify complex points.",
            "16. Maintain consistency in verb tense.",
            "17. Use synonyms to avoid repetition.",
            "18. Avoid overusing adjectives and adverbs.",
            "19. Ensure each sentence adds something new.",
            "20. Eliminate unnecessary words.",
            "21. Use the active voice whenever possible.",
            "22. Review your text for ambiguities.",
            "23. Do not mix different writing styles.",
            "24. Use direct quotes only when necessary.",
            "25. Avoid clichés and set phrases.",
            "26. Maintain a logical structure in the development of ideas.",
            "27. Check consistency in the terminology used.",
            "28. Use smooth transitions between paragraphs.",
            "29. Avoid overusing quotation marks.",
            "30. Use quotation marks to emphasize key words or phrases.",
            "31. Do not overuse exclamation marks.",
            "32. Write in a positive form instead of a negative one.",
            "33. Divide complex sentences into two or more simple sentences.",
            "34. Avoid using redundant words.",
            "35. Write with precision and accuracy.",
            "36. Ensure that the subject and verb agree in number.",
            "37. Use inclusive and non-sexist language.",
            "38. Review the coherence of metaphors and similes.",
            "39. Avoid double negatives.",
            "40. Use the subjunctive correctly in hypothetical situations.",
            "41. Avoid vagueness and ambiguity.",
            "42. Be consistent in the use of capital letters.",
            "43. Use punctuation to guide the reader.",
            "44. Review the use of prepositions.",
            "45. Avoid abrupt changes in topic.",
            "46. Ensure quotes are properly attributed.",
            "47. Use a consistent style throughout the text.",
            "48. Do not repeat the same idea in different words.",
            "49. Avoid idioms and colloquial expressions in formal texts.",
            "50. Use the first person only when appropriate.",
            "51. Maintain objectivity in academic writing.",
            "52. Check consistency in the use of citations and references.",
            "53. Use numbered lists to enumerate points.",
            "54. Use bullet points to highlight important points.",
            "55. Write a good title that reflects the content of the text.",
            "56. Review the structure of subordinate sentences.",
            "57. Avoid using long and complex phrases unnecessarily.",
            "58. Ensure each paragraph has a clear central idea.",
            "59. Avoid overusing acronyms and abbreviations.",
            "60. Maintain the same point of view throughout the text.",
            "61. Avoid using overly technical words without explanation.",
            "62. Use formal language in academic and professional documents.",
            "63. Use the passive voice only when necessary.",
            "64. Review the agreement between nouns and adjectives.",
            "65. Ensure that the pronoun clearly refers to its antecedent.",
            "66. Use adverbs sparingly.",
            "67. Maintain consistency in the structure of lists.",
            "68. Check consistency in the use of verb tenses.",
            "69. Avoid using convoluted or archaic words.",
            "70. Use indirect quotes to paraphrase others' ideas.",
            "71. Avoid filler words.",
            "72. Use bold to highlight key information.",
            "73. Use underlining sparingly.",
            "74. Do not forget to include references and bibliography in academic texts.",
            "75. Ensure images and tables are well-labeled.",
            "76. Check the correct numbering of pages and sections.",
            "77. Use footnotes for important clarifications.",
            "78. Avoid excessive generalizations.",
            "79. Check consistency in the use of single and double quotation marks.",
            "80. Ensure direct quotes are properly formatted.",
            "81. Use parentheses to include additional information without interrupting the text's flow.",
            "82. Avoid ambiguous pronouns.",
            "83. Maintain consistency in the grammatical structure of sentences.",
            "84. Use italics to emphasize words or titles of works.",
            "85. Check consistency in the use of abbreviations.",
            "86. Avoid using weak verbs like do or have.",
            "87. Use the second person only in informal texts.",
            "88. Check consistency in the numbering of examples and figures.",
            "89. Avoid overusing metaphors.",
            "90. Use direct style instead of indirect style when possible.",
            "91. Ensure the main ideas are clearly highlighted.",
            "92. Check consistency in the numbering of chapters and sections.",
            "93. Avoid unnecessary digressions.",
            "94. Use ellipses sparingly.",
            "95. Ensure the title of the text is clear and concise.",
            "96. Avoid overusing interrogative sentences in formal texts.",
            "97. Check consistency in the use of upper and lower case.",
            "98. Avoid using redundant words or phrases.",
            "99. Use precise and specific language.",
            "100. Check consistency in the use of titles and subtitles.",
            "101. Ensure the text flows naturally from one idea to another.",
# Continúa con los demás consejos en inglés...
        "100. Review and edit the text."
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
