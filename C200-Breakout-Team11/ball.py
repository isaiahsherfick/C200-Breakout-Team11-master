import random 
import math
import pygame
import bricks
from paddle import *

random_pull_direction = (random.randint(0,801), 600)                                                #this gives the ball a random direction downwards when it spawns in.




class ball(object):
    """The ball. Moves with simple linear behavior involving x and y coordinates. Call ball.update() every frame."""
    def __init__(self,surface,radius,color):
        self.x = random.randint(0,1001)
        self.y = 400
        self.speed = 5
        self.dy = self.y - random_pull_direction[1]
        self.dx = self.x - random_pull_direction[0]
        self.dz = math.sqrt(self.dx**2 + self.dy**2)
        self.speed_x = self.dx/self.dz * self.speed
        self.speed_y = (self.dy/self.dz * self.speed)
        self.surface = surface
        self.radius = radius
        self.color = color
        
        while abs(self.speed_x) < 2:
            new_pull_direction = (random.randint(0,801), 600)  
            self.dy = self.y - new_pull_direction[1]
            self.dx = self.x - new_pull_direction[0]
            self.dz = math.sqrt(self.dx**2 + self.dy**2)
            self.speed_x = self.dx/self.dz * self.speed
            self.speed_y = -(self.dy/self.dz * self.speed)

    def update(self, collisionobjects=[]):
        self.y += self.speed_y
        self.x += self.speed_x
        if self.x >= 988:
            if self.speed_x > 0:
                self.speed_x *= -1
        elif self.x <= 12:
            if self.speed_x <0:
                self.speed_x *= -1
        if self.y <= 12:
            self.speed_y *= -1
        elif self.y >= 788:
            self.speed_y *= -1

def which_side(ball, brick, brick_list):
    """This is our collision detection system. It detects what side of the brick it hit, and respondes acordingly."""
    top_distance = abs(brick.rectangle.top - (ball.y + ball.radius))                                                                        #These variables are set to the distance between
    bottom_distance = abs(brick.rectangle.bottom - ball.y + ball.radius)                                                                    #the sides and the edges of the ball.
    left_distance = abs(brick.rectangle.left - ball.x + ball.radius)
    right_distance = abs(brick.rectangle.right - ball.x + ball.radius)
    sides_distance = [top_distance,bottom_distance,left_distance,right_distance]                                                            #we put these variables in a list and then find the closest side.
    shortest_side = min(sides_distance)
    if shortest_side == top_distance:
        ball.speed_y *= -1
        if brick.side == "top":
            brick.remove_from_list(brick_list)
            return 20 #Each of these returns 20 because that's how many points the player gets for destroying a brick.
    if shortest_side == bottom_distance:                                                                   #how the ball reacts based on the side we hit.
        ball.speed_y *= -1
        if brick.side == "bottom":
            brick.remove_from_list(brick_list)
            return 20
    if shortest_side == left_distance:
        ball.speed_x *= -1
        if brick.side == "left":
            brick.remove_from_list(brick_list)
            return 20
    if shortest_side == right_distance:
        ball.speed_x *= -1
        if brick.side == "right":
            brick.remove_from_list(brick_list)
            return 20
    if brick.side == "all":
            brick.remove_from_list(brick_list)
            return 20
    return 0

def paddle_location(real_ball,real_paddle):
    """This is the collision detection for the paddle and the ball. It checks the position of the ball relative to the top of the paddle."""
    if real_ball.y + real_ball.radius >= real_paddle.rectangle.top:
        
        if real_ball.x >= real_paddle.rectangle.left and real_ball.x < real_paddle.rectangle.left + 66:                                     #checks to se what segment of the paddle the ball hit, and 
            if real_ball.speed_x > 0:                                                                                                       #the ball reacts according to each segment.
                real_ball.speed_x *= -1
                real_ball.speed_y *= -1
            else:
                real_ball.speed_y *= -1
        if real_ball.x >= real_paddle.rectangle.left + 66 and real_ball.x < real_paddle.rectangle.left + 122:
            real_ball.speed_y *= -1
        if real_ball.x >= real_paddle.rectangle.left + 123 and real_ball.x < real_paddle.rectangle.left + 200:
            if real_ball.speed_x > 0:
                real_ball.speed_y *= -1
            else:
                real_ball.speed_x *= -1
                real_ball.speed_y *= -1
       




