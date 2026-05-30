# Lista de homófonos en español e inglés
homofonos = [
    ("Baca", "Vaca", "Rack", "Cow"),
    ("Basto", "Vasto", "Coarse", "Vast"),
    ("Bienes", "Vienes", "Assets", "You come"),
    ("Grabar", "Gravar", "To record", "To tax"),
    ("Rebelar", "Revelar", "To rebel", "To reveal"),
    ("Savia", "Sabia", "Sap", "Wise"),
    ("Bello", "Vello", "Beautiful", "Hair"),
    ("Tubo", "Tuvo", "Tube", "He/She/It had"),
    ("Botar", "Votar", "To throw away", "To vote"),
    ("Bacilo", "Vacilo", "Bacillus", "I hesitate"),
    ("Barón", "Varón", "Baron", "Male"),
    ("Combino", "Convino", "I combine", "He/She/It agreed"),
    ("Graba", "Grava", "He/She/It records", "Gravel"),
    ("Basta", "Vasta", "Enough", "Vast"),
    ("Botón", "Votón", "Button", "Big voter"),
    ("Brasa", "Balsa", "Ember", "Raft"),
    ("Hierba", "Hierva", "Herb", "He/She/It boils"),
    ("Vello", "Velo", "Hair", "He/She/It watches over"),
    ("Haber", "A ver", "To have", "Let's see"),
    ("Cabe", "Cave", "He/She/It fits", "He/She/It digs")
]

# Función para revisar homófonos
def revisar_homofonos(homofonos):
    for i, (palabra1, palabra2, significado1, significado2) in enumerate(homofonos, 1):
        print(f"{i}. {palabra1} (Spanish: {significado1}) - {palabra2} (Spanish: {significado2})")
        input("Press Enter to continue...")
        print("Please write the first word and its meaning:")
        respuesta_palabra1 = input("Word: ")
        respuesta_significado1 = input("Meaning: ")
        if respuesta_palabra1.strip() == palabra1 and respuesta_significado1.strip() == significado1:
            print("Correct!")
        else:
            print("Incorrect. The correct answer is:")
            print(f"{palabra1} - {significado1}")
        
        print("Please write the second word and its meaning:")
        respuesta_palabra2 = input("Word: ")
        respuesta_significado2 = input("Meaning: ")
        if respuesta_palabra2.strip() == palabra2 and respuesta_significado2.strip() == significado2:
            print("Correct!")
        else:
            print("Incorrect. The correct answer is:")
            print(f"{palabra2} - {significado2}")
        print()

# Ejecutar la función
if __name__ == "__main__":
    revisar_homofonos(homofonos)
