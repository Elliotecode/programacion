import pygame
import random

from config import *
from player import Jugador
from effects import Flash
from levels.level0 import Level_0
from levels.level1 import Level_1
from levels.level2 import Level_2
from levels.level3 import Level_3
from levels.level4 import Level_4
from levels.level5 import Level_5
from levels.level6 import Level_6
from levels.level7 import Level_7
from levels.level8 import Level_8
from levels.level9 import Level_9
from levels.level10 import Level_10
from levels.level11 import Level_11
from levels.level12 import Level_12
from levels.level13 import Level_13
from levels.level14 import Level_14
from levels.level_manager import Level_Manager

#niveles
i = 0
niveles = [Level_0(), Level_1(), Level_2(), Level_3(), Level_4(), Level_5(), Level_6(),
           Level_7(), Level_8(), Level_9(), Level_10(), Level_11(), Level_12(), Level_13(), Level_14()]
nivel_actual = niveles[i]
mannager = Level_Manager()

pygame.display.set_caption("Last Alien Alive")
juego_terminado = False
reloj = pygame.time.Clock()
linea_creada_real = False
ultimo_tiempo_creacion = 0
valores = []
ultimo_tiempo_animacion = 0

def score(pantalla, vidas):
    texto_total = FUENTE.render(f"vidas: {vidas}", True, (255, 255, 255))
    pantalla.blit(texto_total, (10, 10))  # Posición del texto en la pantalla

#instanciar jugadores
player_1 = Jugador()
#flash = Flash()
lineas_fantasmas = []
lineas_reales = []
flash = []

#bucle principal del juego
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    pantalla.fill(COLOR_FONDO)
    FONDO = pygame.transform.scale(FONDO, (ANCHO_PANTALLA, ALTO_PANTALLA))
    pantalla.blit(FONDO, (0, 0))
    tiempo_actual = pygame.time.get_ticks()

    if not juego_terminado:

        #logica de dificultad y niveles
        intervalo_creacion_V = nivel_actual.intervalo_creacion_V
        INTERVALO_DE_DESVANsECIMIENTO_V = nivel_actual.desvanecimiento_V
        for linea_fantasma in lineas_fantasmas:
            velocidad_linea_fantasma_V = nivel_actual.velocidad_linea_V
        print(velocidad_linea_fantasma_V)
        
        variable_sin_valor = nivel_actual.intervalo_creacion_H
        variable_sin_precio = nivel_actual.velocidad_linea_H
        variable_sin_poder = nivel_actual.desvanecimiento_H

        if tiempo_actual - mannager.ultimo_cambio >= mannager.duracion and i < len(niveles) - 1:
            i = i + 1
            nivel_actual = niveles[i]
            print(nivel_actual)
            mannager.ultimo_cambio = tiempo_actual

            print("nuevo nivel:", i)
            print(" ")
            #print(intervalo_creacion_V)
            #print(INTERVALO_DE_DESVANECIMIENTO_V)
            print(" ")

        from lines import Linea_Fantasma, Linea_Real, ocupados
        if tiempo_actual - ultimo_tiempo_creacion >= intervalo_creacion_V:
            lineas_fantasmas.append(Linea_Fantasma(velocidad_linea_fantasma_V))
            ultimo_tiempo_creacion = tiempo_actual

        lineas_fantasmas_eliminadas = []
        lineas_reales_eliminadas = []

        for linea_fantasma in lineas_fantasmas:
            linea_fantasma.dibujar(pantalla)
            linea_fantasma.crecer()
            linea_fantasma.actualizar_estado(tiempo_actual)

            if linea_fantasma.finalizada and not linea_fantasma.reemplazada:
                lineas_reales.append(Linea_Real(linea_fantasma))
                flash.append(Flash())
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

            #logica de desvanecimiento y eliminacion de lineas reales
            if linea_real.colisionada:
                linea_real.desbanecer()
                if linea_real.color == [0, 0, 0, 0] and linea_real not in lineas_reales_eliminadas:
                    lineas_reales_eliminadas.append(linea_real) #elimina la linea real que ha colisionado
                    lineas_fantasmas.append(Linea_Fantasma(velocidad_linea_fantasma_V)) #compensa la linea real eliminada con una nueva linea fantasma
            
            if tiempo_actual - linea_real.tiempo_creacion >= INTERVALO_DE_DESVANECIMIENTO_V:
                linea_real.desbanecer()
                if linea_real.color == [0, 0, 0, 0] and linea_real not in lineas_reales_eliminadas:
                    lineas_reales_eliminadas.append(linea_real)

        
        for linea_real in lineas_reales_eliminadas:
            lineas_reales.remove(linea_real)
            for valor in range(0, 40):
                ocupados.remove(ocupados[0])  # Liberar la posición ocupada al eliminar la línea real

        for efecto_flash in flash:
            efecto_flash.dibujar(pantalla)
            if tiempo_actual - linea_real.tiempo_creacion >= 100:
                efecto_flash.desvanecer()
                if efecto_flash.color[3] == 0:
                    flash.remove(efecto_flash)

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

-ajustes en dificultas:
    - cada 30 segundos, aumenta la velocidad de creación de las lineas fantasma + 20 milisegundos
    - cada 60 segundos, aumenta la velocidad de crecimiento de las lineas fantasma + 20 milisegundos
    y que se generen lineas verticales y horizontales
        -pensar la estrucura de los niveles
    
    -(idea dada por mi hermano) que aparescan puntos de energia que den vidas extras o ralenticen las lineas

-sonido de fondo y efectos de sonido
    -musica Y KFC

-tareas extras:
    - crear menu principal
    - crear menu de pausa y botones de reinicio y continuar
    - generar un executable
    - hacer un web
    - sistema de puntuacion
    - disfrutar el juego

tareas encargadas:
    - repasar el flujo y la creacion de objetos y sus variables
    *

    - intentar que funcione con otros niveles fijos
    -

    - decidir si la logica debe seguir asi (si eso- que hisimos en lines esta correcto)
    -
"""