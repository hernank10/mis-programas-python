import openpyxl
from openpyxl import Workbook
from datetime import datetime

# Lista de estudiantes
estudiantes = ["Alice", "Bob", "Charlie", "Diana", "Edward"]

# Crear o cargar el libro de Excel
try:
    workbook = openpyxl.load_workbook("asistencia.xlsx")
    sheet = workbook.active
except FileNotFoundError:
    workbook = Workbook()
    sheet = workbook.active
    # Crear encabezados
    headers = ["Fecha"] + estudiantes
    sheet.append(headers)

# Registrar la asistencia
asistencia = [datetime.now().strftime("%Y-%m-%d")]  # Fecha actual
print("Marque la asistencia (P para presente, A para ausente):")
for estudiante in estudiantes:
    estado = input(f"{estudiante}: ").strip().upper()
    if estado not in ["P", "A"]:
        print("Entrada no válida. Se marcará como ausente.")
        estado = "A"
    asistencia.append(estado)

# Guardar los datos en la hoja de cálculo
sheet.append(asistencia)
workbook.save("asistencia.xlsx")
print("Asistencia registrada y guardada en 'asistencia.xlsx'")

