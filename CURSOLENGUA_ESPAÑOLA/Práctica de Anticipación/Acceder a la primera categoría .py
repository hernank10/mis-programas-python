# Acceder a la primera categoría
categoria1 = datos['categorias'][0]
print(f"\nCategoría: {categoria1['nombre']}")
print("Ejemplos:")
for ejemplo in categoria1['ejemplos']:
    print(f"- {ejemplo}")

# Acceder a metadatos
print("\nMetadatos:")
print(f"Autor: {datos['metadata']['autor']}")
print(f"Versión: {datos['metadata']['version']}")
