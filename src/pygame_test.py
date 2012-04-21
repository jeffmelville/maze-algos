import pygame
import pygame.locals

import random
import sys
import time

def rand_color():
    return random.randint(0,255)

def main_loop():
    next_flip = 0.0
    while True:
        for event in pygame.event.get():
            print event
            if(event.type == pygame.QUIT):
                return

        if(time.time() > next_flip):
            newColor = (rand_color(), rand_color(), rand_color())
            screen.fill(newColor)
            pygame.display.flip()
            next_flip = time.time() + 0.5




if __name__=='__main__':
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    main_loop()
    pygame.display.quit()

    

