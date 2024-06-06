import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Constantes de la fenêtre
LARGEUR_ECRAN = 1920
HAUTEUR_ECRAN = 1080
TAILLE_GRILLE = 10
TAILLE_CELLULE = 40  # Ajusté pour utiliser l'espace disponible
MARGE = 15

# Couleurs
GRIS = (199, 199, 199)
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
BLEU = (0, 0, 255)
ROUGE = (255, 0, 0)

# Liste de lettres pour les colonnes
LETTRES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

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
        for ligne in range(TAILLE_GRILLE):
            for colonne in range(TAILLE_GRILLE):
                # Dessinez les images des navires aux positions correspondantes dans la grille
                if self.grille[ligne][colonne] == 1:  
                    screen.blit(self.porte_avions_image, (self.decalage_x + colonne * (TAILLE_CELLULE + MARGE),
                                                          self.decalage_y + ligne * (TAILLE_CELLULE + MARGE)))
                if self.grille[ligne][colonne] == 2:
                    screen.blit(self.sous_marin_image, (self.decalage_x + colonne * (TAILLE_CELLULE + MARGE),
                                                          self.decalage_y + ligne * (TAILLE_CELLULE + MARGE)))
                if self.grille[ligne][colonne] == 3:
                    screen.blit(self.torpilleur_image, (self.decalage_x + colonne * (TAILLE_CELLULE + MARGE),
                                                          self.decalage_y + ligne * (TAILLE_CELLULE + MARGE)))
                if self.grille[ligne][colonne] == 4:
                    screen.blit(self.croiseur_image, (self.decalage_x + colonne * (TAILLE_CELLULE + MARGE),
                                                          self.decalage_y + ligne * (TAILLE_CELLULE + MARGE)))
                if self.grille[ligne][colonne] == 5:
                    screen.blit(self.contre_torpilleur_image, (self.decalage_x + colonne * (TAILLE_CELLULE + MARGE),
                                                          self.decalage_y + ligne * (TAILLE_CELLULE + MARGE)))
        self.dessiner_lignes(screen)  # Appelez la méthode pour dessiner les lignes de la grille
        self.dessiner_indications(screen)  # Dessiner les indications de colonnes et de lignes

    def dessiner_lignes(self, screen):
        for ligne in range(TAILLE_GRILLE + 1):
            pygame.draw.line(screen, NOIR, (self.decalage_x + MARGE, self.decalage_y + MARGE + ligne * (TAILLE_CELLULE + MARGE)),
                             (self.decalage_x + MARGE + TAILLE_GRILLE * (TAILLE_CELLULE + MARGE), self.decalage_y + MARGE + ligne * (TAILLE_CELLULE + MARGE)), 2)
        for colonne in range(TAILLE_GRILLE + 1):
            pygame.draw.line(screen, NOIR, (self.decalage_x + MARGE + colonne * (TAILLE_CELLULE + MARGE), self.decalage_y + MARGE),
                             (self.decalage_x + MARGE + colonne * (TAILLE_CELLULE + MARGE), self.decalage_y + MARGE + TAILLE_GRILLE * (TAILLE_CELLULE + MARGE)), 2)

    def dessiner_indications(self, screen):
        font = pygame.font.Font(None, 36)
        for i in range(TAILLE_GRILLE):
            # Dessiner les lettres (colonnes)
            text = font.render(LETTRES[i], True, NOIR)
            text_rect = text.get_rect(center=(self.decalage_x + MARGE + (i + 1) * (TAILLE_CELLULE + MARGE), self.decalage_y + MARGE // 2))
            screen.blit(text, text_rect)
            # Dessiner les chiffres (lignes)
            text = font.render(str(i + 1), True, NOIR)
            text_rect = text.get_rect(center=(self.decalage_x + MARGE // 2, self.decalage_y + MARGE + (i + 1) * (TAILLE_CELLULE + MARGE)))
            screen.blit(text, text_rect)

class JeuBatailleNavale:
    def __init__(self):
        self.ecran = pygame.display.set_mode((LARGEUR_ECRAN, HAUTEUR_ECRAN))
        pygame.display.set_caption("Bataille Navale")
        self.horloge = pygame.time.Clock()
        self.grille_joueur1 = Grille(100, 100)
        self.grille_adversaire = Grille(1080, 100)  

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
    jeu.grille_joueur1.grille[2][2] = 2
    jeu.grille_joueur1.grille[2][3] = 3
    jeu.grille_joueur1.grille[2][4] = 4
    jeu.grille_joueur1.grille[2][5] = 5
    # Placer les bateaux sur la grille de l'adversaire
    # Remplacez ces valeurs par le placement aléatoire des bateaux selon vos règles
    jeu.grille_adversaire.grille[0][0] = 1  # Exemple de placement de bateau
    jeu.grille_adversaire.grille[0][1] = 2
    jeu.grille_adversaire.grille[0][2] = 3
    jeu.grille_adversaire.grille[0][3] = 4
    jeu.grille_adversaire.grille[0][4] = 5

    jeu.executer_jeu()

if __name__ == "__main__":
    configurer_jeu()