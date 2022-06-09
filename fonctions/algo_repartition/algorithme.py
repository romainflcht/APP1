# Copyright : romain_flcht

from fonctions.algo_repartition.tri import *


def algorithme_tri_silos(silos: list, silo_temporaire: list, debug=False) -> None:
    """
        Fonction algorithme qui associe les deux fonctions 'tri_piles' et 'tri_est_possible' pour former un algorithme
        de répartition dans les silos.

        :param silos: Liste de liste dans lesquelles les conteneurs seront répartis.
        :param silo_temporaire: Liste qui contient les conteneurs à répartir.
        :param debug: Booléen qui indique si oui ou non la fonction doit afficher les textes deboguages.
        :return: None.
        """

    # Création d'une liste contenant la totalité des position que peut prendre le curseur
    # lors du dépilage du silo temporaire.
    curseurs = [position for position in range(len(silos))]

    # Initialisation de la dernière position du curseur à -1 pour indiquer qu'il n'y a pas encore de dernière position.
    dernier_curseur = -1

    # Compteur de boucle permettant de savoir où on en est en mode déboguage.
    compteur_boucle = 1

    # Print de débogage.
    if debug:
        print('➔ Début de la fonction \'algorithme_tri_silos\'. ' + '―' * 35)

    # On execute notre algorithme tant que le silo temporaire n'est pas vide.
    while not est_vide(silo_temporaire):

        # Dépilage du silo temporaire et déclaration d'un booléen permettant de tester si le conteneur dépilé
        # a été correctement placé dans les silos.
        valeur_a_place = depiler(silo_temporaire)
        valeur_a_ete_place = False

        # Print de déboguage.
        if debug:
            print(f'➔ Tour de boucle n°{compteur_boucle} : ')
            print(f'    • [✔] Dépilage du conteneur n°{valeur_a_place} du silo temporaire.', end='\n\n')
            print('➔ Début de la répartition dans les silos. ' + '―' * 38)

        # Placement du conteneur dépilé dans les silos.
        for curseur in curseurs:

            # On vérifie si le conteneur n'a pas déjà été placé.
            if not valeur_a_ete_place:

                # On vérifie si le dernier conteneur a été mis dans le même silo.
                if curseur != dernier_curseur:

                    # Si le silo selectionné par le curseur est vide, alors on place le conteneur dans celui-ci.
                    if not silos[curseur]:

                        # Empilage du conteneur, on déclare que le conteneur a été placé et on sauvegarde
                        # le curseur pour ne pas mettre le prochain conteneur au même endroit.
                        empiler(silos[curseur], valeur_a_place)
                        valeur_a_ete_place = True
                        dernier_curseur = curseur

                        # Print de déboguage.
                        if debug:
                            print(f'    • [✔] Le conteneur {valeur_a_place} a été placé dans le'
                                  f' silo n°{curseur + 1}.')

                    elif obtenir_premier_elt_pile(silos[curseur]) > valeur_a_place:

                        # Empilage du conteneur, on déclare que le conteneur a été placé et on sauvegarde
                        # le curseur pour ne pas mettre le prochain conteneur au même endroit.
                        empiler(silos[curseur], valeur_a_place)
                        valeur_a_ete_place = True
                        dernier_curseur = curseur

                        # Print de débogage.
                        if debug:
                            print(f'    • [✔] Le conteneur {valeur_a_place} a été placé dans le'
                                  f' silo n°{curseur + 1}.')

                    else:
                        # Print de déboguage.
                        if debug:
                            print('    • [✖] La valeur à placer est plus grande que la valeur dans le silo séléctionné'
                                  f' ({valeur_a_place} > {obtenir_premier_elt_pile(silos[curseur])})')

                        # La valeur du conteneur est plus grande que le premier élément du silo sélectionné,
                        # on n'empile pas le conteneur dans ce silo.

                else:
                    # Print de déboguage.
                    if debug:
                        print('    • [✖] Le silo sélectionné est le même qu\'au tour précédent, '
                              f'changement de silo.')

                    # Le curseur actuel est le même que le conteneur précédent,
                    # on n'empile pas le conteneur dans ce silo.

            else:
                # Print de déboguage.
                if debug:
                    print(f'    • [~] La valeur a déjà été placé.')

                # Le conteur est marqué comme déjà placé, on arrête la boucle.
                break

        if not valeur_a_ete_place:

            # Si après la boucle le conteneur n'est toujours pas placé, alors on
            # crée un nouveau silo dans lequel on ajoute notre conteneur.
            silos.append([valeur_a_place])
            curseurs.append(len(silos) - 1)
            dernier_curseur = curseurs[-1]

            # Print de débogage.
            if debug:
                print('    • [✔] La valeur n\'as pas été placé, création d\'un nouveau silo'
                      f' n°{len(curseurs)}.')

        if debug:
            print(f'\n➔ Résumé : Le conteneur {valeur_a_place} a été placé dans le silo n°{dernier_curseur + 1}.')
            print('➔ Fin de la répartition dans les silos. ' + '―' * 39, end='\n\n\n')

        # Tant que le tri est possible, alors on l'applique, permettant d'avoir des silos rangés.
        while tri_est_possible(silos, debug):

            # Exécution du tri.
            tri_piles(silos)

        # Print de débogage.
        if debug:
            print(f'➔ Fin tour de boucle n°{compteur_boucle}.')
            print('➔ Fin de la fonction \'algorithme_tri_silos\'. ' + '―' * 36, end='\n\n')

        compteur_boucle += 1


if __name__ == '__main__':
    print('Ce fichier ne doit pas être executé tout seul, il doit être importé à partir d\'un autre script...')
