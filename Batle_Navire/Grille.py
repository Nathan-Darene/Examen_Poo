class Grille:
    def __init__(self, taille):
        """
        Initialise une grille de jeu avec une taille spécifiée.

        :param taille: La taille de la grille (nombre de cases en largeur et en hauteur).
        """
        self.taille = taille
        self.navires = []  # Liste des navires placés sur la grille.

    def ajouter_navire(self, navire, positions):
        """
        Ajoute un navire à la grille à des positions spécifiques.

        :param navire: Instance de la classe Navire.
        :param positions: Liste de tuples représentant les positions (x, y) du navire.
        :raises ValueError: Si les positions sont en dehors de la grille.
        """
        if all(0 <= x < self.taille and 0 <= y < self.taille for x, y in positions):
            navire.placer(positions)
            self.navires.append(navire)
        else:
            raise ValueError("Positions invalides pour le navire.")

    def tirer(self, position):
        """
        Effectue un tir sur la grille à la position spécifiée.

        :param position: Tuple représentant la position (x, y) du tir.
        :return: True si un navire est touché, sinon False.
        """
        for navire in self.navires:
            if position in navire.positions:
                index = navire.positions.index(position)
                navire.touche[index] = True
                return True
        return False
