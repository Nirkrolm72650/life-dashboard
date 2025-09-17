# modules/budget/views.py
import os
import time
from datetime import datetime
from core.utils import create_file
import pandas as pd
import json


DEFAULT_HEADER = ["Date", "Description", "Catégorie", "Montant", "Total"]
DATA_DIR = os.path.join(os.getcwd())
DEFAULT_FILE = os.path.join(DATA_DIR, "budget.csv")
CONFIG_FILE = "config.json"


# Vérifie ou créer un fichier CSV
def ensure_budget_file(path=None):
    """S'assure que le fichier existe ; renvoie le chemin absolu."""
    if path is None or path.strip() == "":
        path = DEFAULT_FILE
    else:
        # si user a donné dossier+nom possible, on gère
        path = os.path.abspath(path)

    dirpath = os.path.dirname(path)
    filename = os.path.basename(path)
    create_file(dirpath, filename, header=DEFAULT_HEADER)
    return path



# -------------------------------
# Gestion du fichier de config
# -------------------------------
def save_config(path):
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump({"last_file": path}, f)

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            return json.load(f).get("last_file")
    return None

# -------------------------------
# Vérifie ou crée un fichier CSV
# -------------------------------
def ensure_budget_file(path=None):
    # si aucun chemin donné → essayer de reprendre celui du config.json
    if not path:
        path = load_config()
    # si toujours rien → proposer à l’utilisateur
    if not path:
        dossier = input("Chemin du dossier (vide = ./data/) : ").strip()
        if not dossier:
            dossier = os.path.join(os.getcwd(), "data")
        os.makedirs(dossier, exist_ok=True)

        name = input("Nom du fichier (sans extension) [budget] : ").strip()
        if not name:
            name = "budget"

        path = os.path.join(dossier, name + ".csv")

    # crée le fichier si inexistant
    if not os.path.exists(path):
        header = ["Date", "Description", "Catégorie", "Montant", "Total"]
        pd.DataFrame(columns=header).to_csv(path, index=False, encoding="utf-8")
        print(f"✅ Nouveau fichier créé : {path}")

    # sauvegarde dans config.json
    save_config(path)
    return path

def show_all(path=None):
    path = ensure_budget_file(path)
    rows = read_csv(path)
    if not rows or len(rows) == 1:
        print("Aucune donnée enregistrée.")
        return
    header = rows[0]
    print(" | ".join(header))
    for row in rows[1:]:
        print(" | ".join(row))


def add_expense(path=None):
    path = ensure_budget_file(path)

    print(f"➡️  Utilisation du fichier : {path}")

    date = input("Entrer la date (JJ/MM/AAAA) [vide = aujourd'hui] : ").strip()
    if not date:
        date = datetime.now().strftime("%d/%m/%Y")

    description = input("Entrer la description : ").strip()
    category = input("Entrer la catégorie : ").strip()

    while True:
        montant = input("Entrer le montant (€) : ").strip().replace(",", ".")
        try:
            montant = float(montant)
            break
        except ValueError:
            print("❌ Montant invalide - recommencez.")

    # Charger le CSV
    df = pd.read_csv(path)

    # Calcul du total cumulatif
    if df.empty:
        total_depense = montant
    else:
        total_depense = df["Total"].iloc[-1] + montant

    # Ajouter la ligne
    new_row = [date, description, category, f"{montant:.2f}", f"{total_depense:.2f}"]
    df.loc[len(df)] = new_row
    df.to_csv(path, index=False, encoding="utf-8")

    print("✅ Dépense ajoutée avec succès.")
    print(df.tail())  # affiche les dernières lignes pour contrôle



def main_budget_menu():
    while True:
        print("\n###############################")
        print("### BIENVENUE DANS FINANCES ###")
        print("###############################\n")

        print("[1] - 💸 Ajouter une dépense")
        print("[2] - 💰 Ajouter un revenu")
        print("[3] - 📜 Afficher toutes les entrées")
        print("[4] - ❌ (placeholder)")
        print("[5] - 📝 Créer un fichier de dépense")
        print("[0] - ↩️ Retour / Quitter")

        choix = input(" > Votre choix : ").strip()

        if choix == "1":
            add_expense(path=None)
        elif choix == "2":
            pass
        elif choix == "3":
            show_all(path=None)
        elif choix == "4":
            print("🚧 Cette fonctionnalité n'est pas encore disponible.")
        elif choix == "5":
            # demande dossier et nom
            path = input("Chemin du dossier (laisser vide = ./data/) : ").strip()
            name = input("Nom du fichier (sans extension) [budget] : ").strip()
            if not name:
                name = "budget"
            
            if not path:
                path_to_use = os.path.join(os.getcwd(), "data", name + ".csv")
            else:
                path_to_use = os.path.join(path, name + ".csv")
            
            try:
                full = ensure_budget_file(path_to_use)
                print(f"Création du fichier en cours... : {full}")
                time.sleep(2)
            except Exception as e:
                print("Erreur création fichier :", e)
        elif choix == "0":
            break
        else:
            print("❌ Choix incorrect. Veuillez recommencer")
