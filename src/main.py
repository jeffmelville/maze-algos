#!/usr/bin/python

import mazelib

def main():
    maze = mazelib.GraphicMaze("../mazes/maze2.txt")
    print maze

    bug = mazelib.Bug(maze)
    bug.move_to(7,1); print bug
    bug.move_to(8,1); print bug
    bug.move_to(8,2); print bug

    print ("Start: (" + str(maze.start_row) + "," +
           str(maze.start_col) + ") : " +
           str(maze(maze.start_row, maze.start_col)))
    

    mazelib.TestGame(maze).main()


if __name__ == "__main__": main()
