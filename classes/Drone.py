import pygame

class Drone:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.color = (255, 0, 0)
        self.velocity = 8

    def getParams(self):
        return (self.x, self.y, self.size, self.size)
    
    def movement(self, map):
        keyboard = pygame.key.get_pressed()

        if keyboard[pygame.K_LEFT]:
            if self.x > 0:
                self.x -= self.velocity
        if keyboard[pygame.K_RIGHT]:
            if self.x < map.get_width():
                self.x += self.velocity
        if keyboard[pygame.K_UP]:
            if self.y > 0:
                self.y -= self.velocity
        if keyboard[pygame.K_DOWN]:
            if self.y < map.get_height():
                self.y += self.velocity

    def draw(self, screen, offset):
        relative_x = self.x + offset[0]
        relative_y = self.y + offset[1]

        pygame.draw.rect(screen, self.color, (relative_x, relative_y, self.size, self.size))
        pygame.draw.polygon(screen, self.color, [(relative_x - 40, relative_y - 40), (relative_x - 40, relative_y + 40 + self.size), (relative_x + 40 + self.size, relative_y + 40 + self.size), (relative_x + 40 + self.size, relative_y - 40)], 2)
