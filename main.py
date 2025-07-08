import pygame as pg, sys, random
from settings import *

def draw_on_screen(screen,tile_grid, comp_grid):
    cell_size = ((WIDTH/TILE_GRID_WIDTH) - SIZE_OFFSET ,(HEIGHT/TILE_GRID_HEIGHT) - SIZE_OFFSET)
    for row in range(TILE_GRID_HEIGHT):
        if comp_grid:
            if tile_grid[row] == comp_grid[row]:continue
        for column in range(TILE_GRID_WIDTH):
            cell_color = DEFAULT_COLORS[tile_grid[row][column]]
            cell_surface = pg.Surface(cell_size)
            cell_surface.fill(cell_color)
            cell_rect = cell_surface.get_frect(topleft = ((cell_size[0] + SIZE_OFFSET) * column , (cell_size[1] + SIZE_OFFSET) * row))
            screen.blit(cell_surface,cell_rect)

def clear_grid(tile_grid):
    for i in range(TILE_GRID_HEIGHT):
        for j in range(TILE_GRID_WIDTH):
            tile_grid[i][j] = 0
    draw_on_screen(screen,tile_grid, [])

def update_cell(tile_grid,x,y):
    cell_state = tile_grid[y][x]
    neighbours = 0
    coords = (x - 1, y - 1)
    for i in range(3):
        if (coords[1] + i) < 0 or (coords[1] + i) >= TILE_GRID_HEIGHT: continue 
        for j in range(3):
           if (coords[0] + j) < 0 or (coords[0] + j) >= TILE_GRID_WIDTH: continue
           if coords[1] + i == y and coords[0] + j == x: continue
           if tile_grid[coords[1] + i][coords[0] + j]: neighbours += 1
    if cell_state:
        if neighbours < 2: 
            cell_state = 0
        elif neighbours > 3: 
            cell_state = 0
    else:
        if neighbours == 3: 
            cell_state = 1
    return cell_state

def update_tile_grid(tile_grid):
    new_tile_grid = tile_grid.copy()
    for i in range(TILE_GRID_HEIGHT):
        new_tile_grid[i] = tile_grid[i].copy()
        for j in range(TILE_GRID_WIDTH):
            new_tile_grid[i][j] = update_cell(tile_grid,j,i)
    return new_tile_grid

pg.init()

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Conway's Game of Life: paused")

clock = pg.time.Clock()

prev_tile_grid = [[0 for _ in range(TILE_GRID_WIDTH)] for _ in range(TILE_GRID_HEIGHT)]
for i in range(10000):
    coords = (random.randint(0,TILE_GRID_HEIGHT - 1),random.randint(0,TILE_GRID_WIDTH - 1))
    prev_tile_grid[coords[0]][coords[1]] = 1

draw_on_screen(screen,prev_tile_grid, [])

paused = True

while (True):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                paused = not paused
                if paused: pg.display.set_caption("Conway's Game of Life: paused")
                else: pg.display.set_caption("Conway's Game of Life: running")
            if event.key == pg.K_LCTRL:
                DEBUG = not DEBUG
            if event.key == pg.K_BACKSPACE:
                clear_grid(prev_tile_grid)
        if event.type == pg.MOUSEBUTTONDOWN:
            pass
        
    
    if not paused:
        screen.fill("black")
        if DEBUG: screen.fill(DEBUG_BACKGROUND_COLOR)
        new_tile_grid = update_tile_grid(prev_tile_grid)
        draw_on_screen(screen,new_tile_grid,prev_tile_grid)
        prev_tile_grid = new_tile_grid.copy()

    if DEBUG:
        print(f"FPS: {int(clock.get_fps())}")

    clock.tick(FPS)
    pg.display.update()