# Copyright : romain_flcht

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# //////////////////////////////////// Fichier : fonction d'affichage de tube //////////////////////////////////////// #
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def afficher_pile(pile: list, nom_pile='  pile  ', espacement_gauche=31) -> None:
    """
    Fonction qui affiche correctement la pile.

    :param pile: La pile qui sera affiché.
    :param nom_pile: Nom de la pile qui sera affiché.
    :param espacement_gauche: Valeur entière permettant de régler l'espacement du coté gauche de la console.
    :return: None
    """

    screen_str = f'{" " * espacement_gauche}{nom_pile}\n{" " * espacement_gauche}╔  ↑↓  ╗\n'

    for elt in pile[::-1]:
        screen_str += f'{" " * espacement_gauche}║  {elt if int(elt) > 9 else "0" + str(elt)}  ║\n'

    print(screen_str + f'{" " * espacement_gauche}╚══════╝')


def afficher_file(file: list, nom_file='  file  ', espacement_gauche=31) -> None:
    """
    Fonction qui affiche correctement la file.

    :param file: La pile qui sera affiché.
    :param nom_file: Nom de la file qui sera affiché.
    :param espacement_gauche: Valeur entière permettant de régler l'espacement du coté gauche de la console.
    :return: None
    """

    screen_str = f'{" " * espacement_gauche}{nom_file}\n{" " * espacement_gauche}╔  ↑   ╗\n'

    for elt in file:
        screen_str += f'{" " * espacement_gauche}║  {elt if elt > 9 else "0" + str(elt)}  ║\n'

    print(screen_str + f'{" " * espacement_gauche}╚   ↑  ╝\n')


def afficher_silos(silos: list) -> None:
    """
    Fonction qui permet un affichage horizontale des silos.

    :param silos: Silos qui seront affichés horizontalement.
    :return: None.
    """

    if not silos:
        return

    # On range les silos du plus rempli au moins rempli, ce qui permet de ne pas avoir de bug d'affichage.
    silos = sorted(silos, key=lambda x: len(x), reverse=True)

    affichage_silos = ''
    max_len = len(silos[0])

    for index_vertical in range(max_len + 1, -3, -1):
        for index_horizontal, silo in enumerate(silos):

            # Affichage du numéro du silo en dernière ligne.
            if index_vertical == - 2:
                affichage_silos += f'silo n°{index_horizontal}{"    " if index_horizontal <= 9 else "   "}'

            # Affichage du bas de la pile.
            elif index_vertical == -1:
                affichage_silos += f'╚══════╝    '

            # Affichage du haut de la pile.
            elif index_vertical == len(silo):
                affichage_silos += f'╔  ↑↓  ╗    '

            # Affichage des valeurs ainsi que des contours du silo.
            elif index_vertical < len(silo):
                # On rajoute un espace si le conteneur a une valeur inférieure à 10 pour éviter un décalage.
                if silo[index_vertical] > 9:
                    affichage_silos += f'║  {silo[index_vertical]}  ║    '
                else:
                    affichage_silos += f'║   {silo[index_vertical]}  ║    '

        affichage_silos += '\n'

    # On affiche le tout.
    print(affichage_silos)


if __name__ == '__main__':
    print('Ce fichier ne doit pas être executé tout seul, il doit être importé à partir d\'un autre script...')
