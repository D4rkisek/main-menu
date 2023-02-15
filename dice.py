import pygame
import random

class dice:
    def __init__(self, x, y, size):
        # Initialize the class with the necessary variables.
        self.x = x
        self.y = y
        self.size = size
        self.value = 1
        # Load the images for each side of the die.
        self.images = {
            1: pygame.image.load('Graphics/dice/diceOne.png'),
            2: pygame.image.load('Graphics/dice/diceTwo.png'),
            3: pygame.image.load('Graphics/dice/diceThree.png'),
            4: pygame.image.load('Graphics/dice/diceFour.png'),
            5: pygame.image.load('Graphics/dice/diceFive.png'),
            6: pygame.image.load('Graphics/dice/diceSix.png')
        }


    def roll(self):
        # Generate a random number between 1 and 6 for the value of the die.
        self.value = random.randint(1, 6)
    def draw(self, surface):
        # Draw the image for the current value of the die on the screen.
        image = self.images[self.value]
        image = pygame.transform.scale(image, (self.size, self.size))
        surface.blit(image, (self.x, self.y))