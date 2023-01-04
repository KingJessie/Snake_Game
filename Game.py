import pygame

class Game:
    """A class for game set up, detecting game over criteria, and game scoring"""

    def __init__(self, surface, len_snake):
        pygame.init()
        self.surface = surface
        self.len_snake = len_snake
        self.speed = 200
        self.font = pygame.font.SysFont('arial', 30)
        pygame.mixer.init()
        self.play_background_music()


    def play_background_music(self):
        """ Music """
        pygame.mixer.music.load( 'sound/background_music.ogg' )
        pygame.mixer.music.play(-1, 0)


    def play_sound(self, sound_name):
        """ Sound effects """
        if sound_name == "crash":
            sound = pygame.mixer.Sound( "sound/crash.ogg" )
        elif sound_name == 'eatenfood':
            sound = pygame.mixer.Sound( "sound/eatenfood.ogg" )
        pygame.mixer.Sound.play(sound)


    def render_background(self):
        """ Background image """
        bg = pygame.image.load( "images/background_image.jpeg" )
        self.surface.blit(bg, (0, 0))
        # draw grid by using pygame drawing line method
        for i in range(0, 1000, 50):
            pygame.draw.line(self.surface, colors_dict['MAROON'], (0, i), (1000, i))
            pygame.draw.line(self.surface, colors_dict['NAVY'], (i, 0), (i, 1000))


    def is_collision(self, x1, y1, x2, y2, size):
        """ Is collision(too close) with wall/tail """
        if x1 >= x2 and x1 < x2 + size:
            if y1 >= y2 and y1 < y2 + size:
                return True
        return False


    def display_score(self, new_len_snake):
        """ Scoreboard for game surface """
        self.len_snake = new_len_snake
        self.score = self.font.render(f"Score: {self.len_snake - 3}", True, (200, 200, 200))
        self.surface.blit(self.score, (250, 10))


    def show_game_over(self, len_snake):
        """ Game over surface """
        self.render_background()
        line1 = self.font.render(f"GAME OVER! Your score is {self.len_snake - 3}", True, (255, 255, 255))
        self.surface.blit(line1, (200, 300))
        line2 = self.font.render("Press ENTER to Play Again. To leave the game press ESC", True, (255, 255, 255))
        self.surface.blit(line2, (200, 350))
        pygame.mixer.music.pause()
        pygame.display.flip()


    def check_speed(self):
        """ Check the snake segments length and increase the speed """
        if self.len_snake > 6:  # increasing speed
            new_speed = 195
        elif self.len_snake > 9:
            new_speed = 185
        elif self.len_snake > 12:
            new_speed = 170
        elif self.len_snake > 15:
            new_speed = 150
        return self.speed


""" Game's variables """
# Dictionary with pre-set colors
colors_dict = {
            'white': (255, 255, 255),
            'black': (0, 0, 0),
            'lilac': (204, 153, 255),
            'rust': (255, 153, 51),
            'nice_yellow': (255, 255, 204),
            'GREEN': (0, 100, 0),
            'MAROON': (102, 0, 0),
            'NAVY': (16, 78, 139),
            'BLUE': (0, 0, 180)
            }

START_POS = [(250, 250), (200, 250), (150, 250)]  # Start positions for first three segments

# move this into the game class?
def restart_game():
    """ function for restarting the game """
    pygame.event.clear()
    while True:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                return True
            if event.key == pygame.K_ESCAPE:
                return False
