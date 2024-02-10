import pygame
from const import FPS


window_size = (1200, 800)
map = pygame.image.load('assets/map.jpg')


x = 0
y = 0
size = 8
pos = (x, y, size, size)
color = (255, 0, 0)

saved_mouse_pos = (0, 0)
offset = (0, 0)

surface = pygame.display.set_mode(window_size)
clock = pygame.time.Clock()
pygame.display.set_caption("Map")

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
        if x < map.get_width():
            x += 8
    if keyboard[pygame.K_UP]:
        if y > 0:
            y -= 8
    if keyboard[pygame.K_DOWN]:
        if y < map.get_height():
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
            x = offset[0]
            y = offset[1]

            if mouse_pos[0] - saved_mouse_pos[0] < 0:
                if mouse_pos[0] - saved_mouse_pos[0] >= window_size[0] - map.get_width():
                    print(1)
                    x = mouse_pos[0] - saved_mouse_pos[0]
                else:
                    print(2)
                    x = window_size[0] - map.get_width()
            else:
                x = 0
            
            if mouse_pos[1] - saved_mouse_pos[1] < 0:
                if mouse_pos[1] - saved_mouse_pos[1] >= window_size[1] - map.get_height():
                    print(3)
                    y = mouse_pos[1] - saved_mouse_pos[1]
                else:
                    print(4)
                    y = window_size[1] - map.get_height()
            else:
                y = 0

            offset = (x, y)

while True:
    clock.tick(FPS)

    surface.blit(map, (offset[0], offset[1]))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    mouse()
    keyboard()

    pygame.draw.rect(surface, color, pos)
    pygame.display.update()
