# domain_forms.py
from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QFormLayout, QMessageBox
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class ConstructionFormWindow(QMainWindow):
    """Formulaire pour le domaine Construction"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("EasySolver - Construction")
        self.setGeometry(150, 150, 800, 600)
        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        title = QLabel("Formulaire - Construction")
        title.setFont(QFont("Segoe UI", 20, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        form_layout = QFormLayout()
        self.chantier = QLineEdit()
        self.chantier.setPlaceholderText("Nom du chantier")
        form_layout.addRow("Chantier :", self.chantier)

        layout.addLayout(form_layout)

        next_btn = QPushButton("Next")
        next_btn.setFixedWidth(150)
        next_btn.setStyleSheet("background-color: #E67E22; color: white; font-weight: bold;")
        next_btn.clicked.connect(self.on_next_clicked)
        layout.addWidget(next_btn, 0, Qt.AlignCenter)

    def on_next_clicked(self):
        chantier = self.chantier.text()
        if not chantier:
            QMessageBox.warning(self, "Erreur", "Veuillez entrer le nom du chantier.")
            return
        QMessageBox.information(self, "Informations saisies", f"Chantier : {chantier}")
        print(f"✅ Chantier : {chantier}")


class FabricationFormWindow(QMainWindow):
    """Formulaire pour le domaine Fabrication"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("EasySolver - Fabrication")
        self.setGeometry(150, 150, 800, 600)
        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        title = QLabel("Formulaire - Fabrication")
        title.setFont(QFont("Segoe UI", 20, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        form_layout = QFormLayout()
        self.produit = QLineEdit()
        self.produit.setPlaceholderText("Nom du produit")
        form_layout.addRow("Produit :", self.produit)

        layout.addLayout(form_layout)

        next_btn = QPushButton("Next")
        next_btn.setFixedWidth(150)
        next_btn.setStyleSheet("background-color: #2980B9; color: white; font-weight: bold;")
        next_btn.clicked.connect(self.on_next_clicked)
        layout.addWidget(next_btn, 0, Qt.AlignCenter)

    def on_next_clicked(self):
        produit = self.produit.text()
        if not produit:
            QMessageBox.warning(self, "Erreur", "Veuillez entrer le nom du produit.")
            return
        QMessageBox.information(self, "Informations saisies", f"Produit : {produit}")
        print(f"✅ Produit : {produit}")


class EnergieFormWindow(QMainWindow):
    """Formulaire pour le domaine Énergie"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("EasySolver - Énergie")
        self.setGeometry(150, 150, 800, 600)
        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        title = QLabel("Formulaire - Énergie")
        title.setFont(QFont("Segoe UI", 20, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        form_layout = QFormLayout()
        self.ligne = QLineEdit()
        self.ligne.setPlaceholderText("Nom de la ligne électrique")
        form_layout.addRow("Ligne :", self.ligne)

        layout.addLayout(form_layout)

        next_btn = QPushButton("Next")
        next_btn.setFixedWidth(150)
        next_btn.setStyleSheet("background-color: #F39C12; color: white; font-weight: bold;")
        next_btn.clicked.connect(self.on_next_clicked)
        layout.addWidget(next_btn, 0, Qt.AlignCenter)

    def on_next_clicked(self):
        ligne = self.ligne.text()
        if not ligne:
            QMessageBox.warning(self, "Erreur", "Veuillez entrer le nom de la ligne.")
            return
        QMessageBox.information(self, "Informations saisies", f"Ligne : {ligne}")
        print(f"✅ Ligne : {ligne}")


class BioinfoFormWindow(QMainWindow):
    """Formulaire pour le domaine Bio-informatique"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("EasySolver - Bio-informatique")
        self.setGeometry(150, 150, 800, 600)
        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        title = QLabel("Formulaire - Bio-informatique")
        title.setFont(QFont("Segoe UI", 20, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        form_layout = QFormLayout()
        self.molecule = QLineEdit()
        self.molecule.setPlaceholderText("Nom de la molécule")
        form_layout.addRow("Molécule :", self.molecule)

        layout.addLayout(form_layout)

        next_btn = QPushButton("Next")
        next_btn.setFixedWidth(150)
        next_btn.setStyleSheet("background-color: #8E44AD; color: white; font-weight: bold;")
        next_btn.clicked.connect(self.on_next_clicked)
        layout.addWidget(next_btn, 0, Qt.AlignCenter)

    def on_next_clicked(self):
        mol = self.molecule.text()
        if not mol:
            QMessageBox.warning(self, "Erreur", "Veuillez entrer le nom de la molécule.")
            return
        QMessageBox.information(self, "Informations saisies", f"Molécule : {mol}")
        print(f"✅ Molécule : {mol}")
