import pygame
import sys

# Inicializar pygame
pygame.init()

# Pantalla
ANCHO, ALTO = 1000, 500
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Ping Pong con fondo verde")

# FPS (velocidad del juego)
clock = pygame.time.Clock()
FPS = 60

# Colores
VERDE = (0, 128, 0)

# Cargar imágenes
paleta_img = pygame.image.load("p.png")
paleta_img = pygame.transform.scale(paleta_img, (15, 100))

pelota_img = pygame.image.load("pelota.png")
pelota_img = pygame.transform.scale(pelota_img, (30, 30))

# Crear rectángulos para posiciones y colisiones
paleta1 = pygame.Rect(50, ALTO // 2 - 50, 15, 100)
paleta2 = pygame.Rect(ANCHO - 65, ALTO // 2 - 50, 15, 100)
pelota = pygame.Rect(ANCHO // 2 - 15, ALTO // 2 - 15, 30, 30)

# Velocidad de la pelota
pelota_vel_x = 6
pelota_vel_y = 6

# Bucle principal del juego
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimiento de paletas
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_w] and paleta1.top > 0:
        paleta1.y -= 7
    if teclas[pygame.K_s] and paleta1.bottom < ALTO:
        paleta1.y += 7
    if teclas[pygame.K_UP] and paleta2.top > 0:
        paleta2.y -= 7
    if teclas[pygame.K_DOWN] and paleta2.bottom < ALTO:
        paleta2.y += 7

    # Movimiento de la pelota
    pelota.x += pelota_vel_x
    pelota.y += pelota_vel_y

    # Rebote arriba/abajo
    if pelota.top <= 0 or pelota.bottom >= ALTO:
        pelota_vel_y *= -1

    # Rebote con paletas
    if pelota.colliderect(paleta1) or pelota.colliderect(paleta2):
        pelota_vel_x *= -1

    # Reinicio si sale de los lados
    if pelota.left <= 0 or pelota.right >= ANCHO:
        pelota.center = (ANCHO // 2, ALTO // 2)
        pelota_vel_x *= -1

    # Dibujo
    ventana.fill(VERDE)  # Fondo verde
    ventana.blit(paleta_img, paleta1.topleft)
    ventana.blit(paleta_img, paleta2.topleft)
    ventana.blit(pelota_img, pelota.topleft)

    pygame.display.flip()
    clock.tick(FPS)
