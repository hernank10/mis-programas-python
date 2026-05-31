def verificar_entrada(correcta, idioma):
    while True:
        entrada = input(f"Escribe la oración en {idioma}: ")
        if entrada.strip() == correcta:
            print("¡Correcto!")
            break
        else:
            print("Incorrecto. Inténtalo de nuevo.")

# Oraciones para verificar en tres idiomas: inglés, español y francés
oraciones = [
    ("Use environment variables in Django.", "Uso de variables de entorno en Django.", "Utiliser des variables d'environnement dans Django."),
    ("Redirects in Flask.", "Redireccionamientos en Flask.", "Redirections dans Flask."),
    ("Middleware in Django.", "Uso de middleware en Django.", "Utilisation de middleware dans Django."),
    ("Upload files in Flask.", "Subir archivos en Flask.", "Télécharger des fichiers dans Flask."),
    ("Implement pagination in Django.", "Implementar paginación en Django.", "Implémenter la pagination dans Django."),
    ("Use flash messages in Flask.", "Uso de flash messages en Flask.", "Utiliser des messages flash dans Flask."),
    ("Unit testing in Django.", "Pruebas unitarias en Django.", "Tests unitaires dans Django."),
    ("Use pytest for testing in Flask.", "Usa pytest para pruebas en Flask.", "Utiliser pytest pour tester dans Flask."),
    ("Configure URLs in Django.", "Configura URLs en Django.", "Configurer des URLs dans Django."),
    ("Integration with REST APIs in Flask.", "Integración con APIs REST en Flask.", "Intégration avec des API REST dans Flask."),
    ("Use Flask-RESTful for REST APIs.", "Usa Flask-RESTful para APIs REST.", "Utiliser Flask-RESTful pour des API REST."),
    ("Protect routes in Flask.", "Protección de rutas en Flask.", "Protéger les routes dans Flask."),
    ("Create users in Django.", "Creación de usuarios en Django.", "Création d'utilisateurs dans Django."),
    ("Handle errors in Flask.", "Manejo de errores en Flask.", "Gérer les erreurs dans Flask."),
    ("Integration tests in Django.", "Pruebas de integración en Django.", "Tests d'intégration dans Django."),
    ("Use Flask-Babel for translation.", "Usa Flask-Babel para traducción.", "Utiliser Flask-Babel pour la traduction."),
    ("Interact with JavaScript in Flask.", "Interacción con JavaScript en Flask.", "Interaction avec JavaScript dans Flask."),
    ("WebSocket integration in Django with Django Channels.", "Integración de WebSockets en Django con Django Channels.", "Intégration de WebSocket dans Django avec Django Channels."),
    ("Use Flask-Mail to send emails.", "Usa Flask-Mail para enviar correos.", "Utiliser Flask-Mail pour envoyer des courriels."),
    ("Use Django Email to send emails.", "Usa Django Email para enviar correos.", "Utiliser Django Email pour envoyer des courriels."),
    # Nuevas oraciones añadidas desde el libro de inglés
    ("The cat is on the table.", "El gato está sobre la mesa.", "Le chat est sur la table."),
    ("She is reading a book.", "Ella está leyendo un libro.", "Elle lit un livre."),
    ("They are playing soccer.", "Ellos están jugando al fútbol.", "Ils jouent au football.")
]

print("Vamos a practicar escribir oraciones sobre el diseño de páginas web y otras oraciones.")
print("Debes escribir cada oración correctamente en inglés, español y francés.")
print("¡Empecemos!\n")

for i, (ingles, espanol, frances) in enumerate(oraciones):
    print(f"Oración {i+1}:")
    
    print("En inglés:")
    verificar_entrada(ingles, "inglés")
    
    print("En español:")
    verificar_entrada(espanol, "español")
    
    print("En francés:")
    verificar_entrada(frances, "francés")
    
    print("\n")

print("¡Felicidades! Has completado todas las oraciones.")
