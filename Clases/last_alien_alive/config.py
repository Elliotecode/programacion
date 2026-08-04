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
vidas = 1
INTERVALO_CREACION = 1000  # Intervalo de creación de líneas fantasma en milisegundos
INTERVALO_DE_DESVANECIMIENTO = 3000  # Intervalo de desvanecimiento de líneas reales en milisegundos
INTERVALO_ANIMACION_JUGADOR = 100  #  de animación del jugador en milisegundos
TIEMPO_LINEA_REAL = 5000
hora_de_muerte = None
game_over = False
jugador_moviendose = False

#rutas de assets

FONDO = pygame.image.load("/home/elliot/Escritorio/Elliot/cosas_principales/programacion/Clases/last_alien_alive/assets/Espaciooooooooo.png").convert()

sonido_laser = pygame.mixer.Sound("/home/elliot/Escritorio/Elliot/cosas_principales/programacion/Clases/last_alien_alive/assets/starwars.mp3")
sonido_colision = pygame.mixer.Sound("/home/elliot/Escritorio/Elliot/cosas_principales/programacion/Clases/last_alien_alive/assets/golpe_por_sable.mp3")
sonido_muerte = pygame.mixer.Sound("/home/elliot/Escritorio/Elliot/cosas_principales/programacion/Clases/last_alien_alive/assets/destruccion.mp3")
sonido_movimiento = pygame.mixer.Sound("/home/elliot/Escritorio/Elliot/cosas_principales/programacion/Clases/last_alien_alive/assets/huida.mp3")

jugador = pygame.image.load("/home/elliot/Escritorio/Elliot/cosas_principales/programacion/Clases/last_alien_alive/assets/alien_blano.png").convert_alpha()
jugador = pygame.transform.scale(jugador, (30, 30))  # Nuevo tamaño: 25x25 píxeles
jugador_caminando = pygame.image.load("/home/elliot/Escritorio/Elliot/cosas_principales/programacion/Clases/last_alien_alive/assets/alien_move.png").convert_alpha()
jugador_caminando = pygame.transform.scale(jugador_caminando, (30, 30))  # Nuevo tamaño: 25x25 píxeles
exp1 = pygame.image.load("/home/elliot/Escritorio/Elliot/cosas_principales/programacion/Clases/last_alien_alive/assets/explosion/exp1.png").convert_alpha()
exp1_redi = pygame.transform.scale(exp1, (30, 30)) #ancho, alto
exp2 = pygame.image.load("/home/elliot/Escritorio/Elliot/cosas_principales/programacion/Clases/last_alien_alive/assets/explosion/exp2.png").convert_alpha()
exp2_redi = pygame.transform.scale(exp2, (50, 50)) #ancho, alto
exp3 = pygame.image.load("/home/elliot/Escritorio/Elliot/cosas_principales/programacion/Clases/last_alien_alive/assets/explosion/exp3.png").convert_alpha()
exp3_redi = pygame.transform.scale(exp3, (70, 70)) #ancho, alto
exp4 = pygame.image.load("/home/elliot/Escritorio/Elliot/cosas_principales/programacion/Clases/last_alien_alive/assets/explosion/exp4.png").convert_alpha()
exp4_redi = pygame.transform.scale(exp4, (110, 110)) #ancho, alto
exp5 = pygame.image.load("/home/elliot/Escritorio/Elliot/cosas_principales/programacion/Clases/last_alien_alive/assets/explosion/exp5.png").convert_alpha()
exp5_redi = pygame.transform.scale(exp5, (130, 130)) #ancho, alto
exp6 = pygame.image.load("/home/elliot/Escritorio/Elliot/cosas_principales/programacion/Clases/last_alien_alive/assets/explosion/exp6.png").convert_alpha()
exp6_redi = pygame.transform.scale(exp6, (150, 150)) #ancho, alto
exp7 = pygame.image.load("/home/elliot/Escritorio/Elliot/cosas_principales/programacion/Clases/last_alien_alive/assets/explosion/exp7.png").convert_alpha()
exp7_redi = pygame.transform.scale(exp7, (170, 170)) #ancho, alto
exp8 = pygame.image.load("/home/elliot/Escritorio/Elliot/cosas_principales/programacion/Clases/last_alien_alive/assets/explosion/exp8.png").convert_alpha()
exp8_redi = pygame.transform.scale(exp8, (190, 190)) #ancho, alto
explosion_frames = [exp1, exp2, exp3, exp4, exp5, exp6, exp7, exp8]