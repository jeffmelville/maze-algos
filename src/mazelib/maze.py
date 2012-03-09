class MazeCell:
    
    WALL = 'X'
    PATH = ' '
    START = 'S'
    END = 'E'
    ALLOWED_TYPES = [WALL, 
                     PATH, 
                     START, 
                     END]
    

    def __init__(self, cell_type):
        if(cell_type not in MazeCell.ALLOWED_TYPES):
            raise ValueError("Cell must be one of " + 
                             str(MazeCell.ALLOWED_TYPES) + 
                             " (was " + cell_type + ")")

        self._cell_type = cell_type
        self._visit_count = 0

    def __str__(self):
        return self._cell_type

    def __repr__(self):
        return self._cell_type

    def is_wall(self):
        return self._cell_type == WALL

    def is_path(self):
        return self._cell_type == PATH

    def is_start(self):
        return self._cell_type == START

    def is_end(self):
        return self._cell_type == END

    def visit(self):
        self._visit_count = self._visit_count + 1

class Maze:
    def __init__(self, maze_file):
        if isinstance(maze_file, str):
            maze_file = open(maze_file, "r")

        self._maze = []

        for line in maze_file:
            this_row = []
            for cell in line.strip():
                this_row.append(MazeCell(cell))
            self._maze.append(this_row)
        
    def __str__(self):
        return "\n".join(["".join([str(cell) for cell in row]) 
                          for row in self._maze])
