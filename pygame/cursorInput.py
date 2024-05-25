
import pygame

# Importan time 
import time

#Inicializan pygame 
pygame.init()

#Crear una ventana de 500x500

display_screen = pygame.display.set_mode((500, 500))

#Establecen el título de la ventana 
text = 'SMALC 2024'

#Establecer el texto y el tamaño de la fuente font 
pygame.font.SysFont(None, 40)

#Crear un objeto de texto con el texto que se va a mostrar (también se puede establecer el color) ing 
font.render(text, True, (255, 0, 0))

# Crear un rectángulo para ell texto

rect = img.get_rect()

rect.topleft= (20, 20)

# Crear un rectángulo para el cursor

cursor = pygame.Rect(rect.topright, (3, rect.height))

running = True

while running:

# Checar eventos

for event in pygame.event.get():

#Checar si se cierra la ventana

if event.type == pygame.QUIT:

running = False

# Checar si se presiona una tecla

if event.type == pygame.KEYDOWN:

#Checar si se presiona la tecla de retroceso

if event.key == pygame.K_BACKSPACE:

# Checar si el texto no está vacío

if len(text) > 0:

#Eliminar el último carácter del texto

text = text[:-1]

# Checar si se presiona una tecla

else: text += event.unicode

# Establecer el texto y el tamaño de la fuente img = font.render(text, True, (255, 0, 0)) rect.size = img.get_size()

cursor.topleft = rect.topright