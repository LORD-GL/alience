import sys
import pygame

def check_events( ship ):
    """ Обрабатывает нажатия клавиш и события мыши"""
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # Переместить в право
                    ship.rect.centerx += 1

def update_screen( game_settings, screen, ship ):
    """ Обновляет экран """
    # перересовка
    screen.fill( game_settings.bg_color )
    # прорисовка кораблика
    ship.blitme()
    # отображение последнего прорисованного экрана
    pygame.display.flip()