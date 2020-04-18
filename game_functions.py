import sys
import pygame

def check_events( ship ):
    """ Обрабатывает нажатия клавиш и события мыши"""
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # Начать перемещение в парво
                    ship.moving_right= True
                elif event.key == pygame.K_LEFT:
                    # Начать перемещение в парво
                    ship.moving_left= True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    # Начать перемещение в парво
                    ship.moving_right= False
                elif event.key == pygame.K_LEFT:
                    # Начать перемещение в парво
                    ship.moving_left = False

def update_screen( game_settings, screen, ship ):
    """ Обновляет экран """
    # перересовка
    screen.fill( game_settings.bg_color )
    # прорисовка кораблика
    ship.blitme()
    # отображение последнего прорисованного экрана
    pygame.display.flip()