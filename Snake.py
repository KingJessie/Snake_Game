import pygame


class Segment:
    """
    Create an object square with sides 20x20, color, position(coordinates) and direction attributes.
    It has methods move(to move itself in the given direction[change coordinates])
    and draw(to reveal itself on the screen).
    """
    side = 50

    def __init__(self, win, position, color):
        self.pos = position
        self.color = color
        self.image = pygame.image.load( "images/block2.jpg" ).convert()
        self.win = win


    def move(self, dir_x, dir_y):
        self.pos = (self.pos[0] + dir_x, self.pos[1] + dir_y)


    def draw(self):
        x_cor = self.pos[0]
        y_cor = self.pos[1]
        self.win.blit(self.image, (x_cor, y_cor))


class Snake:
    """
    An object that contains three other objects(squares) with position and color attributes.
    It has main methods: create snake, move, draw, extend.
    Accessory functions: add_segment, extend, reset, up, down, left, right.
    """

    def __init__(self, surface, color, pos):
        self.segments = []
        self.color = color
        self.create_snake(surface, pos)
        self.head = self.segments[0]
        self.dir_x = 1
        self.dir_y = 0
        self.surface = surface


    def create_snake(self,surface, pos):
        """
        Creates snake with given starts position.
        A loop that takes every pair position coordinates and pass them to the add_segment function.
        """
        for position in pos:
            self.add_segment(surface, position)

    def add_segment(self, surface, position):
        """
        Create a square object for given position.
        """
        new_segment = Segment(surface, position, self.color)
        self.segments.append(new_segment)

    def draw_snake(self):
        """
        Draw the snake segments on the screen.
        """
        for segment in self.segments:
            segment.draw()

    def extend(self):
        """
        Add one more segment to the snake body.
        """
        self.add_segment(self.surface, self.segments[-1].pos)

    def shrinks(self):
        self.segments.pop()

    def reset(self, pos):
        """ Delete the snake from the screen and draw the new one in the other direction(ex. if the walls collision). """
        self.segments.clear()
        self.create_snake(self.surface, pos)
        self.dir_x *= -1
        self.dir_y *= -1
        self.head = self.segments[0]

    def move(self, key):
        """
        The last segment takes coordinates the segment that is behind him,
        next segment takes coordinates the mext segment.
        The head moves on the distance that is the same as the new direction.
        """

        if key == pygame.K_UP:
            self.up()
        elif key == pygame.K_DOWN:
            self.down()
        elif key == pygame.K_RIGHT:
            self.right()
        elif key == pygame.K_LEFT:
            self.left()

        for segment in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[segment - 1].pos[0]
            new_y = self.segments[segment - 1].pos[1]
            self.segments[segment].pos = (new_x, new_y)
        self.head.move(self.dir_x * Segment.side, self.dir_y * Segment.side)


    def up(self):
        """
        Changing direction up. If the snake goes down it can't go up.
        """
        if self.dir_x != 0 and self.dir_y != 1:
            self.dir_x = 0
            self.dir_y = -1

    def down(self):
        """
        Changing direction down. If the snake goes up it can't go down.
        """
        if self.dir_x != 0 and self.dir_y != -1:
            self.dir_x = 0
            self.dir_y = 1

    def left(self):
        """
        Changing direction left. If the snake goes right it can't go left.
        """
        if self.dir_x != 1 and self.dir_y != 0:
            self.dir_x = -1
            self.dir_y = 0

    def right(self):
        """
        Changing direction right. If the snake goes left it can't go right.
        """
        if self.dir_x != -1 and self.dir_y != 0:
            self.dir_x = 1
            self.dir_y = 0
