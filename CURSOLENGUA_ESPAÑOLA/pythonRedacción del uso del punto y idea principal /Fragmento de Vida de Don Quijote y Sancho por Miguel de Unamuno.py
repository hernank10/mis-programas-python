# -*- coding: utf-8 -*-
import textwrap

# Fragmento de "Vida de Don Quijote y Sancho" por Miguel de Unamuno
fragmento = """
En un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero, adarga antigua, rocín flaco y galgo corredor. Una olla de algo más vaca que carnero, salpicón las más noches, duelos y quebrantos los sábados, lentejas los viernes, algún palomino de añadidura los domingos, consumían las tres partes de su hacienda.

El resto della concluían sayo de velarte, calzas de velludo para las fiestas con sus pantuflos de lo mesmo, los días de entre semana se honraba con su vellorí de lo más fino. Tenía en su casa una ama que pasaba de los cuarenta, y una sobrina que no llegaba a los veinte, y un mozo de campo y plaza, que así ensillaba el rocín como tomaba la podadera. Frisa la edad de nuestro hidalgo con los cincuenta años, era de complexión recia, seco de carnes, enjuto de rostro; gran madrugador y amigo de la caza.

Quieren decir que tenía el sobrenombre de Quijada, o Quesada, que en esto hay alguna diferencia en los autores que deste caso escriben; aunque por conjeturas verosímiles se deja entender que se llamaba Quejana. Pero esto importa poco a nuestro cuento; basta que en la narración dél no se salga un punto de la verdad.
"""

def mostrar_fragmento():
    print("Fragmento de 'Vida de Don Quijote y Sancho' por Miguel de Unamuno:\n")
    wrapped_text = textwrap.fill(fragmento, width=80)
    print(wrapped_text)

def solicitar_observacion():
    print("\nObserve cómo la idea principal crece a lo largo de los párrafos y cómo cada uno de ellos contiene un abordaje o aspecto distinto.")
    print("Relea el texto y escriba la idea principal o un aspecto del texto proporcionado.")
    observacion = input("Su observación: ")
    return observacion

def reflexionar_puntuacion():
    print("\nReflexione acerca del uso del punto y seguido y del punto y aparte en el texto proporcionado.")
    reflexion = input("Su reflexión: ")
    return reflexion

def main():
    mostrar_fragmento()
    observacion = solicitar_observacion()
    reflexion = reflexionar_puntuacion()

    print("\nSu observación:")
    print(observacion)
    print("\nSu reflexión sobre el uso del punto y seguido y del punto y aparte:")
    print(reflexion)

if __name__ == "__main__":
    main()
