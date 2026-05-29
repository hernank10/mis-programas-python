import random
import time
import threading

vidas_iniciales = 3
tiempo_limite = 15  # segundos por pregunta

# Teoría como "diapositivas"
teoria = [
    "📘 Las colocaciones léxicas son combinaciones fijas entre verbos y sustantivos.",
    "📘 No se pueden deducir por lógica: se aprende por uso y contexto.",
    "✅ Ejemplos correctos: 'dar una vuelta', 'cunde el desaliento', 'contraer matrimonio'.",
    "❌ Ejemplos incorrectos: 'hacer una vuelta', 'surge el desaliento', 'crear matrimonio'.",
    "📌 Algunas colocaciones cambian según preposición: 'inverso de', 'contrario a'.",
    "✅ Usar bien las colocaciones mejora tu fluidez y naturalidad al hablar.",
]

# Diccionario de preguntas por nivel
preguntas_por_nivel = {
    "fácil": [
        {"frase": "Voy a ___ una vuelta por el parque.", "opciones": ["hacer", "dar", "crear", "formar"], "respuesta": "dar"},
        {"frase": "___ el desaliento en el ambiente escolar.", "opciones": ["Cunde", "Aparece", "Surge", "Emana"], "respuesta": "Cunde"},
        {"frase": "Van a ___ matrimonio pronto.", "opciones": ["formar", "crear", "contraer", "tener"], "respuesta": "contraer"}
    ],
    "intermedio": [
        {"frase": "Es importante ___ la virtud desde jóvenes.", "opciones": ["ejercer", "ejercitar", "imponer", "activar"], "respuesta": "ejercitar"},
        {"frase": "Este resultado es inverso ___ el anterior.", "opciones": ["a", "de", "con", "por"], "respuesta": "de"},
        {"frase": "Este argumento es contrario ___ tus ideas.", "opciones": ["con", "de", "a", "en"], "respuesta": "a"},
    ],
    "difícil": [
        {"frase": "Debemos ___ la actividad empresarial.", "opciones": ["crear", "activar", "desarrollar", "inventar"], "respuesta": "desarrollar"},
        {"frase": "___ influencia en el comportamiento del grupo.", "opciones": ["Ejercita", "Ejerce", "Aplica", "Expone"], "respuesta": "Ejerce"},
        {"frase": "Voy a ___ la consulta como abogado.", "opciones": ["atender", "consultar", "evacuar", "resolver"], "respuesta": "evacuar"}
    ]
}

ejemplos_usuario = []

# Temporizador
def temporizador(tiempo, evento):
    time.sleep(tiempo)
    if not evento.is_set():
        print("\n⏰ ¡Se acabó el tiempo!")
        evento.set()

# Función para jugar
def jugar(nivel):
    preguntas = preguntas_por_nivel[nivel]
    random.shuffle(preguntas)
    vidas = vidas_iniciales
    puntaje = 0
    for i, pregunta in enumerate(preguntas, 1):
        print(f"\n🔹 Pregunta {i} ({nivel.capitalize()})")
        print(pregunta["frase"])
        for idx, opcion in enumerate(pregunta["opciones"], 1):
            print(f"  {idx}. {opcion}")

        evento = threading.Event()
        hilo = threading.Thread(target=temporizador, args=(tiempo_limite, evento))
        hilo.start()

        try:
            respuesta_usuario = input(f"Responde en {tiempo_limite} segundos (1-{len(pregunta['opciones'])}): ")
            evento.set()
            if not respuesta_usuario.isdigit() or not (1 <= int(respuesta_usuario) <= len(pregunta["opciones"])):
                raise
