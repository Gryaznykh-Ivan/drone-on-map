import pygame

from classes.Drone import Drone
from classes.MiniMap import MiniMap
from classes.Settings import SettingsPanel

class Engine:
    def __init__(self):
        self.screen = pygame.display.set_mode((1400, 800))
        self.clock = pygame.time.Clock()
        self.map = pygame.image.load("assets/map.jpg")
        self.drone = Drone(self.screen.get_width() // 2, self.screen.get_height() // 2, 8)
        self.offset = (0, 0)
        self.saved_mouse_pos = (0, 0)
        self.follow_drone = True

        pygame.display.set_caption("Карта")

    def run(self):
        settings_panel = SettingsPanel(self.screen, self)
        mini_map = MiniMap(self.drone, self.map, self.screen)

        while True:
            self.clock.tick(30)
            self.screen.blit(self.map, self.offset)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                
                settings_panel.handle_event(event)

            self.drone.movement(self.map)

            self.mouse()

            if self.follow_drone == True:
                self.offset = (self.screen.get_width() // 2 - self.drone.x, self.screen.get_height() // 2 - self.drone.y)
                self.offset = (min(0, max(-self.map.get_width() + self.screen.get_width(), self.offset[0])),
                               min(0, max(-self.map.get_height() + self.screen.get_height(), self.offset[1])))

            self.drone.draw(self.screen, self.offset)
            mini_map.draw()
            settings_panel.draw()

            pygame.display.update()

    def mouse(self):
        mouse_state = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()

        if mouse_state[0] == True and self.saved_mouse_pos == self.offset:
            self.saved_mouse_pos = (mouse_pos[0] - self.offset[0], mouse_pos[1] - self.offset[1])

        if mouse_state[0] == False and self.saved_mouse_pos != self.offset:
            self.saved_mouse_pos = (self.offset[0], self.offset[1])

        if mouse_state[0] == True:
            if mouse_pos[0] != self.saved_mouse_pos[0] and mouse_pos[1] != self.saved_mouse_pos[1]:
                x = self.offset[0]
                y = self.offset[1]

                if mouse_pos[0] - self.saved_mouse_pos[0] < 0:
                    if mouse_pos[0] - self.saved_mouse_pos[0] >= self.screen.get_width() - self.map.get_width():
                        x = mouse_pos[0] - self.saved_mouse_pos[0]
                    else:
                        x = self.screen.get_width() - self.map.get_width()
                else:
                    x = 0

                if mouse_pos[1] - self.saved_mouse_pos[1] < 0:
                    if mouse_pos[1] - self.saved_mouse_pos[1] >= self.screen.get_height() - self.map.get_height():
                        y = mouse_pos[1] - self.saved_mouse_pos[1]
                    else:
                        y = self.screen.get_height() - self.map.get_height()
                else:
                    y = 0

                self.offset = (x, y)
