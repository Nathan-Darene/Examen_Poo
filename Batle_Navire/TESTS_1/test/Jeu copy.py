import random

from Batle_Navire.TESTS_1.Grille import *
from Bateau import *
# from Joueur import *
# from IA import *
class Jeu:
    def __init__(self):
        self.grille_joueur = Grille()
        self.grille_ordinateur = Grille()
        self.bateaux = [
            ("Porte-avions", 5),
            ("Croiseur", 4),
            ("Contre-torpilleur", 3),
            ("Sous-marin", 3),
            ("Torpilleur", 2)
        ]

    def placer_bateaux_aleatoire(self, grille):
        for nom, taille in self.bateaux:
            place = False
            while not place:
                orientation = random.choice(["horizontal", "vertical"])
                if orientation == "horizontal":
                    x = random.randint(0, 9)
                    y = random.randint(0, 9 - taille)
                    positions = [(x, y + i) for i in range(taille)]
                else:
                    x = random.randint(0, 9 - taille)
                    y = random.randint(0, 9)
                    positions = [(x + i, y) for i in range(taille)]
                if all(grille.grille[x][y] == 0 for (x, y) in positions):
                    grille.ajouter_bateau(Bateau(nom, taille), positions)
                    place = True

    def jouer(self):
        self.placer_bateaux_aleatoire(self.grille_joueur)
        self.placer_bateaux_aleatoire(self.grille_ordinateur)
        tour_joueur = True
        while True:
            if tour_joueur:
                print("Votre grille :")
                self.grille_joueur.afficher()
                coup = input("Entrez la position (ex: B3) pour tirer: ").upper()
                y = ord(coup[0]) - 65
                x = int(coup[1:]) - 1
                if 0 <= x < 10 and 0 <= y < 10:
                    resultat = self.grille_ordinateur.recevoir_tir(x, y)
                    print(resultat)
                else:
                    print("Coordonnées invalides. Essayez encore.")
            else:
                x = random.randint(0, 9)
                y = random.randint(0, 9)
                resultat = self.grille_joueur.recevoir_tir(x, y)
                print(f"L'ordinateur tire en {chr(65+y)}{x+1} : {resultat}")
            tour_joueur = not tour_joueur
