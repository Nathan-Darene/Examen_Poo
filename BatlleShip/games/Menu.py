import pygame
from affichge_ecran import *
from moviepy.editor import VideoFileClip
from pydub import AudioSegment
import numpy as np
import math
import sys
import random
import time
import os

class Menu:
    def __init__(self, options):
        self.options = options
        self.selected_option = 0
        # Chargez votre image de fond
        self.background = pygame.image.load("image/assets/compass-3408928_1920.jpg").convert()
        # Redimensionnez l'image pour correspondre à la taille de la fenêtre
        self.background = pygame.transform.scale(self.background, (largeur, hauteur))
        # Charger le son de sélection
        self.son_selection = pygame.mixer.Sound("sounds/pirate.mp3")

        

    def afficher(self):
        # Affichez l'image de fond à la place de la couleur de fond
        fenetre.blit(self.background, (0, 0))
        # Le reste de votre fonction d'affichage reste inchangé
        self._afficher_titre()
        self._afficher_options()
        # Jouer le son de sélection lors de l'affichage du menu
        self.son_selection.play()
        pygame.display.flip()

    def _afficher_titre(self):
        chemin_police = "font/font_7/ka1.ttf"
        chemin_police1 = "BatlleShip/assets/fonts/game_of_squids/Game Of Squids.ttf"
        chemin_police2 = "BatlleShip/assets/fonts/handwriting_draft/handwriting-draft_free-version.ttf"
        chemin_police3 = "BatlleShip/assets/fonts/sketch_gothic_school/Sketch Gothic School.ttf"
        chemin_police4 = "BatlleShip/assets/fonts/madina/Madina.ttf"

        #taille  et police du texte
        taille_police_0 = 80
        police_0 = pygame.font.Font(chemin_police4, taille_police_0)  # Chargement de la police depuis le chemin spécifié

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
        first_surface = police_0.render("Encadreur : Docteur Diaby", True, NOIR)
        #texte1
        titre_surface = police.render("BattleShip Game", True, NOIR)
        #texte2
        createur = police_1.render("Create By ", True, NOIR)
        #texte3
        auteur = police_2.render("N'Guesan & Sana", True, NOIR)

        #position du texte
        first_surface_rect = first_surface.get_rect()
        titre_rect = titre_surface.get_rect()
        createur_rect = createur.get_rect()
        auteur_rect = auteur.get_rect()


        #position du texte
        first_surface_rect.center = (largeur // 6.5, 70) 
        titre_rect.center = (largeur // 1.3, 160)
        createur_rect.center = (largeur // 1.3, 250)
        auteur_rect.center = (largeur // 1.3, 350)


        #affiche du texte
        fenetre.blit(first_surface, first_surface_rect)
        fenetre.blit(titre_surface ,titre_rect)
        fenetre.blit(createur ,createur_rect)
        fenetre.blit(auteur ,auteur_rect)


    def _afficher_options(self):
        chemin_police = "BatlleShip/assets/fonts/handwriting_draft/handwriting-draft_free-version.ttf"
        taille_police = 70
        police = pygame.font.Font(chemin_police, taille_police)
        for i, option_texte in enumerate(self.options):
            couleur = NOIR if i != self.selected_option else MARRON_1
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
