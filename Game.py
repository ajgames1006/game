## import pygame
import pygame


## start pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    ## poll for events
    ## pygame.QUIT means a user clicked x to close the game
    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False

    #fill the screen to erase anything from last screen
    screen.fill("black")

    ## render game here

    # flip() the display to put your work on screen
    pygame.display.flip()

    #limits fps to 60
    clock.tick(60)

pygame.quit()