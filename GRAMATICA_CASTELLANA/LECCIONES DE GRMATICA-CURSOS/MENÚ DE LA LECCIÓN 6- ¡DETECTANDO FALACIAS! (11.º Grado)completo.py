import random
import sys
import time

def limpiar_consola():
    """Simula la limpieza de la consola (funciona mejor en entornos de terminal)."""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def esperar(mensaje="Presiona Enter para continuar...", limpiar=False):
    """Pausa la ejecución para que el usuario pueda leer."""
    input(f"\n{mensaje}")
    if limpiar:
        limpiar_consola()

# --- Funciones existentes (Teoría, Ejemplos, Ejercicios de Identificación, Práctica de Refutación) ---

def mostrar_teoria():
    limpiar_consola()
    print("📚 **TEORÍA: ARGUMENTOS DESHONESTOS - FALACIAS COMUNES** 📚")
    print("---")
    
    print("\n1. **El Poder y los Peligros de la Persuasión** 🤔")
    print("   Ya sabemos cómo construir argumentos sólidos. Pero, ¿qué pasa cuando alguien intenta convencernos usando trucos o razonamientos defectuosos? A esto le llamamos **falacias**.")
    print("   Una **falacia** es un argumento que parece válido o convincente a primera vista, pero que en realidad esconde un **error lógico** o una intención de engañar. Identificarlas es crucial para nuestro pensamiento crítico.")
    esperar()

    print("\n2. **Explorando Falacias Comunes** 🚨")

    print("\n   **a. Ad Hominem (Ataque Personal):**")
    print("      - **Explicación:** Atacar a la **persona** que presenta el argumento, en lugar de refutar el argumento mismo.")
    print("      - **Ejemplo:** 'No podemos creer lo que dice el científico sobre el cambio climático; ¡él solo busca fama!' (En lugar de discutir sus datos o teorías).")
    esperar()

    print("\n   **b. Ad Populum (Apelación a la Popularidad o al Pueblo):**")
    print("      - **Explicación:** Afirmar que algo es verdadero o correcto solo porque **muchas personas lo creen o lo hacen**. La popularidad no es prueba de verdad.")
    print("      - **Ejemplo:** 'Millones de personas usan esta red social, así que debe ser la mejor para conectar con amigos.' (La popularidad no garantiza que sea la 'mejor' para todos o que sea segura).")
    esperar()

    print("\n   **c. Falsa Causa (Post Hoc, Ergo Propter Hoc):**")
    print("      - **Explicación:** Suponer que porque un evento ocurrió **después** de otro, el primero debe ser la **causa** del segundo. (Correlación no implica causalidad).")
    print("      - **Ejemplo:** 'Desde que prohibieron los patinetes eléctricos en el parque, ha llovido más. La prohibición causó el mal tiempo.' (Absurdo, pero ilustra la idea).")
    esperar()

    print("\n   **d. Generalización Apresurada:**")
    print("      - **Explicación:** Llegar a una **conclusión general basándose en evidencia insuficiente** o en muy pocos casos particulares.")
    print("      - **Ejemplo:** 'Probé un plato de comida de este restaurante y no me gustó; toda su comida debe ser horrible.' (Un solo plato no define la calidad de todo el menú).")
    esperar()

    print("\n   **e. Petición de Principio (Argumento Circular):**")
    print("      - **Explicación:** La **conclusión del argumento ya está implícita o explícitamente contenida en una de las premisas**. Se asume como verdad lo que se quiere probar.")
    print("      - **Ejemplo:** 'El ejercicio físico es bueno porque mejora la salud. Y ¿por qué mejora la salud? Porque es bueno hacer ejercicio.' (No se añade información, se repite la idea).")
    esperar()

    print("\n   **f. Hombre de Paja:**")
    print("      - **Explicación:** **Distorsionar, exagerar o crear una versión débil** del argumento del oponente para que sea más fácil de atacar o refutar, en lugar de debatir la postura real.")
    print("      - **Ejemplo:**")
    print("         - **Persona A:** 'Deberíamos invertir en energías renovables para un futuro más sostenible.'")
    print("         - **Persona B:** 'Ah, ¿así que quieres destruir nuestra economía y dejar a miles de personas sin trabajo en la industria petrolera? ¡Eso es irresponsable!' (B distorsiona la propuesta de A).")
    esperar()

    print("\n   **g. Pendiente Resbaladiza:**")
    print("      - **Explicación:** Afirmar que una **acción inicial inevitablemente conducirá a una serie de consecuencias negativas y extremas**, sin suficiente evidencia para cada paso de la cadena.")
    print("      - **Ejemplo:** 'Si permitimos que los estudiantes usen teléfonos en el aula, pronto no prestarán atención, sus notas bajarán, abandonarán la escuela y terminarán sin futuro.' (Una cadena de eventos exagerada e infundada).")
    esperar()

    print("\n   **h. Ad Ignorantiam (Apelación a la Ignorancia):**")
    print("      - **Explicación:** Afirmar que algo es verdadero porque **no se ha probado que sea falso**, o viceversa. La ausencia de prueba no es una prueba.")
    print("      - **Ejemplo:** 'Nadie ha podido demostrar que los ovnis no nos visitan, por lo tanto, las visitas extraterrestres son una realidad.' (La falta de evidencia en contra no prueba que sea cierto).")
    esperar(limpiar=True)

