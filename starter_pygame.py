import pygame

import time

pygame.init()

screen = pygame.display.set_mode((400,200))
pygame.display.set_caption("Just a test")

while True:
    screen.fill((0,0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    pygame.display.update()