import random

# ==========================
# LISTA DE EJERCICIOS
# ==========================
exercises = [
    # Adición
    ("Me gusta el café y también el té.", "I like coffee and tea too."),
    ("Estudio inglés y además aprendo francés.", "I study English and also learn French."),
    ("Ella canta y además toca la guitarra.", "She sings and also plays the guitar."),
    ("No solo lee, sino que también escribe.", "He not only reads but also writes."),
    ("Estaba cansado, además tenía hambre.", "He was tired; moreover, he was hungry."),
    
    # Contraste
    ("Quiero salir, pero está lloviendo.", "I want to go out, but it is raining."),
    ("Es inteligente, sin embargo, es muy humilde.", "He is smart; however, he is very humble."),
    ("Aunque estaba cansado, siguió trabajando.", "Although he was tired, he kept working."),
    ("Estudia mucho, mientras que su hermano es perezoso.", "He studies a lot, whereas his brother is lazy."),
    ("Es caro, pero vale la pena.", "It is expensive, yet it is worth it."),
    
    # Causa
    ("No vino porque estaba enfermo.", "He didn’t come because he was sick."),
    ("Se quedó en casa ya que llovía.", "She stayed home since it was raining."),
    ("Como no tenía dinero, no pudo comprarlo.", "As he had no money, he couldn’t buy it."),
    ("Puesto que llegaste tarde, empezamos sin ti.", "Since you arrived late, we started without you."),
    ("Debido a la lluvia, cancelaron el partido.", "Due to the rain, they canceled the match."),
    
    # Consecuencia
    ("Estudió mucho, por lo tanto aprobó.", "He studied a lot, therefore he passed."),
    ("Estaba cansada, así que se fue a dormir.", "She was tired, so she went to bed."),
    ("Llovió fuerte, en consecuencia hubo inundaciones.", "It rained heavily; consequently, there were floods."),
    ("No entendió nada, por eso pidió ayuda.", "He didn’t understand anything; that’s why he asked for help."),
    ("Se perdió el bus, de modo que llegó tarde.", "He missed the bus, so he arrived late."),
    
    # Tiempo
    ("Me llamarás cuando llegues.", "You will call me when you arrive."),
    ("Antes de salir, apaga la luz.", "Before leaving, turn off the light."),
    ("Después de cenar, veremos una película.", "After dinner, we will watch a movie."),
    ("Mientras cocinaba, escuchaba música.", "While she was cooking, she was listening to music."),
    ("Tan pronto como llegue, te avisaré.", "As soon as I arrive, I will let you know."),
    
    # Condición
    ("Si estudias, aprobarás.", "If you study, you will pass."),
    ("A menos que llueva, iremos al parque.", "Unless it rains, we will go to the park."),
    ("En caso de que necesites ayuda, llámame.", "In case you need help, call me."),
    ("Con tal de que practiques, mejorarás.", "As long as you practice, you will improve."),
    ("Siempre que vengas, serás bienvenido.", "Whenever you come, you will be welcome."),
    
    # Finalidad
    ("Estudia para que apruebes el examen.", "Study so that you pass the exam."),
    ("Trabaja duro a fin de lograr tus metas.", "Work hard in order to achieve your goals."),
    ("Se esforzó con el fin de ganar la competencia.", "He worked hard in order to win the competition."),
    ("Guardó silencio para no molestar.", "He kept silent so as not to disturb."),
    ("Escribe despacio para que todos entiendan.", "Write slowly so that everyone understands."),
    
    # Resumen/Conclusión
    ("En resumen, debemos trabajar juntos.", "In short, we must work together."),
    ("En conclusión, la investigación fue un éxito.", "In conclusion, the research was a success."),
    ("Para resumir, no tenemos tiempo.", "To sum up, we don’t have time."),
    ("En pocas palabras, la vida es corta.", "In a nutshell, life is short."),
    ("En definitiva, tomaremos la decisión mañana.", "Ultimately, we will make the decision tomorrow."),
]

# Ampliamos hasta 100 repitiendo con variantes
while len(exercises) < 100:
    exercises.extend(exercises[:100-len(exercises)])

# ==========================
# FUNCIONES DEL JUEGO
# ==========================
def play():
    score = 0
    random.shuffle(exercises)

    print("=== PRÁCTICA DE CONECTORES EN INGLÉS ===")
    print("Escribe la traducción en inglés.")
    print("Comandos: 'help' (pista), 'show' (respuesta), 'exit' (salir)\n")

    for i, (spanish, english) in enumerate(exercises, 1):
        print(f"Ejercicio {i}: {spanish}")
        answer = input("Tu respuesta: ").strip()

        if answer.lower() == "exit":
            break
        elif answer.lower() == "help":
            print(f"Pista: {english.split()[0]} ...\n")
            continue
        elif answer.lower() == "show":
            print(f"Respuesta correcta: {english}\n")
            continue

        if answer.lower() == english.lower():
            print("✅ Correcto!\n")
            score += 1
        else:
            print(f"❌ Incorrecto. Respuesta esperada: {english}\n")

    print(f"Tu puntaje final: {score}/{i}")

# ==========================
# EJECUCIÓN
# ==========================
if __name__ == "__main__":
    play()
