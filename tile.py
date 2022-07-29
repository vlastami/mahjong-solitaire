# 144 tiles in the game
import random

import pygame.draw


class Tile:
    deck = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18",
            "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18"]

    def __init__(self, screen, left, up, width, height):
        self.exposed = True
        self.screen = screen
        self.left = left
        self.up = up
        self.width = width
        self.height = height

    def draw_tile(self):
        pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(self.left, self.up, self.width, self.height))
        self.set_image()

    def set_image(self):
        for i in range(len(self.deck)):
            tile_image = pygame.image.load(f"images/{self.deck[i]}.jpg")
            tile_image = pygame.transform.scale(tile_image, (147, 186))
            self.screen.blit(tile_image, (self.left, self.up))
