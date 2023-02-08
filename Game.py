import pygame
import button

# button class
class Button:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):
        # draw button on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))


# Initialize Pygame
pygame.init()

# Set screen size and title
SCREEN_WIDTH = 1240
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main menu")
#####################################################
# load the background image
background = pygame.image.load('landscape.jpg').convert_alpha()
# Scale the background image to fit the screen size
background = pygame.transform.scale(background, (1240, 800))

# load button images
start_img = pygame.image.load('Play.png').convert_alpha()
quit_img = pygame.image.load('Quit.png').convert_alpha()
# create button instance
start_button = Button(100, 200, start_img)
quit_button = Button(450, 200, quit_img)

######################################################
# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #########################################################################
    screen.blit(background, (0, 0))
    start_button.draw()
    quit_button.draw()
    #########################################################################
    pygame.display.update()
# Quit Pygame
pygame.quit()
