__author__ = 'tom'


class ShotDistance:
    OUTSIDE_EIGHTEEN, INSIDE_EIGHTEEN, INSIDE_SIX = range(3)

class ShotLocation:
    LEFT, CENTRE, RIGHT = range(3)

class ShotResult:
    GOAL, SAVED, BLOCKED, OFF_TARGET = range(4)

class MatchSummary:
    HOME_TEAM, AWAY_TEAM, HOME_GOALS, AWAY_GOALS, HOME_POSSESSION, AWAY_POSSESSION, HOME_FOULS, AWAY_FOULS = range(8)

class HostingStatus:
    HOME, AWAY = range(2)

class MatchResult:
    HOME_WIN, AWAY_WIN, DRAW = range(3)

class ShotTestData:
    GOALS, \
        SAVED, \
        ON_TARGET, \
        BLOCKED, \
        OFF_TARGET, \
        LEFT, \
        CENTRE, \
        RIGHT, \
        OUTSIDE_EIGHTEEN, \
        INSIDE_EIGHTEEN, \
        INSIDE_SIX = range(11)

class SetPieceTestData:
    PENALTY_GOALS, \
        PENALTY_MISSES, \
        PENALTY_ATTEMPTS, \
        FREE_KICK_GOALS, \
        FREE_KICKS_ON_TARGET, \
        FREE_KICK_ATTEMPTS = range(6)