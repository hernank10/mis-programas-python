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
def verificar_entrada(correcta, idioma):
    while True:
        entrada = input(f"Escribe la oración en {idioma}: ")
        if entrada.strip() == correcta:
            print("¡Correcto!")
            break
        else:
            print("Incorrecto. Inténtalo de nuevo.")

# Oraciones para verificar en cinco idiomas: inglés, español, francés, latín y griego
oraciones = [
    ("Use environment variables in Django.", "Uso de variables de entorno en Django.", "Utiliser des variables d'environnement dans Django.", "Utere variabilibus ambitus in Django.", "Χρησιμοποιήστε μεταβλητές περιβάλλοντος στο Django."),
    ("Redirects in Flask.", "Redireccionamientos en Flask.", "Redirections dans Flask.", "Redirectiones in Flask.", "Ανακατευθύνσεις στο Flask."),
    ("Middleware in Django.", "Uso de middleware en Django.", "Utilisation de middleware dans Django.", "Usus middleware in Django.", "Χρήση middleware στο Django."),
    ("Upload files in Flask.", "Subir archivos en Flask.", "Télécharger des fichiers dans Flask.", "Fasciculi in Flask.", "Ανεβάστε αρχεία στο Flask."),
    ("Implement pagination in Django.", "Implementar paginación en Django.", "Implémenter la pagination dans Django.", "Implementatio paginationis in Django.", "Υλοποιήστε την σελιδοποίηση στο Django."),
    ("Use flash messages in Flask.", "Uso de flash messages en Flask.", "Utiliser des messages flash dans Flask.", "Utere nuntiis flash in Flask.", "Χρησιμοποιήστε μηνύματα flash στο Flask."),
    ("Unit testing in Django.", "Pruebas unitarias en Django.", "Tests unitaires dans Django.", "Unitas probatio in Django.", "Δοκιμές μονάδας στο Django."),
    ("Use pytest for testing in Flask.", "Usa pytest para pruebas en Flask.", "Utiliser pytest pour tester dans Flask.", "Utere pytest ad probationem in Flask.", "Χρησιμοποιήστε pytest για δοκιμές στο Flask."),
    ("Configure URLs in Django.", "Configura URLs en Django.", "Configurer des URLs dans Django.", "Configurare URLs in Django.", "Ρυθμίστε διευθύνσεις URL στο Django."),
    ("Integration with REST APIs in Flask.", "Integración con APIs REST en Flask.", "Intégration avec des API REST dans Flask.", "Integatio cum API REST in Flask.", "Ενσωμάτωση με REST APIs στο Flask."),
    ("Use Flask-RESTful for REST APIs.", "Usa Flask-RESTful para APIs REST.", "Utiliser Flask-RESTful pour des API REST.", "Utere Flask-RESTful ad API REST.", "Χρησιμοποιήστε Flask-RESTful για REST APIs."),
    ("Protect routes in Flask.", "Protección de rutas en Flask.", "Protéger les routes dans Flask.", "Protectiones vias in Flask.", "Προστατέψτε τις διαδρομές στο Flask."),
    ("Create users in Django.", "Creación de usuarios en Django.", "Création d'utilisateurs dans Django.", "Creatio usorum in Django.", "Δημιουργία χρηστών στο Django."),
    ("Handle errors in Flask.", "Manejo de errores en Flask.", "Gérer les erreurs dans Flask.", "Errorum tractatio in Flask.", "Διαχείριση σφαλμάτων στο Flask."),
    ("Integration tests in Django.", "Pruebas de integración en Django.", "Tests d'intégration dans Django.", "Integationes probationes in Django.", "Δοκιμές ενσωμάτωσης στο Django."),
    ("Use Flask-Babel for translation.", "Usa Flask-Babel para traducción.", "Utiliser Flask-Babel pour la traduction.", "Utere Flask-Babel ad translationem.", "Χρησιμοποιήστε Flask-Babel για μετάφραση."),
    ("Interact with JavaScript in Flask.", "Interacción con JavaScript en Flask.", "Interaction avec JavaScript dans Flask.", "Interagere cum JavaScript in Flask.", "Αλληλεπίδραση με JavaScript στο Flask."),
    ("WebSocket integration in Django with Django Channels.", "Integración de WebSockets en Django con Django Channels.", "Intégration de WebSocket dans Django avec Django Channels.", "Integratio WebSocket in Django cum Django Channels.", "Ενσωμάτωση WebSocket στο Django με τα Django Channels."),
    ("Use Flask-Mail to send emails.", "Usa Flask-Mail para enviar correos.", "Utiliser Flask-Mail pour envoyer des courriels.", "Utere Flask-Mail ad epistulas mittendas.", "Χρησιμοποιήστε Flask-Mail για να στείλετε emails."),
    ("Use Django Email to send emails.", "Usa Django Email para enviar correos.", "Utiliser Django Email pour envoyer des courriels.", "Utere Django Email ad epistulas mittendas.", "Χρησιμοποιήστε το Django Email για να στείλετε emails."),
    # Nuevas oraciones añadidas desde el libro de inglés
    ("The cat is on the table.", "El gato está sobre la mesa.", "Le chat est sur la table.", "Feles est in mensa.", "Η γάτα είναι στο τραπέζι."),
    ("She is reading a book.", "Ella está leyendo un libro.", "Elle lit un livre.", "Ea librum legit.", "Αυτή διαβάζει ένα βιβλίο."),
    ("They are playing soccer.", "Ellos están jugando al fútbol.", "Ils jouent au football.", "Ludunt eu.", "Αυτοί παίζουν ποδόσφαιρο.")
]

print("Vamos a practicar escribir oraciones sobre el diseño de páginas web y otras oraciones.")
print("Debes escribir cada oración correctamente en inglés, español, francés, latín y griego.")
print("¡Empecemos!\n")

for i, (ingles, espanol, frances, latin, griego) in enumerate(oraciones):
    print(f"Oración {i+1}:")
    
    print("En inglés:")
    verificar_entrada(ingles, "inglés")
    
    print("En español:")
    verificar_entrada(espanol, "español")
    
    print("En francés:")
    verificar_entrada(frances, "francés")
    
    print("En latín:")
    verificar_entrada(latin, "latín")
    
    print("En griego:")
    verificar_entrada(griego, "griego")
    
    print("\n")

print("¡Felicidades! Has completado todas las oraciones.")

