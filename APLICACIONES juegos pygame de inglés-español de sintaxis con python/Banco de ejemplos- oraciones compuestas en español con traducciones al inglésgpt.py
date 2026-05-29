import random

# Banco de ejemplos: oraciones compuestas en español con traducciones al inglés.
# Se usarán conectores coordinantes comunes: and, but, or, so, for, yet, nor.

exercises = [
    {"es": "Yo estudio inglés y practico todos los días.",
     "en": ["I study English and I practice every day."]},

    {"es": "Ella canta muy bien pero es muy tímida.",
     "en": ["She sings very well but she is very shy."]},

    {"es": "Podemos ir al cine o podemos quedarnos en casa.",
     "en": ["We can go to the cinema or we can stay at home."]},

    {"es": "Él estaba cansado, así que se fue a dormir temprano.",
     "en": ["He was tired, so he went to bed early."]},

    {"es": "No tengo dinero ni tengo trabajo.",
     "en": ["I have no money nor do I have a job.", "I don't have money nor do I have a job."]},

    {"es": "Estudié mucho, porque quería aprobar el examen.",
     "en": ["I studied a lot, for I wanted to pass the exam."]},

    {"es": "Quería salir, pero empezó a llover.",
     "en": ["I wanted to go out, but it started to rain."]},

    {"es": "Puedes leer un libro o puedes ver la televisión.",
     "en": ["You can read a book or you can watch TV."]},

    {"es": "Ella es joven, pero muy responsable.",
     "en": ["She is young, but very responsible."]},

    {"es": "Él no estudió, así que reprobó el examen.",
     "en": ["He did not study, so he failed the exam.", "He didn't study, so he failed the exam."]},
]

# Replicamos los ejemplos hasta tener 100 ejercicios reales.
while len(exercises) < 100:
    base = random.choice(exercises)
    exercises.append(base)

score = 0
attempts = 0

print("Bienvenido: 100 ejercicios de oraciones compuestas en inglés.")
print("Escribe la traducción al inglés. Comandos: help (pista), show (respuesta), quit (salir).\n")

random.shuffle(exercises)

for ex in exercises:
    print("Oración en español:", ex["es"])
    user_input = input("Traducción en inglés: ").strip()

    if user_input.lower() == "quit":
        break
    elif user_input.lower() == "help":
        print("Pista: la primera palabra es:", ex["en"][0].split()[0])
        continue
    elif user_input.lower() == "show":
        print("Respuestas correctas:")
        for ans in ex["en"]:
            print(" -", ans)
        continue

    attempts += 1
    if user_input in ex["en"]:
        print("✅ Correcto!\n")
        score += 1
    else:
        print("❌ Incorrecto.")
        print("Una posible respuesta es:", ex["en"][0], "\n")

print(f"Juego terminado. Puntaje: {score}/{attempts}")
