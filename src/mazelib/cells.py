class MazeCell:
    def __init__(self):
        self._visit_count = 0

    def is_wall(self):
        return False

    def is_path(self):
        return False

    def is_start(self):
        return False

    def is_end(self):
        return False

    def visit(self):
        self._visit_count = self._visit_count + 1

WALL = 'X'
PATH = ' '
START = 'S'
END = 'E'

class WallCell(MazeCell):
    def __init__(self):
        MazeCell.__init__(self)

    def __str__(self):
        return WALL

    def __repr(self):
        return "WallCell(\"" + WALL + "\")"

    def is_wall(self):
        return True

class PathCell(MazeCell):
    def __init__(self):
        MazeCell.__init__(self)

    def __str__(self):
        return PATH

    def __repr(self):
        return "PathCell(\"" + PATH + "\")"

    def is_path(self):
        return True

class StartCell(MazeCell):
    def __init__(self):
        MazeCell.__init__(self)

    def __str__(self):
        return START

    def __repr(self):
        return "StartCell(\"" + START + "\")"


    def is_start(self):
        return True

class EndCell(MazeCell):
    def __init__(self):
        MazeCell.__init__(self)

    def __str__(self):
        return END

    def __repr(self):
        return "EndCell(\"" + END + "\")"


    def is_end(self):
        return True


CELL_TYPES = { WALL : WallCell, 
               PATH : PathCell, 
               START: StartCell, 
               END  : EndCell }


def cell_factory(cell_type):
    if(cell_type not in CELL_TYPES):
        raise ValueError("Cell must be one of " + 
                         str(CELL_TYPES) + 
                         " (was " + cell_type + ")")

    return CELL_TYPES[cell_type]()
