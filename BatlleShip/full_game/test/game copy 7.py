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
        self.navires = []  # Stocke les informations sur les navires placés

    def dessiner_lignes(self, screen):
        for ligne in range(TAILLE_GRILLE + 1):
            pygame.draw.line(screen, NOIR, (self.decalage_x + MARGE, self.decalage_y + MARGE + ligne * (TAILLE_CELLULE + MARGE)),
                             (self.decalage_x + MARGE + TAILLE_GRILLE * (TAILLE_CELLULE + MARGE), self.decalage_y + MARGE + ligne * (TAILLE_CELLULE + MARGE)), 2)
        for colonne in range(TAILLE_GRILLE + 1):
            pygame.draw.line(screen, NOIR, (self.decalage_x + MARGE + colonne * (TAILLE_CELLULE + MARGE), self.decalage_y + MARGE),
                             (self.decalage_x + MARGE + colonne * (TAILLE_CELLULE + MARGE), self.decalage_y + MARGE + TAILLE_GRILLE * (TAILLE_CELLULE + MARGE)), 2)

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

    def dessiner(self, screen):
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
            etiquette = font.render(str(i + 1), True, NOIR)
            screen.blit(etiquette, (self.decalage_x - MARGE, (MARGE + TAILLE_CELLULE) * i + MARGE + self.decalage_y + TAILLE_CELLULE // 3))
            etiquette = font.render(chr(65 + i), True, NOIR)
            screen.blit(etiquette, ((MARGE + TAILLE_CELLULE) * i + MARGE + self.decalage_x + TAILLE_CELLULE // 3, self.decalage_y - MARGE))

        # Dessiner les images des navires
        for navire in self.navires:
            ligne, colonne, type_navire, orientation = navire
            image_navire = self.images_navires[type_navire]
            taille = self.taille_navires[type_navire]

            if orientation == 'H':
                image_navire = pygame.transform.scale(image_navire, (TAILLE_CELLULE * taille + (taille - 1) * MARGE, TAILLE_CELLULE))
                screen.blit(image_navire, ((MARGE + TAILLE_CELLULE) * colonne + MARGE + self.decalage_x,
                                           (MARGE + TAILLE_CELLULE) * ligne + MARGE + self.decalage_y))
            elif orientation == 'V':
                image_navire = pygame.transform.rotate(image_navire, 90)
                image_navire = pygame.transform.scale(image_navire, (TAILLE_CELLULE, TAILLE_CELLULE * taille + (taille - 1) * MARGE))
                screen.blit(image_navire, ((MARGE + TAILLE_CELLULE) * colonne + MARGE + self.decalage_x,
                                           (MARGE + TAILLE_CELLULE) * ligne + MARGE + self.decalage_y))
    def obtenir_navire_sous_souris(self, pos):
        for i, (ligne, colonne, type_navire, orientation) in enumerate(self.navires):
            taille = self.taille_navires[type_navire]
            x = self.decalage_x + MARGE + (MARGE + TAILLE_CELLULE) * colonne
            y = self.decalage_y + MARGE + (MARGE + TAILLE_CELLULE) * ligne

            if orientation == 'H':
                rect = pygame.Rect(x, y, TAILLE_CELLULE * taille + MARGE * (taille - 1), TAILLE_CELLULE)
            elif orientation == 'V':
                rect = pygame.Rect(x, y, TAILLE_CELLULE, TAILLE_CELLULE * taille + MARGE * (taille - 1))

            if rect.collidepoint(pos):
                return i, type_navire
        return None, None

    def deplacer_navire(self, index, nouvelle_ligne, nouvelle_colonne):
        if 0 <= nouvelle_ligne < TAILLE_GRILLE and 0 <= nouvelle_colonne < TAILLE_GRILLE:
            ligne, colonne, type_navire, orientation = self.navires[index]
            taille = self.taille_navires[type_navire]

            # Vérifier que le nouveau placement est valide (ne sort pas de la grille)
            if (orientation == 'H' and nouvelle_colonne + taille <= TAILLE_GRILLE) or \
               (orientation == 'V' and nouvelle_ligne + taille <= TAILLE_GRILLE):
                # Nettoyer l'ancienne position
                if orientation == 'H':
                    for i in range(taille):
                        self.grille[ligne][colonne + i] = 0
                elif orientation == 'V':
                    for i in range(taille):
                        self.grille[ligne + i][colonne] = 0

                # Placer le navire à la nouvelle position
                self.navires[index] = (nouvelle_ligne, nouvelle_colonne, type_navire, orientation)
                if orientation == 'H':
                    for i in range(taille):
                        self.grille[nouvelle_ligne][nouvelle_colonne + i] = 1
                elif orientation == 'V':
                    for i in range(taille):
                        self.grille[nouvelle_ligne + i][nouvelle_colonne] = 1

    def changer_orientation_navire(self, index):
        ligne, colonne, type_navire, orientation = self.navires[index]
        taille = self.taille_navires[type_navire]

        # Nettoyer l'ancienne position
        if orientation == 'H':
            for i in range(taille):
                self.grille[ligne][colonne + i] = 0
        elif orientation == 'V':
            for i in range(taille):
                self.grille[ligne + i][colonne] = 0

        # Changer l'orientation
        nouvelle_orientation = 'V' if orientation == 'H' else 'H'

        # Vérifier que le nouveau placement est valide (ne sort pas de la grille)
        if (nouvelle_orientation == 'H' and colonne + taille <= TAILLE_GRILLE) or \
           (nouvelle_orientation == 'V' and ligne + taille <= TAILLE_GRILLE):
            # Placer le navire à la nouvelle position avec la nouvelle orientation
            self.navires[index] = (ligne, colonne, type_navire, nouvelle_orientation)
            if nouvelle_orientation == 'H':
                for i in range(taille):
                    self.grille[ligne][colonne + i] = 1
            elif nouvelle_orientation == 'V':
                for i in range(taille):
                    self.grille[ligne + i][colonne] = 1
        else:
            # Si le changement d'orientation échoue, replacer le navire à l'ancienne position avec l'ancienne orientation
            if orientation == 'H':
                for i in range(taille):
                    self.grille[ligne][colonne + i] = 1
            elif orientation == 'V':
                for i in range(taille):
                    self.grille[ligne + i][colonne] = 1

# Classe pour le bouton de changement d'orientation
class Bouton:
    def __init__(self, texte, pos, size):
        self.texte = texte
        self.pos = pos
        self.size = size
        self.rect = pygame.Rect(pos, size)
        self.font = pygame.font.SysFont("sans-serif", 36)
        self.couleur = BLEU

    def dessiner(self, screen):
        pygame.draw.rect(screen, self.couleur, self.rect)
        texte_surface = self.font.render(self.texte, True, BLANC)
        texte_rect = texte_surface.get_rect(center=self.rect.center)
        screen.blit(texte_surface, texte_rect)

    def est_clique(self, pos):
        return self.rect.collidepoint(pos)

# Classe principale du jeu
class JeuBatailleNavale:
    def __init__(self):
        self.ecran = pygame.display.set_mode((LARGEUR_ECRAN, HAUTEUR_ECRAN))
        pygame.display.set_caption("Bataille Navale")
        self.horloge = pygame.time.Clock()
        self.grille1 = Grille(100, 100)
        self.grille2 = Grille(1080, 100)  # Ajusté pour être à droite de la première grille
        self.selectionne = None
        self.grille_selectionnee = None
        self.bouton_orientation = Bouton("Changer Orientation", (50, 900), (300, 50))

    def executer_jeu(self):
        en_cours = True
        en_placement = True

        while en_cours:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    en_cours = False
                elif event.type == pygame.MOUSEBUTTONDOWN and en_placement:
                    pos = pygame.mouse.get_pos()
                    if self.bouton_orientation.est_clique(pos) and self.selectionne is not None and self.grille_selectionnee is not None:
                        self.grille_selectionnee.changer_orientation_navire(self.selectionne)
                        self.selectionne = None  # Réinitialiser la sélection après changement d'orientation
                    else:
                        for grille in [self.grille1, self.grille2]:
                            index, type_navire = grille.obtenir_navire_sous_souris(pos)
                            if index is not None:
                                self.selectionne = index
                                self.grille_selectionnee = grille
                                break
                elif event.type == pygame.MOUSEBUTTONUP and en_placement:
                    self.selectionne = None
                    self.grille_selectionnee = None
                elif event.type == pygame.MOUSEMOTION and self.selectionne is not None and en_placement:
                    pos = pygame.mouse.get_pos()
                    nouvelle_colonne = (pos[0] - self.grille_selectionnee.decalage_x - MARGE) // (TAILLE_CELLULE + MARGE)
                    nouvelle_ligne = (pos[1] - self.grille_selectionnee.decalage_y - MARGE) // (TAILLE_CELLULE + MARGE)
                    self.grille_selectionnee.deplacer_navire(self.selectionne, nouvelle_ligne, nouvelle_colonne)

            self.ecran.fill(GRIS)
            self.grille1.dessiner(self.ecran)
            self.grille2.dessiner(self.ecran)
            self.bouton_orientation.dessiner(self.ecran)
            pygame.display.flip()
            self.horloge.tick(60)

        pygame.quit()
        sys.exit()

# Placer des bateaux de manière fixe pour le test
def configurer_jeu():
    jeu = JeuBatailleNavale()
    jeu.grille1.placer_bateau(0, 0, "porte_avions", 'H')
    jeu.grille1.placer_bateau(4, 1, "croiseur", 'H')
    jeu.grille1.placer_bateau(6, 1, "contre_torpilleur", 'H')
    jeu.grille1.placer_bateau(8, 1, "sous_marin", 'H')
    jeu.grille1.placer_bateau(9, 1, "torpilleur", 'H')

    jeu.executer_jeu()

if __name__ == "__main__":
    configurer_jeu()
