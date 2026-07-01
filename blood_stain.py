from dataclasses import dataclass

@dataclass
class BloodStain:

    id: int

    center_x: float
    center_y: float

    major_axis: float
    minor_axis: float

    impact_angle: float

    ellipse: tuple

    direction_angle: float = None

    area: float = 0

    perimeter: float = 0

    confidence: float = 1.0
