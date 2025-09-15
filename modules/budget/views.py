# modules/budget/views.py
import os
import time
from core.utils import create_file

DEFAULT_HEADER = ["Date", "Description", "Catégorie", "Montant"]
DATA_DIR = os.path.join(os.getcwd(), "data")
DEFAULT_FILE = os.path.join(DATA_DIR, "budget.csv")

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
            pass
        elif choix == "2":
            pass
        elif choix == "3":
            pass
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
