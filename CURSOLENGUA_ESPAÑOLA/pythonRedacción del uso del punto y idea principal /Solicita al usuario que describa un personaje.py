def describir_personaje(personaje):
  """
  Solicita al usuario que describa un personaje.

  Args:
    personaje: El nombre del personaje que se desea describir.
  """

  print(f"**Describa al personaje {personaje}:**")

  # Solicitar al usuario que describa la personalidad del personaje.
  personalidad = input("¿Cómo describiría la personalidad de {personaje}? ")

  # Solicitar al usuario que describa las cualidades que admira del personaje.
  cualidades_admiradas = input(f"¿Qué cualidades admira de {personaje}? ")

  # Solicitar al usuario que describa cómo evoluciona la relación del personaje con otros personajes.
  evolucion_relacion = input(f"¿Cómo cree que la relación entre {personaje} y otros personajes evoluciona a lo largo de la obra? ")

  # Mostrar un resumen de la descripción del personaje.
  print(f"Resumen de la descripción de {personaje}:")
  print(f"- Personalidad: {personalidad}")
  print(f"- Cualidades admiradas: {cualidades_admiradas}")
  print(f"- Evolución de la relación: {evolucion_relacion}")

def main():
  #
