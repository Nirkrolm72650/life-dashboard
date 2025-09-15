def main_budget_menu():
    print("###############################")
    print("### BIENVENUE DANS FINANCES ###")
    print("###############################")
    
    print("Description :")
    print("""
            Cet outil permet d'ajouter une dépense ou un revenu. 
            Il permet également d'établir un résumé des dépenses ou des revenu grâce 
            à un graphique permettant de comparer par mois ou par semaines
    """)

    while True:
        print("[1] - 💸 Ajouter une dépense")
        print("[2] - 💰 Ajouter un revenu")
        print("[3] - 📜 Résumé des dépenses")
        print("[4] - 📜 Résumé des revenus")
        print("[5] - 📝 Créer un fichier de dépense")
        print("[6] - 📝 Créer un fichier de revenu")

        choix = input("> Votre choix : ")

        if choix == 1:
            pass
        elif choix == 2:
            pass
        elif choix == 3:
            pass
        elif choix == 4:
            pass
        elif choix == 5:
            pass
        elif choix == 6:
            pass
        else:
            print("❌ Choix incorrect. Veuillez recommencer")

