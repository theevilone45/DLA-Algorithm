from random import randint
import random
import colorsys

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


class ColorWheel:
    def __init__(self):
        self.hue = 0.5
        self.saturation = 1.0
        self.decrement = 0.001

    def next_color(self):
        # Convert the current hue to an RGB color
        r, g, b = colorsys.hsv_to_rgb(self.hue, self.saturation, 1.0)
        
        # Update the hue for the next call, wrapping around at 1.0
        self.saturation = max((self.saturation - self.decrement), 0.0)
        
        # Return the color as a tuple with RGB values in the range 0-255
        return int(r * 255), int(g * 255), int(b * 255)
