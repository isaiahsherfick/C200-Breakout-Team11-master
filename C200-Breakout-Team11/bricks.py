import pygame
class brick(object):                                                           #defines a brick
    """a class that encompasses all of the bricks"""
    def __init__(self, position, width, height, file, side):
        """position tuple, width, height,the file for the image, whichside to break"""
        self.x = position[0]
        self.y = position[1]        
        self.height = width
        self.width = height
        self.rectangle = pygame.Rect((position[0],position[1]),(self.width,self.height))        #this will be the collision box
        self.image = pygame.image.load(file)
        self.side = side
    def append_to_list(self,list):                                                              #this is to append it to the current_level list at the start of a level
        list.append(self)
    def remove_from_list(self,list):                                                            #this is for deleting the brick after it has been hit
        list.remove(self)
    def fall(self,fall_speed):
        self.y += fall_speed
        self.rectangle = pygame.Rect((self.x,self.y),(self.width,self.height))



brick_images = {"1":"graphics//50x100bricks.jpg","2":"graphics//100x100bricks.jpg","3":"graphics//150x100bricks.jpg","4":"graphics//topbrick.jpg","5":"graphics//rightbrick.jpg","6":"graphics//bottombrick.jpg","7":"graphics//leftbrick.jpg"}       #A dictionary of brick images