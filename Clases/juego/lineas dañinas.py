import pygame
import random

pygame.init()
pygame.font.init()  # Inicializar el módulo de FUENTEs

#tamaño de la pantalla
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
INTERVALO_ANIMACION_JUGADOR = 100  # Intervalo de animación del jugador en milisegundos
ultimo_tiempo_animacion = 0
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
        self.velocidad = 0.50
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
        self.color = (128, 0, 0)
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
        self.color = [255, 255, 255]  # Color blanco
        self.velocidad = 5
        self.control = 0
        self.tiempo_creacion = pygame.time.get_ticks()
        self.colisionada = False

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, self.color, (self.x, self.y, self.ancho, self.alto))

    def oscurecer(self):
        if self.control < 48:
            self.color[1] = self.color[1] - self.velocidad
            self.color[2] = self.color[2] - self.velocidad
            self.control += 1

    def desbanecer(self):
        self.color[0] = max(0, self.color[0] - self.velocidad)
        self.color[1] = max(0, self.color[1] - self.velocidad)
        self.color[2] = max(0, self.color[2] - self.velocidad)

    def quitar_vidas(self, jugador):
        colision = jugador.x + jugador.ancho >= self.x and jugador.x <= self.x + self.ancho
        return colision



#instanciar jugadores
player_1 = Jugador()
lineas_fantasmas = []
lineas_reales = []

#bucle principal del juego
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    pantalla.fill(color_fondo)
    pygame.image.scale(FONDO, (ANCHO_PANTALLA, ALTO_PANTALLA))
    pantalla.blit(FONDO, (0, 0))
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
            #color_fondo = (75, 15, 15)  # Cambia a un color rojo mas fuerte
            if tiempo_actual - linea_real.tiempo_creacion >= 100:
                linea_real.oscurecer()
            #    color_fondo = (25, 0, 0)
            #    #linea_real.flash_blanco(color_fondo)

        #logica de colision controlada y vidas
            if linea_real.quitar_vidas(player_1) and not linea_real.colisionada:
                vidas -= 1
                linea_real.colisionada = True #esto evita colisiones multiples en una misma linea real

            #logica de desvanecimiento y eliminacion de lineas reales
            if linea_real.colisionada:
                linea_real.desbanecer()
                if linea_real.color == [0, 0, 0] and linea_real not in lineas_reales_eliminadas:
                    lineas_reales_eliminadas.append(linea_real) #elimina la linea real que ha colisionado
                    lineas_fantasmas.append(Linea_Fantasma()) #compensa la linea real eliminada con una nueva linea fantasma
            
            if tiempo_actual - linea_real.tiempo_creacion >= INTERVALO_DE_DESVANECIMIENTO:
                linea_real.desbanecer()
                if linea_real.color == [0, 0, 0] and linea_real not in lineas_reales_eliminadas:
                    lineas_reales_eliminadas.append(linea_real)
        
        for linea_real in lineas_reales_eliminadas:
            lineas_reales.remove(linea_real)
            for valor in range(0, 50):
                ocupados.remove(ocupados[0])  # Liberar la posición ocupada al eliminar la línea real

        # Leer teclas presionadas
        teclas = pygame.key.get_pressed()
        # Actualizar posición del jugador
        player_1.mover(teclas)
        if player_1.moviendose_L or player_1.moviendose_R or player_1.moviendose_U or player_1.moviendose_D:
            player_1.animar_walk()
        else:
            player_1.animar_idle()

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

"""
tarea pendiente:
- cuando una linea real descuente una vida, debe desaparecer y compensarlo con una nueva linea fantasma
-ajustes en dificultas:
    - cada 30 segundos, aumenta la velocidad de creaación de las lineas fantasma + 20 milisegundos
    - cada 60 segundos, aumenta la velocidad de crecimiento de las lineas fantasma + 20 milisegundos
    - al minuto 2, que empiesen a generarse 2 lineas fantasma a la vez
    y que se generen lineas verticales y horizontales

- mejorar la estetica del juegos:
    - que las lineas reales desaparescan suavemente is se tocan
            - que el fondo flashe en rojo cuando se pierde una vida
            y flashe blanco cuando se genere una linea real
    - que el jugador parpadee cuando se toque una linea real
    y que se vaya fracturando (haciendo grietas)
    - un oscurecer mas suave 

TAREAS IMPORTANTES:
- hacer que el jugador sea un alien de space invaders
y si funciona mesclarlo con main.py
"""
