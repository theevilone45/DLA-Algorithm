from random import randint
import pygame
import Color
import Settings


class Ball:
    def __init__(self, x=int(Settings.WIDTH / 2), y=int(Settings.HEIGHT / 2), r=Settings.RADIUS, c=Color.sample['WHITE']):
        self.x = x
        self.y = y
        self.r = r
        self.color = c
        self.stuck = False
        pass

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)
        pass

    def move(self, dx, dy):
        if self.x + dx > self.r and self.x + dx < Settings.WIDTH - self.r:
            self.x += dx
        if self.r < self.y + dy < Settings.HEIGHT - self.r:
            self.y += dy
        pass

    def distance(self, object):
        dist_sq = (object.x - self.x) ** 2 + (object.y - self.y) ** 2
        return dist_sq

    def isStuck(self, tree):
       for i in range(len(tree)):
           if self.distance(tree[i]) < (self.r + tree[i].r)**2:
                self.color = Color.randomColor()
                self.stuck = True


    def update(self):
        if not self.stuck:
            dx = randint(-10, 10)
            dy = randint(-10, 10)
            self.move(dx, dy)
        pass
