import pygame
from moviepy.editor import VideoFileClip
import numpy as np
import math

import sys
import random
import time
import os




#importation des class et methode 
from affichge_ecran import *
from Menu import *
# from game_final import  *



if __name__ == "__main__":
    menu = Menu(["Jouer", "Options", "Quitter"])
    ecran_jeu = EcranJeu()
    # ecran_jeu_1 = configurer_jeu()
    ecran_options = EcranOptions()
    ecran_chargement = EcranChargement()  # Ajout d'une instance de la classe EcranChargement

    ecran_actuel = "Menu"
    ecran_jeu = EcranJeu()# Ajout de l'instance de la classe Jeu

    while True:
        if ecran_actuel == "Menu":
            menu.afficher()

        elif ecran_actuel == "Jeu":
            if ecran_chargement.video_terminee():
                ecran_jeu.afficher()  # Afficher le jeu JeuJcJ lorsque ecran_actuel est "Jeu"
            else:
                ecran_chargement.afficher()

        elif ecran_actuel == "Jouer":
            if ecran_chargement.video_terminee():
                ecran_jeu.jouer()  # Afficher le jeu lorsque ecran_actuel est "Jeu"
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
