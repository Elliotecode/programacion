import pygame
import random

pygame.init()
pygame.font.init()  # Inicializar el módulo de FUENTEs

#paco = 1515 #eliminar esta línea después de probar que el archivo se abre bien

#tamaño de la pantalla
ANCHO_PANTALLA = 800
ALTO_PANTALLA = 600
pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))

#titulo de la ventana
pygame.display.set_caption("juegos de habilidad: lineas dañinas")

#color de fondo
COLOR_FONDO = (0, 0, 0)

#FUENTE
FUENTE = pygame.font.SysFont("Arial", 30)  # FUENTE de texto

vidas = 5
#jugador_herido = False
juego_terminado = False
INTERVALO_CREACION = 1000  # Intervalo de creación de líneas fantasma en milisegundos
INTERVALO_DE_DESVANECIMIENTO = 3000  # Intervalo de desvanecimiento de líneas reales en milisegundos
TIEMPO_LINEA_REAL = 5000
FPS = 60  # frames por segundo
reloj = pygame.time.Clock()

ultimo_tiempo_creacion = 0
ocupados = []  # Lista para rastrear las posiciones ocupadas por líneas fantasma
valores = []


def score(pantalla, vidas):
    texto_total = FUENTE.render(f"vidas: {vidas}", True, (255, 255, 255))
    pantalla.blit(texto_total, (10, 10))  # Posición del texto en la pantalla

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
        if teclas[pygame.K_RIGHT] and self.x + self.ancho < ANCHO_PANTALLA:
            self.x += self.velocidad
        if teclas[pygame.K_UP] and self.y > 0:
            self.y -= self.velocidad
        if teclas[pygame.K_DOWN] and self.y + self.alto < ALTO_PANTALLA:
            self.y += self.velocidad


# Necesitamos crear una nueva CLASE para las lineas fantasma y las lineas reales
#configuracion de las lineas fantasma y reales
# configuracion de las lineas fantasma
class Linea_Fantasma:
    def __init__(self):
        while True:
            self.x = random.randint(0, ANCHO_PANTALLA)
            valores = list(range(self.x - 25, self.x + 25))
            if not any(valor in ocupados for valor in valores):
                ocupados.extend(valores)
                #print(ocupados)
                break
        self.y = 0
        self.ancho = 5
        self.alto = ALTO_PANTALLA
        self.color = (128, 0, 0,)  # Color gris semitransparente
        self.velocidad = 0.0625
        self.control = 0
        self.tiempo_creacion = pygame.time.get_ticks()  # Tiempo de creación de la línea fantasma

        #declaración de funciones
        self.finalizada = False #cambia a true cuando termina una linea real
        self.reemplazada = False #cambia a true cuando una linea fantasma se convierte en una linea real
        self.ancho_final = None #cambia de valor cuando una linea real finaliza

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, self.color, (self.x, self.y, self.ancho, self.alto))
    
    def crecer(self):
        if self.finalizada:
            return # si se cumple esta condicion, se detiene el crecimiento
        if self.control < 800:
            self.ancho += self.velocidad
            self.x -= self.velocidad / 2
            self.control += 1

    def actualizar_estado(self, tiempo_actual):
        """
        Comentario bLoque:
        Detiene la línea al terminar su tiempo como línea fantasma.
        """
        if not self.finalizada and (tiempo_actual - self.tiempo_creacion >= TIEMPO_LINEA_REAL):
            self.finalizada = True
            # Congelar ancho en entero para dibujo consistente
            self.ancho_final = int(self.ancho)

#configuracion de las lineas reales
class Linea_Real:
    def __init__(self, linea_fantasma_ref):
        self.x = linea_fantasma_ref.x
        self.y = linea_fantasma_ref.y
        self.ancho = max(linea_fantasma_ref.ancho, 50) #linea_fantasma_1.ancho
        self.alto = linea_fantasma_ref.alto
        self.color = (255, 255, 255)  # Color blanco
        self.velocidad = 0.0625
        self.control = 0
        self.tiempo_creacion = pygame.time.get_ticks()
        self.colisionada = False

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, self.color, (self.x, self.y, self.ancho, self.alto))

    def oscurecer(self):
        self.color = (255, 0, 0)  # Cambia a un color rojo

    def quitar_vidas(self, jugador):
        colision = jugador.x + jugador.ancho >= self.x and jugador.x <= self.x + self.ancho
        return colision


        
#instanciar jugadores
player_1 = Jugador()
"""
player_2 = jugador()
"""

lineas_fantasmas = []
lineas_reales = []

contador_frames = 1

#bucle principal del juego
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

#    if paco == 1515: #vidas > 0 and not juego_terminado:
    pantalla.fill(COLOR_FONDO)
    tiempo_actual = pygame.time.get_ticks()

    if not juego_terminado:
        if tiempo_actual - ultimo_tiempo_creacion >= INTERVALO_CREACION:
            lineas_fantasmas.append(Linea_Fantasma())
            ultimo_tiempo_creacion = tiempo_actual

        lineas_fantasmas_eliminadas = []
        lineas_reales_eliminadas = []
        for linea_fantasma in lineas_fantasmas:
            linea_fantasma.dibujar(pantalla)
            linea_fantasma.crecer()
            linea_fantasma.actualizar_estado(tiempo_actual)

            if linea_fantasma.finalizada and not linea_fantasma.reemplazada:
                lineas_reales.append(Linea_Real(linea_fantasma))
                lineas_fantasmas_eliminadas.append(linea_fantasma)
                linea_fantasma.reemplazada = True  # evita duplicados
        
        for linea_fantasma in lineas_fantasmas_eliminadas:
            lineas_fantasmas.remove(linea_fantasma)

        for linea_real in lineas_reales:
            linea_real.dibujar(pantalla)
            if tiempo_actual - linea_real.tiempo_creacion >= 100:
                linea_real.oscurecer()

        #logica de colision controlada y vidas
            if linea_real.quitar_vidas(player_1) and not linea_real.colisionada:
                vidas -= 1
                linea_real.colisionada = True #esto evita colisiones multiples en una misma linea real
            
            if tiempo_actual - linea_real.tiempo_creacion >= INTERVALO_DE_DESVANECIMIENTO:
                lineas_reales_eliminadas.append(linea_real)
                
        for linea_real in lineas_reales_eliminadas:
            lineas_reales.remove(linea_real)
            for valor in range(0, 50):
                ocupados.remove(ocupados[0])  # Liberar la posición ocupada al eliminar la línea real

        player_1.dibujar(pantalla)
        # Leer teclas presionadas
        teclas = pygame.key.get_pressed()

        # Actualizar posición del jugador
        player_1.mover(teclas)
        
        score(pantalla, vidas)

        if vidas <= 0:
            juego_terminado = True
    

    else:
        mensaje = FUENTE.render("Juego Terminado", True, (255, 0, 0))
        pantalla.blit(mensaje, (ANCHO_PANTALLA // 2 - mensaje.get_width() // 2, ALTO_PANTALLA // 2 - mensaje.get_height() // 2))

        #actualizar pantalla
    pygame.display.flip()
    pygame.time.delay(6)  # 10 milisegundos


pygame.quit()

#

"""
tarea pendiente:
- cuando una linea real descuente una vida, debe desaparecer y compensarlo con una nueva linea fantasma
- mejorar la estetica del juegos:
    - que las lineas reales desaparescan suavemente is se tocan
    - que el fondo flashe en rojo cuando se pierde una vida
    y flashe blanco cuando se genere una linea real
    - que el jugador parpadee cuando se toque una linea real
    y que se vaya fracturando (haciendo grietas) 
"""
