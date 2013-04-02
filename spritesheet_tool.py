import pygame, sys
from pygame.locals import *

WIDTH   = 309
HEIGHT  = 199
SCALE   = 3
    
def main():
    pygame.init()
    pygame.display.set_caption("Spritesheet Tool")
    image = pygame.transform.scale(pygame.image.load('invader.png'), (WIDTH*SCALE, HEIGHT*SCALE))
    DISPLAYSURF = pygame.display.set_mode((WIDTH*SCALE, HEIGHT*SCALE))
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONUP:
                print (event.pos[0] / SCALE), (event.pos[1] / SCALE)
                
        DISPLAYSURF.blit(image, (0, 0))
        pygame.display.update()
        

if __name__ == '__main__':
    main()