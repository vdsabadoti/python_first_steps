# Démonstration : Débogage - Rechercher les erreurs|anomalies|incohérences (~5)

TAB, RAL = '\t', '\n' # Tabulation, Retour À la Ligne

def afficher_info(message, nb_car=80, symb='#'):
    print(RAL + nb_car * symb)
    print(message.center(nb_car))
    print(nb_car * symb)

def saisir_nombre(question, details=""):
    if len(details): print(details)
    return int(input(question + RAL))

def choix_categorie_age():
    age = saisir_nombre("Quel est votre âge ?", 
        "Afficher la catégorie en fonction de l'âge")
    AGE_MAJORITE, AGE_SENIOR = 18, 70
    if 0 < age < AGE_MAJORITE: categorie_age = "mineur"
    elif AGE_MAJORITE <= age < AGE_SENIOR : categorie_age = "majeur"
    elif AGE_SENIOR <= age: categorie_age = "senior"
    else: categorie_age = "indéterminé" # par défaut
    print("Vous êtes donc un", categorie_age)
    
def afficher_table_division(limite=10):
    nb = saisir_nombre("Indiquer un nombre ?", 
        "Afficher une table de division")
    print("Table de division de", nb, "jusqu'à", limite, ":")
    for i in range(1, limite + 1):
        print(TAB, nb, "÷", i, "=", nb / i)

def afficher_couleurs_ArcEnCiel():
    print("Voici les couleurs de l'arc-en-ciel")
    ARC_EN_CIEL = "rouge, orange, jaune, vert, bleu, indigo, violet"
    print(TAB + ARC_EN_CIEL.replace(', ', RAL + TAB).title())

def main():
    afficher_info("Bienvenue dans cette démonstration sur la recherche d'erreurs")
    choix = saisir_nombre("Quel est votre choix ?",
        """Voici les propositions :
    1 - Afficher si mineur/majeur/senior
    2 - Afficher une table de division
    3 - Afficher les couleurs de l'arc en ciel""")

    if choix == 1:
        choix_categorie_age() #Choix n°1 
    elif choix == 2:
        afficher_table_division() #Choix n°2
    elif choix == 3:
        afficher_couleurs_ArcEnCiel() #Choix n°3
    else:
        afficher_info("Désolé, mais ce choix n'est pas dans la liste des propositions !") #Choix n°?

# Appel du programme principal
main()
print('_' * 64, "Fin de la démonstration")
