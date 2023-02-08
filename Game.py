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

    start_button.draw()
    quit_button.draw()
    #########################################################################

    screen.fill((36, 143, 191))
    pygame.display.update()

# Quit Pygame
pygame.quit()
