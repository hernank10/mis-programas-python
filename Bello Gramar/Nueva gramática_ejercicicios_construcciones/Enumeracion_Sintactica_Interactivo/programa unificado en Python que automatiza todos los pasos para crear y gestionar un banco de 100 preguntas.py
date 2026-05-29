import json
import os
import sys
from datetime import datetime
import subprocess

class GestorPreguntas:
    def __init__(self):
        self.archivo_preguntas = "preguntas.json"
        self.categorias = [
            "Enumeración simple",
            "Sujeto-Verbo",
            "Nombres propios",
            "Casos complejos"
        ]
        
        if not os.path.exists(self.archivo_preguntas):
            self.inicializar_archivo()

    def inicializar_archivo(self):
        with open(self.archivo_preguntas, 'w') as f:
            json.dump([], f)

    # PASO 1: Preparación del entorno
    def crear_backup(self):
        fecha = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = f"backups/preguntas_{fecha}.json"
        
        os.makedirs("backups", exist_ok=True)
        with open(self.archivo_preguntas, 'r') as orig, open(backup_file, 'w') as bkp:
            json.dump(json.load(orig), bkp, indent=4)
        
        print(f"Backup creado: {backup_file}")
        return backup_file

    # PASO 2: Generación de preguntas
    def generar_plantilla(self, cantidad=100):
        preguntas = self.cargar_preguntas()
        
        for i in range(len(preguntas) + 1, cantidad + 1):
            nueva_pregunta = {
                "id": i,
                "pregunta": f"Texto de la pregunta {i} (editar)",
                "categoria": self.categorias[i % len(self.categorias)],
                "opciones": ["A) Opción A", "B) Opción B"],
                "correcta": "A",
                "dificultad": min((i // 25) + 1, 4)  # 1-4
            }
            preguntas.append(nueva_pregunta)
        
        self.guardar_preguntas(preguntas)
        print(f"Plantilla con {cantidad} preguntas generada")

    # PASO 3: Validación
    def validar_estructura(self):
        try:
            with open(self.archivo_preguntas, 'r') as f:
                data = json.load(f)
                
                if len(data) != 100:
                    raise ValueError(f"Hay {len(data)} preguntas (deben ser 100)")
                
                for idx, p in enumerate(data):
                    if not all(key in p for key in ['id', 'pregunta', 'opciones', 'correcta']):
                        raise ValueError(f"Pregunta {idx+1}: Estructura incompleta")
                    
                    if p['correcta'] not in ['A', 'B']:
                        raise ValueError(f"Pregunta {idx+1}: Respuesta debe ser A/B")
                
                print("✓ Validación exitosa")
                return True
                
        except Exception as e:
            print(f"Error de validación: {str(e)}")
            return False

    # PASO 4: Integración
    def integrar_aplicacion(self, ruta_aplicacion):
        destino = os.path.join(ruta_aplicacion, self.archivo_preguntas)
        os.replace(self.archivo_preguntas, destino)
        print(f"Archivo integrado en: {destino}")

    # PASO 5: Mantenimiento
    def inicializar_git(self):
        try:
            subprocess.run(["git", "init"], check=True)
            subprocess.run(["git", "add", self.archivo_preguntas], check=True)
            subprocess.run(["git", "commit", "-m", "Banco inicial de 100 preguntas"], check=True)
            print("✓ Repositorio Git inicializado")
        except subprocess.CalledProcessError as e:
            print(f"Error Git: {str(e)}")

    # Helpers
    def cargar_preguntas(self):
        with open(self.archivo_preguntas, 'r') as f:
            return json.load(f)

    def guardar_preguntas(self, data):
        with open(self.archivo_preguntas, 'w') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

def menu_principal():
    print("\n" + "═"*50)
    print(" GESTOR DE PREGUNTAS - ENUMERACIÓN SINTÁCTICA")
    print("═"*50)
    print("1. Generar plantilla de 100 preguntas")
    print("2. Validar estructura del banco")
    print("3. Crear backup")
    print("4. Integrar con aplicación")
    print("5. Inicializar control de versiones (Git)")
    print("6. Salir")
    
    return input("Seleccione una opción: ")

if __name__ == "__main__":
    gestor = GestorPreguntas()
    
    while True:
        opcion = menu_principal()
        
        if opcion == "1":
            gestor.generar_plantilla(100)
            gestor.validar_estructura()
        
        elif opcion == "2":
            if gestor.validar_estructura():
                print("Listo para implementación!")
        
        elif opcion == "3":
            gestor.crear_backup()
        
        elif opcion == "4":
            ruta = input("Ruta absoluta de la aplicación: ")
            gestor.integrar_aplicacion(ruta)
        
        elif opcion == "5":
            gestor.inicializar_git()
        
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción inválida")
