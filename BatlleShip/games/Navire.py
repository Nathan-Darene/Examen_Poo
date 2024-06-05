class Navire:
    def __init__(self, taille, nom):
        """
        Initialise un navire avec une taille et un nom.

        :param taille: La taille du navire.
        :param nom: Le nom du navire.
        """
        self.taille = taille
        self.nom = nom
        self.positions = []  # Liste des positions du navire sur la grille.
        self.touche = [False] * taille  # Liste indiquant si chaque partie du navire a été touchée.

    def placer(self, positions):
        """
        Place le navire aux positions spécifiées.

        :param positions: Liste de tuples représentant les positions (x, y) du navire.
        """
        self.positions = positions

    def est_coule(self):
        """
        Vérifie si le navire est coulé.

        :return: True si toutes les parties du navire sont touchées, sinon False.
        """
        return all(self.touche)
