import pygame, sys, math, time                                                  #imports 
from pygame.locals import *
from bricks import *
from levels import *
from paddle import *
from ball import *
from savescore import *
from graphicsload import *
pygame.init()                                                                   #initializing pygame

pygame.font.init()

font = pygame.font.SysFont("Impact", 150)
score_font = pygame.font.SysFont("Impact", 40)
clock = pygame.time.Clock()                                                     #setting the clock
window_height, window_width = 600, 1000                                         #setting the window
window = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("BreakOut!")
real_ball = ball(window,12,(200,45,45))
real_paddle = paddle()
load_level(level_one)
win = False
lose = False
level_number = 1
fall_speed = level_number / 60
start = True
start_animation_number = 0
start_counter = 0
player_score = 0
view_scores = False
player_name = ("","")
game_over = False
player_lives = 3
elapsed_time = 0
instructions = False

def update_lives():                                     
    global player_lives, real_ball

    player_lives -= 1
    time_of_loss = time.time()
    while time.time() - time_of_loss < 3:
        lost_surface = font.render("BALL LOST", False, (255,255,255))  #This function runs when a player loses a life. It pauses the game for 3 seconds and reinitializes the ball.
        window.blit(lost_surface,(200,200))
        pygame.display.update()
    real_ball.__init__(window,12,(200,45,45))


                                                                #These functions (show_lives through show_time) update relevent information to the player and draw it to the screen.
def show_lives():
    global player_lives
    lives_surface = score_font.render("Lives: " + str(player_lives),False,(255,255,255))
    window.blit(lives_surface,(850,0))

def show_score():
    global player_score
    score_surface = score_font.render("Score: " + str(player_score),False,(255,255,255))
    window.blit(score_surface,(5,0))

def show_time(start_time):
    global elapsed_time
    elapsed_time = int(time.time() - start_time)
    time_surface = score_font.render(str(elapsed_time),False,(255,255,255))
    window.blit(time_surface,(475,0))

def input_name():  #This hideous monstrosity of a function is the only way we could think of implementing a player entering their name for the high score. Father forgive us for our sins
    done = False
    player_name = ""
    while done == False:
        player_name = str.upper(player_name)
        name_surface = font.render(player_name,False,(113,22,22))   
        if lose == True:
            window.blit(lose_screen,(0,0))
        else:
            window.blit(win_screen, (0,0))
        window.blit(name_surface,(350,300))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and len(player_name) == 3:
                    done = True
                    view_highscores = True
                if event.key == pygame.K_BACKSPACE:
                    player_name = player_name[0:len(player_name)-1]
                if len(player_name) < 3:
                    if event.key == pygame.K_q:
                        player_name += "q"
                    if event.key == pygame.K_w:
                        player_name += "w"
                    if event.key == pygame.K_e:
                        player_name += "e"
                    if event.key == pygame.K_r:
                        player_name += "r"
                    if event.key == pygame.K_t:
                        player_name += "t"
                    if event.key == pygame.K_y:
                        player_name += "y"
                    if event.key == pygame.K_u:
                        player_name += "u"
                    if event.key == pygame.K_i:
                        player_name += "i"
                    if event.key == pygame.K_o:
                        player_name += "o"
                    if event.key == pygame.K_p:
                        player_name += "p"
                    if event.key == pygame.K_a:
                        player_name += "a"
                    if event.key == pygame.K_s:
                        player_name += "s"
                    if event.key == pygame.K_d:     #Yup, that's every letter of the alphabet. Just pretend it isn't there. It's better that way.
                        player_name += "d"
                    if event.key == pygame.K_f:
                        player_name += "f"
                    if event.key == pygame.K_g:
                        player_name += "g"
                    if event.key == pygame.K_h:
                        player_name += "h"
                    if event.key == pygame.K_j:
                        player_name += "j"
                    if event.key == pygame.K_k:
                        player_name += "k"
                    if event.key == pygame.K_l:
                        player_name += "l"
                    if event.key == pygame.K_z:
                        player_name += "z"
                    if event.key == pygame.K_x:
                        player_name += "x"
                    if event.key == pygame.K_c:
                        player_name += "c"
                    if event.key == pygame.K_v:
                        player_name += "v"
                    if event.key == pygame.K_b:
                        player_name += "b"
                    if event.key == pygame.K_n:
                        player_name += "n"
                    if event.key == pygame.K_m:
                        player_name += "m"
    return (name_surface, player_name)         

