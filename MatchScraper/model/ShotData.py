__author__ = 'tom'

from Enums import ShotDistance, ShotLocation

EDGE_OF_EIGHTEEN_YARD_BOX_Y = 400.0
EDGE_OF_SIX_YARD_BOX_Y = 235.0
LEFT_POST_X = 315.0
RIGHT_POST_X = 445.0


class ShotData(object):

    def __init__(self, team, result, origin_x, origin_y, end_x, end_y):

        self._team = team
        self._result = result

        self._origin_x = float(origin_x)
        self._origin_y = float(origin_y)
        self._end_x = float(end_x)
        self._end_y = float(end_y)

        # These will be calculated later
        self._distance = self._find_distance()
        self._location = self._find_location()

    @property
    def team(self):
        return self._team

    @property
    def result(self):
        return self._result

    @property
    def distance(self):
        return self._distance

    @property
    def location(self):
        return self._location

    def _find_distance(self):
        """ Given the shot's origin, determine the distance from which it originated. """

        distance = None
        if self._origin_y > EDGE_OF_EIGHTEEN_YARD_BOX_Y:
            distance = ShotDistance.OUTSIDE_EIGHTEEN
        elif EDGE_OF_SIX_YARD_BOX_Y < self._origin_y <= EDGE_OF_EIGHTEEN_YARD_BOX_Y:
            distance = ShotDistance.INSIDE_EIGHTEEN
        elif self._origin_y <= EDGE_OF_SIX_YARD_BOX_Y:
            distance = ShotDistance.INSIDE_SIX
        return distance

    def _find_location(self):
        """ Given the shot's origin, determine if it originated from the left, right, or in front of goal. """

        location = None
        if self._origin_x < LEFT_POST_X:
            location = ShotLocation.LEFT
        elif LEFT_POST_X <= self._origin_x <= RIGHT_POST_X:
            location = ShotLocation.CENTRE
        elif self._origin_x > RIGHT_POST_X:
            location = ShotLocation.RIGHT
        return location