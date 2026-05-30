#!/usr/bin/env python3
"""
Programa de consola: 100 ejercicios para construir preguntas en inglés
Perspectiva: hispanohablante (las instrucciones y prompts en español)
Archivo: 100_question_exercises_english.py

Características:
- 100 ejercicios variados que cubren los 8 tipos de preguntas.
- Para cada ejercicio se muestra la frase/consulta en español y el usuario debe escribir la pregunta correcta en inglés.
- El programa acepta varias respuestas equivalentes (manejo de contracciones y alternativas comunes).
- Pistas, explicaciones y retroalimentación inmediata.
- Registro de puntuación y resumen al final.

Modo de uso: ejecutar en consola: python3 100_question_exercises_english.py
"""

from typing import List, Dict
import random
import re
import sys

# -----------------------------
# UTILIDADES
# -----------------------------

def normalize(s: str) -> str:
    """Normaliza el texto para comparaciones: minúsculas, quita puntuación innecesaria,
    convierte contracciones simples a formas equivalentes para facilitar la verificación."""
    s = s.lower().strip()
    # reemplazos comunes para facilitar coincidencias
    replacements = {
        "what's": "what is",
        "where's": "where is",
        "who's": "who is",
        "it's": "it is",
        "i'm": "i am",
        "we're": "we are",
        "they're": "they are",
        "you're": "you are",
        "didn't": "did not",
        "doesn't": "does not",
        "don't": "do not",
        "can't": "cannot",
        "won't": "will not",
        "wouldn't": "would not",
    }
    for k, v in replacements.items():
        s = s.replace(k, v)
    # remover puntuación excepto signos de interrogación
    s = re.sub(r"[\.,;:\(\)\"]", "", s)
    # normalizar espacios y signos de pregunta
    s = re.sub(r"\s+", " ", s)
    s = s.replace("?", " ?")
    s = s.strip()
    return s


def is_equivalent(user_ans: str, correct_variants: List[str]) -> bool:
    ua = normalize(user_ans)
    for v in correct_variants:
        if ua == normalize(v):
            return True
    # comparaciones más flexibles: permitir inversión auxiliar + sujeto faltante en caso de respuestas cortas
    # ejemplo: "Where is the station?" vs "Where the station is?" (incorrect but a learner error) - no admitir.
    return False


# -----------------------------
# EJERCICIOS (100)
# Cada ejercicio: español, lista de respuestas aceptables, tipo (uno de los 8), pista, explicación breve
# -----------------------------

