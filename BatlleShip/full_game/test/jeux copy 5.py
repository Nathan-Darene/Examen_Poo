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
BLEU = (0, 0, 255)
ROUGE = (255, 0, 0)

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

    def dessiner_lignes(self, screen):
        for ligne in range(TAILLE_GRILLE + 1):
            pygame.draw.line(screen, NOIR, (self.decalage_x + MARGE, self.decalage_y + MARGE + ligne * (TAILLE_CELLULE + MARGE)),
                            (self.decalage_x + MARGE + TAILLE_GRILLE * (TAILLE_CELLULE + MARGE), self.decalage_y + MARGE + ligne * (TAILLE_CELLULE + MARGE)), 2)
        for colonne in range(TAILLE_GRILLE + 1):
            pygame.draw.line(screen, NOIR, (self.decalage_x + MARGE + colonne * (TAILLE_CELLULE + MARGE), self.decalage_y + MARGE),
                            (self.decalage_x + MARGE + colonne * (TAILLE_CELLULE + MARGE), self.decalage_y + MARGE + TAILLE_GRILLE * (TAILLE_CELLULE + MARGE)), 2)

    def placer_bateau(self, ligne_depart, colonne_depart, taille, orientation, type_navire, joueur1=False):
        if orientation == 'H':
            for i in range(taille):
                self.grille[ligne_depart][colonne_depart + i] = 1
        elif orientation == 'V':
            for i in range(taille):
                self.grille[ligne_depart + i][colonne_depart] = 1

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
            screen.blit(etiquette, (self.decalage_x - MARGE, (MARGE + TAILLE_CELLULE) * i + MARGE + self.decalage_y + TAILLE_CELLULE//3))
            etiquette = font.render(chr(65+i), True, NOIR)
            screen.blit(etiquette, ((MARGE + TAILLE_CELLULE) * i + MARGE + self.decalage_x + TAILLE_CELLULE//3, self.decalage_y - MARGE))
        
        # Dessiner les images des navires
        for ligne in range(TAILLE_GRILLE):
            for colonne in range(TAILLE_GRILLE):
                if self.grille[ligne][colonne] == 1 and joueur1:
                    navire_image = self.images_navires["porte_avions"]  # Exemple : utilisez la bonne image ici
                    screen.blit(navire_image, rect[:6])

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
    jeu.grille1.placer_bateau(3, 1, 5, 'V', "porte_avions", joueur1=True)
    jeu.grille1.placer_bateau(4, 1, 4, 'H', "croiseur", joueur1=True)
    jeu.grille1.placer_bateau(6, 1, 3, 'H', "contre_torpilleur", joueur1=True)
    jeu.grille1.placer_bateau(8, 1, 3, 'H', "sous_marin", joueur1=True)
    jeu.grille1.placer_bateau(9, 1, 2, 'H', "torpilleur", joueur1=True)  # Correction ici pour éviter l'index hors limite

    jeu.executer_jeu()

if __name__ == "__main__":
    configurer_jeu()
