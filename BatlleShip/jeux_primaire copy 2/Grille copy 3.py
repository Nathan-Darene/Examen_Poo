import random

class Grille:
    def __init__(self):
        self.grille = [[0] * 10 for _ in range(10)]
        self.bateaux = []

    def ajouter_bateau(self, bateau, positions):
        for (x, y) in positions:
            self.grille[x][y] = bateau.taille
        bateau.placer(positions)
        self.bateaux.append(bateau)

    def verifier_positions_bateau(self, positions):
        # Vérifie si les positions des bateaux respectent l'espacement
        for (x, y) in positions:
            if self.grille[x][y] != 0:
                return False
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if 0 <= x + dx < 10 and 0 <= y + dy < 10:
                        if self.grille[x + dx][y + dy] != 0:
                            return False
        return True

    def placer_bateau_avec_espacement(self, bateau):
        # Place un bateau sur la grille en tenant compte de l'espacement
        espacement = 1
        while True:
            orientation = random.choice(["horizontal", "vertical"])
            if orientation == "horizontal":
                x = random.randint(0, 9)
                y = random.randint(0, 9 - bateau.taille)
                positions = [(x, y + i) for i in range(bateau.taille)]
            else:
                x = random.randint(0, 9 - bateau.taille)
                y = random.randint(0, 9)
                positions = [(x + i, y) for i in range(bateau.taille)]
            if self.verifier_positions_bateau(positions):
                # Ajoute un espace vide autour du bateau
                for (x, y) in positions:
                    for dx in range(-1, 2):
                        for dy in range(-1, 2):
                            if 0 <= x + dx < 10 and 0 <= y + dy < 10:
                                self.grille[x + dx][y + dy] = 0
                self.ajouter_bateau(bateau, positions)
                break

    def afficher(self):
        lettres = "       " + "   ".join(chr(ord('A') + i) for i in range(10))
        print(lettres)
        separateur = "     +" + "+".join(["---"] * 10) + "+"
        print(separateur)
        for i, ligne in enumerate(self.grille):
            ligne_affichage = f"{i+1:2}   | "
            for case in ligne:
                if case == "X":
                    ligne_affichage += "X"
                elif case == -1:
                    ligne_affichage += "0"
                else:
                    ligne_affichage += " " if case == 0 else str(case)
                ligne_affichage += " | "
            print(ligne_affichage)
            print(separateur)

    def recevoir_tir(self, x, y):
        if self.grille[x][y] == 0:
            self.grille[x][y] = -1  # Marquer comme tir raté
            return "À l'eau"
        elif self.grille[x][y] == "X" or self.grille[x][y] == -1:
            return "Déjà touché"
        else:
            for bateau in self.bateaux:
                if bateau.est_touche((x, y)):
                    self.grille[x][y] = "X"
                    if bateau.est_coule():
                        return f"{bateau.nom} Coulé"
                    return bateau.taille
