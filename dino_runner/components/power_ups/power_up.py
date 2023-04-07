import pygame 
from dino_runner.utils.constants import SCREEN_WIDTH

from random import randint

class PowerUp:
    Y_POS_POWER_UP = [250, 350, 400]
    POWER_UP_DURATION = 5000
    
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH*(randint(3, 7)) - 123

        if self.type == "jump":
            self.rect.y = 330
        else:
            self.rect.y = self.Y_POS_POWER_UP[randint(0, len(self.Y_POS_POWER_UP)-1)]

        self.start_time = 0
        self.time_up = 0
        self.used = False

    def update(self, game_speed, player):
        self.rect.x -= game_speed
        if self.rect.colliderect(player.dino_rect):
            if self.type == "jump" and player.jump_vel <= 15:
                player.jump_vel += 1

            if self.type == "life":
                player.sw = True

            self.start_time = pygame.time.get_ticks()
            self.time_up = self.start_time + self.POWER_UP_DURATION
            self.used = True

    
    def draw(self, screen):
        screen.blit(self.image, self.rect)