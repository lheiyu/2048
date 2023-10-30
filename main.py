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

blocks = [[0, 0, 0, 0],
          [0, 0, 0, 0], 
          [0, 0, 0, 0], 
          [0, 0, 0, 0]]

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")

def draw_background():    
    WIN.fill((BG_COLOUR))
    for y in range(BORDER_WIDTH//2-1, HEIGHT+20, 200+BORDER_WIDTH):
        for x in range(BORDER_WIDTH//2-1, WIDTH+20, 200+BORDER_WIDTH):
            pygame.draw.line(WIN, BORDER_COLOUR, (0, y), (WIDTH, y), 20)
            pygame.draw.line(WIN, BORDER_COLOUR, (x, 0), (x, HEIGHT), 20)

def draw_blocks():
    for y, row in enumerate(blocks):
        for x, block in enumerate(row):
            if block != 0:
                pygame.draw.rect(WIN, (230, 220-math.log(block, 2)*10, 155), pygame.Rect(x*BLOCK_HEIGHT+(x+1)*BORDER_WIDTH, y*BLOCK_WIDTH+(y+1)*BORDER_WIDTH, BLOCK_WIDTH, BLOCK_HEIGHT))
                num = pygame.font.SysFont('times new roman', 50, True).render(str(block), True, BLACK)
                preset = BORDER_WIDTH + BLOCK_WIDTH//2
                num_width = num.get_width()
                num_height = num.get_height()
                WIN.blit(num, (preset+x*(BLOCK_WIDTH+BORDER_WIDTH)-num_width//2, preset+y*(BLOCK_HEIGHT+BORDER_WIDTH)-num_height//2))

def init_game():
    new_numbers = [2, 4]
    free_pos = []
    for y, row in enumerate(blocks):
        for x, col in enumerate(row):
            if col == 0:
                free_pos.append([x, y])
    print(free_pos)
    random_block = free_pos[random.randint(0, len(free_pos)-1)]
    random_num = new_numbers[random.randint(0, len(new_numbers)-1)]
    blocks[random_block[1]][random_block[0]] = random_num


def run():
    clock = pygame.time.Clock()
    run = True
    init_game()
    
    
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