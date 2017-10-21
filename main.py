import pygame

import Color
import Settings
from Tree import Tree
from Ball import Ball
from random import randint

exit = False

pygame.init()

screen = pygame.display.set_mode((Settings.WIDTH,Settings.HEIGHT))
pygame.display.set_caption('DLA Algorithm')

clock = pygame.time.Clock()

tree = Tree()
tree.append(Ball())

balls = []

for i in range(Settings.WALKERS_COUNT):
    x = randint(Settings.RADIUS, Settings.WIDTH-Settings.RADIUS)
    y = randint(Settings.RADIUS, Settings.HEIGHT-Settings.RADIUS)
    balls.append(Ball(x,y))

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit = True

    screen.fill(Color.sample['BLACK'])

    #new_balls = balls

    for i in range(len(balls)-1, -1, -1):
        balls[i].isStuck(tree.items)
        balls[i].update()
        balls[i].draw(screen)
        if balls[i].stuck:
            tree.append(balls[i])
            del balls[i]

    tree.draw(screen)

    pygame.display.update()
    clock.tick(Settings.FPS)

    if exit:
        break

pygame.quit()
quit()

