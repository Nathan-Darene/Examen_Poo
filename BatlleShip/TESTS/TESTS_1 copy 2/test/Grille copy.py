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
        # Affichage des lettres en haut
        lettres = "     | " + " | ".join(chr(ord('A') + i) for i in range(10)) +" |"
        print(lettres)
        # Affichage des lignes séparatrices
        separateur = "  " + "+".join(["---"] * 11)
        print(separateur)
        # Affichage de la grille avec les chiffres sur le côté
        for i, ligne in enumerate(self.grille):
            print(f"{i+1:2} | " + " |".join(str(x) for x in ligne) + " |")
            print(separateur)

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
