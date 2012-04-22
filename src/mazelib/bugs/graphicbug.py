import pygame
import pygame.locals as pg

from bug import Bug

TILE_WIDTH, TILE_HEIGHT = 32, 32

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
        image = pygame.Surface((TILE_WIDTH, TILE_HEIGHT))
        transparent_color = (255, 0, 255)
        image.set_colorkey(transparent_color)
        image.fill(transparent_color)

        points = [(TILE_WIDTH / 2, 0), 
                  (0, TILE_HEIGHT), 
                  (TILE_WIDTH, TILE_HEIGHT)]

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
        return (TILE_HEIGHT * col, TILE_WIDTH * row)
