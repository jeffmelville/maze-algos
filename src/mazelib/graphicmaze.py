
import pygame
import pygame.locals as pg 
from maze import Maze

class GraphicMaze(Maze):

    TILE_WIDTH = 32
    TILE_HEIGHT = 32

    def get_screen_size(self):
        return (self.get_width() * GraphicMaze.TILE_WIDTH, 
                self.get_height() * GraphicMaze.TILE_HEIGHT)

    def render(self):
        """Draw the maze on a surface and return it"""
        size = self.get_screen_size()
        image = pygame.Surface(size)

        for map_y in range(self.get_height()):
            for map_x in range(self.get_width()):
                cell = self(map_y, map_x)
                rect = pygame.Rect(map_x*GraphicMaze.TILE_WIDTH, 
                                   map_y*GraphicMaze.TILE_HEIGHT, 
                                   GraphicMaze.TILE_WIDTH, 
                                   GraphicMaze.TILE_HEIGHT)

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

        return image

