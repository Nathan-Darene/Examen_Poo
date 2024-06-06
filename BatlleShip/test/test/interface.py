import pygame
import sys
from pygame.locals import *
from Bateau import *
from Grille import *
from Jeu import *

# Initialisation de Pygame
pygame.init()

# Définition des couleurs
BLANC = (255, 255, 255)
BLEU = (0, 0, 255)
NOIR = (0, 0, 0)

# Définition des dimensions de la fenêtre et de la grille
LARGEUR_FENETRE = 800
HAUTEUR_FENETRE = 600
TAILLE_CASE = 50
MARGE = 50
TAILLE_GRILLE = 10

# Fonction pour dessiner la grille
def dessiner_grille(surface, grille, x_offset, y_offset):
    for x in range(TAILLE_GRILLE):
        for y in range(TAILLE_GRILLE):
            couleur_case = BLANC
            if grille[x][y] == "X":
                couleur_case = BLEU
            pygame.draw.rect(surface, couleur_case, (x_offset + x * TAILLE_CASE, y_offset + y * TAILLE_CASE, TAILLE_CASE, TAILLE_CASE))
            pygame.draw.rect(surface, NOIR, (x_offset + x * TAILLE_CASE, y_offset + y * TAILLE_CASE, TAILLE_CASE, TAILLE_CASE), 1)

# Fonction pour dessiner les bateaux
def dessiner_bateaux(surface, bateaux, x_offset, y_offset):
    for bateau in bateaux:
        nom_bateau = bateau.nom
        taille_bateau = bateau.taille
        # Dessiner un rectangle pour représenter le bateau
        pygame.draw.rect(surface, NOIR, (x_offset + bateau.positions[0][0] * TAILLE_CASE, y_offset + bateau.positions[0][1] * TAILLE_CASE, TAILLE_CASE * taille_bateau, TAILLE_CASE))
        # Afficher le nom du bateau
        font = pygame.font.Font(None, 24)
        text = font.render(nom_bateau, True, NOIR)
        surface.blit(text, (x_offset + bateau.positions[0][0] * TAILLE_CASE, y_offset + bateau.positions[0][1] * TAILLE_CASE - 25))

# Fonction principale du jeu
def jouer_jeu():
    # Création de la fenêtre
    fenetre = pygame.display.set_mode((LARGEUR_FENETRE, HAUTEUR_FENETRE))
    pygame.display.set_caption("Bataille Navale")

    # Création des grilles
    grille_joueur = Grille()
    grille_ia = Grille()

    # Placement des bateaux
    jeu = Jeu()
    jeu.placer_bateaux_aleatoire(grille_joueur)
    jeu.placer_bateaux_aleatoire(grille_ia)

    # Boucle principale
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Effacer l'écran
        fenetre.fill(BLANC)

        # Dessiner les grilles
        dessiner_grille(fenetre, grille_joueur.grille, MARGE, MARGE)
        dessiner_grille(fenetre, grille_ia.grille, LARGEUR_FENETRE - MARGE - TAILLE_CASE * TAILLE_GRILLE, MARGE)

        # Dessiner les bateaux
        dessiner_bateaux(fenetre, grille_joueur.bateaux, MARGE, MARGE)
        dessiner_bateaux(fenetre, grille_ia.bateaux, LARGEUR_FENETRE - MARGE - TAILLE_CASE * TAILLE_GRILLE, MARGE)

        # Mettre à jour l'affichage
        pygame.display.flip()

# Lancer le jeu
if __name__ == "__main__":
    jouer_jeu()
