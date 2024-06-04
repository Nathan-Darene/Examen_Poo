import random
from Joueur import Joueur

class IA(Joueur):
    def __init__(self, nom):
        """
        Initialise un joueur IA avec un nom.

        :param nom: Nom de l'IA.
        """
        super().__init__(nom)

    def tirer(self, joueur_adverse):
        """
        Effectue un tir aléatoire sur la grille de l'adversaire.

        :param joueur_adverse: Instance de la classe Joueur représentant l'adversaire.
        """
        while True:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if joueur_adverse.grille_personnelle.grille[x][y] == 0 or joueur_adverse.grille_personnelle.grille[x][y] == 1:
                continue  # Continue de chercher une case non encore attaquée
            else:
                position = (x, y)
                super().tirer(position, joueur_adverse)
                break
