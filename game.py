import pygame
import os
import sys
from p_classes import Board, SpritePictures, NormalSprite, HealphBar, Ground


def game_sobstvenno(*args, **kwargs):
    pygame.init()
    pygame.display.set_caption('game')
    size = 500, 500
    screen = pygame.display.set_mode(size)
    running = True
    screen.fill('black')
    all_sprites = pygame.sprite.Group()
    health = HealphBar(all_sprites, 6, 21)
    ground = Ground(screen, 500, 500, 50)
    all_sprites.draw(screen)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                ground.get_click(event.pos)
        screen.fill('black')
        ground.render()
        all_sprites.draw(screen)
        pygame.display.flip()
        # pygame.time.Clock().tick(200)


# def main():

if __name__ == '__main__':
    game_sobstvenno()
