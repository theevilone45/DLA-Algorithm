from random import randint
import random

sample = {
    'RED': (255, 0, 0),
    'GREEN': (0, 255, 0),
    'BLUE': (0, 0, 255),
    'WHITE': (255, 255, 255),
    'BLACK': (0, 0, 0)
}


def randomColor():
    r = randint(20, 255)
    g = 0
    b = 0

    return (r, g, b)


def randomSample():
    key=random.choice(sample.keys())
    return sample[key]
