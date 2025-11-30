import pygame # importar libreria de para componentes graficos especializadp en videojuegos
import random # importar llibreria para meanejo del azar

pygame.init()

# definir dimensiones de pantalla
# Tamaños de pantallas: mobile | tablet | desktop | screen
ancho_pantalla = 770
alto_pantalla = 400


# Configuración
fuente = pygame.font.SysFont("Arial", 30) #fuente de texto
clock = pygame.time.Clock()


# crear la pantalla
pantalla = pygame.display.set_mode((ancho_pantalla, alto_pantalla))
pygame.display.set_caption("Demo de Objetos cayendo") #dar nombre a la ventana

# paleta de colores
color_fondo = (30, 30, 30)
# Siguiente modificación: Cambiar el color de los objetos a un color aleatorio cada vez que se crea un nuevo objeto

#control de velocidad
FPS = 60 #frames por segundo

#creacion del objeto que cae
class Fall_shapes:
    def __init__(self):
        self.ancho = random.randint(20, 75)
        self.alto = random.randint(20, 75)
        self.x = random.randint(0, ancho_pantalla - self.ancho)
        self.y = -10 #inicia en la parte superior
        self.velocidad = random.randint(1, 6)
        self.forma = random.choice(["rect", "circle", "poligone"]) # Forma del objeto aleatoria dentro de una lista
        self.color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255)) # Color del objeto aleatorio dentro de una lista
    def mover(self):
        self.y += self.velocidad

    def dibujar(self, pantalla):
        # Opción de rectángulo
        if self.forma == "rect":
            pygame.draw.rect(pantalla, self.color, (self.x, self.y, self.ancho, self.alto))
        # Ópcion de círculo
        elif self.forma == "circle":
            radio = self.alto // 2    
            centro_x = self.x + radio
            centro_y = self.y + radio
            pygame.draw.circle(pantalla, self.color, (centro_x, centro_y), radio)
        # Opción de polígono
        else:
            pygame.draw.polygon(pantalla, self.color, [(self.x, self.y), (self.x + self.ancho, self.y), (self.x + self.ancho // 2, self.y - self.alto)])
        
    def fuera_pantalla(self):
        if self.y > alto_pantalla:
            return True
        else:
            return False

objetos = []
contador_frames = 0

contador_total = 0
contador_no_circulos = 0
contador_poligonos = 0
contador_poligonos_rb = 0



# Bucle principal del juego
ejecutando = True
while ejecutando:
    # Pintar el fondo
    pantalla.fill(color_fondo)

    # Manejar eventos (cerrar ventana)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

        # O cuando se alcanza un número máximo de objetos: 500

    # Cada 60 cuadros (1 segundo) agregar un nuevo objeto
    contador_frames += 1
    if contador_frames >= 60:
        objetos.append(Fall_shapes())
        contador_frames = 0

    # Mover y dibujar cada objeto
    # objetos = [ objeto_1, objeto_2, objeto_3, ... , objeto_45 ]
    objetos_eliminados = []
    for obj in objetos:
        obj.mover()
        obj.dibujar(pantalla)

        #contar todo
        if obj.fuera_pantalla():
            objetos_eliminados.append(obj)
            contador_total += 1
        #contar todo excepto circulos
            if obj.fuera_pantalla() and obj.forma == "rect" or obj.forma == "poligone":
                contador_no_circulos += 1
            #contar solo poligonos
            if obj.fuera_pantalla() and obj.forma == "poligone":
                contador_poligonos += 1
                #contar solo poligonos de color rojo y azul
                if obj.color[0] <= 165 and obj.color[1] <= 255 and obj.color[2] >= 165 or obj.color[0] >= 128 and obj.color[1] <= 128 and obj.color[2] <= 128 :
                    contador_poligonos_rb += 1

    for obj in objetos_eliminados:
        objetos.remove(obj)

    # Contar objetos en pantalla
    texto_total = fuente.render(f"Total: {contador_total}", True, (255, 255, 255))
    pantalla.blit(texto_total, (10, 10))

    #contar todos menos circulos
    texto_no_circulos = fuente.render(f"Todos menos circulos: {contador_no_circulos}", True, (255, 255, 255))
    pantalla.blit(texto_no_circulos, (10, 50))

    #contar solo poligonos
    texto_poligonos = fuente.render(f"Poligonos: {contador_poligonos}", True, (255, 255, 255))
    pantalla.blit(texto_poligonos, (10, 90))

    #contar poligonos rojos y azules
    texto_poligonos_rb = fuente.render(f"Poligonos rojos y azules: {contador_poligonos_rb}", True, (255, 255, 255))
    pantalla.blit(texto_poligonos_rb, (10, 130))
    
    # Actualizar pantalla
    pygame.display.flip()

    # Controlar la velocidad del bucle
    clock.tick(FPS)

#finalizar pygame
pygame.quit()





# ---------------- Tarea ----------------
# Opción easy:
#      Contar todos los objetos que caen excepto los círculos
# Opción medium:
#      Contar solo lo objetos tipo polígono
# Opción hard:
#      Contar solo los objetos tipo polígono de color rojos y azules