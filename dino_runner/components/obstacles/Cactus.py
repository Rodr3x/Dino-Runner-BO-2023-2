from dino_runner.components.obstacles.Obstacle import Obstacle
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS

from random import randint
class Cactus(Obstacle):
    Y_POS_CACTUS = 390
    vec = SMALL_CACTUS + LARGE_CACTUS
    def __init__(self):
        self.type = randint(0, 5)
        image = self.vec[self.type]
        super().__init__(image, "Cactus")

        if self.type >= 3:
            self.rect.y = self.Y_POS_CACTUS - 25
        else:
            self.rect.y = self.Y_POS_CACTUS
        







