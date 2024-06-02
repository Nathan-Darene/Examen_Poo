import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Définition des couleurs
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Définition des dimensions de la fenêtre
TAILLE_CASE = 40
TAILLE_GRILLE = 10
LARGEUR_FENETRE = TAILLE_CASE * (TAILLE_GRILLE + 2) * 2
HAUTEUR_FENETRE = TAILLE_CASE * (TAILLE_GRILLE + 2)

# Création de la fenêtre
fenetre = pygame.display.set_mode((LARGEUR_FENETRE, HAUTEUR_FENETRE))
pygame.display.set_caption("Bataille Navale")

# Fonction pour dessiner une grille
def dessiner_grille(debut_x, debut_y):
    for x in range(TAILLE_GRILLE + 1):
        pygame.draw.line(fenetre, BLUE, (debut_x + x * TAILLE_CASE, debut_y), (debut_x + x * TAILLE_CASE, debut_y + TAILLE_GRILLE * TAILLE_CASE))
    for y in range(TAILLE_GRILLE + 1):
        pygame.draw.line(fenetre, BLUE, (debut_x, debut_y + y * TAILLE_CASE), (debut_x + TAILLE_GRILLE * TAILLE_CASE, debut_y + y * TAILLE_CASE))

# Boucle principale du jeu
def main():
    while True:
        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Remplir l'écran de blanc
        fenetre.fill(WHITE)

        # Dessiner les deux grilles
        dessiner_grille(TAILLE_CASE, TAILLE_CASE)
        dessiner_grille(TAILLE_CASE * (TAILLE_GRILLE + 2), TAILLE_CASE)

        # Afficher les labels
        font = pygame.font.SysFont(None, 36)
        label_joueur = font.render("Votre grille de jeu", True, BLACK)
        label_adversaire = font.render("La grille de l'adversaire", True, BLACK)
        fenetre.blit(label_joueur, (TAILLE_CASE, TAILLE_CASE * (TAILLE_GRILLE + 1.5)))
        fenetre.blit(label_adversaire, (TAILLE_CASE * (TAILLE_GRILLE + 2), TAILLE_CASE * (TAILLE_GRILLE + 1.5)))

        # Afficher le bouton "Jouer"
        bouton_jouer = pygame.Rect(TAILLE_CASE * (TAILLE_GRILLE + 6), TAILLE_CASE * (TAILLE_GRILLE // 2), 100, 50)
        pygame.draw.rect(fenetre, (0, 255, 0), bouton_jouer)
        label_jouer = font.render("Jouer", True, BLACK)
        fenetre.blit(label_jouer, (TAILLE_CASE * (TAILLE_GRILLE + 6) + 20, TAILLE_CASE * (TAILLE_GRILLE // 2) + 10))

        pygame.display.flip()

# Démarrer le jeu
if __name__ == "__main__":
    main()
