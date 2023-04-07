from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.components.power_ups.jump import Jump
from dino_runner.components.power_ups.life import Life

from random import randint
import pygame

class PowerUpManager:
    def __init__(self):
        #pygame.mixer.music.load("dino_runner/components/musicshield.mp3")
        self.power_ups = []
    
    def update(self, game_speed, points, player):
        if len(self.power_ups) == 0 and points % 400 == 0:
            c = randint(0, 3)
            if c == 0:
                self.power_ups.append(Shield())
            elif c == 1:
                self.power_ups.append(Hammer())
            elif c == 2:
                self.power_ups.append(Jump())
            else:
                self.power_ups.append(Life())

        for power_up in self.power_ups:
            if power_up.used or power_up.rect.x < -power_up.rect.width:
                self.power_ups.pop()

            if power_up.used:
                player.set_power_up(power_up)
            power_up.update(game_speed, player)
    
    def draw(self, screen):
        #pygame.mixer.music.play(3)
        for power_up in self.power_ups:
            power_up.draw(screen)