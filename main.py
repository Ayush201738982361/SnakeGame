import pygame
import random

pygame.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
blue = (0, 0, 102)

# Creating window
screen_width = 700
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption("SnakeGame")
pygame.display.update()

# Game specific variables
exit_game = False
game_over = False
snake_x = 45
snake_y = 55
velocity_x = 0
velocity_y = 0

food_x = random.randint(20, screen_width // 1.5)
food_y = random.randint(20, screen_height // 1.5)
food_size = 20
score = 0
init_velocity = 5
snake_size = 30
fps = 60
font = pygame.font.SysFont(None, 55)

snk_list = []
snk_length = 1

clock = pygame.time.Clock()

def score_text(text, color, x, y):
    font_text = font.render(text, True, color)
    gameWindow.blit(font_text, [x, y])

def plot_snake(gameWindow, blue, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(gameWindow, blue, [x, y, snake_size, snake_size])

def gameloop():
    global exit_game
    global game_over
    global snake_x
    global snake_y
    global velocity_x
    global velocity_y
    global food_x
    global food_y
    global score
    global init_velocity
    global snake_size
    global snk_list
    global snk_length

    # Game Loop
    while not exit_game:
        if game_over:
            gameWindow.fill(white)
            score_text("Oops! Game Over, Better Luck Next Time", red, screen_width // 6.5, screen_height // 2.5)
            score_text("Press Enter to Continue", red, screen_width // 2.8, screen_height // 2)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

            snake_x += velocity_x
            snake_y += velocity_y

            if abs(snake_x - food_x) < 15 and abs(snake_y - food_y) < 15:
                score += 10
                food_x = random.randint(20, screen_width // 1.5)
                food_y = random.randint(20, screen_height // 1.5)
                snk_length += 3.5


        gameWindow.fill(black)
        score_text("Score: " + str(score), white, 5, 5)
        pygame.draw.rect(gameWindow, red, [food_x, food_y, food_size, food_size])

        head = []
        head.append(snake_x)
        head.append(snake_y)
        snk_list.append(head)

        if len(snk_list) > snk_length:
            del snk_list[0]

        if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
            game_over = True

        plot_snake(gameWindow, blue, snk_list, snake_size)

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

gameloop()
