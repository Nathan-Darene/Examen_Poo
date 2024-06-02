from Grille import Grille

class Joueur:
    def __init__(self, nom):
        """
        Initialise un joueur avec un nom et deux grilles (personnelle et de l'adversaire).

        :param nom: Le nom du joueur.
        """
        self.nom = nom
        self.grille_personnelle = Grille(10)  # Grille personnelle du joueur.
        self.grille_adversaire = Grille(10)  # Grille de l'adversaire.

    def placer_navire(self, navire, positions):
        """
        Place un navire sur la grille personnelle du joueur.

        :param navire: Instance de la classe Navire.
        :param positions: Liste de tuples représentant les positions (x, y) du navire.
        """
        self.grille_personnelle.ajouter_navire(navire, positions)

    def tirer(self, position, adversaire):
        """
        Effectue un tir sur la grille de l'adversaire à la position spécifiée.

        :param position: Tuple représentant la position (x, y) du tir.
        :param adversaire: Instance de la classe Joueur représentant l'adversaire.
        :return: True si un navire de l'adversaire est touché, sinon False.
        """
        return adversaire.grille_personnelle.tirer(position)
