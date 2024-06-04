import random
from Grille import *
from Bateau import *
# from Joueur import *
# from IA import *
class Jeu:
    def __init__(self):
        self.grille_joueur = Grille()
        self.grille_ia = Grille()
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

    def afficher_grilles(self):
        separateur = "     +" + "+".join(["---"] * 10) + "+"
        print("")
        print("\t\tGrille du joueur:".center(30) + " " * 10 + "\t\t\t Grille de l'IA:".center(30))
        print("")
        lettres = "       " + " | ".join(chr(ord('A') + i) for i in range(10))
        print(lettres + " " * 10 + lettres)
        print(separateur + " " * 10 + separateur)
        for i in range(10):
            ligne_joueur = f"{i+1:2}   | " + " | ".join(str(x) for x in self.grille_joueur.grille[i]) + " |"
            ligne_ia = f"{i+1:2}   | " + " | ".join(str(x) if x == 6 else " " for x in self.grille_ia.grille[i]) + " |"
            print(ligne_joueur + " " * 10 + ligne_ia)
            print(separateur + " " * 10 + separateur)

    def jouer(self):
        self.placer_bateaux_aleatoire(self.grille_joueur)
        self.placer_bateaux_aleatoire(self.grille_ia)
        tour_joueur = True
        while True:
            self.afficher_grilles()
            if tour_joueur:
                print("C'est à votre tour de jouer.")
                coup = input("Entrez la position (ex: B3) pour tirer: ").upper()
                y = ord(coup[0]) - 65
                x = int(coup[1:]) - 1
                if 0 <= x < 10 and 0 <= y < 10:
                    resultat = self.grille_ia.recevoir_tir(x, y)
                    print(resultat)
                else:
                    print("Coordonnées invalides. Essayez encore.")
            else:
                print("Tour de l'IA...")
                x = random.randint(0, 9)
                y = random.randint(0, 9)
                resultat = self.grille_joueur.recevoir_tir(x, y)
                print(f"L'IA tire en {chr(65+y)}{x+1} :\n >> {resultat}")
            tour_joueur = not tour_joueur
