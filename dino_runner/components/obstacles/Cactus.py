from dino_runner.components.obstacles.Obstacle import Obstacle
from dino_runner.utils.constants import SMALL_CACTUS
from random import randint
class Cactus(Obstacle):
    Y_POS_CACTUS = 390

    def __init__(self):
        self.type = randint(0, 2)
        image = SMALL_CACTUS[self.type]
        super().__init__(image)
        self.rect.y = self.Y_POS_CACTUS 
        







