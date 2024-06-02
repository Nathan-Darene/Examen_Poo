class Grille:
    def __init__(self, taille=10):
        """
        Initialise une grille de jeu de taille spécifiée (par défaut 10x10).
        
        : taille : Taille de la grille (taille x taille).
        """
        self.taille = taille
        self.navires = []  # Liste des navires placés sur la grille.
        self.tirs = []  # Liste des tirs reçus.

    """Déclaration de la méthode
    # self : fait référence à l'instance de la classe qui contient cette méthode.
    # navire : est une instance de la classe Navire.
    # positions : est une liste de tuples représentant les positions (x, y) où le navire doit être placé sur la grille."""
    def ajouter_navire(self, navire, positions):
        """
        Ajoute un navire à la grille à des positions spécifiques.
        
        :parametre navire: Instance de la classe Navire.
        :parametre positions: Liste des tuples représentant les positions (x, y) du navire.
        :raises ValueError: Si les positions sont en dehors de la grille.
        """
        if all(0 <= x < self.taille and 0 <= y < self.taille for x, y in positions):
            # 0 <= x : Cette partie vas vérifie  que x est supérieur ou égal à 0 en gros x ne doit pas être un nombre négatif.
            # x < self.taille : Cette partie vérifie que x est strictement inférieur à self.taille. Cela garantit que x est dans les limites de la taille spécifiée par self.taille.
            navire.placer(positions)
            self.navires.append(navire)
        else:
            raise ValueError("Positions izvalides pour le navire.")

    def recevoir_tir(self, position):
        """
        Gère la réception d'un tir à une position spécifique.
        
        :param position: Tuple (x, y) représentant la position du tir.
        :return: True si le tir touche un navire, sinon False.
        """
        self.tirs.append(position)
        for navire in self.navires:
            if navire.verifier_tir(position):
                if navire.est_coule():
                    print(f"{navire.nom} coulé!")
                else:
                    print(f"{navire.nom} touché!")
                return True
        print("À l'eau!")
        return False
