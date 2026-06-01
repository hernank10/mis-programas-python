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
    print("📚 **TEORÍA: LA ESTRUCTURA DE UN ARGUMENTO SÓLIDO** 📚")
    print("---")
    
    print("\n1. **La Arquitectura del Razonamiento: ¿Cómo se construye un argumento sólido?** 🤔")
    print("   En grados anteriores, aprendimos que una opinión necesita razones (argumentos) y pruebas (evidencias). Ahora, vamos a darle una **estructura formal** a esas ideas, algo esencial para ensayos, debates y cualquier texto persuasivo.")
    print("   Piensa en un argumento como un edificio bien construido: necesita un plano principal (la tesis), pilares fuertes (los argumentos de apoyo) y un buen techo que lo cierre (la conclusión).")
    esperar()

    print("\n2. **La TESIS: El Corazón de tu Argumento** ❤️")
    print("   La **TESIS** es la **idea central, la postura principal** que quieres defender o probar en tu texto. ¡Es la afirmación clave sobre la que girará toda tu argumentación!")
    print("   - Debe ser una oración **completa, clara, específica y debatible** (alguien podría estar en desacuerdo).")
    print("   - **❌ Mal ejemplo de Tesis:** 'Los animales son importantes.' (Demasiado general, no debatible).")
    print("   - **✅ Buen ejemplo de Tesis:** 'La implementación de programas de reciclaje obligatorio es crucial para la sostenibilidad ambiental urbana.' (Clara, específica, se puede debatir).")
    esperar()

    print("\n3. **ARGUMENTOS DE APOYO: Los Pilares del Razonamiento** 💪")
    print("   Los **ARGUMENTOS DE APOYO** son las **razones principales** que utilizas para sustentar tu tesis. Cada argumento de apoyo es una afirmación que, si se prueba con evidencias, fortalece tu tesis.")
    print("   - Piensa en ellos como los 'porqués' de tu tesis. Puedes usar argumentos lógicos, de autoridad o de experiencia.")
    print("   - **Ejemplo (para la tesis 'La implementación de programas de reciclaje obligatorio es crucial para la sostenibilidad ambiental urbana'):**")
    print("     - **Argumento 1:** 'Reduce significativamente la cantidad de residuos que llegan a los vertederos.'")
    print("     - **Argumento 2:** 'Fomenta la economía circular al dar nueva vida a los materiales.'")
    print("     - **Argumento 3:** 'Disminuye el consumo de recursos naturales y la energía necesaria para producir nuevos materiales.'")
    print("   - ¡Recuerda! Cada argumento de apoyo debe ser, a su vez, sustentado con **evidencias** (datos, ejemplos, citas de expertos).")
    esperar()

    print("\n4. **La CONCLUSIÓN: Cerrando con Fuerza** 💥")
    print("   La **CONCLUSIÓN** es la parte final de tu argumentación donde **reafirmas tu tesis principal** de una manera fresca y convincente. A veces, también puedes resumir brevemente tus argumentos más importantes.")
    print("   - No es solo repetir la tesis al pie de la letra, sino darle un cierre que deje una impresión duradera en el lector/oyente.")
    print("   - **Ejemplo (para la tesis de reciclaje):** 'En resumen, considerando la reducción de residuos, el impulso a la economía circular y la conservación de recursos, resulta innegable que la obligatoriedad del reciclaje es una medida fundamental para asegurar un futuro urbano más sostenible y responsable.'")
    print("   - La conclusión debe dejar al público con una idea clara y reforzada de tu postura.")
    esperar(limpiar=True)

def mostrar_ejemplos():
    limpiar_consola()
    print("💡 **EJEMPLOS: ARGUMENTOS SÓLIDOS EN ACCIÓN** 💡")
    print("---")

    print("\n**Ejemplo 1: La importancia de aprender un segundo idioma.**")
    print(" - **TESIS:** Aprender un segundo idioma desde la infancia ofrece beneficios cognitivos y culturales invaluables para los estudiantes.")
    print(" - **ARGUMENTO DE APOYO 1:** Mejora las habilidades cognitivas como la resolución de problemas y la multitarea.")
    print(" - **ARGUMENTO DE APOYO 2:** Permite una mayor apreciación y comprensión de diferentes culturas y perspectivas.")
    print(" - **CONCLUSIÓN:** Por lo tanto, integrar la enseñanza de un segundo idioma desde temprana edad es esencial para desarrollar mentes más ágiles y ciudadanos globales más empáticos.")
    esperar()

    print("\n**Ejemplo 2: ¿Deberían prohibirse los deberes escolares en primaria?**")
    print(" - **TESIS:** Prohibir los deberes escolares en la educación primaria beneficiaría el bienestar y el desarrollo integral de los niños.")
    print(" - **ARGUMENTO DE APOYO 1:** Reduce el estrés y la presión académica excesiva en los niños pequeños.")
    print(" - **ARGUMENTO DE APOYO 2:** Permite más tiempo para actividades extracurriculares, juego libre y tiempo en familia.")
    print(" - **CONCLUSIÓN:** En consecuencia, al eliminar los deberes en primaria, se fomenta un equilibrio más saludable entre la vida escolar y personal de los niños, promoviendo un desarrollo más completo y feliz.")
    esperar(limpiar=True)

