import pygame
import time
import random

pygame.init() #init() - Initializes pygame modules

clock = pygame.time.Clock()

#color codes in terms of RGB

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
orange = (255, 128, 0)

game_over = False
game_end = False

#size of the screen

display_width = 600
display_height = 400
dis = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Snake Game")
snake_block = 10
snake_list = []

#creating snake body
def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, red, [x[0], x[1], snake_block, snake_block])


#main func loop

def snake_game():
    game_over = False
    game_end = False
    # coordinates of the snake

    x1 = display_width / 2
    y1 = display_height / 2

    x1_change = 0
    y1_change = 0

    start = time.time()

    snake_list = []
    length_of_snake = 1
    snake_speed = 15

    paused = False

    foodx = round(random.randrange(0, display_width - snake_block)/10)*10
    foody = round(random.randrange(0, display_height - snake_block)/10)*10
    while not game_over:

        while game_end == True:

    #displaying score

            dis.fill(blue)
            font_style = pygame.font.SysFont("Ariel", 25)

            msg = font_style.render("You lost! Replay? Press P. To exit press Q", True, red)

            dis.blit(msg, [display_width / 6, display_height / 3])

            score = length_of_snake - 1
            score_font = pygame.font.SysFont("Ariel", 35)
            value = score_font.render("Score: " + str(score), True, green)
            dis.blit(value, [display_width / 3, display_height / 5])
            value = score_font.render("Time taken: " + str(time1) + " sec", True, green)
            dis.blit(value, [display_width / 3, display_height / 10])
            pygame.display.update()

    #asking if we want to play again or exit

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        snake_game()
                    if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                        game_over = True
                        game_end = False
    #entering directions

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    x1_change = 0
                    y1_change = -snake_block

                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    x1_change = -snake_block
                    y1_change = 0

                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    x1_change = snake_block
                    y1_change = 0

                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    x1_change = 0
                    y1_change = snake_block
                elif event.key == pygame.K_SPACE:
                    while not paused:
                        for event in pygame.event.get():

                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_c:
                                    paused = True

                                elif event.key == pygame.K_q:
                                    pygame.quit()
                                    quit()

                        dis.fill(orange)
                        pause_style = pygame.font.SysFont("Ariel", 25)

                        pause_msg = pause_style.render("Paused! continue? Press c. To exit press Q", True, black)

                        dis.blit(pause_msg, [display_width / 6, display_height / 3])
                        pygame.display.update()
            #if the snake hit boundaries - game over
        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_end = True

        x1 += x1_change
        y1 += y1_change

        dis.fill(black)
        #increasing snake's size after eating food

        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]
        for x in snake_list[:-1]:
            if x == snake_head:
                game_end = True
        snake(snake_block, snake_list)
        pygame.display.update()
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, display_width - snake_block)/10)*10
            foody = round(random.randrange(0, display_height - snake_block)/10)*10
            length_of_snake += 1
        #tracking speed of snake by clock module

        clock.tick(snake_speed)
        stop = time.time()
        time1 = int(stop - start)
    pygame.quit()
    quit()


snake_game()
