import pygame


class Window:
    """Class for creating the snake game window"""

    def __init__(self, width=1000, height=800, RGB_colour=(255,255,255)):
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((self.width, self.height))
        self.window.fill((RGB_colour))
        pygame.display.set_caption("CFG SNAKE")
        pygame.display.update()

