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
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
BLEU = (0, 0, 255)
ROUGE = (255, 0, 0)

contre_torpilleur_image = pygame.image.load("BatlleShip/assets/images/contre_torpilleur.png")
porte_avions_image = pygame.image.load("BatlleShip/assets/images/porte_avions.png")
croiseur_image = pygame.image.load("BatlleShip/assets/images/croiseur.png")
torpilleur_image = pygame.image.load("BatlleShip/assets/images/torpilleur.png")
sous_marin = pygame.image.load("BatlleShip/assets/images/sous_marin.png")



# Classe pour représenter la grille
class Grille:
    def __init__(self, decalage_x, decalage_y):
        self.grille = [[0 for _ in range(TAILLE_GRILLE)] for _ in range(TAILLE_GRILLE)]
        self.decalage_x = decalage_x
        self.decalage_y = decalage_y


    #La méthode dessiner_lignes est responsable du dessin des lignes noires qui délimitent les cellules de chaque  grilles.

    def dessiner_lignes(self, screen):
        for ligne in range(TAILLE_GRILLE + 1):
            pygame.draw.line(screen, NOIR, (self.decalage_x + MARGE, self.decalage_y + MARGE + ligne * (TAILLE_CELLULE + MARGE)),
                            (self.decalage_x + MARGE + TAILLE_GRILLE * (TAILLE_CELLULE + MARGE), self.decalage_y + MARGE + ligne * (TAILLE_CELLULE + MARGE)), 2)
            
        for colonne in range(TAILLE_GRILLE + 1):
            pygame.draw.line(screen, NOIR, (self.decalage_x + MARGE + colonne * (TAILLE_CELLULE + MARGE), self.decalage_y + MARGE),
                            (self.decalage_x + MARGE + colonne * (TAILLE_CELLULE + MARGE), self.decalage_y + MARGE + TAILLE_GRILLE * (TAILLE_CELLULE + MARGE)), 2)

    def dessiner(self, screen):
        font = pygame.font.SysFont(None, 36)
        # Dessiner les cellules
        for ligne in range(TAILLE_GRILLE):
            for colonne in range(TAILLE_GRILLE):
                couleur = BLANC if self.grille[ligne][colonne] == 0 else BLEU
                pygame.draw.rect(screen,
                                couleur,
                                [(MARGE + TAILLE_CELLULE) * colonne + MARGE + self.decalage_x,
                                (MARGE + TAILLE_CELLULE) * ligne + MARGE + self.decalage_y,
                                TAILLE_CELLULE,
                                TAILLE_CELLULE], 1)
        
        # Dessiner les lignes de la grille
        self.dessiner_lignes(screen)

        # Dessiner les étiquettes
        for i in range(TAILLE_GRILLE):
            etiquette = font.render(str(i+1), True, NOIR)
            screen.blit(etiquette, (self.decalage_x - MARGE, (MARGE + TAILLE_CELLULE) * i + MARGE + self.decalage_y + TAILLE_CELLULE//3))
            etiquette = font.render(chr(65+i), True, NOIR)
            screen.blit(etiquette, ((MARGE + TAILLE_CELLULE) * i + MARGE + self.decalage_x + TAILLE_CELLULE//3, self.decalage_y - MARGE))


    def placer_bateau(self, ligne_depart, colonne_depart, taille, orientation, joueur1=False):
        if joueur1:  # Vérifier si c'est la grille du joueur 1
            for i in range(taille):
                if orientation == 'H':
                    self.grille[ligne_depart][colonne_depart + i] = 0  # Effacer le bateau
                elif orientation == 'V':
                    self.grille[ligne_depart + i][colonne_depart] = 0  # Effacer le bateau
        else:  # Placer le bateau normalement
            if orientation == 'H':
                for i in range(taille):
                    self.grille[ligne_depart][colonne_depart + i] = 1
            elif orientation == 'V':
                for i in range(taille):
                    self.grille[ligne_depart + i][colonne_depart] = 1

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
            
            self.ecran.fill(BLANC)
            self.grille1.dessiner(self.ecran)
            self.grille2.dessiner(self.ecran)
            pygame.display.flip()
            self.horloge.tick(60)
        
        pygame.quit()
        sys.exit()

# Placer des bateaux de manière fixe pour le test
def configurer_jeu():
    jeu = JeuBatailleNavale()
    jeu.grille1.placer_bateau(2, 1, 5, 'H', joueur1=True)  # Exemple de placement de bateaux
    jeu.grille1.placer_bateau(2, 1, 3, 'H', joueur1=True)
    jeu.grille1.placer_bateau(4, 2, 3, 'H', joueur1=True)
    jeu.grille1.placer_bateau(6, 1, 2, 'H', joueur1=True)
    jeu.grille1.placer_bateau(8, 1, 2, 'H', joueur1=True)

    jeu.executer_jeu()

if __name__ == "__main__":
    configurer_jeu()
