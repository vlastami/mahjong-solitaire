import random

import pygame
from tile import Tile


class Board:
    def __init__(self, screen):
        self.tiles_coordinates = []
        self.screen = screen
        self.colors = []


    def create_tiles_default(self):
        self.tiles_coordinates = [(20, 10), (20, 80), (20, 150), (20, 220), (20, 290), (20, 360), (20, 430), (20, 500), (20, 570),
                                  (220, 10), (220, 80), (220, 150), (220, 220), (220, 290), (220, 360), (220, 430), (220, 500),
                                  (220, 570),
                                  (420, 10), (420, 80), (420, 150), (420, 220), (420, 290), (420, 360), (420, 430), (420, 500),
                                  (420, 570),
                                  (620, 10), (620, 80), (620, 150), (620, 220), (620, 290), (620, 360), (620, 430), (620, 500),
                                  (620, 570)]
        self.colors = [
            (242, 125, 125), (233, 249, 199), (123, 221, 179), (99, 189, 159), (91, 159, 143), (58, 147, 189),
            (137, 163, 62), (133, 124, 106), (253, 197, 12), (251, 86, 48), (14, 26, 64), (3, 57, 108), (61, 81, 128),
            (222, 177, 94), (176, 124, 59), (73, 92, 131), (122, 134, 182), (168, 164, 206), (242, 125, 125),
            (233, 249, 199), (123, 221, 179), (99, 189, 159), (91, 159, 143), (58, 147, 189),
            (137, 163, 62), (133, 124, 106), (253, 197, 12), (251, 86, 48), (14, 26, 64), (3, 57, 108), (61, 81, 128),
            (222, 177, 94), (176, 124, 59), (73, 92, 131), (122, 134, 182), (168, 164, 206)]

        for i in self.tiles_coordinates:
            tile = Tile(self.screen, self.colors[len(i)], i[0], i[1], 60, 60)
            tile.draw_tile()