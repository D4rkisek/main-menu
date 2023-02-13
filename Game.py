import pygame
import button
import crosshair
import dice
import player

# Initialize Pygame
pygame.init()
# Set screen size and title
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Catan")
# load the icon for the game
icon = pygame.image.load('icon.png').convert_alpha()
# add the icon
pygame.display.set_icon(icon)
###################### Universal instances ##################################################

# crosshair
pygame.mouse.set_visible(False)
# load crosshair image & create a crosshair object and add it to a sprite group
crosshair = crosshair.crosshair("cursor_fist.gif", "cursor.gif")
crosshair_group = pygame.sprite.Group(crosshair)
crosshair_group.add(crosshair)

# load button images
start_img = pygame.image.load('Play.png').convert_alpha()
quit_img = pygame.image.load('Quit.png').convert_alpha()
start_img2 = pygame.image.load('Play2.png').convert_alpha()
quit_img2 = pygame.image.load('Quit2.png').convert_alpha()

#regular button
reg_button = pygame.image.load('buttons.png').convert_alpha()

#################### Main menu Stage #####################################################
# load the background image for the main menu
background = pygame.image.load('landscape.jpg').convert_alpha()
# Scale the background image to fit the screen size
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# create button instances
start_button = button.Button(SCREEN_WIDTH/5, SCREEN_HEIGHT/2.5, start_img, start_img2)
quit_button = button.Button(SCREEN_WIDTH/1.8, SCREEN_HEIGHT/2.5, quit_img, quit_img2)
#################### Main menu Stage END #######################################################


#################### Game Stage ###############################################################
# create a button instance
quit_button2 = button.Button(SCREEN_WIDTH*0, SCREEN_HEIGHT*0, quit_img, quit_img2)
# roll the dice button
dice_roll = button.Button(SCREEN_WIDTH - reg_button.get_width(),
                          SCREEN_HEIGHT - reg_button.get_height(),
                          reg_button, reg_button)

# Player
# RBG value
BLACK = (0, 0, 0)
# Set the font size
font_size = 30
# Load the Pygame Serif font
font = pygame.font.Font(None, font_size)
# create a player instance
player1 = player.player("Mark", BLACK)

# die
dice1 = dice.dice(SCREEN_WIDTH/1.5, SCREEN_HEIGHT/2, 50)
# second die
dice2 = dice.dice(SCREEN_WIDTH/1.2, SCREEN_HEIGHT/2, 50)

######################## Game Stage END #######################################################

#################### Game Stage Function ######################################################
def game():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        ####################################################################
        # background colour
        screen.fill((79, 129, 189))

        # button
        if quit_button2.draw(screen):
            print('QUIT')
            running = False

        # Display the player's name and score
        player1.display(screen, font, 50, SCREEN_HEIGHT/4)

        # dice
        dice1.draw(screen)
        dice2.draw(screen)

        # roll the dice button
        if dice_roll.draw(screen):
            dice1.roll()
            dice2.roll()
            print('Dice value:', dice1.value + dice2.value)

        # crosshair
        crosshair_group.draw(screen)
        crosshair_group.update()
        #########################################################################
        pygame.display.update()

############################# Main Game Loop #################################################
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
        game()
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

