import pygame
import time
import random
import os

pygame.init()
black=(0,0,0)
green=(100,255,178)
red=(255,0,0)
white=(255,255,255)
screen_width=550
screen_hight=500

clock=pygame.time.Clock()
font=pygame.font.SysFont(None,50)
game_screen=pygame.display.set_mode((screen_width,screen_hight))
pygame.display.update()

def snake(game_screen,green,snake_list,si):
    for x,y in snake_list:
        snake_head=pygame.draw.rect(game_screen,green,[x,y,si,si])


def food(g,r,x,y,fs):
    pygame.draw.rect(g,r,[x,y,fs,fs])


def text(t,c,x,y):
    screen_text=font.render(t,True,c)
    game_screen.blit(screen_text,[x,y])


def game_loop():
    snake_x=45
    snake_y=50
    snake_size=10
    food_x=random.randint(10,screen_width-50)
    food_y=random.randint(30,screen_width-50)
    food_size=13
    velosity_x=0
    velosity_y=0
    fps=30
    score=0

    snake_list=[]
    snake_length=1

    if not os.path.exists("up_score.txt"):
        with open("up_score.txt","w") as f:
            f.write("0")
    with open("up_score.txt","r") as f:
        high_score=f.read()
    exit_game=False
    game_over=False
    while not exit_game:
        if game_over==True:
            game_screen.fill(white)
            text("game over",red,200,250)
            for even in pygame.event.get():
                if even.type == pygame.QUIT:
                    exit_game=True

                if even.type==pygame.KEYDOWN:
                    if even.key==pygame.K_RETURN:
                        game_loop()
        else:
            for even in pygame.event.get():
                if even.type == pygame.QUIT:
                    exit_game=True

                if even.type==pygame.KEYDOWN:
                    if even.key==pygame.K_RIGHT:
                        velosity_x=5
                        velosity_y=0

                    if even.key==pygame.K_LEFT:
                        velosity_x=-5
                        velosity_y=0

                    if even.key==pygame.K_DOWN:
                        velosity_x=0
                        velosity_y=5

                    if even.key==pygame.K_UP:
                        velosity_x=0
                        velosity_y=-5

            snake_x=snake_x+velosity_x
            snake_y=snake_y+velosity_y
            if snake_x<0 or snake_x > screen_width or snake_y<0 or snake_y > screen_hight:
                game_over=True

            if abs(snake_x - food_x)<10 and abs(snake_y - food_y)<10:
                score=score+5
                food_x = random.randint(10, screen_width - 50)
                food_y = random.randint(30, screen_width - 50)
                snake_length=snake_length+5

            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list)>snake_length:
                del snake_list[0]

            if head in snake_list[:-1]:
                game_over=True



            game_screen.fill(white)
            text("score : "+ str(score),red,5,5)
            snake(game_screen, black, snake_list, snake_size)
            food(game_screen,red,food_x,food_y,food_size)

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
game_loop()