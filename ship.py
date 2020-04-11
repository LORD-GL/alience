import pygame

class Ship():
    def __init__( self, screen ):
        "Инициализация корабля"
        self.screen = screen
        
        # загрузка скина корабля
        self.image = pygame.image.load( 'images/ship.bmp' )
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Каждый новый корабль появляется у нижнего экрана
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme( self ):
        """рисует корабль в тек. позиции """
        self.screen.blit( self.image, self.rect )