import pygame
import sys
from pygame import mixer
from main import colors_dict

# general music setup
pygame.init()

# general parameters
width = 1000
height = 800

# background music
mixer.init()
mixer.music.load( 'sound/background_music.ogg' )
mixer.music.play()

# control how fast the game runs
clock = pygame.time.Clock()

# Display surface
screen = pygame.display.set_mode((width, height))
second_surface = pygame.Surface([width, height])

# Add logo to the window
"""icon = pygame.image.load('Screenshot 2022-05-05 at 18.47.48.png')
pygame.display.set_icon(icon)"""

class Background(pygame.sprite.Sprite):
    def __init__(self, image, location):
        #call Sprite initialiser
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load( "images/background_image.jpeg" )
        self.rect = self.image.get_rect(topleft=location)

second_surface = Background('background_image.jpeg', [0,0])

#  Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit ()
            sys.exit ()

    # notes - origin is in top left hand side, downwards to increase y
    # user to see the drawn elements
    screen.blit(second_surface.image, second_surface.rect)

    # keep display active using a loop
    for i in range (0, 1000, 50):
        pygame.draw.line(screen, (colors_dict['MAROON']), (0, i), (1000, i))
        pygame.draw.line(screen, (colors_dict['NAVY']), (i, 0), (i, 1000))

    pygame.display.update ()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
quit()

