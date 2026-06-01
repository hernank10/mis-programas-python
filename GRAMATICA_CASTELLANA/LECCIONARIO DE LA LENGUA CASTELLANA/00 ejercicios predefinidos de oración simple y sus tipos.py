import random

def cargar_ejercicios_oracion_simple():
    """
    Carga los 100 ejercicios predefinidos de oración simple y sus tipos
    directamente en el código.
    """
    print("Cargando 100 ejercicios de Oración Simple y sus Tipos directamente...")
    return {
        "Sintaxis": {
            "Básico": {
                "Oración Simple y sus Tipos": [
                    {"pregunta": "Clasifica la oración: 'El sol brilla intensamente.'", "respuesta": "enunciativa", "explicacion": "Afirma un hecho."},
                    {"pregunta": "Clasifica la oración: '¿Has terminado tu tarea?'", "respuesta": "interrogativa", "explicacion": "Formula una pregunta directa."},
                    {"pregunta": "Clasifica la oración: '¡Qué día tan hermoso!'", "respuesta": "exclamativa", "explicacion": "Expresa una emoción intensa."},
                    {"pregunta": "Clasifica la oración: 'Cierra la puerta, por favor.'", "respuesta": "imperativa", "explicacion": "Expresa una orden o petición."},
                    {"pregunta": "Clasifica la oración: 'Quizás llueva mañana.'", "respuesta": "dubitativa", "explicacion": "Expresa duda o posibilidad."},
                    {"pregunta": "Clasifica la oración: 'Ojalá vengas pronto.'", "respuesta": "desiderativa", "explicacion": "Expresa un deseo."},
                    {"pregunta": "Clasifica la oración: 'Mañana tenemos examen.'", "respuesta": "enunciativa", "explicacion": "Afirma un hecho o evento."},
                    {"pregunta": "Clasifica la oración: '¿Quién es ese chico?'", "respuesta": "interrogativa", "explicacion": "Formula una pregunta directa."},
                    {"pregunta": "Clasifica la oración: '¡No lo puedo creer!'", "respuesta": "exclamativa", "explicacion": "Expresa asombro o incredulidad."},
                    {"pregunta": "Clasifica la oración: 'Trae el libro aquí.'", "respuesta": "imperativa", "explicacion": "Expresa una orden."},
                    {"pregunta": "Clasifica la oración: 'Tal vez me equivoque.'", "respuesta": "dubitativa", "explicacion": "Expresa duda."},
                    {"pregunta": "Clasifica la oración: 'Así te vaya muy bien.'", "respuesta": "desiderativa", "explicacion": "Expresa un deseo de éxito."},
                    {"pregunta": "Clasifica la oración: 'El perro ladra fuerte.'", "respuesta": "enunciativa", "explicacion": "Afirma una acción."},
                    {"pregunta": "Clasifica la oración: '¿Cuándo llega el tren?'", "respuesta": "interrogativa", "explicacion": "Formula una pregunta sobre tiempo."},
                    {"pregunta": "Clasifica la oración: '¡Qué frío hace!'", "respuesta": "exclamativa", "explicacion": "Expresa una sensación intensa."},
                    {"pregunta": "Clasifica la oración: 'No pises el césped.'", "respuesta": "imperativa", "explicacion": "Expresa una prohibición o mandato."},
                    {"pregunta": "Clasifica la oración: 'Probablemente llegue tarde.'", "respuesta": "dubitativa", "explicacion": "Expresa probabilidad."},
                    {"pregunta": "Clasifica la oración: 'Que tengas un buen viaje.'", "respuesta": "desiderativa", "explicacion": "Expresa un deseo de bienestar."},
                    {"pregunta": "Clasifica la oración: 'Hemos comido paella.'", "respuesta": "enunciativa", "explicacion": "Afirma una acción pasada."},
                    {"pregunta": "Clasifica la oración: '¿Dónde está mi teléfono?'", "respuesta": "interrogativa", "explicacion": "Formula una pregunta sobre ubicación."},
                    {"pregunta": "Clasifica la oración: '¡Por fin vacaciones!'", "respuesta": "exclamativa", "explicacion": "Expresa alivio o entusiasmo."},
                    {"pregunta": "Clasifica la oración: 'Ayúdame con esto.'", "respuesta": "imperativa", "explicacion": "Expresa una petición de ayuda."},
                    {"pregunta": "Clasifica la oración: 'Posiblemente vaya al cine.'", "respuesta": "dubitativa", "explicacion": "Expresa una posibilidad."},
                    {"pregunta": "Clasifica la oración: 'Dios quiera que apruebes.'", "respuesta": "desiderativa", "explicacion": "Expresa un deseo con una invocación."},
                    {"pregunta": "Clasifica la oración: 'La película empieza a las ocho.'", "respuesta": "enunciativa", "explicacion": "Afirma un horario."},
                    {"pregunta": "Clasifica la oración: '¿Por qué llegaste tarde?'", "respuesta": "interrogativa", "explicacion": "Formula una pregunta sobre la causa."},
                    {"pregunta": "Clasifica la oración: '¡Menuda sorpresa!'", "respuesta": "exclamativa", "explicacion": "Expresa asombro."},
                    {"pregunta": "Clasifica la oración: 'Estudia para el examen.'", "respuesta": "imperativa", "explicacion": "Expresa un consejo o mandato."},
                    {"pregunta": "Clasifica la oración: 'A lo mejor no viene.'", "respuesta": "dubitativa", "explicacion": "Expresa incertidumbre."},
                    {"pregunta": "Clasifica la oración: 'Que te diviertas mucho.'", "respuesta": "desiderativa", "explicacion": "Expresa un deseo de diversión."},
                    {"pregunta": "Clasifica la oración: 'Los pájaros cantan.'", "respuesta": "enunciativa", "explicacion": "Afirma un hecho."},
                    {"pregunta": "Clasifica la oración: '¿Sabes la respuesta?'", "respuesta": "interrogativa", "explicacion": "Formula una pregunta sobre conocimiento."},
                    {"pregunta": "Clasifica la oración: '¡Qué barbaridad!'", "respuesta": "exclamativa", "explicacion": "Expresa indignación o asombro."},
                    {"pregunta": "Clasifica la oración: 'Siéntate aquí.'", "respuesta": "imperativa", "explicacion": "Expresa una orden."},
                    {"pregunta": "Clasifica la oración: 'Quizá gane la lotería.'", "respuesta": "dubitativa", "explicacion": "Expresa una posibilidad lejana."},
                    {"pregunta": "Clasifica la oración: 'Ojalá que sí.'", "respuesta": "desiderativa", "explicacion": "Expresa un deseo afirmativo."},
                    {"pregunta": "Clasifica la oración: 'El agua hierve.'", "respuesta": "enunciativa", "explicacion": "Afirma un estado."},
                    {"pregunta": "Clasifica la oración: '¿Comiste ya?'", "respuesta": "interrogativa", "explicacion": "Formula una pregunta simple."},
                    {"pregunta": "Clasifica la oración: '¡Qué suerte!'", "respuesta": "exclamativa", "explicacion": "Expresa buena fortuna."},
                    {"pregunta": "Clasifica la oración: 'No hagas eso.'", "respuesta": "imperativa", "explicacion": "Expresa una orden negativa."},
                    {"pregunta": "Clasifica la oración: 'Tal vez esté equivocado.'", "respuesta": "dubitativa", "explicacion": "Expresa incertidumbre."},
                    {"pregunta": "Clasifica la oración: 'Que te mejores pronto.'", "respuesta": "desiderativa", "explicacion": "Expresa un deseo de recuperación."},
                    {"pregunta": "Clasifica la oración: 'Ella es mi hermana.'", "respuesta": "enunciativa", "explicacion": "Afirma una relación."},
                    {"pregunta": "Clasifica la oración: '¿Me ayudas, por favor?'", "respuesta": "interrogativa", "explicacion": "Formula una pregunta educada."},
                    {"pregunta": "Clasifica la oración: '¡Dios mío!'", "respuesta": "exclamativa", "explicacion": "Expresa sorpresa o consternación."},
                    {"pregunta": "Clasifica la oración: 'Ven aquí ahora mismo.'", "respuesta": "imperativa", "explicacion": "Expresa una orden urgente."},
                    {"pregunta": "Clasifica la oración: 'Probablemente no lo sepa.'", "respuesta": "dubitativa", "explicacion": "Expresa probabilidad negativa."},
                    {"pregunta": "Clasifica la oración: 'Ojalá pudiera volar.'", "respuesta": "desiderativa", "explicacion": "Expresa un deseo irrealizable."},
                    {"pregunta": "Clasifica la oración: 'Estoy cansado.'", "respuesta": "enunciativa", "explicacion": "Afirma un estado físico."},
                    {"pregunta": "Clasifica la oración: '¿A dónde vas?'", "respuesta": "interrogativa", "explicacion": "Formula una pregunta sobre destino."},
                    {"pregunta": "Clasifica la oración: '¡Qué pena!'", "respuesta": "exclamativa", "explicacion": "Expresa lástima o desilusión."},
                    {"pregunta": "Clasifica la oración: 'Escúchame bien.'", "respuesta": "imperativa", "explicacion": "Expresa una orden de atención."},
                    {"pregunta": "Clasifica la oración: 'A lo mejor consigo el trabajo.'", "respuesta": "dubitativa", "explicacion": "Expresa una posibilidad optimista."},
                    {"pregunta": "Clasifica la oración: 'Que en paz descanse.'", "respuesta": "desiderativa", "explicacion": "Expresa un deseo de reposo eterno."},
                    {"pregunta": "Clasifica la oración: 'Mi coche es nuevo.'", "respuesta": "enunciativa", "explicacion": "Afirma una característica."},
                    {"pregunta": "Clasifica la oración: '¿Entendiste la explicación?'", "respuesta": "interrogativa", "explicacion": "Formula una pregunta sobre comprensión."},
                    {"pregunta": "Clasifica la oración: '¡Genial!'", "respuesta": "exclamativa", "explicacion": "Expresa aprobación o entusiasmo."},
                    {"pregunta": "Clasifica la oración: 'Lee el capítulo cinco.'", "respuesta": "imperativa", "explicacion": "Expresa un mandato o sugerencia."},
                    {"pregunta": "Clasifica la oración: 'Quizás no lo necesitemos.'", "respuesta": "dubitativa", "explicacion": "Expresa una posibilidad de no necesidad."},
                    {"pregunta": "Clasifica la oración: 'Que tengas un día excelente.'", "respuesta": "desiderativa", "explicacion": "Expresa un deseo de éxito en el día."},
                    {"pregunta": "Clasifica la oración: 'El cielo está despejado.'", "respuesta": "enunciativa", "explicacion": "Afirma una condición meteorológica."},
                    {"pregunta": "Clasifica la oración: '¿Cómo te sientes?'", "respuesta": "interrogativa", "explicacion": "Formula una pregunta sobre estado de ánimo."},
                    {"pregunta": "Clasifica la oración: '¡Maravilloso!'", "respuesta": "exclamativa", "explicacion": "Expresa admiración."},
                    {"pregunta": "Clasifica la oración: 'No te preocupes.'", "respuesta": "imperativa", "explicacion": "Expresa un consejo o ruego."},
                    {"pregunta": "Clasifica la oración: 'Tal vez sea lo mejor.'", "respuesta": "dubitativa", "explicacion": "Expresa una posibilidad de conveniencia."},
                    {"pregunta": "Clasifica la oración: 'Ojalá llueva café en el campo.'", "respuesta": "desiderativa", "explicacion": "Expresa un deseo poético."},
                    {"pregunta": "Clasifica la oración: 'Ella cocina muy bien.'", "respuesta": "enunciativa", "explicacion": "Afirma una habilidad."},
                    {"pregunta": "Clasifica la oración: '¿Vendrás a la fiesta?'", "respuesta": "interrogativa", "explicacion": "Formula una pregunta sobre un evento futuro."},
                    {"pregunta": "Clasifica la oración: '¡Qué desastre!'", "respuesta": "exclamativa", "explicacion": "Expresa frustración o decepción."},
                    {"pregunta": "Clasifica la oración: 'Haz tu cama.'", "respuesta": "imperativa", "explicacion": "Expresa una orden doméstica."},
                    {"pregunta": "Clasifica la oración: 'Probablemente haga sol.'", "respuesta": "dubitativa", "explicacion": "Expresa una probabilidad meteorológica."},
                    {"pregunta": "Clasifica la oración: 'Que te acompañe la suerte.'", "respuesta": "desiderativa", "explicacion": "Expresa un deseo de buena fortuna."},
                    {"pregunta": "Clasifica la oración: 'El examen fue fácil.'", "respuesta": "enunciativa", "explicacion": "Afirma una cualidad del examen."},
                    {"pregunta": "Clasifica la oración: '¿A qué hora llegas?'", "respuesta": "interrogativa", "explicacion": "Formula una pregunta sobre horario."},
                    {"pregunta": "Clasifica la oración: '¡Viva la vida!'", "respuesta": "exclamativa", "explicacion": "Expresa alegría o celebración."},
                    {"pregunta": "Clasifica la oración: 'Coge tu paraguas.'", "respuesta": "imperativa", "explicacion": "Expresa un mandato."},
                    {"pregunta": "Clasifica la oración: 'A lo mejor se arrepiente.'", "respuesta": "dubitativa", "explicacion": "Expresa una posibilidad de cambio de opinión."},
                    {"pregunta": "Clasifica la oración: 'Que todo salga bien.'", "respuesta": "desiderativa", "explicacion": "Expresa un deseo de éxito."},
                    {"pregunta": "Clasifica la oración: 'Nos vemos mañana.'", "respuesta": "enunciativa", "explicacion": "Afirma un encuentro futuro."},
                    {"pregunta": "Clasifica la oración: '¿Leíste el periódico?'", "respuesta": "interrogativa", "explicacion": "Formula una pregunta sobre una acción pasada."},
                    {"pregunta": "Clasifica la oración: '¡Increíble!'", "respuesta": "exclamativa", "explicacion": "Expresa asombro."},
                    {"pregunta": "Clasifica la oración: 'Pasa la sal.'", "respuesta": "imperativa", "explicacion": "Expresa una petición."},
                    {"pregunta": "Clasifica la oración: 'Quizás no haya solución.'", "respuesta": "dubitativa", "explicacion": "Expresa una posibilidad de falta de solución."},
                    {"pregunta": "Clasifica la oración: 'Ojalá no te olvides.'", "respuesta": "desiderativa", "explicacion": "Expresa un deseo de no olvido."},
                    {"pregunta": "Clasifica la oración: 'El café está caliente.'", "respuesta": "enunciativa", "explicacion": "Afirma una característica."},
                    {"pregunta": "Clasifica la oración: '¿Estás de acuerdo?'", "respuesta": "interrogativa", "explicacion": "Formula una pregunta sobre opinión."},
                    {"pregunta": "Clasifica la oración: '¡Qué susto!'", "respuesta": "exclamativa", "explicacion": "Expresa miedo o sobresalto."},
                    {"pregunta": "Clasifica la oración: 'No te rindas.'", "respuesta": "imperativa", "explicacion": "Expresa un consejo o ánimo."},
                    {"pregunta": "Clasifica la oración: 'Tal vez tenga razón.'", "respuesta": "dubitativa", "explicacion": "Expresa una posibilidad de acierto."},
                    {"pregunta": "Clasifica la oración: 'Que así sea.'", "respuesta": "desiderativa", "explicacion": "Expresa conformidad con un deseo."},
                    {"pregunta": "Clasifica la oración: 'Los niños juegan.'", "respuesta": "enunciativa", "explicacion": "Afirma una acción."},
                    {"pregunta": "Clasifica la oración: '¿Vamos al parque?'", "respuesta": "interrogativa", "explicacion": "Formula una invitación o sugerencia."},
                    {"pregunta": "Clasifica la oración: '¡Magnífico!'", "respuesta": "exclamativa", "explicacion": "Expresa gran aprobación."},
                    {"pregunta": "Clasifica la oración: 'Dame tu mano.'", "respuesta": "imperativa", "explicacion": "Expresa una petición."},
                    {"pregunta": "Clasifica la oración: 'Probablemente sea difícil.'", "respuesta": "dubitativa", "explicacion": "Expresa probabilidad de dificultad."},
                    {"pregunta": "Clasifica la oración: 'Ojalá te guste.'", "respuesta": "desiderativa", "explicacion": "Expresa un deseo de agrado."},
                    {"pregunta": "Clasifica la oración: 'La flor es roja.'", "respuesta": "enunciativa", "explicacion": "Afirma una cualidad."},
                    {"pregunta": "Clasifica la oración: '¿Qué hora es?'", "respuesta": "interrogativa", "explicacion": "Formula una pregunta sobre el tiempo."},
                    {"pregunta": "Clasifica la oración: '¡Estupendo!'", "respuesta": "exclamativa", "explicacion": "Expresa satisfacción."},
                    {"pregunta": "Clasifica la oración: 'No olvides tus llaves.'", "respuesta": "imperativa", "explicacion": "Expresa un recordatorio o mandato negativo."},
                    {"pregunta": "Clasifica la oración: 'A lo mejor encontramos la solución.'", "respuesta": "dubitativa", "explicacion": "Expresa una posibilidad de hallazgo."},
                    {"pregunta": "Clasifica la oración: 'Que te lo pases bien.'", "respuesta": "desiderativa", "explicacion": "Expresa un deseo de disfrute."},
                    {"pregunta": "Clasifica la oración: 'Ella tiene un perro.'", "respuesta": "enunciativa", "explicacion": "Afirma una posesión."},
                    {"pregunta": "Clasifica la oración: '¿Viste la película?'", "respuesta": "interrogativa", "explicacion": "Formula una pregunta sobre una acción pasada."},
                    {"pregunta": "Clasifica la oración: '¡Qué barbaridad!'", "respuesta": "exclamativa", "explicacion": "Expresa indignación o asombro."},
                    {"pregunta": "Clasifica la oración: 'Abre la ventana.'", "respuesta": "imperativa", "explicacion": "Expresa una orden simple."},
                    {"pregunta": "Clasifica la oración: 'Quizás no sea buena idea.'", "respuesta": "dubitativa", "explicacion": "Expresa una posibilidad de mala idea."},
                    {"pregunta": "Clasifica la oración: 'Ojalá que no llueva.'", "respuesta": "desiderativa", "explicacion": "Expresa un deseo de que no ocurra algo."},
                    {"pregunta": "Clasifica la oración: 'El coche es rápido.'", "respuesta": "enunciativa", "explicacion": "Afirma una cualidad."},
                    {"pregunta": "Clasifica la oración: '¿Puedes ayudarme con esto?'", "respuesta": "interrogativa", "explicacion": "Formula una pregunta indirecta o petición."},
                    {"pregunta": "Clasifica la oración: '¡Qué dolor!'", "respuesta": "exclamativa", "explicacion": "Expresa una sensación de dolor."},
                    {"pregunta": "Clasifica la oración: 'Vete de aquí.'", "respuesta": "imperativa", "explicacion": "Expresa una orden para irse."}
                ]
            }
        }
    }

