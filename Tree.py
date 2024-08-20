
from typing import List, Set
import pygame
from pygame import gfxdraw
from Ball import Ball
from CommonTypes import Vector
from ScreenSegment import ScreenSegment
import Settings
import Color


class Tree:
    def __init__(self) -> None:
        self.tree_segments: Set[ScreenSegment] = set()
        self.tree_neighbours: Set[ScreenSegment] = set()
        self.tree_objects: Set[Ball] = set()
        self.object_update_list: List[Ball] = []
        self.segment_update_list: List[ScreenSegment] = []
        pass

    def append_neighbours(self, segment: ScreenSegment) -> None:
        self.tree_neighbours.update(segment.neighbours.get_list())
        self.tree_neighbours.discard(None)
        pass

    def append_object(self, obj: Ball) -> None:
        self.tree_objects.add(obj)
    
    def append_to_update_list(self, obj: Ball) -> None:
        self.object_update_list.append(obj)

    def append_segment(self, segment: ScreenSegment) -> None:
        self.tree_segments.add(segment)
        self.append_neighbours(segment)
        pass

    def update_tree_objects(self) -> None:
        self.tree_objects.update(self.object_update_list)
        self.object_update_list.clear()

    def update_tree_segments(self) -> None:
        for seg in self.segment_update_list:
            self.append_segment(seg)
        self.segment_update_list.clear()

    def handle_collision_with_tree(self, other: Ball) -> bool:
        for obj in self.tree_objects:
            if obj is other:
                continue

            distance = obj.distance(other)
            if distance <= obj.radius + other.radius:
                overlap = obj.radius + other.radius - distance
                dx = (other.position.x - obj.position.x) / distance
                dy = (other.position.y - obj.position.y) / distance
                # obj.position.x -= dx * separation
                # obj.position.y -= dy * separation
                other.position.x += dx * overlap
                other.position.y += dy * overlap

                other.is_stuck = True
                self.append_to_update_list(other)
                return True
        return False

    def handle_collisions_in_segments(self) -> None:
        for seg in self.tree_segments:
            for obj in seg.objects:
                self.handle_collision_with_tree(obj)
        pass

    def handle_collisions_in_neighbours(self) -> None:
        for seg in self.tree_neighbours:
            for obj in seg.objects:
                if self.handle_collision_with_tree(obj):
                    self.segment_update_list.append(seg)
                # if collision_pos is not None:
                #     self.append_segment(seg)

    def debug_draw(self, screen: pygame.Surface) -> None:
        for neighbour in self.tree_neighbours:
            gfxdraw.rectangle(
                screen,
                pygame.Rect(neighbour.position.x, neighbour.position.y, Settings.SEGMENT_SIZE+1, Settings.SEGMENT_SIZE+1),
                Color.sample["BLUE"],
            )
        for seg in self.tree_segments:
            gfxdraw.rectangle(
                screen,
                pygame.Rect(seg.position.x, seg.position.y, Settings.SEGMENT_SIZE+1, Settings.SEGMENT_SIZE+1),
                Color.sample["GREEN"],
            )
        pass
