# Lección 004 – 5.º grado: Conectores y signos de puntuación compuesta

ejercicios = [
    ("No me gusta el brócoli __ lo como porque es saludable.", "pero"),
    ("Llovía mucho __ decidimos no salir.", "por eso"),
    ("Salimos temprano __ el tráfico estaba terrible.", "aunque"),
    ("A Sofía le encanta leer novelas; __ a su hermana, los cómics.", "en cambio"),
    ("Tengo tres mascotas: un perro, un gato __ un pez.", "y"),
    ("María estudió toda la tarde __ no logró entender la lección.", "pero"),
    ("Juan es responsable; __, es muy puntual.", "además"),
    ("Quiero ir al cine __ no tengo dinero.", "pero"),
    ("__ ¿por qué estás tan triste?", "¡"),
    ("__ ¡qué hermoso paisaje!", "¡"),
    ("Hoy vamos a estudiar tres temas: historia, geografía __ matemáticas.", "y"),
    ("No me gusta madrugar __, debo hacerlo para ir al colegio.", "sin embargo"),
    ("Los estudiantes llegaron puntuales; __, organizaron sus carpetas.", "luego"),
    ("Quiero ir al parque __ mi madre no me deja salir solo.", "pero"),
    ("__ ¿quieres venir conmigo a la biblioteca?", "¿"),
    ("Había muchas tareas: matemáticas, ciencias, lenguaje __ sociales.", "y"),
    ("El cielo está nublado; __, sal sin paraguas bajo tu riesgo.", "así que"),
    ("Paula quiere mejorar sus notas; __, empezó a estudiar más.", "por eso"),
    ("__ ¡qué día tan agotador he tenido!", "¡"),
    ("La maestra dijo: “Saquen sus cuadernos __ copien los ejercicios.”", "y")
]

puntaje = 0

print("\n📝 Lección 004 – 5.º Grado\n")
print("Completa con el conector o signo de puntuación adecuado.\n")

for i, (oracion, respuesta_correcta) in enumerate(ejercicios, start=1):
    user_input = input(f"{i}. {oracion.replace('__', '___')}\nTu respuesta: ").strip().lower()
    
    if user_input == respuesta_correcta:
        print("✅ ¡Correcto!\n")
        puntaje += 1
    else:
        print(f"❌ Incorrecto. La respuesta correcta era: '{respuesta_correcta}'\n")

print(f"🎯 Puntaje final: {puntaje} de {len(ejercicios)}")
if puntaje == 20:
    print("🏆 ¡Excelente trabajo! Has completado todos los ejercicios correctamente.")
elif puntaje >= 15:
    print("👍 ¡Muy bien! Sigue practicando para llegar al 100%.")
else:
    print("📘 Revisa los conectores y signos de puntuación, y vuelve a intentarlo.")
