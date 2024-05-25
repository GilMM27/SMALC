# Importar pygame
import pygame
 
# Importar sys
import sys
 
# Inicializar pygame
pygame.init()
 
# Crear un reloj
clock = pygame.time.Clock()

# Crear una ventana de 500x500
display_screen = pygame.display.set_mode((500, 500))
 
# Establecer el título de la ventana
base_font = pygame.font.Font(None, 40)
 
 
# User text es una cadena vacía
user_text = ''
 
# Crear un rectángulo para el texto
input_rect = pygame.Rect(200, 200, 140, 32)
color_active = pygame.Color("lightskyblue")
color_passive = pygame.Color("gray15")
color = color_passive
 

# Establecer el cursor en la posición del rectángulo
active = False

while True:
     # Checar eventos
    for event in pygame.event.get():
        # Checar si se cierra la ventana
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
 
        # Checar si se presiona el botón del mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Checar si el cursor está en el rectángulo
            if input_rect.collidepoint(event.pos):
                active = True
        # Checar si se presiona una tecla
        if event.type == pygame.KEYDOWN:
            # Checar si el cursor está activo
            if event.key == pygame.K_BACKSPACE:
                 
                # Checar si el texto no está vacío
                user_text = user_text[0:-1]
            else:
                user_text += event.unicode
    # Establecer el color de fondo con RGB
    display_screen.fill((0, 0, 0))
    # Checar si el cursor está activo
    if active:
        color = color_active
    else:
        color = color_passive
    # Dibujar el rectángulo
    pygame.draw.rect(display_screen, color, input_rect)
     
    # Checar si el texto no está vacío
    text_surface = base_font.render(user_text, True, (255, 255, 255))
    display_screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
    # Actualizar la ventana
    input_rect.w = max(100, text_surface.get_width() + 10)
    # Checar si el cursor está activo
    pygame.display.flip()
    clock.tick(60)
