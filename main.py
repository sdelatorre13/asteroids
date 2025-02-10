import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    play_game = True
    while play_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("BLACK")
        pygame.display.flip()

if __name__ == "__main__":
    main()