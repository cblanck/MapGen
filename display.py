#! /usr/bin/python
import os, sys, pygame, random
from tile import Tile

window_x = 640
window_y = 640

tile_width = 96
tile_height = 48
x_start = -tile_width
y_start = -tile_height

tiles_x = int(window_x/tile_width)*2
tiles_y = int(window_y/tile_height)*2

tile_names = ["tile_grass.png"]

def main():
    pygame.init()
    window_size = (window_x, window_y)
    window = pygame.display.set_mode(window_size)
    pygame.display.set_caption("MapGen")
    screen = pygame.display.get_surface()
    clock = pygame.time.Clock()
    tile_group = pygame.sprite.Group()
    tiles = [[None]*tiles_y]*tiles_x
    for i, ts in enumerate(tiles):
        for j, tile in enumerate(ts):
            tiles[i][j] = Tile(tile_group, image = random.choice(tile_names))
            tiles[i][j].rect.x = x_start + (tile_width/2)*i
            tiles[i][j].rect.y = y_start + (tile_height/2)*j
    while 1:
        time_passed = clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
        tile_group.draw(screen)
        pygame.display.flip()


if __name__=="__main__":
    main()
