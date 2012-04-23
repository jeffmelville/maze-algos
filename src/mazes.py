#!/usr/bin/python
import argparse
import sys

import pygame

import mazelib
from mazerunner import MazeRunner

BUG_IMPLS = {
    "RightWallFollower" : mazelib.bugs.RightWallFollower,
    "Wavefront"         : mazelib.bugs.Wavefront
}

def main():
    argparser = argparse.ArgumentParser(description = "A maze solving program")

    argparser.add_argument('-m','--maze', 
                           help="The maze file to load",
                           required=True)

    argparser.add_argument('-b','--bug', 
                           help="The type of bug to to solve the maze",
                           required=True)

    args = argparser.parse_args(sys.argv[1:])

    pygame.init()

    maze = mazelib.GraphicMaze(args.maze)
    bug = get_bug(args.bug, maze)

    MazeRunner(maze, bug).main()

def get_bug(name, maze):
    return BUG_IMPLS[name](maze)


if __name__ == "__main__": main()