def realizar_ejercicios():
    limpiar_consola()
    print("📝 **EJERCICIOS: ¡IDENTIFICA LA ESTRUCTURA DEL ARGUMENTO!** 📝")
    print("---")
    print("Lee cada pasaje y di si la frase destacada es la **TESIS**, un **ARGUMENTO DE APOYO** o la **CONCLUSIÓN**.")
    esperar("¡Manos a la obra!")

    ejercicios = [
        {"pasaje": "Es vital que los gobiernos inviertan más en energía solar. **Esta fuente de energía es limpia y renovable.** Además, reduce la dependencia de los combustibles fósiles. Por todo esto, la inversión en energía solar es una prioridad.", "destacado": "Esta fuente de energía es limpia y renovable.", "respuesta": "argumento de apoyo", "pista": "Es una razón que defiende la inversión en energía solar."},
        {"pasaje": "**Los videojuegos desarrollan habilidades de resolución de problemas en los jóvenes.** Esto se debe a que muchos juegos requieren estrategia y pensamiento crítico. Además, fomentan la creatividad al permitir la construcción de mundos virtuales. Por tanto, su potencial educativo es innegable.", "destacado": "Los videojuegos desarrollan habilidades de resolución de problemas en los jóvenes.", "respuesta": "tesis", "pista": "Es la idea principal que se va a defender en el texto."},
        {"pasaje": "La prohibición de los plásticos de un solo uso es crucial. **Ayuda a proteger la vida marina y los ecosistemas acuáticos.** También disminuye la acumulación de basura. En definitiva, esta medida es fundamental para la salud de nuestro planeta.", "destacado": "Ayuda a proteger la vida marina y los ecosistemas acuáticos.", "respuesta": "argumento de apoyo", "pista": "Es una razón específica para la prohibición de plásticos."},
        {"pasaje": "El voluntariado en la comunidad trae grandes beneficios. Fomenta el sentido de pertenencia y mejora la autoestima. **En resumen, participar en actividades de voluntariado es una forma efectiva de construir una sociedad más solidaria y un bienestar personal.**", "destacado": "En resumen, participar en actividades de voluntariado es una forma efectiva de construir una sociedad más solidaria y un bienestar personal.", "respuesta": "conclusion", "pista": "Es la frase que cierra y resume la idea principal."},
        {"pasaje": "**El aprendizaje de idiomas extranjeros debería ser obligatorio desde la escuela primaria.** Esto se debe a que mejora la agilidad mental. También abre puertas a oportunidades culturales y laborales. Por ende, es una inversión a largo plazo.", "destacado": "El aprendizaje de idiomas extranjeros debería ser obligatorio desde la escuela primaria.", "respuesta": "tesis", "pista": "Es la afirmación principal que se defiende."},
        {"pasaje": "El uso excesivo de redes sociales puede tener efectos negativos en la salud mental de los adolescentes. **Puede aumentar sentimientos de ansiedad y depresión.** Además, distorsiona la percepción de la realidad. En conclusión, es necesario un uso consciente.", "destacado": "Puede aumentar sentimientos de ansiedad y depresión.", "respuesta": "argumento de apoyo", "pista": "Es una de las razones que explican los efectos negativos."},
        {"pasaje": "La lectura regular es fundamental para el desarrollo intelectual. Amplía el vocabulario y mejora la comprensión. **Por lo tanto, fomentar el hábito de la lectura desde temprana edad es crucial para formar individuos críticos y bien informados.**", "destacado": "Por lo tanto, fomentar el hábito de la lectura desde temprana edad es crucial para formar individuos críticos y bien informados.", "respuesta": "conclusion", "pista": "La frase final que resume y concluye el argumento."},
        {"pasaje": "**La educación pública de calidad es un pilar fundamental para el progreso de una nación.** Garantiza igualdad de oportunidades para todos los ciudadanos. Además, invierte en el capital humano del país. Por estas razones, es una prioridad.", "destacado": "La educación pública de calidad es un pilar fundamental para el progreso de una nación.", "respuesta": "tesis", "pista": "Es la afirmación central que se argumenta."},
        {"pasaje": "El transporte público eficiente es vital para las grandes ciudades. **Reduce la congestión del tráfico y la contaminación del aire.** También es más económico para los ciudadanos. En definitiva, mejora la calidad de vida urbana.", "destacado": "Reduce la congestión del tráfico y la contaminación del aire.", "respuesta": "argumento de apoyo", "pista": "Es una razón específica por la que el transporte público es vital."},
        {"pasaje": "El arte debe ser accesible para todos. Promueve la creatividad y la expresión personal. **En consecuencia, las políticas públicas deben asegurar el acceso universal a museos y exposiciones.**", "destacado": "En consecuencia, las políticas públicas deben asegurar el acceso universal a museos y exposiciones.", "respuesta": "conclusion", "pista": "Sintetiza la idea y propone una acción basada en los argumentos."},
        
        # Más ejercicios para completar los 20
        {"pasaje": "**El voluntariado debería ser una actividad obligatoria en la secundaria.** Fomenta la empatía y la responsabilidad social. Además, permite a los jóvenes adquirir nuevas habilidades. Su impacto positivo es evidente.", "destacado": "El voluntariado debería ser una actividad obligatoria en la secundaria.", "respuesta": "tesis", "pista": "Es la postura principal del argumento."},
        {"pasaje": "Invertir en tecnología educativa en las aulas es esencial. **Prepara a los estudiantes para el mundo digital del futuro.** También personaliza el aprendizaje. Por ende, modernizar las herramientas es clave.", "destacado": "Prepara a los estudiantes para el mundo digital del futuro.", "respuesta": "argumento de apoyo", "pista": "Es una razón que apoya la inversión en tecnología."},
        {"pasaje": "El deporte profesional fomenta valores positivos. **Inspira a la juventud a llevar vidas activas y saludables.** Genera trabajo y promueve el turismo deportivo. Claramente, su impacto social es significativo.", "destacado": "Inspira a la juventud a llevar vidas activas y saludables.", "respuesta": "argumento de apoyo", "pista": "Es una razón específica de los beneficios del deporte."},
        {"pasaje": "Las dietas veganas son una opción sostenible y ética. **Reducen la huella de carbono y el consumo de agua asociado a la ganadería.** Además, evitan el maltrato animal. Por eso, son una elección consciente.", "destacado": "Reducen la huella de carbono y el consumo de agua asociado a la ganadería.", "respuesta": "argumento de apoyo", "pista": "Es una razón específica para la sostenibilidad."},
        {"pasaje": "La pena de muerte no es una medida justa ni efectiva. No disuade el crimen y es irreversible en caso de error. **Por lo tanto, se deben buscar alternativas que promuevan la justicia restaurativa y la rehabilitación.**", "destacado": "Por lo tanto, se deben buscar alternativas que promuevan la justicia restaurativa y la rehabilitación.", "respuesta": "conclusion", "pista": "Es la frase final que propone una acción o reafirma la postura."},
        {"pasaje": "**El acceso a internet debería ser considerado un derecho humano básico.** Permite el acceso a la información y la educación. También facilita la comunicación y la participación ciudadana. Su universalidad es vital.", "destacado": "El acceso a internet debería ser considerado un derecho humano básico.", "respuesta": "tesis", "pista": "Es la afirmación principal que se defiende."},
        {"pasaje": "La crisis climática requiere acciones urgentes. **Las emisiones de gases de efecto invernadero están calentando el planeta a un ritmo alarmante.** Esto está causando desastres naturales más frecuentes. Es imperativo actuar ya.", "destacado": "Las emisiones de gases de efecto invernadero están calentando el planeta a un ritmo alarmante.", "respuesta": "argumento de apoyo", "pista": "Es una razón que explica por qué la crisis es urgente."},
        {"pasaje": "La robótica avanzada traerá grandes cambios al mercado laboral. **Creará nuevos empleos en áreas de tecnología y mantenimiento.** Sin embargo, también automatizará tareas repetitivas. En suma, requerirá una adaptación constante.", "destacado": "Creará nuevos empleos en áreas de tecnología y mantenimiento.", "respuesta": "argumento de apoyo", "pista": "Es una de las razones sobre el impacto de la robótica."},
        {"pasaje": "Es fundamental que las ciudades promuevan espacios verdes. **Mejoran la calidad del aire y reducen el estrés de los ciudadanos.** Además, fomentan la biodiversidad. En definitiva, son esenciales para el bienestar urbano.", "destacado": "Mejoran la calidad del aire y reducen el estrés de los ciudadanos.", "respuesta": "argumento de apoyo", "pista": "Es una de las razones que justifican la importancia de los espacios verdes."},
        {"pasaje": "La inteligencia artificial tiene el potencial de revolucionar la medicina. Puede ayudar a diagnosticar enfermedades con mayor precisión y a desarrollar nuevos tratamientos. **En conclusión, la IA es una herramienta prometedora para el futuro de la salud.**", "destacado": "En conclusión, la IA es una herramienta prometedora para el futuro de la salud.", "respuesta": "conclusion", "pista": "La frase final que resume y reafirma el potencial de la IA."},
    ]

    puntuacion = 0
    
    random.shuffle(ejercicios) # Mezclar ejercicios

    for i, ej in enumerate(ejercicios):
        print(f"\n--- Ejercicio {i+1}/20 ---")
        print(f"Pasaje: \"{ej['pasaje']}\"")
        print(f"Frase destacada: \"{ej['destacado']}\"")
        
        valido = False
        while not valido:
            respuesta_usuario = input("¿Qué parte de la estructura argumentativa es? (TESIS / ARGUMENTO DE APOYO / CONCLUSIÓN): ").strip().lower()
            if respuesta_usuario in ["tesis", "argumento de apoyo", "conclusion"]:
                valido = True
            else:
                print("Por favor, responde con 'TESIS', 'ARGUMENTO DE APOYO' o 'CONCLUSIÓN'.")

        if respuesta_usuario == ej['respuesta'].lower():
            print("✅ ¡Correcto! ¡Identificaste bien esa parte!")
            puntuacion += 1
        else:
            print(f"❌ ¡Incorrecto! La respuesta correcta era: '{ej['respuesta'].upper()}'.")
            print(f"Pista: {ej['pista']}")
        
        esperar()

    limpiar_consola()
    print("--- ¡FIN DE LOS EJERCICIOS! ---")
    print(f"\nHas completado los ejercicios. ¡Tu puntuación final es: {puntuacion}/{len(ejercicios)}!")
    if puntuacion >= 16:
        print("🎉 ¡Felicidades! ¡Eres un arquitecto de argumentos sólidos!")
    elif puntuacion >= 10:
        print("👍 ¡Muy bien! Ya entiendes las partes clave de un argumento.")
    else:
        print("✍️ ¡Sigue practicando! Con más esfuerzo, ¡estructurarás tus ideas como un experto!")
    esperar(limpiar=True)


