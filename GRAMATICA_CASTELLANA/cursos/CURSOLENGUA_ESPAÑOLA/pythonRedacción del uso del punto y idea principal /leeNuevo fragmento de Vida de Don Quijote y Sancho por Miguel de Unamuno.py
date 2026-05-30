# -*- coding: utf-8 -*-
import textwrap

# Nuevo fragmento de "Vida de Don Quijote y Sancho" por Miguel de Unamuno
fragmento = """
Pero no ha mucho tiempo que vino a escribir la historia de los ingeniosos caballeros Don Quijote de la Mancha y Sancho Panza, su escudero, Miguel de Unamuno, y en ella hallamos una serie de observaciones y reflexiones sobre los caracteres de estos dos personajes, los cuales resultan ser de gran interés.

Don Quijote, a quien en realidad llamaban Alonso Quijano, era un hidalgo pobre, pero de espíritu noble y aventurero. A pesar de sus pocos recursos, decidió armarse caballero andante y salir en busca de aventuras, decidido a deshacer entuertos y a defender la justicia. Su carácter idealista y soñador lo lleva a ver el mundo no como es, sino como él cree que debería ser.

Sancho Panza, su fiel escudero, es un labrador bonachón y práctico, que acompaña a Don Quijote en sus andanzas. A diferencia de su amo, Sancho ve el mundo tal como es, con sus dificultades y realidades cotidianas. Su lealtad a Don Quijote, a pesar de no compartir sus fantasías, demuestra una amistad profunda y sincera.

Estos personajes representan dos visiones del mundo: la idealista y la realista, y a través de sus interacciones, Unamuno nos invita a reflexionar sobre la naturaleza humana y la búsqueda del ideal.
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

def solicitar_detalles_personajes():
    print("\nDescriba los personajes mencionados en el texto y proporcione más detalles sobre ellos.")
    print("Puede hablar sobre sus características, comportamientos y cualquier otra información relevante.")
    descripcion_don_quijote = input("Descripción de Don Quijote: ")
    descripcion_sancho_panza = input("Descripción de Sancho Panza: ")
    return descripcion_don_quijote, descripcion_sancho_panza

def reflexionar_puntuacion():
    print("\nReflexione acerca del uso del punto y seguido y del punto y aparte en el texto proporcionado.")
    reflexion = input("Su reflexión: ")
    return reflexion

def main():
    mostrar_fragmento()
    observacion = solicitar_observacion()
    descripcion_don_quijote, descripcion_sancho_panza = solicitar_detalles_personajes()
    reflexion = reflexionar_puntuacion()

    print("\nSu observación:")
    print(observacion)
    print("\nDescripción de Don Quijote:")
    print(descripcion_don_quijote)
    print("\nDescripción de Sancho Panza:")
    print(descripcion_sancho_panza)
    print("\nSu reflexión sobre el uso del punto y seguido y del punto y aparte:")
    print(reflexion)

if __name__ == "__main__":
    main()
