import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #game init
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode( ( game_settings.screen_width, game_settings.screen_height ) )
    pygame.display.set_caption( "Alience" )

    # создание корабля
    ship = Ship( screen, game_settings )

    # Создание группы для хранения пуль
    bullets = Group()

    # основной цикл
    while True:
        # события клавы и мыши
        gf.check_events( game_settings, screen, ship, bullets )
        # Обработка событий
        ship.update()
        # Обработка пуль
        bullets.update()
        # обновление экрана
        gf.update_screen( game_settings, screen, ship, bullets )

run_game()