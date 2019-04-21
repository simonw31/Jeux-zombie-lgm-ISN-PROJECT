#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
COLORS = (RED, GREEN, BLUE)
color_index = 0

pygame.init()
screen = pygame.display.set_mode((400, 400))

stop = False

clickable_area = pygame.Rect((100, 100), (100, 100))
rect_surf = pygame.Surface(clickable_area.size)
rect_surf.fill(COLORS[color_index])

while not stop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop = True

        elif event.type == MOUSEBUTTONUP:  # quand je relache le bouton
            if event.button == 1:  # 1= clique gauche
                if clickable_area.collidepoint(event.pos):
                    color_index = (color_index + 1) % 3
                    rect_surf.fill(COLORS[color_index])

    screen.fill(0)  # On efface tout l'écran
    screen.blit(rect_surf, clickable_area)
    pygame.display.flip()

pygame.quit()