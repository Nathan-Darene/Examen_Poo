import pygame
import sys

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

# Classe pour représenter la grille
class Grille:
    def __init__(self, decalage_x, decalage_y):
        self.grille = [[0 for _ in range(TAILLE_GRILLE)] for _ in range(TAILLE_GRILLE)]
        self.decalage_x = decalage_x
        self.decalage_y = decalage_y
        # Chargement des images des Navires
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
        self.navires = []  # Stocke les informations sur les navires placés

    def dessiner_lignes(self, screen):
        for ligne in range(TAILLE_GRILLE + 1):
            pygame.draw.line(screen, NOIR, (self.decalage_x + MARGE, self.decalage_y + MARGE + ligne * (TAILLE_CELLULE + MARGE)),
                             (self.decalage_x + MARGE + TAILLE_GRILLE * (TAILLE_CELLULE + MARGE), self.decalage_y + MARGE + ligne * (TAILLE_CELLULE + MARGE)), 2)
        for colonne in range(TAILLE_GRILLE + 1):
            pygame.draw.line(screen, NOIR, (self.decalage_x + MARGE + colonne * (TAILLE_CELLULE + MARGE), self.decalage_y + MARGE),
                             (self.decalage_x + MARGE + colonne * (TAILLE_CELLULE + MARGE), self.decalage_y + MARGE + TAILLE_GRILLE * (TAILLE_CELLULE + MARGE)), 2)

    def placer_bateau(self, ligne_depart, colonne_depart, type_navire, orientation='H', joueur1=False):
        taille = self.taille_navires[type_navire]
        if orientation == 'H':
            if colonne_depart + taille <= TAILLE_GRILLE:
                for i in range(taille):
                    self.grille[ligne_depart][colonne_depart + i] = 1
                self.navires.append((ligne_depart, colonne_depart, type_navire, orientation))
        elif orientation == 'V':
            if ligne_depart + taille <= TAILLE_GRILLE:
                for i in range(taille):
                    self.grille[ligne_depart + i][colonne_depart] = 1
                self.navires.append((ligne_depart, colonne_depart, type_navire, orientation))

    def dessiner(self, screen, joueur1=False):
        font = pygame.font.SysFont("sans-serif", 36)

        for ligne in range(TAILLE_GRILLE):
            for colonne in range(TAILLE_GRILLE):
                rect = [(MARGE + TAILLE_CELLULE) * colonne + MARGE + self.decalage_x,
                        (MARGE + TAILLE_CELLULE) * ligne + MARGE + self.decalage_y,
                        TAILLE_CELLULE,
                        TAILLE_CELLULE]
                pygame.draw.rect(screen, BLANC, rect, 1)

        # Dessiner les lignes de la grille
        self.dessiner_lignes(screen)

        # Dessiner les étiquettes
        for i in range(TAILLE_GRILLE):
            etiquette = font.render(str(i+1), True, NOIR)
            screen.blit(etiquette, (self.decalage_x - MARGE, (MARGE + TAILLE_CELLULE) * i + MARGE + self.decalage_y + TAILLE_CELLULE // 3))
            etiquette = font.render(chr(65 + i), True, NOIR)
            screen.blit(etiquette, ((MARGE + TAILLE_CELLULE) * i + MARGE + self.decalage_x + TAILLE_CELLULE // 3, self.decalage_y - MARGE))

        # Dessiner les images des navires
        for navire in self.navires:
            ligne, colonne, type_navire, orientation = navire
            image_navire = self.images_navires[type_navire]
            taille = self.taille_navires[type_navire]

            if orientation == 'H':
                image_navire = pygame.transform.scale(image_navire, (TAILLE_CELLULE * taille + MARGE * (taille - 1), TAILLE_CELLULE))
                screen.blit(image_navire, ((MARGE + TAILLE_CELLULE) * colonne + MARGE + self.decalage_x,
                                           (MARGE + TAILLE_CELLULE) * ligne + MARGE + self.decalage_y))
            elif orientation == 'V':
                image_navire = pygame.transform.scale(image_navire, (TAILLE_CELLULE, TAILLE_CELLULE * taille + MARGE * (taille - 1)))
                screen.blit(image_navire, ((MARGE + TAILLE_CELLULE) * colonne + MARGE + self.decalage_x,
                                           (MARGE + TAILLE_CELLULE) * ligne + MARGE + self.decalage_y))

# Classe principale du jeu
class JeuBatailleNavale:
    def __init__(self):
        self.ecran = pygame.display.set_mode((LARGEUR_ECRAN, HAUTEUR_ECRAN))
        pygame.display.set_caption("Bataille Navale")
        self.horloge = pygame.time.Clock()
        self.grille1 = Grille(100, 100)
        self.grille2 = Grille(1080, 100)  # Ajusté pour être à droite de la première grille

    def executer_jeu(self):
        en_cours = True
        while en_cours:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    en_cours = False

            self.ecran.fill(GRIS)
            self.grille1.dessiner(self.ecran, joueur1=True)
            self.grille2.dessiner(self.ecran)
            pygame.display.flip()
            self.horloge.tick(60)

        pygame.quit()
        sys.exit()

# Placer des bateaux de manière fixe pour le test
def configurer_jeu():
    jeu = JeuBatailleNavale()
    # Exemple de placement de bateaux
    jeu.grille1.placer_bateau(2, 1, "porte_avions", 'V', joueur1=True)
    jeu.grille1.placer_bateau(4, 1, "croiseur", 'V', joueur1=True)
    jeu.grille1.placer_bateau(6, 1, "contre_torpilleur", 'V', joueur1=True)
    jeu.grille1.placer_bateau(8, 1, "sous_marin", 'V', joueur1=True)
    jeu.grille1.placer_bateau(9, 1, "torpilleur", 'V', joueur1=True)  # Correction ici pour éviter l'index hors limite

    jeu.executer_jeu()

if __name__ == "__main__":
    configurer_jeu()