def mostrar_ejemplos():
    limpiar_consola()
    print("💡 **EJEMPLOS: ¡IDENTIFICANDO FALACIAS!** 💡")
    print("---")

    print("\n**Ejemplo 1:** 'No podemos confiar en la opinión del Dr. López sobre la vacuna, ¡él siempre ha sido un poco excéntrico y vive aislado!'")
    print(" - **Tipo de Falacia:** **Ad Hominem**. Se ataca la personalidad del Dr. López, no la validez de su argumento sobre la vacuna.")
    esperar()

    print("\n**Ejemplo 2:** 'Todo el mundo en mi clase piensa que las clases a las 7 AM son una tortura, así que deben eliminarlas del horario escolar.'")
    print(" - **Tipo de Falacia:** **Ad Populum**. La opinión popular de un grupo (la clase) no justifica una medida educativa.")
    esperar()

    print("\n**Ejemplo 3:** 'Después de que mi equipo de fútbol empezó a usar uniformes verdes, ganaron todos sus partidos. ¡Los uniformes verdes les dan suerte!'")
    print(" - **Tipo de Falacia:** **Falsa Causa**. Se asume que el color del uniforme es la causa de las victorias sin una conexión lógica real.")
    esperar()

    print("\n**Ejemplo 4:** 'Conocí a dos políticos que eran corruptos, por lo tanto, todos los políticos son corruptos.'")
    print(" - **Tipo de Falacia:** **Generalización Apresurada**. Se saca una conclusión general sobre una profesión entera basándose en solo dos ejemplos.")
    esperar()

    print("\n**Ejemplo 5:** 'La libertad de expresión es fundamental porque es esencial para una sociedad libre.'")
    print(" - **Tipo de Falacia:** **Petición de Principio**. La conclusión ('es esencial para una sociedad libre') es básicamente una reafirmación de la premisa ('la libertad de expresión es fundamental'). No se aporta nueva información.")
    esperar()

    print("\n**Ejemplo 6:**")
    print("  - **Persona A:** 'Deberíamos considerar implementar un sistema de transporte público más robusto para reducir el uso de autos.'")
    print("  - **Persona B:** 'Así que lo que quieres es obligar a todos a usar buses lentos y sucios, y eliminar los autos privados. ¡Eso es una dictadura!'")
    print(" - **Tipo de Falacia:** **Hombre de Paja**. La Persona B distorsiona el argumento de la Persona A a una posición extrema y fácilmente atacable que no fue la original.")
    esperar()

    print("\n**Ejemplo 7:** 'Si le das un dulce a un niño cada vez que llora, pronto esperará dulces todo el tiempo, luego exigirá más y más, y terminará siendo un adulto caprichoso y malcriado que no puede lidiar con la frustración.'")
    print(" - **Tipo de Falacia:** **Pendiente Resbaladiza**. Se exagera una pequeña acción inicial (un dulce) hasta una serie de consecuencias extremas y negativas sin suficiente justificación.")
    esperar()

    print("\n**Ejemplo 8:** 'No hay pruebas de que exista vida inteligente en otros planetas, por lo tanto, no existe.'")
    print(" - **Tipo de Falacia:** **Ad Ignorantiam**. La ausencia de prueba no es una prueba de inexistencia.")
    esperar(limpiar=True)


