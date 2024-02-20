import pygame


class Checkbox:
    def __init__(self, screen, position, label=""):
        self.screen = screen
        self.position = position
        self.label = label
        self.font = pygame.font.SysFont(None, 14)
        self.rect = pygame.Rect(position, (20, 20))
        self.checked = False

    def draw(self):
        pygame.draw.rect(self.screen, (0, 0, 0), self.rect, 2)
        if self.checked:
            pygame.draw.line(self.screen, (0, 0, 0), (self.position[0] + 2, self.position[1] + 7), (self.position[0] + 7, self.position[1] + 15), 4)
            pygame.draw.line(self.screen, (0, 0, 0), (self.position[0] + 7, self.position[1] + 15), (self.position[0] + 17, self.position[1] + 2), 4)
        
        if self.label:
            label_text = self.font.render(self.label, True, (0, 0, 0))
            self.screen.blit(label_text, (self.position[0] + 30, self.position[1] + 4))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.checked = not self.checked
