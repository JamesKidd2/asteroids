import pygame
import constants
from constants import *
pygame.init()

screen = pygame.display.set_mode((constants.SCREEN_WIDTH, 
                                  constants.SCREEN_HEIGHT))
def main():
    print("'Starting asteroids!'")
    print(f"'Screen width: {constants.SCREEN_WIDTH}'")
    print(f"'Screen height: {constants.SCREEN_HEIGHT}'")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill((0,0,0))
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()