def realizar_ejercicios():
    limpiar_consola()
    print("📝 **EJERCICIOS: ¡IDENTIFICA LA FALACIA!** 📝")
    print("---")
    print("Lee cada afirmación y escribe el tipo de falacia que contiene.")
    print("Opciones válidas: AD HOMINEM, AD POPULUM, FALSA CAUSA, GENERALIZACIÓN APRESURADA, PETICIÓN DE PRINCIPIO, HOMBRE DE PAJA, PENDIENTE RESBALADIZA, AD IGNORANTIAM.")
    esperar("¡Manos a la obra!")

    ejercicios = [
        {"falacia": "El candidato a la alcaldía no debería hablar de educación, ¡si él ni siquiera terminó la universidad!", "tipo": "ad hominem", "pista": "Ataca a la persona, no a sus ideas."},
        {"falacia": "La mayoría de la gente en mi ciudad piensa que el nuevo centro comercial es lo mejor, así que no puede ser malo para los pequeños negocios.", "tipo": "ad populum", "pista": "Basado en la popularidad, no en hechos económicos."},
        {"falacia": "Desde que me compré zapatillas nuevas, he corrido más rápido. Las zapatillas nuevas son la causa de mi mejora.", "tipo": "falsa causa", "pista": "Confunde correlación con causalidad."},
        {"falacia": "Probé dos restaurantes en esta ciudad y ambos eran caros. Por lo tanto, comer aquí es muy costoso.", "tipo": "generalización apresurada", "pista": "Saca una conclusión amplia de pocos ejemplos."},
        {"falacia": "Dios es real porque lo dice la fe, y la fe es creer en lo que es real.", "tipo": "petición de principio", "pista": "La conclusión ya está incluida en la premisa."},
        {"falacia": "Mi oponente dice que debemos reducir la jornada laboral. Lo que él quiere es que la gente trabaje menos y el país se vuelva perezoso.", "tipo": "hombre de paja", "pista": "Distorsiona el argumento original para atacarlo."},
        {"falacia": "Si dejamos que los estudiantes elijan sus materias, pronto querrán elegir el horario, luego las reglas de la escuela, y al final, la escuela se convertirá en un caos sin control.", "tipo": "pendiente resbaladiza", "pista": "Exagera las consecuencias futuras."},
        {"falacia": "No se ha demostrado que el té verde cure el cáncer, por lo tanto, no lo hace.", "tipo": "ad ignorantiam", "pista": "La falta de prueba no es prueba de no existencia."},
        {"falacia": "Todos mis amigos están comprando este nuevo videojuego, así que debe ser increíble y yo también debo tenerlo.", "tipo": "ad populum", "pista": "Apela a lo que 'todos hacen'."},
        {"falacia": "No podemos aceptar el argumento de María sobre la igualdad de género; ella es muy feminista y solo ve las cosas desde su perspectiva.", "tipo": "ad hominem", "pista": "Ataca la ideología de la persona en lugar del argumento."},
        {"falacia": "Después de que mi equipo de fútbol perdió, me puse calcetines diferentes al día siguiente y ganaron. Los calcetines diferentes me dieron suerte.", "tipo": "falsa causa", "pista": "Asocia eventos sin relación causal real."},
        {"falacia": "Visité un solo pueblo en la costa y la gente era muy amable. Por lo tanto, toda la gente de la costa es muy amable.", "tipo": "generalización apresurada", "pista": "Basado en una sola experiencia limitada."},
        {"falacia": "Los ovnis existen porque nadie ha probado lo contrario.", "tipo": "ad ignorantiam", "pista": "Se basa en la ausencia de evidencia en contra."},
        {"falacia": "Fumar es malo porque es perjudicial para la salud, y es perjudicial para la salud porque es malo fumar.", "tipo": "petición de principio", "pista": "El argumento se repite a sí mismo."},
        {"falacia": "El profesor dice que no se debe usar IA para las tareas. Él solo quiere que trabajemos más.", "tipo": "ad hominem", "pista": "Desacredita al profesor, no su regla."},
        {"falacia": "Si permitimos que los niños jueguen con tablets, se volverán adictos, no socializarán y nunca desarrollarán habilidades del mundo real.", "tipo": "pendiente resbaladiza", "pista": "Cadena de consecuencias extremas no justificadas."},
        {"falacia": "Si la mayoría de los estudiantes prefiere las clases virtuales, entonces estas son intrínsecamente superiores a las presenciales.", "tipo": "ad populum", "pista": "La preferencia popular no define la superioridad intrínseca."},
        {"falacia": "Comencé el día con el pie izquierdo y luego me caí. Por lo tanto, levantarme con el pie izquierdo me causó la caída.", "tipo": "falsa causa", "pista": "Superstición que asume causalidad por secuencia."},
        {"falacia": "Mi vecino, que es vegetariano, se enfermó la semana pasada. Ser vegetariano te hace más propenso a enfermarte.", "tipo": "generalización apresurada", "pista": "Un solo caso no es suficiente para generalizar."},
        {"falacia": "El alma es inmortal porque no puede morir.", "tipo": "petición de principio", "pista": "Define inmortalidad por no poder morir, es circular."},
    ]

    puntuacion = 0
    
    random.shuffle(ejercicios) 

    for i, ej in enumerate(ejercicios):
        print(f"\n--- Ejercicio {i+1}/{len(ejercicios)} ---")
        print(f"Afirmación: \"{ej['falacia']}\"")
        
        valido = False
        while not valido:
            respuesta_usuario = input("¿Qué tipo de falacia contiene? ").strip().lower()
            if respuesta_usuario in ["ad hominem", "ad populum", "falsa causa", "generalización apresurada", 
                                      "petición de principio", "hombre de paja", "pendiente resbaladiza", "ad ignorantiam"]:
                valido = True
            else:
                print("Respuesta no válida. Usa una de las opciones listadas.")

        if respuesta_usuario == ej['tipo'].lower():
            print("✅ ¡Correcto! ¡Identificaste la falacia correctamente!")
            puntuacion += 1
        else:
            print(f"❌ ¡Incorrecto! La respuesta correcta era: '{ej['tipo'].upper()}'.")
            print(f"Pista: {ej['pista']}")
        
        esperar()

    limpiar_consola()
    print("--- ¡FIN DE LOS EJERCICIOS DE IDENTIFICACIÓN! ---")
    print(f"\nHas completado los ejercicios. ¡Tu puntuación final es: {puntuacion}/{len(ejercicios)}!")
    if puntuacion >= 17: # 85%
        print("🎉 ¡Felicidades! ¡Eres un experto detective de falacias!")
    elif puntuacion >= 12: # 60%
        print("👍 ¡Muy bien! Ya entiendes cómo detectar las falacias más comunes.")
    else:
        print("✍️ ¡Sigue practicando! Con más esfuerzo, ¡ninguna falacia te engañará!")
    esperar(limpiar=True)


