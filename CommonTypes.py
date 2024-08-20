import math
import random
from typing import Self, overload

class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x: float = x
        self.y: float = y
    
    def length(self) -> float:
        return math.sqrt(self.x * self.x + self.y * self.y)
    
    def __mul__(self, other: float) -> Self:
        return Vector(self.x * other, self.y * other)
    
    def __add__(self, other: Self) -> Self:
        return Vector(self.x + other.x, self.y + other.y)
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    
    pass


def origin() -> Vector:
    return Vector(0,0)


def random_vec(max_length: float) -> Vector:
    angle = random.uniform(0, 2 * math.pi)
    length = random.uniform(0, max_length)
    return Vector(length * math.cos(angle), length * math.sin(angle))

def random_vec_in_range(upper_left: Vector, lower_right: Vector) -> Vector:
    x = random.uniform(upper_left.x, lower_right.x)
    y = random.uniform(upper_left.y, lower_right.y)
    return Vector(x,y)