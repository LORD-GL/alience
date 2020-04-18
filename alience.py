import pygame
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
    ship = Ship( screen )

    # основной цикл
    while True:
        # события клавы и мыши
        gf.check_events()
        # перересовка
        screen.fill( game_settings.bg_color )
        # прорисовка кораблика
        ship.blitme()
        # отображение последнего прорисованного экрана
        pygame.display.flip()

run_game()