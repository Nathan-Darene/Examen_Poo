class Grille:
    def __init__(self):
        self.grille = [[0] * 10 for _ in range(10)]
        self.bateaux = []

    def ajouter_bateau(self, bateau, positions):
        for (x, y) in positions:
            self.grille[x][y] = bateau.taille
        bateau.placer(positions)
        self.bateaux.append(bateau)

    def afficher(self):
        for ligne in self.grille:
            print(" ".join(str(x) for x in ligne))

    def recevoir_tir(self, x, y):
        if self.grille[x][y] == 0:
            return "À l'eau"
        elif self.grille[x][y] == 6:
            return "Déjà touché"
        else:
            for bateau in self.bateaux:
                if bateau.est_touche((x, y)):
                    self.grille[x][y] = 6
                    if bateau.est_coule():
                        return f"Coulé {bateau.nom}"
                    return "Touché"
