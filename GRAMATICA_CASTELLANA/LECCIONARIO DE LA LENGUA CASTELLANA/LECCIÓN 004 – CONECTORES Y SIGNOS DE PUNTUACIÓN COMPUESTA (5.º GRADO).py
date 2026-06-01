# -*- coding: utf-8 -*-
import textwrap

# TEORÍA
teoria = """
LECCIÓN 004 – CONECTORES Y SIGNOS DE PUNTUACIÓN COMPUESTA (5.º GRADO)

Los conectores son palabras que enlazan ideas dentro de una oración o entre oraciones.
Ejemplos: y, pero, aunque, sin embargo, por eso, además, en cambio, luego...

Los signos de puntuación compuesta (como el punto y coma, los dos puntos, y los signos dobles: “”, ¿?, ¡!) ayudan a organizar mejor el texto y a expresar emociones o preguntas con claridad.

TIPOS DE CONECTORES:
– ADICIÓN: y, además, también
– CONTRASTE: pero, sin embargo, aunque
– CAUSA / CONSECUENCIA: porque, por eso, así que
– COMPARACIÓN / ALTERNANCIA: en cambio, sin embargo, mientras que
– TIEMPO: luego, después, entonces

EJEMPLOS:
1. Fui al parque, **pero** comenzó a llover. ➜ Contraste
2. Me gusta la historia; **además**, me interesa la geografía. ➜ Adición
3. Estaba enfermo, **por eso** no vino a clase. ➜ Consecuencia
4. “¿Quieres venir al cine?”, preguntó Laura. ➜ Diálogo con signos “ ”

Ahora completa las siguientes oraciones con el conector o signo correcto.
"""

print(textwrap.fill(teoria, width=90))
print("\n🔽 ESCRIBE EL CONECTOR O SIGNO QUE FALTA EN CADA ORACIÓN:\n")

# NUEVOS 20 EJERCICIOS
ejercicios = [
    ("Marcos estudió mucho; __, no logró aprobar el examen.", "sin embargo"),
    ("La niña lloraba; __, todos se acercaron a consolarla.", "por eso"),
    ("__ ¿cuántos libros leíste este mes?", "¿"),
    ("Estaba cansado, __ tenía que seguir trabajando.", "pero"),
    ("Lucía es amable; __, todos la respetan.", "por eso"),
    ("No solo canta bien, __ también baila excelente.", "sino"),
    ("“__ has llegado muy temprano”, dijo el maestro.", "¡"),
    ("No entendía la explicación; __, pidió ayuda.", "por eso"),
    ("Tienes que estudiar más, __ no vas a pasar el año.", "o"),
    ("No quiero chocolate __ galletas, gracias.", "ni"),
    ("Juan tomó el lápiz, la regla __ comenzó a trazar líneas.", "y"),
    ("Es muy puntual; __, siempre llega antes que los demás.", "de hecho"),
    ("__ ¡qué sorpresa verte por aquí!", "¡"),
    ("Algunos niños corren en el patio; __, otros prefieren leer.", "mientras"),
    ("Estaban viendo televisión; __, llegó papá con la cena.", "entonces"),
    ("Traje varias cosas: lápices, cuadernos __ colores.", "y"),
    ("Es divertido, __ a veces puede ser molesto.", "aunque"),
    ("No dijo una palabra; __, sus ojos lo decían todo.", "sin embargo"),
    ("__ ¿puedes ayudarme con la tarea?", "¿"),
    ("Tenía frío __ no llevaba abrigo.", "porque"),
]

# CORRECCIÓN
puntaje = 0
for i, (oracion, respuesta) in enumerate(ejercicios, 1):
    user_input = input(f"{i}. {oracion.replace('__', '___')}\nTu respuesta: ").strip().lower()
    if user_input == respuesta:
        print("✅ Correcto\n")
        puntaje += 1
    else:
        print(f"❌ Incorrecto. La respuesta correcta era: '{respuesta}'\n")

# RESULTADO FINAL
print(f"\n🎯 Puntaje final: {puntaje} de {len(ejercicios)}")
if puntaje == 20:
    print("🏆 ¡Excelente! Has logrado un resultado perfecto.")
elif puntaje >= 15:
    print("👍 Muy bien, ¡sigue practicando!")
else:
    print("📘 Te recomiendo repasar la teoría y volver a intentarlo.")
