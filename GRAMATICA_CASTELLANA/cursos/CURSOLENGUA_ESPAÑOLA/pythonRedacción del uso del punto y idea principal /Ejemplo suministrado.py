def main():
    # Ejemplo suministrado
    ejemplo = "Saludos, estimado equipo. Quería aclarar la situación con las cajas de libros incunables que hemos enviado. Han viajado por error desde Río de la Plata hasta Valladolid, Barcelona y Venezuela, pero ahora están en Puerto Rico. Necesitamos recuperarlos urgentemente para la exhibición en el museo holandés."

    # Abreviaturas de países
    abrev_paises = {
        "EE. UU.": "Estados Unidos",
        "C. Rica": "Costa Rica",
        "Arg.": "Argentina",
        "Dr. J. Pérez": "Doctor Juan Pérez",
        "Lic. M. Gómez": "Licenciado Marta Gómez"# Agrega aquí las abreviaturas de otros países
    }

    # Nombres de personas
    nombres_personas = {
        "Dr. J. Pérez": "Doctor Juan Pérez",
        "Lic. M. Gómez": "Licenciado Marta Gómez",
                "Dr. J. Pérez": "Doctor Juan Pérez",
        "Lic. M. Gómez": "Licenciado Marta Gómez"# Agrega aquí otros nombres de personas
    }

    # Nombres de oficinas internacionales
    oficinas_internacionales = {
        "ONU": "Organización de las Naciones Unidas",
        "OMC": "Organización Mundial del Comercio",
        "Dr. J. Pérez": "Doctor Juan Pérez",
        "Lic. M. Gómez": "Licenciado Marta Gómez"# Agrega aquí otros nombres de oficinas
    }

    # Reemplaza las abreviaturas en el ejemplo
    for abrev, completo in abrev_paises.items():
        ejemplo = ejemplo.replace(abrev, completo)

    for abrev, completo in nombres_personas.items():
        ejemplo = ejemplo.replace(abrev, completo)

    for abrev, completo in oficinas_internacionales.items():
        ejemplo = ejemplo.replace(abrev, completo)

    print(ejemplo)


if __name__ == "__main__":
    main()
