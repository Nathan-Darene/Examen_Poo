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