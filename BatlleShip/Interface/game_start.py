import pygame
import sys

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


from game_start import *
from game_final import *
from Grille import *


# Classe principale du jeu
class game_start:
    def __init__(self):
        self.ecran = pygame.display.set_mode((LARGEUR_ECRAN, HAUTEUR_ECRAN))
        pygame.display.set_caption("Bataille Navale")
        self.horloge = pygame.time.Clock()
        self.grille1 = Grille(100, 100)
        self.grille2 = Grille(1080, 100)
        self.selectionne_joueur1 = None
        self.selectionne_joueur2 = None
        self.joueur_actif = 1
        self.joueur1_pret = False  # Indique si le joueur 1 est prêt

        # Dimensions du bouton "Prêt"
        self.bouton_pret = pygame.Rect(280, 650, 150, 50)  # Position et taille du bouton

    def executer_jeu(self):
        en_cours = True
        en_placement = True

        while en_cours:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    en_cours = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if self.bouton_pret.collidepoint(pos):
                        self.joueur1_pret = True  # Le joueur 1 est prêt
                        en_placement = False  # Terminer la phase de placement pour le joueur 1
                    elif en_placement and not self.joueur1_pret:
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
                elif event.type == pygame.MOUSEMOTION and en_placement and not self.joueur1_pret:
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

            # Dessiner le bouton "Prêt"
            if not self.joueur1_pret:
                pygame.draw.rect(self.ecran, VERT, self.bouton_pret)
                font = pygame.font.SysFont("sans-serif", 36)
                texte_pret = font.render("Prêt", True, NOIR)
                self.ecran.blit(texte_pret, (self.bouton_pret.x + 50, self.bouton_pret.y + 10))

            pygame.display.flip()
            self.horloge.tick(60)

        pygame.quit()
        sys.exit()