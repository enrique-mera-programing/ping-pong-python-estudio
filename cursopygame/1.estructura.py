import pygame, sys

# Inicializar pygame
pygame.init()

# configuracion de pantalla

ANCHO, ALTO = 800, 600
print((ANCHO, ALTO))
ventana= pygame.display.set_mode((ANCHO,ALTO)) # (ancho, alto) es porque el atributo pide q sean coordenadas y las cordenadas van en este formato (a,b)
pygame.display.set_caption("Mi primer juego") # nombre de la ventana

#color

Azul = (0,100,255)

#reloj: controla los fps para q se mantengan en lo q definamos si no puede hacer q la pc se vuelva lenta
reloj = pygame.time.Clock()

# si es jugador esta en una pantalla con la codicion dada para q se ejecute el bucle correcto
jugador= 1

#eventos de la ventana
print(pygame.event.get())
while jugador==1:
    for evento in pygame.event.get():
        if evento.type==pygame.QUIT:
            pygame.quit() # cierra el MODULOS en ejecucion de pygame para evitar q se cuelgue y asi
            sys.exit()
            
    # pinta la ventana del color
    ventana.fill(Azul)

    # aplica los cambios de pintado en este caso

    pygame.display.flip()

    # se define los fps en q va a trabajar el programa o juego en este caso
    reloj.tick(60)