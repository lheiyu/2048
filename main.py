import pygame
import math
import random

pygame.init()
pygame.font.init()

FPS = 60
WIDTH, HEIGHT = 900, 900
BORDER_WIDTH = 20
BLOCK_WIDTH, BLOCK_HEIGHT = 200, 200

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BG_COLOUR = (205, 197, 154)
BORDER_COLOUR = (105, 99, 63)

blocks = [[2, 4, 8, 16],
          [0, 0, 0, 0], 
          [0, 0, 0, 0], 
          [0, 0, 0, 0]]
          


WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")

def draw_background():    
    WIN.fill((BG_COLOUR))
    for i in range(BORDER_WIDTH//2-1, HEIGHT+20, 200+BORDER_WIDTH):
        for j in range(BORDER_WIDTH//2-1, WIDTH+20, 200+BORDER_WIDTH):
            pygame.draw.line(WIN, BORDER_COLOUR, (0, i), (WIDTH, i), 20)
            pygame.draw.line(WIN, BORDER_COLOUR, (j, 0), (j, HEIGHT), 20)

def draw_blocks():
    for i, row in enumerate(blocks):
        for j, block in enumerate(row):
            if block != 0:
                pygame.draw.rect(WIN, (230, 220-math.log(block, 2)*10, 155), pygame.Rect(j*BLOCK_HEIGHT+(j+1)*BORDER_WIDTH, i*BLOCK_WIDTH+(i+1)*BORDER_WIDTH, BLOCK_WIDTH, BLOCK_HEIGHT))
                num = pygame.font.SysFont('times new roman', 50, True).render(str(block), True, BLACK)
                preset = BORDER_WIDTH + BLOCK_WIDTH//2
                num_width = num.get_width()
                num_height = num.get_height()
                WIN.blit(num, (preset+j*(BLOCK_WIDTH+BORDER_WIDTH)-num_width//2, preset+i*(BLOCK_HEIGHT+BORDER_WIDTH)-num_height//2))
                #WIN.blit(num, (BLOCK_WIDTH/2 + j*(BLOCK_WIDTH+BORDER_WIDTH), BLOCK_HEIGHT/2 + i*(BLOCK_HEIGHT+BORDER_WIDTH)))
                #fix pos of number

def run():
    clock = pygame.time.Clock()
    run = True
    
    global blocks
    
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        
        draw_background()
        draw_blocks()
        pygame.display.flip()
    

if __name__ == "__main__":
    run()