def level_pause(bricklist, levelnumber,levelscreens):
   global level_number,win,real_ball,level_number,fall_speed
   while bricklist == []:
        if level_number < 5:
            window.blit(levelscreens[(level_number-1)],(0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()                                           #This shows the relevent pre-level information after a player completes a level, and it loads the next level.
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    level_number +=1
                    change_level(win,level_number)
                    real_ball.__init__(window,12,(200,45,45))
                    fall_speed = level_number/60
  
time_initialized = False
while True:                                                                     #Main Game Loop
    while start:
        window.fill((0,0,0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    start = False
                if event.key == pygame.K_w:
                    view_scores = True              #Controls the player has access to on the start screen
                    start = False
                if event.key == pygame.K_s:
                    instructions = True
                    start = False
        start_animation_number += 1
        if start_animation_number >= 15:
            if start_counter == 0:
                start_animation_number = 0
                start_counter = 1
            elif start_counter == 1:               #Cute little animation for the start screen
                start_animation_number = 0
                start_counter = 2
            elif start_counter == 2:
                start_animation_number = 0
                start_counter = 0 
        window.blit(start_screens[start_counter],(0,0))

        pygame.display.update()
        clock.tick(60)
    while view_scores:
        window.fill((61,12,12))
        score_list = view_highscores(player_name[1],str(player_score))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_highscores(score_list)
                pygame.quit()
                sys.exit()                          #Shows the high score screen

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and game_over == False:
                    score_y = 10
                    save_highscores(score_list)
                    start = True
                    view_scores = False

                    
            
            score_x,score_y = 400,10
            for score in score_list:
                score_surface = score_font.render(score,False,(113,22,22))
                window.blit(score_surface,(score_x,score_y))
                score_y +=50
            pygame.display.update()
    while instructions:
        window.blit(instructions_screen,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_highscores(score_list)
                pygame.quit()
                sys.exit()
                                                        #Code that runs while the player is viewing the instructions.
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s and game_over == False:
                    start = True
                    instructions = False
        pygame.display.update()
    if start == False and instructions == False and view_scores == False:
        if player_lives <= 0:
            lose = True
        window.fill((0,0,0))

        if level_number == 5 and current_level == []:
            win = True 
        
        for event in pygame.event.get():                                            #exiting the game
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = True
                    while paused:
                        pause_surface = font.render("PAUSED",False,(200,50,50))
                        window.blit(pause_surface,(250,200))
                        pygame.display.update()
                        for event in pygame.event.get():                                            #exiting the game
                            if event.type == pygame.QUIT:
                                 pygame.quit()
                                 sys.exit()
                            if event.type == pygame.KEYDOWN:
                                 if event.key == pygame.K_p:
                                     paused  = False
        key = pygame.key.get_pressed()
        if key[pygame.K_a] or key[pygame.K_LEFT]:
            real_paddle.move(0)
        if key[pygame.K_d] or key[pygame.K_RIGHT]:
            real_paddle.move(1)
        pygame.draw.rect(window,(200,50,50),(real_paddle.rectangle)) 
    
        for brick in current_level:                                                 #Blits every brick in the current level to the screen
            window.blit(brick.image,(brick.x,brick.y))
        pygame.draw.circle(real_ball.surface,real_ball.color,(int(real_ball.x),int(real_ball.y)),real_ball.radius)  #Draws the ball which was initialized earlier using attributes of the ball object
    
        real_ball.update()
        if real_ball.y >= 630:
            update_lives()
        for brick in current_level:                                                 #Checks to see if the ball is touching the side of a brick. If so, removes the brick from the current level and causes the ball to behave appropriately.
            if real_ball.y - real_ball.radius <= brick.rectangle.bottom and real_ball.y + real_ball.radius >= brick.rectangle.top:
                if real_ball.x + real_ball.radius >= brick.rectangle.left and real_ball.x - real_ball.radius <= brick.rectangle.right:
                    player_score += which_side(real_ball,brick,current_level)
        paddle_location(real_ball,real_paddle)
        if level_number > 1:
            for brick in current_level:             #Every level after 1 has a falling element. Speed increases linearly depending on level.
                brick.fall(fall_speed,)
        if level_number < 5:
            level_pause(current_level,level_number,level_screens)
        for brick in current_level:
            if brick.y >= 500:
                lose = True
        show_score()
        show_lives()
        if time_initialized == False:
            start_time = time.time()        #You don't wanna store the time on every iteration of the loop, now do you?
            time_initialized = True
        show_time(start_time)
 
                


    
        if win == True:
            name_entered = False
            game_over = True
            while win:
                window.fill((0,0,0))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()                  #This loop is entered when the player beats the fifth level and allows them to write their name using the input_name() function and view high scores
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            win = False
                            view_scores = True
                            break
                window.blit(win_screen,(0,0))
                pygame.display.update()
                if name_entered == False:
                    player_name = input_name()
                    name_entered = True
                window.blit(player_name[0],(350,300))
                pygame.display.update()
                clock.tick(60)
        if lose == True:
            game_over = True
            name_entered = False
            while lose:
                window.fill((0,0,0))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()                  #Literally the same thing as the win loop with a different screen
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            view_scores = True
                            lose = False
                            break
                window.blit(lose_screen,(0,0))
                pygame.display.update()
                if name_entered == False:
                    player_name = input_name()
                    name_entered = True
                window.blit(player_name[0],(350,300))
                pygame.display.update()
                clock.tick(60)
    
        pygame.display.update()                                                   #updating the screen
        clock.tick(60)
    
