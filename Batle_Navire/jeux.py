import pygame
from moviepy.editor import VideoFileClip
import numpy as np
import math
import sys
import random
import time
import os

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
MARRON_CLAIR = (240, 217, 181)
MARRON = (181, 136, 98)
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)
FOND=(255,221,204)
FOND1=(4,5,8,255)
FOND2=(31,37,40,255)
OR = (255,215,0)
ORANGE = (214, 125, 8)
NOIR_DOUCE = (29, 29, 28)
# Taille de la fenêtre
largeur, hauteur = 1920, 1080
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("BattleShip")

# Police de texte
police = pygame.font.SysFont(None, 40)

# Son
pygame.mixer.init()
effet="sounds/choix.mp3"
effet_1 = "sounds/choix2.mp3"
effet_2 = "sounds/choix3.mp3"
effet_3 = "sounds/choix4.mp3"
effet_4 = "sounds/choix5.mp3"
effet_5 = "sounds/choix6.mp3"
effet_6 = "sounds/choix7.mp3"



son_selection = pygame.mixer.Sound(effet)
son_selection_move = pygame.mixer.Sound(effet_2)
son_selection_capture2 = pygame.mixer.Sound(effet_5)


# Modifiez votre classe Menu pour inclure une image de fond
class Menu:
    def __init__(self, options):
        self.options = options
        self.selected_option = 0
        # Chargez votre image de fond
        self.background = pygame.image.load("image/assets/compass-3408928_1920.jpg").convert()
        # Redimensionnez l'image pour correspondre à la taille de la fenêtre
        self.background = pygame.transform.scale(self.background, (largeur, hauteur))

    def afficher(self):
        # Affichez l'image de fond à la place de la couleur de fond
        fenetre.blit(self.background, (0, 0))
        # Le reste de votre fonction d'affichage reste inchangé
        self._afficher_titre()
        self._afficher_options()
        pygame.display.flip()

    def _afficher_titre(self):
        chemin_police = "font/font_7/ka1.ttf"
        chemin_police1 = "assets/fonts/game_of_squids/Game Of Squids.ttf"
        chemin_police2 = "assets/fonts/handwriting_draft/handwriting-draft_free-version.ttf"
        chemin_police3 = "assets/fonts/sketch_gothic_school/Sketch Gothic School.ttf"
        chemin_police4 = "assets/fonts/Valorant_Font/Valorant_Font.ttf"

