class Navire:
    def __init__(self, taille, nom):
        """
        Initialise un navire avec une taille spécifique et un nom.
        
        :param taille: Taille du navire (nombre de cases qu'il occupe).
        :param nom: Nom du navire.
        """
        self.taille = taille
        self.nom = nom
        self.positions = []  # Liste des positions (x, y) occupées par le navire.
        self.touche = [False] * taille  # État de chaque partie du navire (touché ou non).

    def est_coule(self):
        """
        Vérifie si le navire est complètement coulé.
        
        :return: True si toutes les parties du navire sont touchées, sinon False.
        """
        return all(self.touche)

    def placer(self, positions):
        """
        Place le navire à des positions spécifiques sur la grille.
        
        :param positions: Liste des tuples représentant les positions (x, y) du navire.
        """
        self.positions = positions

    def verifier_tir(self, position):
        """
        Vérifie si une position donnée touche le navire.
        
        :param position: Tuple (x, y) représentant la position du tir.
        :return: True si le tir touche le navire, sinon False.
        """
        if position in self.positions:
            index = self.positions.index(position)
            self.touche[index] = True
            return True
        return False
