#! /usr/bin/python
from pygame import *

def main():
    init()
    window_size = (640, 480)
    window = display.set_mode(window_size)
    display.set_caption("MapGen")
    screen = display.get_surface()
    clock = time.Clock()
    tiles = [[None]*10]*10
    print tiles[0][0]

if __name__=="__main__":
    main()