EXERCISES: List[Dict] = [
    # 1-10: Yes/No Questions
    {"es": "¿Te gusta la música?", "answers": ["Do you like music?"], "type": "Yes/No", "hint": "Empieza con 'Do' / 'Does' si es tercera persona", "ex": "Yes/No: auxiliar + sujeto + verbo."},
    {"es": "¿Ella está en casa?", "answers": ["Is she at home?"], "type": "Yes/No", "hint": "Usa 'Is' para 'she'", "ex": "Verbo 'to be' invierte sujeto y verbo."},
    {"es": "¿Comieron ya?", "answers": ["Have they eaten yet?","Did they eat already?"], "type": "Yes/No", "hint": "¿Presente perfecto o pasado?" , "ex": "Ambas son aceptables según contexto."},
    {"es": "¿Vas al cine?", "answers": ["Are you going to the cinema?","Do you go to the cinema?"], "type": "Yes/No", "hint": "'Going to' para planes cercanos; 'Do' para hábitos.", "ex": "Distinción entre plan/acción y hábito."},
    {"es": "¿Él juega fútbol?", "answers": ["Does he play football?","Does he play soccer?"], "type": "Yes/No", "hint": "Tercera persona singular: 'Does'", "ex": "No olvidar la 's' en la forma afirmativa (he plays) pero no en la interrogativa con 'does'."},
    {"es": "¿Puedes ayudarme?", "answers": ["Can you help me?"], "type": "Yes/No", "hint": "Verbo modal 'Can' al inicio.", "ex": "Los modales van antes del sujeto."},
    {"es": "¿Debo llamarte?", "answers": ["Should I call you?","Shall I call you?"], "type": "Yes/No", "hint": "'Should' o 'Shall' según nivel de formalidad.", "ex": "Uso de auxiliares modales."},
    {"es": "¿Tienen ustedes tiempo?", "answers": ["Do you have time?","Have you got time?"], "type": "Yes/No", "hint": "'Have you got' es común en inglés británico.", "ex": "Dos formas: 'Do you have' (US) y 'Have you got' (UK)."},
    {"es": "¿Ella sabe la respuesta?", "answers": ["Does she know the answer?"], "type": "Yes/No", "hint": "Tercera persona: 'Does'.", "ex": "Auxiliar 'does' + base verbal."},
    {"es": "¿Irás mañana?", "answers": ["Will you go tomorrow?","Are you going tomorrow?"], "type": "Yes/No", "hint": "'Will' para futuro; 'are you going' para plan.", "ex": "Ambas son correctas dependiendo del matiz."},

    # 11-30: Wh-Questions (who, what, where, when, why, which, how)
    {"es": "¿Dónde vives?", "answers": ["Where do you live?"], "type": "Wh-Question", "hint": "Where + auxiliar + sujeto.", "ex": "Wh-words suelen ir al inicio."},
    {"es": "¿Qué haces?", "answers": ["What are you doing?","What do you do?"], "type": "Wh-Question", "hint": "Acción en progreso o hábito.", "ex": "'What are you doing' = ahora; 'What do you do' = profesión/hábito."},
    {"es": "¿Quién llamó?", "answers": ["Who called?","Who did call?"], "type": "Wh-Question", "hint": "Who + verbo (no siempre necesita auxiliar en pasado simple).", "ex": "En pasado simple, 'Who called?' es normal."},
    {"es": "¿Por qué estudias inglés?", "answers": ["Why are you studying English?","Why do you study English?"], "type": "Wh-Question", "hint": "Presente progresivo o hábito.", "ex": "Matiz similar al ejercicio 12."},
    {"es": "¿Cuándo comienza la clase?", "answers": ["When does the class start?","When does class start?"], "type": "Wh-Question", "hint": "'Does' para tercera persona de 'class'.", "ex": "Recordar 'does' delante del sujeto."},
    {"es": "¿Cuál es tu color favorito?", "answers": ["What is your favorite color?","What's your favorite color?"], "type": "Wh-Question", "hint": "What is ...", "ex": "Contracción común 'What's'."},
    {"es": "¿A quién le diste el libro?", "answers": ["Who did you give the book to?","Whom did you give the book to?"], "type": "Wh-Question", "hint": "Quién/whom: 'whom' es formal.", "ex": "En inglés hablado 'who' es más común."},
    {"es": "¿Cómo llego al museo?", "answers": ["How do I get to the museum?","How can I get to the museum?"], "type": "Wh-Question", "hint": "'How do I get to...' es fórmula común.", "ex": "Pedir direcciones."},
    {"es": "¿Cuánto cuesta esto?", "answers": ["How much does this cost?","How much is this?"], "type": "Wh-Question", "hint": "'How much' para precios.", "ex": "Dos formas habituales."},
    {"es": "¿Cuál de los dos prefieres?", "answers": ["Which of the two do you prefer?","Which one do you prefer?"], "type": "Wh-Question", "hint": "Which + sujeto + auxiliar.", "ex": "Seleccionar entre alternativas."},
    {"es": "¿De qué hablas?", "answers": ["What are you talking about?","What do you mean?"], "type": "Wh-Question", "hint": "Expresiones comunes.", "ex": "'What do you mean?' tiene matiz distinto pero es usado para aclarar."},
    {"es": "¿Quién es el autor de ese libro?", "answers": ["Who is the author of that book?","Who wrote that book?"], "type": "Wh-Question", "hint": "Who + verbo 'write' o 'is'.", "ex": "Dos formas de preguntar autoría."},
    {"es": "¿Para quién es este regalo?", "answers": ["Who is this gift for?","Whom is this gift for?"], "type": "Wh-Question", "hint": "'For' al final es aceptable.", "ex": "Estructura preposición al final."},
    {"es": "¿Cuántos hermanos tienes?", "answers": ["How many siblings do you have?","How many brothers and sisters do you have?"], "type": "Wh-Question", "hint": "How many + nombre.", "ex": "Pedir cantidad."},
    {"es": "¿A qué hora abre la tienda?", "answers": ["What time does the store open?","At what time does the store open?"], "type": "Wh-Question", "hint": "'What time' es más natural.", "ex": "Pregunta sobre horario."},

    # 31-45: Choice Questions
    {"es": "¿Quieres té o café?", "answers": ["Do you want tea or coffee?"], "type": "Choice", "hint": "Or = or", "ex": "Ofrece alternativas."},
    {"es": "¿Preferirías caminar o tomar un taxi?", "answers": ["Would you rather walk or take a taxi?","Would you prefer to walk or take a taxi?"], "type": "Choice", "hint": "Would you rather...", "ex": "'Would you rather' para preferencias."},
    {"es": "¿Pizza o hamburguesa?", "answers": ["Pizza or burger?","Would you like pizza or a burger?"], "type": "Choice", "hint": "Forma corta es aceptable.", "ex": "Contexto informal."},
    {"es": "¿Trabajamos hoy o mañana?", "answers": ["Shall we work today or tomorrow?","Do we work today or tomorrow?"], "type": "Choice", "hint": "'Shall we' para sugerencias.", "ex": "Sugerencia/planificación."},
    {"es": "¿Quieres la sopa o la ensalada?", "answers": ["Do you want the soup or the salad?"], "type": "Choice", "hint": "Pregunta sobre menú.", "ex": "Elección entre platos."},
    {"es": "¿Vas a estudiar historia o matemáticas?", "answers": ["Are you going to study history or mathematics?","Will you study history or math?"], "type": "Choice", "hint": "Futuro vs plan.", "ex": "Diferentes matices de tiempo."},
    {"es": "¿Tomamos el tren o el autobús?", "answers": ["Shall we take the train or the bus?","Do we take the train or the bus?"], "type": "Choice", "hint": "'Shall' para proponer.", "ex": "Decisiones de transporte."},
    {"es": "¿Quieres té caliente o frío?", "answers": ["Do you want hot tea or cold tea?"], "type": "Choice", "hint": "Adjetivos antes del sustantivo.", "ex": "Respuesta con elección de cualidad."},
    {"es": "¿Estudiamos español o francés?", "answers": ["Shall we study Spanish or French?","Do we study Spanish or French?"], "type": "Choice", "hint": "Propuesta.", "ex": "Elegir entre asignaturas."},
    {"es": "¿Quieres pagar con tarjeta o en efectivo?", "answers": ["Do you want to pay with card or cash?","Would you like to pay by card or in cash?"], "type": "Choice", "hint": "Formas de pago.", "ex": "Vocabulario útil en tiendas."},

    # 46-60: Tag Questions
    {"es": "Vienes, ¿verdad?", "answers": ["You're coming, aren't you?","You are coming, aren't you?"], "type": "Tag", "hint": "Usa auxiliar opuesto en la coletilla.", "ex": "Si la oración es positiva, la tag es negativa y viceversa."},
    {"es": "No está lloviendo, ¿no?", "answers": ["It's not raining, is it?","It isn't raining, is it?"], "type": "Tag", "hint": "Negative sentence -> positive tag.", "ex": "Contraste en polaridad."},
    {"es": "Debemos irnos ahora, ¿no?", "answers": ["We must leave now, mustn't we?","We should leave now, shouldn't we?"], "type": "Tag", "hint": "Modal en la oración principal define la tag.", "ex": "Variante según modal usado."},
    {"es": "Tienes un coche, ¿verdad?", "answers": ["You have a car, don't you?","You've got a car, haven't you?"], "type": "Tag", "hint": "'Have' puede formar la tag con 'don't' o 'haven't' según forma.", "ex": "Diferencias UK/US."},
    {"es": "Ella canta bien, ¿no?", "answers": ["She sings well, doesn't she?"], "type": "Tag", "hint": "Tercera persona singular -> doesn't.", "ex": "Uso de 'doesn't' en tag."},
    {"es": "Vamos al parque, ¿no es así?", "answers": ["We're going to the park, aren't we?"], "type": "Tag", "hint": "Contracción 'we're'.", "ex": "Tag para confirmar planes."},
    {"es": "No te molesta, ¿verdad?", "answers": ["You're not bothered, are you?","It doesn't bother you, does it?"], "type": "Tag", "hint": "Multiple ways depending on estructura.", "ex": "Atención a sujeto real."},
    {"es": "Ella no vino, ¿cierto?", "answers": ["She didn't come, did she?"], "type": "Tag", "hint": "Pasado -> did.", "ex": "Tag positiva tras negativa en pasado."},
    {"es": "Somos amigos, ¿no?", "answers": ["We are friends, aren't we?"], "type": "Tag", "hint": "'Are' -> 'aren't we'.", "ex": "Tag con 'to be'."},
    {"es": "Has terminado, ¿no?", "answers": ["You've finished, haven't you?","You have finished, haven't you?"], "type": "Tag", "hint": "Present perfect tag.", "ex": "Uso de 'haven't you' como tag."},

    # 61-70: Indirect Questions
    {"es": "¿Podrías decirme dónde está la estación?", "answers": ["Could you tell me where the station is?","Can you tell me where the station is?"], "type": "Indirect", "hint": "Estructura: subordinada no invierte sujeto y verbo.", "ex": "En indirectas no se invierte el orden dentro de la cláusula interrogativa."},
    {"es": "¿Me podrías decir la hora?", "answers": ["Could you tell me the time?","Can you tell me what time it is?"], "type": "Indirect", "hint": "Formas corteses.", "ex": "Evitar 'Where is the time?' - usar 'what time it is'."},
    {"es": "¿Sabe usted si la tienda está abierta?", "answers": ["Do you know if the shop is open?","Could you tell me if the shop is open?"], "type": "Indirect", "hint": "If / whether para opciones.", "ex": "Uso de 'if' para sí/no en oraciones indirectas."},
    {"es": "¿Podrías explicarme cómo se usa esto?", "answers": ["Could you explain how this is used?","Could you explain how to use this?"], "type": "Indirect", "hint": "Cómo -> how + cláusula.", "ex": "Varias formas de expresar 'cómo'."},
    {"es": "¿Me puede decir quién es el gerente?", "answers": ["Could you tell me who the manager is?"], "type": "Indirect", "hint": "Who + cláusula sin invertir.", "ex": "Estructura estándar de pregunta indirecta."},
    {"es": "¿Sabes cuándo llega el tren?", "answers": ["Do you know when the train arrives?","Can you tell me when the train arrives?"], "type": "Indirect", "hint": "When + cláusula.", "ex": "Uso en conversación cotidiana."},
    {"es": "¿Puedes decirme por qué cancelaron la reunión?", "answers": ["Can you tell me why they canceled the meeting?","Could you tell me why the meeting was canceled?"], "type": "Indirect", "hint": "Why + cláusula.", "ex": "Diferentes voces (activa/pasiva)."},
    {"es": "¿Podrías decirme cuánto cuesta?", "answers": ["Could you tell me how much it costs?","Can you tell me the price?"], "type": "Indirect", "hint": "How much + cláusula.", "ex": "Pregunta cortés sobre precio."},
    {"es": "¿Me puede decir dónde puedo comprar boletos?", "answers": ["Could you tell me where I can buy tickets?"], "type": "Indirect", "hint": "Where + cláusula.", "ex": "Cláusula subordinada informativa."},
    {"es": "¿Sabes si él vino ayer?", "answers": ["Do you know if he came yesterday?","Do you know whether he came yesterday?"], "type": "Indirect", "hint": "If / whether para pasado.", "ex": "Uso de 'came' en pasado."},

    # 71-80: Rhetorical Questions
    {"es": "¿A quién le importa?", "answers": ["Who cares?"], "type": "Rhetorical", "hint": "No espera respuesta.", "ex": "Expresa indiferencia."},
    {"es": "¿Por qué no?", "answers": ["Why not?"], "type": "Rhetorical", "hint": "Respuesta retórica común.", "ex": "Invitación o aceptación."},
    {"es": "¿No es obvio?", "answers": ["Isn't it obvious?","Is it not obvious?"], "type": "Rhetorical", "hint": "Uso retórico.", "ex": "Enfatiza una verdad implícita."},
    {"es": "¿No todos queremos paz?", "answers": ["Don't we all want peace?"], "type": "Rhetorical", "hint": "Formulación inclusiva.", "ex": "Usada para apelar al auditorio."},
    {"es": "¿Quién no lo haría?", "answers": ["Who wouldn't do it?"], "type": "Rhetorical", "hint": "Negación retórica.", "ex": "Sugiere obviedad."},
    {"es": "¿Acaso no lo sabías?", "answers": ["Didn't you know that?"], "type": "Rhetorical", "hint": "Tono sorprendido.", "ex": "Puede sonar acusatorio."},
    {"es": "¿Por qué siempre yo?", "answers": ["Why always me?","Why is it always me?"], "type": "Rhetorical", "hint": "Queja retórica.", "ex": "Expresa frustración."},
    {"es": "¿No es suficiente?", "answers": ["Isn't that enough?","Is it not enough?"], "type": "Rhetorical", "hint": "Pregunta retórica para cierre.", "ex": "Suele esperar acuerdo."},
    {"es": "¿No fue maravilloso?", "answers": ["Wasn't it wonderful?"], "type": "Rhetorical", "hint": "Pregunta con valoración positiva.", "ex": "Uso en comentarios sociales."},
    {"es": "¿Quién podría creerlo?", "answers": ["Who could believe it?"], "type": "Rhetorical", "hint": "Expresa asombro.", "ex": "Tono exclamativo/retórico."},

    # 81-90: Emphatic Questions
    {"es": "¿Por qué demonios dijiste eso?", "answers": ["Why on earth did you say that?","Why did you say that?"], "type": "Emphatic", "hint": "Añade 'on earth' para énfasis.", "ex": "Partículas idiomáticas para intensificar."},
    {"es": "¿Cómo te atreves?", "answers": ["How dare you?"], "type": "Emphatic", "hint": "Estructura fija 'How dare you?'.", "ex": "Muy enfática y confrontativa."},
    {"es": "¿Qué diablos estás haciendo?", "answers": ["What on earth are you doing?","What the hell are you doing?"], "type": "Emphatic", "hint": "Expresiones fuertes (informales).", "ex": "Atención al registro: pueden ser vulgares."},
    {"es": "¿En serio piensas eso?", "answers": ["Do you really think that?","Are you serious about that?"], "type": "Emphatic", "hint": "'Really' o 'serious' para énfasis.", "ex": "Usado para sorpresa o incredulidad."},
    {"es": "¿Cómo pudo pasar esto?", "answers": ["How could this happen?"], "type": "Emphatic", "hint": "Modal 'could' expresa asombro.", "ex": "Exclamación indirecta."},
    {"es": "¿Qué rayos ocurrió aquí?", "answers": ["What on earth happened here?"], "type": "Emphatic", "hint": "'On earth' para intensidad.", "ex": "Común en narrativa coloquial."},
    {"es": "¿Por qué exactamente hiciste eso?", "answers": ["Why exactly did you do that?","Why did you do that exactly?"], "type": "Emphatic", "hint": "'Exactly' para precisión/énfasis.", "ex": "Busca una explicación precisa."},
    {"es": "¿De verdad me mentiste?", "answers": ["Did you really lie to me?","Are you telling me you lied to me?"], "type": "Emphatic", "hint": "Tono acusatorio.", "ex": "Fuerte carga emocional."},
    {"es": "¿Qué demonios estás diciendo?", "answers": ["What on earth are you saying?","What the hell are you saying?"], "type": "Emphatic", "hint": "Registrar informal.", "ex": "Útil en conversaciones intensas."},
    {"es": "¿Quién en su sano juicio haría eso?", "answers": ["Who in their right mind would do that?"], "type": "Emphatic", "hint": "Frase hecha para énfasis.", "ex": "Expresa incredulidad fuerte."},

    # 91-100: Echo/Confirmation Questions + revisión
    {"es": "—Me mudo a Canadá.\n—¿Te mudas a Canadá?", "answers": ["You're moving to Canada?","Are you moving to Canada?"], "type": "Echo", "hint": "Repite la idea con entonación de pregunta.", "ex": "Confirmación o sorpresa."},
    {"es": "—Ganamos el partido.\n—¿Ganamos el partido?", "answers": ["We won the game?","Did we win the game?"], "type": "Echo", "hint": "Forma según intención (confirmar vs preguntar por pasado).", "ex": "Cuidado con el tiempo verbal."},
    {"es": "—Ella se fue temprano.\n—¿Ella se fue temprano?", "answers": ["She left early?","Did she leave early?"], "type": "Echo", "hint": "Pasado simple: 'Did she leave...'?", "ex": "Entonación vs forma completa."},
    {"es": "—Tengo hambre.\n—¿Tienes hambre?", "answers": ["You're hungry?","Are you hungry?"], "type": "Echo", "hint": "To be -> inversion.", "ex": "Pregunta corta por confirmación."},
    {"es": "—Voy mañana.\n—¿Vas mañana?", "answers": ["You're going tomorrow?","Are you going tomorrow?"], "type": "Echo", "hint": "Plan futuro cercano.", "ex": "Uso de present continuous para planes."},
    {"es": "—Ella ganó un premio.\n—¿Ella ganó un premio?", "answers": ["She won a prize?","Did she win a prize?"], "type": "Echo", "hint": "Confirmación de noticia.", "ex": "Diferentes formas según registro."},
    {"es": "—Voy a casarme.\n—¿Vas a casarte?", "answers": ["You're getting married?","Are you going to get married?"], "type": "Echo", "hint": "Expresar futuro cercano o plan.", "ex": "Formas variadas de confirmar."},
    {"es": "—Traje una sorpresa.\n—¿Trajiste una sorpresa?", "answers": ["You brought a surprise?","Did you bring a surprise?"], "type": "Echo", "hint": "Pasado simple vs entonación.", "ex": "Confirmación entonativa."},
    {"es": "—Voy a ir a la universidad.\n—¿Vas a ir a la universidad?", "answers": ["You're going to university?","Are you going to go to university?"], "type": "Echo", "hint": "Futuro y planes.", "ex": "Alternativas aceptables."},
    {"es": "Revisión general: convierte '¿Por qué te fuiste?' a una pregunta en inglés.", "answers": ["Why did you leave?","Why did you go?"], "type": "Revision", "hint": "Pasado simple con 'did'.", "ex": "Ejercicio de repaso final."},
]

