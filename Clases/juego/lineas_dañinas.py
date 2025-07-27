import pygame
import random

pygame.init()
pygame.font.init()  # Inicializar el módulo de fuentes


#tamaño de la pantalla
ancho_pantalla = 800
alto_pantalla = 600
pantalla = pygame.display.set_mode((ancho_pantalla, alto_pantalla))

#titulo de la ventana
pygame.display.set_caption("juegos de habilidad: lineas dañinas")

#color de fondo
color_fondo = (0, 0, 0)

#fuente
fuente = pygame.font.SysFont("Arial", 30)  # Fuente de texto

vidas = 5
jugador_herido = False
juego_terminado = False


def score(pantalla, vidas):
    texto_total = fuente.render(f"vidas: {vidas}", True, (255, 255, 255))
    pantalla.blit(texto_total, (10, 10))  # Posición del texto en la pantalla

#definir el jugador
class jugador:
    def __init__(self):
        self.x = 375  # Posición inicial en el centro de la pantalla
        self.y = 300
        self.ancho = 25
        self.alto = 25
        self.velocidad = 0.35
        self.color = (255, 255, 255)  # Color blanco

    #declaración de funciones
    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, self.color, (self.x, self.y, self.ancho, self.alto))

    #def nueva_funcion (self, datos_entrada):
        #self.valores
        #operaciones
        #return resultado


    ###### función de ejemplo #####
    # def suma_dos_numeros(self, numero1, numero2)
#         suma = numero1 + numero2
#         return suma

    def mover(self, teclas):
        if teclas[pygame.K_LEFT] and self.x > 0:
            self.x -= self.velocidad
        if teclas[pygame.K_RIGHT] and self.x + self.ancho < ancho_pantalla:
            self.x += self.velocidad
        if teclas[pygame.K_UP] and self.y > 0:
            self.y -= self.velocidad
        if teclas[pygame.K_DOWN] and self.y + self.alto < alto_pantalla:
            self.y += self.velocidad


# Necesitamos crear una nueva CLASE para las lineas fantasma y las lineas reales
#configuracion de las lineas fantasma y reales
# configuracion de las lineas fantasma
class linea_fantasma:
    def __init__(self):
        self.x = random.randint(0, ancho_pantalla)
        self.y = 0
        self.ancho = 5
        self.alto = alto_pantalla
        self.color = (128, 0, 0,)  # Color gris semitransparente
        self.velocidad = 0.0625
        self.control = 0
        self.tiempo_creacion = pygame.time.get_ticks()  # Tiempo de creación de la línea fantasma

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, self.color, (self.x, self.y, self.ancho, self.alto))
    
    def crecer(self, control):
        if control < 800:
            self.ancho += self.velocidad
            self.x -= self.velocidad / 2
            self.control += 1

#configuracion de las lineas reales
class linea_real:
    def __init__(self, linea_fantasma_ref):
        self.x = linea_fantasma_ref.x
        self.y = linea_fantasma_ref.y
        self.ancho = max(linea_fantasma_ref.ancho, 50) #linea_fantasma_1.ancho
        self.alto = linea_fantasma_ref.alto
        self.color = (255, 255, 255)  # Color rojo
        self.velocidad = 0.0625
        self.control = 0

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, self.color, (self.x, self.y, self.ancho, self.alto))

    def oscurecer(self):
        self.color = (255, 0, 0)  # Cambia el color a rojo brillante
        
    def quitar_vidas(self, jugador):
        colision = jugador.x + jugador.ancho >= self.x and jugador.x <= self.x + self.ancho
        return colision


        
#instanciar jugadores
player_1 = jugador()
#player_2 = jugador()

lineas_fantasmas = []
lineas_reales = []

#instanciar lineas fantasma
linea_fantasma_1 = linea_fantasma()

#instanciar lineas reales
linea_real_1 = None

#contadores de vidas



#bucle principal del juego
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    pantalla.fill(color_fondo)

    if vidas > 0 and not juego_terminado:
        linea_fantasma_1.dibujar(pantalla)
        linea_fantasma_1.crecer(linea_fantasma_1.control)
        tiempo_actual = pygame.time.get_ticks()

        if linea_real_1 is None and (tiempo_actual - linea_fantasma_1.tiempo_creacion >= 4000):
            linea_real_1 = linea_real(linea_fantasma_1)

        if linea_real_1 is not None:
            linea_real_1.dibujar(pantalla)
            linea_real_1.oscurecer()
            if linea_real_1.quitar_vidas(player_1):
                if not jugador_herido:
                    vidas -= 1
                    jugador_herido = True
            else:
                jugador_herido = False

        player_1.dibujar(pantalla)
        teclas = pygame.key.get_pressed()
        player_1.mover(teclas)
        score(pantalla, vidas)
    else:
        juego_terminado = True
        mensaje = fuente.render("¡Perdiste!", True, (255, 0, 0))
        pantalla.blit(mensaje, (ancho_pantalla // 2 - mensaje.get_width() // 2, alto_pantalla // 2 - mensaje.get_height() // 2))
        pygame.display.flip()
        pygame.time.delay(2000)  # Espera 2 segundos mostrando el mensaje
        ejecutando = False       # Sale del bucle principal

    pygame.display.flip()
    pygame.time.delay(1)

pygame.quit()






#     def dibujar(self, pantalla):


# class linea_real:
#     def __init__(self):


#     def dibujar(self, pantalla):