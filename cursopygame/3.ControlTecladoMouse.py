import pygame, sys

pygame.init()
ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Control teclado y mouse")
clock = pygame.time.Clock()

jugador = pygame.Rect(200, 100, 50, 50)
color = (0, 255, 0)
velocidad = 5

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Evento de tecla presionada (solo una vez)
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                print("¡Disparo!")
            if evento.key == pygame.K_ESCAPE:
                print("Juego pausado")

        # Evento de mouse
        if evento.type == pygame.MOUSEBUTTONDOWN:
            color=(255, 0, 0)
            print("Clic izquierdo en:", evento.pos)
        else:
            color=(0, 255, 0)

        # mover el jugador con el movimiento del mouse

        # .center selecciona la posicion
        # evento.pos captura la posicion del mouse en la ventana
        if evento.type == pygame.MOUSEMOTION:
            jugador.center = evento.pos
            print(jugador.center, evento)

    # Teclas presionadas (mientras estén sostenidas)
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_w]:
        jugador.y -= velocidad
    if teclas[pygame.K_s]:
        jugador.y += velocidad
    if teclas[pygame.K_a]:
        jugador.x -= velocidad
    if teclas[pygame.K_d]:
        jugador.x += velocidad

    # Dibujar
    ventana.fill((0, 0, 10))
    pygame.draw.rect(ventana, color, jugador)
    pygame.display.flip()
    clock.tick(60)
