from dino_runner.components.obstacles.Obstacle import Obstacle
from dino_runner.utils.constants import BIRD
from random import randint
import math

class Birds(Obstacle):
    Y_POS_BIRD  = [100, 250, 300, 350]
    vec = BIRD
    def __init__(self, type):
        self.type = type
        image = self.vec[self.type]
        super().__init__(image)
        c = randint(0, len(self.Y_POS_BIRD)-1)
        self.rect.y = self.Y_POS_BIRD[c]