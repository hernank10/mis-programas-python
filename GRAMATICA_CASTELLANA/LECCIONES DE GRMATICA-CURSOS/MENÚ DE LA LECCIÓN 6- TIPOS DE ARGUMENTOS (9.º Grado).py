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
    print("📚 **TEORÍA: TIPOS DE ARGUMENTOS - ¡CONVENCIENDO CON ESTRATEGIA!** 📚")
    print("---")
    
    print("\n1. **Recordando: ¿Por Qué Argumentar?** 🤔")
    print("   Una opinión fuerte no es solo lo que creemos, sino por qué lo creemos y con qué pruebas podemos demostrarlo.")
    print("   Los **argumentos** son las razones que usamos para apoyar nuestra postura. ¡Pero no todos los argumentos son iguales!")
    print("   Existen diferentes tipos de argumentos que nos ayudan a convencer de distintas maneras.")
    esperar()

    print("\n2. **Argumentos Lógicos: La Fuerza de la Razón** 🧠")
    print("   Estos argumentos se basan en la **razón**, la **lógica** y las relaciones de **causa y efecto**.")
    print("   Si las premisas son verdaderas, la conclusión debe serlo. Piensa en 'si... entonces...'.")
    print("   - **Ejemplo:** 'Si no consumes suficiente agua, tu cuerpo se deshidrata, por lo tanto, debes beber agua regularmente para mantener tu salud.'")
    print("   - Se usan hechos, estadísticas generales o principios que parecen de 'sentido común'.")
    esperar()

    print("\n3. **Argumentos de Autoridad: La Voz del Experto** 👨‍🏫👩‍🔬")
    print("   Se basan en la opinión o el conocimiento de una **persona, institución o estudio que es reconocido como experto** en el tema.")
    print("   Es importante que la autoridad sea creíble y relevante para el tema.")
    print("   - **Ejemplo:** 'Según la Organización Mundial de la Salud (OMS), la actividad física moderada ayuda a prevenir enfermedades crónicas.'")
    print("   - Fíjate en frases como: 'Según [experto]...', 'Estudios de [institución] demuestran...'.")
    esperar()

    print("\n4. **Argumentos de Experiencia: Lo Vivido y lo Observado** 🚶‍♀️🌟")
    print("   Se apoyan en **experiencias personales, anécdotas, observaciones o situaciones** que tú o alguien más ha vivido directamente.")
    print("   Son efectivos porque humanizan el argumento y pueden conectar emocionalmente con el público.")
    print("   - **Ejemplo:** 'Sé que el trabajo en equipo es fundamental, porque en mi último proyecto escolar, cuando todos colaboramos, logramos un resultado excelente que no habríamos conseguido solos.'")
    print("   - A menudo usan frases como: 'Mi experiencia me dice...', 'He observado que...', 'Un caso que conozco es...'.")
    esperar(limpiar=True)

def mostrar_ejemplos():
    limpiar_consola()
    print("💡 **EJEMPLOS: ¡IDENTIFICANDO TIPOS DE ARGUMENTOS!** 💡")
    print("---")

    print("\n**Ejemplo 1:** 'Si reciclamos más, reduciremos la contaminación del medio ambiente y ayudaremos a conservar los recursos naturales. Por eso, el reciclaje es vital.'")
    print(" - **Tipo:** Lógico (Causa y Efecto: reciclar --> menos contaminación, más conservación).")
    esperar()

    print("\n**Ejemplo 2:** 'El famoso científico Stephen Hawking afirmó que la inteligencia es la capacidad de adaptarse al cambio. Esto demuestra su importancia en la vida.'")
    print(" - **Tipo:** Autoridad (Se cita a un científico reconocido).")
    esperar()

    print("\n**Ejemplo 3:** 'En mi viaje a la selva amazónica, vi con mis propios ojos cómo la deforestación está destruyendo hábitats, por lo que es urgente proteger estos ecosistemas.'")
    print(" - **Tipo:** Experiencia (Se basa en una observación personal directa).")
    esperar()

    print("\n**Ejemplo 4:** 'Las vitaminas son esenciales para el buen funcionamiento del cuerpo, ya que ayudan en procesos como la visión, el crecimiento y la inmunidad.'")
    print(" - **Tipo:** Lógico (Principio general de funcionamiento biológico).")
    esperar()

    print("\n**Ejemplo 5:** 'Según el director de nuestra escuela, la puntualidad es clave para el éxito académico, porque demuestra responsabilidad y compromiso.'")
    print(" - **Tipo:** Autoridad (Se cita al director de la escuela, una figura de autoridad en ese contexto).")
    esperar(limpiar=True)


