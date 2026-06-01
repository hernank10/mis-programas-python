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

# --- Teoría ---
def mostrar_teoria():
    limpiar_consola()
    print("🧠 **TEORÍA: ARGUMENTACIÓN AVANZADA Y LÓGICA** 🔬")
    print("---")
    
    print("\n**1. Revisión Rápida: Los Fundamentos del Argumento**")
    print("   Un argumento es un conjunto de razones (premisas) que apoyan una afirmación (conclusión).")
    print("   En este nivel, no solo buscamos que los argumentos 'suenen bien', sino que sean **lógicamente impecables** y **fundamentados en la verdad**.")
    esperar()

    print("\n**2. Lógica Formal vs. Lógica Informal: Validez y Solidez**")
    print("   La **lógica** es la herramienta para evaluar la fuerza real de un razonamiento.")

    print("\n   **a. Lógica Formal:**")
    print("      - Se centra en la **estructura (forma)** del argumento, no en su contenido.")
    print("      - Concepto clave: **VALIDEZ**.")
    print("      - Un argumento es **válido** si su conclusión se sigue *necesariamente* de sus premisas. Si las premisas fueran verdaderas, la conclusión DEBERÍA ser verdadera.")
    print("      - **Importante:** Un argumento válido puede tener premisas falsas y/o una conclusión falsa.")
    print("      - **Ejemplo (Válido, pero NO sólido):**")
    print("        * Premisa 1: Todos los pájaros son mamíferos. (Falso)")
    print("        * Premisa 2: Un gorrión es un pájaro. (Verdadero)")
    print("        * Conclusión: Por lo tanto, un gorrión es un mamífero. (Falso)")
    print("        * *Análisis:* Es **válido** porque la estructura lógica es correcta. Si las premisas fueran ciertas, la conclusión lo sería.")
    esperar()

    print("\n   **b. Lógica Informal:**")
    print("      - Se centra en el **contenido** del argumento, su **pertinencia**, la **aceptabilidad** de las premisas y la **fuerza de la inferencia**.")
    print("      - Concepto clave: **SOLIDEZ (Soundness)**.")
    print("      - Un argumento es **sólido** si es **válido** (formalmente correcto) Y **todas sus premisas son verdaderas**.")
    print("      - **Un argumento sólido siempre tiene una conclusión verdadera.**")
    print("      - **Ejemplo (Válido y Sólido):**")
    print("        * Premisa 1: Todos los peces viven en el agua. (Verdadero)")
    print("        * Premisa 2: Un tiburón es un pez. (Verdadero)")
    print("        * Conclusión: Por lo tanto, un tiburón vive en el agua. (Verdadero)")
    print("        * *Análisis:* Este argumento es **válido** (estructura correcta) y **sólido** (premisas verdaderas).")
    print("      - Las falacias (vistas en lecciones anteriores) son errores que impiden la solidez.")
    print("   **Diferencia clave:** La **validez** es sobre la *forma*; la **solidez** es sobre la *forma* Y el *contenido* (verdad de las premisas).")
    esperar()

    print("\n**3. Tipos de Razonamiento: Deductivo e Inductivo**")

    print("\n   **a. Razonamiento Deductivo:**")
    print("      - Va de lo **general a lo particular**.")
    print("      - Si las premisas son verdaderas y el argumento es válido, la conclusión es **necesariamente verdadera**.")
    print("      - **Objetivo:** Probar una conclusión específica a partir de verdades generales con **certeza**.")
    print("      - **Ejemplo:**")
    print("        * Premisa 1: Todos los insectos tienen seis patas.")
    print("        * Premisa 2: Las hormigas son insectos.")
    print("        * Conclusión: Por lo tanto, las hormigas tienen seis patas.")
    esperar()

    print("\n   **b. Razonamiento Inductivo:**")
    print("      - Va de lo **particular a lo general**.")
    print("      - Las premisas proporcionan **evidencia que apoya la probabilidad** de que la conclusión sea verdadera, pero no la garantizan.")
    print("      - **Objetivo:** Formular generalizaciones, predicciones o hipótesis basadas en observaciones específicas con **probabilidad** o **fuerza**.")
    print("      - **Evaluación:** Se evalúan como **fuertes/débiles**, no válidos/inválidos.")
    print("      - **Ejemplo:**")
    print("        * Premisa 1: Cada perro que he visto tiene cola.")
    print("        * Conclusión: Por lo tanto, todos los perros tienen cola.")
    print("        * *Análisis:* Es **fuerte**, pero no 100% cierto (podría haber un perro sin cola por accidente o mutación).")
    esperar(limpiar=True)

