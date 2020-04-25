import pygame
from pygame.sprite import Sprite

class Alien( Sprite ):
    """ Класс, пришельца """
    def __init__( self, game_settings, screen ):
        super().__init__()
        self.screen = screen
        self.game_settings = game_settings

        # Загрузка изображения и назначение атрибута rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Каждый новый прищелец появляется в верхнем углу
        self.rect.x = self.rect.width
        self.rect.x = self.rect.height

        self.x = float( self.rect.x )

    def blitme( self ):
        """ """
        self.screen.blit( self.image, self.rect )