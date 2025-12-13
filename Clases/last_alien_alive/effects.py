"""
traer la clase de flash
"""
class Flash:
    def __init__(self):
        self.color = [255, 255, 255, 65]  # Blanco con transparencia
        self.x = 0
        self.y = 0
        self.ancho = ANCHO_PANTALLA
        self.alto = ALTO_PANTALLA
        self.control = 0
        self.velocidad = 1.5

    def dibujar(self, pantalla):
        self.surface_flash = pygame.Surface((self.ancho, self.alto), pygame.SRCALPHA)
        self.surface_flash.fill(self.color)
        pantalla.blit(self.surface_flash, (self.x, self.y, self.ancho, self.alto))

    def desvanecer(self):
        self.color[3] = max(0, self.color[3] - self.velocidad)

    def reiniciar(self):
        self.color[3] = 65  # Reiniciar la transparencia