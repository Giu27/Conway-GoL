import pygame as pg, sys, random
from settings import *

def draw_on_screen(screen,tile_grid, comp_grid):
    cell_size = (WIDTH/TILE_GRID_WIDTH,HEIGHT/TILE_GRID_HEIGHT)
    for row in range(TILE_GRID_HEIGHT):
        if tile_grid[row] == comp_grid[row]:continue
        for column in range(TILE_GRID_WIDTH):
            cell_color = DEFAULT_COLORS[tile_grid[row][column]]
            cell_surface = pg.Surface(cell_size)
            cell_surface.fill(cell_color)
            cell_rect = cell_surface.get_frect(topleft = (cell_size[0] * column, cell_size[1] * row))
            screen.blit(cell_surface,cell_rect)

def update_tile_grid(tile_grid):
    new_tile_grid = tile_grid.copy()
    for i in range(TILE_GRID_HEIGHT):
        new_tile_grid[i] = tile_grid[i].copy()
    for i in range(100):
        indexes = (random.randint(0,TILE_GRID_HEIGHT - 1),random.randint(0,TILE_GRID_WIDTH - 1))
        new_tile_grid[indexes[0]][indexes[1]] = int(not new_tile_grid[indexes[0]][indexes[1]])
    return new_tile_grid

pg.init()

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Conway's Game of Life")

clock = pg.time.Clock()

prev_tile_grid = [[0 for _ in range(TILE_GRID_WIDTH)] for _ in range(TILE_GRID_HEIGHT)]

while (True):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    new_tile_grid = update_tile_grid(prev_tile_grid)
    draw_on_screen(screen,new_tile_grid,prev_tile_grid)
    prev_tile_grid = new_tile_grid.copy()

    if DEBUG:
        print(f"FPS: {int(clock.get_fps())}")

    clock.tick(FPS)
    pg.display.update()