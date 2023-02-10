import pygame


# button class
class Button:
    def __init__(self, x, y, image, image2,):
        self.image = image
        self.image2 = image2
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.offset = 0

    def draw(self, surface):
        action = False  # just a variable used for boolean values, i.e., a flag
        # get mouse's position
        pos = pygame.mouse.get_pos()
        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):  # is the cursor colliding the rectangle of the button
            # draw the second button on screen
            surface.blit(self.image2, (self.rect.x, self.rect.y))

            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:  # [0] means left click, [1] means middle click, [2] means right click
                self.clicked = True
                action = True
                self.offset = 6
            elif pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
                self.offset = 0

            surface.blit(self.image2, (self.rect.x, self.rect.y + self.offset))
        else:  # draw the first button on screen
            surface.blit(self.image, (self.rect.x, self.rect.y))

        # restarts the state of 'action' variable, so the program can register the button being clicked infinite times
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False


        # this allows to use if statements in the draw() methods, because it returns boolean values
        return action
