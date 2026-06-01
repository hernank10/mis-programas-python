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
    print("📚 **TEORÍA: CONSTRUYENDO UNA OPINIÓN CON ESTRUCTURA** 📚")
    print("---")
    
    print("\n1. **¿Qué es una Opinión Estructurada?** 🤔")
    print("   Todos tenemos opiniones, que son lo que pensamos o creemos sobre algo. Pero una **opinión estructurada** no es solo lo que crees, ¡sino **por qué lo crees** y **con qué pruebas** puedes demostrarlo!")
    print("   Es como construir un edificio fuerte: necesita buenos cimientos y pilares para no caerse.")
    esperar()

    print("\n2. **Los 4 Pilares de una Opinión Fuerte** 💪")
    print("   Para que tu opinión sea clara y convincente, necesita estas partes:")
    print("   a. **POSTURA (o Tesis):** Es tu idea principal. Lo que tú piensas o defiendes en una sola frase clara.")
    print("      - Ej: 'Es importante reciclar la basura.'")
    esperar()
    
    print("   b. **ARGUMENTOS (o Razones):** Son los 'porqués' de tu postura. Explican y justifican tu idea principal.")
    print("      - Ej: 'Argumento 1: Reciclar ayuda a cuidar el planeta.'")
    print("      - Ej: 'Argumento 2: Reduce la cantidad de basura en los vertederos.'")
    esperar()

    print("   c. **EVIDENCIAS (o Pruebas/Ejemplos):** Son los datos, hechos, ejemplos o experiencias que demuestran que tus argumentos son ciertos. ¡Son tu 'prueba'!")
    print("      - Ej: 'Evidencia 1 (para Argumento 1): Al reciclar, se ahorra energía y se contamina menos el aire y el agua.'")
    print("      - Ej: 'Evidencia 2 (para Argumento 2): Muchas ciudades están llenas de basura y no hay espacio para más.'")
    esperar()

    print("   d. **CONCLUSIÓN:** Es el cierre de tu opinión. Reafirmas tu postura principal, a veces resumiendo tus razones más importantes.")
    print("      - Ej: 'Por lo tanto, reciclar es una acción sencilla y necesaria para proteger nuestro medio ambiente y nuestro futuro.'")
    esperar(limpiar=True)

def mostrar_ejemplos():
    limpiar_consola()
    print("💡 **EJEMPLOS: OPINIONES BIEN ESTRUCTURADAS** 💡")
    print("---")

    print("\n**Ejemplo 1: ¿Por qué el ejercicio es importante?**")
    print(" - **POSTURA:** Hacer ejercicio regularmente es muy beneficioso para nuestra salud.")
    print(" - **ARGUMENTO 1:** Ayuda a nuestro cuerpo a estar fuerte y sano.")
    print(" - **EVIDENCIA 1:** Las personas que hacen ejercicio se enferman menos y tienen más energía.")
    print(" - **ARGUMENTO 2:** Mejora nuestro estado de ánimo.")
    print(" - **EVIDENCIA 2:** Al hacer deporte, el cerebro libera sustancias que nos hacen sentir más felices y menos estresados.")
    print(" - **CONCLUSIÓN:** Por todo esto, dedicar tiempo al ejercicio es una excelente inversión en nuestro bienestar físico y mental.")
    esperar()

    print("\n**Ejemplo 2: ¿Deberían las mascotas ir al colegio?**")
    print(" - **POSTURA:** Las mascotas no deberían venir al colegio.")
    print(" - **ARGUMENTO 1:** Podrían causar alergias a algunos compañeros.")
    print(" - **EVIDENCIA 1:** Muchos niños son alérgicos al pelo de gatos o perros y podrían tener estornudos o picazón.")
    print(" - **ARGUMENTO 2:** Podrían distraer a los estudiantes en clase.")
    print(" - **EVIDENCIA 2:** Si un perro ladra o un gato corre por el aula, los niños se enfocarían en la mascota y no en el profesor.")
    print(" - **CONCLUSIÓN:** Por lo tanto, aunque las mascotas son adorables, lo mejor es que se queden en casa para que el colegio sea un lugar seguro y sin distracciones para todos.")
    esperar(limpiar=True)

