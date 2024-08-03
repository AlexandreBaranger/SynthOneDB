import tkinter as tk
from tkinter import scrolledtext

def generate_sequence(freq, val1, val2, duration):
    sequence = ""
    elapsed_time = 0
    counter = 0

    while elapsed_time < duration:
        seconds = elapsed_time // 1000
        milliseconds = elapsed_time % 1000
        if counter % 2 == 0:
            sequence += f"{seconds}.{milliseconds:03d}_{val1}\n"
        else:
            sequence += f"{seconds}.{milliseconds:03d}_{val2}\n"
        elapsed_time += freq
        counter += 1

    return sequence

def on_generate():
    try:
        frequency = float(entry_frequency.get().replace(',', '.'))
        value1 = int(entry_value1.get())
        value2 = int(entry_value2.get())
        duration = float(entry_duration.get().replace(',', '.'))

        # Convertir les valeurs en millisecondes
        frequency_ms = int(frequency * 1000)
        duration_ms = int(duration * 1000)

        result = generate_sequence(frequency_ms, value1, value2, duration_ms)
        text_output.delete(1.0, tk.END)
        text_output.insert(tk.END, result)
    except ValueError:
        text_output.delete(1.0, tk.END)
        text_output.insert(tk.END, "Veuillez entrer des valeurs valides.")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Générateur de Séquence")

# Création des champs de saisie et des étiquettes
label_frequency = tk.Label(root, text="Fréquence (s.ms):")
label_frequency.grid(row=0, column=0, padx=5, pady=5)
entry_frequency = tk.Entry(root)
entry_frequency.grid(row=0, column=1, padx=5, pady=5)

label_value1 = tk.Label(root, text="Valeur 1:")
label_value1.grid(row=1, column=0, padx=5, pady=5)
entry_value1 = tk.Entry(root)
entry_value1.grid(row=1, column=1, padx=5, pady=5)

label_value2 = tk.Label(root, text="Valeur 2:")
label_value2.grid(row=2, column=0, padx=5, pady=5)
entry_value2 = tk.Entry(root)
entry_value2.grid(row=2, column=1, padx=5, pady=5)

label_duration = tk.Label(root, text="Durée (s.ms):")
label_duration.grid(row=3, column=0, padx=5, pady=5)
entry_duration = tk.Entry(root)
entry_duration.grid(row=3, column=1, padx=5, pady=5)

# Bouton pour générer la séquence
button_generate = tk.Button(root, text="Générer", command=on_generate)
button_generate.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Zone de texte pour afficher la séquence générée
text_output = scrolledtext.ScrolledText(root, width=40, height=10)
text_output.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Lancement de la boucle principale de l'interface
root.mainloop()
