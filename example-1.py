from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel
import sys

class MaFenetre(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Démonstration Signaux et Slots")
        self.setGeometry(100, 100, 300, 200)

        # Création du widget central
        widget_central = QWidget()
        self.setCentralWidget(widget_central)
        
        # Création du layout vertical
        layout = QVBoxLayout()
        
        # Création d'un label pour afficher le compteur
        self.compteur_label = QLabel("Compteur: 0")
        layout.addWidget(self.compteur_label)
        
        # Création de deux boutons
        self.bouton_increment = QPushButton("Incrémenter")
        self.bouton_reset = QPushButton("Réinitialiser")
        
        # Ajout des boutons au layout
        layout.addWidget(self.bouton_increment)
        layout.addWidget(self.bouton_reset)
        
        # Application du layout au widget central
        widget_central.setLayout(layout)
        
        # Initialisation du compteur
        self.compteur = 0
        
        # Connexion des signaux aux slots
        self.bouton_increment.clicked.connect(self.incrementer_compteur)
        self.bouton_reset.clicked.connect(self.reinitialiser_compteur)

    def incrementer_compteur(self):
        """Slot pour incrémenter le compteur"""
        self.compteur += 1
        self.compteur_label.setText(f"Compteur: {self.compteur}")
    
    def reinitialiser_compteur(self):
        """Slot pour réinitialiser le compteur"""
        self.compteur = 0
        self.compteur_label.setText(f"Compteur: {self.compteur}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    fenetre = MaFenetre()
    fenetre.show()
    sys.exit(app.exec_())