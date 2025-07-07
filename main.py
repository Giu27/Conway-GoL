import pygame as pg, sys
from settings import *

pg.init()

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Conwat's Game of Life")

clock = pg.time.Clock()

while (True):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    
    if DEBUG:
        print(f"FPS: {int(clock.get_fps())}")

    clock.tick(FPS)
    pg.display.update()