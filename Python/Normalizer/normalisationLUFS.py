import tkinter as tk
from tkinter import filedialog
import os
import subprocess
import shutil

def normalize_audio(input_file, output_file):
    # Chemin vers l'exécutable FFmpeg
    ffmpeg_path = 'C:/FFmpeg/bin/ffmpeg.exe'

    output_file = os.path.splitext(output_file)[0] + '.wav'
    # Commande FFmpeg pour la normalisation avec loudness range target à -18 LUFS
    command = [ffmpeg_path, '-i', input_file, '-af', 'loudnorm=I=-9:LRA=11:tp=-2', '-ar', '96000', '-acodec', 'pcm_s24le', output_file]

    # Exécution de la commande FFmpeg
    subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    print("Normalisation terminée avec succès.")

def normalize_files_in_folder(input_folder, output_folder):
    # Parcourir récursivement tous les fichiers et dossiers dans le dossier source
    for root, dirs, files in os.walk(input_folder):
        # Parcourir tous les fichiers dans le dossier actuel
        for file in files:
            # Vérifie si le fichier est un fichier audio (vous pouvez ajouter plus de conditions si nécessaire)
            if file.lower().endswith(('.mp3', '.wav', '.flac', '.ogg')):
                input_file = os.path.join(root, file)
                # Créer l'arborescence des dossiers dans le dossier de sortie s'ils n'existent pas déjà
                relative_path = os.path.relpath(root, input_folder)
                output_directory = os.path.join(output_folder, relative_path)
                os.makedirs(output_directory, exist_ok=True)
                output_file = os.path.join(output_directory, file)
                # Normalisation du fichier audio
                normalize_audio(input_file, output_file)
                print("Fichier audio normalisé créé :", output_file)

# Dialogue de sélection de dossier d'entrée
root = tk.Tk()
root.withdraw()
input_folder = filedialog.askdirectory(title="Sélectionnez le dossier contenant les fichiers audio à normaliser")

if input_folder:
    # Dialogue de sélection de dossier de sortie
    output_folder = filedialog.askdirectory(title="Sélectionnez le dossier de sortie")

    if output_folder:
        # Normalisation des fichiers dans le dossier d'entrée et sortie
        normalize_files_in_folder(input_folder, output_folder)
    else:
        print("Aucun dossier de sortie sélectionné.")
else:
    print("Aucun dossier d'entrée sélectionné.")