def realizar_ejercicios():
    limpiar_consola()
    print("📝 **EJERCICIOS: ¡CLASIFICANDO ARGUMENTOS!** 📝")
    print("---")
    print("Lee cada argumento y escribe si es **LÓGICO**, de **AUTORIDAD** o de **EXPERIENCIA**.")
    esperar("¡Manos a la obra!")

    ejercicios = [
        {"argumento": "Si comes una dieta balanceada y haces ejercicio, tendrás una vida más saludable. Por eso, la vida sana es importante.", "respuesta": "lógico", "pista": "Piensa en causa-efecto."},
        {"argumento": "Mi profesor de historia siempre dice que 'quien no conoce su historia, está condenado a repetirla'.", "respuesta": "autoridad", "pista": "Hay una figura citada."},
        {"argumento": "Después de pasar un año estudiando inglés, ahora puedo ver películas sin subtítulos, lo que demuestra que la práctica constante funciona.", "respuesta": "experiencia", "pista": "Es una vivencia personal."},
        {"argumento": "Según la NASA, el universo está en constante expansión, lo que implica que siempre hay algo nuevo por descubrir.", "respuesta": "autoridad", "pista": "Organización científica reconocida."},
        {"argumento": "Si mezclas azul y amarillo, obtendrás verde. Esta regla se aplica en todas las pinturas.", "respuesta": "lógico", "pista": "Es una regla o principio universal."},
        {"argumento": "En mi vecindario, cuando la gente se organiza para limpiar las calles, todo se ve mejor y hay menos basura.", "respuesta": "experiencia", "pista": "Es una observación de tu entorno."},
        {"argumento": "La lectura fomenta la empatía, porque nos permite ver el mundo desde diferentes perspectivas.", "respuesta": "lógico", "pista": "Es una relación de causa-efecto (leer -> empatía)."},
        {"argumento": "El Dr. García, especialista en psicología infantil, asegura que establecer rutinas ayuda a los niños a sentirse más seguros.", "respuesta": "autoridad", "pista": "Se cita a un experto."},
        {"argumento": "Aprendí que no debo dejar mis cosas tiradas, ya que una vez perdí mi juguete favorito por desordenado.", "respuesta": "experiencia", "pista": "Es una anécdota personal."},
        {"argumento": "Si las temperaturas globales siguen subiendo, el nivel del mar aumentará, afectando las ciudades costeras.", "respuesta": "lógico", "pista": "Consecuencia de una acción."},
        {"argumento": "La Constitución de Colombia garantiza la libertad de expresión a todos sus ciudadanos.", "respuesta": "autoridad", "pista": "Es una ley o documento legal."},
        {"argumento": "Cuando me esforcé mucho en matemáticas, logré entender temas complejos que antes me parecían imposibles.", "respuesta": "experiencia", "pista": "Relato de un logro personal."},
        {"argumento": "Todos los seres vivos necesitan agua para sobrevivir; por lo tanto, el agua es fundamental para la vida en la Tierra.", "respuesta": "lógico", "pista": "Principio biológico universal."},
        {"argumento": "El estudio publicado en la revista 'Nature' concluye que el ejercicio al aire libre mejora la salud mental.", "respuesta": "autoridad", "pista": "Publicación científica."},
        {"argumento": "Después de varios intentos, descubrí que la mejor manera de aprender a programar es practicando cada día.", "respuesta": "experiencia", "pista": "Conclusión de tu propia práctica."},
        {"argumento": "Si un objeto se lanza al aire, la gravedad hará que caiga de vuelta al suelo. Es una ley física.", "respuesta": "lógico", "pista": "Es una ley o principio científico."},
        {"argumento": "Mi abuelo, que fue agricultor toda su vida, siempre decía que 'la tierra da lo que se le siembra'.", "respuesta": "autoridad", "pista": "Sabiduría popular o experiencia de una figura respetada."},
        {"argumento": "Cuando viajo, prefiero llevar mochila que maleta, porque he comprobado que es más cómodo para moverse.", "respuesta": "experiencia", "pista": "Basado en tu propia comodidad comprobada."},
        {"argumento": "La falta de sueño provoca irritabilidad y reduce la capacidad de atención. Por eso, dormir bien es crucial.", "respuesta": "lógico", "pista": "Relación directa de causa y efecto."},
        {"argumento": "La Real Academia Española define 'resiliencia' como la capacidad de adaptarse frente a la adversidad.", "respuesta": "autoridad", "pista": "Se cita una fuente de conocimiento lingüístico."},
    ]

    puntuacion = 0
    
    random.shuffle(ejercicios) # Mezclar ejercicios

    for i, ej in enumerate(ejercicios):
        print(f"\n--- Ejercicio {i+1}/20 ---")
        print(f"Argumento: '{ej['argumento']}'")
        
        valido = False
        while not valido:
            respuesta_usuario = input("¿Qué tipo de argumento es? (LÓGICO / AUTORIDAD / EXPERIENCIA): ").strip().lower()
            if respuesta_usuario in ["lógico", "logico", "autoridad", "experiencia"]:
                valido = True
            else:
                print("Por favor, responde con 'LÓGICO', 'AUTORIDAD' o 'EXPERIENCIA'.")

        if respuesta_usuario == ej['respuesta'].lower() or (respuesta_usuario == "logico" and ej['respuesta'].lower() == "lógico"):
            print("✅ ¡Correcto! ¡Identificaste el tipo de argumento!")
            puntuacion += 1
        else:
            print(f"❌ ¡Incorrecto! La respuesta correcta era: '{ej['respuesta'].upper()}'.")
            print(f"Pista: {ej['pista']}")
        
        esperar()

    limpiar_consola()
    print("--- ¡FIN DE LOS EJERCICIOS! ---")
    print(f"\nHas completado los ejercicios. ¡Tu puntuación final es: {puntuacion}/{len(ejercicios)}!")
    if puntuacion >= 16:
        print("🎉 ¡Excelente! ¡Eres un estratega en la argumentación!")
    elif puntuacion >= 10:
        print("👍 ¡Muy bien! Ya entiendes los diferentes tipos de argumentos.")
    else:
        print("✍️ ¡Sigue practicando! Con más esfuerzo, ¡distinguirás cada argumento sin problema!")
    esperar(limpiar=True)


