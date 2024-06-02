from Navire import Navire
from Joueur import Joueur


class Jeu:
    def __init__(self, joueur1, joueur2):
        """
        Initialise le jeu avec deux joueurs.
        
        :joueur1: Instance de la classe Joueur représentant le premier joueur.
        :joueur2: Instance de la classe Joueur représentant le second joueur.
        """
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.tour = joueur1  # Le jeu commence avec le joueur1.

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
        return all(navires.est_coule() for navires in self.joueur1.grille_personnelle.navires) or \
               all(navires.est_coule() for navires in self.joueur2.grille_personnelle.navires)

    def jouer(self):
        """
        Lance la boucle principale du jeu où les joueurs tirent à tour de rôle jusqu'à ce qu'un joueur gagne.
        """
        while not self.est_fini():
            print(f"Tour de {self.tour.nom}")
            x = int(input("Entrer la coordonnée x: "))
            y = int(input("Entrer la coordonnée y: "))
            position = (x, y)
            if self.tour == self.joueur1:
                self.joueur1.tirer(position, self.joueur2)
            else:
                self.joueur2.tirer(position, self.joueur1)
            self.changer_tour()
        print("Jeu terminé! Le gagnant est " + ("joueur1" if all(navire.est_coule() for navire in self.joueur2.grille_personnelle.navires) else "joueur2") + " !")

# Exemple de création de jeu
joueur1 = Joueur("Alice")
joueur2 = Joueur("Bob")


# Création de navires
navire1 = Navire(5, "Porte-avions")
navire2 = Navire(4, "Cuirassé")

# Placement des navires sur les grilles des joueurs
joueur1.placer_navire(navire1, [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)])
joueur2.placer_navire(navire2, [(1, 0), (1, 1), (1, 2), (1, 3)])

# Création et lancement du jeu
jeu = Jeu(joueur1, joueur2)
jeu.jouer()
