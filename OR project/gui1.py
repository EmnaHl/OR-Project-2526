"""
EasySolver - Interface d'accueil avec LOGO intégré
Application de Recherche Opérationnelle utilisant PyQt5
INSAT - Projet RO - VERSION AVEC LOGO
"""

import sys
from io import BytesIO
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QFrame, QMessageBox
)
from PyQt5.QtCore import Qt, QSize, QByteArray
from PyQt5.QtGui import QFont, QPixmap, QImage, QPainter
from PyQt5.QtSvg import QSvgRenderer
from domain_forms import  ConstructionFormWindow, FabricationFormWindow , EnergieFormWindow, BioinfoFormWindow
from sante_form import SanteFormWindow

# Logo EasySolver en SVG
EASYSOLVER_LOGO_SVG = """
<svg width="120" height="120" viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="logoGradient" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#1E8B9C;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#16697A;stop-opacity:1" />
    </linearGradient>
  </defs>
  <circle cx="60" cy="60" r="58" fill="url(#logoGradient)" stroke="white" stroke-width="2"/>
  <circle cx="60" cy="60" r="12" fill="#27AE60" stroke="white" stroke-width="2"/>
  <circle cx="30" cy="40" r="8" fill="#E67E22" stroke="white" stroke-width="1.5"/>
  <circle cx="90" cy="40" r="8" fill="#2980B9" stroke="white" stroke-width="1.5"/>
  <circle cx="25" cy="80" r="8" fill="#F39C12" stroke="white" stroke-width="1.5"/>
  <circle cx="95" cy="80" r="8" fill="#8E44AD" stroke="white" stroke-width="1.5"/>
  <line x1="60" y1="60" x2="30" y2="40" stroke="white" stroke-width="1.5" opacity="0.7"/>
  <line x1="60" y1="60" x2="90" y2="40" stroke="white" stroke-width="1.5" opacity="0.7"/>
  <line x1="60" y1="60" x2="25" y2="80" stroke="white" stroke-width="1.5" opacity="0.7"/>
  <line x1="60" y1="60" x2="95" y2="80" stroke="white" stroke-width="1.5" opacity="0.7"/>
  <line x1="30" y1="40" x2="90" y2="40" stroke="white" stroke-width="1" opacity="0.5"/>
  <line x1="25" y1="80" x2="95" y2="80" stroke="white" stroke-width="1" opacity="0.5"/>
  <text x="60" y="105" font-family="Arial" font-size="10" font-weight="bold" 
        text-anchor="middle" fill="white">EasySolver</text>
</svg>
"""


class DomainButton(QPushButton):
    """Bouton personnalisé pour chaque domaine"""

    def __init__(self, title, icon_text, description, color_hex, domain_id, parent=None):
        super().__init__()
        self.domain_id = domain_id
        self.color_hex = color_hex
        self.icon_text = icon_text
        self.title_text = title
        self.description_text = description

        self.setMinimumSize(300, 220)
        self.setMaximumSize(400, 280)
        self.setCursor(Qt.PointingHandCursor)
        self.setFocusPolicy(Qt.NoFocus)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(10)

        self.icon_label = QLabel(self.icon_text)
        icon_font = QFont("Segoe UI Emoji", 44)
        self.icon_label.setFont(icon_font)
        self.icon_label.setAlignment(Qt.AlignCenter)

        self.title_label = QLabel(self.title_text)
        self.title_label.setFont(QFont("Segoe UI", 13, QFont.Bold))
        self.title_label.setAlignment(Qt.AlignCenter)

        self.desc_label = QLabel(self.description_text)
        self.desc_label.setFont(QFont("Segoe UI", 9))
        self.desc_label.setAlignment(Qt.AlignCenter)
        self.desc_label.setWordWrap(True)

        main_layout.addStretch(1)
        main_layout.addWidget(self.icon_label)
        main_layout.addWidget(self.title_label)
        main_layout.addWidget(self.desc_label)
        main_layout.addStretch(1)

        self.setLayout(main_layout)
        self.apply_button_styles()
        self.clicked.connect(self.on_clicked)

    def apply_button_styles(self):
        rgb = self.hex_to_rgb(self.color_hex)
        light_rgb = self.lighten_color_rgb(rgb)
        dark_color = self.darken_color(self.color_hex)

        style = f"""
            QPushButton {{
                background: qlineargradient(
                    x1:0, y1:0, x2:1, y2:1,
                    stop:0 rgba({light_rgb[0]}, {light_rgb[1]}, {light_rgb[2]}, 0.15),
                    stop:1 rgba({light_rgb[0]}, {light_rgb[1]}, {light_rgb[2]}, 0.05)
                );
                border: 3px solid {self.color_hex};
                border-radius: 18px;
            }}
            QPushButton:hover {{
                background: {self.color_hex};
                border: 3px solid {dark_color};
            }}
            QPushButton:hover QLabel {{
                color: white;
            }}
        """
        self.setStyleSheet(style)

    @staticmethod
    def hex_to_rgb(hex_color):
        hex_color = hex_color.lstrip('#')
        return (int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16))

    @staticmethod
    def lighten_color_rgb(rgb, factor=0.2):
        return tuple(min(255, int(c + (255 - c) * factor)) for c in rgb)

    @staticmethod
    def darken_color(hex_color, factor=0.15):
        rgb = DomainButton.hex_to_rgb(hex_color)
        dark_rgb = tuple(int(c * (1 - factor)) for c in rgb)
        return f"#{dark_rgb[0]:02x}{dark_rgb[1]:02x}{dark_rgb[2]:02x}"

    def on_clicked(self):
        domain_names = {
            'sante': 'Santé - Tournées d\'infirmières à domicile',
            'construction': 'Construction - Planification de chantier',
            'fabrication': 'Fabrication - Emballage de produits',
            'energie': 'Énergie - Extension de réseau électrique',
            'bioinformatique': 'Bio-informatique - Appariement optimal'
        }

        name = domain_names.get(self.domain_id, self.title_text)
        if self.domain_id == "sante":
            self.form_window = SanteFormWindow()
            self.form_window.show()
        elif self.domain_id == "construction":
            self.form_window =  ConstructionFormWindow()
            self.form_window.show()
        elif self.domain_id == "fabrication":
            self.form_window = FabricationFormWindow()
            self.form_window.show()
        elif self.domain_id == "energie":
            self.form_window = EnergieFormWindow()
            self.form_window.show()
        else:
            self.form_window = BioinfoFormWindow()
            self.form_window.show()
    
        print(f"✓ Domaine sélectionné : {name}")

