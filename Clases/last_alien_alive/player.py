"""
traer la clase jugador
"""
import pygame
import random
pygame.init()

#jugador = pygame.image.load("Clases/juego/assets/alien_blano.png").convert_alpha()
#jugador = pygame.transform.scale(jugador, (30, 30))  # Nuevo tamaño: 25x25 píxeles

#jugador_caminando = pygame.image.load("Clases/juego/assets/alien_move.png").convert_alpha()
#jugador_caminando = pygame.transform.scale(jugador_caminando, (30, 30))  # Nuevo tamaño: 25x25 píxeles
#ANCHO_PANTALLA = 800

#ALTO_PANTALLA = 600
#pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))

class Jugador:
    def __init__(self):
        self.x = 375  # Posición inicial en el centro de la pantalla
        self.y = 300
        self.ancho = 25
        self.alto = 25
        self.velocidad = 0.75
        self.color = (255, 255, 255)  # Color blanco

    #declaración de funciones
    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, self.color, (self.x, self.y, self.ancho, self.alto))

    def animar_idle(self):
        pantalla.blit(jugador, (self.x, self.y))

    def animar_walk(self):
        pantalla.blit(jugador_caminando, (self.x, self.y))

    def banderas(self):
        self.moviendose_L = False
        self.moviendose_R = False
        self.moviendose_U = False
        self.moviendose_D = False

    def mover(self, teclas):
        if teclas[pygame.K_LEFT] and self.x > 0:
            self.x -= self.velocidad
            self.moviendose_L = True
        else:
            self.moviendose_L = False
        if teclas[pygame.K_RIGHT] and self.x + self.ancho < ANCHO_PANTALLA:
            self.x += self.velocidad
            self.moviendose_R = True
        else:
            self.moviendose_R = False
        if teclas[pygame.K_UP] and self.y > 0:
            self.y -= self.velocidad
            self.moviendose_U = True
        else:
            self.moviendose_U = False
        if teclas[pygame.K_DOWN] and self.y + self.alto < ALTO_PANTALLA:
            self.y += self.velocidad
            self.moviendose_D = True
        else:
            self.moviendose_D = False