def realizar_ejercicios():
    limpiar_consola()
    print("📝 **EJERCICIOS: ¡ORGANIZA TU OPINIÓN!** 📝")
    print("---")
    print("Lee estas partes de opiniones desordenadas y colócalas en el lugar correcto (Postura, Argumento, Evidencia, Conclusión).")
    esperar("¡Empecemos!")

    ejercicios = [
        {"tema": "Los videojuegos",
         "partes": [
             ("Los videojuegos no son solo un pasatiempo, sino que pueden ser educativos.", "postura"),
             ("Muchos juegos están diseñados para desarrollar el pensamiento estratégico y la resolución de problemas.", "argumento"),
             ("Juegos como 'Minecraft' o 'Kerbal Space Program' enseñan diseño, ingeniería y física de forma práctica.", "evidencia"),
             ("Además, fomentan la creatividad al permitir a los jugadores construir mundos y diseñar personajes.", "argumento"),
             ("En 'Roblox', los niños pueden programar sus propios juegos y compartirlos, desarrollando habilidades digitales.", "evidencia"),
             ("Por lo tanto, los videojuegos, usados con moderación, son una herramienta valiosa para el aprendizaje y la creatividad.", "conclusion")
         ]},
        {"tema": "La comida rápida",
         "partes": [
             ("La comida rápida no es buena para nuestra salud.", "postura"),
             ("Contiene demasiada grasa y azúcar, lo que nos hace engordar.", "argumento"),
             ("Una hamburguesa grande con papas y refresco tiene muchas más calorías de las que necesitamos en una comida.", "evidencia"),
             ("Además, comerla seguido puede causar enfermedades graves a largo plazo.", "argumento"),
             ("Estudios demuestran que las personas que consumen mucha comida rápida tienen más riesgo de diabetes y problemas cardíacos.", "evidencia"),
             ("En resumen, para mantenernos sanos, debemos evitar la comida rápida y preferir alimentos nutritivos.", "conclusion")
         ]},
         {"tema": "El uso del teléfono en clase",
         "partes": [
             ("Usar el teléfono en clase es perjudicial para el aprendizaje.", "postura"),
             ("Distrae a los estudiantes y les impide prestar atención.", "argumento"),
             ("Cuando suena una notificación o llega un mensaje, la mente se desvía del tema de la clase.", "evidencia"),
             ("Además, puede afectar el rendimiento académico de forma negativa.", "argumento"),
             ("Los estudios muestran que los alumnos que usan el móvil en clase suelen tener notas más bajas.", "evidencia"),
             ("Por lo tanto, para garantizar un buen ambiente de aprendizaje, el uso del teléfono debe estar restringido durante las clases.", "conclusion")
         ]},
         {"tema": "Leer libros",
         "partes": [
             ("Leer libros es una actividad fundamental para nuestro desarrollo.", "postura"),
             ("Amplía nuestro vocabulario y mejora nuestra escritura.", "argumento"),
             ("Al leer, encontramos palabras nuevas y vemos cómo se construyen las frases correctamente.", "evidencia"),
             ("También nos permite explorar mundos y culturas diferentes sin salir de casa.", "argumento"),
             ("Puedes viajar a Egipto antiguo en una novela o aprender sobre animales de la selva en un libro de ciencias.", "evidencia"),
             ("En conclusión, la lectura es una puerta al conocimiento y a la imaginación que nos enriquece de muchas maneras.", "conclusion")
         ]},
    ]
    
    puntuacion = 0
    total_preguntas = 0

    for idx, ej in enumerate(ejercicios):
        random.shuffle(ej['partes']) # Mezclar las partes para cada ejercicio
        print(f"\n--- Ejercicio {idx+1}/4: Tema: {ej['tema']} ---")
        print("Organiza las siguientes partes de una opinión:")
        for i, (texto, _) in enumerate(ej['partes']):
            print(f" {i+1}. {texto}")
        
        respuestas_correctas_orden = [p[1] for p in ej['partes']] # Obtener el orden de las etiquetas correctas
        respuestas_ordenadas_textos = [p[0] for p in ej['partes']] # Obtener el orden de los textos para mostrar

        print("\nIndica el número de cada frase y a qué parte corresponde (Postura, Argumento, Evidencia, Conclusión).")
        print("Ejemplo: 1. Postura, 2. Argumento, etc.")
        
        respuestas_usuario = []
        for j in range(len(ej['partes'])):
            valido = False
            while not valido:
                try:
                    respuesta = input(f"Frase {j+1}: ").strip().lower()
                    num_frase, tipo = respuesta.split('.')
                    num_frase = int(num_frase.strip()) - 1 # Convertir a índice de lista
                    tipo = tipo.strip().lower()

                    if 0 <= num_frase < len(ej['partes']) and tipo in ["postura", "argumento", "evidencia", "conclusion"]:
                        respuestas_usuario.append((num_frase, tipo))
                        valido = True
                    else:
                        print("Formato incorrecto o tipo no válido. Usa 'Número. Tipo' (ej: 1. Postura).")
                except ValueError:
                    print("Formato incorrecto. Usa 'Número. Tipo' (ej: 1. Postura).")

        # Comprobar respuestas
        aciertos_ejercicio = 0
        for num_frase_usuario, tipo_usuario in respuestas_usuario:
            texto_frase = ej['partes'][num_frase_usuario][0]
            tipo_real = ej['partes'][num_frase_usuario][1]
            if tipo_usuario == tipo_real:
                print(f"✅ Frase '{texto_frase}' - ¡Correcto! Es una {tipo_real}.")
                aciertos_ejercicio += 1
            else:
                print(f"❌ Frase '{texto_frase}' - Incorrecto. Esperaba '{tipo_real}', dijiste '{tipo_usuario}'.")
        
        puntuacion += aciertos_ejercicio
        total_preguntas += len(ej['partes'])

        esperar()

    limpiar_consola()
    print("--- ¡FIN DE LOS EJERCICIOS! ---")
    print(f"\nHas completado los ejercicios. ¡Tu puntuación final es: {puntuacion}/{total_preguntas}!")
    if puntuacion >= total_preguntas * 0.75:
        print("🎉 ¡Felicidades! ¡Eres un constructor experto de opiniones!")
    elif puntuacion >= total_preguntas * 0.5:
        print("👍 ¡Buen trabajo! Sigue practicando y serás un maestro en esto.")
    else:
        print("✍️ ¡No te preocupes! Sigue repasando la estructura y lo lograrás.")
    esperar(limpiar=True)


