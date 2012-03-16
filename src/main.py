#!/usr/bin/python

import mazelib

if __name__ == "__main__":
    maze = mazelib.Maze("../mazes/maze1.txt")

    print maze

    bug = mazelib.Bug(maze)
    bug.move_to(7,1); print bug
    bug.move_to(8,1); print bug
    bug.move_to(8,2); print bug
    
    print ("Start: (" + str(maze.start_row) + "," +
           str(maze.start_col) + ") : " +
           str(maze(maze.start_row, maze.start_col)))
