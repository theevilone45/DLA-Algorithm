import Settings
from Ball import Ball

class Tree:
    def __init__(self):
        self.items = []
        pass

    def append(self, object):
        self.items.append(object)

    def draw(self, screen):
        for i in range(len(self.items)):
            self.items[i].draw(screen)
        pass