def mostrar_instrucciones():
    print("""
    Instrucciones:
    1. Introduce una oración o párrafo.
    2. Selecciona el caso en el que deseas practicar el uso de la coma.
    3. El programa te permitirá colocar las comas en los lugares adecuados.
    
    Casos:
    1. Comas entre palabras de la misma índole (nombres, adjetivos, etc.).
    2. Comas para separar elementos en una enumeración.
    3. Comas para separar cláusulas independientes en una oración compuesta.
    4. Comas para separar elementos en una serie de adjetivos.
    5. Comas para indicar aposición.
    6. Comas para separar elementos en una fecha o dirección.
    7. Comas para indicar el vocativo.
    8. Comas para separar elementos en una lista de elementos coordinados.
    9. Comas para separar elementos en una cita textual.
    10. Comas para separar elementos en una oración con aposición explicativa.
    11. Comas para separar elementos en una oración con incisos o aclaraciones.
    12. Comas para separar elementos en una oración con expresiones explicativas o de énfasis.
    """)

def obtener_oracion():
    return input("Introduce una oración o párrafo: ")

def seleccionar_caso():
    print("""
    Selecciona el caso:
    1. Comas entre palabras de la misma índole (nombres, adjetivos, etc.).
    2. Comas para separar elementos en una enumeración.
    3. Comas para separar cláusulas independientes en una oración compuesta.
    4. Comas para separar elementos en una serie de adjetivos.
    5. Comas para indicar aposición.
    6. Comas para separar elementos en una fecha o dirección.
    7. Comas para indicar el vocativo.
    8. Comas para separar elementos en una lista de elementos coordinados.
    9. Comas para separar elementos en una cita textual.
    10. Comas para separar elementos en una oración con aposición explicativa.
    11. Comas para separar elementos en una oración con incisos o aclaraciones.
    12. Comas para separar elementos en una oración con expresiones explicativas o de énfasis.
    """)
    while True:
        try:
            seleccion = int(input("Introduce el número correspondiente al caso: "))
            if 1 <= seleccion <= 12:
                return seleccion
            else:
                print("Por favor, introduce un número entre 1 y 12.")
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número.")

def modificar_oracion(oracion, caso):
    if caso == 1:
        print("Ejemplo: Juan, Pedro, María y Ana son amigos.")
    elif caso == 2:
        print("Ejemplo: Me gusta leer, escribir, pintar y bailar.")
    elif caso == 3:
        print("Ejemplo: Estudia mucho, y obtendrás buenas calificaciones.")
    elif caso == 4:
        print("Ejemplo: El perro grande, peludo y juguetón corre por el parque.")
    elif caso == 5:
        print("Ejemplo: Mi hermano, el médico, trabaja en el hospital.")
    elif caso == 6:
        print("Ejemplo: Nací el 10 de mayo de 1990, en Bogotá, Colombia.")
    elif caso == 7:
        print("Ejemplo: María, ven aquí.")
    elif caso == 8:
        print("Ejemplo: Compré manzanas, peras, plátanos y uvas.")
    elif caso == 9:
        print("Ejemplo: El profesor dijo: ‘Estudien para el examen’.")
    elif caso == 10:
        print("Ejemplo: Mi hermano, que es médico, trabaja en el hospital.")
    elif caso == 11:
        print("Ejemplo: El libro, según mi opinión, es excelente.")
    elif caso == 12:
        print("Ejemplo: El libro, en mi opinión, es excelente.")
    
    print("Tu oración original:")
    print(oracion)
    
    print("\nIntroduce tu oración con las comas correctas según la regla seleccionada:")
    oracion_modificada = input("Oración modificada: ")
    return oracion_modificada

def main():
    mostrar_instrucciones()
    
    while True:
        oracion = obtener_oracion()
        caso = seleccionar_caso()
        
        oracion_modificada = modificar_oracion(oracion, caso)
        print("\nOración modificada:")
        print(oracion_modificada)
        
        continuar = input("\n¿Quieres practicar otra oración? (s/n): ").lower()
        if continuar != 's':
            break

if __name__ == "__main__":
    main()
