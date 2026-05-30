def regla_valida(palabra, regla):
    """
    Verifica si una palabra cumple con una regla dada.

    Args:
        palabra: La palabra a evaluar.
        regla: La regla a aplicar (una cadena de texto).

    Returns:
        True si la palabra cumple la regla, False en caso contrario.
    """

    # Ejemplo: Regla para verificar si la palabra comienza con C
    if regla == "La palabra comienza con C":
        return palabra[0] == 'C'

    # Agrega más condiciones para otras reglas
    # ...

    return False
