import pygame
import random

from config import ANCHO_PANTALLA, ALTO_PANTALLA
ocupados = []  # Lista para rastrear las posiciones ocupadas por líneas fantasma

# configuracion de las lineas fantasma
class Linea_Fantasma:
    def __init__(self):
        while True:
            self.x = random.randint(0, ANCHO_PANTALLA)
            valores = list(range(self.x - 20, self.x + 20))
            if not any(valor in ocupados for valor in valores):
                ocupados.extend(valores)
                #print(ocupados)
                break
        self.y = 0
        self.ancho = 5
        self.alto = ALTO_PANTALLA
        self.color = (128, 0, 0, 128)
        self.velocidad = 0.0625
        self.control = 0
        self.tiempo_creacion = pygame.time.get_ticks()  # Tiempo de creación de la línea fantasma

        #declaración de funciones
        self.finalizada = False #cambia a true cuando termina una linea real
        self.reemplazada = False #cambia a true cuando una linea fantasma se convierte en una linea real
        self.ancho_final = None #cambia de valor cuando una linea real finaliza

    def dibujar(self, pantalla):
        #pygame.draw.rect(pantalla, self.color, (self.x, self.y, self.ancho, self.alto))
        surface_fantasma = pygame.Surface((self.ancho, self.alto), pygame.SRCALPHA)
        surface_fantasma.fill(self.color)
        pantalla.blit(surface_fantasma, (self.x, self.y, self.ancho, self.alto))
    
    def crecer(self):
        if self.finalizada:
            return # si se cumple esta condicion, se detiene el crecimiento
        if self.ancho < 40:
            self.ancho = min(40, self.ancho + self.velocidad)
            self.x -= self.velocidad / 2


    def actualizar_estado(self, tiempo_actual):
        """
        Comentario bLoque:
        Detiene la línea al terminar su tiempo como línea fantasma.
        """
        if not self.finalizada and self.ancho == 40:    #if not self.finalizada and (tiempo_actual - self.tiempo_creacion >= TIEMPO_LINEA_REAL):
            self.finalizada = True
            # Congelar ancho en entero para dibujo consistente
            self.ancho_final = int(self.ancho)


#configuracion de las lineas reales
class Linea_Real:
    def __init__(self, linea_fantasma_ref):
        self.x = linea_fantasma_ref.x
        self.y = linea_fantasma_ref.y
        self.ancho = linea_fantasma_ref.ancho
        self.alto = linea_fantasma_ref.alto
        self.color = [255, 255, 255, 255]  # Color blanco
        self.velocidad = 5
        self.control = 0
        self.tiempo_creacion = pygame.time.get_ticks()
        self.colisionada = False

    def dibujar(self, pantalla):
        surface_real = pygame.Surface((self.ancho, self.alto), pygame.SRCALPHA)
        surface_real.fill(self.color)
        pantalla.blit(surface_real, (self.x, self.y, self.ancho, self.alto))
        #pygame.draw.rect(pantalla, self.color, (self.x, self.y, self.ancho, self.alto))

    def oscurecer(self):
        if self.control < 48:
            self.color[1] = self.color[1] - self.velocidad
            self.color[2] = self.color[2] - self.velocidad
            self.control += 1

    def desbanecer(self):
        self.color[0] = max(0, self.color[0] - self.velocidad)
        self.color[1] = max(0, self.color[1] - self.velocidad)
        self.color[2] = max(0, self.color[2] - self.velocidad)
        self.color[3] = max(0, self.color[3] - self.velocidad)

    def quitar_vidas(self, jugador):
        colision = jugador.x + jugador.ancho >= self.x and jugador.x <= self.x + self.ancho
        return colision