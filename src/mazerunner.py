import pygame
import pygame.locals as pg

import mazelib

class MazeRunner:

    SOLVE_STEP = pygame.USEREVENT + 1
    STEP_PERIOD = 100 #100 ms per solve step
    FRAMERATE = 40 #40 fps max

    def __init__ (self, maze, bug):
        self.screen = pygame.display.set_mode(maze.get_screen_size())
        self.maze = maze
        self.bug = bug
        self.maze_image = self.maze.render()

    def main(self):
        """
        Run the solving animation
        """
        #solve a step every half-second
        pygame.time.set_timer(MazeRunner.SOLVE_STEP, MazeRunner.STEP_PERIOD)
        clock = pygame.time.Clock()
        self.game_over = False
        while not self.game_over:
            clock.tick(MazeRunner.FRAMERATE)
            self._process_events()
            self._render_maze()
            

    def _process_events(self):
        """
        Process events from the pygame event queue
        """
        for event in pygame.event.get():
            if event.type == MazeRunner.SOLVE_STEP:
                self.bug.take_step()
            elif event.type == pg.QUIT:
                self.game_over = True

    def _render_maze(self):
        """
        Render the current state of the maze
        """
        self.screen.blit(self.maze_image, (0,0))
        overlay = self.bug.render_overlay()
        bug_image = self.bug.render()
        bug_loc = self.bug.get_render_location()

        if overlay is not None:
            self.screen.blit(overlay, (0,0))

        self.screen.blit(bug_image, bug_loc)
        pygame.display.flip()


