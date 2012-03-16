from maze import Maze

class Bug:
    """
    Acts as an agent solving the maze. This base class serves as a place to
    put functions that might be useful for many different kinds of maze solvers.
    """
    def __init__(self, maze):
        self._maze = maze
        self._row = maze.start_row
        self._col = maze.start_col
    
    def is_valid_path(self, to_row, to_col):
        """
        Check whether a spot to move to is a valid place for a bug to visit.
        """
        return not self._maze(to_row, to_col).is_wall()

    def get_valid_moves(self):
        """
        Return a list of tuples to valid moves, always starting with north and
        moving clockwise
        """
        pass

    def is_one_away(self, to_row, to_col):
        """
        Check to see whether a space is one move away from the current location
        """
        return abs(to_row - self._row) + abs(to_col - self._col) == 1

    def move_to(self, to_row, to_col):
        """
        Move the bug to a new space
        """
        assert self.is_valid_path(to_row, to_col), "Tried to move into a wall!"
        assert self.is_one_away(to_row, to_col), "That spot is too far away!"

        self._row = to_row
        self._col = to_col

    def __str__(self):
        """
        Return the current position of the bug
        """
        return "(" + str(self._row) + "," + str(self._col) + ")"
