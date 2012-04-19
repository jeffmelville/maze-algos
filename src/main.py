#!/usr/bin/python

import mazelib
import pygame

def main():
    maze = mazelib.GraphicMaze("../mazes/maze1.txt")
    pygame.init()
    pygame.display.set_mode((1344,320))
    print maze

    bug = mazelib.Bug(maze)
    bug.move_to(7,1); print bug
    bug.move_to(8,1); print bug
    bug.move_to(8,2); print bug

    print ("Start: (" + str(maze.start_row) + "," +
        str(maze.start_col) + ") : " +
        str(maze(maze.start_row, maze.start_col)))
    #pygame.display.set_mode((maze.get_width(), maze.get_height()))
    mazelib.TestGame(maze).main()

if __name__ == "__main__": main()