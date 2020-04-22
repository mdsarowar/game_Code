import pygame
import random
pygame.init()

window_hight=800
window_width=600

white=(255,255,255)
red=(255,0,0)
black=(0,0,0)

window_screen=pygame.display.set_mode((window_hight,window_width))
pygame.display.set_caption('Snake Game')

clock=pygame.time.Clock()

exit_game=False
game_over=False
snake_x=45
snake_y=55
food_x = random.randint(10, window_width / 2)
food_y = random.randint(10, window_hight / 2)
valocity_x=0
valocity_y=0
snake_size=10
score=0
fps=40

while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game=True

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                valocity_x=5
                valocity_y=0

            if event.key==pygame.K_LEFT:
                valocity_x = -5
                valocity_y = 0

            if event.key==pygame.K_UP:
                valocity_x = 0
                valocity_y = -5                                                                                                                   

            if event.key==pygame.K_DOWN:
                valocity_x = 0
                valocity_y = 5

    snake_x=snake_x + valocity_x
    snake_y=snake_y + valocity_y
    if abs(snake_x - food_x )<8  and abs(snake_y -food_y )<8 :
        score=score+5
        print(score)
        food_x = random.randint(10, window_width-100)
        food_y = random.randint(10, window_hight-100)



    window_screen.fill(white)
    pygame.draw.rect(window_screen,black,[snake_x,snake_y,snake_size,snake_size])
    pygame.draw.rect(window_screen, red, [food_x, food_y, snake_size, snake_size])

    pygame.display.update()
    clock.tick(fps)
pygame.quit()
quit()