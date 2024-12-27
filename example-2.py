from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QLabel, QPushButton)
from PyQt5.QtCore import pyqtSignal
import sys

class VuePrincipale(QWidget):
    # Définition du signal personnalisé
    nom_change = pyqtSignal(str)  # Signal qui transportera une chaîne de caractères

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vue Principale")       
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        
        # Champ de saisie pour le nom
        self.input_nom = QLineEdit()
        self.input_nom.setPlaceholderText("Entrez un nom")
        
        # Bouton pour valider le changement
        self.bouton_valider = QPushButton("Changer le nom")
        self.bouton_valider.clicked.connect(self.emettre_nouveau_nom)

        layout.addWidget(QLabel("Modifier le nom :"))
        layout.addWidget(self.input_nom)
        layout.addWidget(self.bouton_valider)
        
        self.setLayout(layout)

    def emettre_nouveau_nom(self):
        # Émet le signal avec le nouveau nom
        nouveau_nom = self.input_nom.text()
        if nouveau_nom:
            self.nom_change.emit(nouveau_nom)

class VueSecondaire(QWidget):
    def __init__(self, titre="Vue Secondaire"):
        super().__init__()
        self.setWindowTitle(titre)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        
        # Label pour afficher le nom
        self.label_nom = QLabel("Nom actuel : -")
        layout.addWidget(self.label_nom)
        
        self.setLayout(layout)

    def mettre_a_jour_nom(self, nouveau_nom):
        # Slot qui met à jour l'affichage du nom
        self.label_nom.setText(f"Nom actuel : {nouveau_nom}")

class FenetrePrincipale(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Démonstration Signaux Personnalisés")
        self.setGeometry(100, 100, 800, 400)

        # Création d'un widget pour contenir les deux vues
        widget_central = QWidget()
        layout_principal = QVBoxLayout()

        # Création des vues
        self.vue_principale = VuePrincipale()
        self.vue_secondaire1 = VueSecondaire("Vue Secondaire 1")
        self.vue_secondaire1.setStyleSheet('background-color: #D46F4D; padding:20px;')

        self.vue_secondaire2 = VueSecondaire("Vue Secondaire 2")
        self.vue_secondaire2.setStyleSheet('background-color: #08C5D1; padding: 20px;')
        # Connexion du signal personnalisé aux slots des vues secondaires
        self.vue_principale.nom_change.connect(self.vue_secondaire1.mettre_a_jour_nom)
        self.vue_principale.nom_change.connect(self.vue_secondaire2.mettre_a_jour_nom)

        # Ajout des vues au layout
        layout_principal.addWidget(self.vue_principale)
        layout_principal.addWidget(self.vue_secondaire1)
        layout_principal.addWidget(self.vue_secondaire2)

        widget_central.setLayout(layout_principal)
        self.setCentralWidget(widget_central)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    fenetre = FenetrePrincipale()
    fenetre.show()
    sys.exit(app.exec_())