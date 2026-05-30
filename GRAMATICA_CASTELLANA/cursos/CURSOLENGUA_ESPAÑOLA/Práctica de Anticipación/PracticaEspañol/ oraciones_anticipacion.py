import json

ruta_archivo = 'oraciones_anticipacion.json'

try:
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        datos = json.load(archivo)  # La variable se define dentro del bloque with
    
    # Acceso a los datos DENTRO del bloque where se definió
    categoria1 = datos['categorias'][0]
    
    print("\nCategoría:", categoria1['nombre'])
    print("Ejemplos:")
    for ejemplo in categoria1['ejemplos']:
        print("-", ejemplo)

except Exception as e:
    print(f"Error: {str(e)}")