def crear_ejemplos_propios():
    limpiar_consola()
    print("✍️ **¡CONSTRUYE TU PROPIA OPINIÓN ESTRUCTURADA!** ✍️")
    print("---")
    print("¡Vamos a elegir un tema y construir una opinión completa con todos sus pilares!")
    print("Piensa en un tema que te interese y sobre el que tengas algo que decir.")
    esperar("¡Manos a la obra!")

    opiniones_creadas = []
    
    for i in range(2): # Pedir 2 opiniones completas
        print(f"\n--- Tu Opinión {i+1}/2 ---")
        tema_opinion = input("¿Sobre qué tema vas a opinar?: ").strip()
        
        print("\nAhora, vamos a construir tu opinión paso a paso:")
        postura = input("1. Tu POSTURA (lo que piensas sobre el tema en una frase): ").strip()
        argumento1 = input("2. ARGUMENTO 1 (una razón para tu postura): ").strip()
        evidencia1 = input("3. EVIDENCIA 1 (una prueba o ejemplo para tu argumento 1): ").strip()
        argumento2 = input("4. ARGUMENTO 2 (otra razón para tu postura): ").strip()
        evidencia2 = input("5. EVIDENCIA 2 (una prueba o ejemplo para tu argumento 2): ").strip()
        conclusion = input("6. CONCLUSIÓN (reafirma tu postura y cierra tu opinión): ").strip()

        opiniones_creadas.append({
            "tema": tema_opinion,
            "postura": postura,
            "argumento1": argumento1,
            "evidencia1": evidencia1,
            "argumento2": argumento2,
            "evidencia2": evidencia2,
            "conclusion": conclusion
        })
        print("\n¡Tu opinión ha sido construida!")
        esperar()

    limpiar_consola()
    print("--- ¡TUS OPINIONES ESTRUCTURADAS! ---")
    print("\nAquí están las opiniones que construiste:")
    for j, opinion in enumerate(opiniones_creadas):
        print(f"\n**OPINIÓN {j+1}: Tema - {opinion['tema']}**")
        print(f"  **POSTURA:** {opinion['postura']}")
        print(f"  **ARGUMENTO 1:** {opinion['argumento1']}")
        print(f"  **EVIDENCIA 1:** {opinion['evidencia1']}")
        print(f"  **ARGUMENTO 2:** {opinion['argumento2']}")
        print(f"  **EVIDENCIA 2:** {opinion['evidencia2']}")
        print(f"  **CONCLUSIÓN:** {opinion['conclusion']}")
        print("---")
    
    print("\n¡Magnífico trabajo construyendo tus propias opiniones con una estructura sólida!")
    esperar(limpiar=True)


def mostrar_menu():
    while True:
        limpiar_consola()
        print("--- MENÚ DE LA LECCIÓN 6: OPINIONES ESTRUCTURADAS (8.º Grado Primaria) ---")
        print("\n1. Teoría (¡Aprendemos a construir opiniones fuertes!)")
        print("2. Ejemplos (¡Vemos opiniones bien hechas!)")
        print("3. Ejercicios (¡A organizar nuestras ideas!)")
        print("4. Crear Mis Propias Opiniones (¡Construye tus propios argumentos!)")
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
            print("\n¡Gracias por aprender a expresar tus ideas con estructura! ¡Tu voz es importante!")
            sys.exit()
        else:
            print("\nOpción no válida. Por favor, elige un número del 1 al 5.")
            esperar()

# Iniciar la aplicación
if __name__ == "__main__":
    mostrar_menu()
