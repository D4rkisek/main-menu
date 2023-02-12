import pygame
import button
import crosshair

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


# crosshair
pygame.mouse.set_visible(False)
# load crosshair image & create a crosshair object and add it to a sprite group
crosshair = crosshair.crosshair("cursor_fist.gif", "cursor.gif")
crosshair_group = pygame.sprite.Group(crosshair)
crosshair_group.add(crosshair)
# Get a reference to the crosshair object from the group and call the switch_image() method on it
# crosshair = crosshair_group.sprites()[0] # get the first (and only) sprite in the group


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
    # buttons
    screen.blit(background, (0, 0))
    if start_button.draw(screen):
        print('START')
    if quit_button.draw(screen):
        print('QUIT')
        running = False

    # crosshair
    crosshair_group.draw(screen)
    crosshair_group.update()
    crosshair.switch_image([start_button, quit_button])
    #########################################################################
    pygame.display.update()
# Quit Pygame
pygame.quit()
