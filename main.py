import pygame
import random

pygame.init()

FPS = 60
WIDTH, HEIGHT = 900, 900
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BG_COLOUR = (205, 197, 154)
BORDER_COLOUR = (105, 99, 63)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")

def draw_gameplay():    
    WIN.fill((BG_COLOUR))
    
    
    pygame.display.flip()

def run():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        draw_gameplay()
    

if __name__ == "__main__":
    run()