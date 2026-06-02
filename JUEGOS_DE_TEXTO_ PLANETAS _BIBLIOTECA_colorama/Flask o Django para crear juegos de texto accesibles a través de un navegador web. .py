from flask import Flask, request, render_template_string

app = Flask(__name__)

estado_juego = "inicio"

@app.route("/", methods=["GET", "POST"])
def juego():
    global estado_juego
    mensaje = ""
    if request.method == "POST":
        comando = request.form.get("comando").lower()
        if comando == "salir":
            mensaje = "¡Gracias por jugar!"
            estado_juego = "fin"
        elif comando == "ir norte":
            mensaje = "Te diriges al norte."
            estado_juego = "norte"
        else:
            mensaje = "Comando no reconocido."

    html = f"""
    <h1>Juego de Texto Web</h1>
    <p>Estado actual: {estado_juego}</p>
    <form method="post">
        <input type="text" name="comando">
        <input type="submit" value="Enviar">
    </form>
    <p>{mensaje}</p>
    """
    return render_template_string(html)

if __name__ == "__main__":
    app.run(debug=True)
