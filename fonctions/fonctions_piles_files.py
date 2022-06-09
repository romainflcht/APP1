# Copyright : romain_flcht

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# ////////////////////////////////// Fichier : fonction script de pile et de files /////////////////////////////////// #
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def est_vide(pile_file: list) -> bool:
    return pile_file == []


def empiler(pile: list, element: int) -> list:
    """
    Fonction script 'empiler' pour la structure de donnée 'Piles'.

    :param element: Elément à empiler dans la pile.
    :param pile: Pile mis en paramètre à laquelle on va ajouter l'élément.
    :return: On renvoie la pile avec l'élément empilé.
    """

    pile.append(element)
    return pile


def enfiler(file: list, element: int) -> list:
    """
    Fonction script 'enfiler' pour la structure de donnée 'Files'.

    :param element: Elément à enfiler dans la file.
    :param file: File mis en paramètre à laquelle on va ajouter l'élément.
    :return: On renvoie la pile avec l'élément enfilé.
    """

    file.append(element)
    return file


def depiler(pile: list):
    """
    Fonction script qui dépile les structures de données 'Pile'.

    :param pile: Pile passée en paramètre qui va être dépilé.
    :return: En revoie l'élément dépilé et la pile dépilé.
    """
    if est_vide(pile):
        # Depilage d'une pile déja vide...
        return False

    # Revoie de l'élément dépilé ainsi que de la nouvelle valeur de la pile.
    return pile.pop()


def defiler(file: list):
    """
    Fonction script qui défiler les structures de données 'File'.

    :param file: File passée en paramètre qui va être défilé.
    :return: En revoie l'élément défilé et la file défilé.
    """
    if est_vide(file):
        # Defilage d'une file déja vide...
        return False

    # Revoie de l'élément fépilé ainsi que de la nouvelle valeur de la file.
    return file.pop(0)


def obtenir_premier_elt_pile(pile: list):
    """
    Fonction qui permet d'obtenir le premier élément d'une pile.

    :param pile: Pile que l'on va lire.
    :return: Renvoie le premier élément de la Pile.
    """

    if est_vide(pile):
        # Pile vide, pas d'élément à obtenir.
        return None

    else:
        # Renvoie le premier élément de la pile.
        return pile[len(pile) - 1]


def obtenir_premier_elt_file(file: list):
    """
    Fonction qui permet d'obtenir le premier élément d'une file.

    :param file: File que l'on va lire.
    :return: Renvoie le premier élément de la file.
    """

    if est_vide(file):
        # File vide, pas d'élément à obtenir.
        return None

    else:
        # Renvoie le premier élément de la file.
        return file[0]


if __name__ == '__main__':
    print('Ce fichier ne doit pas être executé tout seul, il doit être importé à partir d\'un autre script...')
