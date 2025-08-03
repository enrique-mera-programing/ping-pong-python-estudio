import pygame, sys

pygame.init()


ANCHO, ALTO = 800, 600
print((ANCHO, ALTO))
ventana= pygame.display.set_mode((ANCHO,ALTO)) 
pygame.display.set_caption("Mi primer juego") 
Azul = (0,100,255)
reloj = pygame.time.Clock()
jugador= 1

# dibujar cuadrado (posicion derecha, posicion arriba, ancho, alto)
cuadrado=pygame.Rect(ANCHO/2,0,5,ALTO)
cuadrado1=pygame.Rect(0,0,5,ALTO)

# movimiento del cuadrado
velocidad_movimiento=5
print(pygame.event.get())
while jugador==1:
    for evento in pygame.event.get():
        if evento.type==pygame.QUIT:
            pygame.quit() 
            sys.exit()

    #leer las teclas a precionar
    teclas=pygame.key.get_pressed()
    
    #movimiento
    if teclas[pygame.K_LEFT]:
        cuadrado.x -= velocidad_movimiento
    if teclas[pygame.K_RIGHT]:
        cuadrado.x += velocidad_movimiento
    if teclas[pygame.K_a]:
        cuadrado1.x -= velocidad_movimiento
    if teclas[pygame.K_d]:
        cuadrado1.x += velocidad_movimiento
    
    # validar q no salga de la pantalla
    if cuadrado.x < 0: #recordar que comienza a leer desde el 0
        cuadrado.x = 0
    if cuadrado.x > ANCHO - 5: # es menos 5 porque  es el ancho del cuadrado y eso igual ocupa
        cuadrado.x = ANCHO - 5

    if cuadrado.colliderect(cuadrado1): # detecta cuando 2 cuadrados colicionan o se tocan
        print('colicion')
    
    ventana.fill(Azul)

    # dibujar en la ventana
    pygame.draw.rect(ventana,(0,0,0,0),cuadrado)
    pygame.draw.rect(ventana,(0,0,0,0),cuadrado1)

    pygame.display.flip()

    reloj.tick(60)