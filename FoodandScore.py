import pygame
import random

""" Here is only food. Score is in the Game file. """

class Apple:
    """A class for the apple that the snake must collide with to 'eat' it.
        After an apple is eaten, a new one appears in a random position on the game surface"""
    SIZE = 40

    def __init__(self, parent_screen, snake_segments):
        self.parent_screen = parent_screen
        self.image = pygame.image.load( "images/apple.png" )
        self.x = 1
        self.y = 1
        self.move(snake_segments)

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self, snake_segments):
        new_x = random.randrange(0, 950, 50)
        new_y = random.randrange(0, 750, 50)
        for each in snake_segments:
            if each.pos[0] == new_x and each.pos[1] == new_y:       # check the apple appears not on the snake body
                new_x = random.randrange(0, 950, 50)
                new_y = random.randrange(0, 750, 50)
        self.x = new_x
        self.y = new_y
        self.draw()