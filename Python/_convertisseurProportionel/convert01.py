import tkinter as tk

def convertir_playback_rate(valeur, echelle_initiale_max=100, echelle_finale_max=4):
    if not (0 <= valeur <= echelle_initiale_max):
        raise ValueError(f"La valeur doit être comprise entre 0 et {echelle_initiale_max}")
    return (valeur / echelle_initiale_max) * echelle_finale_max

def convertir_attack_curve(valeur, echelle_initiale_min=-1, echelle_initiale_max=1, echelle_finale_max=100):
    if not (echelle_initiale_min <= valeur <= echelle_initiale_max):
        raise ValueError(f"La valeur doit être comprise entre {echelle_initiale_min} et {echelle_initiale_max}")
    return ((valeur - echelle_initiale_min) / (echelle_initiale_max - echelle_initiale_min)) * echelle_finale_max

def convertir_attack_time(valeur, echelle_initiale_min=-1, echelle_initiale_max=1, echelle_finale_max=1):
    if not (echelle_initiale_min <= valeur <= echelle_initiale_max):
        raise ValueError(f"La valeur doit être comprise entre {echelle_initiale_min} et {echelle_initiale_max}")
    return ((valeur - echelle_initiale_min) / (echelle_initiale_max - echelle_initiale_min)) * echelle_finale_max

def convertir_decay_time(valeur, echelle_initiale_min=-1, echelle_initiale_max=1, echelle_finale_max=1):
    if not (echelle_initiale_min <= valeur <= echelle_initiale_max):
        raise ValueError(f"La valeur doit être comprise entre {echelle_initiale_min} et {echelle_initiale_max}")
    return ((valeur - echelle_initiale_min) / (echelle_initiale_max - echelle_initiale_min)) * echelle_finale_max

def calculer_conversion():
    try:
        playback_rate = float(entry_playback_rate.get())
        attack_curve = float(entry_attack_curve.get())
        attack_time = float(entry_attack_time.get())
        decay_time = float(entry_decay_time.get())

        playback_rate_converted = convertir_playback_rate(playback_rate)
        attack_curve_converted = convertir_attack_curve(attack_curve)
        attack_time_converted = convertir_attack_time(attack_time)
        decay_time_converted = convertir_decay_time(decay_time)

        # Formatage des résultats avec 2 décimales
        result_text.set(f"PlaybackRate (0-100 à 0-4) : {playback_rate_converted:.2f}\n"
                        f"AttackCurve (-1 à 1 à 0-100) : {attack_curve_converted:.2f}\n"
                        f"AttackTime (-1 à 1 à 0-1) : {attack_time_converted:.2f}\n"
                        f"DecayTime (-1 à 1 à 0-1) : {decay_time_converted:.2f}")
    except ValueError as e:
        result_text.set(f"Erreur : {e}")

# Interface utilisateur avec tkinter
app = tk.Tk()
app.title("Convertisseur de Valeurs")

# Configurer la fenêtre pour qu'elle soit toujours au-dessus
app.attributes('-topmost', True)

# Labels
tk.Label(app, text="PlaybackRate (0-100)").grid(row=0, column=0, padx=10, pady=5)
tk.Label(app, text="AttackCurve (-1 à 1)").grid(row=1, column=0, padx=10, pady=5)
tk.Label(app, text="AttackTime (-1 à 1)").grid(row=2, column=0, padx=10, pady=5)
tk.Label(app, text="DecayTime (-1 à 1)").grid(row=3, column=0, padx=10, pady=5)

# Entrées
entry_playback_rate = tk.Entry(app)
entry_attack_curve = tk.Entry(app)
entry_attack_time = tk.Entry(app)
entry_decay_time = tk.Entry(app)

entry_playback_rate.grid(row=0, column=1, padx=10, pady=5)
entry_attack_curve.grid(row=1, column=1, padx=10, pady=5)
entry_attack_time.grid(row=2, column=1, padx=10, pady=5)
entry_decay_time.grid(row=3, column=1, padx=10, pady=5)

# Bouton de calcul
btn_calculer = tk.Button(app, text="Calculer", command=calculer_conversion)
btn_calculer.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Texte de résultat
result_text = tk.StringVar()
result_label = tk.Label(app, textvariable=result_text, justify="left")
result_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Lancement de l'application
app.mainloop()
