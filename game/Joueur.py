from Grille import Grille

class Joueur:
    def __init__(self, nom):
        """
        Initialise un joueur avec un nom spécifique.
        
        :param nom: Nom du joueur.
        """
        self.nom = nom
        self.grille_personnelle = Grille()  # Grille contenant les navires du joueur.
        self.grille_tirs = Grille()  # Grille enregistrant les tirs effectués par le joueur.

    def placer_navire(self, navire, positions):
        """
        Place un navire sur la grille personnelle du joueur.
        
        :param navire: Instance de la classe Navire.
        :param positions: Liste des tuples représentant les positions (x, y) du navire.
        """
        self.grille_personnelle.ajouter_navire(navire, positions)

    def tirer(self, position, adversaire):
        """
        Effectue un tir sur la grille de l'adversaire.
        
        :param position: Tuple (x, y) représentant la position du tir.
        :param adversaire: Instance de la classe Joueur représentant l'adversaire.
        :return: True si le tir touche un navire, sinon False.
        """
        result = adversaire.grille_personnelle.recevoir_tir(position)
        self.grille_tirs.tirs.append((position, result))
        return result
