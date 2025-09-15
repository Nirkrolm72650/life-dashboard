# core/utils.py
import csv
import os

def create_file(path=None, filename="budget.csv", header=None):
    """
    Crée le fichier CSV avec header si nécessaire.
    - path : dossier (chemin) où créer le fichier. Si None ou vide -> cwd/data
    - filename : nom du fichier (avec ou sans .csv)
    Retourne le chemin absolu du fichier créé (ou existant).
    """
    header = header or ["Date", "Description", "Catégorie", "Montant"]

    if not path:
        path = os.path.join(os.getcwd(), "data")
    full_dir = os.path.abspath(path)
    os.makedirs(full_dir, exist_ok=True)

    if not filename.lower().endswith(".csv"):
        filename = filename + ".csv"

    full_path = os.path.join(full_dir, filename)

    if os.path.exists(full_path):
        # fichier déjà présent : on ne l'écrase pas
        return full_path

    with open(full_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)

    return full_path

def append_row(path, row):
    """
    Ajoute une ligne (list) à un CSV existant.
    Si le dossier n'existe pas, le crée.
    """
    dirpath = os.path.dirname(path)
    if dirpath and not os.path.exists(dirpath):
        os.makedirs(dirpath, exist_ok=True)

    with open(path, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(row)

def read_csv(path):
    """Retourne la liste des lignes d'un CSV (y compris header) ou [] si inexistant."""
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        return list(reader)
