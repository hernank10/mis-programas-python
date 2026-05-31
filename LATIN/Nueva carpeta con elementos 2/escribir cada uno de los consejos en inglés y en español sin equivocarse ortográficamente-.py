# Lista de consejos en inglés
consejos_en_ingles = [
    "Use environment variables in Django.",
    "Redirects in Flask.",
    "Redirects in Django.",
    "Middleware in Flask.",
    "Middleware in Django.",
    "Upload files in Flask.",
    "Upload files in Django.",
    "Implement pagination in Flask.",
    "Implement pagination in Django.",
    "Use flash messages in Flask.",
    "Use messages in Django.",
    "Unit testing in Flask.",
    "Unit testing in Django.",
    "Use pytest for testing in Flask.",
    "Use pytest for testing in Django.",
    "Configure URLs in Flask.",
    "Configure URLs in Django.",
    "Integration with REST APIs in Flask.",
    "Integration with REST APIs in Django.",
    "Use Flask-RESTful for REST APIs.",
    "Use Django REST Framework.",
    "Configure an admin in Django.",
    "Protect routes in Flask.",
    "Protect routes in Django.",
    "Create users in Django.",
    "Handle errors in Flask.",
    "Handle errors in Django.",
    "Integration tests in Flask.",
    "Integration tests in Django.",
    "Use Flask-Babel for translation.",
    "Use Django Internationalization.",
    "Interact with JavaScript in Flask.",
    "Interact with JavaScript in Django.",
    "WebSocket integration in Flask with Flask-SocketIO.",
    "WebSocket integration in Django with Django Channels.",
    "Use Flask-Mail to send emails.",
    "Use Django Email to send emails."
]

# Lista de consejos en español
consejos_en_espanol = [
    "Uso de variables de entorno en Django.",
    "Redireccionamientos en Flask.",
    "Redireccionamientos en Django.",
    "Uso de middleware en Flask.",
    "Uso de middleware en Django.",
    "Subir archivos en Flask.",
    "Subir archivos en Django.",
    "Implementar paginación en Flask.",
    "Implementar paginación en Django.",
    "Uso de flash messages en Flask.",
    "Uso de mensajes en Django.",
    "Pruebas unitarias en Flask.",
    "Pruebas unitarias en Django.",
    "Usa pytest para pruebas en Flask.",
    "Usa pytest para pruebas en Django.",
    "Configura URLs en Flask.",
    "Configura URLs en Django.",
    "Integración con APIs REST en Flask.",
    "Integración con APIs REST en Django.",
    "Usa Flask-RESTful para APIs REST.",
    "Usa Django REST Framework.",
    "Configura un administrador en Django.",
    "Protección de rutas en Flask.",
    "Protección de rutas en Django.",
    "Creación de usuarios en Django.",
    "Manejo de errores en Flask.",
    "Manejo de errores en Django.",
    "Pruebas de integración en Flask.",
    "Pruebas de integración en Django.",
    "Usa Flask-Babel para traducción.",
    "Usa Django Internationalization.",
    "Interacción con JavaScript en Flask.",
    "Interacción con JavaScript en Django.",
    "Integración de WebSockets en Flask con Flask-SocketIO.",
    "Integración de WebSockets en Django con Django Channels.",
    "Usa Flask-Mail para enviar correos.",
    "Usa Django Email para enviar correos."
]

# Función para verificar la entrada del usuario
def verificar_entrada(correcta):
    while True:
        entrada = input("Escribe correctamente: ")
        if entrada.strip() == correcta:
            print("¡Correcto!")
            break
        else:
            print("Incorrecto. Inténtalo de nuevo.")

# Main
print("Vamos a practicar escribir consejos sobre el diseño de páginas web.")
print("Debes escribir cada consejo correctamente en inglés y en español.")
print("¡Empecemos!\n")

for i in range(len(consejos_en_ingles)):
    print(f"Consejo {i+1}:")
    print("En inglés:")
    print(consejos_en_ingles[i])
    verificar_entrada(consejos_en_ingles[i])
    
    print("En español:")
    print(consejos_en_espanol[i])
    verificar_entrada(consejos_en_espanol[i])
    print("\n")

print("¡Felicidades! Has completado todos los consejos.")
