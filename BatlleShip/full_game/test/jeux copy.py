import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Constantes de la fenêtre
LARGEUR_ECRAN = 800
HAUTEUR_ECRAN = 600
TAILLE_GRILLE = 10
TAILLE_CELLULE = 30  # Ajusté pour rendre les cellules plus petites
MARGE = 10  # Ajusté pour rendre les marges plus petites

# Couleurs
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

    def dessiner(self, screen):
        font = pygame.font.SysFont(None, 18)
        for ligne in range(TAILLE_GRILLE):
            for colonne in range(TAILLE_GRILLE):
                couleur = BLANC if self.grille[ligne][colonne] == 0 else BLEU
                pygame.draw.rect(screen,
                                 couleur,
                                 [(MARGE + TAILLE_CELLULE) * colonne + MARGE + self.decalage_x,
                                  (MARGE + TAILLE_CELLULE) * ligne + MARGE + self.decalage_y,
                                  TAILLE_CELLULE,
                                  TAILLE_CELLULE], 1)
        
        # Dessiner les étiquettes
        for i in range(TAILLE_GRILLE):
            etiquette = font.render(str(i+1), True, NOIR)
            screen.blit(etiquette, (self.decalage_x - MARGE, (MARGE + TAILLE_CELLULE) * i + MARGE + self.decalage_y + TAILLE_CELLULE//3))
            etiquette = font.render(chr(65+i), True, NOIR)
            screen.blit(etiquette, ((MARGE + TAILLE_CELLULE) * i + MARGE + self.decalage_x + TAILLE_CELLULE//3, self.decalage_y - MARGE))

    def placer_bateau(self, ligne_depart, colonne_depart, taille, orientation):
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
        self.grille1 = Grille(50, 50)
        self.grille2 = Grille(450, 50)  # Ajusté pour être à droite de la première grille

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
    jeu.grille1.placer_bateau(0, 1, 5, 'H')  # Exemple de placement de bateaux
    jeu.grille1.placer_bateau(2, 1, 3, 'H')
    jeu.grille1.placer_bateau(4, 2, 3, 'H')
    jeu.grille1.placer_bateau(6, 1, 2, 'H')
    jeu.grille1.placer_bateau(8, 1, 2, 'H')

    jeu.executer_jeu()

if __name__ == "__main__":
    configurer_jeu()
