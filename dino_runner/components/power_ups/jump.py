from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.utils.constants import JUMP, JUMP_TYPE

class Jump(PowerUp):
    def __init__(self):
        self.image = JUMP
        self.type = JUMP_TYPE
        super().__init__(self.image, self.type)