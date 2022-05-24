import pygame



class Text:
    def __init__(self, initial_text, font):
        self.color = pygame.Color(255, 255, 255)
        self.font = font
        self.update(initial_text)

    def update(self, text):
        self.renderedText = self.font.render(text, True, self.color)

    def draw(self, surface, pos=(0,0)):
        surface.blit(self.renderedText, pos)