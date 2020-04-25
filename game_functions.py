import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_keydown_events(event, ship, screen, game_settings, bullets ):
    """Реагирует на нажатие клавиш"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # Создание новой пули и включение ее в группу bullet
        fire_bullet( ship, screen, game_settings, bullets )
    elif event.key == pygame.K_q:
        sys.exit()

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

def update_screen( game_settings, screen, ship, bullets, alience ):
    """ Обновляет экран """
    # перересовка
    screen.fill( game_settings.bg_color )
    #все пули выводятся позади корабля и пришельцев
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # прорисовка кораблика
    ship.blitme()
    # Прорисовка прищельцев
    alience.draw( screen )
    # отображение последнего прорисованного экрана
    pygame.display.flip()

def update_bullets( bullets ):
    """ Обновляет позиции и уничтожает старые пули """
    bullets.update()
    #цикл для удаления не нужных пуль
    for bullet in bullets.copy():
        if bullet.rect.bottom < 0:
            bullets.remove( bullet )

def get_number_alience_( game_settings, alien_width ):
    """ вычисляет кол. прищельцев в ряду"""
    avulable_space_x = game_settings.screen_width - 2 * alien_width
    number_alien_x = int( avulable_space_x / ( 2 * alien_width ) )
    return number_alien_x

def create_alien( game_settings, screen, alience, alien_number, alien_width ):
    # Создание прищельца и размещение его в ряду
    alien = Alien( game_settings, screen )
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alience.add( alien )

def create_fleet( game_settings, screen , alience):
    """ Создает флот прищельцев """
    # Создание прищельца и вычисление кол. прищельцев в ряду
    # Интервал между соседними прищельцами равен одной ширине прищельца

    alien = Alien( game_settings, screen )
    alien_width = alien.rect.width
    number_alien_x = get_number_alience_( game_settings, alien_width )
    for alien_number in range( number_alien_x ):
        create_alien( game_settings, screen, alience, alien_number, alien_width )

    
    