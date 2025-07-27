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
def score(pantalla, vidas):
    texto_total = fuente.render(f"vidas: {vidas}", True, (255, 255, 255))
    pantalla.blit(texto_total, (10, 10))  # Posición del texto en la pantalla

FPS = 60  # frames por segundo

#definir el jugador
class Jugador:
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
class Linea_Fantasma:
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
class Linea_Real:
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
        
    def quitar_vidas(self, vidas, jugador):
        if self.x == jugador.x + jugador.ancho:
            vidas -= 1
            print(f"¡Vida perdida! Vidas restantes: {vidas}")


        
#instanciar jugadores
player_1 = Jugador()
#player_2 = jugador()

lineas_fantasmas = []
lineas_reales = []

#instanciar lineas fantasma
linea_fantasma_1 = Linea_Fantasma()

#instanciar lineas reales
linea_real_1 = None

#contadores de vidas


contador_frames = 1
ultimo_tiempo = 0
#bucle principal del juego
ejecutando = True
while ejecutando:
    pantalla.fill(color_fondo)
    tiempo_actual = pygame.time.get_ticks()
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
    contador_frames += 0.25

    if contador_frames >= FPS:
        lineas_fantasmas.append(Linea_Fantasma())
        contador_frames = 0

    if  (tiempo_actual - ultimo_tiempo >= 4000):
        lineas_fantasmas.append(Linea_Fantasma())
        ultimo_tiempo = tiempo_actual

    lineas_fantasmas_eliminadas = []
    for linea_fantasma in lineas_fantasmas:
        linea_fantasma.dibujar(pantalla)
        linea_fantasma.crecer(linea_fantasma.control)
        if tiempo_actual - linea_fantasma.tiempo_creacion >= 4000:
            lineas_reales.append(Linea_Real(linea_fantasma))
            lineas_fantasmas_eliminadas.append(linea_fantasma)

    #eliminarlas de la existencia
    for linea_fantasma in lineas_fantasmas_eliminadas:
        lineas_fantasmas.remove(linea_fantasma)

    #for linea_real in lineas_reales:
    #    linea_real.dibujar(pantalla)


#    if lineas_reales is not None:
#        for linea_real in lineas_reales:
#            lineas_reales.dibujar(pantalla)
#            lineas_reales.oscurecer()
#            lineas_reales.quitar_vidas(vidas, player_1)


    player_1.dibujar(pantalla)
    # Leer teclas presionadas
    teclas = pygame.key.get_pressed()

    # Actualizar posición del jugador
    player_1.mover(teclas)
     
    score(pantalla, vidas)
    
    #actualizar pantalla
    pygame.display.flip()
    pygame.time.delay(1)  # 10 milisegundos

pygame.quit()






