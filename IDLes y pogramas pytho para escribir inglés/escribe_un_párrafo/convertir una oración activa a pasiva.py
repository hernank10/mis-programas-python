# Función para convertir una oración activa a pasiva
def convertir_a_pasiva(oracion_activa):
    palabras = oracion_activa.split()
    sujeto = palabras[0]
    verbo = palabras[1]
    complemento = " ".join(palabras[2:])
    oracion_pasiva = f"{complemento} fue {verbo} por {sujeto}"
    return oracion_pasiva

# Función para traducir una oración activa o pasiva al inglés (simple)
def traducir_a_ingles(oracion):
    traduccion = oracion
    traducciones = {
        "el programador": "the programmer",
        "el código": "the code",
        "analiza": "analyzes",
        "escribe": "writes",
        "fue": "was",
        "por": "by"
    }
    
    for espanol, ingles in traducciones.items():
        traduccion = traduccion.replace(espanol, ingles)
    
    return traduccion

# Función principal para procesar las oraciones
def procesar_oraciones():
    # Lista de oraciones activas predeterminadas
    oraciones_activas = [
        "El programador escribe el código",
        "El ingeniero analiza el sistema",
        "El profesor enseña la gramática"
    ]
    
    # Procesar las oraciones predeterminadas
    for oracion_activa in oraciones_activas:
        oracion_pasiva = convertir_a_pasiva(oracion_activa)
        traduccion_activa = traducir_a_ingles(oracion_activa)
        traduccion_pasiva = traducir_a_ingles(oracion_pasiva)
        
        print(f"Oración activa: {oracion_activa}")
        print(f"Oración pasiva: {oracion_pasiva}")
        print(f"Traducción activa: {traduccion_activa}")
        print(f"Traducción pasiva: {traduccion_pasiva}")
        print()
    
    # Solicitar nuevas oraciones activas al usuario
    for _ in range(3):
        nueva_oracion = input("Ingresa una nueva oración activa: ")
        oracion_pasiva = convertir_a_pasiva(nueva_oracion)
        traduccion_activa = traducir_a_ingles(nueva_oracion)
        traduccion_pasiva = traducir_a_ingles(oracion_pasiva)
        
        print(f"Oración activa: {nueva_oracion}")
        print(f"Oración pasiva: {oracion_pasiva}")
        print(f"Traducción activa: {traduccion_activa}")
        print(f"Traducción pasiva: {traduccion_pasiva}")
        print()

# Llamar a la función principal
if __name__ == "__main__":
    procesar_oraciones()