def crear_ejemplos_propios():
    limpiar_consola()
    print("✍️ **¡CREA TUS PROPIOS ARGUMENTOS!** ✍️")
    print("---")
    print("Vamos a practicar creando un argumento de cada tipo para una postura. ¡Usa tu creatividad!")
    esperar("¡Empecemos a construir!")

    print("\n--- PASO 1: Elige una postura (lo que vas a defender) ---")
    postura_elegida = input("Escribe una postura (ej: 'El uso de bicicletas debería promoverse más.'): ").strip()
    
    print(f"\nTu postura es: '{postura_elegida}'")
    print("Ahora, vamos a crear un argumento de cada tipo para apoyarla.")

    argumentos_creados = {
        "logico": "",
        "autoridad": "",
        "experiencia": ""
    }

    # Argumento Lógico
    print("\n--- Crea un ARGUMENTO LÓGICO para tu postura ---")
    print("Piensa en una razón basada en causa-efecto o en principios generales.")
    argumentos_creados["logico"] = input("Tu argumento lógico: ").strip()

    # Argumento de Autoridad
    print("\n--- Crea un ARGUMENTO DE AUTORIDAD para tu postura ---")
    print("Piensa en una persona o institución experta que apoye tu idea.")
    argumentos_creados["autoridad"] = input("Tu argumento de autoridad: ").strip()

    # Argumento de Experiencia
    print("\n--- Crea un ARGUMENTO DE EXPERIENCIA para tu postura ---")
    print("Piensa en una anécdota personal o una observación que hayas hecho.")
    argumentos_creados["experiencia"] = input("Tu argumento de experiencia: ").strip()

    limpiar_consola()
    print("--- ¡TUS ARGUMENTOS CREADOS! ---")
    print(f"\n**Tu postura:** {postura_elegida}")
    print("\n**Aquí están los argumentos que creaste para apoyarla:**")
    print(f"  - **LÓGICO:** '{argumentos_creados['logico']}'")
    print(f"  - **DE AUTORIDAD:** '{argumentos_creados['autoridad']}'")
    print(f"  - **DE EXPERIENCIA:** '{argumentos_creados['experiencia']}'")
    
    print("\n¡Excelente trabajo pensando estratégicamente para apoyar tus ideas!")
    esperar(limpiar=True)


def mostrar_menu():
    while True:
        limpiar_consola()
        print("--- MENÚ DE LA LECCIÓN 6: TIPOS DE ARGUMENTOS (9.º Grado) ---")
        print("\n1. Teoría (¡Aprendemos la variedad de razones para convencer!)")
        print("2. Ejemplos (¡Vemos los argumentos en acción!)")
        print("3. Ejercicios (¡A clasificar los argumentos!)")
        print("4. Crear Mis Propios Argumentos (¡Construye tus propias razones!)")
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
            print("\n¡Gracias por aprender a convencer con estrategia! ¡Sigue fortaleciendo tu capacidad argumentativa!")
            sys.exit()
        else:
            print("\nOpción no válida. Por favor, elige un número del 1 al 5.")
            esperar()

# Iniciar la aplicación
if __name__ == "__main__":
    mostrar_menu()
