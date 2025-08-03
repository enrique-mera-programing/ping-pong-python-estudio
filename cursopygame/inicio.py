import pygame
import sys

# Inicializamos Pygame
pygame.init()

# Definimos el tamaño de la ventana
ancho, alto = 800, 600
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Pantalla de Inicio")

# Reloj para controlar los FPS (cuántas veces se actualiza por segundo)
clock = pygame.time.Clock()

# Colores que vamos a usar (en formato RGB)
VERDE = (0, 128, 0)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
GRIS = (200, 200, 200)

# Fuentes (tamaño grande para título, más pequeño para texto)
fuente_grande = pygame.font.Font(None, 60)
fuente_pequena = pygame.font.Font(None, 40)

# Variables para guardar el nombre y controlar el estado
nombre = ""               # Texto que escribe el usuario
escribiendo = True        # Si está escribiendo o no
iniciar_juego = False     # Si ya pulsó el botón "JUGAR"

# Definimos las áreas (rectángulos) donde irán los botones y el campo de texto
boton_jugar = pygame.Rect(ancho // 2 - 100, 350, 200, 50)   # (x, y, ancho, alto)
boton_salir = pygame.Rect(ancho // 2 - 100, 420, 200, 50)
input_nombre = pygame.Rect(ancho // 2 - 150, 250, 300, 50)

# Función que dibuja todo en pantalla
def dibujar_pantalla():
    # Pintamos el fondo de verde
    ventana.fill(VERDE)

    # Mostramos el título "Bienvenido a Pong"
    titulo = fuente_grande.render("🏓 Bienvenido a Pong", True, BLANCO)
    ventana.blit(titulo, (ancho // 2 - titulo.get_width() // 2, 100))

    # Texto que dice "Escribe tu nombre:"
    instruccion = fuente_pequena.render("Escribe tu nombre:", True, BLANCO)
    ventana.blit(instruccion, (ancho // 2 - instruccion.get_width() // 2, 210))

    # Cuadro blanco donde el usuario escribe
    pygame.draw.rect(ventana, BLANCO, input_nombre, 2)  # (2) = borde de grosor 2
    texto_nombre = fuente_pequena.render(nombre, True, BLANCO)
    ventana.blit(texto_nombre, (input_nombre.x + 10, input_nombre.y + 10))

    # Botón "JUGAR"
    pygame.draw.rect(ventana, GRIS, boton_jugar)
    txt_jugar = fuente_pequena.render("JUGAR", True, NEGRO)
    ventana.blit(txt_jugar, (boton_jugar.x + 60, boton_jugar.y + 10))

    # Botón "SALIR"
    pygame.draw.rect(ventana, GRIS, boton_salir)
    txt_salir = fuente_pequena.render("SALIR", True, NEGRO)
    ventana.blit(txt_salir, (boton_salir.x + 65, boton_salir.y + 10))

    # Mostramos todo lo dibujado en la pantalla
    pygame.display.flip()

# Bucle principal de la pantalla de inicio
while not iniciar_juego:
    # Revisamos los eventos (teclado, mouse, salir, etc.)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            # Si cierra la ventana, terminamos el programa
            pygame.quit()
            sys.exit()

        # Si el usuario está escribiendo su nombre...
        if evento.type == pygame.KEYDOWN and escribiendo:
            if evento.key == pygame.K_BACKSPACE:
                # Borrar letra si presiona Backspace
                nombre = nombre[:-1]
            elif evento.key == pygame.K_RETURN:
                # Si presiona Enter, termina de escribir
                escribiendo = False
            elif len(nombre) < 15 and evento.unicode.isprintable():
                # Agrega letra si es válida y no excede 15 caracteres
                nombre += evento.unicode

        # Si hace clic con el mouse...
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_jugar.collidepoint(evento.pos):
                # Si da clic en "JUGAR" y el nombre no está vacío, inicia el juego
                if nombre.strip() != "":
                    iniciar_juego = True
            if boton_salir.collidepoint(evento.pos):
                # Si da clic en "SALIR", cierra todo
                pygame.quit()
                sys.exit()

    # Dibujamos la pantalla en cada vuelta del bucle
    dibujar_pantalla()
    clock.tick(30)  # Limitamos a 30 FPS