# --- Ejemplos ---
def mostrar_ejemplos():
    limpiar_consola()
    print("💡 **EJEMPLOS DE VALIDEZ, SOLIDEZ Y TIPOS DE RAZONAMIENTO** 💡")
    print("---")

    print("\n**Ejemplo 1: Deductivo, Válido y Sólido**")
    print("   - P1: Todos los atletas olímpicos entrenan duro.")
    print("   - P2: María es una atleta olímpica.")
    print("   - C: Por lo tanto, María entrena duro.")
    print("   *Análisis:* La conclusión se sigue necesariamente (válido) y todas las premisas son verdaderas (sólido).")
    esperar()

    print("\n**Ejemplo 2: Deductivo, Válido, pero NO Sólido**")
    print("   - P1: Todos los peces vuelan. (Falso)")
    print("   - P2: Una trucha es un pez. (Verdadero)")
    print("   - C: Por lo tanto, una trucha vuela. (Falso)")
    print("   *Análisis:* La estructura es correcta (válido), pero una premisa es falsa, por lo tanto, no es sólido.")
    esperar()

    print("\n**Ejemplo 3: Deductivo, Inválido (y por ende, no sólido)**")
    print("   - P1: Algunos estudiantes usan gafas.")
    print("   - P2: Juan usa gafas.")
    print("   - C: Por lo tanto, Juan es estudiante.")
    print("   *Análisis:* La conclusión NO se sigue necesariamente. Juan podría usar gafas por otra razón (inválido).")
    esperar()

    print("\n**Ejemplo 4: Inductivo Fuerte**")
    print("   - P1: Cada vez que he ido al parque en verano, ha hecho sol.")
    print("   - C: Es probable que la próxima vez que vaya al parque en verano, haga sol.")
    print("   *Análisis:* Las premisas aportan evidencia fuerte, haciendo la conclusión probable, pero no garantizada.")
    esperar()
    
    print("\n**Ejemplo 5: Inductivo Débil (Generalización Apresurada)**")
    print("   - P1: Ayer conocí a un conductor de taxi y era muy amable.")
    print("   - C: Por lo tanto, todos los conductores de taxi son muy amables.")
    print("   *Análisis:* La evidencia es insuficiente para la generalización, es un argumento inductivo muy débil.")
    esperar(limpiar=True)

