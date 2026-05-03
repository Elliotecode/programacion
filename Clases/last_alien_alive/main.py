import pygame
pygame.init()
pygame.mixer.init()

from config import *
from player import Jugador
from lines import Linea_Fantasma, Linea_Real, ocupados
from effects import Flash

pygame.display.set_caption("Last Alien Alive")
juego_terminado = False
game_over_pending = False
game_over_start_time = 0
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
                flash.append(Flash())
                sonido_laser.play()
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
                if vidas > 0:
                    sonido_colision.play()
                else:
                    sonido_muerte.play()

            #logica de desvanecimiento y eliminacion de lineas reales
            if linea_real.colisionada:
                linea_real.desbanecer()
                if linea_real.color == [0, 0, 0, 0] and linea_real not in lineas_reales_eliminadas:
                    lineas_reales_eliminadas.append(linea_real) #elimina la linea real que ha colisionado
                    if linea_real.post_mortem is None:
                        linea_real.post_mortem = tiempo_actual #marca el tiempo de muerte para evitar colisiones posteriores y controlar el tiempo de desvanecimiento post-mortem
                    elif linea_real.port_mortem - tiempo_actual >= 1750: #si han pasado 2 segundos desde la muerte, se elimina la linea real
                        lineas_fantasmas.append(Linea_Fantasma()) #compensa la linea real eliminada con una nueva linea fantasma
            
            if tiempo_actual - linea_real.tiempo_creacion >= INTERVALO_DE_DESVANECIMIENTO:
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
        if game_over == False:
            player_1.mover(teclas)
            if player_1.moviendose_L or player_1.moviendose_R or player_1.moviendose_U or player_1.moviendose_D:
                player_1.animar_walk()
            else:
                player_1.animar_idle()
        else:
            pass

        score(pantalla, vidas)

        if vidas <= 0:
            game_over = True
            if hora_de_muerte is None:
                hora_de_muerte = tiempo_actual
            elif tiempo_actual - hora_de_muerte >= 2000:
                juego_terminado = True
    

    else:
        mensaje = FUENTE.render("Juego Terminado", True, (255, 0, 0))
        pantalla.blit(mensaje, (ANCHO_PANTALLA // 2 - mensaje.get_width() // 2, ALTO_PANTALLA // 2 - mensaje.get_height() // 2))

        #actualizar pantalla
    pygame.display.flip()
    pygame.time.delay(6)  # 10 milisegundos


pygame.quit()

"""
-sonido al moverse
-musica de fondo
-musica al perder :(

bugs:
si chocas con muchas lineas reales, se crean tantas que el juego se queda sin espacio para crear mas lineas fantasma y termina muriendo.


"""