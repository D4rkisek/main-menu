import pygame
import button



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
start_button = button.Button(250, 350, start_img)
quit_button = button.Button(670, 350, quit_img)

######################################################
# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #########################################################################
    screen.blit(background, (0, 0))
    if start_button.draw(screen):
        print('START')
    if quit_button.draw(screen):
        print('QUIT')
        running = False
    #########################################################################
    pygame.display.update()
# Quit Pygame
pygame.quit()
