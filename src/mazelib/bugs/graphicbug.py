import pygame
import pygame.locals as pg

from bug import Bug
from ..graphicmaze import GraphicMaze

class GraphicBug(Bug):

    def __init__(self, maze):
        super(GraphicBug, self).__init__(maze)
        self._rotate_angles = {
            Bug.NORTH : 0,
            Bug.EAST  : 270,
            Bug.SOUTH : 180,
            Bug.WEST  : 90
        }

    def render(self):
        """
        Create a tile-sized triangle with the correct facing for a bug
        """
        image = pygame.Surface((GraphicMaze.TILE_WIDTH, GraphicMaze.TILE_HEIGHT))
        transparent_color = (255, 0, 255)
        image.set_colorkey(transparent_color)
        image.fill(transparent_color)

        points = [(GraphicMaze.TILE_WIDTH / 2, 0), 
                  (0, GraphicMaze.TILE_HEIGHT), 
                  (GraphicMaze.TILE_WIDTH, GraphicMaze.TILE_HEIGHT)]

        blue_color = (0, 0, 255)
        pygame.draw.polygon(image, blue_color, points)
        
        rotate_angle = self._rotate_angles[self.get_facing()]

        image = pygame.transform.rotate(image, rotate_angle)

        return image

    def render_overlay(self):
        """
        Implementing classes should override this method to render any
        overlays useful for showing how to solve the maze
        """
        return None

    def get_render_location(self):
        """
        Get the screen location the bug should be blitted to
        """
        (row, col) = self.get_location()
        return (GraphicMaze.TILE_HEIGHT * col, GraphicMaze.TILE_WIDTH * row)
