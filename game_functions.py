import sys
import pygame
from bullet import Bullet

def check_keydown_events(event, ship, screen, game_settings, bullets ):
    """Реагирует на нажатие клавиш"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # Создание новой пули и включение ее в группу bullet
        fire_bullet( ship, screen, game_settings, bullets )

def fire_bullet( ship, screen, game_settings, bullets ):
    """ Создание новой пули и включение ее в группу bullet если максимум не достигнут """
    if len( bullets ) < game_settings.bullet_allowed:
            new_bullet = Bullet( screen, game_settings, ship )
            bullets.add( new_bullet )

def check_keyup_events(event, ship):
    """Реагирует на отпускание клавиш """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events( game_settings, screen, ship, bullets ):
    """ Обрабатывает нажатия клавиш и события мыши"""
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                check_keydown_events(event, ship, screen, game_settings, bullets )
            elif event.type == pygame.KEYUP:
                check_keyup_events(event, ship)

def update_screen( game_settings, screen, ship, bullets ):
    """ Обновляет экран """
    # перересовка
    screen.fill( game_settings.bg_color )
    #все пули выводятся позади корабля и пришельцев
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # прорисовка кораблика
    ship.blitme()
    # отображение последнего прорисованного экрана
    pygame.display.flip()

def update_bullets( bullets ):
    """ Обновляет позиции и уничтожает старые пули """
    bullets.update()
    #цикл для удаления не нужных пуль
    for bullet in bullets.copy():
        if bullet.rect.bottom < 0:
            bullets.remove( bullet )