def practicar_refutacion():
    limpiar_consola()
    print("✍️ **PRACTICA DE REFUTACIÓN DE FALACIAS** ✍️")
    print("---")
    print("A continuación, verás una falacia. Piensa cómo la refutarías de manera lógica y respetuosa.")
    print("Luego, te mostraremos una sugerencia de refutación para que compares.")
    esperar("¡Empecemos a desarmar argumentos!")

    refutation_exercises = [
        {"falacia": "No hay que confiar en lo que dice ese economista; ¡está calvo y usa gafas viejas!", "tipo": "Ad Hominem", "sugerencia_refutacion": "Enfócate en el argumento, no en la apariencia. Puedes decir: 'La apariencia de una persona no tiene relación con la validez de sus ideas económicas. Centrémonos en sus propuestas económicas.'"},
        {"falacia": "Todos mis compañeros de clase están de acuerdo en que la tarea es inútil, así que el profesor debería eliminarla.", "tipo": "Ad Populum", "sugerencia_refutacion": "Explica que la popularidad no define la utilidad. Puedes decir: 'Aunque muchos no estén de acuerdo, el número de personas que opinan algo no determina si la tarea es útil para el aprendizaje. Podríamos discutir su propósito y objetivos.'"},
        {"falacia": "Desde que me mudé a esta casa, mi equipo de fútbol favorito siempre gana. Mi nueva casa trae suerte al equipo.", "tipo": "Falsa Causa", "sugerencia_refutacion": "Señala la falta de conexión lógica. Puedes decir: 'Que tu equipo gane después de tu mudanza es una coincidencia, no hay evidencia que relacione tu casa con los resultados deportivos del equipo.'"},
        {"falacia": "Conocí a un turista de ese país que fue muy grosero. Toda la gente de ese país es grosera.", "tipo": "Generalización Apresurada", "sugerencia_refutacion": "Pide más evidencia o señala la muestra insuficiente. Puedes decir: 'Basar una conclusión sobre un país entero en la experiencia con una sola persona es una generalización apresurada; una persona no representa a toda una población.'"},
        {"falacia": "La verdad es importante porque es fundamental decirla.", "tipo": "Petición de Principio", "sugerencia_refutacion": "Muestra que el argumento es circular. Puedes decir: 'Estás usando la misma idea para probarse a sí misma. Necesitamos una razón externa o más información para entender por qué la verdad es importante, no una simple repetición.'"},
        {"falacia": "Mi vecino dice que deberíamos apoyar el comercio local. Lo que él quiere es que paguemos más por todo y que los grandes supermercados desaparezcan.", "tipo": "Hombre de Paja", "sugerencia_refutacion": "Clarifica la posición real del oponente. Puedes decir: 'Mi vecino no ha dicho que quiera que paguemos más ni que desaparezcan los supermercados; su punto es apoyar la economía local y los pequeños negocios, lo cual es diferente a lo que sugieres.'"},
        {"falacia": "Si no exigimos que los estudiantes usen uniforme, se vestirán de manera inapropiada, esto causará distracciones, la disciplina desaparecerá y la escuela se volverá un desorden total.", "tipo": "Pendiente Resbaladiza", "sugerencia_refutacion": "Cuestiona la inevitabilidad de las consecuencias. Puedes decir: 'No hay evidencia de que no usar uniforme conduzca inevitablemente a la falta de disciplina o al caos. Se pueden establecer reglas de vestimenta sin que sea un uniforme completo, por ejemplo.'"},
        {"falacia": "Como nadie ha demostrado que los viajes en el tiempo son imposibles, es probable que existan y que ya nos estén visitando viajeros del futuro.", "tipo": "Ad Ignorantiam", "sugerencia_refutacion": "Recuerda que la ausencia de prueba no es prueba. Puedes decir: 'El hecho de que no podamos probar la imposibilidad de algo no lo convierte automáticamente en una posibilidad o una realidad. La carga de la prueba recae en quien afirma que algo existe.'"},
    ]
    random.shuffle(refutation_exercises)

    for i, ej in enumerate(refutation_exercises):
        print(f"\n--- Práctica de Refutación {i+1}/{len(refutation_exercises)} ---")
        print(f"**Falacia a Refutar ({ej['tipo']}):**")
        print(f"\"{ej['falacia']}\"")
        
        print("\nAhora, escribe tu refutación:")
        input("Tu refutación (presiona Enter cuando termines de escribir): ") # Permite al usuario escribir, pero no guarda
        
        print("\n--- Sugerencia de Refutación ---")
        print(f"Tipo de Falacia: {ej['tipo']}")
        print(f"Sugerencia: {ej['sugerencia_refutacion']}")
        
        esperar()

    limpiar_consola()
    print("--- ¡FIN DE LA PRÁCTICA DE REFUTACIÓN! ---")
    print("\n¡Has practicado cómo desarmar argumentos defectuosos!")
    print("Recuerda: la clave es identificar el error lógico y señalarlo de forma clara y respetuosa.")
    esperar(limpiar=True)

