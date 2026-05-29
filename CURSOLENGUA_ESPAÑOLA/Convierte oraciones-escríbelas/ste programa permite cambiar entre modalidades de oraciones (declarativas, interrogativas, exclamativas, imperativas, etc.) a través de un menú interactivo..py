import random

# Lista de 100 oraciones sobre el tema de la codificación en Python, clasificadas por modalidad.
oraciones = [
    # Declarativas
    "Python es un lenguaje de programación muy popular.",
    "El código en Python es fácil de leer y escribir.",
    "Las listas en Python permiten almacenar múltiples valores.",
    "Los bucles en Python se usan para repetir acciones.",
    "El condicional if-else en Python se usa para tomar decisiones.",
    "Python tiene una amplia biblioteca estándar.",
    "Las funciones en Python ayudan a estructurar el código.",
    "Python admite programación orientada a objetos.",
    "La comunidad de Python es muy activa y ofrece mucho apoyo.",
    "El manejo de excepciones en Python es muy flexible.",
    # Interrogativas
    "¿Cómo se ejecuta un bucle en Python?",
    "¿Qué es una función lambda en Python?",
    "¿Puedes explicar cómo funcionan las listas en Python?",
    "¿Qué significa la palabra clave 'pass' en Python?",
    "¿Cómo se gestiona el manejo de errores en Python?",
    "¿Sabes cómo crear un diccionario en Python?",
    "¿Cuándo usas 'try' y 'except' en Python?",
    "¿Cuál es la sintaxis de un bucle for en Python?",
    "¿Qué tipo de datos maneja Python?",
    "¿Por qué es importante la indentación en Python?",
    # Imperativas
    "Escribe una función en Python que sume dos números.",
    "Utiliza un bucle for para recorrer una lista en Python.",
    "Declara una variable en Python y asigna un valor.",
    "Crea un programa en Python que verifique si un número es par.",
    "Usa la función input() para pedir datos al usuario en Python.",
    "Escribe un programa en Python que cuente cuántos elementos hay en una lista.",
    "Utiliza el módulo math de Python para realizar cálculos matemáticos.",
    "Escribe un script en Python que lea un archivo de texto.",
    "Declara una lista en Python con cinco elementos.",
    "Usa la sentencia if para comprobar si un número es mayor que otro en Python.",
    # Exclamativas
    "¡Python es un lenguaje increíble!",
    "¡Qué fácil es usar listas en Python!",
    "¡El manejo de errores en Python es muy flexible!",
    "¡Me encanta cómo Python maneja las funciones!",
    "¡Las expresiones lambda en Python son muy útiles!",
    "¡Es increíble cómo puedes hacer tanto con tan poco código en Python!",
    "¡Python hace que la programación sea divertida!",
    "¡Cuántas bibliotecas existen para Python!",
    "¡Qué genial es poder usar Python para procesamiento de datos!",
    "¡Las posibilidades con Python son infinitas!",
    # Desiderativas
    "Ojalá Python tuviera aún más bibliotecas para análisis de datos.",
    "Ojalá pudiera aprender Python más rápido.",
    "Ojalá todas las funciones en Python fueran tan fáciles de escribir.",
    "Ojalá hubiera más documentación sobre ciertas bibliotecas en Python.",
    "Ojalá más personas aprendieran a programar en Python.",
    "Ojalá todas las empresas usaran Python como su principal lenguaje.",
    "Ojalá los bucles en Python fueran más rápidos.",
    "Ojalá las listas en Python pudieran manejar más datos.",
    "Ojalá hubiera más tutoriales avanzados de Python en línea.",
    "Ojalá Python fuera aún más eficiente en procesamiento de grandes datos.",
    # Dubitativas
    "Tal vez Python sea el mejor lenguaje de programación.",
    "Tal vez debería aprender más sobre decoradores en Python.",
    "Tal vez las listas en Python no sean lo suficientemente rápidas.",
    "Tal vez los bucles en Python se pueden optimizar mejor.",
    "Tal vez debería aprender a usar numpy en Python.",
    "Tal vez la comunidad de Python me pueda ayudar con mi problema.",
    "Tal vez debería usar más funciones lambda en Python.",
    "Tal vez Python no sea la mejor opción para mi proyecto.",
    "Tal vez pueda escribir un código más eficiente en Python.",
    "Tal vez la sintaxis de Python no sea tan complicada como parece."
]

def convertir_oracion(oracion, modalidad):
    """Convierte una oración a la modalidad deseada."""
    if modalidad == 'interrogativa':
        return convertir_a_interrogativa(oracion)
    elif modalidad == 'imperativa':
        return convertir_a_imperativa(oracion)
    elif modalidad == 'exclamativa':
        return convertir_a_exclamativa(oracion)
    elif modalidad == 'desiderativa':
        return convertir_a_desiderativa(oracion)
    elif modalidad == 'dubitativa':
        return convertir_a_dubitativa(oracion)

def convertir_a_interrogativa(oracion):
    if oracion.endswith('?'):
        return oracion
    else:
        return oracion + '?'

def convertir_a_imperativa(oracion):
    palabras = oracion.split()
    return "Haz " + " ".join(palabras).lower()

def convertir_a_exclamativa(oracion):
    return f"¡{oracion}!"

def convertir_a_desiderativa(oracion):
    return f"Ojalá {oracion}"

def convertir_a_dubitativa(oracion):
    return f"Tal vez {oracion}"

def menu():
    # Selecciona una oración aleatoria
    oracion_original = random.choice(oraciones)
    print(f"Oración original: {oracion_original}")
    
    # Solicita al usuario que la escriba de nuevo
    oracion_usuario = input("Escribe nuevamente la oración: ")
    
    # Verifica si la oración es igual
    if oracion_usuario.strip() == oracion_original.strip():
        print("¡Correcto! Has escrito la oración correctamente.")
        
        # Menú para que el usuario transforme la oración
        print("Selecciona la modalidad a la que deseas transformar la oración:")
        print("1. Interrogativa")
        print("2. Imperativa")
        print("3. Exclamativa")
        print("4. Desiderativa")
        print("5. Dubitativa")
        
        opcion = input("Opción: ")
        
        modalidades = {
            "1": "interrogativa",
            "2": "imperativa",
            "3": "exclamativa",
            "4": "desiderativa",
            "5": "dubitativa"
        }
        
        modalidad = modalidades.get(opcion, None)
        
        if modalidad:
            # Solicitar al usuario que haga su propia transformación
            oracion_transformada_usuario = input(f"Escribe tu versión en modalidad {modalidad}: ")
            
            # Transformar la oración original usando la función del programa
            oracion_convertida = convertir_oracion(oracion_original, modalidad)
            
            # Verificar la transformación del usuario
            if oracion_transformada_usuario.strip() == oracion_convertida.strip():
                print("¡Tu transformación es correcta!")
            else:
                print("Tu transformación no coincide con la esperada.")
                print(f"Transformación esperada: {oracion_convertida}")
        else:
            print("Opción inválida.")
    else:
        print("La oración no coincide. Inténtalo de nuevo.")

# Iniciar el programa
if __name__ == "__main__":
    while True:
        menu()
        continuar = input("¿Quieres convertir otra oración? (s/n): ")
        if continuar.lower() != 's':
            break
