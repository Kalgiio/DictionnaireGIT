
#uojefoiuzepfizj
def ajouterunplat()
    input("Veuillez entrer le nom du nouveau plat")
    input("Veuillez entrer les ingrédients du nouveau plat")

def initialiser():
    dicomiam = {"Tarte au citron meringuée":["Farine",
                                            "Beurre",
                                            "Sucre",
                                            "Sucre glace",
                                            "Oeuf",
                                            "Sel",
                                            "Crème au citron",
                                            "Jus de citron",
                                            "Meringue"],
                "Kefta":["oignons",
                         "persil",
                         "poivre",
                         "sel",
                         "cumin",
                         "paprika",
                         "huile d'olive",
                         "viande hachée",
                         "tomates pelées",
                         "oeuf"
]}
    print("============= Test affichage =============")
    for cle, valeur in dicomiam.items():
        print("La recette pour", cle, "est : ", valeur)
    print("============= Test affichage =============")
    menuPrincipale()


def modifierunplat():
    print("ajouter le plat a modifier")
    return

def supprimerplat():
    print("Quel plat voulez-vous supprimer ?")
    return

def remplacerunplat():
    print("quel est le plat a remplacer")
    return

def menuPrincipale():
    print("Bonjour")
    flag = True
    while flag:
        print("Que souhaitez-vous faire ? ")
        print("1. Afficher les plats")
        print("2. Ajouter des plats")
        print("3. Supprimer des plats")
        print("4. Modifier des plats")
        print("5. Remplacer des plats")
        print("q. Quitter")
        choix = input()
    match choix :
        case "1":
            print("Afficher les plats")
            return menuPrincipale()
        case "2":
            return ajouterunplat()
        case "3":
            return supprimerplat()
        case "4":
            return modifierunplat()
        case "5":
            return remplacerunplat()
        case "q":
            flag = False
        case _:
            print("Erreur : Commande incorrecte")
    print("Aurevoir")




def main():
    initialiser()

if __name__ == '__main__':
    main()

