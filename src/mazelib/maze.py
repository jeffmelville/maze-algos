import cells

class Maze:
    def __init__(self, maze_file):
        if isinstance(maze_file, str):
            maze_file = open(maze_file, "r")

        self._maze = []

        rownum = 0
        for line in maze_file:
            this_row = []
            colnum = 0
            for cell in line.strip():
                maze_cell = cells.cell_factory(cell)
                if(maze_cell.is_start()):
                    self.start_col = colnum
                    self.start_row = rownum

                this_row.append(maze_cell)
                colnum = colnum + 1
                
            self._maze.append(this_row)
            rownum = rownum + 1

    def get_size(self):
        width = 0
        height = len(self._maze)
        if height: width = len(self._maze[0])
        return (width, height)

    def get_height(self):
        return self.get_size()[1]

    def get_width(self):
        return self.get_size()[0]


    def __call__(self, row, col):
        return self._maze[row][col]
        
    def __str__(self):
        return "\n".join(["".join([str(cell) for cell in row]) 
                          for row in self._maze])
