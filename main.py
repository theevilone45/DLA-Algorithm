from typing import Self
import pygame

import Settings
from enum import Enum
from ScreenSegment import *;

class RunningState(Enum):
    STARTED = 0
    PAUSED = 1
    DONE = 2

class App:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((Settings.WIDTH, Settings.HEIGHT))
        pygame.display.set_caption("DLA Algorithm")
        self.clock = pygame.time.Clock()
        self.state: RunningState = RunningState.STARTED
        self.segment_grid: SegmentGrid = SegmentGrid()
        self.init_objects()
        pass

    def __del__(self) -> None:
        pygame.quit()

    def init_objects(self) -> None:
        pass

    def debug_draw(self) -> None:
        self.segment_grid.debug_draw(self.screen)

    def run(self) -> None:
        while self.state is not RunningState.DONE:
            self.screen.fill(Color.sample["BLACK"])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.state = RunningState.DONE

            if Settings.DEBUG_DRAW:
                self.debug_draw()

            pygame.display.flip()
            self.clock.tick(Settings.FPS)
        pass
        
if __name__ == "__main__":
    app = App()
    app.run()




