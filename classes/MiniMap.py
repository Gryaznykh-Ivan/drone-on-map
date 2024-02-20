import pygame

class MiniMap:
    def __init__(self, drone, map_image, screen):
        self.drone = drone
        self.map_image = map_image
        self.screen = screen
        self.width = 200
        self.height = 200
        self.border_color = (255, 255, 255)
        self.drone_color = (255, 0, 0)

    def draw(self):
        drone_x, drone_y, drone_view_around = self.drone.x, self.drone.y, self.drone.view_around
        x1 = max(0, drone_x - drone_view_around)
        y1 = max(0, drone_y - drone_view_around)
        x2 = min(self.map_image.get_width(), drone_x + drone_view_around)
        y2 = min(self.map_image.get_height(), drone_y + drone_view_around)

        mini_map_width = x2 - x1
        mini_map_height = y2 - y1

        mini_map = pygame.transform.scale(self.map_image.subsurface((x1, y1, mini_map_width, mini_map_height)), (self.width, self.height))
        self.screen.blit(mini_map, (self.screen.get_width() - self.width, 0))

        drone_x_on_mini_map = int((self.drone.x - x1) / mini_map_width * self.width) + (self.screen.get_width() - self.width)
        drone_y_on_mini_map = int((self.drone.y - y1) / mini_map_height * self.height)

        pygame.draw.rect(self.screen, self.drone_color, (drone_x_on_mini_map, drone_y_on_mini_map, self.drone.size, self.drone.size))
        pygame.draw.rect(self.screen, self.border_color, (self.screen.get_width() - self.width, 0, self.width, self.height), 2)