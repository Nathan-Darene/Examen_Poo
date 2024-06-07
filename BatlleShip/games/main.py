import pygame
import sys
import random
from Grille import*

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




# Classe principale du jeu
class main:
    def __init__(self):
        self.ecran = pygame.display.set_mode((LARGEUR_ECRAN, HAUTEUR_ECRAN))
        pygame.display.set_caption("Bataille Navale")
        self.horloge = pygame.time.Clock()
        self.grille1 = Grille(100, 100)
        self.grille2 = Grille(1080, 100)  # Ajusté pour être à droite de la première grille
        self.selectionne_joueur1 = None
        self.selectionne_joueur2 = None
        self.joueur_actif = 1  # Commence par le joueur 1

    def executer_jeu(self):
        en_cours = True
        en_placement = True

        while en_cours:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    en_cours = False
                elif event.type == pygame.MOUSEBUTTONDOWN and en_placement:
                    pos = pygame.mouse.get_pos()
                    if self.joueur_actif == 1:
                        index, type_navire = self.grille1.obtenir_navire_sous_souris(pos)
                        if index is not None:
                            self.selectionne_joueur1 = index
                    elif self.joueur_actif == 2:
                        index, type_navire = self.grille2.obtenir_navire_sous_souris(pos)
                        if index is not None:
                            self.selectionne_joueur2 = index
                elif event.type == pygame.MOUSEBUTTONUP and en_placement:
                    if self.joueur_actif == 1:
                        self.selectionne_joueur1 = None
                    elif self.joueur_actif == 2:
                        self.selectionne_joueur2 = None
                elif event.type == pygame.MOUSEMOTION and en_placement:
                    pos = pygame.mouse.get_pos()
                    nouvelle_colonne = (pos[0] - MARGE) // (TAILLE_CELLULE + MARGE)
                    nouvelle_ligne = (pos[1] - MARGE) // (TAILLE_CELLULE + MARGE)
                    if self.joueur_actif == 1 and self.selectionne_joueur1 is not None:
                        self.grille1.deplacer_navire(self.selectionne_joueur1, nouvelle_ligne, nouvelle_colonne)
                    elif self.joueur_actif == 2 and self.selectionne_joueur2 is not None:
                        self.grille2.deplacer_navire(self.selectionne_joueur2, nouvelle_ligne, nouvelle_colonne)

            self.ecran.fill(GRIS)
            self.grille1.dessiner(self.ecran)
            self.grille2.dessiner(self.ecran)
            pygame.display.flip()
            self.horloge.tick(60)

        pygame.quit()
        sys.exit()