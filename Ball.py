import math
from random import randint
from typing import Self
import pygame
from pygame import gfxdraw
import Color
import Settings
from CommonTypes import Vector, origin, random_vec
from enum import Enum


class Boundry(Enum):
    NONE=0,
    HORIZONTAL=1,
    VERTICAL=2

class Ball:
    def __init__(self, position: Vector):
        self.position: Vector = position
        self.velocity: Vector = origin()
        self.acceleartion: Vector = random_vec()
        self.radius: int = 0
        self.color: Color = Color.sample["BLACK"]
        pass

    def draw(self, screen):
        gfxdraw.aacircle(screen, self.position.x(), self.position.y(), self.radius, self.color)
        gfxdraw.filled_circle(screen, int(self.position.x), int(self.position.y), self.radius, self.color)
        pass

    def distance(self, object: Self) -> float:
        dist_sq = (object.position.x - self.position.x) ** 2 + (
            object.position.y - self.position.y
        ) ** 2
        return math.sqrt(dist_sq)
    
    def detect_boundry_hit(self, dt) -> Boundry:
        future_position: Vector = self.position + self.velocity * dt
        if future_position.x <= 0 or future_position.x >= Settings.WIDTH:
            return Boundry.HORIZONTAL
        if future_position.y <= 0 or future_position.y >= Settings.HEIGHT:
            return Boundry.VERTICAL
        return Boundry.NONE
    

    def handle_boundry_hit(self, dt) -> None:
        hitted_boundry = self.detect_boundry_hit(dt)
        if hitted_boundry == Boundry.HORIZONTAL:
            self.velocity.x = -self.velocity.x
            self.acceleartion.x = -self.acceleartion.x
        elif hitted_boundry == Boundry.VERTICAL:
            self.velocity.y = -self.velocity.y
            self.acceleartion.y = -self.acceleartion.y

    def update(self, dt) -> None:
        self.handle_boundry_hit(dt)
        
        if self.velocity.length() <= Settings.MAX_VELOCITY:
            self.velocity += self.acceleartion * dt
        self.position += self.velocity * dt
        pass
