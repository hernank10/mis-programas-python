# Listas de palabras
sinonimos = [
    ("Alegre", "Contento"), ("Casa", "Hogar"), ("Bello", "Hermoso"),
    ("Rápido", "Veloz"), ("Difícil", "Complicado"), ("Enseñar", "Instruir"),
    ("Comprender", "Entender"), ("Triste", "Melancólico"), ("Amigo", "Compañero"),
    ("Escribir", "Redactar")
]

isonimos = [
    ("Coche (Esp)", "Carro (LatAm)"), ("Ordenador (Esp)", "Computadora (LatAm)"), 
    ("Zumo (Esp)", "Jugo (LatAm)"), ("Tarta (Esp)", "Pastel (LatAm)"), 
    ("Móvil (Esp)", "Celular (LatAm)"), ("Autobús (Esp)", "Bus (LatAm)"), 
    ("Aparcar (Esp)", "Estacionar (LatAm)"), ("Gafas (Esp)", "Lentes (LatAm)"), 
    ("Piso (Esp)", "Departamento (LatAm)"), ("Chaqueta (Esp)", "Campera (LatAm)")
]

homonimos = [
    ("Banco (institución financiera)", "Banco (asiento)"), 
    ("Gato (animal)", "Gato (herramienta)"), ("Vela (cera para iluminar)", "Vela (navegar)"), 
    ("Caja (recipiente)", "Caja (verbo 'cajar')"), ("Cura (sacerdote)", "Cura (sanación)"), 
    ("Bota (calzado)", "Bota (verbo 'botar')"), ("Hoja (planta)", "Hoja (papel)"), 
    ("Río (cuerpo de agua)", "Río (verbo 'reír')"), ("Carta (misiva)", "Carta (menú)"), 
    ("Ratón (animal)", "Ratón (dispositivo de computadora)")
]

homofonas = [
    ("Haya (verbo 'haber')", "Haya (árbol)"), ("Vaya (verbo 'ir')", "Valla (cerca)"), 
    ("Cazar (atrapar)", "Casar (unir en matrimonio)"), ("Grabar (registrar)", "Gravar (imponer un impuesto)"), 
    ("Basto (tosco)", "Vasto (amplio)"), ("Hondo (profundo)", "Onda (curva)"), 
    ("Herrar (poner herraduras)", "Errar (equivocarse)"), ("Bello (hermoso)", "Vello (pelusa)"), 
    ("Hierba (planta)", "Hierva (verbo 'hervir')"), ("Votar (sufragar)", "Botar (arrojar)")
]

antonimos = [
    ("Día", "Noche"), ("Alto", "Bajo"), ("Frío", "Calor"), 
    ("Feliz", "Triste"), ("Blanco", "Negro"), ("Rápido", "Lento"), 
    ("Grande", "Pequeño"), ("Claro", "Oscuro"), ("Abierto", "Cerrado"), 
    ("Nuevo", "Viejo")
]

# Función para practicar
def practicar_palabras(palabras, categoria):
    print(f"\nPracticando {categoria}:")
    correctas = 0
    for par in palabras:
        respuesta = input(f"Escribe el sinónimo de '{par[0]}': ").strip()
        if respuesta.lower() == par[1].lower():
            print("¡Correcto!")
            correctas += 1
        else:
            print(f"Incorrecto. La respuesta correcta es '{par[1]}'")
    print(f"Obtuviste {correctas} de {len(palabras)} correctas.\n")

# Practicar cada categoría
practicar_palabras(sinonimos, "Sinónimos")
practicar_palabras(isonimos, "Isónimos")
practicar_palabras(homonimos, "Homónimos")
practicar_palabras(homofonas, "Homófonas")
practicar_palabras(antonimos, "Antónimos")
