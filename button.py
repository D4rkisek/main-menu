import pygame


# button class
class Button:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False # just a variable used for boolean values, i.e., a flag
        # get mouse's position
        pos = pygame.mouse.get_pos()
        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos): # is the cursor colliding the rectangle of the button
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:  # [0] means left click, [1] means middle click, [2] means right click
                self.clicked = True
                action = True

        # restarts the state of 'action' variable, so the program can register the button being clicked infinite times
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

        # this allows to use if statements in the draw() methods, because it returns boolean values
        return action