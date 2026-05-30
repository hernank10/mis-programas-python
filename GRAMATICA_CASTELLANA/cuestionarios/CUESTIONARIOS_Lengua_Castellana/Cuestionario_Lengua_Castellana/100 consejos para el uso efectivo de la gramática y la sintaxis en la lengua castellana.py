def mostrar_consejos(idioma):
    consejos_es = [
        "1.Comprende las reglas básicas de acentuación: Conoce las reglas para las palabras agudas, llanas y esdrújulas.",
        "2.Usa correctamente el punto y coma: Empléalo para separar ideas que están relacionadas pero no son completamente independientes.",
        "3.Evita el dequeísmo: No uses (de que) cuando no es necesario. Por ejemplo, en vez de (pienso de que), usa (pienso que).",
        "4.Domina el uso de las tildes diacríticas: Diferencia palabras como té (bebida) de te (pronombre).",
        "5.Utiliza adecuadamente las comas: Coloca comas para separar elementos en una lista, antes de conjunciones adversativas como (pero), y en oraciones subordinadas.",
        "6.No abuses de las comas: Evita las comas innecesarias que pueden interrumpir la fluidez de la oración.",
        "7.Conoce los tiempos verbales: Domina el uso del presente, pretérito, futuro, condicional, y subjuntivo.",
        "8.Usa correctamente los pronombres: Asegúrate de usar el pronombre adecuado según el género y número.",
        "9.Evita el laísmo y leísmo: Utiliza /le/ para el complemento indirecto /a una persona/ y /lo/la/ para el complemento directo.",
        "10. Aprende a usar correctamente las preposiciones: Cada preposición tiene un uso específico que debe respetarse.",
        "11. No confíes demasiado en los correctores automáticos: Revísalo siempre, pues pueden cometer errores.",
        "12. Evita la redundancia: No repitas palabras o ideas innecesariamente.",
        "13. Usa correctamente el /que/ y /cual/: Diferencia su uso en frases relativas."
        "14. Comprende las oraciones subordinadas: Aprende a construir oraciones complejas usando conjunciones subordinadas.",
        "15. Usa el gerundio correctamente: No lo utilices como adjetivo y evita /gerundios de posterioridad/.",
        "16. Emplea adecuadamente los conectores: Usa conectores para enlazar ideas y mejorar la cohesión del texto.",
        "17. Diferencia entre /porque/ y /por qué/: Usa /porque/ para explicar y /por qué/ para preguntar.",
        "18. Practica el uso de los artículos: Asegúrate de que coincidan en género y número con el sustantivo.",
        "19. Usa adecuadamente las conjunciones: Diferencia entre conjunciones coordinantes y subordinantes.",
        "20. Aprende a usar la voz pasiva: Conviértela a voz activa para hacer oraciones más directas.",
        "21. Evita el uso excesivo de adjetivos: Sé conciso y preciso en su uso.",
        "22. Usa los adverbios con moderación: No sobrecargues tus frases con demasiados adverbios.",
        "23. Diferencia entre /haber/ y /a ver/: /Haber/ es un verbo auxiliar y /a ver/ una locución.",
        "24. Conoce las diferencias entre homófonos: Como /baca/ y /vaca/.",
        "25. Usa correctamente las oraciones interrogativas: Asegúrate de usar la estructura adecuada para hacer preguntas."
        "26. Comprende el uso de la raya y el guion: Usa la raya para diálogos y el guion para unir palabras compuestas.",
        "27. Domina la concordancia: Asegúrate de que el sujeto y el verbo concuerden en número y persona.",
        "28. Evita los pleonasmos: No uses expresiones redundantes como /subir para arriba/.",
        "29. Comprende el uso del subjuntivo: Es fundamental para expresar deseos, dudas o hipótesis.",
        "30. Usa correctamente los paréntesis: Para insertar información adicional sin romper la estructura de la oración.",
        "31. Evita las oraciones demasiado largas: Divide ideas complejas en varias oraciones más cortas.",
        "32. Usa los puntos suspensivos con moderación: Úsalos para indicar una pausa significativa o una omisión, pero no abuses de ellos.",
        "33. Diferencia entre /hay/, /ahí/ y /ay/: /Hay/ indica existencia, /ahí/ lugar, y /ay/ es una exclamación.",
        "34. Evita los vulgarismos: Usa un lenguaje adecuado y formal en contextos profesionales o académicos.",
        "35. Practica el uso del condicional: Es útil para expresar posibilidades y condiciones.",
        "36. Evita las muletillas: Palabras o expresiones innecesarias que interrumpen la fluidez del discurso.",
        "37. Domina la acentuación en los hiatos: Identifica cuándo dos vocales fuertes necesitan una tilde.",
        "38. Usa correctamente el pronombre /se/: Conoce sus usos como reflexivo, impersonal y pasivo.",
        "39. Evita las oraciones impersonales excesivas: A veces es mejor usar un sujeto explícito."
        "40. Comprende el uso de los demostrativos: /Este/, /ese/, /aquel/, y sus variantes.",
        "41. Usa la concordancia entre adjetivos y sustantivos: En género y número.",
        "42. Evita las cacofonías: Repeticiones de sonidos que pueden hacer la lectura incómoda.",
        "43. Conoce el uso correcto de los pronombres relativos: /Que/, /quien/, /cual/, etc.",
        "44. Practica la elisión de palabras: A veces es mejor omitir palabras que se sobreentienden.",
        "45. Usa correctamente el verbo /haber/: En oraciones impersonales y como verbo auxiliar.",
        "46. Evita el abuso de la primera persona: Diversifica los sujetos en tu discurso.",
        "47. Domina el uso de los puntos y comas en listas: Usa comas para separar elementos y punto y coma para separar sublistas.",
        "48. Conoce las formas irregulares de los verbos: Como /andar/, /caber/, /dar/, etc.",
        "49. Evita el abuso de los adjetivos calificativos: Sé preciso en la descripción.",
        "50. Usa correctamente el modo imperativo: Para dar órdenes o instrucciones claras.",
        "51. Practica el uso del pretérito perfecto: Es útil para expresar acciones pasadas relacionadas con el presente.",
        "52. Comprende el uso de las oraciones yuxtapuestas: Cuando dos oraciones están relacionadas pero no unidas por un nexo.",
        "53. Domina la acentuación en diptongos y triptongos: Diferencia entre acentos ortográficos y prosódicos.",
        "54. Usa correctamente las comillas: Para citar palabras o frases textuales.",
        "55. Evita la ambigüedad: Sé claro y preciso en tus expresiones para evitar confusiones.",
        "56. Usa los pronombres átonos correctamente: Como /me/, /te/, /se/, /nos/, /os/.",
        "57. Practica el uso de las oraciones exclamativas: Para expresar emociones fuertes.",
        "58. Conoce las diferencias entre /tú/ y /tu/: /Tú/ es pronombre personal y /tu/ es un adjetivo posesivo.",
        "59. Evita las expresiones coloquiales en textos formales: Sé consciente del registro que utilizas.",
        "60. Domina el uso de las conjunciones copulativas: /Y/, /e/, /ni/.",
        "61. Usa correctamente el verbo /ser/ y /estar/: Diferencia entre situaciones permanentes y temporales.",
        "62. Evita el abuso de los adverbios terminados en -mente: No satures el texto con ellos.",
        "63. Practica el uso del pretérito imperfecto: Es útil para describir acciones pasadas en desarrollo.",
        "64. Comprende el uso del gerundio compuesto: Para expresar acciones anteriores a la acción principal.",
        "65. Usa correctamente los verbos pronominales: Como /acordarse/, /arrepentirse/.",
        "66. Evita las repeticiones innecesarias: Varía el vocabulario para evitar monotonía.",
        "67. Domina el uso del condicional compuesto: Para expresar acciones que habrían ocurrido bajo ciertas condiciones.",
        "68. Usa correctamente las oraciones subordinadas adverbiales: Como las causales, temporales, concesivas, etc.",
        "69. Practica el uso del futuro simple y compuesto: Para expresar acciones futuras o probabilidad.",
        "70. Conoce las reglas de uso del artículo neutro /lo/: Cuando se refiere a cualidades o características.",
        "71. Evita los barbarismos: Palabras extranjeras o incorrectas en lugar de términos castellanos.",
        "72. Domina el uso de los sufijos y prefijos: Para formar palabras correctamente.",
        "73. Usa correctamente las oraciones condicionales: Con /si/ y sus variantes.",
        "74. Practica el uso de los apócopes: Como /gran/ en lugar de /grande/ ante sustantivos singulares masculinos.",
        "75. Comprende el uso del participio irregular: Como /impreso/, /abierto/, /dicho/.",
        "76. Evita las frases hechas y clichés: Aporta originalidad y frescura a tu texto.",
        "77. Usa correctamente el verbo /ir/ y sus conjugaciones: Evita confusiones con otros verbos.",
        "78. Domina el uso del modo subjuntivo: Especialmente en oraciones subordinadas.",
        "79. Practica el uso de las oraciones impersonales: Con verbos como /hacer/, /ser/, /haber/.",
        "80. Conoce las diferencias entre /de/ y /dé/: /Dé/ es una forma del verbo /dar/.",
        "81. Evita los extranjerismos innecesarios: Usa términos en español siempre que sea posible.",
        "82. Domina el uso de los participios pasivos y activos: Como /cantado/ o /activo/.",
        "83. Usa correctamente los adjetivos determinativos: Como /este/, /ese/, /aquel/.",
        "84. Practica el uso de los conectores lógicos: Como /por tanto/, /sin embargo/, /en consecuencia/.",
        "85. Comprende el uso del presente de indicativo: Es el tiempo verbal más común y versátil.",
        "86. Usa correctamente los adjetivos numerales: Como /primero/, /segundo/, /tercero/.",
        "87. Evita los vulgarismos y expresiones malsonantes: Especialmente en contextos formales.",
        "88. Domina el uso del verbo /tener/: Y sus conjugaciones en diferentes tiempos.",
        "89. Practica el uso de las perífrasis verbales: Como /ir a + infinitivo/, /tener que + infinitivo/.",
        "90. Conoce las reglas de concordancia en oraciones subordinadas: Para mantener la coherencia.",
        "93. Domina el uso de las oraciones adversativas: Con /pero/,/aunque/, /sin embargo/.",
        "94. Usa correctamente los posesivos: /Mi/, /tu/, /su/, /nuestro/, /vuestro/.",
        "95. Practica el uso de las oraciones copulativas: Con verbos como /ser/, /estar/, /parecer/.",
        "96. Conoce las diferencias entre /más/ y /mas/: /Más/ es una palabra de cantidad y /mas/ una conjunción.",
        "97. Evita la ambigüedad en los pronombres: Asegúrate de que el referente esté claro.",
        "98. Usa correctamente el verbo /deber/: Diferencia entre /deber/ y /deber de/.",
        "99. Practica el uso del estilo directo e indirecto: Para relatar diálogos y pensamientos.",
        "100. Conoce las diferencias entre /este/, /éste/ y /esté/: /Éste/ ya no lleva tilde según la RAE, pero /esté/ es un verbo en subjuntivo.",
        "101. Usa un lenguaje preciso y específico.",
        "102. Revisa la coherencia en el uso de los títulos y subtítulos.",
        "103. Asegúrate de que el texto fluya naturalmente de una idea a otra.",
    ]
    consejos_en = [
        "1. Use simple sentences.",
        "2. Avoid overusing the passive voice.",
        "1. Understand basic accentuation rules: Know the rules for stressed, unstressed, and esdrújula (proparoxytone) words.",
        "2. Use semicolons correctly: Use them to separate ideas that are related but not entirely independent.",
        "3. Avoid /dequeísmo/: Don't use /de que/ when it's unnecessary. For example, instead of /pienso de que/, use /pienso que/.",
        "4. Master the use of diacritical marks: Differentiate words like /té/ (tea) from /te/ (you).",
        "5. Use commas appropriately: Place commas to separate items in a list, before adversative conjunctions like /but,/ and in subordinate clauses.",
        "6. Don't overuse commas: Avoid unnecessary commas that can interrupt the flow of the sentence.",
        "7. Know verb tenses: Master the use of present, past, future, conditional, and subjunctive tenses.",
        "8. Usa correctamente los pronombres: Asegúrate de usar el pronombre adecuado según el género y número.",
        "9. Avoid /laísmo/ and /leísmo/: Use /le/ for indirect objects (for a person) and /lo/la/ for direct objects.",
        "10. Learn to use prepositions correctly: Each preposition has a specific use that must be respected.",
        "11. Don't rely too much on spell checkers: Always review, as they can make mistakes.",
        "12. Avoid redundancy: Don't repeat words or ideas unnecessarily.",
        "13. Use /que/ and /cual/ correctly: Differentiate their use in relative clauses.",
        "14. Understand subordinate clauses: Learn to construct complex sentences using subordinating conjunctions.",
        "15. Use the gerund correctly: Don't use it as an adjective and avoid /gerunds of posteriority.",
        "16. Use connectors properly: Use connectors to link ideas and improve the cohesion of the text.",
        "17. Differentiate between /porque/ and /por qué/: Use /porque/ to explain and /por qué/ to ask.",
        "18. Practice the use of articles: Ensure they match in gender and number with the noun.",
        "19. Use conjunctions correctly: Differentiate between coordinating and subordinating conjunctions.",
        "20. Learn to use passive voice: Convert it to active voice to make sentences more direct.",
        "21. Avoid excessive use of adjectives: Be concise and precise in their use.",
        "22. Use adverbs in moderation: Don't overload your sentences with too many adverbs.",
        "23. Differentiate between /haber/ and /a ver/: /Haber/ is an auxiliary verb, and /a ver/ is a phrase meaning /let's see.",
        "24. Know the differences between homophones: Like /baca/ (roof rack) and /vaca/ (cow).",
        "25. Use interrogative sentences correctly: Ensure you use the proper structure to ask questions.",
        "26. Understand the use of the dash and hyphen: Use the dash for dialogues and the hyphen for compound words.",
        "27. Master subject-verb agreement: Ensure the subject and verb agree in number and person.",
        "28. Avoid pleonasms: Don't use redundant expressions like /upwards/ or /downwards/.",
        "29. Understand the use of the subjunctive: It's essential for expressing wishes, doubts, or hypotheses.",
        "30. Use parentheses appropriately: To insert additional information without breaking the sentence structure.",
        "31. Avoid overly long sentences: Break down complex ideas into several shorter sentences.",
        "32. Use ellipses sparingly: Use them to indicate a significant pause or omission, but don't overuse them.",
        "33. Differentiate between /hay,/ /ahí,/ and /ay/: /Hay/ indicates existence, /ahí/ indicates place, and /ay/ is an exclamation.",
        "34. Avoid vulgarisms: Use appropriate and formal language in professional or academic contexts.",
        "35. Practice the use of the conditional: It is useful for expressing possibilities and conditions.",
        "36. Avoid filler words: Words or phrases that interrupt the flow of speech unnecessarily.",
        "37. Master accentuation in hiatuses: Identify when two strong vowels need an accent.",
        "38. Use the pronoun /se/ correctly: Know its uses as reflexive, impersonal, and passive.",
        "39. Avoid excessive impersonal sentences: Sometimes it's better to use an explicit subject.",
        "40.. Understand the use of demonstratives: /Este,/ /ese,/ /aquel,/ and their variants.",
        "41. Use agreement between adjectives and nouns: In gender and number.",
        "42. Avoid cacophonies: Repetitions of sounds that can make reading uncomfortable.",
        "43. Know the correct use of relative pronouns: /Que,/ /quien,/ /cual,/ etc.",
        "44. Practice word omission: Sometimes it's better to omit words that are understood.",
        "45. Use the verb /haber/ correctly: In impersonal sentences and as an auxiliary verb.",
        "46. Avoid overusing the first person: Diversify the subjects in your speech.",
        "47. Master the use of semicolons in lists: Use commas to separate items and semicolons to separate sublists.",
        "48. Know irregular verb forms: Like /andar,/ /caber,/ /dar,/ etc.",
        "49. Avoid overusing qualifying adjectives: Be precise in description.",
        "50. Use the imperative mood correctly: To give clear orders or instructions.",
        "51. Practice the use of the present perfect: It is useful for expressing past actions related to the present.",
        "52. Understand juxtaposed sentences: When two sentences are related but not connected by a conjunction.",
        "53. Master accentuation in diphthongs and triphthongs: Differentiate between orthographic and prosodic accents.",
        "54. Use quotation marks correctly: To quote words or phrases textually.",
        "55. Avoid ambiguity: Be clear and precise in your expressions to avoid confusion.",
        "56. Use unstressed pronouns correctly: Like /me,/ /te,/ /se,/ /nos,/ /os./",
        "57. Practice the use of exclamatory sentences: To express strong emotions.",
        "58. Know the differences between /tú/ and /tu/: /Tú/ is a personal pronoun, and /tu/ is a possessive adjective.",
        "59. Avoid colloquial expressions in formal texts: Be aware of the register you are using.",
        "60. Master the use of coordinating conjunctions: /Y,/ /e,/ /ni/.",
        "61. Use the verb /ser/ and /estar/ correctly: Differentiate between permanent and temporary situations.",
        "62. Avoid overusing adverbs ending in -mente: Don't saturate the text with them.",
        "63. Practice the use of the imperfect past tense: It is useful for describing ongoing past actions.",
        "64. Understand the use of the compound gerund: To express actions that occurred before the main action.",
        "65. Use pronominal verbs correctly: Like /acordarse,/ /arrepentirse.",
        "66. Avoid unnecessary repetitions: Vary your vocabulary to avoid monotony.",
        "67. Master the use of the compound conditional: To express actions that would have occurred under certain conditions.",
        "68. Use subordinate adverbial clauses correctly: Like causal, temporal, concessive, etc.",
        "69. Practice the use of the simple and compound future: To express future actions or probability.",
        "70. Know the rules for using the neuter article /lo/: When referring to qualities or characteristics.",
        "71. Avoid barbarisms: Foreign or incorrect words instead of Spanish terms.",
        "72. Master the use of suffixes and prefixes: To form words correctly.",
        "73. Use conditional sentences correctly: With /si/ and its variants.",
        "74. Practice the use of apocopes: Like /gran/ instead of /grande/ before singular masculine nouns.",
        "75. Understand the use of irregular participles: Like /impreso,/ /abierto,/ /dicho.",
        "76. Avoid clichés and trite expressions: Add originality and freshness to your text.",
        "77. Use the verb /ir/ and its conjugations correctly: Avoid confusion with other verbs.",
        "78. Master the use of the subjunctive mood: Especially in subordinate clauses.",
        "79. Practice the use of impersonal sentences: With verbs like /hacer,/ /ser,/ /haber.",
        "80. Know the differences between /de/ and /dé/: /Dé/ is a form of the verb /dar.",
        "81. Avoid unnecessary foreign words: Use Spanish terms whenever possible.",
        "82. Master the use of passive and active participles: Like /cantado/ (sung) or /activo/ (active).",
        "83. Use determinative adjectives correctly: Like /this,/ /that,/ /that one.",
        "84. Practice the use of logical connectors: Like /therefore,/ /however,/ /as a result.",
        "85. Understand the use of the present indicative: It is the most common and versatile verb tense.",
        "86. Use numeral adjectives correctly: Like /first," "second," "third.",
        "87. Avoid vulgarisms and offensive expressions: Especially in formal contexts.",
        "88. Master the use of the verb /tener/: And its conjugations in different tenses.",
        "89. Practice the use of verbal periphrases: Like /going to + infinitive,/ /have to + infinitive.",
        "90. Know the rules of agreement in subordinate clauses: To maintain coherence.",
        "91. Use reflexive pronouns correctly: Like /myself,/ /yourself," "himself.",
        "92. Avoid anacoluthons: Avoid interruptions or abrupt changes in sentence structure.",
        "93. Master the use of adversative sentences: With /but," "although," "however.",
        "94. Use possessives correctly: /My," "your," "his/her," "our," "your.",
        "95. Practice the use of copulative sentences: With verbs like /to be," "to seem.",
        "96. Know the differences between /más/ and /mas/: /Más/ indicates quantity, and /mas/ is a conjunction.",
        "97. Avoid ambiguity in pronouns: Ensure that the reference is clear.",
        "98. Use the verb /deber/ correctly: Differentiate between /deber/ (must) and /deber de/ (should).",
        "99. Practice the use of direct and indirect speech: To narrate dialogues and thoughts.",
        "100. Know the differences between /este,/ /éste,/ and /esté/: /Éste/ no longer carries an accent according to the RAE, but /esté/ is a verb in the subjunctive mood.",
        "101. Ensure the text flows naturally from one idea to another.",
        # Continúa con los demás consejos en inglés...
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