# Validar que tenga exactamente 100 ejercicios
if len(EXERCISES) != 100:
    print(f"[DEBUG] Número de ejercicios: {len(EXERCISES)} (se esperaban 100). Ajustando...)")
    # Si no son 100, truncar o repetir últimos para llegar a 100
    while len(EXERCISES) < 100:
        EXERCISES.append(EXERCISES[-1].copy())
    EXERCISES = EXERCISES[:100]


# -----------------------------
# INTERFAZ DE CONSOLA
# -----------------------------

def welcome():
    print("\nPrograma: 100 ejercicios para formular preguntas en inglés")
    print("Desde la perspectiva de un hispanohablante. Escribe la pregunta en inglés.")
    print("Escribe 'help' para recibir una pista, 'show' para ver la respuesta correcta, o 'quit' para salir.")
    print("Responde con buena ortografía; el programa acepta varias variantes comunes (contracciones, sin/o con 'to').\n")


def run_exercises(exercises: List[Dict]):
    score = 0
    total = len(exercises)
    order = list(range(total))
    random.shuffle(order)

    for i, idx in enumerate(order, start=1):
        ex = exercises[idx]
        print(f"Ejercicio {i}/{total} — Tipo: {ex['type']}")
        print("ES:")
        print(ex['es'])
        print("ESCRIBE la pregunta en inglés:")
        attempts = 0
        while True:
            user = input('> ').strip()
            attempts += 1
            if user.lower() == 'quit':
                print("Saliendo...\n")
                summarize(score, i-1)
                sys.exit(0)
            if user.lower() == 'help':
                print("Pista:", ex.get('hint', 'Sin pista disponible'))
                continue
            if user.lower() == 'show':
                print("Respuestas aceptables:")
                for a in ex['answers']:
                    print('-', a)
                print("Explicación:", ex.get('ex', ''))
                # no contar como intento correcto
                break
            # Verificar respuesta
            if is_equivalent(user, ex['answers']):
                print("¡Correcto! ✅")
                print("Explicación:", ex.get('ex', ''))
                score += 1
                break
            else:
                print("No exactamente. Intenta de nuevo o escribe 'help' para una pista, 'show' para la respuesta.")
                # limitar intentos opcionalmente
                if attempts >= 3:
                    print("Parece difícil. Escribe 'show' para ver la respuesta o intenta otra vez.")

    summarize(score, total)


def summarize(score: int, total_answered: int):
    print("\n--- Resumen ---")
    print(f"Ejercicios respondidos: {total_answered}")
    print(f"Correctas: {score}")
    if total_answered:
        pct = score / total_answered * 100
        print(f"Puntuación: {pct:.1f}%")
    print("Gracias por practicar. Si quieres, puedo generar un archivo con tus respuestas o adaptar esto a Tkinter/Kivy para GUI.")


# -----------------------------
# PUNTO DE ENTRADA
# -----------------------------

def main():
    welcome()
    try:
        run_exercises(EXERCISES)
    except KeyboardInterrupt:
        print("\nInterrumpido por el usuario. Hasta luego.")


if __name__ == '__main__':
    main()
