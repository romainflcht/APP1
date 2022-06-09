# Copyright : romain_flcht

from fonctions.fonctions_piles_files import est_vide, depiler, empiler


def vidange_silos(silos: list, silo_final: list) -> None:
    """
    Fonction qui dépile tout les silos en un seul silo.
    :param silos: Silos a dépilé.
    :param silo_final: Silo dans lequel tout les conteneurs seront dépilé.
    :return:
    """
    for silo in silos:
        while not est_vide(silo):
            empiler(silo_final, depiler(silo))
