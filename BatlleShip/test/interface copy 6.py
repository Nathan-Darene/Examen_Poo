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

# Liste de lettres pour les colonnes
LETTRES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

# Identifiants pour les navires
PORTE_AVIONS = 1
CROISEUR = 2
CONTRE_TORPILLEUR = 3
SOUS_MARIN = 4
TORPILLEUR = 5

# Classe pour représenter la grille
class Grille:
    def __init__(self, decalage_x, decalage_y):
        self.grille = [[0 for _ in range(TAILLE_GRILLE)] for _ in range(TAILLE_GRILLE)]
        self.decalage_x = decalage_x
        self.decalage_y = decalage_y
        # Chargez les images des navires
        self.images = {
            PORTE_AVIONS: pygame.image.load("assets/images/porte_avions.png"),
            CROISEUR: pygame.image.load("assets/images/croiseur.png"),
            CONTRE_TORPILLEUR: pygame.image.load("assets/images/contre_torpilleur.png"),
            SOUS_MARIN: pygame.image.load("assets/images/sous_marin.png"),
            TORPILLEUR: pygame.image.load("assets/images/torpilleur.png")
        }
        
    def dessiner(self, screen):
        for ligne in range(TAILLE_GRILLE):
            for colonne in range(TAILLE_GRILLE):
                if self.grille[ligne][colonne] in self.images:
                    screen.blit(self.images[self.grille[ligne][colonne]], (self.decalage_x + colonne * (TAILLE_CELLULE + MARGE),
                                                                           self.decalage_y + ligne * (TAILLE_CELLULE + MARGE)))
        self.dessiner_lignes(screen)
        self.dessiner_indications(screen)

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
            text_rect = text.get_rect(center=(self.decalage_x + MARGE + (i + 1) * (TAILLE_CELLULE + MARGE), self.decalage_y))
            screen.blit(text, text_rect)
            # Dessiner les chiffres (lignes)
            text = font.render(str(i + 1), True, NOIR)
            text_rect = text.get_rect(center=(self.decalage_x, self.decalage_y + MARGE + (i + 1) * (TAILLE_CELLULE + MARGE)))
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
    jeu.grille_joueur1.grille[2][1] = PORTE_AVIONS  # Porte-avions (5 cases)
    jeu.grille_joueur1.grille[2][2] = PORTE_AVIONS
    jeu.grille_joueur1.grille[2][3] = PORTE_AVIONS
    jeu.grille_joueur1.grille[2][4] = PORTE_AVIONS
    jeu.grille_joueur1.grille[2][5] = PORTE_AVIONS
    jeu.grille_joueur1.grille[4][1] = CROISEUR  # Croiseur (4 cases)
    jeu.grille_joueur1.grille[4][2] = CROISEUR
    jeu.grille_joueur1.grille[4][3] = CROISEUR
    jeu.grille_joueur1.grille[4][4] = CROISEUR
    jeu.grille_joueur1.grille[6][1] = CONTRE_TORPILLEUR  # Contre-torpilleur (3 cases)
    jeu.grille_joueur1.grille[6][2] = CONTRE_TORPILLEUR
    jeu.grille_joueur1.grille[6][3] = CONTRE_TORPILLEUR
    jeu.grille_joueur1.grille[8][1] = SOUS_MARIN  # Sous-marin (3 cases)
    jeu.grille_joueur1.grille[8][2] = SOUS_MARIN
    jeu.grille_joueur1.grille[8][3] = SOUS_MARIN
    jeu.grille_joueur1.grille[9][1] = TORPILLEUR  # Torpilleur (2 cases)
    jeu.grille_joueur1.grille[9][2] = TORPILLEUR

    # Placer les bateaux sur la grille de l'adversaire
    jeu.grille_adversaire.grille[0][0] = PORTE_AVIONS  # Porte-avions (5 cases)
    jeu.grille_adversaire.grille[0][1] = PORTE_AVIONS
    jeu.grille_adversaire.grille[0][2] = PORTE_AVIONS
    jeu.grille_adversaire.grille[0][3] = PORTE_AVIONS
    jeu.grille_adversaire.grille[0][4] = PORTE_AVIONS
    jeu.grille_adversaire.grille[2][0] = CROISEUR  # Croiseur (4 cases)
    jeu.grille_adversaire.grille[2][1] = CROISEUR
    jeu.grille_adversaire.grille[2][2] = CROISEUR
    jeu.grille_adversaire.grille[2][3] = CROISEUR
    jeu.grille_adversaire.grille[4][0] = CONTRE_TORPILLEUR  # Contre-torpilleur (3 cases)
    jeu.grille_adversaire.grille[4][1] = CONTRE_TORPILLEUR
    jeu.grille_adversaire.grille[4][2] = CONTRE_TORPILLEUR
    jeu.grille_adversaire.grille[6][0] = SOUS_MARIN  # Sous-marin (3 cases)
    jeu.grille_adversaire.grille[6][1] = SOUS_MARIN
    jeu.grille_adversaire.grille[6][2] = SOUS_MARIN
    jeu.grille_adversaire.grille[8][0] = TORPILLEUR  # Torpilleur (2 cases)
    jeu.grille_adversaire.grille[8][1] = TORPILLEUR

    jeu.executer_jeu()

if __name__ == "__main__":
    configurer_jeu()
