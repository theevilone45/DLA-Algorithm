from random import randint
import random

type Color = tuple[int, int, int]

sample = {
    'RED': (255, 0, 0),
    'GREEN': (0, 255, 0),
    'BLUE': (0, 0, 255),
    'MAGENTA': (255,0,255),
    'WHITE': (255, 255, 255),
    'BLACK': (0, 0, 0)
}


def randomColor() -> Color:
    r = randint(20, 255)
    g = 0
    b = 0

    return (r, g, b)


def randomSample() -> Color:
    key=random.choice(sample.keys())
    return sample[key]
