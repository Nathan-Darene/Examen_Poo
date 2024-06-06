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
        # Chargez les images des navires
        self.porte_avions_image = pygame.image.load("BatlleShip/assets/images/porte_avions.png")
        self.sous_marin_image = pygame.image.load("BatlleShip/assets/images/sous_marin.png")
        self.torpilleur_image = pygame.image.load("BatlleShip/assets/images/torpilleur.png")
        self.croiseur_image = pygame.image.load("BatlleShip/assets/images/croiseur.png")
        self.contre_torpilleur_image = pygame.image.load("BatlleShip/assets/images/contre_torpilleur.png")

    def dessiner(self, screen):
        # Dessinez les images des navires
        for ligne in range(TAILLE_GRILLE):
            for colonne in range(TAILLE_GRILLE):
                if self.grille[ligne][colonne] == 1:  # Si la case contient un navire
                    # Dessinez l'image correspondant au type de navire
                    if colonne + 4 < TAILLE_GRILLE and self.grille[ligne][colonne:colonne + 5] == [1] * 5:
                        image_navire = self.porte_avions_image
                    elif colonne + 3 < TAILLE_GRILLE and self.grille[ligne][colonne:colonne + 4] == [1] * 4:
                        image_navire = self.croiseur_image
                    elif colonne + 2 < TAILLE_GRILLE and self.grille[ligne][colonne:colonne + 3] == [1] * 3:
                        image_navire = self.contre_torpilleur_image
                    elif colonne + 1 < TAILLE_GRILLE and self.grille[ligne][colonne:colonne + 2] == [1] * 2:
                        image_navire = self.torpilleur_image
                    else:
                        image_navire = self.sous_marin_image
                    # Dessinez l'image sur la case de la grille
                    screen.blit(image_navire, ((MARGE + TAILLE_CELLULE) * colonne + MARGE + self.decalage_x,
                                               (MARGE + TAILLE_CELLULE) * ligne + MARGE + self.decalage_y))


class JeuBatailleNavale:
    def __init__(self):
        self.ecran = pygame.display.set_mode((LARGEUR_ECRAN, HAUTEUR_ECRAN))
        pygame.display.set_caption("Bataille Navale")
        self.horloge = pygame.time.Clock()
        self.grille_joueur1 = Grille(100, 100)
        self.grille_adversaire = Grille(1080, 100)  # Ajusté pour être à droite de la grille du joueur 1

    def executer_jeu(self):
        en_cours = True
        while en_cours:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    en_cours = False
            
            self.ecran.fill(GRIS)
            self.grille_joueur1.dessiner(self.ecran)
            self.grille_adversaire.dessiner(self.ecran)
            pygame.display.flip()
            self.horloge.tick(60)
        
        pygame.quit()
        sys.exit()

# Placer des bateaux de manière fixe pour le test
def configurer_jeu():
    jeu = JeuBatailleNavale()
    # Placer les bateaux sur la grille du joueur 1
    # Remplacez ces valeurs par le placement aléatoire des bateaux selon vos règles
    jeu.grille_joueur1.grille[2][1] = 1  # Exemple de placement de bateau
    jeu.grille_joueur1.grille[2][2] = 1
    jeu.grille_joueur1.grille[2][3] = 1
    jeu.grille_joueur1.grille[2][4] = 1
    jeu.grille_joueur1.grille[2][5] = 1
    # Placer les bateaux sur la grille de l'adversaire
    # Remplacez ces valeurs par le placement aléatoire des bateaux selon vos règles
    jeu.grille_adversaire.grille[0][0] = 1  # Exemple de placement de bateau
    jeu.grille_adversaire.grille[0][1] = 1
    jeu.grille_adversaire.grille[0][2] = 1
    jeu.grille_adversaire.grille[0][3] = 1
    jeu.grille_adversaire.grille[0][4] = 1

    jeu.executer_jeu()

if __name__ == "__main__":
    configurer_jeu()
