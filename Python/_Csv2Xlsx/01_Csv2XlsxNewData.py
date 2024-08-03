import os
import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QFileDialog

def ajouter_donnees_a_xlsx(fichier_xlsx, dossier_csv):
    # Lit le fichier Excel existant
    try:
        df_existing = pd.read_excel(fichier_xlsx, header=None)
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier Excel : {e}")
        return
    
    # Obtenez la liste des fichiers CSV déjà présents dans le fichier Excel
    csv_files_in_excel = set(df_existing[2].dropna().unique())  # Utilise la colonne avec les noms de fichiers CSV

    # Crée une liste pour stocker les nouvelles données
    data_combined = []

    # Parcourt tous les fichiers dans le dossier sélectionné
    for root, dirs, files in os.walk(dossier_csv):
        for file in files:
            # Vérifie si le fichier a l'extension .csv et n'est pas déjà dans le fichier Excel
            if file.endswith('.csv') and file not in csv_files_in_excel:
                # Construit le chemin complet vers le fichier
                chemin_fichier = os.path.join(root, file)
                try:
                    # Lit le fichier CSV
                    df = pd.read_csv(chemin_fichier, header=None)
                    # Initialisation d'une liste pour stocker les données d'une ligne
                    data_row = [file, '', '']  # Commence avec le nom du fichier et deux colonnes vides
                    for index, row in df.iterrows():
                        data_row.extend(row)  # Ajoute chaque ligne du CSV à la liste
                    # Ajout de la ligne à la liste combinée
                    data_combined.append(data_row)
                except Exception as e:
                    print(f"Erreur en lisant {chemin_fichier}: {e}")

    # Si de nouvelles données sont trouvées, les ajouter au fichier Excel existant
    if data_combined:
        df_new_data = pd.DataFrame(data_combined)
        df_updated = pd.concat([df_existing, df_new_data], ignore_index=True)

        # Sauvegarde le DataFrame mis à jour dans le fichier Excel
        df_updated.to_excel(fichier_xlsx, index=False, header=False)
        print(f"Données ajoutées au fichier Excel : {fichier_xlsx}")
    else:
        print("Aucune nouvelle donnée à ajouter.")

app = QApplication(sys.argv)

# Ouvre une boîte de dialogue pour sélectionner le fichier Excel existant
fichier_xlsx = QFileDialog.getOpenFileName(None, "Sélectionnez le fichier Excel", "", "Fichiers Excel (*.xlsx)")[0]

# Vérifie si un fichier a été sélectionné
if fichier_xlsx:
    # Ouvre une boîte de dialogue pour sélectionner un dossier contenant les CSV
    dossier_csv = QFileDialog.getExistingDirectory(None, "Sélectionnez un dossier contenant les CSV")

    # Vérifie si un dossier a été sélectionné
    if dossier_csv:
        ajouter_donnees_a_xlsx(fichier_xlsx, dossier_csv)
    else:
        print("Aucun dossier sélectionné.")
else:
    print("Aucun fichier Excel sélectionné.")
