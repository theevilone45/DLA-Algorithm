
from typing import List
from ScreenSegment import ScreenSegment


class Tree:
    def __init__(self) -> None:
        self.tree_segments: List[ScreenSegment] = []
        pass

    def append(self, segment: ScreenSegment) -> None:
        self.tree_segments.append(segment)
        pass