# --- Ejercicios de identificación ---
def realizar_ejercicios():
    limpiar_consola()
    print("📝 **EJERCICIOS: IDENTIFICA TIPO Y EVALÚA** 📝")
    print("---")
    print("Para cada argumento, identifica si es **DEDUCTIVO** o **INDUCTIVO**.")
    print("Luego, para los DEDUCTIVOS, indica si es **VÁLIDO** y **SÓLIDO** (sí/no).")
    print("Para los INDUCTIVOS, indica si es **FUERTE** o **DÉBIL**.")
    esperar("¡Empecemos!")

    ejercicios = [
        {"arg": "Todos los perros son mamíferos. Fido es un perro. Por lo tanto, Fido es un mamífero.", 
         "tipo_esperado": "DEDUCTIVO", "validez_esperada": "VÁLIDO", "solidez_esperada": "SÓLIDO"},
        {"arg": "Cada vez que tiro una pelota al aire, cae. Por lo tanto, la próxima vez que tire una pelota al aire, caerá.", 
         "tipo_esperado": "INDUCTIVO", "fuerza_esperada": "FUERTE"},
        {"arg": "Todos los peces pueden volar. Los delfines son peces. Por lo tanto, los delfines pueden volar.", 
         "tipo_esperado": "DEDUCTIVO", "validez_esperada": "VÁLIDO", "solidez_esperada": "NO SÓLIDO"},
        {"arg": "Algunos científicos usan gafas. Mi padre usa gafas. Por lo tanto, mi padre es científico.", 
         "tipo_esperado": "DEDUCTIVO", "validez_esperada": "INVÁLIDO", "solidez_esperada": "NO APLICA"}, # Inválido => No Sólido
        {"arg": "He comido pizza en cinco pizzerías diferentes de esta ciudad y todas eran deliciosas. Probablemente, todas las pizzerías de esta ciudad son deliciosas.", 
         "tipo_esperado": "INDUCTIVO", "fuerza_esperada": "FUERTE"},
        {"arg": "Todos los gatos tienen cola. Félix no tiene cola. Por lo tanto, Félix no es un gato.", 
         "tipo_esperado": "DEDUCTIVO", "validez_esperada": "VÁLIDO", "solidez_esperada": "SÓLIDO"},
        {"arg": "Conocí a una persona de esa ciudad y era muy ruidosa. Todas las personas de esa ciudad son ruidosas.", 
         "tipo_esperado": "INDUCTIVO", "fuerza_esperada": "DÉBIL"},
        {"arg": "Si es de día, hay luz solar. Es de día. Por lo tanto, hay luz solar.", 
         "tipo_esperado": "DEDUCTIVO", "validez_esperada": "VÁLIDO", "solidez_esperada": "SÓLIDO"},
        {"arg": "Cada estudiante en la clase B obtuvo una A en el examen. Por lo tanto, el examen era fácil.", 
         "tipo_esperado": "INDUCTIVO", "fuerza_esperada": "DÉBIL"}, # Puede ser que la clase B sea muy buena
        {"arg": "Todas las plantas realizan fotosíntesis. Una rosa es una planta. Por lo tanto, una rosa realiza fotosíntesis.", 
         "tipo_esperado": "DEDUCTIVO", "validez_esperada": "VÁLIDO", "solidez_esperada": "SÓLIDO"},
        {"arg": "El sol ha salido todos los días hasta ahora. Por lo tanto, el sol saldrá mañana.", 
         "tipo_esperado": "INDUCTIVO", "fuerza_esperada": "FUERTE"},
        {"arg": "Ningún futbolista es un malabarista. Messi es futbolista. Por lo tanto, Messi no es malabarista.", 
         "tipo_esperado": "DEDUCTIVO", "validez_esperada": "VÁLIDO", "solidez_esperada": "SÓLIDO"},
        {"arg": "La mayoría de los votantes en las encuestas apoya al Candidato X. Por lo tanto, el Candidato X ganará las elecciones.", 
         "tipo_esperado": "INDUCTIVO", "fuerza_esperada": "FUERTE"}, # Depende de la calidad de la encuesta, pero en general es fuerte
        {"arg": "Si llueve, las calles se mojan. Las calles están mojadas. Por lo tanto, llovió.", 
         "tipo_esperado": "DEDUCTIVO", "validez_esperada": "INVÁLIDO", "solidez_esperada": "NO APLICA"}, # Podrían estar mojadas por otra razón (lavado, etc.)
        {"arg": "Todos los insectos tienen ocho patas. Una araña es un insecto. Por lo tanto, una araña tiene ocho patas.", 
         "tipo_esperado": "DEDUCTIVO", "validez_esperada": "VÁLIDO", "solidez_esperada": "NO SÓLIDO"}, # Insectos tienen 6, arañas no son insectos
        {"arg": "Este medicamento funcionó en 9 de cada 10 pacientes en el estudio. Es probable que funcione en ti.", 
         "tipo_esperado": "INDUCTIVO", "fuerza_esperada": "FUERTE"},
        {"arg": "Todos los cuadrados tienen cuatro lados. Esta figura es un cuadrado. Por lo tanto, esta figura tiene cuatro lados.", 
         "tipo_esperado": "DEDUCTIVO", "validez_esperada": "VÁLIDO", "solidez_esperada": "SÓLIDO"},
        {"arg": "Mis últimas tres predicciones meteorológicas fueron correctas. Por lo tanto, mi próxima predicción también será correcta.", 
         "tipo_esperado": "INDUCTIVO", "fuerza_esperada": "DÉBIL"}, # 3 predicciones no son suficientes para una conclusión fuerte
        {"arg": "Si un animal es un perro, entonces es un mamífero. Este animal es un mamífero. Por lo tanto, este animal es un perro.", 
         "tipo_esperado": "DEDUCTIVO", "validez_esperada": "INVÁLIDO", "solidez_esperada": "NO APLICA"}, # Podría ser otro mamífero
        {"arg": "Todos los cuerpos celestes con anillos son planetas. Saturno tiene anillos. Por lo tanto, Saturno es un planeta.", 
         "tipo_esperado": "DEDUCTIVO", "validez_esperada": "VÁLIDO", "solidez_esperada": "SÓLIDO"},
    ]

    random.shuffle(ejercicios)
    puntuacion = 0

    for i, ej in enumerate(ejercicios):
        limpiar_consola()
        print(f"\n--- Ejercicio {i+1}/{len(ejercicios)} ---")
        print(f"Argumento: \"{ej['arg']}\"")
        
        # Preguntar tipo de razonamiento
        tipo_valido = False
        while not tipo_valido:
            respuesta_tipo = input("¿Es DEDUCTIVO o INDUCTIVO? ").strip().upper()
            if respuesta_tipo in ["DEDUCTIVO", "INDUCTIVO"]:
                tipo_valido = True
            else:
                print("Respuesta no válida. Por favor, escribe DEDUCTIVO o INDUCTIVO.")

        es_deductivo_correcto = (respuesta_tipo == ej["tipo_esperado"])
        if es_deductivo_correcto:
            print("✅ Tipo correcto.")
        else:
            print(f"❌ Tipo incorrecto. La respuesta correcta era: {ej['tipo_esperado']}.")

        if ej["tipo_esperado"] == "DEDUCTIVO":
            # Preguntar validez
            validez_valida = False
            while not validez_valida:
                respuesta_validez = input("¿Es VÁLIDO? (Sí/No) ").strip().upper()
                if respuesta_validez in ["SÍ", "SI", "NO"]:
                    validez_valida = True
                else:
                    print("Respuesta no válida. Por favor, escribe Sí o No.")
            
            es_valido_correcto = (("SÍ" in respuesta_validez and ej["validez_esperada"] == "VÁLIDO") or 
                                  ("NO" in respuesta_validez and ej["validez_esperada"] == "INVÁLIDO"))
            
            if es_valido_correcto:
                print("✅ Validez correcta.")
            else:
                print(f"❌ Validez incorrecta. La respuesta correcta era: {ej['validez_esperada']}.")

            # Preguntar solidez (solo si es válido o si aplica para la explicación)
            if ej["validez_esperada"] == "VÁLIDO": # Solo preguntamos solidez si es válido
                solidez_valida = False
                while not solidez_valida:
                    respuesta_solidez = input("¿Es SÓLIDO? (Sí/No) ").strip().upper()
                    if respuesta_solidez in ["SÍ", "SI", "NO"]:
                        solidez_valida = True
                    else:
                        print("Respuesta no válida. Por favor, escribe Sí o No.")
                
                es_solido_correcto = (("SÍ" in respuesta_solidez and ej["solidez_esperada"] == "SÓLIDO") or 
                                      ("NO" in respuesta_solidez and ej["solidez_esperada"] == "NO SÓLIDO"))

                if es_solido_correcto:
                    print("✅ Solidez correcta.")
                else:
                    print(f"❌ Solidez incorrecta. La respuesta correcta era: {ej['solidez_esperada']}.")
            else: # Si es inválido, automáticamente no es sólido. No preguntamos.
                es_solido_correcto = True # Para la puntuación, se considera 'correcto' no preguntar.
                print("  (Es inválido, por lo tanto, no es sólido.)")

            if es_deductivo_correcto and es_valido_correcto and es_solido_correcto:
                puntuacion += 1

        elif ej["tipo_esperado"] == "INDUCTIVO":
            # Preguntar fuerza
            fuerza_valida = False
            while not fuerza_valida:
                respuesta_fuerza = input("¿Es FUERTE o DÉBIL? ").strip().upper()
                if respuesta_fuerza in ["FUERTE", "DÉBIL"]:
                    fuerza_valida = True
                else:
                    print("Respuesta no válida. Por favor, escribe FUERTE o DÉBIL.")
            
            es_fuerza_correcto = (respuesta_fuerza == ej["fuerza_esperada"])
            if es_fuerza_correcto:
                print("✅ Fuerza inductiva correcta.")
            else:
                print(f"❌ Fuerza inductiva incorrecta. La respuesta correcta era: {ej['fuerza_esperada']}.")
            
            if es_deductivo_correcto and es_fuerza_correcto:
                puntuacion += 1
        
        esperar("Presiona Enter para el siguiente ejercicio...")

    limpiar_consola()
    print("--- ¡FIN DE LOS EJERCICIOS DE EVALUACIÓN! ---")
    print(f"\nHas completado los ejercicios. ¡Tu puntuación final es: {puntuacion}/{len(ejercicios)}!")
    if puntuacion >= len(ejercicios) * 0.85:
        print("🎉 ¡Felicidades! ¡Dominas la lógica y la argumentación!")
    elif puntuacion >= len(ejercicios) * 0.6:
        print("👍 ¡Muy bien! Estás en camino a un sólido pensamiento crítico.")
    else:
        print("✍️ ¡Sigue practicando! La lógica es una habilidad que mejora con la práctica.")
    esperar(limpiar=True)