# --- Nueva función para generar ejemplos aleatorios ---

def generar_ejemplos_aleatorios():
    limpiar_consola()
    print("✨ **GENERADOR DE EJEMPLOS ALEATORIOS DE FALACIAS** ✨")
    print("---")
    print("Aquí tienes 20 nuevos ejemplos de falacias para que sigas practicando.")
    esperar()

    # Bases de datos para construir falacias aleatorias
    sujetos = ["el nuevo alcalde", "el último estudio científico", "mi vecino Juan", "la moda de los pantalones anchos", 
               "el grupo musical de moda", "la decisión del director", "la clase de matemáticas", "ese político", 
               "los estudiantes de otra escuela", "los libros antiguos", "la nueva dieta", "el uso de redes sociales",
               "las clases virtuales", "el calentamiento global", "la medicina alternativa"]
    
    cualidades_negativas = ["es un inepto", "siempre ha sido problemático", "tiene un pasado oscuro", "no sabe de lo que habla", 
                            "está comprada", "es muy idealista", "es un fracasado", "no tiene experiencia"]
    
    consecuencias_extremas = ["la sociedad colapsará", "nos quedaremos sin futuro", "la gente se volverá inútil", 
                              "todo se descontrolará", "terminaremos en la miseria", "el fin del mundo está cerca",
                              "los valores se perderán", "la civilización retrocederá"]
    
    eventos = ["la campana sonó", "pasó un gato negro", "me puse la camiseta de la suerte", "el sol salió", 
               "terminó el semestre", "llovío mucho", "un pájaro cantó", "la luz se fue"]
    
    resultados = ["saqué buena nota", "gané la lotería", "me enfermé", "todo salió mal", "tuve un buen día", 
                  "mi equipo perdió", "encontré dinero", "me sentí feliz"]

    generales_negativos = ["son todos iguales", "no sirven para nada", "son la peor opción", "siempre son un desastre"]
    
    afirmaciones_populares = ["todo el mundo lo dice", "es la tendencia actual", "millones lo usan", "es el producto más vendido",
                              "la mayoría está de acuerdo"]
    
    cosas_inexistentes = ["unicornios", "hadas", "pie grande", "monstruo del Lago Ness", "el Yeti", "el eslabón perdido",
                          "soluciones mágicas"]

    opciones_hombre_paja = [
        "quiere que volvamos a la Edad de Piedra.",
        "busca destruir toda nuestra economía.",
        "solo le interesa el caos.",
        "pretende controlar nuestras vidas.",
        "quiere que seamos esclavos del sistema.",
        "en realidad odia el progreso."
    ]

    for i in range(20):
        tipo_falacia = random.choice([
            "Ad Hominem", "Ad Populum", "Falsa Causa", "Generalización Apresurada",
            "Petición de Principio", "Hombre de Paja", "Pendiente Resbaladiza", "Ad Ignorantiam"
        ])
        
        falacia_generada = ""
        
        if tipo_falacia == "Ad Hominem":
            sujeto = random.choice(sujetos)
            cualidad = random.choice(cualidades_negativas)
            falacia_generada = f"No podemos aceptar lo que dice {sujeto} sobre el tema, ¡él {cualidad}!"
        
        elif tipo_falacia == "Ad Populum":
            afirmacion = random.choice(afirmaciones_populares)
            tema = random.choice(["este nuevo producto", "esa idea", "la moda de...", "esta canción"])
            falacia_generada = f"{afirmacion}, así que {tema} debe ser lo correcto/mejor."
        
        elif tipo_falacia == "Falsa Causa":
            evento1 = random.choice(eventos)
            resultado = random.choice(resultados)
            falacia_generada = f"Después de que {evento1}, {resultado}. Por lo tanto, {evento1} causó que {resultado}."
            
        elif tipo_falacia == "Generalización Apresurada":
            num_ejemplos = random.choice(["un", "dos", "tres"])
            sustantivo_singular = random.choice(["vecino", "estudiante", "político", "jefe", "maestro"])
            sustantivo_plural = f"{sustantivo_singular}s"
            adjetivo = random.choice(["arrogante", "deshonesto", "flojo", "amable", "inteligente", "distraído"])
            falacia_generada = f"Conocí a {num_ejemplos} {sustantivo_singular} de esa profesión/lugar y era muy {adjetivo}. Por lo tanto, todos los {sustantivo_plural} de allí son {adjetivo}s."

        elif tipo_falacia == "Petición de Principio":
            tema = random.choice(["la verdad", "la justicia", "la libertad", "la paz", "la belleza"])
            falacia_generada = f"{tema.capitalize()} es importante porque es fundamental para tener {tema}."
            
        elif tipo_falacia == "Hombre de Paja":
            sujeto_a = random.choice(["El profesor", "Mi amigo", "El político", "El activista"])
            argumento_a = random.choice(["propuso reducir la tarea.", "sugirió más espacios verdes.", "quiere discutir el presupuesto.", "habló de la igualdad."])
            sujeto_b = random.choice(["su oponente", "otro estudiante", "un crítico"])
            ataque = random.choice(opciones_hombre_paja)
            falacia_generada = f"{sujeto_a} {argumento_a} ¡Pero {sujeto_b} {ataque}"
            
        elif tipo_falacia == "Pendiente Resbaladiza":
            accion_inicial = random.choice(["Si permitimos una pequeña infracción", "Si dejamos que usen el celular", 
                                             "Si no ponemos reglas estrictas", "Si se relaja la disciplina"])
            consecuencia_leve = random.choice(["la gente se acostumbrará", "empezarán a pedir más", "habrá un poco de desorden"])
            consecuencia_extrema = random.choice(consecuencias_extremas)
            falacia_generada = f"{accion_inicial}, luego {consecuencia_leve}, y finalmente, {consecuencia_extrema}."

        elif tipo_falacia == "Ad Ignorantiam":
            cosa_inexistente = random.choice(cosas_inexistentes)
            falacia_generada = f"Nadie ha probado que {cosa_inexistente} no existan, por lo tanto, deben existir."

        print(f"\n--- Ejemplo Aleatorio {i+1} ---")
        print(f"Falacia: \"{falacia_generada}\"")
        print(f"Tipo Sugerido: {tipo_falacia}")
        esperar()

    limpiar_consola()
    print("--- ¡FIN DE LA GENERACIÓN DE EJEMPLOS! ---")
    print("\n¡Esperamos que estos nuevos ejemplos te ayuden a seguir perfeccionando tu ojo para las falacias!")
    esperar(limpiar=True)

