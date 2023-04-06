from dino_runner.components.obstacles.Obstacle import Obstacle
from dino_runner.utils.constants import BIRD
from random import randint
import math

class Birds(Obstacle):
    Y_POS_BIRD  = [200, 250, 300, 350]
    def __init__(self):
        self.type = type
        self.image = BIRD[0]
        super().__init__(self.image, "Birds")
        cc = randint(0, len(self.Y_POS_BIRD)-1)
        self.rect.y = self.Y_POS_BIRD[cc]