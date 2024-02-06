import pygame
from const import FPS

surface = pygame.display.set_mode((1200, 800))

pygame.display.set_caption("Map")

imgBG = pygame.image.load('assets/map.jpg')
clock = pygame.time.Clock()

x = 0
y = 0
size = 8
pos = (x, y, size, size)
color = (255, 0, 0)

saved_mouse_pos = (0, 0)
offset = (0, 0)


def keyboard():
    global x
    global y
    global size
    global pos

    keyboard = pygame.key.get_pressed()

    if keyboard[pygame.K_LEFT]:
        if x > 0:
            x -= 8
    if keyboard[pygame.K_RIGHT]:
        if x < 1765:
            x += 8
    if keyboard[pygame.K_UP]:
        if y > 0:
            y -= 8
    if keyboard[pygame.K_DOWN]:
        if y < 819:
            y += 8

    pos = (x, y, size, size)

def mouse():
    global saved_mouse_pos
    global offset

    mouse_state = pygame.mouse.get_pressed()
    mouse_pos = pygame.mouse.get_pos()

    if mouse_state[0] == True and saved_mouse_pos == offset:
        saved_mouse_pos = (mouse_pos[0] - offset[0], mouse_pos[1] - offset[1])
    
    if mouse_state[0] == False and saved_mouse_pos != offset:
        saved_mouse_pos = (offset[0], offset[1])

    if mouse_state[0] == True:
        if mouse_pos[0] != saved_mouse_pos[0] and mouse_pos[1] != saved_mouse_pos[1]:
            offset = (mouse_pos[0] - saved_mouse_pos[0], mouse_pos[1] - saved_mouse_pos[1])

while True:
    clock.tick(FPS)

    surface.blit(imgBG, (offset[0], offset[1]))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    mouse()
    keyboard()

    pygame.draw.rect(surface, color, pos)
    pygame.display.update()
