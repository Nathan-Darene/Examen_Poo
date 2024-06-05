class Bateau:
    def __init__(self, nom, taille):
        self.nom = nom
        self.taille = taille
        self.positions = []
        self.touches = 0

    def placer(self, positions):
        self.positions = positions

    def est_touche(self, position):
        if position in self.positions:
            self.touches += 1
            return True
        return False

    def est_coule(self):
        return self.touches == self.taille
