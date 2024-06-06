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
        #Chargement des images des Navire 
        self.contre_torpilleur_image = pygame.image.load("/media/nathan/liaison/Documents/Examen_POO/BatlleShip/assets/images/contre_torpilleur.png")
        self.porte_avions_image = pygame.image.load("/media/nathan/liaison/Documents/Examen_POO/BatlleShip/assets/images/porte_avions.png")
        self.torpilleur_image = pygame.image.load("/media/nathan/liaison/Documents/Examen_POO/BatlleShip/assets/images/torpilleur.png")
        self.sous_marin_image = pygame.image.load("/media/nathan/liaison/Documents/Examen_POO/BatlleShip/assets/images/sous_marin.png")
        self.croiseur_image = pygame.image.load("/media/nathan/liaison/Documents/Examen_POO/BatlleShip/assets/images/croiseur.png")


    #La méthode dessiner_lignes est responsable du dessin des lignes noires qui délimitent les cellules de chaque  grilles.
    def dessiner_lignes(self, screen):
        for ligne in range(TAILLE_GRILLE + 1):
            pygame.draw.line(screen, NOIR, (self.decalage_x + MARGE, self.decalage_y + MARGE + ligne * (TAILLE_CELLULE + MARGE)),
                            (self.decalage_x + MARGE + TAILLE_GRILLE * (TAILLE_CELLULE + MARGE), self.decalage_y + MARGE + ligne * (TAILLE_CELLULE + MARGE)), 2)
            
        for colonne in range(TAILLE_GRILLE + 1):
            pygame.draw.line(screen, NOIR, (self.decalage_x + MARGE + colonne * (TAILLE_CELLULE + MARGE), self.decalage_y + MARGE),
                            (self.decalage_x + MARGE + colonne * (TAILLE_CELLULE + MARGE), self.decalage_y + MARGE + TAILLE_GRILLE * (TAILLE_CELLULE + MARGE)), 2)
            
    def placer_bateau(self, ligne_depart, colonne_depart, taille, orientation, joueur1=False):
            if joueur1:
                if orientation == 'H':
                    if taille == 5:
                        self.type_navire = "porte_avions"
                    elif taille == 4:
                        self.type_navire = "croiseur"
                    elif taille == 3:
                        self.type_navire = "contre_torpilleur"
                    elif taille == 2:
                        self.type_navire = "torpilleur"
                else:  # Orientation verticale
                    if taille == 5:
                        self.type_navire = "porte_avions"
                    elif taille == 4:
                        self.type_navire = "croiseur"
                    
                    



    def dessiner(self, screen,joueur1=False):
        font = pygame.font.SysFont("sans-serif", 36)
        # Dessiner les images des navire
        for ligne in range(TAILLE_GRILLE):
            for colonne in range(TAILLE_GRILLE):
                if self.grille[ligne][colonne] == 1 and joueur1:  # Si la case est occupée par un navire du joueur 1
                    navire_image = getattr(self, self.type_navire + "_image").copy()  # Obtenir l'image du navire                
                    pygame.draw.rect(screen,
                                navire_image,
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

        # Dictionnaire pour associer les tailles aux types de navires
        taille_type_navire = {
        5: "porte_avions",
        4: "croiseur",
        3: "contre_torpilleur",
        3: "sous_marin",
        2: "torpilleur",
        }

        # Dessiner les images des navires
        for ligne in range(TAILLE_GRILLE):
            for colonne in range(TAILLE_GRILLE):
                if self.grille[ligne][colonne] == 1 and joueur1:  # Si la case est occupée par un navire
                    taille_navire = self.verifier_taille_navire(ligne, colonne, joueur1)  # Obtenir la taille du navire
                    navire_image = getattr(self, taille_type_navire[taille_navire] + "_image").copy()
                    if joueur1:  # Vérifier si c'est la grille du joueur 1
                        # Placer les images des navires du joueur 1
                        if self.grille[ligne][colonne:colonne + 5] == [1] * 5:  # Porte-avions
                            navire_image = self.porte_avions_image.copy()  # Faire une copie pour la rotation
                        elif self.grille[ligne][colonne:colonne + 4] == [1] * 4:  # Croiseur
                            navire_image = self.croiseur_image.copy()
                        elif self.grille[ligne][colonne:colonne + 3] == [1] * 3:  # Contre-torpilleur
                            navire_image = self.contre_torpilleur_image.copy()
                        elif ligne + 2 < TAILLE_GRILLE and all(
                                self.grille[ligne + i][colonne] == 1 for i in range(3)):  # Sous-marin
                            navire_image = self.sous_marin_image.copy()
                        elif colonne + 1 < TAILLE_GRILLE and self.grille[ligne][colonne:colonne + 2] == [1] * 2:  # Torpilleur
                            navire_image = self.torpilleur_image




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
            self.grille1.dessiner(self.ecran)
            self.grille2.dessiner(self.ecran)
            pygame.display.flip()
            self.horloge.tick(60)
        
        pygame.quit()
        sys.exit()

# Placer des bateaux de manière fixe pour le test
def configurer_jeu():
    jeu = JeuBatailleNavale()
    jeu.grille1.placer_bateau(2, 1, 5, 'H', joueur1=False)  # Exemple de placement de bateaux
    jeu.grille1.placer_bateau(2, 1, 3, 'H', joueur1=False)
    jeu.grille1.placer_bateau(4, 2, 3, 'H', joueur1=False)
    jeu.grille1.placer_bateau(6, 1, 2, 'H', joueur1=False)
    jeu.grille1.placer_bateau(8, 1, 2, 'H', joueur1=False)

    jeu.executer_jeu()

if __name__ == "__main__":
    configurer_jeu()
