import pygame

pygame.init()
pygame.font.init()

#variables globales ;)
ANCHO_PANTALLA = 800
ALTO_PANTALLA = 600
pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
FPS = 60  # frames por segundok

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
hora_de_muerte = None
game_over = False
jugador_moviendose = False

#rutas de assets

FONDO = pygame.image.load("assets/espaciooooooooo.png").convert()

sonido_laser = pygame.mixer.Sound("assets/starwars.mp3")
sonido_colision = pygame.mixer.Sound("assets/golpe_por_sable.mp3")
sonido_muerte = pygame.mixer.Sound("assets/destruccion.mp3")
sonido_movimiento = pygame.mixer.Sound("assets/huida.mp3")

jugador = pygame.image.load("assets/alien_blano.png").convert_alpha()
jugador = pygame.transform.scale(jugador, (30, 30))  # Nuevo tamaño: 25x25 píxeles
jugador_caminando = pygame.image.load("assets/alien_move.png").convert_alpha()
jugador_caminando = pygame.transform.scale(jugador_caminando, (30, 30))  # Nuevo tamaño: 25x25 píxeles
exp1 = pygame.image.load("assets/explosion/exp1.png").convert_alpha()
exp2 = pygame.image.load("assets/explosion/exp2.png").convert_alpha()
exp3 = pygame.image.load("assets/explosion/exp3.png").convert_alpha()
exp4 = pygame.image.load("assets/explosion/exp4.png").convert_alpha()
exp5 = pygame.image.load("assets/explosion/exp5.png").convert_alpha()
exp6 = pygame.image.load("assets/explosion/exp6.png").convert_alpha()
exp7 = pygame.image.load("assets/explosion/exp7.png").convert_alpha()
exp8 = pygame.image.load("assets/explosion/exp8.png").convert_alpha()