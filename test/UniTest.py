from unittest import TestCase, main
from unittest.mock import patch
import pygame.constants
from Window import Window
from Snake import Segment, Snake




START_POSITIONS = [(250, 250), (200, 250), (150, 250)]


class TestSegment(TestCase):

    def setUp(self):
        self.window = Window()
        self.test_segment = Segment(self.window, (250, 250), color=(255, 255, 255))


    def test_segment_move(self):
        Expected_pos = (260, 260)
        self.test_segment.move(10, 10)
        self.assertEqual(Expected_pos, self.test_segment.pos)


class TestSnake(TestCase):

    def setUp(self):
        self.window = Window()
        self.test_snake = Snake(self.window, (0, 100, 0), START_POSITIONS)

    def test_create_snake(self):
        self.test_snake.segments = []
        self.test_snake.create_snake(self.window, START_POSITIONS)
        self.assertEqual(3, len(self.test_snake.segments))

    def test_add_segment(self):
        self.test_snake.segments = []
        self.test_snake.add_segment(self.window, START_POSITIONS[0])
        self.assertEqual(1, len(self.test_snake.segments))

    def test_extend(self):
        self.test_snake.extend()
        self.assertEqual(self.test_snake.segments[-2].pos, self.test_snake.segments[-1].pos)

    @patch('Snake.Segment.draw')
    def test_draw_snake(self, segment_draw):
        self.test_snake.draw_snake()
        self.assertEqual(segment_draw.call_count, len(self.test_snake.segments))


    def test_move_up(self):
        self.test_snake.dir_x, self.test_snake.dir_y = 1, 0
        self.test_snake.move(pygame.constants.K_UP)
        new_positions = [self.test_snake.segments[0].pos, self.test_snake.segments[1].pos, self.test_snake.segments[2].pos]
        expected_pos = [(250, 200), (250, 250), (200, 250)]
        self.assertEqual(expected_pos, new_positions)

    def test_move_down(self):
        self.test_snake.dir_x, self.test_snake.dir_y = 1, 0
        self.test_snake.move(pygame.constants.K_DOWN)
        new_positions = [self.test_snake.segments[0].pos, self.test_snake.segments[1].pos, self.test_snake.segments[2].pos]
        expected_pos = [(250, 300), (250, 250), (200, 250)]
        self.assertEqual(expected_pos, new_positions)

    def test_move_left(self):
        self.test_snake.segments[0].pos, self.test_snake.segments[1].pos, self.test_snake.segments[2].pos = [(100, 100), (100, 150), (100, 200)]
        self.test_snake.dir_x, self.test_snake.dir_y = 0, -1
        self.test_snake.move(pygame.constants.K_LEFT)
        new_positions = [self.test_snake.segments[0].pos, self.test_snake.segments[1].pos, self.test_snake.segments[2].pos]
        expected_pos = [(50, 100), (100, 100), (100, 150)]
        self.assertEqual(expected_pos, new_positions)

    def test_move_right(self):
        self.test_snake.segments[0].pos, self.test_snake.segments[1].pos, self.test_snake.segments[2].pos = [(100, 100), (100, 150), (100, 200)]
        self.test_snake.dir_x, self.test_snake.dir_y = 0, -1
        self.test_snake.move(pygame.constants.K_RIGHT)
        new_positions = [self.test_snake.segments[0].pos, self.test_snake.segments[1].pos, self.test_snake.segments[2].pos]
        expected_pos = [(150, 100), (100, 100), (100, 150)]
        self.assertEqual(expected_pos, new_positions)

    def test_reset(self):
        self.test_snake.add_segment(self.window, self.test_snake.segments[-1].pos)
        self.test_snake.add_segment(self.window, self.test_snake.segments[-1].pos)
        test_len_snake = len(self.test_snake.segments)
        test_cords = (self.test_snake.dir_x, self.test_snake.dir_y)
        self.test_snake.reset(START_POSITIONS)
        self.assertNotEqual((test_len_snake, test_cords), (len(self.test_snake.segments), (self.test_snake.dir_x, self.test_snake.dir_y)))


if __name__ == '__main__':
    main()