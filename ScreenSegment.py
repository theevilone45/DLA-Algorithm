from typing import List, Self
import Settings
import Color
from pygame import gfxdraw
import pygame


class ScreenSegment:
    def __init__(self, grid_x: int, grid_y: int) -> None:
        self.balls = []
        self.neighbours: List[ScreenSegment] = []
        self.grid_x: int = grid_x
        self.grid_y: int = grid_y
        self.x: int = self.grid_x * Settings.SEGMENT_SIZE
        self.y: int = self.grid_y * Settings.SEGMENT_SIZE

    def debug_draw(self, screen: pygame.Surface) -> None:
        gfxdraw.rectangle(
            screen,
            pygame.Rect(self.x, self.y, Settings.SEGMENT_SIZE, Settings.SEGMENT_SIZE),
            Color.sample["WHITE"],
        )
        pass

    def add_neighbour(self, neighbour: Self) -> None :
        self.neighbours.append(neighbour)
        pass


class SegmentGrid:
    def __init__(self) -> None:
        self.segments: List[ScreenSegment] = []
        self.grid_width = Settings.WIDTH // Settings.SEGMENT_SIZE
        self.grid_height = Settings.HEIGHT // Settings.SEGMENT_SIZE
        # populate grid
        for i in range(self.grid_width):
            for j in range(self.grid_height):
                self.segments.append(ScreenSegment(i, j))
        # populate neighbours

        pass
    
    def get_segment(self, grid_x, grid_y) -> ScreenSegment:
        return self.segments[grid_y * self.grid_width + grid_x]

    def debug_draw(self, screen: pygame.Surface) -> None:
        for seg in self.segments:
            seg.debug_draw(screen)
