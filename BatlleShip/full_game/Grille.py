from Bateau import*

class Grille:
    def __init__(self):
        self.grille = [[0 for _ in range(10)] for _ in range(10)]

    def ajouter_bateau(self, bateau, positions):
        for x, y in positions:
            self.grille[x][y] = bateau

    def recevoir_tir(self, x, y):
        if self.grille[x][y] == 0:
            self.grille[x][y] = "O"
            return "manqué"
        elif isinstance(self.grille[x][y], Bateau):
            self.grille[x][y] = "X"
            return "touché"
        else:
            return "déjà visé"