# --- Menú principal con la nueva opción ---

def mostrar_menu():
    while True:
        limpiar_consola()
        print("--- MENÚ DE LA LECCIÓN 6: ¡DETECTANDO FALACIAS! (11.º Grado) ---")
        print("\n1. Teoría (¡Aprendemos qué son y cuáles son las falacias comunes!)")
        print("2. Ejemplos (¡Vemos cómo lucen las falacias en la práctica!)")
        print("3. Ejercicios (¡A practicar identificando tipos de falacias!)")
        print("4. Practicar Refutación (¡Aprende a desarmar falacias!)")
        print("5. Generar Nuevos Ejemplos Aleatorios (¡Más práctica y variedad!) ✨")
        print("6. Salir")
        print("---")

        opcion = input("Elige una opción (1-6): ").strip()

        if opcion == '1':
            mostrar_teoria()
        elif opcion == '2':
            mostrar_ejemplos()
        elif opcion == '3':
            realizar_ejercicios()
        elif opcion == '4':
            practicar_refutacion()
        elif opcion == '5':
            generar_ejemplos_aleatorios()
        elif opcion == '6':
            print("\n¡Gracias por fortalecer tu pensamiento crítico! ¡Sigue analizando los argumentos con cuidado!")
            sys.exit()
        else:
            print("\nOpción no válida. Por favor, elige un número del 1 al 6.")
            esperar()

# Iniciar la aplicación
if __name__ == "__main__":
    mostrar_menu()
