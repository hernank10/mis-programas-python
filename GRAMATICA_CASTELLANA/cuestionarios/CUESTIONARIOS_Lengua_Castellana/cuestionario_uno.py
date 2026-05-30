def main():
    print("🏛️ 👩¡Bienvenido al cuestionario de gramática avanzada! 👨‍🏫 🏛")
    print("👩Responde las preguntas escribiendo la letra de la opción correcta (a, b, c o d), o completa las oraciones según corresponda.\n")
    
    # Lista de preguntas con opciones y respuestas correctas
    preguntas = [
        {
            "pregunta": "¿👩Cuál es el uso principal de los paréntesis en el siguiente ejemplo? \n'Pedro (mi mejor amigo) vino a visitarme.'",
            "opciones": ["a) Aclaración", "b) Enumeración", "c) Vocativo", "d) Exclamación"],
            "respuesta": "a",
            "retroalimentacion": "Los paréntesis se usan aquí para hacer una aclaración adicional sobre 'Pedro'."
        },
        {
            "pregunta": "👩Completa la oración con la forma correcta del verbo:\nSi yo ________ (tener) tiempo, iría contigo.",
            "respuesta": "tuviera",
            "retroalimentacion": "La forma correcta es 'tuviera', ya que se trata de una oración condicional irreal."
        },
        {
            "pregunta": "👩¿Qué tipo de morfema es el sufijo '-ito' en 'perrito'?",
            "opciones": ["a) Derivativo diminutivo", "b) Flexivo de número", "c) Derivativo aumentativo", "d) Flexivo de género"],
            "respuesta": "a",
            "retroalimentacion": "El sufijo '-ito' es derivativo diminutivo porque modifica el significado del sustantivo original."
        },
        {
            "pregunta": "👩Completa la oración con la forma correcta:\nEl libro (que, cual) ________ leí, fue muy interesante.",
            "respuesta": "que",
            "retroalimentacion": "La palabra 'que' es la forma adecuada para esta oración porque introduce una oración subordinada especificativa."
        },
        {
            "pregunta": "👩¿Cuál es el uso correcto de los paréntesis en la siguiente oración? \n'Salió de casa temprano (a las 6:00 AM) para evitar el tráfico.'",
            "opciones": ["a) Aclaración temporal", "b) Indicar ironía", "c) Enumeración", "d) Vocativo"],
            "respuesta": "a",
            "retroalimentacion": "Aquí los paréntesis se usan para hacer una aclaración temporal sobre la hora exacta."
        },
        {
            "pregunta": "👩¿Cómo se llama el proceso en el que una palabra cambia para concordar en género o número?",
            "opciones": ["a) Flexión", "b) Derivación", "c) Composición", "d) Parasíntesis"],
            "respuesta": "a",
            "retroalimentacion": "La flexión permite que una palabra cambie para concordar en género o número."
        },
        {
            "pregunta": "👩Completa la oración con la preposición correcta:\nMe interesa mucho aprender ________ historia y cultura.",
            "respuesta": "sobre",
            "retroalimentacion": "La preposición correcta es 'sobre', porque indica el tema de interés."
        },
        {
            "pregunta": "👩¿Qué tipo de palabra es 'rápido' en la oración: 'Corre rápido al mercado'?",
            "opciones": ["a) Sustantivo", "b) Verbo", "c) Adverbio", "d) Adjetivo"],
            "respuesta": "c",
            "retroalimentacion": "'Rápido' actúa como adverbio porque modifica al verbo 'corre'."
        },
        {
            "pregunta": "👩¿Qué función cumplen los paréntesis en esta oración? \n'Los planetas (Mercurio, Venus, Tierra y Marte) son parte del sistema solar.'",
            "opciones": ["a) Enumeración", "b) Aclaración explicativa", "c) Ironía", "d) Vocativo"],
            "respuesta": "b",
            "retroalimentacion": "Los paréntesis aquí hacen una aclaración explicativa sobre los planetas mencionados."
        },
        {
            "pregunta": "👩Completa la oración: \nEl prefijo 'in-' en 'inmortal' significa ________.",
            "respuesta": "negación",
            "retroalimentacion": "El prefijo 'in-' significa negación, indicando que algo no es mortal."
        }
    ]
    
    puntuacion = 0

    # Bucle para recorrer las preguntas
    for i, pregunta in enumerate(preguntas):
        print(f"Pregunta {i + 1}: {pregunta['pregunta']}")
        
        if "opciones" in pregunta:
            for opcion in pregunta["opciones"]:
                print(opcion)
            respuesta = input("Tu respuesta: ").lower()
        else:
            respuesta = input("Completa la oración: ").strip().lower()
        
        if respuesta == pregunta["respuesta"]:
            print("¡Correcto!")
            puntuacion += 1
        else:
            print("Incorrecto.")
        print("Retroalimentación:", pregunta["retroalimentacion"], "\n")
    
    print(f"Tu puntuación final es: {puntuacion}/{len(preguntas)}")
    print("¡👩Gracias por participar!")

if __name__ == "__main__":
    main()
