import math
import random

class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x: float = x
        self.y: float = y
    
    def length(self) -> float:
        return math.sqrt(self.x * self.x + self.y * self.y)
    
    pass


def origin() -> Vector:
    return Vector(0,0)

def random_vec(max_length: float) -> Vector:
    angle = random.uniform(0.0, 2 * math.pi)
    max_length