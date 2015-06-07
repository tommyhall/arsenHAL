__author__ = 'tom'

# Represents match data for a team

from Enums import ShotResult, ShotDistance, ShotLocation


class TeamMatchData(object):

    def __init__(self, team_name, hosting_status):

        self._team_name = team_name
        self._hosting_status = hosting_status  # home or away

        # Summary statistics
        self._possession_pct = None
        self._fouls = None
        self._goals = None

        # Attacking statistics
        self._crosses_successful = None
        self._crosses_failed = None
        self._corners_successful = None
        self._corners_failed = None
        self._take_ons_successful = None
        self._take_ons_failed = None

        # Defensive statistics
        self._tackles_successful = None
        self._tackles_failed = None
        self._interceptions = None
        self._blocks = None

        # Passing statistics
        self._defensive_third_passes_successful = None
        self._defensive_third_passes_failed = None
        self._middle_third_passes_successful = None
        self._middle_third_passes_failed = None
        self._attacking_third_passes_successful = None
        self._attacking_third_passes_failed = None
        self._backward_passes_successful = None
        self._backward_passes_failed = None
        self._square_passes_successful = None
        self._square_passes_failed = None
        self._forward_passes_successful = None
        self._forward_passes_failed = None
        self._short_passes_successful = None
        self._short_passes_failed = None
        self._long_passes_successful = None
        self._long_passes_failed = None
        self._chances_created_open_play = None

        # Shooting statistics
        self._shot_attempts = []
        self._penalty_attempts = []
        self._free_kick_attempts = []

    @property
    def team_name(self):
        return self._team_name

    @property
    def hosting_status(self):
        """ Home/away status of this team """
        return self._hosting_status

    @property
    def possession_pct(self):
        return self._possession_pct

    @possession_pct.setter
    def possession_pct(self, value):
        self._possession_pct = float(value)

    @property
    def fouls(self):
        return self._fouls

    @fouls.setter
    def fouls(self, value):
        self._fouls = int(value)

    @property
    def goals(self):
        return self._goals

    @goals.setter
    def goals(self, value):
        self._goals = int(value)

    def number_of_goals_scored(self):
        return sum(1 for shot in self._shot_attempts if shot.result == ShotResult.GOAL)

    def own_goals_awarded(self):
        return self._goals - self.number_of_goals_scored()

    @property
    def crosses_successful(self):
        return self._crosses_successful

    @crosses_successful.setter
    def crosses_successful(self, value):
        self._crosses_successful = int(value)

    @property
    def crosses_failed(self):
        return self._crosses_failed

    @crosses_failed.setter
    def crosses_failed(self, value):
        self._crosses_failed = int(value)

    @property
    def corners_successful(self):
        return self._corners_successful

    @corners_successful.setter
    def corners_successful(self, value):
        self._corners_successful = int(value)

    @property
    def corners_failed(self):
        return self._corners_failed

    @corners_failed.setter
    def corners_failed(self, value):
        self._corners_failed = int(value)

    @property
    def take_ons_successful(self):
        return self._take_ons_successful

    @take_ons_successful.setter
    def take_ons_successful(self, value):
        self._take_ons_successful = int(value)

    @property
    def take_ons_failed(self):
        return self._take_ons_failed

    @take_ons_failed.setter
    def take_ons_failed(self, value):
        self._take_ons_failed = int(value)

    @property
    def tackles_successful(self):
        return self._tackles_successful

    @tackles_successful.setter
    def tackles_successful(self, value):
        self._tackles_successful = int(value)

    @property
    def tackles_failed(self):
        return self._tackles_failed

    @tackles_failed.setter
    def tackles_failed(self, value):
        self._tackles_failed = int(value)

    @property
    def interceptions(self):
        return self._interceptions

    @interceptions.setter
    def interceptions(self, value):
        self._interceptions = int(value)

    @property
    def blocks(self):
        return self._blocks

    @blocks.setter
    def blocks(self, value):
        self._blocks = int(value)

    @property
    def shot_attempts(self):
        return self._shot_attempts

    @shot_attempts.setter
    def shot_attempts(self, shot_attempts_list):
        self._shot_attempts = shot_attempts_list

    def shots_on_target(self):
        return sum(1 for shot in self._shot_attempts
                   if shot.result == ShotResult.SAVED
                   or shot.result == ShotResult.GOAL)

    def shots_saved(self):
        return sum(1 for shot in self._shot_attempts
                   if shot.result == ShotResult.SAVED)

    def shots_blocked(self):
        return sum(1 for shot in self._shot_attempts
                   if shot.result == ShotResult.BLOCKED)

    def shots_off_target(self):
        return sum(1 for shot in self._shot_attempts
                   if shot.result == ShotResult.OFF_TARGET)

    def shots_outside_eighteen_yard_box(self):
        return sum(1 for shot in self._shot_attempts
                   if shot.distance == ShotDistance.OUTSIDE_EIGHTEEN)

    def shots_inside_eighteen_yard_box(self):
        return sum(1 for shot in self._shot_attempts
                   if shot.distance == ShotDistance.INSIDE_EIGHTEEN
                   or shot.distance == ShotDistance.INSIDE_SIX)

    def shots_inside_six_yard_box(self):
        return sum(1 for shot in self._shot_attempts
                   if shot.distance == ShotDistance.INSIDE_SIX)

    def shots_from_left_of_goal(self):
        return sum(1 for shot in self._shot_attempts if shot.location == ShotLocation.LEFT)

    def shots_from_centre_of_goal(self):
        return sum(1 for shot in self._shot_attempts if shot.location == ShotLocation.CENTRE)

    def shots_from_right_of_goal(self):
        return sum(1 for shot in self._shot_attempts if shot.location == ShotLocation.RIGHT)

    def total_shot_attempts(self):
        return len(self._shot_attempts)

    @property
    def free_kick_attempts(self):
        return self._free_kick_attempts

    @free_kick_attempts.setter
    def free_kick_attempts(self, list_of_attempts):
        self._free_kick_attempts = list_of_attempts

    def free_kick_goals(self):
        return sum(1 for attempt in self._free_kick_attempts if attempt.result == ShotResult.GOAL)

    def free_kicks_on_target(self):
        return sum(1 for attempt in self._free_kick_attempts if attempt.result == ShotResult.GOAL
                   or attempt.result == ShotResult.SAVED)

    def total_free_kick_attempts(self):
        return len(self._free_kick_attempts)

    @property
    def penalty_attempts(self):
        return self._penalty_attempts

    @penalty_attempts.setter
    def penalty_attempts(self, list_of_attempts):
        self._penalty_attempts = list_of_attempts

    def penalty_goals(self):
        return sum(1 for shot in self._penalty_attempts if shot.result == ShotResult.GOAL)

    def penalties_missed(self):
        return sum(1 for shot in self._penalty_attempts if shot.result != ShotResult.GOAL)

    def total_penalty_attempts(self):
        return len(self._penalty_attempts)

    @property
    def defensive_third_passes_successful(self):
        return self._defensive_third_passes_successful

    @defensive_third_passes_successful.setter
    def defensive_third_passes_successful(self, value):
        self._defensive_third_passes_successful = int(value)

    @property
    def defensive_third_passes_failed(self):
        return self._defensive_third_passes_failed

    @defensive_third_passes_failed.setter
    def defensive_third_passes_failed(self, value):
        self._defensive_third_passes_failed = int(value)

    @property
    def middle_third_passes_successful(self):
        return self._middle_third_passes_successful

    @middle_third_passes_successful.setter
    def middle_third_passes_successful(self, value):
        self._middle_third_passes_successful = int(value)

    @property
    def middle_third_passes_failed(self):
        return self._middle_third_passes_failed

    @middle_third_passes_failed.setter
    def middle_third_passes_failed(self, value):
        self._middle_third_passes_failed = int(value)

    @property
    def attacking_third_passes_successful(self):
        return self._attacking_third_passes_successful

    @attacking_third_passes_successful.setter
    def attacking_third_passes_successful(self, value):
        self._attacking_third_passes_successful = int(value)

    @property
    def attacking_third_passes_failed(self):
        return self._attacking_third_passes_failed

    @attacking_third_passes_failed.setter
    def attacking_third_passes_failed(self, value):
        self._attacking_third_passes_failed = int(value)

    @property
    def backward_passes_successful(self):
        return self._backward_passes_successful

    @backward_passes_successful.setter
    def backward_passes_successful(self, value):
        self._backward_passes_successful = int(value)

    @property
    def backward_passes_failed(self):
        return self._backward_passes_failed

    @backward_passes_failed.setter
    def backward_passes_failed(self, value):
        self._backward_passes_failed = int(value)

    @property
    def square_passes_successful(self):
        return self._square_passes_successful

    @square_passes_successful.setter
    def square_passes_successful(self, value):
        self._square_passes_successful = int(value)

    @property
    def square_passes_failed(self):
        return self._square_passes_failed

    @square_passes_failed.setter
    def square_passes_failed(self, value):
        self._square_passes_failed = int(value)

    @property
    def forward_passes_successful(self):
        return self._forward_passes_successful

    @forward_passes_successful.setter
    def forward_passes_successful(self, value):
        self._forward_passes_successful = int(value)

    @property
    def forward_passes_failed(self):
        return self._forward_passes_failed

    @forward_passes_failed.setter
    def forward_passes_failed(self, value):
        self._forward_passes_failed = int(value)

    @property
    def short_passes_successful(self):
        return self._short_passes_successful

    @short_passes_successful.setter
    def short_passes_successful(self, value):
        self._short_passes_successful = int(value)

    @property
    def short_passes_failed(self):
        return self._short_passes_failed

    @short_passes_failed.setter
    def short_passes_failed(self, value):
        self._short_passes_failed = int(value)

    @property
    def long_passes_successful(self):
        return self._long_passes_successful

    @long_passes_successful.setter
    def long_passes_successful(self, value):
        self._long_passes_successful = int(value)

    @property
    def long_passes_failed(self):
        return self._long_passes_failed

    @long_passes_failed.setter
    def long_passes_failed(self, value):
        self._long_passes_failed = int(value)

    @property
    def chances_created_open_play(self):
        return self._chances_created_open_play

    @chances_created_open_play.setter
    def chances_created_open_play(self, value):
        self._chances_created_open_play = int(value)

    def total_passes_successful(self):
        return self._defensive_third_passes_successful + \
            self._middle_third_passes_successful + \
            self._attacking_third_passes_successful

    def total_passes_failed(self):
        return self._defensive_third_passes_failed + \
            self._middle_third_passes_failed + \
            self._attacking_third_passes_failed

    def total_pass_attempts(self):
        return self.total_passes_successful + self.total_passes_failed