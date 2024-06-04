class Grille:
    def __init__(self):
        # Initialisation de la grille avec des cases vides (0) pour chaque position
        self.grille = [[0] * 10 for _ in range(10)]
        # Liste pour stocker les bateaux placés sur la grille
        self.bateaux = []

    def ajouter_bateau(self, bateau, positions):
        # Place un bateau sur la grille et met à jour les positions occupées par le bateau
        for (x, y) in positions:
            self.grille[x][y] = bateau.taille
        # Ajoute le bateau à la liste des bateaux
        bateau.placer(positions)
        self.bateaux.append(bateau)

    def afficher(self):
        # Affichage des lettres des colonnes en haut de la grille
        lettres = "       " + " | ".join(chr(ord('A') + i) for i in range(10))
        print(lettres)
        # Affichage des lignes séparatrices entre les lignes de la grille
        separateur = "     +" + "+".join(["--"] * 10) + "+"
        print(separateur)
        # Affichage de chaque ligne de la grille avec les chiffres des lignes sur le côté
        for i, ligne in enumerate(self.grille):
            ligne_affichage = f"{i+1:2}   | "
            # Parcours de chaque case de la ligne
            for case in ligne:
                # Si la case est touchée mais sans bateau, affiche "0"
                if case == 0:
                    ligne_affichage += "0"
                # Si la case est touchée et contient un bateau, affiche "X"
                elif case == 6:
                    ligne_affichage += "X"
                # Sinon, affiche le numéro du bateau
                else:
                    ligne_affichage += str(case)
                ligne_affichage += " | "
            print(ligne_affichage)
            print(separateur)

    def recevoir_tir(self, x, y):
        # Vérifie si la case est vide (0)
        if self.grille[x][y] == 0:
            # Marque la case comme touchée sans bateau
            self.grille[x][y] = 0
            # Renvoie "À l'eau" pour indiquer que le tir a touché une case vide
            return "À l'eau"
        # Vérifie si la case a déjà été touchée
        elif self.grille[x][y] == 6:
            # Renvoie "Déjà touché" si la case a déjà été touchée
            return "Déjà touché"
        # Si la case contient un numéro de bateau
        else:
            # Parcourt tous les bateaux pour vérifier si l'un d'eux est touché
            for bateau in self.bateaux:
                if bateau.est_touche((x, y)):
                    # Marque la case comme touchée avec un bateau
                    self.grille[x][y] = 6
                    # Vérifie si le bateau est coulé
                    if bateau.est_coule():
                        # Renvoie le nom du beteau suivie du  mots Coulé  si le bateau est coulé
                        return f"{bateau.nom} Coulé"
                    # Renvoie la taille du bateau touché
                    return bateau.taille
