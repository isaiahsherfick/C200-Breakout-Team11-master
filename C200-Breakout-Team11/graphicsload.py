import pygame,sys
#This is just all of our external images to help clean up our main loop.
start_one = pygame.image.load("graphics//startscreenbreakout.jpg")
start_two = pygame.image.load("graphics//startscreenbreakout2.jpg")
start_three = pygame.image.load("graphics//startscreenbreakout3.jpg")
level_two_screen =  pygame.image.load("graphics//level2.jpg")
level_three_screen =  pygame.image.load("graphics//level3.jpg")
level_four_screen =  pygame.image.load("graphics//level4.jpg")
level_five_screen =  pygame.image.load("graphics//level5.jpg")
start_screens = [start_one,start_two,start_three]
level_screens = [level_two_screen, level_three_screen, level_four_screen, level_five_screen]
win_screen = pygame.image.load("graphics//winscreen.jpg")
lose_screen = pygame.image.load("graphics//losescreen.jpg")
instructions_screen = pygame.image.load("graphics//instructions.jpg")