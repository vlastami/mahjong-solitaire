import pygame
from board import Board
from tile import Tile

FPS = 60

pygame.init()
screen = pygame.display.set_mode((750, 650))
pygame.display.set_caption("Mahjong")
background_image = pygame.image.load("images/background.jpg")
background_image = pygame.transform.scale(background_image,(750,650))


def main():
    run = True
    clock = pygame.time.Clock()

    board = Board(screen)



    while run:
        clock.tick(FPS)
        screen.blit(background_image,(0,0))
        board.create_tiles_default()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()
    pygame.quit()

main()