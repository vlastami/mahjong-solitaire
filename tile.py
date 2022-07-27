# 144 tiles in the game
import random

import pygame.draw


class Tile:

    def __init__(self, screen, color, left, up, width, height):
        self.exposed = True
        self.screen = screen
        self.left = left
        self.up = up
        self.width = width
        self.height = height
        self.color = color

    def draw_tile(self):

        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.left, self.up, self.width, self.height))
