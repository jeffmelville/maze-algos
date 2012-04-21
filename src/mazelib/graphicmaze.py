
import pygame
import pygame.locals as pg 
from maze import Maze

TILE_WIDTH, TILE_HEIGHT = 32,32 

class GraphicMaze(Maze):


    def render(self):
        """Draw the maze on a surface and return it"""
        width = self.get_width() * TILE_WIDTH
        height = self.get_height() * TILE_HEIGHT
        print "%d,%d" % (width, height)
        image = pygame.Surface((width, height))

        for map_y in range(self.get_height()):
            for map_x in range(self.get_width()):
                cell = self(map_y, map_x)
                rect = pygame.Rect(map_x*TILE_WIDTH, map_y*TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT)
                color = (0,0,0)
                if cell.is_path():
                    color=(255,255,255)
                elif cell.is_start():
                    color=(0, 255,0)
                elif cell.is_end():
                    color=(255, 0, 0)
                elif cell.is_wall():
                    color=(0,0,0)
                image.fill(color, rect=rect)
                #image.blit(cell_tile, map_x*TILE_WIDTH, map_y*TILE_HEIGHT)

        return image


class TestGame:

    def __init__ (self, maze):
        self.screen = pygame.display.get_surface()
        self.maze = maze
        self.maze_image = self.maze.render()

    def main(self):
        self.screen.blit(self.maze_image, (0,0))
        pygame.display.flip()
        clock = pygame.time.Clock()
        self.game_over = False
        while not self.game_over:
            clock.tick(15)
            for event in pygame.event.get(): 
                if event.type == pg.QUIT:
                    self.game_over = True



