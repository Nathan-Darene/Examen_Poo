import pygame
import sys
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

# Classe pour représenter la grille
class Grille:
    def __init__(self, decalage_x, decalage_y):
        # Initialise une grille vide
        self.grille = [[0 for _ in range(TAILLE_GRILLE)] for _ in range(TAILLE_GRILLE)]
        self.decalage_x = decalage_x  # Décalage horizontal de la grille
        self.decalage_y = decalage_y  # Décalage vertical de la grille
        
        # Chargement des images des navires
        self.images_navires = {
            "contre_torpilleur": pygame.image.load("BatlleShip/assets/images/contre_torpilleur.png"),
            "porte_avions": pygame.image.load("BatlleShip/assets/images/porte_avions.png"),
            "sous_marin": pygame.image.load("BatlleShip/assets/images/sous_marin.png"),
            "torpilleur": pygame.image.load("BatlleShip/assets/images/torpilleur.png"),
            "croiseur": pygame.image.load("BatlleShip/assets/images/croiseur.png")
        }
        
        # Tailles des navires
        self.taille_navires = {
            "porte_avions": 5,
            "croiseur": 4,
            "contre_torpilleur": 3,
            "sous_marin": 3,
            "torpilleur": 2
        }
        
        # Liste pour stocker les navires placés
        self.navires = []

    def dessiner_lignes(self, screen):
        # Dessine les lignes de la grille
        for ligne in range(TAILLE_GRILLE + 1):
            pygame.draw.line(screen, NOIR,
                             (self.decalage_x + ESPACE_ETIQUETTES, self.decalage_y + ESPACE_ETIQUETTES + ligne * (TAILLE_CELLULE + MARGE)),
                             (self.decalage_x + ESPACE_ETIQUETTES + TAILLE_GRILLE * (TAILLE_CELLULE + MARGE), self.decalage_y + ESPACE_ETIQUETTES + ligne * (TAILLE_CELLULE + MARGE)), 2)
        for colonne in range(TAILLE_GRILLE + 1):
            pygame.draw.line(screen, NOIR,
                             (self.decalage_x + ESPACE_ETIQUETTES + colonne * (TAILLE_CELLULE + MARGE), self.decalage_y + ESPACE_ETIQUETTES),
                             (self.decalage_x + ESPACE_ETIQUETTES + colonne * (TAILLE_CELLULE + MARGE), self.decalage_y + ESPACE_ETIQUETTES + TAILLE_GRILLE * (TAILLE_CELLULE + MARGE)), 2)

    def placer_bateau(self, ligne_depart, colonne_depart, type_navire, orientation='H'):
        # Place un bateau sur la grille à la position donnée
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

    def placer_bateaux_aleatoires(self):
        # Place les bateaux de manière aléatoire sur la grille
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
        # Vérifie si un bateau peut être placé à la position donnée
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
        # Dessine la grille, les étiquettes et les navires
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
        # Obtient le navire sous la position de la souris
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
        # Déplace un navire à une nouvelle position si possible
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

# Classe principale du jeu
class JeuBatailleNavale:
    def __init__(self):
        self.ecran = pygame.display.set_mode((LARGEUR_ECRAN, HAUTEUR_ECRAN))  # Crée la fenêtre de jeu
        pygame.display.set_caption("Bataille Navale")  # Définit le titre de la fenêtre
        self.horloge = pygame.time.Clock()  # Crée une horloge pour contrôler le FPS
        self.grille1 = Grille(100, 100)  # Grille du joueur 1
        self.grille2 = Grille(1080, 100)  # Grille du joueur 2
        self.selectionne_joueur1 = None  # Index du navire sélectionné par le joueur 1
        self.selectionne_joueur2 = None  # Index du navire sélectionné par le joueur 2
        self.joueur_actif = 1  # Le joueur 1 commence

    def executer_jeu(self):
        en_cours = True  # Variable pour garder le jeu en cours d'exécution
        en_placement = True  # Variable pour indiquer si le jeu est en phase de placement des navires

        while en_cours:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Ferme le jeu si l'utilisateur clique sur le bouton de fermeture
                    en_cours = False
                elif event.type == pygame.MOUSEBUTTONDOWN and en_placement:
                    pos = pygame.mouse.get_pos()  # Obtient la position de la souris
                    if self.joueur_actif == 1:
                        index, type_navire = self.grille1.obtenir_navire_sous_souris(pos)
                        if index is not None:
                            self.selectionne_joueur1 = index  # Sélectionne le navire sous la souris pour le joueur 1
                    elif self.joueur_actif == 2:
                        index, type_navire = self.grille2.obtenir_navire_sous_souris(pos)
                        if index is not None:
                            self.selectionne_joueur2 = index  # Sélectionne le navire sous la souris pour le joueur 2
                elif event.type == pygame.MOUSEBUTTONUP and en_placement:
                    if self.joueur_actif == 1:
                        self.selectionne_joueur1 = None  # Désélectionne le navire pour le joueur 1
                    elif self.joueur_actif == 2:
                        self.selectionne_joueur2 = None  # Désélectionne le navire pour le joueur 2
                elif event.type == pygame.MOUSEMOTION and en_placement:
                    pos = pygame.mouse.get_pos()  # Obtient la position de la souris
                    nouvelle_colonne = (pos[0] - MARGE) // (TAILLE_CELLULE + MARGE)
                    nouvelle_ligne = (pos[1] - MARGE) // (TAILLE_CELLULE + MARGE)
                    if self.joueur_actif == 1 and self.selectionne_joueur1 is not None:
                        self.grille1.deplacer_navire(self.selectionne_joueur1, nouvelle_ligne, nouvelle_colonne)
                    elif self.joueur_actif == 2 and self.selectionne_joueur2 is not None:
                        self.grille2.deplacer_navire(self.selectionne_joueur2, nouvelle_ligne, nouvelle_colonne)

            self.ecran.fill(GRIS)  # Remplit l'écran avec la couleur de fond
            self.grille1.dessiner(self.ecran)  # Dessine la grille du joueur 1
            self.grille2.dessiner(self.ecran)  # Dessine la grille du joueur 2
            pygame.display.flip()  # Met à jour l'affichage
            self.horloge.tick(60)  # Limite le jeu à 60 FPS

        pygame.quit()  # Quitte Pygame
        sys.exit()  # Ferme le programme

# Placer des bateaux de manière fixe pour le test
def configurer_jeu():
    jeu = JeuBatailleNavale()

    # Placement fixe des navires pour le joueur 1
    jeu.grille1.placer_bateau(0, 0, "porte_avions", 'V')
    jeu.grille1.placer_bateau(4, 2, "croiseur", 'V')
    jeu.grille1.placer_bateau(6, 1, "contre_torpilleur", 'H')
    jeu.grille1.placer_bateau(7, 1, "sous_marin", 'H')
    jeu.grille1.placer_bateau(8, 3, "torpilleur", 'H')

    # Placement aléatoire des navires pour le joueur 2
    jeu.grille2.placer_bateaux_aleatoires()

    # Exécute le jeu
    jeu.executer_jeu()

if __name__ == "__main__":
    configurer_jeu()
