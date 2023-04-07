from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.utils.constants import LIFE, LIFE_TYPE

class Life(PowerUp):
    def __init__(self):
        self.image = LIFE
        self.type = LIFE_TYPE
        super().__init__(self.image, self.type)