import pygame
from pygame.sprite import Sprite

class Bullet( Sprite ):
    """ Класс для успарвления пулями, выпущенными кораблем """

    def __init__( self, screen, game_settings, ship ):
        """ Создает объект пули в позии корабля """
        super().__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, game_settings.bullet_width, game_settings.buller_height )
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float( self.rect.y )

        self.color = game_settings.bullet_color
        self.speed_factor = game_settings.bullet_speed_factor

    def update( self ):
        """ Перемещение пули """
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet( self ):
        """ Вывод пули на экран """
        pygame.draw.rect( self.screen, self.color, self.rect )