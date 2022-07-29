import random

import pygame
from tile import Tile


class Board:
    def __init__(self, screen):
        self.tiles_coordinates = []
        self.screen = screen



    def create_tiles_default(self):
        self.tiles_coordinates = [(20, 10), (20, 80), (20, 150), (20, 220), (20, 290), (20, 360), (20, 430), (20, 500), (20, 570),
                                  (220, 10), (220, 80), (220, 150), (220, 220), (220, 290), (220, 360), (220, 430), (220, 500),
                                  (220, 570),
                                  (420, 10), (420, 80), (420, 150), (420, 220), (420, 290), (420, 360), (420, 430), (420, 500),
                                  (420, 570),
                                  (620, 10), (620, 80), (620, 150), (620, 220), (620, 290), (620, 360), (620, 430), (620, 500),
                                  (620, 570)]

        for i in self.tiles_coordinates:
            tile = Tile(self.screen, i[0], i[1], 60, 60)
            tile.draw_tile()

