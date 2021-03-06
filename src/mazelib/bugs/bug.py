from ..maze import Maze

class Bug(object):
    NORTH = 1
    EAST  = 2
    SOUTH = 3
    WEST  = 4

    """
    Acts as an agent solving the maze. This base class serves as a place to
    put functions that might be useful for many different kinds of maze solvers.
    """
    def __init__(self, maze):
        self._maze = maze
        self._row = maze.start_row
        self._col = maze.start_col
        self._facing = Bug.EAST
        self._num_moves = 0

    def take_step(self):
        """
        Take a step in solving the maze. Subclasses should implement this
        function to solve the maze one step at a time
        """
        pass
    
    def is_valid_path(self, to_row, to_col):
        """
        Check whether a spot to move to is a valid place for a bug to visit.
        """
        if to_row < 0 or to_col < 0:
            return False

        (width, height) = self._maze.get_size()

        if to_row >= height or to_col >= width:
            return False

        return not self._maze(to_row, to_col).is_wall()

    def get_valid_moves(self):
        """
        Return a list of tuples to valid moves, always starting with north and
        moving clockwise
        """
        return self.get_valid_moves_from(self._row, self._col)

    def get_valid_moves_from(self, row, col):
        """
        Return a list of tuples to valid moves from (row, col), always 
        starting with north and moving clockwise
        """
        moves = []
        self._add_if_valid(moves, *self.get_north_from(row, col))
        self._add_if_valid(moves, *self.get_east_from(row, col))
        self._add_if_valid(moves, *self.get_south_from(row, col))
        self._add_if_valid(moves, *self.get_west_from(row, col))
        return moves

    def get_location(self):
        """
        Get the current location of the bug as a tuple (row, column)
        """
        return (self._row, self._col)

    def get_dir(self, direction):
        """
        Get the move to a direction
        """
        return self.get_dir_from(direction, self._row, self._col)


    def get_dir_from(self, direction, row, col):
        """
        Get the move to a direction from any place
        """
        if direction == Bug.NORTH:
            return self.get_north_from(row, col)
        elif direction == Bug.EAST:
            return self.get_east_from(row, col)
        elif direction == Bug.SOUTH:
            return self.get_south_from(row, col)
        elif direction == Bug.WEST:
            return self.get_west_from(row, col)

        assert False, "Bad direction value passed!"

    def get_north_from(self, row, col):
        """
        Get the position north of (row, col)
        """
        return ((row - 1, col))

    def get_north(self):
        """
        Return the position north of the current spot
        """
        return self.get_north_from(self._row, self._col)

    def get_east_from(self, row, col):
        """
        Return the position east of (row, col)
        """
        return ((row, col + 1))

    def get_east(self):
        """
        Return the position east of the current spot
        """
        return self.get_east_from(self._row, self._col)

    def get_south_from(self, row, col):
        """
        Return the position south of (row, col)
        """
        return ((row + 1, col))

    def get_south(self):
        """
        Return the position south of the current spot
        """
        return self.get_south_from(self._row, self._col)

    def get_west_from(self, row, col):
        """
        Return the position west of (row, col)
        """
        return ((row, col - 1))

    def get_west(self):
        """
        Return the position west of the current spot
        """
        return self.get_west_from(self._row, self._col)

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
        self._num_moves = self._num_moves + 1

        self._update_facing(to_row, to_col)
        self._row = to_row
        self._col = to_col

    def get_num_moves(self):
        return self._num_moves
        
    def get_facing(self):
        """
        Get the current facing of the bug
        """
        return self._facing

    def _update_facing(self, to_row, to_col):
        if (to_row, to_col) == self.get_north():
            self._facing = Bug.NORTH
        elif (to_row, to_col) == self.get_east():
            self._facing = Bug.EAST
        elif (to_row, to_col) == self.get_south():
            self._facing = Bug.SOUTH
        elif (to_row, to_col) == self.get_west():
            self._facing = Bug.WEST

    def _add_if_valid(self, moves, to_row, to_col):
        """
        Add the move specified by to_row and to_col to the moves list if
        it is a valid place to go.
        """
        if(self.is_valid_path(to_row, to_col)):
            moves.append((to_row, to_col))

        return moves

    def __str__(self):
        """
        Return the current position of the bug
        """
        return "(" + str(self._row) + "," + str(self._col) + ")"
