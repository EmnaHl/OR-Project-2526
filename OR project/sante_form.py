# sante_form.py
import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QPushButton, QLineEdit, QFormLayout, QMessageBox
)
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt
from sante_backend import generate_infirmieres, save_sante_data


class SanteFormWindow(QMainWindow):
    """Formulaire pour le domaine Santé"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("EasySolver - Santé")
        self.setGeometry(150, 150, 800, 600)
        self.init_ui()
        self.set_background("nurse_bg.png")  # <-- ajout du background

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        title = QLabel("Formulaire - Santé")
        title.setFont(QFont("Segoe UI", 20, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        form_layout = QFormLayout()
        form_layout.setLabelAlignment(Qt.AlignLeft)
        form_layout.setFormAlignment(Qt.AlignTop | Qt.AlignHCenter)

        self.nbre_infirmieres = QLineEdit()
        self.nbre_infirmieres.setPlaceholderText("Entre 3 et 24")
        form_layout.addRow("Nombre d'infirmières :", self.nbre_infirmieres)

        coord_layout = QHBoxLayout()
        self.coord_x = QLineEdit()
        self.coord_x.setPlaceholderText("X")
        self.coord_y = QLineEdit()
        self.coord_y.setPlaceholderText("Y")
        coord_layout.addWidget(self.coord_x)
        coord_layout.addWidget(self.coord_y)
        form_layout.addRow("Coordonnées du siège :", coord_layout)

        layout.addLayout(form_layout)

        next_btn = QPushButton("Next")
        next_btn.setFixedWidth(150)
        next_btn.setStyleSheet("background-color: #27AE60; color: white; font-weight: bold;")
        next_btn.clicked.connect(self.on_next_clicked)
        layout.addWidget(next_btn, 0, Qt.AlignCenter)

    def on_next_clicked(self):
        try:
            nbre = int(self.nbre_infirmieres.text())
            if not (3 <= nbre <= 24):
                raise ValueError("Le nombre doit être compris entre 3 et 24.")
        except ValueError as e:
            QMessageBox.warning(self, "Erreur", f"Nombre d'infirmières invalide : {e}")
            return

        try:
            x = int(self.coord_x.text())
            y = int(self.coord_y.text())
        except ValueError:
            QMessageBox.warning(self, "Erreur", "Coordonnées X et Y invalides.")
            return

        # Génération automatique des infirmières
        infirmieres = generate_infirmieres(nbre)

        # Sauvegarde des données (siège et infirmières)
        save_sante_data(x, y, infirmieres)

        QMessageBox.information(
            self, "Succès",
            "Les données ont été enregistrées et les infirmières générées automatiquement !"
        )
        print(f"✅ Nombre infirmières : {nbre}, Siège : ({x}, {y})")

    def set_background(self, image_path):
        """Définit un arrière-plan image pour la fenêtre SanteFormWindow."""
        bg = QLabel(self)
        bg.setPixmap(QPixmap(image_path))
        bg.setScaledContents(True)
        bg.lower()  # se place derrière tous les widgets
        bg.resize(self.width(), self.height())
        self.bg_label = bg

    def resizeEvent(self, event):
        """Permet au background de suivre le redimensionnement."""
        if hasattr(self, "bg_label"):
            self.bg_label.resize(self.width(), self.height())
        super().resizeEvent(event)

