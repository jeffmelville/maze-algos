from graphicbug import GraphicBug
from bug import Bug
from ..graphicmaze import GraphicMaze

import pygame

from collections import deque

class Wavefront(GraphicBug):

    def __init__(self, maze):
        super(Wavefront, self).__init__(maze)
        (width, height) = maze.get_size()

        self._to_compute = deque() #queue of waves to fill in
        self._waves = [] #keeps track of the waves
        for row in range(0, height):
            self._waves.append([-1]*width)

        self._waves[maze.end_row][maze.end_col] = 0
        self._to_compute.append((maze.end_row, maze.end_col))

        fontname = pygame.font.get_default_font()
        self._font = pygame.font.Font(fontname, 20)

    def take_step(self):
        if self._maze(*self.get_location()).is_end():
            return

        if len(self._to_compute) > 0:
            self._fill_wavefront()
        else:
            self._follow_wavefront()

    def _follow_wavefront(self):
        adjacent_paths = self.get_valid_moves()
        next_row, next_col = 0, 0
        min_val = self._waves[self._row][self._col]
        for (row, col) in adjacent_paths:
            if self._waves[row][col] < min_val:
                min_val = self._waves[row][col]
                next_row, next_col = row, col

        self.move_to(next_row, next_col)
            

    def _fill_wavefront(self):
        (cur_row, cur_col) = self._to_compute.popleft()
        adjacent_paths = self.get_valid_moves_from(cur_row, cur_col)

        for (row, col) in adjacent_paths:
            if(self._waves[row][col] == -1):
                cur_dist = self._waves[cur_row][cur_col]
                self._waves[row][col] = cur_dist + 1
                self._to_compute.append((row, col))

    def render_overlay(self):
        """
        Render the wavefront distance overlay image
        """
        black = (0,0,0)
        white = (255,255,255)
        transparent_color = (255, 0, 255)

        image_size = self._maze.get_screen_size()
        image = pygame.Surface(image_size)
        image.set_colorkey(transparent_color)
        image.fill(transparent_color)

        for map_y in range(len(self._waves)):
            for map_x in range(len(self._waves[map_y])):
                if(self._waves[map_y][map_x] != -1):
                    text = self._font.render(str(self._waves[map_y][map_x]),
                                             True, black)

                    (x_off, y_off) = self._center_text(text)
                    position = (map_x*GraphicMaze.TILE_WIDTH  + x_off, 
                                map_y*GraphicMaze.TILE_HEIGHT + y_off)
                    image.blit(text, position)

        return image

    def _center_text(self, image):
        """
        Calculate the additional offsets required to center the numbers in
        a tile.
        """
        y_offset = (GraphicMaze.TILE_HEIGHT / 2) - (image.get_height() / 2)
        x_offset = (GraphicMaze.TILE_WIDTH  / 2) - (image.get_width()  / 2)

        return (x_offset, y_offset)

