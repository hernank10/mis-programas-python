def mostrar_reglas():
    """
    Muestra las reglas del uso de 'i', 'y' (ye) y dígrafos en castellano.
    """
    reglas = """
    Reglas del uso de 'i', 'y' (ye) y dígrafos en castellano:

    1. Uso de la 'i':
       - La letra 'i' se utiliza como vocal tónica o átona.
       - Se usa en los infinitivos de los verbos de la segunda y tercera conjugación.
       - Forma parte de diptongos y triptongos.
       Ejemplos: 'viviendo', 'ciudad', 'pierna', 'aire'.

    2. Uso de la 'y':
       - La letra 'y' puede ser una conjunción copulativa que se usa para unir palabras o frases.
       - Se utiliza como fonema en posición final de palabra.
       - Se encuentra en palabras de origen griego.
       Ejemplos: 'hoy', 'rey', 'yate', 'yogur'.

    3. Uso de dígrafos:
       - 'll': Representa un solo sonido en español. Ejemplos: 'llama', 'calle'
       - 'ch': Representa un solo sonido. Ejemplos: 'chico', 'muchacho'.
       - 'qu': Utilizado para representar el sonido /k/ antes de 'e' o 'i'. Ejemplos: 'queso', 'química'.
       - 'gu': Utilizado para representar el sonido /g/ antes de 'e' o 'i'. Ejemplos: 'guerra', 'guitarra'.

    4. La letra "i" es la novena letra del alfabeto español y su uso está ampliamente extendido en la formación de palabras. Aquí se presentan algunas de sus reglas y usos más importantes:
       1.	Vocal tónica y átona: La "i" puede ser una vocal tónica (con acento) o átona (sin acento). Ejemplos de "i" tónica incluyen palabras como "librería" y "maría", mientras que ejemplos de "i" átona incluyen "camino" y "amigo".
       2.	Diptongos y triptongos: La "i" forma diptongos cuando se combina con otra vocal en la misma sílaba, como en "aire" y "ciudad". También puede formar triptongos, como en "limpiáis" y "estudiáis".
       3.	Infinitivos y formas verbales: La "i" es común en los infinitivos de los verbos de la segunda conjugación (-er) y tercera conjugación (-ir), como en "vivir" y "temer". También aparece en muchas formas verbales, como en "comía" y "decía".

    """
    print(reglas)

def verificar_reglas():
    """
    Pide al usuario que escriba nuevamente las reglas y verifica la exactitud.
    """
    reglas_originales = """
    1. Uso de la 'i':
       - La letra 'i' se utiliza como vocal tónica o átona.
       - Se usa en los infinitivos de los verbos de la segunda y tercera conjugación.
       - Forma parte de diptongos y triptongos.
       Ejemplos: 'viviendo', 'ciudad', 'pierna', 'aire'.

    2. Uso de la 'y':
       - La letra 'y' puede ser una conjunción copulativa que se usa para unir palabras o frases.
       - Se utiliza como fonema en posición final de palabra.
       - Se encuentra en palabras de origen griego.
       Ejemplos: 'hoy', 'rey', 'yate', 'yogur'.

    3. Uso de dígrafos:
       - 'll': Representa un solo sonido en español. Ejemplos: 'llama', 'calle'.
       - 'ch': Representa un solo sonido. Ejemplos: 'chico', 'muchacho'.
       - 'qu': Utilizado para representar el sonido /k/ antes de 'e' o 'i'. Ejemplos: 'queso', 'química'.
       - 'gu': Utilizado para representar el sonido /g/ antes de 'e' o 'i'. Ejemplos: 'guerra', 'guitarra'.
    """
    
    print("\nEscribe las reglas que acabas de leer (no copies y pegues):\n")
    usuario_reglas = input().strip()
    
    if usuario_reglas == reglas_originales.strip():
        print("\n¡Correcto! Has memorizado bien las reglas.")
    else:
        print("\nHay algunas diferencias. Por favor, revisa y vuelve a intentarlo.")
        diferencias = mostrar_diferencias(usuario_reglas, reglas_originales.strip())
        print("\nDiferencias encontradas:\n")
        print(diferencias)

def mostrar_diferencias(texto1, texto2):
    """
    Muestra las diferencias entre dos textos.
    """
    import difflib
    texto1_lineas = texto1.splitlines()
    texto2_lineas = texto2.splitlines()
    
    d = difflib.Differ()
    diferencias = list(d.compare(texto1_lineas, texto2_lineas))
    return '\n'.join(diferencias)

def main():
    print("Bienvenido al programa para memorizar las reglas de 'i', 'y' (ye) y dígrafos en castellano.\n")
    
    mostrar_reglas()
    
    while True:
        opcion = input("\n¿Listo para escribir las reglas? (s/n): ").strip().lower()
        
        if opcion == 's':
            verificar_reglas()
            break
        elif opcion == 'n':
            print("Tómate tu tiempo y vuelve cuando estés listo.")
            break
        else:
            print("Opción no válida. Por favor, ingresa 's' para sí o 'n' para no.")

if __name__ == "__main__":
    main()
