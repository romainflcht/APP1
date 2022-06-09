# Copyright : romain_flcht

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# ////////////////////////////////// Fichier : fonction de génération du tube //////////////////////////////////////// #
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
from random import shuffle


def generation_tube(nb_element: int) -> list:
    """
    Fonction qui génère aléatoirement le contenu du tube.

    :param nb_element: Correspond au nombre de conteneurs à générer aléatoirement.
    :return: revoie une liste correspondant au tube contenant les conteneurs générés.
    """
    tube = []
    # Evite d'avoir deux fois le même nombre et donc évite le cas où deux conteneurs ont la même radioactivité.
    for i in range(1, nb_element + 1):
        tube.append(i)

    shuffle(tube)
    return tube


if __name__ == '__main__':
    print('Ce fichier ne doit pas être executé tout seul, il doit être importé à partir d\'un autre script...')
