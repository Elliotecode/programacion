import pygame
pygame.init()
pygame.mixer.init()

from config import *
from player import Jugador
from lines import Linea_Fantasma, Linea_Real, ocupados
from effects import Flash

sonar_al_moverser = sonido_movimiento.play()

pygame.display.set_caption("Last Alien Alive")
juego_terminado = False
game_over_pending = False
game_over_start_time = 0
reloj = pygame.time.Clock()
linea_creada_real = False
ultimo_tiempo_creacion = 0
valores = []
ultimo_tiempo_animacion = 0

#i = 1
#explosion_frames = [exp1, exp2, exp3, exp4, exp5, exp6, exp7, exp8]
#frame_actual = explosion_frames[i - 1]

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
                if game_over == False:
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

                if sonar_al_moverser.get_busy() == True:
                    pass
                else:
                    sonido_movimiento.play()

            else:
                player_1.animar_idle()
        else:
            final_x = player_1.x
            final_y = player_1.y
            print("pocision final", final_x, final_y)
            print("pocision final", final_x + 10, final_y + 10)
            print("pocision final", final_x - 10, final_y - 10)

        if game_over == True:
            if tiempo_actual - hora_de_muerte <= 100:
                pantalla.blit(exp1_redi, (final_x - 15, final_y - 15))
            if tiempo_actual - hora_de_muerte >= 100 and tiempo_actual - hora_de_muerte <= 200:
                pantalla.blit(exp2_redi, (final_x - 25, final_y - 25))
            if tiempo_actual - hora_de_muerte >= 200 and tiempo_actual - hora_de_muerte <= 300:
                pantalla.blit(exp3_redi, (final_x - 35, final_y - 35))
            if tiempo_actual - hora_de_muerte >= 300 and tiempo_actual - hora_de_muerte <= 400:
                pantalla.blit(exp4_redi, (final_x - 55, final_y - 55))
            if tiempo_actual - hora_de_muerte >= 400 and tiempo_actual - hora_de_muerte <= 500:
                pantalla.blit(exp5_redi, (final_x - 65, final_y - 65)) 
            if tiempo_actual - hora_de_muerte >= 500 and tiempo_actual - hora_de_muerte <= 600:
                pantalla.blit(exp6_redi, (final_x - 75, final_y - 75))
            if tiempo_actual - hora_de_muerte >= 600 and tiempo_actual - hora_de_muerte <= 700:
                pantalla.blit(exp7_redi, (final_x - 85, final_y - 85))
            if tiempo_actual - hora_de_muerte >= 700 and tiempo_actual - hora_de_muerte <= 800:
                pantalla.blit(exp8_redi, (final_x - 95, final_y - 95))


                """            
                if tiempo_actual - game_over_start_time >= 2000:
                    exp3_redi = pygame.transform.scale(exp3, (75, 75)) #ancho, alto
                    pantalla.blit(exp3_redi, (final_x - 75, final_y - 75))
                """         
            
        """   
        x + a = derecha
        x - a = izquierda
        y + a = abajo
        y - a = arriba

        formula usada = x - h, y - a
                        ____________
                              2    

        """

        score(pantalla, vidas)

        if vidas <= 0:
            game_over = True
            if hora_de_muerte is None:
                hora_de_muerte = tiempo_actual
            elif tiempo_actual - hora_de_muerte >= 4000:
                juego_terminado = True
    

    else:
        efecto_flash.dibujar(pantalla)
        mensaje = FUENTE.render("Juego Terminado", True, (128, 0, 0))
        pantalla.blit(mensaje, (ANCHO_PANTALLA // 2 - mensaje.get_width() // 2, ALTO_PANTALLA // 2 - mensaje.get_height() // 2))

        #actualizar pantalla
    pygame.display.flip()
    pygame.time.delay(6)  # 10 milisegundos


pygame.quit()

"""
SONORO:
    -incormporar musica de fondo
    -musica al perder :(
-VISUAL:
    -animacion de muerte
        -sustiruir el if por un ciclo for que llame cada una de las pocisiones del arreglo.
        -en cada iteracion revisar la pocision de los diferentes frames de la animacion (modificar x y para que esten centradas)
    -hacer la linea real mas brillante
    -(extra) hacer la linea real difuminada
-JUGABILIDAD:
    -hacer un menu de inicio
    -hacer que puedas reiniciar el juego sin tener que cerrar la ventana
    -lineas verticales (beta)
-DIFICULTADES Y NIVELES:
    -implementementar niveles
-BUGS:
    -nada por ahora
"""