class EasySolverUI(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.setWindowTitle('EasySolver - Optimisation RO')
        self.setGeometry(100, 100, 1400, 950)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.create_header())
        main_layout.addWidget(self.create_content(), 1)
        main_layout.addWidget(self.create_footer())

        central_widget.setLayout(main_layout)

    def create_header(self):
        header = QFrame()
        header.setFixedHeight(220)
        header.setStyleSheet("background: #1E8B9C;")

        layout = QHBoxLayout()
        layout.setContentsMargins(50, 30, 50, 30)

        logo_label = QLabel()
        logo_pixmap = self.svg_to_pixmap(EASYSOLVER_LOGO_SVG, QSize(120, 120))
        logo_label.setPixmap(logo_pixmap)

        text_layout = QVBoxLayout()
        
        title = QLabel("EasySolver")
        title.setFont(QFont("Segoe UI", 42, QFont.Bold))
        title.setStyleSheet("color: white;")

        subtitle = QLabel(
            "Plateforme d'Optimisation en Recherche Opérationnelle<br>"
            "<span style='color:#FFD700; font-weight:bold;'>With EasySolver, solve complex problems with ease!</span>"
        )
        subtitle.setFont(QFont("Segoe UI", 12))
        subtitle.setStyleSheet("color: white;")

        text_layout.addWidget(title)
        text_layout.addWidget(subtitle)

        layout.addWidget(logo_label)
        layout.addLayout(text_layout)

        header.setLayout(layout)
        return header

    def create_content(self):
        content_widget = QWidget()
        layout = QVBoxLayout()

        intro_title = QLabel("Sélectionnez votre domaine d'application")
        intro_title.setFont(QFont("Segoe UI", 18, QFont.Bold))
        intro_title.setAlignment(Qt.AlignCenter)

        layout.addWidget(intro_title)

        grid = QGridLayout()
        domains = [
            ("Santé", "🏥", "Organisation des tournées", "#27AE60", "sante"),
            ("Construction", "🏗️", "Planification de chantier", "#E67E22", "construction"),
            ("Fabrication", "📦", "Emballage optimal", "#2980B9", "fabrication"),
            ("Énergie", "⚡", "Lignes électriques", "#F39C12", "energie"),
            ("Bio-informatique", "🧬", "Appariement moléculaire", "#8E44AD", "bioinformatique")
        ]

        for i, d in enumerate(domains):
            btn = DomainButton(*d)
            grid.addWidget(btn, i // 3, i % 3)

        layout.addLayout(grid)
        content_widget.setLayout(layout)
        return content_widget

    def create_footer(self):
        footer = QFrame()
        footer.setFixedHeight(60)
        layout = QVBoxLayout()

        copy = QLabel("© 2025 EasySolver - INSAT | Projet de Recherche Opérationnelle")
        copy.setFont(QFont("Segoe UI", 10))
        copy.setAlignment(Qt.AlignCenter)

        layout.addWidget(copy)
        footer.setLayout(layout)
        return footer

    @staticmethod
    def svg_to_pixmap(svg_str, size):
        """Convertir un SVG en QPixmap via QSvgRenderer (obligatoire)"""

        renderer = QSvgRenderer(QByteArray(svg_str.encode("utf-8")))
        image = QImage(size.width(), size.height(), QImage.Format_ARGB32)
        image.fill(Qt.transparent)

        painter = QPainter(image)
        renderer.render(painter)
        painter.end()

        return QPixmap.fromImage(image)


def main():
    app = QApplication(sys.argv)
    window = EasySolverUI()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
