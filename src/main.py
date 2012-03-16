#!/usr/bin/python

import mazelib

if __name__ == "__main__":
    maze = mazelib.Maze("../mazes/maze1.txt")

    print maze
    print ("Start: (" + str(maze.start_row) + "," +
           str(maze.start_col) + ") : " +
           str(maze(maze.start_row, maze.start_col)))
