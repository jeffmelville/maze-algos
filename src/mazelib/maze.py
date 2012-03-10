import cells

class Maze:
    def __init__(self, maze_file):
        if isinstance(maze_file, str):
            maze_file = open(maze_file, "r")

        self._maze = []

        for line in maze_file:
            this_row = []
            for cell in line.strip():
                this_row.append(cells.cell_factory(cell))
            self._maze.append(this_row)
        
    def __str__(self):
        return "\n".join(["".join([str(cell) for cell in row]) 
                          for row in self._maze])
