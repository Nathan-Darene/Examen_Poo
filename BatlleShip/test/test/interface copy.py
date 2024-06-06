import pygame
import random
from Grille import Grille
from Bateau import Bateau
from Jeu import Jeu

pygame.init()


# Taille de l'écran
ECRAN_LARGEUR = 800
ECRAN_HAUTEUR = 600

# Couleurs
COULEUR_BLANC = (255, 255, 255)
COULEUR_NOIR = (0, 0, 0)
COULEUR_BLEU = (0, 0, 255)
COULEUR_ROUGE = (255, 0, 0)
COULEUR_GRIS = (128, 128, 128)

# Images des navires
IMAGE_PORTE_AVIONS = pygame.image.load("BatlleShip/assets/images/porte_avions.png")
IMAGE_CROISEUR = pygame.image.load("BatlleShip/assets/images/croiseur.png")
IMAGE_CONTRE_TORPILLEUR = pygame.image.load("BatlleShip/assets/images/contre_torpilleur.png")
IMAGE_SOUS_MARIN = pygame.image.load("BatlleShip/assets/images/sous_marin.png")
IMAGE_TORPILLEUR = pygame.image.load("BatlleShip/assets/images/torpilleur.png")

# Taille des cases
TAILLE_CASE = 50

# Police d'écriture
POLICE = pygame.font.Font(None, 32)

class InterfaceGraphique:
    def __init__(self):
        self.ecran = pygame.display.set_mode((ECRAN_LARGEUR, ECRAN_HAUTEUR))
        pygame.display.set_caption("Bataille Navale")
        self.jeu = Jeu()

    def afficher_grille(self, grille, x_debut, y_debut):
        for i, ligne in enumerate(grille.grille):
            for j, case in enumerate(ligne):
                x = x_debut + j * TAILLE_CASE
                y = y_debut + i * TAILLE_CASE
                if case == 0:
                    pygame.draw.rect(self.ecran, COULEUR_BLEU, (x, y, TAILLE_CASE, TAILLE_CASE))
                elif case == "X":
                    pygame.draw.rect(self.ecran, COULEUR_ROUGE, (x, y, TAILLE_CASE, TAILLE_CASE))
                elif case != 0:
                    image_navire = self.get_image_navire(case)
                    self.ecran.blit(image_navire, (x, y))

    def get_image_navire(self, taille_navire):
        if taille_navire == 5:
            return IMAGE_PORTE_AVIONS
        elif taille_navire == 4:
            return IMAGE_CROISEUR
        elif taille_navire == 3:
            return IMAGE_CONTRE_TORPILLEUR
        elif taille_navire == 2:
            return IMAGE_SOUS_MARIN
        else:
            return IMAGE_TORPILLEUR

    def afficher_resultat(self, resultat):
        texte = POLICE.render(resultat, True, COULEUR_NOIR)
        rect_texte = texte.get_rect(center=(ECRAN_LARGEUR // 2, ECRAN_HAUTEUR // 2))
        self.ecran.blit(texte, rect_texte)

    def afficher_aide(self):
        texte_aide = [
            "0 - Pas de bateau",
            "2 - Torpilleur",
            "3 - Sous-marin",
            "3 - Contre-torpilleur",
            "4 - Croiseur",
            "5 - Porte-avions",
            "X - Bateau touché"
        ]
        # y = 20
        # for ligne in texte_aide:


def main():
    interface = InterfaceGraphique()
    jeu = interface.jeu

    # Placer les bateaux aléatoirement
    jeu.placer_bateaux_aleatoire(jeu.grille_joueur)
    jeu.placer_bateaux_aleatoire(jeu.grille_ia)

    tour_joueur = True
    fin_jeu = False
    while not fin_jeu:
        # Gérer les événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin_jeu = True

            # Clic gauche sur une case
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if tour_joueur:
                    x = event.pos[0] // TAILLE_CASE
                    y = event.pos[1] // TAILLE_CASE
                    if 0 <= x < 10 and 0 <= y < 10:
                        resultat = jeu.grille_ia.recevoir_tir(x, y)
                        jeu.tirs_joueur[x][y] = True
                        tour_joueur = not tour_joueur

        # Afficher l'interface
        interface.ecran.fill(COULEUR_GRIS)

        # Afficher les grilles
        interface.afficher_grille(jeu.grille_joueur, 100, 100)
        interface.afficher_grille(jeu.grille_ia, 450, 100)

        # Afficher le tour actuel
        if tour_joueur:
            texte_tour = POLICE.render("Votre tour", True, COULEUR_BLEU)
        else:
            texte_tour = POLICE.render("Tour de l'IA", True, COULEUR_ROUGE)
        interface.ecran.blit(texte_tour, (100, 20))

        # Mettre à jour l'affichage
        pygame.display.flip()

        # Vérifier si tous les bateaux sont coulés
        if jeu.grille_joueur.verifier_victoire() or jeu.grille_ia.verifier_victoire():
            fin_jeu = True

    # Afficher le message de fin de partie
    if jeu.grille_joueur.verifier_victoire():
        texte_fin = POLICE.render("Vous avez gagné !", True, COULEUR_BLEU)
    else:
        texte_fin = POLICE.render("L'IA a gagné !", True, COULEUR_ROUGE)
    interface.ecran.blit(texte_fin, (ECRAN_LARGEUR // 2 - 150, ECRAN_HAUTEUR // 2 - 30))
    pygame.display.flip()

    # Attendre quelques secondes avant de quitter
    pygame.time.wait(3000)

    pygame.quit()

if __name__ == "__main__":
    main()
