# Copyright : romain_flcht

from fonctions.fonctions_affichage import afficher_pile, afficher_file, afficher_silos
from fonctions.algo_repartition.algorithme import algorithme_tri_silos
from fonctions.algo_repartition.vidange_silos import vidange_silos
from fonctions.fonctions_piles_files import empiler, defiler
from fonctions.fonction_generation import generation_tube
from acsii_art.ascii_art import texte_debut_programme, texte_au_revoir
from time import time

if __name__ == '__main__':
    print(texte_debut_programme, end='')
    input('• [✔] Appuyez sur entrée pour déclancher l\'évacuation d\'urgence...')

    # Génération du tube et de tout les silos nécéssaires.
    tube = generation_tube(5)
    silo_temporaire = []
    silos = [[], [], []]
    silo_final = []

    print('\n• [~] Vidange du Tube principal en cours...', end='\n\n')

    afficher_file(tube, '  Tube  ')
    afficher_pile(silo_temporaire, 'silo_temp.')

    # Défilage du tube dans le silo temporaire.
    for _ in range(len(tube)):
        empiler(silo_temporaire, defiler(tube))

    print('\n• [✔] Vidange du Tube principal terminé !', end='\n\n')

    afficher_file(tube, '  Tube  ')
    afficher_pile(silo_temporaire, 'silo_temp.')

    print('\n• [~] Répartition du silo temporaire en cours...')
    start_timer = time()
    algorithme_tri_silos(silos, silo_temporaire)

    afficher_silos(silos)

    print('• [✔] Répartition du silo temporaire terminé en {:e} secondes ! '.format(time() - start_timer), end='\n\n')
    print('• [~] Regroupement des conteneurs en cours...', end='\n\n')

    vidange_silos(silos, silo_final)

    afficher_pile(silo_final, 'silo_final')
    print('\n• [✔] Regroupement des conteneurs terminé ! À bientôt :)', end='\n\n')
    print(texte_au_revoir, end='\n\n')
