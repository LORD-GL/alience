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

    def check_edges( self ):
        """ True, если достиг края"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right: return True
        elif self.rect.right <= 0: return True

    def update( self ):
        """ перемещает прищельца в право"""
        self.x += self.game_settings.alien_speed_factor * self.game_settings.fleet_direction
        self.rect.x = self.x
