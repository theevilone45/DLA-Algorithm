from typing import List, Self
from Ball import Ball
import Settings
import Color
from CommonTypes import Vector, random_vec_in_range
from pygame import gfxdraw
import pygame


class Neighbours:
    def __init__(self) -> None:
        self.up: ScreenSegment = None
        self.left: ScreenSegment = None
        self.down: ScreenSegment = None
        self.right: ScreenSegment = None
        self.up_left: ScreenSegment = None
        self.up_right: ScreenSegment = None
        self.down_left: ScreenSegment = None
        self.down_right: ScreenSegment = None

    def __repr__(self) -> str:
        return f"up={self.up},left={self.left},down={self.down},right={self.right},up_left={self.up_left},up_right={self.up_right},down_left={self.down_left},down_right={self.down_right}"

class ScreenSegment:
    def __init__(self, grid_x: int, grid_y: int, index: int) -> None:
        self.objects: List[Ball] = []
        self.neighbours: Neighbours = Neighbours()
        self.index: int = index
        self.grid_x: int = grid_x
        self.grid_y: int = grid_y
        self.position: Vector = Vector(
            self.grid_x * Settings.SEGMENT_SIZE,
            self.grid_y * Settings.SEGMENT_SIZE
        )
        self.font: pygame.font.Font = pygame.font.Font(None, 15)
        self.add_objects()

    def draw(self, screen: pygame.Surface):
        for obj in self.objects:
            obj.draw(screen)

    def pass_to_neighbour(self, obj: Ball, neighbour) -> None:
        if neighbour is None:
            return
        if self.objects.count(obj) == 0:
            return
        self.objects.remove(obj)
        neighbour.objects.append(obj)

    def handle_object_pass(self, obj: Ball) -> None:
        if obj.position.y < self.position.y:
            if obj.position.x < self.position.x:
                self.pass_to_neighbour(obj, self.neighbours.up_left)
                pass
            if obj.position.x > self.position.x + Settings.SEGMENT_SIZE:
                self.pass_to_neighbour(obj, self.neighbours.up_right)
                pass
            self.pass_to_neighbour(obj, self.neighbours.up)
            pass
        if obj.position.y > self.position.y + Settings.SEGMENT_SIZE:
            if obj.position.x < self.position.x:
                self.pass_to_neighbour(obj, self.neighbours.down_left)
                pass
            if obj.position.x > self.position.x + Settings.SEGMENT_SIZE:
                self.pass_to_neighbour(obj, self.neighbours.down_right)
                pass
            self.pass_to_neighbour(obj, self.neighbours.down)
            pass
        if obj.position.x < self.position.x:
            self.pass_to_neighbour(obj, self.neighbours.left)
            pass
        if obj.position.x > self.position.x + Settings.SEGMENT_SIZE:
            self.pass_to_neighbour(obj, self.neighbours.right)
        pass

    def update(self):
        for obj in self.objects:
            obj.update(1/Settings.FPS)
            self.handle_object_pass(obj)

    def add_objects(self) -> None:
        for i in range(Settings.OBJECTS_PER_SEGMENT):
            random_position: Vector = random_vec_in_range(self.position, self.position + Vector(Settings.SEGMENT_SIZE, Settings.SEGMENT_SIZE))
            self.objects.append(Ball(random_position))

    def debug_text_draw(self, screen: pygame.Surface) -> None:
        line_size = self.font.get_linesize()
        text = self.font.render(f"current: <{self.grid_x}, {self.grid_y}>", True, Color.sample["WHITE"])
        screen.blit(text, (self.position.x+10, self.position.y+10))
        text = self.font.render(f"objects: {len(self.objects)}", True, Color.sample["WHITE"])
        screen.blit(text, (self.position.x+10, self.position.y+10+line_size))
        # neighbours_text = repr(self.neighbours).split(",")
        # for i, line in enumerate(neighbours_text):
        #     text = self.font.render(f"{line}", True, Color.sample["WHITE"])
        #     screen.blit(text, (self.position.x+10, self.position.y+10+(line_size*(i+2))))
        pass

    def __repr__(self) -> str:
        return f"<{self.grid_x}; {self.grid_y}>"

    def debug_draw(self, screen: pygame.Surface) -> None:
        gfxdraw.rectangle(
            screen,
            pygame.Rect(self.position.x, self.position.y, Settings.SEGMENT_SIZE+1, Settings.SEGMENT_SIZE+1),
            Color.sample["WHITE"],
        )
        self.debug_text_draw(screen)
        pass


