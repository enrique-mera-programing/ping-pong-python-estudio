import pygame, sys
pygame.init()

ancho, alto = 800, 600
ventana = pygame.display.set_mode((ancho, alto))
reloj = pygame.time.Clock()

pelota = pygame.Rect(ancho//2, alto//2, 20, 20)
raqueta = pygame.Rect(30, alto//2 - 50, 10, 100)

vel_x, vel_y = 7, 7
vel_raqueta = 7

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimiento de la pelota
    pelota.x += vel_x
    pelota.y += vel_y

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_w] and raqueta.top > 0:
        raqueta.y -= vel_raqueta
    if teclas[pygame.K_s] and raqueta.bottom < alto:
        raqueta.y += vel_raqueta


    # Rebote con techo y suelo
    if pelota.top <= 0 or pelota.bottom >= alto:
        vel_y *= -1

# Rebote con raqueta
    if pelota.colliderect(raqueta):
        vel_x *= -1
    # Rebote en x
    if pelota.x < 0 or pelota.x > ancho-5: #recordar que comienza a leer desde el 0
        vel_x *= -1
        

    # Dibujar
    ventana.fill((0, 128, 0))
    pygame.draw.rect(ventana, (255, 255, 255), raqueta)
    pygame.draw.ellipse(ventana, (255, 255, 255), pelota)
    pygame.display.flip()
    reloj.tick(60)

    
