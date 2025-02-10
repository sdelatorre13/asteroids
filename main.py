import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    play_game = True
    while play_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play_game = False
        
        updatable.update(dt)

        screen.fill("BLACK")
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()

        dt = fps.tick(60) / 1000

if __name__ == "__main__":
    main()