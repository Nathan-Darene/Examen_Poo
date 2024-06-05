import random

class Grille:
    def __init__(self):
        self.grille = [[0] * 10 for _ in range(10)]
        self.tirs_rates = [[False] * 10 for _ in range(10)]
        self.bateaux = []

    def ajouter_bateau(self, bateau, positions):
        for (x, y) in positions:
            self.grille[x][y] = bateau.taille
        bateau.placer(positions)
        self.bateaux.append(bateau)

    def verifier_positions_bateau(self, positions):
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
                self.ajouter_bateau(bateau, positions)
                break

    def recevoir_tir(self, x, y):
        if self.grille[x][y] == 0:
            self.tirs_rates[x][y] = True  # Marque comme tir raté
            return "À l'eau"
        elif self.grille[x][y] == "X" or self.tirs_rates[x][y]:
            return "Déjà touché"
        else:
            for bateau in self.bateaux:
                if bateau.est_touche((x, y)):
                    self.grille[x][y] = "X"
                    if bateau.est_coule():
                        return f"{bateau.nom} Coulé"
                    return bateau.taille
