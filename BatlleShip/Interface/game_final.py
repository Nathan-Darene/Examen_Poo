import pygame
# import sys
# import random

#importation des modulle necessaire 

from game_start import*

# Initialisation de Pygame
pygame.init()

# Constantes de la fenêtre
LARGEUR_ECRAN = 1920  # Largeur de la fenêtre de jeu
HAUTEUR_ECRAN = 1080  # Hauteur de la fenêtre de jeu
TAILLE_GRILLE = 10  # Taille de la grille (10x10)
TAILLE_CELLULE = 45  # Taille de chaque cellule de la grille
MARGE = 5  # Marge entre les cellules de la grille
ESPACE_ETIQUETTES = 30  # Espace pour les étiquettes de ligne et colonne

# Couleurs utilisées dans le jeu
GRIS = (199, 199, 199)  # Couleur de fond
BLANC = (255, 255, 255)  # Couleur des cellules
NOIR = (0, 0, 0)  # Couleur des lignes de la grille et du texte
VERT = (0, 255, 0)  # Couleur du bouton "Prêt"



# Placer des bateaux de manière fixe pour le test
def configurer_jeu():
    jeu = game_start()

    # Placement fixe des navires pour le joueur 1
    jeu.grille1.placer_bateau(1, 1, "porte_avions", 'H')
    jeu.grille1.placer_bateau(2, 2, "croiseur", 'H')
    jeu.grille1.placer_bateau(3, 3, "contre_torpilleur", 'H')
    jeu.grille1.placer_bateau(4, 4, "sous_marin", 'H')
    jeu.grille1.placer_bateau(5, 5, "torpilleur", 'H')

    # Placement aléatoire des navires pour le joueur 2
    jeu.grille2.placer_bateaux_aleatoires()

    # Exécute le jeu
    jeu.executer_jeu()

if __name__ == "__main__":
    configurer_jeu()
