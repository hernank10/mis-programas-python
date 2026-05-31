def mostrar_pregunta(pregunta, opciones, respuesta_correcta):
    """Muestra una pregunta y evalúa la respuesta del usuario."""
    print("\n" + pregunta)
    for i, opcion in enumerate(opciones, 1):
        print(f"{i}. {opcion}")
    try:
        respuesta_usuario = int(input("Elige la opción correcta (1/2/3): "))
        if respuesta_usuario == respuesta_correcta:
            print("🌟📜✏️🕵🏛¡Correcto!✅")
            return True
        else:
            print(f"Incorrecto❌. La respuesta correcta era: {opciones[respuesta_correcta - 1]}")
            return False
    except ValueError:
        print("Entrada inválida❌. Por favor, selecciona una opción válida.")
        return False

def cuestionario_descriptivo():
    """🌟📜✏️🕵🏛 Cuestionario interactivo sobre la Gramática descriptiva del español.🌟📜✏️🕵🏛"""
    preguntas = [
        ("🌟📜✏️🕵🏛¿Qué es un fonema?", 
         ["La unidad mínima de significado en una lengua.",
          "La unidad mínima distintiva de sonido.",
          "La combinación de dos sonidos."],
         2),
        ("🌟📜✏️🕵🏛¿Qué es una consonante oclusiva?", 
         ["Un sonido que se produce con una vibración de las cuerdas vocales.",
          "Un sonido que se produce cerrando completamente el paso del aire.",
          "Un sonido que se produce sin obstáculo en el flujo del aire."], 
         2),
        ("🌟📜✏️🕵🏛¿Qué es un morfema?", 
         ["Una palabra completa.", 
          "La unidad mínima con significado gramatical.", 
          "Una categoría gramatical."], 
         2),
        ("🌟📜✏️🕵🏛¿Qué tipo de morfema es el sufijo *-ito* en *perrito*?", 
         ["Morfema derivativo.", 
          "Morfema flexivo.", 
          "Morfema léxico."], 
         1),
        ("🌟📜✏️🕵🏛¿Qué es una oración simple?", 
         ["Una oración que contiene un solo verbo conjugado.",
          "Una oración con dos o más verbos conjugados.",
          "Una oración subordinada."], 
         1),
        ("🌟📜✏️🕵🏛¿Qué función tiene el complemento directo en la oración?", 
         ["Modificar el verbo.", 
          "Señalar quién realiza la acción.", 
          "Completar el significado del verbo transitivo."], 
         3),
        ("🌟📜✏️🕵🏛¿Qué es un campo semántico?", 
         ["Un conjunto de palabras relacionadas por su forma.",
          "Un conjunto de palabras relacionadas por su significado.",
          "Un conjunto de palabras derivadas del mismo origen."], 
         2),
        ("🌟📜✏️🕵🏛¿Qué es un sinónimo?", 
         ["Una palabra con significado opuesto.",
          "Una palabra con significado similar.",
          "Una palabra que suena igual pero tiene diferente significado."], 
         2),
    ]
    
    print("🌟📜✏️🕵🏛¡Bienvenido al Cuestionario sobre la Gramática descriptiva del español!🌟📜✏️🕵🏛")
    puntuacion = 0
    for pregunta, opciones, respuesta_correcta in preguntas:
        if mostrar_pregunta(pregunta, opciones, respuesta_correcta):
            puntuacion += 1
    
    print(f"\n🌟📜✏️🕵🏛¡Has completado el cuestionario! Tu puntuación final es {puntuacion}/{len(preguntas)}.")

# Llamada al cuestionario
cuestionario_descriptivo()
