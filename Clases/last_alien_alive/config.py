import pygame

pygame.init()
pygame.font.init()

#variables globales ;)
ANCHO_PANTALLA = 800
ALTO_PANTALLA = 600
pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
FPS = 60  # frames por segundo

#color de fondo
COLOR_FONDO = (25, 0, 0)

#FUENTE
FUENTE = pygame.font.SysFont("Arial", 30)  # FUENTE de texto

#variables de juego
vidas = 5
INTERVALO_CREACION = 1000  # Intervalo de creación de líneas fantasma en milisegundos
INTERVALO_DE_DESVANECIMIENTO = 3000  # Intervalo de desvanecimiento de líneas reales en milisegundos
INTERVALO_ANIMACION_JUGADOR = 100  #  de animación del jugador en milisegundos
TIEMPO_LINEA_REAL = 5000

#rutas de assets
FONDO = pygame.image.load("assets/espacioooooo.jpg").convert()
jugador = pygame.image.load("assets/alien_blano.png").convert_alpha()
jugador = pygame.transform.scale(jugador, (30, 30))  # Nuevo tamaño: 25x25 píxeles
jugador_caminando = pygame.image.load("Clases/juego/assets/alien_move.png").convert_alpha()
jugador_caminando = pygame.transform.scale(jugador_caminando, (30, 30))  # Nuevo tamaño: 25x25 píxeles

#level 0
velocidad_linea_f_V = 0.0625
intervalo = 1000
desvanecimiento = 3000

#level 1
velocidad_linea_f_V_1 = 0.0625
intervalo_1 = 800
desvanecimiento_1 = 2500

def niveles (nivel): 
    return INTERVALO_CREACION, INTERVALO_DE_DESVANECIMIENTO, velocidad_linea_f_V