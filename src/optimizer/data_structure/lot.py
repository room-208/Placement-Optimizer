import random


class Lot:
    def __init__(self, height: int, width: int) -> None:
        self.height = height
        self.width = width
        self.x = None
        self.y = None