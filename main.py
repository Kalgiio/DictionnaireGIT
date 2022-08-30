def ajouterunplat(dicomiam):
    nouveauplat = input("Veuillez entrer le nom du nouveau plat")
    listeingredient = input("Veuillez entrer les ingrédients du nouveau plat")
    dicomiam[nouveauplat]=listeingredient


def initialiser():
    dicomiam = {"Tarte au citron meringuée": ["Farine",
                                              "Beurre",
                                              "Sucre",
                                              "Sucre glace",
                                              "Oeuf",
                                              "Sel",
                                              "Crème au citron",
                                              "Jus de citron",
                                              "Meringue"],
                "Kefta": ["oignons",
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
    menuPrincipale(dicomiam)


def modifierunplat(dicomiam):
    print("ajouter le plat a modifier")
    return


def supprimerplat(dicomiam):
    platsupprime = input()
    for i in dicomiam:
        print(i)
    for j in dicomiam:
        if j == platsupprime:
            del dicomiam[j]
        else:
            print("Erreur : Le plat n'est pas dans la liste")


def remplacerunplat(dicomiam):
    supprimerplat(dicomiam)
    ajouterunplat(dicomiam)


def afficherplat(dicomiam):
    for cle, valeur in dicomiam.items():
        print("La recette pour", cle, "est : ", valeur)


def menuPrincipale(dicomiam):
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
        match choix:
            case "1":
                afficherplat(dicomiam)
            case "2":
                ajouterunplat(dicomiam)
            case "3":
                supprimerplat(dicomiam)
            case "4":
                modifierunplat(dicomiam)
            case "5":
                platsupprime = input()
                for i in dicomiam:
                    print(i)
                for j in dicomiam:
                    if j == platsupprime:
                        del dicomiam[j]
                    else:
                        print("Erreur : Le plat n'est pas dans la liste")
                print()
                platremplace = input()
                print("Quel liste d'ingrédient voulez-vous mettre dans ce plât ?")
                listeingredient = input()
                dicomiam[platremplace].remove()
                dicomiamtmp = {platremplace}
                remplacerunplat(dicomiam)
            case "q":
                flag = False
            case _:
                print("Erreur : Commande incorrecte")
    print("Aurevoir")


def main():
    initialiser()


if __name__ == '__main__':
    main()