def normalizar_respuesta(respuesta):
    """Normaliza una respuesta para comparación (quitar espacios, minúsculas, eliminar tildes)."""
    if isinstance(respuesta, str):
        return respuesta.strip().lower().replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')
    return respuesta

def comparar_respuestas(respuesta_usuario, respuesta_correcta):
    """Compara la respuesta del usuario con la respuesta correcta después de normalizar."""
    return normalizar_respuesta(respuesta_usuario) == normalizar_respuesta(respuesta_correcta)

def iniciar_practica_oracion_simple():
    """Inicia la práctica de oración simple y sus tipos en consola."""
    ejercicios_castellano = cargar_ejercicios_oracion_simple()
    
    # Accedemos directamente a los ejercicios de oración simple y sus tipos
    ejercicios_oracion_simple = ejercicios_castellano["Sintaxis"]["Básico"]["Oración Simple y sus Tipos"]
    
    if not ejercicios_oracion_simple:
        print("No hay ejercicios de oración simple y sus tipos disponibles.")
        return

    random.shuffle(ejercicios_oracion_simple) # Mezclar los ejercicios

    puntuacion = 0
    resultados = []

    print("\n--- ¡Bienvenido a la Práctica de la Oración Simple y sus Tipos! ---")
    print("Clasifica cada oración en uno de los siguientes tipos:")
    print("enunciativa, interrogativa, exclamativa, imperativa, dubitativa, desiderativa")
    print(f"Tienes {len(ejercicios_oracion_simple)} ejercicios para practicar.\n")

    for i, ejercicio in enumerate(ejercicios_oracion_simple):
        print(f"\n--- Ejercicio {i + 1} de {len(ejercicios_oracion_simple)} ---")
        print(f"Oración: '{ejercicio['pregunta']}'")
        
        respuesta_usuario = input("Tu clasificación: ").strip()

        es_correcta = comparar_respuestas(respuesta_usuario, ejercicio['respuesta'])

        if es_correcta:
            print("¡Correcto! ✅")
            puntuacion += 1
        else:
            print("Incorrecto. ❌")
        
        print(f"La clasificación correcta era: {ejercicio['respuesta']}")
        print(f"Explicación: {ejercicio['explicacion']}")
        
        resultados.append({
            "pregunta": ejercicio['pregunta'],
            "tu_respuesta": respuesta_usuario,
            "correcta": es_correcta,
            "respuesta_correcta": ejercicio['respuesta'],
            "explicacion": ejercicio['explicacion']
        })

    print("\n--- Práctica Terminada ---")
    print(f"Has obtenido {puntuacion} de {len(ejercicios_oracion_simple)} respuestas correctas.")
    print("\n--- Resumen de Resultados ---")
    for res in resultados:
        estado = "✅ CORRECTO" if res['correcta'] else "❌ INCORRECTO"
        print(f"\nOración: '{res['pregunta']}'")
        print(f"Tu clasificación: {res['tu_respuesta']}")
        print(f"Clasificación correcta: {res['respuesta_correcta']}")
        print(f"Estado: {estado}")
        print(f"Explicación: {res['explicacion']}")
    
    print("\n¡Gracias por practicar!")

if __name__ == "__main__":
    iniciar_practica_oracion_simple()