# --- Nueva función para generar ejemplos aleatorios ---
def generar_ejemplos_aleatorios():
    limpiar_consola()
    print("✨ **GENERADOR DE EJEMPLOS ALEATORIOS** ✨")
    print("---")
    print("Aquí tienes 20 nuevos ejemplos de argumentos para que sigas practicando su identificación.")
    esperar()

    # Bases de datos para construir falacias aleatorias
    sujetos_general = ["Todos los estudiantes de esta universidad", "Cada persona en este país", 
                       "Los mamíferos", "Los metales", "Todos los números pares", "Los ciudadanos mayores de 18 años"]
    propiedades_general = ["pueden votar", "son vertebrados", "conducen electricidad", "han nacido"]

    sujetos_especifico = ["Juan", "Este perro", "El agua", "El hierro", "El número 4", "María", "Mi computadora"]
    propiedades_especifico_verdadero = ["es un estudiante", "ladra", "hierve a 100°C", "es un metal", "es un número par"]
    propiedades_especifico_falso = ["puede volar", "es de color azul", "es un ave", "es invisible", "es divisible por 3"]

    observaciones = ["He visto 1000 cisnes blancos", "Todos los cuervos que he visto son negros", 
                     "Las manzanas que he probado en esta región son dulces", "Cada día amanece después de la noche"]
    conclusiones_probables = ["Por lo tanto, todos los cisnes son blancos.", "Por lo tanto, todos los cuervos son negros.",
                              "Probablemente, todas las manzanas de esta región son dulces.", "El sol saldrá mañana."]
    
    observaciones_debiles = ["Conocí a una persona de ese equipo y era desorganizada", "Solo dos personas se quejaron del servicio"]
    conclusiones_improbables = ["Por lo tanto, todo el equipo es desorganizado.", "El servicio es terrible para todos."]

    opciones_inv_ded = [
        ("Si hay fuego, hay humo. Hay humo. Por lo tanto, hay fuego.", "DEDUCTIVO", "INVÁLIDO"), # Puede haber humo sin fuego (niebla, humo de chimenea)
        ("Algunos gatos son negros. Mi gato es negro. Por lo tanto, mi gato es un gato.", "DEDUCTIVO", "INVÁLIDO"), # La conclusión es obvia, pero la estructura no garantiza que 'ser negro' implique 'ser gato' si la primera premisa solo habla de 'algunos'.
        ("Todos los libros son interesantes. 'Romeo y Julieta' es interesante. Por lo tanto, 'Romeo y Julieta' es un libro.", "DEDUCTIVO", "INVÁLIDO"), # Puede ser un libro, pero la estructura no lo fuerza.
        ("Todos los perros son animales. Un canario es un animal. Por lo tanto, un canario es un perro.", "DEDUCTIVO", "INVÁLIDO"),
    ]

    for i in range(20):
        tipo_arg = random.choice(["DEDUCTIVO", "INDUCTIVO"])
        falacia_generada = ""
        
        if tipo_arg == "DEDUCTIVO":
            caso_validez = random.choice(["SOLIDO", "NO_SOLIDO_PREMISA_FALSA", "INVALIDO"])
            if caso_validez == "SOLIDO":
                p1_idx = random.randint(0, len(sujetos_general) - 1)
                p2_idx = random.randint(0, len(sujetos_especifico) - 1)
                
                p1 = f"{sujetos_general[p1_idx]} {propiedades_general[p1_idx % len(propiedades_general)]}."
                p2 = f"{sujetos_especifico[p2_idx]} {propiedades_especifico_verdadero[p2_idx % len(propiedades_especifico_verdadero)]}."
                # La conclusión para un sólido debe seguir la estructura: Si P1: Todos A son B, P2: C es A, C: C es B
                # Esto es más complejo de generar aleatoriamente sin un sistema de lógica formal.
                # Simplificaremos con una estructura fija para el ejemplo.
                falacia_generada = f"Si todos los X son Y, y Z es X, entonces Z es Y. (Ej: Todos los perros son mamíferos. Fido es un perro. Por lo tanto, Fido es un mamífero.)" # Placeholder
                if random.choice([True, False]): # Intentar generar uno "realmente" sólido
                    suj_gen = random.choice(["Los humanos", "Las aves", "Los cuadrados", "Los árboles"])
                    prop_gen = random.choice(["son mortales", "tienen alas", "tienen cuatro lados", "crecen con el sol"])
                    suj_esp = random.choice(["Sócrates", "Un águila", "Mi mesa", "Un roble"])
                    if suj_esp == "Mi mesa": # Asegurar coherencia
                        prop_gen = "tienen cuatro patas"
                        suj_gen = "Todas las mesas"
                    elif suj_esp == "Un roble":
                        prop_gen = "crecen con el sol"
                        suj_gen = "Los árboles"
                    
                    falacia_generada = f"P1: {suj_gen} {prop_gen}. P2: {suj_esp} es un/una {suj_gen[:-1] if suj_gen.endswith('s') else suj_gen}. C: Por lo tanto, {suj_esp} {prop_gen}."
                    
            elif caso_validez == "NO_SOLIDO_PREMISA_FALSA":
                p1_idx = random.randint(0, len(sujetos_general) - 1)
                p2_idx = random.randint(0, len(sujetos_especifico) - 1)
                
                suj_gen = random.choice(["Todos los peces", "Todos los gatos", "Todos los insectos", "Todos los autos"])
                prop_gen = random.choice(["pueden volar", "hablan español", "tienen ocho patas", "funcionan con agua"])
                suj_esp = random.choice(["Un tiburón", "Mi mascota", "Una mosca", "Mi coche"])
                
                falacia_generada = f"P1: {suj_gen} {prop_gen}. P2: {suj_esp} es un/una {suj_gen[:-1] if suj_gen.endswith('s') else suj_gen}. C: Por lo tanto, {suj_esp} {prop_gen}."
            
            elif caso_validez == "INVALIDO":
                falacia_generada = random.choice(opciones_inv_ded)[0] # Tomar solo el argumento
                
            
        elif tipo_arg == "INDUCTIVO":
            if random.choice([True, False]): # Fuerte o débil
                obs = random.choice(observaciones)
                conc = random.choice(conclusiones_probables)
                falacia_generada = f"{obs}. {conc}"
            else:
                obs = random.choice(observaciones_debiles)
                conc = random.choice(conclusiones_improbables)
                falacia_generada = f"{obs}. {conc}"

        print(f"\n--- Nuevo Ejemplo {i+1} ---")
        print(f"Argumento: \"{falacia_generada}\"")
        print(f"Tipo: {tipo_arg}") # No damos la validez/fuerza para que practiquen
        esperar()

    limpiar_consola()
    print("--- ¡FIN DE LA GENERACIÓN DE EJEMPLOS! ---")
    print("\n¡Esperamos que estos nuevos ejemplos te ayuden a seguir perfeccionando tu habilidad para evaluar argumentos!")
    esperar(limpiar=True)

# --- Menú principal ---
def mostrar_menu():
    while True:
        limpiar_consola()
        print("--- MENÚ: LECCIÓN 6 - ARGUMENTACIÓN AVANZADA Y LÓGICA (Preuniversitario) ---")
        print("\n1. Teoría (Validez, Solidez, Deductivo vs. Inductivo)")
        print("2. Ejemplos (Casos prácticos de argumentos)")
        print("3. Ejercicios (Identifica y evalúa argumentos)")
        print("4. Generar Nuevos Ejemplos Aleatorios (¡Más práctica!) ✨")
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
            generar_ejemplos_aleatorios()
        elif opcion == '5':
            print("\n¡Gracias por seguir desarrollando tu pensamiento crítico! ¡Hasta la próxima!")
            sys.exit()
        else:
            print("\nOpción no válida. Por favor, elige un número del 1 al 5.")
            esperar()

# Iniciar la aplicación
if __name__ == "__main__":
    mostrar_menu()
