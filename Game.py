import pygame
import button

# Initialize Pygame
pygame.init()

# Set screen size and title
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Catan")
####################################################################
# load the background image for the main menu
background = pygame.image.load('landscape.jpg').convert_alpha()
# Scale the background image to fit the screen size
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# load the icon for the game
icon = pygame.image.load('icon.png').convert_alpha()
# add the icon
pygame.display.set_icon(icon)


# load button images
start_img = pygame.image.load('Play.png').convert_alpha()
quit_img = pygame.image.load('Quit.png').convert_alpha()
start_img2 = pygame.image.load('Play2.png').convert_alpha()
quit_img2 = pygame.image.load('Quit2.png').convert_alpha()
# create button instance
start_button = button.Button(SCREEN_WIDTH/5, SCREEN_HEIGHT/2.5, start_img, start_img2)
quit_button = button.Button(SCREEN_WIDTH/1.8, SCREEN_HEIGHT/2.5, quit_img, quit_img2)

######################################################################
# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    ####################################################################
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
