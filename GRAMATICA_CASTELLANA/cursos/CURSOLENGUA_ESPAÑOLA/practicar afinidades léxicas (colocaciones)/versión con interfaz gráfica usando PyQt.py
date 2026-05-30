import sys
import random
import csv
import os
from datetime import datetime
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit,
                             QMessageBox, QRadioButton, QButtonGroup, QGroupBox)

combinaciones = {
    'dar': ["dar una vuelta", "dar la razón", "dar miedo", "dar un consejo"],
    'hacer': ["hacer una pregunta", "hacer ejercicio", "hacer daño"],
    'tener': ["tener razón", "tener éxito", "tener hambre"],
    'ejercer': ["ejercer influencia", "ejercer presión"],
    'ejercitar': ["ejercitar la virtud", "ejercitar la memoria"],
    'cundir': ["cundir el desaliento", "cundir el pánico"],
    'evacuar': ["evacuar la consulta"],
    'reírse': ["reírse de alguien", "reírse con alguien"],
    'contraer': ["contraer matrimonio", "contraer deudas"]
}

niveles = {
    "fácil": ["dar una vuelta", "hacer una pregunta", "tener razón"],
    "medio": ["ejercer influencia", "ejercitar la virtud", "reírse de alguien"],
    "difícil": ["cundir el desaliento", "evacuar la consulta", "contraer matrimonio"]
}

class EntrenadorVerbal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Entrenamiento de Combinaciones Verbales")

        self.nivel = "fácil"
        self.vidas = 3
        self.puntos = 0
        self.correctas = 0
        self.incorrectas = 0
        self.frases = []
        self.frase_actual = ""

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.radio_group = QButtonGroup(self)
        nivel_box = QGroupBox("Selecciona un nivel")
        nivel_layout = QVBoxLayout()

        for nivel in niveles:
            btn = QRadioButton(nivel.capitalize())
            if nivel == "fácil":
                btn.setChecked(True)
            self.radio_group.addButton(btn)
            self.radio_group.setId(btn, list(niveles.keys()).index(nivel))
            nivel_layout.addWidget(btn)

        nivel_box.setLayout(nivel_layout)
        layout.addWidget(nivel_box)

        self.btn_comenzar = QPushButton("Comenzar")
        self.btn_comenzar.clicked.connect(self.comenzar)
        layout.addWidget(self.btn_comenzar)

        self.lbl_frase = QLabel("")
        layout.addWidget(self.lbl_frase)

        self.entry_oracion = QLineEdit()
        layout.addWidget(self.entry_oracion)

        self.btn_verificar = QPushButton("Verificar")
        self.btn_verificar.clicked.connect(self.verificar)
        layout.addWidget(self.btn_verificar)

        self.lbl_estado = QLabel("Vidas: 3 | Puntos: 0")
        layout.addWidget(self.lbl_estado)

        self.setLayout(layout)

    def comenzar(self):
        idx = self.radio_group.checkedId()
        self.nivel = list(niveles.keys())[idx]
        self.vidas = 3
        self.puntos = 0
        self.correctas = 0
        self.incorrectas = 0
        self.frases = niveles[self.nivel].copy()
        random.shuffle(self.frases)
        self.siguiente_frase()

    def siguiente_frase(self):
        if self.vidas <= 0 or not self.frases:
            self.finalizar()
            return
        self.frase_actual = self.frases.pop()
        self.lbl_frase.setText(f"Escribe una oración con: '{self.frase_actual}'")
        self.entry_oracion.clear()

    def verificar(self):
        oracion = self.entry_oracion.text().strip()
        verbo = self.frase_actual.split()[0]
        if verbo in oracion:
            self.puntos += 10
            self.correctas += 1
            QMessageBox.information(self, "Correcto", "¡Bien hecho! Ganaste 10 puntos.")
        else:
            self.vidas -= 1
            self.incorrectas += 1
            QMessageBox.warning(self, "Incorrecto", f"Debías usar el verbo '{verbo}'. Pierdes una vida.")
        self.lbl_estado.setText(f"Vidas: {self.vidas} | Puntos: {self.puntos}")
        self.siguiente_frase()

    def finalizar(self):
        QMessageBox.information(self, "Fin", f"Correctas: {self.correctas}\nIncorrectas: {self.incorrectas}\nPuntos: {self.puntos}")
        self.guardar_estadisticas()

    def guardar_estadisticas(self):
        datos = {
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "nivel": self.nivel,
            "correctas": self.correctas,
            "incorrectas": self.incorrectas,
            "puntos": self.puntos,
            "vidas_restantes": self.vidas
        }
        archivo = "estadisticas_gui_pyqt.csv"
        archivo_nuevo = not os.path.exists(archivo)
        with open(archivo, mode='a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=datos.keys())
            if archivo_nuevo:
                writer.writeheader()
            writer.writerow(datos)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EntrenadorVerbal()
    window.show()
    sys.exit(app.exec_())
