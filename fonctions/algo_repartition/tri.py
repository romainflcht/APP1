# Copyright : romain_flcht

from fonctions.fonctions_piles_files import *


def obtenir_index_valeurs(silos: list, debug=False) -> tuple:
    """
    Fonction qui permet d'obtenir les deux premiers maximum, ainsi que leur index, des premiers éléments des silos
    présent dans la liste 'silos' mis en paramètre qui correspondent respectivement à la valeur sur laquel on va empiler
    l'autre valeur.
    :param silos: Liste contenant les silos dans lesquel seront répartit les conteneurs radioactifs.
    :param debug: Booléen qui indique si oui ou non la fonction doit afficher les textes deboguages.
    :return: Renvoie les index ainsi que les valeurs des deux premiers maximum.
    """

    # Création d'une liste qui contiendra les premiers éléments de chaques silos (-1 si le silo est vide).
    elt_silos = []

    # Récupération des premiers éléments de chaques silos.
    for silo in silos:
        if type(silo) is list:
            if not silo:
                # Si le silo est vide on met -1 pour conserver la bonne indexation.
                elt_silos.append(-1)
            else:
                # Sinon on ajoute la valeur du premier conteneur.
                elt_silos.append(obtenir_premier_elt_pile(silo))

    # Récupération de l'index et de la valeur du premier élément du silo dans lequel on depilera un conteneur.
    valeur_elt_empiler_sur = max(elt_silos)
    index_silo_emplier_sur = elt_silos.index(valeur_elt_empiler_sur)

    # On enlève le maximum pour trouver le second plus grand conteneur.
    elt_silos[index_silo_emplier_sur] = -1

    # Récuperation de l'index et de la valeur du second maximum qui sera alors empilé sur le conteur
    # précédemment trouvé (Le premier maximum).
    valeur_elt_a_depiler = max(elt_silos)
    index_silo_a_depiler = elt_silos.index(valeur_elt_a_depiler)

    # Print de déboguage
    if debug:
        print('➔ Début de la fonction \'obtenir_index_valeurs\'. ' + '―' * 35)
        print(f'    • À partir des silos {silos} : ')
        print(f'        ➔ On empilera {valeur_elt_a_depiler} (silo n°{index_silo_a_depiler})')
        print(f'        ➔ Sur {valeur_elt_empiler_sur} (silo n°{index_silo_emplier_sur})', end='\n\n')
        print('➔ Fin de la fonction \'obtenir_index_valeurs\'. ' + '―' * 36, end='\n\n\n')

    # Renvoie de toute les valeurs et index obtenus.
    return valeur_elt_empiler_sur, index_silo_emplier_sur, valeur_elt_a_depiler, index_silo_a_depiler


def tri_est_possible(silos: list, debug=False) -> bool:
    """
    Fonction qui vérifie si un réarrangement des conteneurs est possile. Si un réarrangement est possible, on renvoie
    'True' sinon on renvoie 'False'.

    Conditions pour qu'un réarrangement soit possible :
        ➔ Si le silo ne contient qu'un seul élément.
        ➔ Si la valeur sous le premier élément est plus grande que la valeur sur laquel l'élément sera empilé.

    :param silos: Liste contenant les silos dans lesquel seront répartit les conteneurs radioactifs.
    :param debug: Booléen qui indique si oui ou non la fonction doit afficher les textes deboguages.
    :return: Renvoie True ou False selon si le réarrangement est possible.
    """

    # Obtention de toutes les valeurs importantes au bon fonctionnement de la fonction.
    valeur_elt_empiler_sur, index_silo_emplier_sur, \
        valeur_elt_a_depiler, index_silo_a_depiler = obtenir_index_valeurs(silos, debug)

    if debug:
        print('➔ Début de la fonction \'tri_est_possible\'. ' + '―' * 38)

    # Verification des conditions pour lesquelles un réarrangement est possible.
    if valeur_elt_a_depiler == -1:

        # Print de déboguage.
        if debug:
            print('    • [✖] La valeur à déplacer est vide (-1), aucun déplacement ne sera fait.', end='\n\n')
            print('➔ Fin de la fonction \'tri_est_possible\'. ' + '―' * 39, end='\n\n\n')

        # Si la valeur a déplacer est vide, on ne le déplace pas.
        return False

    elif len(silos[index_silo_a_depiler]) <= 1:

        # Print de déboguage.
        if debug:
            print(f'    • [✔] Le silo ne possède qu\'un seul élément ({valeur_elt_a_depiler}),'
                  ' le déplacement sera effectué.', end='\n\n')
            print('➔ Fin de la fonction \'tri_est_possible\'. ' + '―' * 39, end='\n\n\n')

        # Si le silo ne contient qu'un seul élément, on le déplace.
        return True

    elif len(silos[index_silo_a_depiler]) >= 2:
        if silos[index_silo_a_depiler][-2] > valeur_elt_empiler_sur:

            # Print de déboguage.
            if debug:
                print('    • [✔] La valeur sous l\'élément à déplacer est plus grande que la valeur du conteneur sur '
                      f'lequel on va le déplacer ({silos[index_silo_a_depiler][-2]} > {valeur_elt_empiler_sur}), '
                      'le déplacement sera effectué.', end='\n\n')
                print('➔ Fin de la fonction \'tri_est_possible\'. ' + '―' * 39, end='\n\n\n')

            # Si la valeur sous l'élément à déplacer est plus grande que la valeur sur laquelle on le déplace,
            # alors on le déplace.
            return True

        else:

            # Print de déboguage.
            if debug:
                print('    • [✖] La valeur sous l\'élément à déplacer est plus petite que la valeur du conteneur sur '
                      f'lequel on va le déplacer ({silos[index_silo_a_depiler][-2]} < {valeur_elt_empiler_sur}), '
                      'aucun déplacement ne sera fait.', end='\n\n')
                print('➔ Fin de la fonction \'tri_est_possible\'. ' + '―' * 39, end='\n\n\n')

            # Sinon on ne le déplace pas.
            return False


def tri_piles(silos: list, debug=False) -> None:
    """
    :param silos: Liste contenant les silos dans lequels les conteneurs seront répartis.
    :param debug: Booléen qui indique si oui ou non la fonction doit afficher les textes deboguages.
    :return: None.
    """

    # Obtention de toutes les valeurs importantes au bon fonctionnement de la fonction.
    valeur_elt_empiler_sur, index_silo_emplier_sur, \
        valeur_elt_a_depiler, index_silo_a_depiler = obtenir_index_valeurs(silos, debug)

    # La fonction étant executé uniquement si un tri est possible, alors on ne re-vérifie pas si le tri est possible
    # et on l'effectue directement.
    empiler(silos[index_silo_emplier_sur], depiler(silos[index_silo_a_depiler]))


if __name__ == '__main__':
    print('Ce fichier ne doit pas être executé tout seul, il doit être importé à partir d\'un autre script...')
