import pygame

class Ship():
    def __init__( self, screen, game_settings ):
        "Инициализация корабля"
        self.screen = screen
        self.game_settings = game_settings

        # загрузка скина корабля
        self.image = pygame.image.load( 'images/ship.bmp' )
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Сохранение везественной координаты центра корабля
        self.center = float( self.rect.centerx )

        # Каждый новый корабль появляется у нижнего экрана
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Флаг перемещения
        self.moving_right = False
        self.moving_left = False

    def update( self ):
        """ Обновляет позицию корабля с учетом флага """
        if self.moving_right:
            self.center += self.game_settings.ship_speed_factor
        if self.moving_left:
            self.center -= self.game_settings.ship_speed_factor
        #обновление атрибута rect на основании self.center
        self.rect.centerx = int( self.center )

    def blitme( self ):
        """рисует корабль в тек. позиции """
        self.screen.blit( self.image, self.rect )