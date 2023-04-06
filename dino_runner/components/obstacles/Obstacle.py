import pygame
from dino_runner.utils.constants import SCREEN_WIDTH
from dino_runner.utils.constants import BIRD

class Obstacle:
    def __init__(self, image, name):
        self.image = image
        self.name = name
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.step_index = 0

    def update(self, game_speed, player): # para actualizar
        if self.name == "Birds":
            self.image = BIRD[0] if self.step_index < 5 else BIRD[1]
            self.step_index += 1
            game_speed *= 1.20

        self.rect.x -= game_speed
        if self.rect.colliderect(player.dino_rect):
            if player.hammer:
                self.rect.x = self.rect.x + 950
                player.reset()

            elif not player.shield:
                pygame.time.delay(300)
                player.dino_dead = True
        

        if self.step_index >= 10:
            self.step_index = 0

    def draw(self, screen): # para dibujar
        screen.blit(self.image, self.rect)


