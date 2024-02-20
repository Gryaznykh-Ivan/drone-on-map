import pygame

class Drone:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.color = (255, 0, 0)
        self.velocity = 8
        self.view_around = 80

    def getParams(self):
        return (self.x, self.y, self.size, self.size)
    
    def movement(self, map):
        keyboard = pygame.key.get_pressed()

        if keyboard[pygame.K_LEFT]:
            if self.x > self.view_around:
                self.x -= self.velocity
        if keyboard[pygame.K_RIGHT]:
            if self.x < map.get_width() - self.view_around:
                self.x += self.velocity
        if keyboard[pygame.K_UP]:
            if self.y > self.view_around:
                self.y -= self.velocity
        if keyboard[pygame.K_DOWN]:
            if self.y < map.get_height() - self.view_around:
                self.y += self.velocity

    def draw(self, screen, offset):
        relative_x = self.x + offset[0]
        relative_y = self.y + offset[1]

        pygame.draw.rect(screen, self.color, (relative_x, relative_y, self.size, self.size))
        pygame.draw.polygon(screen, self.color, [(relative_x - self.view_around, relative_y - self.view_around), (relative_x - self.view_around, relative_y + self.view_around + self.size), (relative_x + self.view_around + self.size, relative_y + self.view_around + self.size), (relative_x + self.view_around + self.size, relative_y - self.view_around)], 2)
