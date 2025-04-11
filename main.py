# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}") 
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()

    clock = pygame.time.Clock()


    updatable = pygame.sprite.Group() # group holding objects to be updated
    drawable = pygame.sprite.Group() # group holding objects to be drawn

    Player.containers = (updatable, drawable) # create Player objects AFTER this static field is made!

    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    dt = 0 # delta time

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # GAME LOOP BEGINS HERE
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        

        # DRAW SCREEN
        updatable.update(dt) # update all objects in the updatable group

        screen.fill("black")

        # draw each object in the drawable group
        for obj in drawable:
            obj.draw(screen)

        # TIME MANAGEMENT
        # refresh the screen
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()