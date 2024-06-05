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
        lettres = "     | " + " | " .join(chr(ord('A') + i) for i in range(10))+" |"
        # for i in range(10):
        #     lettres += chr(ord('A') + i) + " | "
            
        print(lettres)
        # Affichage des lignes séparatrices
        separateur = "  " + "+".join(["---"] * 11)+ "+"
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


#Explication du code de la class Grille

# ord(): La fonction ord() retourne le point de code Unicode de son argument
        # Ici, 'A' est un caractère et son point de code Unicode est 65. En Python, 
        # les lettres majuscules sont attribuées des codes Unicode consécutifs, 
        # donc le point de code Unicode de 'B' est 66, celui de 'C' est 67, et ainsi de suite.

# ord('A') + i: Cette expression ajoute la valeur i à 65, ce qui revient à augmenter le code Unicode 
        # de la lettre 'A' par la valeur de i. Ainsi, lorsque i est 0, cela donne 65 (le code Unicode de 'A'), 
        # lorsque i est 1, cela donne 66 (le code Unicode de 'B'), et ainsi de suite. Cela permet de générer 
        # les codes Unicode successifs pour les lettres de A à J.

# chr(...): La fonction chr() retourne la chaîne représentant un caractère dont le code Unicode est le nombre entier passé en argument. 
        # Ainsi, chr(ord('A') + i) convertit le code Unicode calculé en caractère correspondant. 
        # Par exemple, lorsque i est 0, cela donnera 'A', lorsque i est 1, cela donnera 'B', et ainsi de suite jusqu'à 'J'.

# En résumé, chr(ord('A') + i) est une expression qui génère les lettres de A à J en utilisant les codes Unicode des lettres majuscules consécutives.

# .join(): La méthode join() en Python est utilisée pour concaténer une séquence de chaînes de caractères en une seule chaîne de caractères. 
# Exemple : 
# separateur = ", "
# sequence = ["a", "b", "c", "d"]
# resultat = separateur.join(sequence)
# print(resultat)

# resultat: a, b, c, d
