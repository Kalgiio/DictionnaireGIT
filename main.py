#modification apporté
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
    for cle, valeur in dicomiam.items():
        print("La recette pour", cle, "est : ", valeur)

def main():
    initialiser()

if __name__ == '__main__':
    main()

