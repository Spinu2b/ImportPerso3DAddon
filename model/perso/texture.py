from typing import List


class Texture:
    def __init__(self):
        self.width = 0
        self.height = 0
        self.pixels = []  # type: List[Color]
