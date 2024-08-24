
from typing import List, Set
import pygame
from pygame import gfxdraw
from Ball import Ball
from CommonTypes import Vector
from ScreenSegment import ScreenSegment, SegmentGrid
import Settings
import Color


class Tree:
    def __init__(self, segments: SegmentGrid) -> None:
        #
        self.objects: Set[Ball] = set()
        self.next_objects: Set[Ball] = set()
        self.segments: SegmentGrid = segments
        self.color_wheel: Color.ColorWheel = Color.ColorWheel()
        pass

    def append_object(self, obj: Ball) -> None:
        #
        obj.is_stuck = True
        obj.color = self.color_wheel.next_color()
        self.next_objects.add(obj)
        seg = self.segments[obj.get_segment_id()]
        seg.add_to_tree(obj)

    def apply_next_objects(self) -> None:
        self.objects.update(self.next_objects)

    def handle_collisions_in_segment(self, obj: Ball, seg: ScreenSegment) -> None:
        #
        all_segments = seg.neighbours.get_list()
        all_segments.append(seg)
        for ss in all_segments:
            for other in ss.objects:
                if obj is other:
                    continue
                distance = other.distance(obj)
                if distance <= obj.radius + other.radius:
                    overlap = obj.radius + other.radius - distance
                    dx = (other.position.x - obj.position.x) / distance
                    dy = (other.position.y - obj.position.y) / distance
                    other.position.x += dx * overlap
                    other.position.y += dy * overlap
                    self.append_object(other)
                    

    def handle_collisions(self) -> None:
        for i, obj in enumerate(self.objects):
            # get segment
            seg_id = obj.get_segment_id()
            try:
                seg = self.segments[seg_id]
                self.handle_collisions_in_segment(obj, seg)
            except IndexError:
                pass
            
        pass

    def debug_draw(self, screen: pygame.Surface) -> None:
        pass
