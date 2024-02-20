import pygame

from classes.ui.Checkbox import Checkbox

class SettingsPanel:
    def __init__(self, screen, engine):
        relative_x = screen.get_width() - 200
        relative_y = 200

        self.screen = screen
        self.engine = engine
        self.font = pygame.font.SysFont(None, 24)
        self.panel_rect = pygame.Rect(relative_x, relative_y, 200, self.screen.get_height() - 200)
        self.checkbox = Checkbox(screen, (relative_x + 10, relative_y + 30), "Следовать за дроном")

    def draw(self):
        relative_x = self.screen.get_width() - 200
        relative_y = 200

        pygame.draw.rect(self.screen, (200, 200, 200), self.panel_rect)

        text = self.font.render("Настройки", True, (0, 0, 0))
        self.screen.blit(text, (relative_x + 10, relative_y + 10))

        self.checkbox.draw()



    def handle_event(self, event):
        self.checkbox.handle_event(event)
        if self.checkbox.checked != self.engine.follow_drone:
            self.engine.follow_drone = self.checkbox.checked