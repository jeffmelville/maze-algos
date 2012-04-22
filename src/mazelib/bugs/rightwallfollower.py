from graphicbug import GraphicBug
from bug import Bug

class RightWallFollower(GraphicBug):
    
    RIGHT_TURNS = {
        Bug.NORTH : [Bug.EAST, Bug.NORTH, Bug.WEST, Bug.SOUTH],
        Bug.EAST  : [Bug.SOUTH, Bug.EAST, Bug.NORTH, Bug.WEST],
        Bug.SOUTH : [Bug.WEST, Bug.SOUTH, Bug.EAST, Bug.NORTH],
        Bug.WEST  : [Bug.NORTH, Bug.WEST, Bug.SOUTH, Bug.EAST],
    }

    def __init__(self, maze):
        super(RightWallFollower,self).__init__(maze)

    def take_step(self):
        places_to_move = RightWallFollower.RIGHT_TURNS[self.get_facing()]

        #Bail if we've already solved the maze
        if self._maze(*self.get_location()).is_end():
            return

        for direction in places_to_move:
            new_pos = self.get_dir(direction)
            if self.is_valid_path(*new_pos):
                self.move_to(*new_pos)
                return

        assert False, "Nowhere to move!"
