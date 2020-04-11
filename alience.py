import sys
import pygame
from settings import Settings

def run_game():
    #game init
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode( ( game_settings.screen_width, game_settings.screen_height ) )
    pygame.display.set_caption( "Alience" )

    # основной цикл
    while True:
        # события клавы и мыши
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # перересовка
        screen.fill( game_settings.bg_color )
        # отображение последнего прорисованного экрана
        pygame.display.flip()

run_game()