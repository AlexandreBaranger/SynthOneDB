import os
import sys
from PyQt5.QtWidgets import QApplication, QFileDialog

def supprimer_fichiers_meta(dossier):
    # Parcourt tous les fichiers et dossiers dans le dossier sélectionné
    for root, dirs, files in os.walk(dossier):
        for file in files:
            # Vérifie si le fichier a l'extension .meta
            if file.endswith('.meta'):
                # Construit le chemin complet vers le fichier
                chemin_fichier = os.path.join(root, file)
                try:
                    # Supprime le fichier
                    os.remove(chemin_fichier)
                    print(f"Supprimé: {chemin_fichier}")
                except Exception as e:
                    print(f"Erreur en supprimant {chemin_fichier}: {e}")

app = QApplication(sys.argv)

# Ouvre une boîte de dialogue pour sélectionner un dossier
dossier_selectionne = QFileDialog.getExistingDirectory(None, "Sélectionnez un dossier")

# Vérifie si un dossier a été sélectionné
if dossier_selectionne:
    supprimer_fichiers_meta(dossier_selectionne)
else:
    print("Aucun dossier sélectionné.")
