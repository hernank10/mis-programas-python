def main():
    print("=== Práctica de Grupos Sintácticos ===")
    print("Oración original: 'El mensajero llevó las cartas al correo.'\n")
    
    # Grupos sintácticos iniciales
    sujeto = "El mensajero"
    verbo = "llevó"
    complemento_directo = "las cartas"
    complemento_indirecto = "al correo"
    
    print("Identifica los grupos sintácticos:\n")
    print(f"Sujeto: {sujeto}")
    print(f"Verbo: {verbo}")
    print(f"Complemento directo: {complemento_directo}")
    print(f"Complemento indirecto: {complemento_indirecto}\n")
    
    input("Presiona Enter para continuar...\n")
    
    print("Ahora reorganiza los grupos sintácticos para crear nuevas oraciones:")
    print("Escribe el número correspondiente al grupo que deseas añadir en cada posición:")
    opciones = {
        "1": sujeto,
        "2": verbo,
        "3": complemento_directo,
        "4": complemento_indirecto
    }
    
    print("\nOpciones:")
    for key, value in opciones.items():
        print(f"{key}: {value}")
    
    # Crear una nueva oración
    nueva_oracion = []
    for i in range(4):
        eleccion = input(f"Selecciona el grupo {i + 1} (1-4): ")
        while eleccion not in opciones:
            eleccion = input("Opción no válida. Selecciona nuevamente (1-4): ")
        nueva_oracion.append(opciones[eleccion])
    
    # Mostrar la oración creada
    print("\nNueva oración:")
    print(" ".join(nueva_oracion) + ".\n")
    
    # Repetir o salir
    repetir = input("¿Quieres crear otra oración? (s/n): ").strip().lower()
    if repetir == 's':
        print("\n")
        main()
    else:
        print("¡Gracias por practicar! Hasta pronto.")

if __name__ == "__main__":
    main()
