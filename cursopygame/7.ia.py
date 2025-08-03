import pygame, sys
pygame.init()

# Ventana
ancho, alto = 800, 600
ventana = pygame.display.set_mode((ancho, alto))
reloj = pygame.time.Clock()

# Objetos
pelota = pygame.Rect(ancho//2, alto//2, 20, 20)
jugador = pygame.Rect(30, alto//2 - 50, 10, 100)
oponente = pygame.Rect(ancho - 40, alto//2 - 50, 10, 100)
bollColor=(255, 255, 255)
# Velocidades
vel_x, vel_y = 5, 5
vel_jugador = 7
vel_oponente = 3  # puede bajarse para que falle más

# Bucle principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Controles del jugador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_w] and jugador.top > 0:
        jugador.y -= vel_jugador
    if teclas[pygame.K_s] and jugador.bottom < alto:
        jugador.y += vel_jugador

    # Movimiento de pelota
    pelota.x += vel_x
    pelota.y += vel_y

    # Rebote con bordes superior/inferior
    if pelota.top <= 0 or pelota.bottom >= alto:
        vel_y *= -1

    # Colisiones con raquetas
    if pelota.colliderect(jugador): 
        vel_x *= -1
        bollColor = (0, 0, 255)
    elif pelota.colliderect(oponente):
        vel_x *= -1
        bollColor = (255, 0, 0)

    # IA del oponente
    if oponente.centery < pelota.centery and oponente.bottom < alto:
        oponente.y += vel_oponente
    elif oponente.centery > pelota.centery and oponente.top > 0:
        oponente.y -= vel_oponente

    # Reinicio si sale
    if pelota.left <= 0 or pelota.right >= ancho:
        pelota.x, pelota.y = ancho//2, alto//2
        vel_x *= -1
        bollColor = (255,255, 255)

    # Dibujar
    ventana.fill((0, 128, 0))  # verde
    pygame.draw.rect(ventana, (255, 255, 255), jugador)
    pygame.draw.rect(ventana, (255, 255, 255), oponente)
    pygame.draw.ellipse(ventana, bollColor, pelota)
    pygame.display.flip()
    reloj.tick(60)
