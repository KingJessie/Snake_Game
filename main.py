import pygame
from Window import Window
from Snake import Snake
from FoodandScore import Apple
from Game import Game, colors_dict, START_POS, restart_game
# from Player import Player


def reset():
    snake.reset(START_POS)
    food.move(snake.segments)
    pygame.mixer.music.unpause()
    game_functions.raw_score = 0


def update_window(surface):
    """
    Function that updates the screen every time through the loop for updating the picture.
    This function doesn't belong to any classes.
    """
    global snake, food
    game_functions.render_background()
    game_functions.display_score(len(snake.segments))
    snake.draw_snake()

    food.draw()
    pygame.display.flip()


if __name__ == "__main__":
    # getting instance of player class
    # player = Player()

    while True:
        answer = input('Are you ready to play? y/n: ')
        if answer == 'y' or answer == 'Y' or answer == 'yes':
            break

    pygame.init()
    window = Window()
    snake = Snake(window.window, colors_dict['nice_yellow'], START_POS)
    food = Apple(window.window, snake.segments)
    game_functions = Game(window.window, len(snake.segments))
    pygame.mixer.music.unpause()
    game_functions.play_background_music()

    game_running = True

    while game_running:
        update_window(window.window)

        key = None
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_running = False
                else:
                    key = event.key
                break
            elif event.type == pygame.QUIT:
                game_running = False
        snake.move(key)

        # snake has eaten an apple
        if game_functions.is_collision(snake.head.pos[0], snake.head.pos[1], food.x, food.y, food.SIZE):
            game_functions.play_sound("eatenfood")
            snake.extend()
            food.move(snake.segments)

        # detect wall - condition for what happens when snake collides with wall - game over
        if snake.head.pos[0] > window.width or snake.head.pos[0] < 0 or snake.head.pos[1] > window.height or snake.head.pos[1] < 0: # The snake should be reset, scoring should be reset and the new game starts.
            game_functions.play_sound('crash')
            game_functions.show_game_over(len(snake.segments))
            # logging player score in the DB
            player.log_score(len(snake.segments))
            game_running = restart_game()
            if game_running:
                reset()

        # detect tail
        for i in range(3, len(snake.segments)):
            if game_functions.is_collision(snake.head.pos[0], snake.head.pos[1], snake.segments[i].pos[0], snake.segments[i].pos[1], snake.head.side):
                    game_functions.play_sound('crash')
                    game_functions.show_game_over(len(snake.segments))
                    # logging player score in DB
                    player.log_score(len(snake.segments))
                    game_running = restart_game()
                    if game_running:
                        reset()
                        break

        pygame.time.wait(game_functions.speed)