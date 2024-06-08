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
VERT = (0, 255, 0)  # Couleur du bouton "Prêt"

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
                for i in range(taille):
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

    def deplacer_navire(self, index, nouvelle_ligne, nouvelle_colonne, nouvelle_orientation=None):
        if 0 <= nouvelle_ligne < TAILLE_GRILLE and 0 <= nouvelle_colonne < TAILLE_GRILLE:
            ligne, colonne, type_navire, orientation = self.navires[index]
            taille = self.taille_navires[type_navire]

            if nouvelle_orientation:
                orientation = nouvelle_orientation

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
        self.ecran = pygame.display.set_mode((LARGEUR_ECRAN, HAUTEUR_ECRAN))
        pygame.display.set_caption("Bataille Navale")
        self.horloge = pygame.time.Clock()
        self.grille1 = Grille(100, 100)
        self.grille2 = Grille(1080, 100)
        self.selectionne_joueur1 = None
        self.selectionne_joueur2 = None
        self.joueur_actif = 1
        self.joueur1_pret = False  # Indique si le joueur 1 est prêt

        # Dimensions du bouton "Prêt"
        self.bouton_pret = pygame.Rect(280, 650, 150, 50)  # Position et taille du bouton
        self.champ_direction = pygame.Rect(280, 720, 150, 50)  # Position et taille du champ de saisie
        self.bouton_valider_direction = pygame.Rect(450, 720, 150, 50)  # Bouton pour valider la direction

        self.direction = 'H'  # Direction par défaut

    def executer_jeu(self):
        en_cours = True
        en_placement = True
        actif_champ_direction = False

        while en_cours:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    en_cours = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if self.bouton_pret.collidepoint(pos):
                        self.joueur1_pret = True  # Le joueur 1 est prêt
                        en_placement = False  # Terminer la phase de placement pour le joueur 1
                    elif self.champ_direction.collidepoint(pos):
                        actif_champ_direction = True
                    elif self.bouton_valider_direction.collidepoint(pos):
                        if self.selectionne_joueur1 is not None:
                            navire = self.grille1.navires[self.selectionne_joueur1]
                            self.grille1.deplacer_navire(self.selectionne_joueur1, navire[0], navire[1], self.direction)
                    else:
                        actif_champ_direction = False

                    if en_placement and not self.joueur1_pret:
                        if self.joueur_actif == 1:
                            index, type_navire = self.grille1.obtenir_navire_sous_souris(pos)
                            if index is not None:
                                self.selectionne_joueur1 = index
                        elif self.joueur_actif == 2:
                            index, type_navire = self.grille2.obtenir_navire_sous_souris(pos)
                            if index is not None:
                                self.selectionne_joueur2 = index
                elif event.type == pygame.MOUSEBUTTONUP and en_placement:
                    if self.joueur_actif == 1:
                        self.selectionne_joueur1 = None
                    elif self.joueur_actif == 2:
                        self.selectionne_joueur2 = None
                elif event.type == pygame.MOUSEMOTION and en_placement and not self.joueur1_pret:
                    pos = pygame.mouse.get_pos()
                    nouvelle_colonne = (pos[0] - MARGE) // (TAILLE_CELLULE + MARGE)
                    nouvelle_ligne = (pos[1] - MARGE) // (TAILLE_CELLULE + MARGE)
                    if self.joueur_actif == 1 and self.selectionne_joueur1 is not None:
                        self.grille1.deplacer_navire(self.selectionne_joueur1, nouvelle_ligne, nouvelle_colonne)
                    elif self.joueur_actif == 2 and self.selectionne_joueur2 is not None:
                        self.grille2.deplacer_navire(self.selectionne_joueur2, nouvelle_ligne, nouvelle_colonne)
                elif event.type == pygame.KEYDOWN and actif_champ_direction:
                    if event.key == pygame.K_BACKSPACE:
                        self.direction = self.direction[:-1]
                    elif event.key == pygame.K_RETURN:
                        actif_champ_direction = False
                    else:
                        self.direction += event.unicode.upper()

            self.ecran.fill(GRIS)
            self.grille1.dessiner(self.ecran)
            self.grille2.dessiner(self.ecran)

            # Dessiner le bouton "Prêt"
            if not self.joueur1_pret:
                pygame.draw.rect(self.ecran, VERT, self.bouton_pret)
                font = pygame.font.SysFont("sans-serif", 36)
                texte_pret = font.render("Prêt", True, NOIR)
                self.ecran.blit(texte_pret, (self.bouton_pret.x + 50, self.bouton_pret.y + 10))

                # Dessiner le champ de saisie pour la direction
                pygame.draw.rect(self.ecran, BLANC, self.champ_direction)
                texte_direction = font.render(self.direction, True, NOIR)
                self.ecran.blit(texte_direction, (self.champ_direction.x + 10, self.champ_direction.y + 10))

                # Dessiner le bouton pour valider la direction
                pygame.draw.rect(self.ecran, VERT, self.bouton_valider_direction)
                texte_valider = font.render("Valider", True, NOIR)
                self.ecran.blit(texte_valider, (self.bouton_valider_direction.x + 20, self.bouton_valider_direction.y + 10))

            pygame.display.flip()
            self.horloge.tick(60)

        pygame.quit()
        sys.exit()

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