def construir_argumento_completo():
    limpiar_consola()
    print("✍️ **¡CONSTRUYE TU PROPIO ARGUMENTO COMPLETO!** ✍️")
    print("---")
    print("Ahora es tu turno de construir un argumento sólido con todas sus partes.")
    print("Piensa en un tema que te interese y sobre el que tengas una postura clara.")
    esperar("¡Manos a la obra!")

    argumento_completo = {}
    
    print("\n--- PASO 1: Define tu TESIS (Postura Principal) ---")
    print("¿Qué quieres defender o probar en una oración clara y específica?")
    argumento_completo["tesis"] = input("Tu Tesis: ").strip()
    
    print(f"\n--- PASO 2: Escribe tus ARGUMENTOS DE APOYO (Mínimo 2) ---")
    print("¿Cuáles son las razones principales que sustentan tu tesis?")
    argumento_completo["argumento1"] = input("Argumento de Apoyo 1: ").strip()
    argumento_completo["argumento2"] = input("Argumento de Apoyo 2: ").strip()
    
    print("\n--- PASO 3: Redacta tu CONCLUSIÓN ---")
    print("Reafirma tu tesis y cierra tu argumento de manera convincente.")
    argumento_completo["conclusion"] = input("Tu Conclusión: ").strip()

    limpiar_consola()
    print("--- ¡TU ARGUMENTO CONSTRUIDO! ---")
    print("\nAquí está el argumento sólido que has creado:")
    print(f"\n**TESIS:** {argumento_completo['tesis']}")
    print(f"  **ARGUMENTO 1:** {argumento_completo['argumento1']}")
    print(f"  **ARGUMENTO 2:** {argumento_completo['argumento2']}")
    print(f"  **CONCLUSIÓN:** {argumento_completo['conclusion']}")
    
    print("\n¡Excelente trabajo diseñando la arquitectura de tus propias ideas!")
    esperar(limpiar=True)


def mostrar_menu():
    while True:
        limpiar_consola()
        print("--- MENÚ DE LA LECCIÓN 6: ARGUMENTOS SÓLIDOS (10.º Grado) ---")
        print("\n1. Teoría (¡Aprendemos la arquitectura de un argumento!)")
        print("2. Ejemplos (¡Vemos argumentos bien estructurados!)")
        print("3. Ejercicios (¡A identificar las partes del argumento!)")
        print("4. Construye Tu Propio Argumento Completo (¡Crea tus propias ideas sólidas!)")
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
            construir_argumento_completo()
        elif opcion == '5':
            print("\n¡Gracias por aprender a construir argumentos sólidos! ¡Tu capacidad de persuasión será increíble!")
            sys.exit()
        else:
            print("\nOpción no válida. Por favor, elige un número del 1 al 5.")
            esperar()

# Iniciar la aplicación
if __name__ == "__main__":
    mostrar_menu()
