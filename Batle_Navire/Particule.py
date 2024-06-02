import pygame
from affichge_ecran import *
from moviepy.editor import VideoFileClip
import numpy as np
import math
import sys
import random
import time
import os



class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = random.randint(5, 15)
        self.color = OR  # Couleur des particules
        self.speed_x = random.uniform(-1, 1)
        self.speed_y = random.uniform(-1, 1)
        self.life = 100  # Durée de vie des particules

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.life -= 1
        self.size -= 0.1

    def draw(self, screen):
        if self.life > 0:
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), int(self.size))



class ParticleManager:
    def __init__(self):
        self.particles = []

    def add_particle(self, x, y):
        self.particles.append(Particle(x, y))

    def update(self):
        for particle in self.particles[:]:
            particle.update()
            if particle.life <= 0:
                self.particles.remove(particle)

    def draw(self, screen):
        for particle in self.particles:
            particle.draw(screen)