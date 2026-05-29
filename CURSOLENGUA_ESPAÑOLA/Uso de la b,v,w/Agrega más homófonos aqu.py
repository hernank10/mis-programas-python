# Lista de homófonos
homofonos = {
    "baca": "soporte en el techo de los vehículos",
    "vaca": "hembra del toro",
    "beta": "segunda letra del alfabeto griego",
    "veta": "vena o filón",
    "barón": "título de la nobleza",
    "varón": "hombre",
    "basto": "tosco o grosero",
    "vasto": "amplio o extenso",
    # Agrega más homófonos aquí
}

# Imprime los homófonos y sus significados
for palabra, significado in homofonos.items():
    print(f"{palabra.capitalize()} - {significado}")

# Ejemplo de uso
palabra_elegida = input("Elige una palabra para ver su significado: ")
if palabra_elegida in homofonos:
    print(f"Significado de '{palabra_elegida}': {homofonos[palabra_elegida]}")
else:
    print("Palabra no encontrada en la lista de homófonos.")

# Puedes agregar más funcionalidades según tus necesidades.
