import pygame

class Level_Manager:
    def __init__(self):
        self.ultimo_cambio = pygame.time.get_ticks()
        self.duracion = 30000
        