import random

ejemplos = [
    ("Bastantes problemas tenemos...", "Bastantes problemas no tenemos..."),
    ("Con poco se conforma María.", "Con poco no se conforma María."),
    ("Eso haría él.", "Eso no haría él."),
    ("Muchas cosas aprendimos en la escuela.", "Muchas cosas no aprendimos en la escuela."),
    ("Gran esfuerzo hicieron para ganar.", "Gran esfuerzo no hicieron para ganar."),
    ("Rápidamente salió del salón.", "Rápidamente no salió del salón."),
    ("Fácil solución encontraron.", "Fácil solución no encontraron."),
    ("Ese consejo me dio mi padre.", "Ese consejo no me dio mi padre."),
    ("Un problema difícil enfrentamos ayer.", "Un problema difícil no enfrentamos ayer."),
    ("Tal decisión tomaron los jueces.", "Tal decisión no tomaron los jueces."),
    ("Muy tarde llegaron los invitados.", "Muy tarde no llegaron los invitados."),
    ("Grandes avances lograron en poco tiempo.", "Grandes avances no lograron en poco tiempo."),
    ("Otro camino eligieron los exploradores.", "Otro camino no eligieron los exploradores."),
    ("Ese problema resolvió el ingeniero.", "Ese problema no resolvió el ingeniero."),
    ("Un gran susto nos llevamos.", "Un gran susto no nos llevamos."),
    ("Mucho dinero gastaron en la boda.", "Mucho dinero no gastaron en la boda."),
    ("Varias soluciones propusieron en la reunión.", "Varias soluciones no propusieron en la reunión."),
    ("Ese consejo siguió Pedro.", "Ese consejo no siguió Pedro."),
    ("Demasiada confianza tenían en el proyecto.", "Demasiada confianza no tenían en el proyecto."),
    ("Gran impacto tuvo la noticia.", "Gran impacto no tuvo la noticia."),
]

def practicar():
    print("Bienvenido al ejercicio de incompatibilidad de la negación en estructuras con anteposición.")
    print("Deberás indicar si la versión negativa de la oración es correcta o incorrecta.")
    puntuacion = 0
    random.shuffle(ejemplos)
    
    for afirmativa, negativa in ejemplos:
        print("\nOración original:")
        print(afirmativa)
        print("\nVersión negativa:")
        print(negativa)
        respuesta = input("¿Es correcta la versión negativa? (sí/no): ").strip().lower()
        
        if respuesta == "no":
            print("Correcto. La negación en esta estructura no es compatible.")
            puntuacion += 1
        else:
            print("Incorrecto. La negación en esta estructura no es compatible.")
        
    print(f"\nTu puntuación final es: {puntuacion}/{len(ejemplos)}")
    print("¡Gracias por participar!")

if __name__ == "__main__":
    practicar()
