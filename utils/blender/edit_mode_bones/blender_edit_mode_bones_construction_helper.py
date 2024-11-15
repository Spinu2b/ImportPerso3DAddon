

from typing import Tuple


class BlenderEditModeBonesConstructionHelper:
    def calculate_head_and_tail_position(
        self
    ) -> Tuple[Tuple[float, float, float], Tuple[float, float, float]]:

        return ((0,0,0),(0,0,0.10))