import pygame
import sys
import random
from Grille import*
from main import*

# Initialisation de Pygame
pygame.init()

# Constantes de la fenêtre
LARGEUR_ECRAN = 1920
HAUTEUR_ECRAN = 1080
TAILLE_GRILLE = 10
TAILLE_CELLULE = 45  # Ajusté pour utiliser l'espace disponible
MARGE = 20

# Couleurs
GRIS = (199, 199, 199)
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)


# Placer des bateaux de manière fixe pour le test
def configurer_jeu():
    jeu = main()
                               

    jeu.grille1.placer_bateau(0, 0, "porte_avions", 'V')
    jeu.grille1.placer_bateau(4, 2, "croiseur", 'V')
    jeu.grille1.placer_bateau(6, 1, "contre_torpilleur", 'H')
    jeu.grille1.placer_bateau(7, 1, "sous_marin", 'H')
    jeu.grille1.placer_bateau(8, 3, "torpilleur", 'H')

    jeu.grille2.placer_bateaux_aleatoires()

    jeu.executer_jeu()

if __name__ == "__main__":
    configurer_jeu()
