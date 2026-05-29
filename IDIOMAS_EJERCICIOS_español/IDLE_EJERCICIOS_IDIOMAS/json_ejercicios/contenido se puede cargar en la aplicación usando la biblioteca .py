import json

with open('contenido.json', 'r') as archivo:
    contenido = json.load(archivo)

for regla in contenido['reglas_ortograficas']:
    print(f"Regla: {regla['titulo']}\nDescripción: {regla['descripcion']}\nEjemplo: {regla['ejemplo']}\n")
