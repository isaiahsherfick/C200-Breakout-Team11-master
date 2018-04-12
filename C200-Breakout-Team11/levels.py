import pygame
from bricks import *

level_one = ["12 3  1113  2 112 2 ",                                                    #levels will go here. they are lists of strings where each string
             "12 12 3  12 13  2 11",]                                                    #represents a row of bricks. have to add white space after larger bricks to account
                                                                                        #for size
level_two = ["3  3  1113  2 113  1",
             "2 13  12 2 3  12 3  "]
level_three = ["2 2 13  12 2 3  3  1",
               "3  2 1112 3  2 3  2 ",
               "12 3  2 3  12 3  3  "]
level_four = ["3  12 3  13  3  112 ",
              "5  3  2 13  12 3  7 ",
              "13  6  3  6  2 3  11"]
level_five = ["3  4 3  4 3  4 2 12 ",
              "5  2 12 3  13  2 17 ",
              "15  2 16  3  6  117 "]

current_level = []

def load_level(level):
    """this is a function that reads the current level and loads the bricks into the current_level list"""
    global current_level
    x,y = 0,25
    for row in level:                                                                           #each string in the level is a row
        for column in row:                                                                      #each character is a column
            if column == "1":                                                                   #determines what brick to load
                brick((x,y),100,50,brick_images["1"],"all").append_to_list(current_level)
            if column == "2":
                brick((x,y),100,100,brick_images["2"],"all").append_to_list(current_level)
            if column == "3":
                brick((x,y),100,150,brick_images["3"],"all").append_to_list(current_level)
            if column == "4":
                brick((x,y),100,150,brick_images["4"],"top").append_to_list(current_level)
            if column == "5":
                brick((x,y),100,100,brick_images["5"],"right").append_to_list(current_level)
            if column == "6":
                brick((x,y),100,150,brick_images["6"],"bottom").append_to_list(current_level)
            if column == "7":
                brick((x,y),100,150,brick_images["7"],"left").append_to_list(current_level)
            x+=50
        y+=100
        x=0
    
    return current_level


def change_level(win,lvl):
    """this is a function that changes the level. call it when the level is going to change."""
    
                                                                                       #these load each level based upon the levels set above.
    if lvl == 2:                                                                       #and the change the variable that defines the number.
        load_level(level_two)
    if lvl == 3:
        load_level(level_three)
    if lvl == 4:
        load_level(level_four)
    if lvl == 5:
        load_level(level_five)
    
    



