class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_clr = (70, 130, 180)

        self.ship_speed = 2.3
        self.ship_limit = 3

        self.bullet_width = 4
        self.bullet_height = 15
        self.bullet_clr = (60,60,60)
        self.bullets_allowed = 5

        self.fleet_dropspeed = 8
        
        self.speedup = 1.3
        self.score_scale = 1.6

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 2
        self.bullet_speed = 4
        self.alien_speed = 1.3

        self.fleet_direction = 1

        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed *= self.speedup
        self.bullet_speed *= self.speedup
        self.alien_speed *= self.speedup
        self.alien_points = int(self.alien_points * self.score_scale)
