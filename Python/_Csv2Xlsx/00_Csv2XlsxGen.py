import os
import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QFileDialog

def lire_csv_et_generer_xlsx(dossier):
    # Crée une liste pour stocker les données
    data_combined = []

    # Parcourt tous les fichiers dans le dossier sélectionné
    for root, dirs, files in os.walk(dossier):
        for file in files:
            # Vérifie si le fichier a l'extension .csv
            if file.endswith('.csv'):
                # Construit le chemin complet vers le fichier
                chemin_fichier = os.path.join(root, file)
                try:
                    # Lit le fichier CSV
                    df = pd.read_csv(chemin_fichier, header=None)
                    # Initialisation d'une liste pour stocker les données d'une ligne
                    data_row = [file]  # Commence avec le nom du fichier
                    for index, row in df.iterrows():
                        data_row.extend(row)  # Ajoute chaque ligne du CSV à la liste
                    # Ajout de la ligne à la liste combinée
                    data_combined.append(data_row)
                except Exception as e:
                    print(f"Erreur en lisant {chemin_fichier}: {e}")

    # Crée un DataFrame avec les données combinées
    df_combined = pd.DataFrame(data_combined)

    # Ajoute deux colonnes vides avant les colonnes de données
    df_combined.insert(0, 'Colonne vide 1', '')  # Insère une colonne vide à la première position
    df_combined.insert(1, 'Colonne vide 2', '')  # Insère une autre colonne vide à la deuxième position

    # Sauvegarde le DataFrame dans un fichier Excel
    chemin_fichier_xlsx = os.path.join(dossier, '_csvSelection.xlsx')
    df_combined.to_excel(chemin_fichier_xlsx, index=False, header=False)
    print(f"Fichier Excel généré: {chemin_fichier_xlsx}")

app = QApplication(sys.argv)

# Ouvre une boîte de dialogue pour sélectionner un dossier
dossier_selectionne = QFileDialog.getExistingDirectory(None, "Sélectionnez un dossier")

# Vérifie si un dossier a été sélectionné
if dossier_selectionne:
    lire_csv_et_generer_xlsx(dossier_selectionne)
else:
    print("Aucun dossier sélectionné.")
