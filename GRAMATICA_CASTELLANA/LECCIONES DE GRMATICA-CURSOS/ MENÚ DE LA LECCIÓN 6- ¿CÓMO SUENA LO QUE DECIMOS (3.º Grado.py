import time
import random
import sys

def limpiar_consola():
    """Simula la limpieza de la consola (funciona mejor en entornos de terminal)."""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def esperar(mensaje="Presiona Enter para continuar...", limpiar=False):
    """Pausa la ejecución para que el usuario pueda leer."""
    input(f"\n{mensaje}")
    if limpiar:
        limpiar_consola()

def mostrar_teoria():
    limpiar_consola()
    print("📚 **TEORÍA: ¿CÓMO SUENA LO QUE DECIMOS? ENTINACIÓN Y SIGNOS** 📚")
    print("---")
    
    print("\n1. **El Tono Mágico de Nuestra Voz: La Entonación**")
    print("   Cuando hablamos, nuestra voz tiene una **música especial** llamada **entonación**. Nos dice si estamos contentos, tristes, preguntando o simplemente contando algo.")
    print("   - Intenta decir 'Es tarde' con voz de sorpresa: ¡Es tarde!")
    print("   - Ahora, di 'Es tarde' como si fuera una pregunta: ¿Es tarde?")
    print("   - Y ahora, solo contando: Es tarde.")
    print("   ¡La misma frase, pero suena diferente!")
    esperar()

    print("\n2. **Los Signos de Puntuación: Las Notas Musicales de la Escritura**")
    print("   Cuando escribimos, no podemos usar nuestra voz. ¡Por eso tenemos los **signos de puntuación**!")
    print("   Son como las notas musicales que le dicen al que lee cómo debe sonar lo que escribimos.")
    esperar()

    print("\n3. **El Punto (.) ¡Para Terminar una Idea!**")
    print("   El **punto (.)** se usa al final de una oración cuando **contamos algo** o damos información. Es como una pequeña pausa para tomar aire.")
    print("   - Tu voz baja un poquito al final.")
    print("   - Ejemplo: 'El sol brilla en el cielo.'")
    print("   - Ejemplo: 'Mi perro juega con la pelota.'")
    esperar()

    print("\n4. **Los Signos de Interrogación (¿?) ¡Para Hacer Preguntas!**")
    print("   Ya los conoces. Los **signos de interrogación (¿?)** se usan para **hacer preguntas**.")
    print("   - Tu voz sube un poquito al final.")
    print("   - Siempre van uno al principio (¿) y otro al final (?).")
    print("   - Ejemplo: '¿Qué hora es?'")
    print("   - Ejemplo: '¿Cuándo vamos al parque?'")
    esperar()

    print("\n5. **Los Signos de Exclamación (¡!) ¡Para Sentir Emoción!**")
    print("   Los **signos de exclamación (¡!)** se usan cuando queremos expresar una **emoción fuerte**: alegría, sorpresa, miedo, enojo, o cuando damos una orden.")
    print("   - Tu voz suena más fuerte o más emocionada.")
    print("   - Siempre van uno al principio (¡) y otro al final (!).")
    print("   - Ejemplo: '¡Qué alegría verte!'")
    print("   - Ejemplo: '¡Cuidado con el escalón!'")
    esperar(limpiar=True)

def mostrar_ejemplos():
    limpiar_consola()
    print("💡 **EJEMPLOS DE ORACIONES CON SU MÚSICA** 💡")
    print("---")

    print("\n**Oraciones con Punto (.):** (Voz normal, contando algo)")
    print(" - La tortuga es lenta.")
    print(" - Mañana iré al colegio.")
    print(" - Las flores son bonitas.")
    esperar()

    print("\n**Oraciones con Signos de Interrogación (¿?):** (Voz de pregunta)")
    print(" - ¿Me acompañas al cine?")
    print(" - ¿Cuántos años tienes?")
    print(" - ¿Dónde está tu mochila?")
    esperar()

    print("\n**Oraciones con Signos de Exclamación (¡!):** (Voz con emoción)")
    print(" - ¡Feliz cumpleaños!")
    print(" - ¡Qué delicioso pastel!")
    print(" - ¡Auxilio, un ratón!")
    esperar(limpiar=True)

def realizar_ejercicios():
    limpiar_consola()
    print("📝 **EJERCICIOS: ¡PONIENDO LOS SIGNOS CORRECTOS!** 📝")
    print("---")
    print("¡Lee cada frase y elige el signo correcto (punto, interrogación o exclamación)!")
    print("Escribe: '.' para punto, '?' para interrogación, '!' para exclamación.")
    esperar("¡Empecemos!")

    ejercicios = [
        # Elegir el signo correcto (10 ejercicios)
        {"consigna": "Qué divertido es jugar", "respuesta": "!", "contexto": "Cuando algo es muy divertido, ¡lo exclamamos!", "tipo": "Exclamación"},
        {"consigna": "El perro duerme en su casa", "respuesta": ".", "contexto": "Estamos contando dónde duerme el perro.", "tipo": "Punto"},
        {"consigna": "Qué hora es", "respuesta": "?", "contexto": "Queremos saber la hora.", "tipo": "Interrogación"},
        {"consigna": "Cuidado con el vidrio", "respuesta": "!", "contexto": "Es una advertencia o una sorpresa.", "tipo": "Exclamación"},
        {"consigna": "Te gusta el chocolate", "respuesta": "?", "contexto": "Queremos saber si le gusta.", "tipo": "Interrogación"},
        {"consigna": "Mi mamá es la mejor", "respuesta": "!", "contexto": "Es una expresión de cariño y admiración.", "tipo": "Exclamación"},
        {"consigna": "El cielo es azul", "respuesta": ".", "contexto": "Es una descripción, estamos contando un hecho.", "tipo": "Punto"},
        {"consigna": "Vienes a mi fiesta", "respuesta": "?", "contexto": "Es una invitación que pregunta.", "tipo": "Interrogación"},
        {"consigna": "Qué sorpresa verte", "respuesta": "!", "contexto": "Expresamos asombro.", "tipo": "Exclamación"},
        {"consigna": "Tengo un gato negro", "respuesta": ".", "contexto": "Estamos informando sobre nuestra mascota.", "tipo": "Punto"},
        
        # Escribir la oración completa con signos (10 ejercicios)
        {"consigna": "Cómo te sientes (pregunta)", "respuesta": "¿cómo te sientes?", "feedback": "Recuerda los signos al principio y al final."},
        {"consigna": "Qué susto me diste (emoción)", "respuesta": "¡qué susto me diste!", "feedback": "¡Ponle la emoción correcta con sus signos!"},
        {"consigna": "El pájaro canta en el árbol (contar)", "respuesta": "el pájaro canta en el árbol.", "feedback": "Solo una información, usa el punto."},
        {"consigna": "Quién llamó a la puerta (pregunta)", "respuesta": "¿quién llamó a la puerta?", "feedback": "Es para saber la identidad."},
        {"consigna": "Mira qué lindo (emoción)", "respuesta": "¡mira qué lindo!", "feedback": "Expresa admiración."},
        {"consigna": "Hoy es viernes (contar)", "respuesta": "hoy es viernes.", "feedback": "Simplemente informa el día."},
        {"consigna": "A dónde vas (pregunta)", "respuesta": "¿a dónde vas?", "feedback": "Pregunta por el lugar."},
        {"consigna": "Increíble (emoción)", "respuesta": "¡increíble!", "feedback": "Es una exclamación de asombro."},
        {"consigna": "Tengo hambre (contar)", "respuesta": "tengo hambre.", "feedback": "Solo una información."},
        {"consigna": "Es verdad (pregunta)", "respuesta": "¿es verdad?", "feedback": "Para verificar algo."},
    ]

    puntuacion = 0
    random.shuffle(ejercicios) # Mezclar ejercicios

    for i, ejercicio in enumerate(ejercicios):
        print(f"\n--- Ejercicio {i+1}/20 ---")
        print(f"Consigna: {ejercicio['consigna']}")
        
        es_correcta = False
        if ejercicio["tipo"] in ["Exclamación", "Punto", "Interrogación"]: # Ejercicios de elegir el signo
            respuesta_usuario = input("Escribe el signo correcto (., ?, !): ").strip()
            if respuesta_usuario == ejercicio['respuesta']:
                es_correcta = True
        else: # Ejercicios de escribir la oración completa
            respuesta_usuario = input("Escribe la oración completa con sus signos: ").strip().lower()
            if respuesta_usuario == ejercicio['respuesta']:
                es_correcta = True

        if es_correcta:
            print("✅ ¡Perfecto! ¡Correcto!")
            puntuacion += 1
        else:
            print(f"❌ ¡Intenta de nuevo!")
            print(f"La respuesta correcta era: \"{ejercicio['respuesta']}\"")
            if "contexto" in ejercicio:
                print(f"Pista: {ejercicio['contexto']}")
            elif "feedback" in ejercicio:
                print(f"Pista: {ejercicio['feedback']}")
        esperar()

    limpiar_consola()
    print("--- ¡FIN DE LOS EJERCICIOS! ---")
    print(f"\nHas completado los ejercicios. ¡Tu puntuación final es: {puntuacion}/{len(ejercicios)}!")
    if puntuacion >= 16:
        print("🎉 ¡Excelente! ¡Eres un director de orquesta de la puntuación!")
    elif puntuacion >= 10:
        print("👍 ¡Muy bien! Ya sabes cómo darle la 'música' a tus oraciones.")
    else:
        print("✍️ ¡No te preocupes! Sigue practicando los signos, ¡lo lograrás!")
    esperar(limpiar=True)

def crear_ejemplos_propios():
    limpiar_consola()
    print("✍️ **¡CREA TUS PROPIAS ORACIONES CON MÚSICA!** ✍️")
    print("---")
    print("¡Vamos a inventar 20 oraciones con puntos, preguntas y exclamaciones!")
    print("Recuerda los signos correctos: .  ¿?  ¡!")
    esperar("¡Empecemos a crear!")

    ejemplos_propios = []
    tipos_oracion = [
        "una oración que cuente algo (con .)", "una oración que pregunte algo (con ¿?)", "una oración que exclame algo (con ¡!)",
        "una oración que cuente algo (con .)", "una oración que pregunte algo (con ¿?)", "una oración que exclame algo (con ¡!)",
        "una oración que cuente algo (con .)", "una oración que pregunte algo (con ¿?)", "una oración que exclame algo (con ¡!)",
        "una oración que cuente algo (con .)", "una oración que pregunte algo (con ¿?)", "una oración que exclame algo (con ¡!)",
        "una oración que cuente algo (con .)", "una oración que pregunte algo (con ¿?)", "una oración que exclame algo (con ¡!)",
        "una oración que cuente algo (con .)", "una oración que pregunte algo (con ¿?)", "una oración que exclame algo (con ¡!)",
        "una oración que cuente algo (con .)", "una oración que pregunte algo (con ¿?)", # Los últimos dos para completar 20
    ]

    for i in range(20):
        print(f"\nEjemplo {i+1}/20: Escribe {tipos_oracion[i]}:")
        ejemplo = input("Tu oración: ").strip()
        ejemplos_propios.append(f"{i+1}. {ejemplo} ({tipos_oracion[i].split('(')[1].replace(')', '')})") # Solo el tipo de signo
        print("¡Guardada!")

    limpiar_consola()
    print("--- ¡TUS ORACIONES INVENTADAS! ---")
    print("\nAquí están tus 20 oraciones:")
    for ejemplo in ejemplos_propios:
        print(ejemplo)
    print("\n¡Magnífico trabajo creando tus propias oraciones! ¡Ahora tienen la música correcta!")
    esperar(limpiar=True)

def mostrar_menu():
    while True:
        limpiar_consola()
        print("--- MENÚ DE LA LECCIÓN 6: ¿CÓMO SUENA LO QUE DECIMOS? (3.º Grado Primaria) ---")
        print("\n1. Teoría (¡Aprendemos sobre la música de las palabras!)")
        print("2. Ejemplos (¡Vemos oraciones con su sonido!)")
        print("3. Ejercicios (¡A practicar los signos!)")
        print("4. Crear Mis Propias Oraciones (¡Inventa tus frases con música!)")
        print("5. Salir")
        print("---")

        opcion = input("Elige una opción (1-5): ").strip()

        if opcion == '1':
            mostrar_teoria()
        elif opcion == '2':
            mostrar_ejemplos()
        elif opcion == '3':
            realizar_ejercicios()
        elif opcion == '4':
            crear_ejemplos_propios()
        elif opcion == '5':
            print("\n¡Gracias por aprender sobre la puntuación! ¡Nos vemos pronto!")
            sys.exit()
        else:
            print("\nOpción no válida. Por favor, elige un número del 1 al 5.")
            esperar()

# Iniciar la aplicación
if __name__ == "__main__":
    mostrar_menu()