class SegmentGrid:
    def __init__(self) -> None:
        self.segments: List[ScreenSegment] = []
        self.grid_width = Settings.WIDTH // Settings.SEGMENT_SIZE
        self.grid_height = Settings.HEIGHT // Settings.SEGMENT_SIZE
        # populate grid
        index = 0
        for i in range(self.grid_width):
            for j in range(self.grid_height):
                self.segments.append(ScreenSegment(i, j, index))
                index += 1
        # populate neighbours
        self.populate_neighbours()

        pass

    def populate_middle_neighbours(self) -> None:
        for i in range(1, self.grid_width - 1):
            for j in range(1, self.grid_height - 1):
                self.get_segment(i,j).neighbours.up = self.get_segment(i, j-1)
                self.get_segment(i,j).neighbours.left = self.get_segment(i-1, j)
                self.get_segment(i,j).neighbours.down = self.get_segment(i, j+1)
                self.get_segment(i,j).neighbours.right = self.get_segment(i+1, j)
                self.get_segment(i,j).neighbours.up_left = self.get_segment(i-1, j-1)
                self.get_segment(i,j).neighbours.up_right = self.get_segment(i+1, j-1)
                self.get_segment(i,j).neighbours.down_left = self.get_segment(i-1, j+1)
                self.get_segment(i,j).neighbours.down_right = self.get_segment(i+1, j+1)

    def populate_up_border_neighbours(self) -> None:
        for i in range(self.grid_width):
            if i > 0:
                self.get_segment(i,0).neighbours.left = self.get_segment(i-1, 0)
                self.get_segment(i,0).neighbours.down_left = self.get_segment(i-1, 1)
            if i < self.grid_width - 1:
                self.get_segment(i,0).neighbours.right = self.get_segment(i+1, 0)
                self.get_segment(i,0).neighbours.down_right = self.get_segment(i+1, 1)
            self.get_segment(i,0).neighbours.down = self.get_segment(i, 1)

    def populate_down_border_neighbours(self) -> None:
        for i in range(self.grid_width):
            if i > 0:
                self.get_segment(i,self.grid_height - 1).neighbours.left = self.get_segment(i-1, self.grid_height - 1)
                self.get_segment(i,self.grid_height - 1).neighbours.up_left = self.get_segment(i-1, self.grid_height - 2)
            if i < self.grid_width - 1:
                self.get_segment(i,self.grid_height - 1).neighbours.right = self.get_segment(i+1, self.grid_height - 1)
                self.get_segment(i,self.grid_height - 1).neighbours.up_right = self.get_segment(i+1, self.grid_height - 2)
            self.get_segment(i,self.grid_height - 1).neighbours.up = self.get_segment(i, self.grid_height - 2)

    def populate_left_border_neighbours(self) -> None:
        for j in range(1, self.grid_height-1):
            self.get_segment(0, j).neighbours.up = self.get_segment(0, j-1)
            self.get_segment(0, j).neighbours.right = self.get_segment(1, j)
            self.get_segment(0, j).neighbours.down = self.get_segment(0, j+1)
            self.get_segment(0, j).neighbours.up_right = self.get_segment(1, j-1)
            self.get_segment(0, j).neighbours.down_right = self.get_segment(1, j+1)

    def populate_right_border_neighbours(self) -> None:
        for j in range(1, self.grid_height-1):
            self.get_segment(self.grid_width - 1, j).neighbours.up = self.get_segment(self.grid_width - 1, j-1)
            self.get_segment(self.grid_width - 1, j).neighbours.left = self.get_segment(self.grid_width - 2, j)
            self.get_segment(self.grid_width - 1, j).neighbours.down = self.get_segment(self.grid_width - 1, j+1)
            self.get_segment(self.grid_width - 1, j).neighbours.up_left = self.get_segment(self.grid_width - 2, j-1)
            self.get_segment(self.grid_width - 1, j).neighbours.down_left = self.get_segment(self.grid_width - 2, j+1)

    def populate_neighbours(self) -> None:
        self.populate_middle_neighbours()
        self.populate_up_border_neighbours()
        self.populate_down_border_neighbours()
        self.populate_left_border_neighbours()
        self.populate_right_border_neighbours()
        pass

    def draw(self, screen: pygame.Surface) -> None:
        for seg in self.segments:
            seg.draw(screen)

    def update(self) -> None:
        for seg in self.segments:
            seg.update()
    
    def get_segment(self, grid_x, grid_y) -> ScreenSegment:
        return self.segments[grid_x * self.grid_height + grid_y]

    def debug_draw(self, screen: pygame.Surface) -> None:
        for seg in self.segments:
            seg.debug_draw(screen)
