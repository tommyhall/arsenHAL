__author__ = 'tom'

from Enums import MatchResult


class MatchData(object):

    def __init__(self, season, matchday, home_team_data, away_team_data):
        self._season = season
        self._matchday = matchday
        self._home_team_data = home_team_data  # a TeamMatchData object
        self._away_team_data = away_team_data  # a TeamMatchData object
        self._home_goals = home_team_data.number_of_goals_scored() + home_team_data.own_goals_awarded()
        self._away_goals = away_team_data.number_of_goals_scored() + away_team_data.own_goals_awarded()
        self._result = self._get_result()
        self._winner = self._get_winner()

    @property
    def home_team_data(self):
        return self._home_team_data

    @property
    def away_team_data(self):
        return self._away_team_data

    @property
    def season(self):
        return self._season

    @property
    def matchday(self):
        return self._matchday

    @property
    def home_goals(self):
        return self._home_goals

    @property
    def away_goals(self):
        return self._away_goals

    @property
    def result(self):
        return self._result

    @property
    def winner(self):
        return self._winner

    def _get_result(self):
        if self._home_goals > self._away_goals:
            return MatchResult.HOME_WIN
        elif self._home_goals < self._away_goals:
            return MatchResult.AWAY_WIN
        else:
            return MatchResult.DRAW

    def _get_winner(self):
        if self._result == MatchResult.HOME_WIN:
            return self._home_team_data.team_name
        elif self._result == MatchResult.AWAY_WIN:
            return self._away_team_data.team_name
        else:
            return None

    def display_match_statistics(self):
        pass