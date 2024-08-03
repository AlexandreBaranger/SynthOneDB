import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QFileDialog, QMessageBox

def rechercher_dans_xlsx():
    app = QApplication(sys.argv)

    # Ouvre une boîte de dialogue pour sélectionner un fichier Excel
    fichier_xlsx, _ = QFileDialog.getOpenFileName(None, "Sélectionnez un fichier Excel", "", "Fichiers Excel (*.xlsx)")

    # Vérifie si un fichier a été sélectionné
    if not fichier_xlsx:
        print("Aucun fichier sélectionné.")
        return

    try:
        # Charger le fichier Excel
        df = pd.read_excel(fichier_xlsx, header=None)

        while True:
            # Demander à l'utilisateur de saisir un mot ou une phrase
            recherche = input("Entrez un mot ou une phrase à rechercher dans la deuxième colonne : ")

            # Diviser la phrase en mots
            mots_recherche = recherche.split()

            # Rechercher les lignes qui contiennent au moins un mot de la recherche dans la deuxième colonne (index 1)
            resultats = df[df[1].astype(str).apply(lambda cell: any(mot.lower() in cell.lower() for mot in mots_recherche))]

            # Vérifier si des résultats ont été trouvés
            if not resultats.empty:
                print(f"Résultats trouvés pour '{recherche}' :")
                print(resultats)
            else:
                print(f"Aucun résultat trouvé pour '{recherche}'.")

            # Demander à l'utilisateur s'il veut sauvegarder les résultats ou refaire une recherche
            action = input("Voulez-vous sauvegarder les résultats (s) ou refaire une recherche (r)? ").strip().lower()

            if action == 's' and not resultats.empty:
                # Ouvrir une boîte de dialogue pour choisir le nom et l'emplacement du fichier de sauvegarde
                chemin_sauvegarde, _ = QFileDialog.getSaveFileName(None, "Enregistrer le fichier", "", "Fichiers Excel (*.xlsx)")

                if chemin_sauvegarde:
                    # Sauvegarder les résultats dans un nouveau fichier Excel
                    resultats.to_excel(chemin_sauvegarde, index=False, header=False)
                    print(f"Résultats sauvegardés dans '{chemin_sauvegarde}'.")
                else:
                    print("Aucun fichier de sauvegarde sélectionné.")
                break  # Sortir de la boucle après la sauvegarde
            elif action == 'r':
                continue  # Refaire une recherche
            else:
                print("Action invalide ou aucun résultat à sauvegarder.")
                break

    except Exception as e:
        print(f"Erreur en lisant {fichier_xlsx}: {e}")

# Appeler la fonction pour lancer le processus de recherche
rechercher_dans_xlsx()
