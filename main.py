from typing import Self
import pygame

from Ball import Ball
from CommonTypes import Vector
import Settings
from enum import Enum
from ScreenSegment import *
from Tree import Tree;

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
        self.font = pygame.font.Font(None, 20)
        self.state: RunningState = RunningState.STARTED
        self.segment_grid: SegmentGrid = SegmentGrid()
        self.tree: Tree = Tree(self.segment_grid)
        self.init_tree()
        pass

    def __del__(self) -> None:
        pygame.quit()

    def draw_fps(self) -> None:
        fps = self.clock.get_fps()
        fps_text = self.font.render(f"FPS: {int(fps)}", True, Color.sample["WHITE"])
        self.screen.blit(fps_text, (5,5))

    def init_tree(self) -> None:
        init_segment = self.segment_grid[Settings.TREE_INIT_SEGMENT[0], Settings.TREE_INIT_SEGMENT[1]]
        self.tree.append_object(init_segment.objects[0])
        pass

    def debug_draw(self) -> None:
        self.segment_grid.debug_draw(self.screen)
        self.tree.debug_draw(self.screen)

    def handle_events(self) -> None:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.state = RunningState.DONE
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        if self.state is RunningState.PAUSED:
                            self.state = RunningState.STARTED
                        else:
                            self.state = RunningState.PAUSED
                    if event.key == pygame.K_s:
                        Settings.DEBUG_DRAW = not Settings.DEBUG_DRAW

    def run(self) -> None:
        while self.state is not RunningState.DONE:
            self.screen.fill(Color.sample["BLACK"])
            self.handle_events()
            if self.state is RunningState.STARTED:
                self.segment_grid.update()
                self.tree.handle_collisions()
                self.tree.apply_next_objects()
                  
            self.segment_grid.draw(self.screen)
            if Settings.DEBUG_DRAW:
                self.debug_draw()

            if Settings.SHOW_FPS:
                self.draw_fps()
            pygame.display.flip()
            self.clock.tick(Settings.FPS)
        pass
        
if __name__ == "__main__":
    app = App()
    app.run()