#taille  et police du texte
        # taille_police_0 = 50
        # police_0 = pygame.font.Font(chemin_police2, taille_police_0)  # Chargement de la police depuis le chemin spécifié

        #taille  et police du texte1
        taille_police = 90
        police = pygame.font.Font(chemin_police2, taille_police)  # Chargement de la police depuis le chemin spécifié

        #taille  et police du texte2
        taille_police_1 = 50
        police_1 = pygame.font.Font(chemin_police2, taille_police_1)  # Chargement de la police depuis le chemin spécifié

        #taille  et police du texte3
        taille_police_2 = 50
        police_2 = pygame.font.Font(chemin_police2, taille_police_2)  # Chargement de la police depuis le chemin spécifié

        #texte
        # first_surface = police_0.render("WELCOM TO", True, NOIR)
        
        #texte1
        titre_surface = police.render("BattleShip Game", True, NOIR)
        #texte2
        createur = police_1.render("Create By ", True, NOIR)
        #texte3
        auteur = police_2.render("Nathan & Sana", True, NOIR)

        #position du texte
        # first_surface_rect = first_surface.get_rect()
        titre_rect = titre_surface.get_rect()
        createur_rect = createur.get_rect()
        auteur_rect = auteur.get_rect()


        #position du texte
        # first_surface_rect.center = (largeur // 2, 50) 
        titre_rect.center = (largeur // 1.3, 160)
        createur_rect.center = (largeur // 1.3, 250)
        auteur_rect.center = (largeur // 1.3, 350)


        #affiche du texte
        # fenetre.blit(first_surface, first_surface_rect)
        fenetre.blit(titre_surface ,titre_rect)
        fenetre.blit(createur ,createur_rect)
        fenetre.blit(auteur ,auteur_rect)


    def _afficher_options(self):
        chemin_police = "assets/fonts/handwriting_draft/handwriting-draft_free-version.ttf"
        taille_police = 70
        police = pygame.font.Font(chemin_police, taille_police)
        for i, option_texte in enumerate(self.options):
            couleur = NOIR if i != self.selected_option else VERT
            self._afficher_texte(option_texte, largeur // 1.3, 500 + i * 100, couleur,police)

    def _afficher_texte(self, texte, x, y, couleur,police):
        texte_surface = police.render(texte, True, couleur)
        texte_rect = texte_surface.get_rect()
        texte_rect.center = (x, y)
        fenetre.blit(texte_surface, texte_rect)

    def selectionner_option_suivante(self):
        self.selected_option = (self.selected_option + 1) % len(self.options)
        son_selection.play()  # Jouer le son de sélection

    def selectionner_option_precedente(self):
        self.selected_option = (self.selected_option - 1) % len(self.options)
        son_selection.play()  # Jouer le son de sélection

    def executer_action(self):
        option = self.options[self.selected_option]
        if option == "Jouer":
            return "Jeu"
        elif option == "Options":
            return "Options"
        elif option == "Quitter":
            pygame.quit()
            sys.exit()

# class Particle:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.size = random.randint(5, 15)
#         self.color = OR  # Couleur des particules
#         self.speed_x = random.uniform(-1, 1)
#         self.speed_y = random.uniform(-1, 1)
#         self.life = 100  # Durée de vie des particules

#     def update(self):
#         self.x += self.speed_x
#         self.y += self.speed_y
#         self.life -= 1
#         self.size -= 0.1

#     def draw(self, screen):
#         if self.life > 0:
#             pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), int(self.size))



# class ParticleManager:
#     def __init__(self):
#         self.particles = []

#     def add_particle(self, x, y):
#         self.particles.append(Particle(x, y))

#     def update(self):
#         for particle in self.particles[:]:
#             particle.update()
#             if particle.life <= 0:
#                 self.particles.remove(particle)

#     def draw(self, screen):
#         for particle in self.particles:
#             particle.draw(screen)


class EcranJeu:
    def __init__(self):
        self.message = "Jeu en cours..."

    def afficher(self):
        fenetre.fill(BLANC)
        self._afficher_message()
        pygame.display.flip()

    def _afficher_message(self):
        message_surface = police.render(self.message, True, NOIR)
        message_rect = message_surface.get_rect()
        message_rect.center = (largeur // 2, hauteur // 2)
        fenetre.blit(message_surface, message_rect)



class EcranChargement:
    def __init__(self):
        char1 = "video/,-556022149_small.mp4"
        char2 = "video/6824-196344457_small.mp4"
        char3 = "video/49740-459802154_small.mp4"
        char4 = "video/111036-689918641_small.mp4"
        char5 = "video/112264-693798391_small.mp4"
        
        self.video = VideoFileClip(char5)
        self.video_surface = pygame.Surface((self.video.size[0], self.video.size[1])).convert()
        self.video.set_duration(30)  # Définition de la durée de la vidéo à 30 secondes
        self.video.set_position(("center", "center"))
        self.video.set_audio(None)  # Désactivation de l'audio de la vidéo
        self.start_time = pygame.time.get_ticks()  # Temps de démarrage de l'affichage de la vidéo
        self.loop_count = 0  # Initialisation du compteur de boucles

    def afficher(self):
        fenetre.fill(FOND2)
        # Calcul de l'instant actuel dans la vidéo en secondes
        video_time = (pygame.time.get_ticks() - self.start_time) / 1000
        # Vérification si le temps écoulé a atteint ou dépassé la durée de la vidéo
        if video_time >= self.video.duration:
            # Incrémenter le compteur de boucles
            self.loop_count += 1
            # Vérifier si le nombre de boucles est atteint
            if self.loop_count >= 1:
                # Arrêter la vidéo
                return
            # Réinitialiser le temps de démarrage pour afficher la vidéo en boucle
            self.start_time = pygame.time.get_ticks()
        # Obtention du cadre actuel de la vidéo
        self.video_blit = self.video.get_frame(video_time % self.video.duration)  # Utiliser le reste de la division pour boucler la vidéo
        self.video_surface.blit(pygame.image.frombuffer(self.video_blit, self.video.size, 'RGB'), (0, 0))
        fenetre.blit(self.video_surface, (0, 0))
        pygame.display.flip()

    def video_terminee(self):
        # La vidéo est considérée comme terminée après avoir bouclé trois fois
        return self.loop_count >= 1



class EcranOptions:
    def __init__(self):
        self.message = "Options"
        self.bouton_retour = pygame.Rect(20, 20, 100, 40)

    def afficher(self):
        fenetre.fill(BLANC)
        self._afficher_message()
        self._afficher_bouton_retour()
        pygame.display.flip()

    def _afficher_message(self):
        message_surface = police.render(self.message, True, NOIR)
        message_rect = message_surface.get_rect()
        message_rect.center = (largeur // 2, 100)
        fenetre.blit(message_surface, message_rect)

    def _afficher_bouton_retour(self):
        pygame.draw.rect(fenetre, ROUGE, self.bouton_retour)
        texte_surface = police.render("Retour", True, BLANC)
        texte_rect = texte_surface.get_rect()
        texte_rect.center = self.bouton_retour.center
        fenetre.blit(texte_surface, texte_rect)

    def verifier_clic_retour(self, pos):
        if self.bouton_retour.collidepoint(pos):
            return True
        return False

if __name__ == "__main__":
    menu = Menu(["Jouer", "Options", "Quitter"])
    ecran_jeu = EcranJeu()
    ecran_options = EcranOptions()
    ecran_chargement = EcranChargement()  # Ajoutez une instance de la classe EcranChargement

    ecran_actuel = "Menu"
    ecran_jeu = EcranJeu()# Ajout de l'instance de la classe Jeu

    while True:
        if ecran_actuel == "Menu":
            menu.afficher()

        elif ecran_actuel == "Jeu":
            if ecran_chargement.video_terminee():
                ecran_jeu.jouer()  # Afficher le jeu JeuJcJ lorsque ecran_actuel est "Jeu"
            else:
                ecran_chargement.afficher()

        elif ecran_actuel == "Jouer":
            if ecran_chargement.video_terminee():
                ecran_jeu.jouer()  # Afficher le jeu JeuJcJ lorsque ecran_actuel est "Jeu"
            else:
                ecran_chargement.afficher()
        elif ecran_actuel == "Options":
            ecran_options.afficher()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if ecran_actuel == "Menu":
                    if event.key == pygame.K_DOWN:
                        menu.selectionner_option_suivante()
                    elif event.key == pygame.K_UP:
                        menu.selectionner_option_precedente()
                    elif event.key == pygame.K_RETURN:
                        ecran_actuel = menu.executer_action()
                elif ecran_actuel == "Jeu":
                    if event.key == pygame.K_ESCAPE:
                        ecran_actuel = "Menu"
                elif ecran_actuel == "jeu_JcIA":
                    if event.key == pygame.K_ESCAPE:
                        ecran_actuel = "Menu"
                elif ecran_actuel == "Options":
                    if event.key == pygame.K_ESCAPE:
                        ecran_actuel = "Menu"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if ecran_actuel == "Menu":
                    if event.button == 1:  # Clic gauche de la souris
                        if 250 <= event.pos[1] <= 320:
                            ecran_actuel = menu.executer_action()
                        elif 320 < event.pos[1] <= 390:
                            ecran_actuel = "Options"
                        elif 390 < event.pos[1] <= 460:
                            pygame.quit()
                            sys.exit()
                elif ecran_actuel == "Options":
                    if event.button == 1:  # Clic gauche de la souris
                        if ecran_options.verifier_clic_retour(event.pos):
                            ecran_actuel = "Menu"
