import pygame
class paddle(object):
    """The paddle the player controls with WASD. There should only be one of these, but a class will keep things organized anyway."""
    def __init__(self):
        self.width = 200
        self.height = 50
        self.x = 300
        self.y = 525
        self.rectangle = pygame.Rect((self.x,self.y),(self.width,self.height))
    def move(self,direction):
        """Changes the paddle's x coordinate. Call this when checking for key press events in main.py and pass it int 0 for left, int 1 for right."""
        if direction == 0 and self.x > 0:
            self.x -= 10
            self.rectangle = pygame.Rect((self.x,self.y),(self.width,self.height))
        elif direction == 1 and self.x < 800:
            self.x += 10
            self.rectangle = pygame.Rect((self.x,self.y),(self.width,self.height))
        

