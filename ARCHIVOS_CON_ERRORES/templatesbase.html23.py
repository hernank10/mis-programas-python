<!-- templates/base.html -->
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Aprende Numerales</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <style>
        .main-container { max-width: 800px; margin: 2rem auto; }
        .card { margin: 1rem 0; }
        .progress { height: 25px; margin: 1rem 0; }
    </style>
</head>
<body>
    <nav class="navbar navbar-dark bg-dark">
        <a class="navbar-brand" href="/">Numerales Españoles</a>
    </nav>
    
    <div class="container main-container">
        {% block content %}{% endblock %}
    </div>

    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script>
        // Lógica común para prácticas y cuestionarios
        function manejarRespuesta(url, data) {
            $.post(url, data, function(response) {
                const resultado = JSON.parse(response);
                if(resultado.correcto) {
                    alert('✅ Correcto!');
                } else {
                    alert(`❌ Incorrecto. Respuesta correcta: ${resultado.respuesta_correcta || resultado.categoria_correcta}`);
                }
                window.location.reload();
            });
        }
    </script>
</body>
</html>
