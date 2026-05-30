import random
import sqlite3
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base
from faker import Faker
from tabulate import tabulate
import pandas as pd
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import matplotlib.pyplot as plt
from datetime import datetime

# Configuración inicial
fake = Faker('es_ES')
Base = declarative_base()
engine = create_engine('sqlite:///derivacion.db')
Session = sessionmaker(bind=engine)

# Modelos de base de datos
class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    puntos = Column(Integer, default=0)
    racha = Column(Integer, default=0)

class Afijo(Base):
    __tablename__ = 'afijos'
    id = Column(Integer, primary_key=True)
    tipo = Column(String)  # prefijo/sufijo
    forma = Column(String)
    categoria = Column(String)
    regla = Column(String)
    ejemplo = Column(String)

class Excepcion(Base):
    __tablename__ = 'excepciones'
    id = Column(Integer, primary_key=True)
    palabra = Column(String)
    explicacion = Column(String)

class Progreso(Base):
    __tablename__ = 'progreso'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    fecha = Column(String)
    puntos = Column(Integer)

Base.metadata.create_all(engine)

class DerivacionAvanzada:
    def __init__(self):
        self.session = Session()
        self.usuario_actual = None
        self.cargar_datos_iniciales()
    
    def cargar_datos_iniciales(self):
        if not self.session.query(Afijo).first():
            afijos_base = [
                {'forma': '-dad', 'tipo': 'sufijo', 'categoria': 'cualidad', 
                 'regla': 'Adjetivo + -dad', 'ejemplo': 'bondad'},
                {'forma': 'des-', 'tipo': 'prefijo', 'categoria': 'negación',
                 'regla': 'Prefijo negativo', 'ejemplo': 'deshacer'}
            ]
            for afijo in afijos_base:
                self.session.add(Afijo(**afijo))
            self.session.commit()

    def menu_principal(self):
        while True:
            print("\n" + "="*40)
            print(" DERIVACIÓN AVANZADA ".center(40, '★'))
            print("="*40)
            if self.usuario_actual:
                print(f"Usuario: {self.usuario_actual.nombre} | Puntos: {self.usuario_actual.puntos} | Racha: {self.usuario_actual.racha}")
            print("1. Ejercicios interactivos\n2. Generar lista\n3. Reglas\n4. Tablas comparativas\n5. Casos especiales\n6. Gráficos de progreso\n7. Exportar datos\n8. Salir")
            
            opcion = input("Selección: ")
            
            if opcion == '1': self.ejercicios_interactivos()
            elif opcion == '2': self.generar_lista()
            elif opcion == '3': self.mostrar_reglas()
            elif opcion == '4': self.tablas_comparativas()
            elif opcion == '5': self.consultar_excepciones()
            elif opcion == '6': self.graficos_progreso()
            elif opcion == '7': self.exportar_datos()
            elif opcion == '8': break
            else: print("Opción inválida")

    def ejercicios_interactivos(self):
        if not self.usuario_actual:
            self.registrar_usuario()
            
        ejercicio = random.choice([self._ejercicio_afijos, self._ejercicio_excepciones])
        resultado = ejercicio()
        
        if resultado:
            self.actualizar_puntos(10)
            self.actualizar_racha(1)
        else:
            self.actualizar_racha(0)

    def _ejercicio_afijos(self):
        afijo = self.session.query(Afijo).order_by(sqlalchemy.func.random()).first()
        palabra = fake.word().lower()
        print(f"\nForma una palabra usando: {afijo.forma}")
        respuesta = input(f"Base: {palabra} → ").strip().lower()
        
        solucion = f"{afijo.forma}{palabra}" if afijo.tipo == 'prefijo' else f"{palabra}{afijo.forma}"
        if respuesta == solucion:
            print("✅ Correcto!")
            return True
        else:
            print(f"❌ Solución: {solucion}")
            return False

    def actualizar_puntos(self, puntos):
        self.usuario_actual.puntos += puntos
        self.session.add(Progreso(
            usuario_id=self.usuario_actual.id,
            fecha=datetime.now().strftime("%Y-%m-%d"),
            puntos=puntos
        ))
        self.session.commit()

    def actualizar_racha(self, incremento):
        self.usuario_actual.racha = self.usuario_actual.racha + incremento if incremento else 0
        self.session.commit()

    def graficos_progreso(self):
        datos = self.session.query(Progreso).filter_by(usuario_id=self.usuario_actual.id).all()
        if datos:
            fechas = [d.fecha for d in datos]
            puntos = [d.puntos for d in datos]
            
            plt.figure(figsize=(10, 5))
            plt.plot(fechas, puntos, marker='o')
            plt.title('Progreso de aprendizaje')
            plt.xlabel('Fecha')
            plt.ylabel('Puntos acumulados')
            plt.grid(True)
            plt.savefig('progreso.png')
            print("Gráfico guardado como 'progreso.png'")
        else:
            print("No hay datos de progreso aún")

    def exportar_datos(self):
        formatos = {'1': ('PDF', self._exportar_pdf), '2': ('Excel', self._exportar_excel)}
        print("\nFormatos de exportación:")
        [print(f"{k}. {v[0]}") for k, v in formatos.items()]
        
        opcion = input("Seleccione formato: ")
        if opcion in formatos:
            formatos[opcion][1]()
        else:
            print("Opción inválida")

    def _exportar_pdf(self):
        pdf = canvas.Canvas("reporte.pdf", pagesize=letter)
        pdf.setFont("Helvetica", 12)
        
        # Cabecera
        pdf.drawString(100, 750, f"Reporte de aprendizaje: {self.usuario_actual.nombre}")
        pdf.drawString(100, 730, f"Puntos totales: {self.usuario_actual.puntos}")
        
        # Datos
        y = 700
        for progreso in self.session.query(Progreso).filter_by(usuario_id=self.usuario_actual.id):
            pdf.drawString(100, y, f"{progreso.fecha}: {progreso.puntos} puntos")
            y -= 20
        
        pdf.save()
        print("Reporte PDF generado: 'reporte.pdf'")

    def _exportar_excel(self):
        datos = []
        for p in self.session.query(Progreso).filter_by(usuario_id=self.usuario_actual.id):
            datos.append([p.fecha, p.puntos])
        
        df = pd.DataFrame(datos, columns=['Fecha', 'Puntos'])
        df.to_excel('progreso.xlsx', index=False)
        print("Archivo Excel generado: 'progreso.xlsx'")

    def registrar_usuario(self):
        nombre = input("\nIngrese su nombre: ")
        self.usuario_actual = Usuario(nombre=nombre)
        self.session.add(self.usuario_actual)
        self.session.commit()

if __name__ == "__main__":
    app = DerivacionAvanzada()
    app.menu_principal()
