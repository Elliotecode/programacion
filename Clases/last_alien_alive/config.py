"""
declarar en este archivo todas las variales globales del juego
"""
import pygame
import random
pygame.init()
ANCHO_PANTALLA = 800
ALTO_PANTALLA = 600
pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))

jugador = pygame.image.load("Clases/juego/assets/alien_blano.png").convert_alpha()
jugador = pygame.transform.scale(jugador, (30, 30))  # Nuevo tamaño: 25x25 píxeles

jugador_caminando = pygame.image.load("Clases/juego/assets/alien_move.png").convert_alpha()
jugador_caminando = pygame.transform.scale(jugador_caminando, (30, 30))  # Nuevo tamaño: 25x25 píxeles

#titulo de la ventana
pygame.display.set_caption("juegos de habilidad: lineas dañinas")

#color de fondo
color_fondo = (25, 0, 0)
FONDO = pygame.image.load("Clases/juego/assets/espacioooooo.jpg").convert()

#FUENTE
FUENTE = pygame.font.SysFont("Arial", 30)  # FUENTE de texto

vidas = 5
juego_terminado = False
INTERVALO_CREACION = 1000  # Intervalo de creación de líneas fantasma en milisegundos
INTERVALO_DE_DESVANECIMIENTO = 3000  # Intervalo de desvanecimiento de líneas reales en milisegundos
INTERVALO_ANIMACION_JUGADOR = 100  #  de animación del jugador en milisegundos
ultimo_tiempo_animacion = 0
TIEMPO_LINEA_REAL = 5000
FPS = 60  # frames por segundo
reloj = pygame.time.Clock()
linea_creada_real = False
ultimo_tiempo_creacion = 0
ocupados = []  # Lista para rastrear las posiciones ocupadas por líneas fantasma
valores = []