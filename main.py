
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

def menuPrincipale():
    print("1 . Afficher les plats")
    print("2 . Ajouter des plats")
    print("3 . Supprimer des plats")
    print("4 . Modifier des plats")
    print("5 . Remplacer des plats")
    choix = input("Du coup on fait quoi ? ")
    match choix :
        case "1":
            print("Afficher les plats")
            return menuPrincipale()
        case _:
            print("On à pas ajouter les autres")
            return menuPrincipale()




def main():
    initialiser()

if __name__ == '__main__':
    main()

