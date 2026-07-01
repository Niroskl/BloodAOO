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

    area: float
    perimeter: float

    direction_angle: float = None

    confidence: float = 1.0
