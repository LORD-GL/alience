class Settings():
    """ Класс для хранения всех настроек игры """

    def  __init__( self ):
        """ Инициализирует настройки игры """
        # Параметры экрана
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = ( 230, 230, 230 )

        # Настройки корабля
        self.ship_speed_factor = 1.5

        #Параметры пули
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = ( 60, 60, 60 )
        self.bullet_allowed = 5

        # Настройки пришельцев
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # 1 - вправо, -1 - влево
        self.fleet_direction = 1