import pygame
import sys
import random

WINDOW_WIDTH=600
WINDOW_HEIGHT=600
GRID_SIZE=10
ROWS=WINDOW_HEIGHT//GRID_SIZE
COLUMNS=WINDOW_WIDTH//GRID_SIZE

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)



pygame.init()
window=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption('Falling Sand')
clock = pygame.time.Clock()

def make_grid(rows, columns):
    return [[(0,BLACK)] * columns for _ in range(rows)]

def Draw(window, grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j][0] == 1:
                color= grid[i][j][1]
                pygame.draw.rect(window, color, (j * GRID_SIZE, i * GRID_SIZE, GRID_SIZE, GRID_SIZE))



def Falling(grid):
    for i in range(len(grid)-2,-1,-1):
        for j in range(len(grid[0])):
            if i+4<ROWS and grid[i][j][0] ==1 and grid [i+4][j][0]==0:
                grid[i + 4][j] = grid[i][j]
                grid[i][j] = (0, BLACK)
            elif grid[i][j][0] ==1 and grid [i+1][j][0]==0 :
                grid[i + 1][j] = grid[i][j]
                grid[i][j] = (0, BLACK)
            elif j+1<COLUMNS and j-1>=0:
                if grid[i][j][0]==1 and grid[i+1][j][0]==1 and (grid[i+1][j+1][0]==0 or grid[i+1][j-1][0]==0):
                    if grid[i+1][j+1][0]==0:
                        grid[i+1][j+1]=grid [i][j]
                        grid [i][j]=(0,BLACK)
                    elif grid[i+1][j-1][0]==0:
                        grid[i+1][j-1]=grid[i][j]
                        grid [i][j]=(0,BLACK)
                    elif grid[i+1][j+1][0]==0 and grid[i+1][j-1][0]==0:
                        grid[i+1][j+random.choice([-1,1])]=grid [i][j]
                        grid [i][j]=(0,BLACK)

def mouse_pressed(grid, pos):
    x, y = pos
    row = y // GRID_SIZE
    column = x // GRID_SIZE
    if grid[row][column][0] == 0:
        if random.randint(0,100)<80:
            grid[row][column]=(1,Change_Color())
        else:
            for i in range(row - 2, row + 2):
                for j in range(column - 2, column + 2):
                    grid[i][j] = (1,Change_Color())


hue = 0

def Change_Color():
    global hue
    color = pygame.Color(0)
    color.hsva = (hue, 100, 100, 100)
    hue = (hue + 1) % 360  
    return color

def main():
    grid = make_grid(ROWS, COLUMNS)
    running = True
    mouse_down = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_down = True
                mouse_pressed(grid, event.pos)
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_down = False
            elif event.type == pygame.MOUSEMOTION and mouse_down:
                mouse_pressed(grid, event.pos)

        Falling(grid)
        
        window.fill(BLACK)
        Draw(window, grid)
        pygame.display.flip()
        clock.tick(10)

    pygame.quit()
    sys.exit()
if __name__ == "__main__":
    main()









