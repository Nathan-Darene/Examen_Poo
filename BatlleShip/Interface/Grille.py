import pygame
import random

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

from Grille import *
from game_final import *

# Classe pour représenter la grille
class Grille:
    def __init__(self, decalage_x, decalage_y):
        self.grille = [[0 for _ in range(TAILLE_GRILLE)] for _ in range(TAILLE_GRILLE)]
        self.decalage_x = decalage_x
        self.decalage_y = decalage_y
        
        self.images_navires = {
            "contre_torpilleur": pygame.image.load("BatlleShip/assets/images/contre_torpilleur.png"),
            "porte_avions": pygame.image.load("BatlleShip/assets/images/porte_avions.png"),
            "sous_marin": pygame.image.load("BatlleShip/assets/images/sous_marin.png"),
            "torpilleur": pygame.image.load("BatlleShip/assets/images/torpilleur.png"),
            "croiseur": pygame.image.load("BatlleShip/assets/images/croiseur.png")
        }
        
        self.taille_navires = {
            "porte_avions": 5,
            "croiseur": 4,
            "contre_torpilleur": 3,
            "sous_marin": 3,
            "torpilleur": 2
        }
        
        self.navires = []

    def dessiner_lignes(self, screen):
        for ligne in range(TAILLE_GRILLE + 1):
            pygame.draw.line(screen, NOIR,
                             (self.decalage_x + ESPACE_ETIQUETTES, self.decalage_y + ESPACE_ETIQUETTES + ligne * (TAILLE_CELLULE + MARGE)),
                             (self.decalage_x + ESPACE_ETIQUETTES + TAILLE_GRILLE * (TAILLE_CELLULE + MARGE), self.decalage_y + ESPACE_ETIQUETTES + ligne * (TAILLE_CELLULE + MARGE)), 2)
        for colonne in range(TAILLE_GRILLE + 1):
            pygame.draw.line(screen, NOIR,
                             (self.decalage_x + ESPACE_ETIQUETTES + colonne * (TAILLE_CELLULE + MARGE), self.decalage_y + ESPACE_ETIQUETTES),
                             (self.decalage_x + ESPACE_ETIQUETTES + colonne * (TAILLE_CELLULE + MARGE), self.decalage_y + ESPACE_ETIQUETTES + TAILLE_GRILLE * (TAILLE_CELLULE + MARGE)), 2)

    def placer_bateau(self, ligne_depart, colonne_depart, type_navire, orientation='H'):
        taille = self.taille_navires[type_navire]
        if orientation == 'H':
            if colonne_depart + taille <= TAILLE_GRILLE:
                for i in range(1,taille):
                    self.grille[ligne_depart][colonne_depart + i] = 1
                self.navires.append((ligne_depart, colonne_depart, type_navire, orientation))
        elif orientation == 'V':
            if ligne_depart + taille <= TAILLE_GRILLE:
                for i in range(taille):
                    self.grille[ligne_depart + i][colonne_depart] = 1
                self.navires.append((ligne_depart, colonne_depart, type_navire, orientation))

    def placer_bateaux_aleatoires(self):
        for type_navire, taille in self.taille_navires.items():
            place = False
            while not place:
                orientation = random.choice(['H', 'V'])
                if orientation == 'H':
                    ligne_depart = random.randint(0, TAILLE_GRILLE - 1)
                    colonne_depart = random.randint(0, TAILLE_GRILLE - taille)
                else:
                    ligne_depart = random.randint(0, TAILLE_GRILLE - taille)
                    colonne_depart = random.randint(0, TAILLE_GRILLE - 1)

                if self.peut_placer_bateau(ligne_depart, colonne_depart, taille, orientation):
                    self.placer_bateau(ligne_depart, colonne_depart, type_navire, orientation)
                    place = True

    def peut_placer_bateau(self, ligne, colonne, taille, orientation):
        if orientation == 'H':
            if colonne + taille > TAILLE_GRILLE:
                return False
            for i in range(taille):
                if self.grille[ligne][colonne + i] != 0:
                    return False
        elif orientation == 'V':
            if ligne + taille > TAILLE_GRILLE:
                return False
            for i in range(taille):
                if self.grille[ligne + i][colonne] != 0:
                    return False
        return True

    def dessiner(self, screen):
        font = pygame.font.SysFont("sans-serif", 36)

        for ligne in range(TAILLE_GRILLE):
            for colonne in range(TAILLE_GRILLE):
                rect = [(MARGE + TAILLE_CELLULE) * colonne + MARGE + self.decalage_x + ESPACE_ETIQUETTES,
                        (MARGE + TAILLE_CELLULE) * ligne + MARGE + self.decalage_y + ESPACE_ETIQUETTES,
                        TAILLE_CELLULE,
                        TAILLE_CELLULE]
                pygame.draw.rect(screen, BLANC, rect, 1)

        self.dessiner_lignes(screen)

        for i in range(TAILLE_GRILLE):
            etiquette = font.render(str(i + 1), True, NOIR)
            screen.blit(etiquette, (self.decalage_x + ESPACE_ETIQUETTES - MARGE - 30, 
                                    (MARGE + TAILLE_CELLULE) * i + MARGE + self.decalage_y + ESPACE_ETIQUETTES + TAILLE_CELLULE // 3))
            etiquette = font.render(chr(65 + i), True, NOIR)
            screen.blit(etiquette, ((MARGE + TAILLE_CELLULE) * i + MARGE + self.decalage_x + ESPACE_ETIQUETTES + TAILLE_CELLULE // 3, 
                                    self.decalage_y + ESPACE_ETIQUETTES - MARGE - 30))

        for navire in self.navires:
            ligne, colonne, type_navire, orientation = navire
            image_navire = self.images_navires[type_navire]
            taille = self.taille_navires[type_navire]

            if orientation == 'H':
                image_navire = pygame.transform.rotate(image_navire, 90)
                image_navire = pygame.transform.scale(image_navire, (TAILLE_CELLULE * taille + MARGE * (taille - 1), TAILLE_CELLULE))
                screen.blit(image_navire, ((MARGE + TAILLE_CELLULE) * colonne + MARGE + self.decalage_x + ESPACE_ETIQUETTES,
                                           (MARGE + TAILLE_CELLULE) * ligne + MARGE + self.decalage_y + ESPACE_ETIQUETTES))
            elif orientation == 'V':
                image_navire = pygame.transform.scale(image_navire, (TAILLE_CELLULE, TAILLE_CELLULE * taille + MARGE * (taille - 1)))
                screen.blit(image_navire, ((MARGE + TAILLE_CELLULE) * colonne + MARGE + self.decalage_x + ESPACE_ETIQUETTES,
                                           (MARGE + TAILLE_CELLULE) * ligne + MARGE + self.decalage_y + ESPACE_ETIQUETTES))

    def obtenir_navire_sous_souris(self, pos):
        for i, (ligne, colonne, type_navire, orientation) in enumerate(self.navires):
            taille = self.taille_navires[type_navire]
            x = self.decalage_x + MARGE + (MARGE + TAILLE_CELLULE) * colonne + ESPACE_ETIQUETTES
            y = self.decalage_y + MARGE + (MARGE + TAILLE_CELLULE) * ligne + ESPACE_ETIQUETTES

            if orientation == 'H':
                rect = pygame.Rect(x, y, TAILLE_CELLULE * taille + MARGE * (taille - 1), TAILLE_CELLULE)
            elif orientation == 'V':
                rect = pygame.Rect(x, y, TAILLE_CELLULE, TAILLE_CELLULE * taille + MARGE * (taille - 1))

            if rect.collidepoint(pos):
                return i, type_navire
        return None, None

    def deplacer_navire(self, index, nouvelle_ligne, nouvelle_colonne):
        if 0 <= nouvelle_ligne < TAILLE_GRILLE and 0 <= nouvelle_colonne < TAILLE_GRILLE:
            ligne, colonne, type_navire, orientation = self.navires[index]
            taille = self.taille_navires[type_navire]

            if orientation == 'H' and nouvelle_colonne + taille > TAILLE_GRILLE:
                return
            if orientation == 'V' and nouvelle_ligne + taille > TAILLE_GRILLE:
                return

            for i in range(taille):
                if orientation == 'H' and self.grille[nouvelle_ligne][nouvelle_colonne + i] != 0:
                    return
                if orientation == 'V' and self.grille[nouvelle_ligne + i][nouvelle_colonne] != 0:
                    return

            if orientation == 'H':
                for i in range(taille):
                    self.grille[ligne][colonne + i] = 0
            elif orientation == 'V':
                for i in range(taille):
                    self.grille[ligne + i][colonne] = 0

            self.navires[index] = (nouvelle_ligne, nouvelle_colonne, type_navire, orientation)
            if orientation == 'H':
                for i in range(taille):
                    self.grille[nouvelle_ligne][nouvelle_colonne + i] = 1
            elif orientation == 'V':
                for i in range(taille):
                    self.grille[nouvelle_ligne + i][nouvelle_colonne] = 1
