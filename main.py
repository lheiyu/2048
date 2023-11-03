import pygame
import math
import random

pygame.init()
pygame.font.init()

FPS = 60
WIDTH, HEIGHT = 650, 650
BORDER_WIDTH = 10
BLOCK_WIDTH, BLOCK_HEIGHT = 150, 150

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BG_COLOUR = (205, 197, 154)
BORDER_COLOUR = (105, 99, 63)
BLOCK_COLOURS = ["#fcefe6", "#f2e8cb" , "#f5b682", "#f29446", "#ff775c", "#e64c2e", "#ede291", "#fce130", "#ffdb4a", "#f0b922", "#fad74d"]              

blocks = [[0, 0, 0, 0],
          [0, 0, 0, 0], 
          [0, 0, 0, 0], 
          [0, 0, 0, 0]]

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")

def draw_background():    
    WIN.fill((BG_COLOUR))
    for y in range(BORDER_WIDTH//2-1, HEIGHT+20, BLOCK_WIDTH+BORDER_WIDTH):
        for x in range(BORDER_WIDTH//2-1, WIDTH+20, BLOCK_HEIGHT+BORDER_WIDTH):
            pygame.draw.line(WIN, BORDER_COLOUR, (0, y), (WIDTH, y), 20)
            pygame.draw.line(WIN, BORDER_COLOUR, (x, 0), (x, HEIGHT), 20)

def draw_blocks():
    for y, row in enumerate(blocks):
        for x, block in enumerate(row):
            if block != 0:
                pygame.draw.rect(WIN, BLOCK_COLOURS[int(math.log(block, 2))], 
                                 pygame.Rect(x*BLOCK_HEIGHT+(x+1)*BORDER_WIDTH, y*BLOCK_WIDTH+(y+1)*BORDER_WIDTH, BLOCK_WIDTH, BLOCK_HEIGHT))
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
    random_block = free_pos[random.randint(0, len(free_pos)-1)]
    random_num = new_numbers[random.randint(0, len(new_numbers)-1)]
    blocks[random_block[1]][random_block[0]] = random_num


def up(blocks):
    for y, row in enumerate(blocks):
        for x, col in enumerate(row):
            if 4 > y > 0:
                if col != 0:
                    current_y = y
                    while blocks[current_y-1][x] == 0 and current_y > 0:
                        blocks[current_y-1][x] = blocks[current_y][x]
                        blocks[current_y][x] = 0
                        current_y -= 1                    
                    
def up_merge(blocks):
    for y, row in enumerate(blocks):
        for x, col in enumerate(row):
            if y < len(blocks) - 1 and col == blocks[y+1][x] and col!= 0:
                    blocks[y][x] *= 2
                    blocks[y+1][x] = 0
                    up(blocks)
                               

def left(blocks):
    for y, row in enumerate(blocks):
        for x, col in enumerate(row):
            if 4 > x > 0:
                if col != 0:
                    current_x = x
                    while blocks[y][current_x-1] == 0 and current_x > 0:
                        blocks[y][current_x-1] = blocks[y][current_x]
                        blocks[y][current_x] = 0
                        current_x -= 1
                        
def left_merge(blocks):
    for y, row in enumerate(blocks):
        for x, col in enumerate(row):
            if x < len(row) - 1 and col == blocks[y][x+1] and col != 0:
                    blocks[y][x] *= 2
                    blocks[y][x+1] = 0
                    left(blocks)
                        

def down(blocks):
    for y in range(len(blocks)-1, -1, -1):
        row = blocks[y]
        for x in range(len(row)-1, -1, -1):
            col = blocks[y][x]
            if 3 > y >= 0:
                if col != 0:
                    current_y = y
                    while current_y < 3 and blocks[current_y+1][x] == 0:
                        blocks[current_y+1][x] = blocks[current_y][x]
                        blocks[current_y][x] = 0
                        current_y = current_y + 1
                        
def down_merge(blocks):
    for y in range(len(blocks)-1, 0, -1):
        row = blocks[y]
        for x in range(len(row)-1, -1, -1):
            col = blocks[y][x]
            if y > 0 and col == blocks[y-1][x] and col != 0:
                blocks[y][x] *= 2
                blocks[y-1][x] = 0
                down(blocks)
                
                        
def right(blocks):
    for y in range(len(blocks)-1, -1, -1):
        row = blocks[y]
        for x in range(len(row)-1, -1, -1):
            col = blocks[y][x]
            if 3 > x >= 0:  
                if col != 0:
                    current_x = x
                    while current_x < 3 and blocks[y][current_x+1] == 0:
                        blocks[y][current_x+1] = blocks[y][current_x]
                        blocks[y][current_x] = 0
                        current_x = current_x + 1
                        
def right_merge(blocks):
    for y in range(len(blocks)-1, -1, -1):
        row = blocks[y]
        for x in range(len(row)-1, 0, -1):
            col = blocks[y][x]
            if x > 0 and col == blocks[y][x-1] and col != 0:
                blocks[y][x] *= 2
                blocks[y][x-1] = 0
                right(blocks)



def run():
    #run once only
    clock = pygame.time.Clock()
    run = True
    init_game()
    
    #loops
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    up(blocks)
                    up_merge(blocks)
                    init_game()
                if event.key == pygame.K_DOWN:
                    down(blocks)
                    down_merge(blocks)
                    init_game()
                if event.key == pygame.K_LEFT:
                    left(blocks)
                    left_merge(blocks)
                    init_game()
                if event.key == pygame.K_RIGHT:
                    right(blocks)
                    right_merge(blocks)
                    init_game()
                
        draw_background()
        draw_blocks()
        pygame.display.flip()

if __name__ == "__main__":
    run()