#! /usr/bin/python
import os, sys, pygame, random
from tile import Tile

window_x = 640
window_y = 640

tiles_x = 20
tiles_y = 20

tile_names = ["grass1.jpg", "grass2.jpg", "grass3.jpg", "flower.jpg", "tree.jpg", "stump.jpg"]

def main():
    pygame.init()
    window_size = (window_x, window_y)
    window = pygame.display.set_mode(window_size)
    pygame.display.set_caption("MapGen")
    screen = pygame.display.get_surface()
    clock = pygame.time.Clock()
    tile_group = pygame.sprite.Group()
    tiles = [[None]*tiles_x]*tiles_y
    for i, ts in enumerate(tiles):
        for j, tile in enumerate(ts):
            tiles[i][j] = Tile(tile_group, image = random.choice(tile_names))
            tiles[i][j].rect.x = window_x/tiles_x * i
            tiles[i][j].rect.y = window_y/tiles_y * j
    while 1:
        time_passed = clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
        tile_group.draw(screen)
        pygame.display.flip()


if __name__=="__main__":
    main()
