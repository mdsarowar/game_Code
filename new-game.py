import pygame
import random
import os

pygame.mixer.init()


pygame.init()


screen_hight=700
screen_wedith=700

white = (102, 255, 178)
red = (255, 0, 0)
black = (0, 0, 0)

game_screen=pygame.display.set_mode((screen_wedith,screen_hight))
pygame.display.set_caption("new Snake game")

# imig=pygame.image.load("")
# imig=pygame.transform.scale(imig,(screen_wedith,screen_hight)).convert_alpha()

clock=pygame.time.Clock()


font=pygame.font.SysFont(None,50)

def snack_draw(scree,color,snake_list ,sn_size):
    for x,y in snake_list:
        pygame.draw.rect(scree, color, [x, y, sn_size, sn_size])

def food_draw(screen,color,hight,width,size):
    pygame.draw.rect(screen, color, [hight, width, size, size])

def Text(text,color,x,y):
    screen_text=font.render(text,True,color)
    game_screen.blit(screen_text,[x,y])
def welcome():
    exit_game=False

    while not exit_game:

        game_screen.fill(white)
        Text("welcome", black, 200, 300)
        for even in pygame.event.get():
            if even.type==pygame.QUIT:
                exit_game=True
            if even.type==pygame.KEYDOWN:
                if even.key==pygame.K_SPACE:
                    pygame.mixer.music.load('game_song.mp3')
                    pygame.mixer.music.play()
                    main_game()

        pygame.display.update()



def main_game():


    exit_game = False
    game_over=False
    snack_x = 20
    snack_y = 45
    snack_size = 10
    if(not os.path.exists('high_score.txt')):
        with open("high_score.txt","w") as i:
            i.write("0")


    with open("high_score.txt","r")as f:
        high_score=f.read()

    food_x = random.randint(10, (screen_hight - 100))
    food_y = random.randint(48, (screen_wedith - 100))
    food_size = 13

    fps = 40

    score = 0

    velocity_x = 0
    velocity_y = 0

    snake_list = []
    snake_length = 1

    while not exit_game:
        if game_over == True:
            if score > int(high_score):
                high_score = score
                game_screen.fill(white)
                Text("Congratulation  !! ", red, 200, 300)
                Text(" It is High Score ", red, 200, 350)
                Text("Your score is : " + str(score), red, 200, 400)




            elif score <int(high_score):
                game_screen.fill(white)
                Text("Game Over !",red,200,300)
                Text("Your score is : " + str(score), red, 150, 350)


            with open("high_score.txt", "w") as f:
                f.write(str(high_score))


            for even in pygame.event.get():
                if even.type ==pygame.QUIT:
                    exit_game=True

                if even.type == pygame.KEYDOWN:
                    if even.key == pygame.K_RETURN:
                        pygame.mixer.music.load('game_song.mp3')
                        pygame.mixer.music.play()
                        main_game()


            pygame.display.update()

        else:
            for even in pygame.event.get():
                if even.type ==pygame.QUIT:
                    exit_game=True

                if even.type == pygame.KEYDOWN:
                    if even.key == pygame.K_RIGHT:
                        velocity_x=5
                        velocity_y=0

                    if even.key == pygame.K_LEFT:
                        velocity_x=-5
                        velocity_y=0

                    if even.key == pygame.K_UP:
                        velocity_x=0
                        velocity_y=-5

                    if even.key == pygame.K_DOWN:
                        velocity_x=0
                        velocity_y=5


            if abs(snack_x-food_x)<12 and abs(snack_y - food_y)<12 :
                score = score+5
                food_x = random.randint(10, (screen_hight - 100))
                food_y = random.randint(48, (screen_wedith - 100))
                snake_length = snake_length + 5

                # if score > int(high_score):
                #     high_score=score


            snack_x=snack_x+velocity_x
            snack_y=snack_y+velocity_y

            head = []
            head.append(snack_x)
            head.append(snack_y)
            snake_list.append(head)

            if len(snake_list) > snake_length:
                del snake_list[0]

            if head in snake_list[:-1]:
                game_over=True



            if snack_x <0 or snack_x > screen_wedith or snack_y <0 or snack_y > screen_hight:
                game_over= True

            game_screen.fill(white)
            # game_screen.blit(imig,(0,0))
            Text("   Score : "+str(score)+"                         High_score : "+str(high_score),red,5,5)
            snack_draw(game_screen,black,snake_list ,snack_size)
            food_draw(game_screen,red,food_x,food_y,food_size)
        pygame.display.update()
        clock.tick(fps)


    pygame.quit()
    quit()
welcome()