# Programa interactivo de completar frases y organizar oraciones

def cuestionario():
    preguntas = [
        {
            "tipo": "completar",
            "pregunta": "👨Completa la frase: 'Si hubiera más tiempo, nosotros _________ (poder) viajar a más lugares.'",
            "respuesta": "podríamos",
            "retroalimentacion": "🎒✏️📘La respuesta correcta es 'podríamos', ya que en oraciones condicionales irreales se usa el condicional simple."
        },
        {
            "tipo": "completar",
            "pregunta": "👨Completa la oración: 'Estoy interesado ______ aprender más sobre literatura hispanoamericana.'",
            "respuesta": "en",
            "retroalimentacion": "🎒✏️📘La preposición adecuada es 'en', ya que indica interés en algo."
        },
        {
            "tipo": "👩organizar",
            "pregunta": "Organiza la oración: 'ayer / llovió / no / a pesar de que / salió / con / paraguas / Ana'",
            "respuesta": "A pesar de que no llovió ayer, Ana salió con paraguas.",
            "retroalimentacion": "🎒✏️📘El orden correcto respeta la subordinación y el sentido lógico de la frase."
        },
        {
            "tipo": "👩completar",
            "pregunta": "Completa la oración: 'El niño estaba buscando su juguete, pero no lo encontró porque alguien _________ había escondido.'",
            "respuesta": "se lo",
            "retroalimentacion": "🎒✏️📘La respuesta correcta es 'se lo', combinando el pronombre reflexivo 'se' y el objeto directo 'lo'."
        },
        {
            "tipo": "👩opcion",
            "pregunta": "Completa la oración: '________ termine mis tareas, podré salir a jugar.'\n a) Cuando\n b) Aunque\n c) Porque\n d) Si",
            "respuesta": "a",
            "retroalimentacion": "🎒✏️📘La conjunción 'cuando' introduce una oración subordinada temporal."
        }

    ]

    print("🏛️ 👩¡Bienvenido al cuestionario de gramática!👨‍🏫 🏛️")
    puntuacion = 0

    for i, pregunta in enumerate(preguntas):
        print(f"\nPregunta {i + 1}:")
        print(pregunta["pregunta"])
        
        if pregunta["tipo"] == "opcion":
            respuesta_usuario = input(" 👩Escribe la letra de tu respuesta: ").strip().lower()
        else:
            respuesta_usuario = input(" 👩Tu respuesta: ").strip()

        if respuesta_usuario == pregunta["respuesta"]:
            print("✅ ¡ 🚀🌠🏅Correcto!")
            puntuacion += 1
        else:
            print("❌ 👨Incorrecto.")
        
        print(f"💡 Retroalimentación: {pregunta['retroalimentacion']}")

    print("\n  👩¡Has completado el cuestionario!🎒✏️📘")
    print(f"Tu puntuación final es: {puntuacion}/{len(preguntas)}")

# Ejecutar el programa
if __name__ == "__main__":
    cuestionario()
