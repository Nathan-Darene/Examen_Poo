import pygame
import sys
from Navire import Navire
from Joueur import Joueur
from IA import IA

class Jeu:
    def __init__(self, joueur1, joueur2):
        """
        # Initialise le jeu avec deux joueurs et configure la fenêtre Pygame.

        :param joueur1: Instance de la classe Joueur représentant le premier joueur.
        :param joueur2: Instance de la classe Joueur représentant le second joueur.
        """
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.tour = joueur1  # Le jeu commence avec le joueur1.
        self.taille_case = 40
        self.largeur_fenetre = self.taille_case * 12 * 2
        self.hauteur_fenetre = self.taille_case * 12
        self.fenetre = pygame.display.set_mode((self.largeur_fenetre, self.hauteur_fenetre))
        pygame.display.set_caption("Bataille Navale")

    def dessiner_grille(self, debut_x, debut_y):
        """
        Dessine une grille de jeu à une position spécifiée avec des cases semi-transparentes.

        :param debut_x: Coordonnée x du coin supérieur gauche de la grille.
        :param debut_y: Coordonnée y du coin supérieur gauche de la grille.
        """
        for x in range(10):
            for y in range(10):
                # Dessine un rectangle semi-transparent
                rect = pygame.Surface((self.taille_case, self.taille_case), pygame.SRCALPHA)
                rect.fill((0, 0, 255, 64))  # Bleu avec opacité réduite
                self.fenetre.blit(rect, (debut_x + x * self.taille_case, debut_y + y * self.taille_case))
        
        for x in range(11):
            pygame.draw.line(self.fenetre, (0, 0, 0), (debut_x + x * self.taille_case, debut_y), (debut_x + x * self.taille_case, debut_y + self.taille_case * 10))
            pygame.draw.line(self.fenetre, (0, 0, 0), (debut_x, debut_y + x * self.taille_case), (debut_x + self.taille_case * 10, debut_y + x * self.taille_case))

    def changer_tour(self):
        """
        Change le tour au joueur suivant.
        """
        self.tour = self.joueur1 if self.tour == self.joueur2 else self.joueur2

    def est_fini(self):
        """
        Vérifie si le jeu est terminé (tous les navires d'un joueur sont coulés).

        :return: True si le jeu est terminé, sinon False.
        """
        return all(navire.est_coule() for navire in self.joueur1.grille_personnelle.navires) or \
               all(navire.est_coule() for navire in self.joueur2.grille_personnelle.navires)

    def jouer(self):
        """
        Lance la boucle principale du jeu où les joueurs tirent à tour de rôle jusqu'à ce qu'un joueur gagne.
        """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.fenetre.fill((255, 255, 255))
            self.dessiner_grille(self.taille_case, self.taille_case)
            self.dessiner_grille(self.taille_case * 13, self.taille_case)

            font = pygame.font.SysFont(None, 36)
            label_joueur = font.render("Votre grille de jeu", True, (0, 0, 0))
            label_adversaire = font.render("La grille de l'adversaire", True, (0, 0, 0))
            self.fenetre.blit(label_joueur, (self.taille_case, self.taille_case * 11.5))
            self.fenetre.blit(label_adversaire, (self.taille_case * 13, self.taille_case * 11.5))

            bouton_jouer = pygame.Rect(self.taille_case * 22, self.taille_case * 5, 100, 50)
            pygame.draw.rect(self.fenetre, (0, 255, 0), bouton_jouer)
            label_jouer = font.render("Jouer", True, (0, 0, 0))
            self.fenetre.blit(label_jouer, (self.taille_case * 22 + 20, self.taille_case * 5 + 10))

            pygame.display.flip()

            if self.est_fini():
                gagnant = "joueur1" if all(navire.est_coule() for navire in self.joueur2.grille_personnelle.navires) else "joueur2"
                print("Jeu terminé! Le gagnant est " + gagnant + " !")
                break

            if self.tour == self.joueur1:
                # Tour du joueur humain
                x = int(input("Entrer la coordonnée x: "))
                y = int(input("Entrer la coordonnée y: "))
                position = (x, y)
                self.joueur1.tirer(position, self.joueur2)
            else:
                # Tour de l'IA
                self.joueur2.tirer(self.joueur1)

            self.changer_tour()

if __name__ == "__main__":
    pygame.init()

    joueur1 = Joueur("Alice")
    joueur2 = IA("Bob")

    navire1 = Navire(5, "Porte-avions")
    navire2 = Navire(4, "Cuirassé")

    joueur1.placer_navire(navire1, [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)])
    joueur2.placer_navire(navire2, [(1, 0), (1, 1), (1, 2), (1, 3)])

    jeu = Jeu(joueur1, joueur2)
    jeu.jouer()
