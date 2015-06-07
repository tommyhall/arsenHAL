__author__ = 'tom'

import urllib2
from bs4 import BeautifulSoup
from Enums import ShotResult, MatchSummary, HostingStatus
from model.ShotData import ShotData
from model.TeamMatchData import TeamMatchData
from model.MatchData import MatchData


class MatchScraper(object):

    def __init__(self):

        # This will be defined outside of the class and passed into scrape_team_data()
        self._match_url = None

        self._summary_path = "/summary#tabs-wrapper-anchor"
        self._team_stats_path = "/team-stats/"

        # Shots (team)
        self._shots_path = "/0_SHOT_01#tabs-wrapper-anchor"
        self._penalties_path = "/0_SHOT_09#tabs-wrapper-anchor"
        self._free_kicks_path = "/0_SHOT_07#tabs-wrapper-anchor"

        # Passes (team)
        self._def_third_passes_path = "/1_PASS_0801#tabs-wrapper-anchor"
        self._mid_third_passes_path = "/1_PASS_0802#tabs-wrapper-anchor"
        self._att_third_passes_path = "/1_PASS_08#tabs-wrapper-anchor"
        self._backward_passes_path = "/1_PASS_15#tabs-wrapper-anchor"
        self._square_passes_path = "/1_PASS_16#tabs-wrapper-anchor"
        self._forward_passes_path = "/1_PASS_14#tabs-wrapper-anchor"
        self._long_passes_path = "/1_PASS_12#tabs-wrapper-anchor"
        self._short_passes_path = "/1_PASS_13#tabs-wrapper-anchor"
        self._chances_created_open_play_path = "/1_PASS_1101#tabs-wrapper-anchor"

        # Attack (team)
        self._crosses_path = "/2_ATTACK_01#tabs-wrapper-anchor"
        self._takeons_path = "/2_ATTACK_02#tabs-wrapper-anchor"
        self._corners_path = "/2_ATTACK_03#tabs-wrapper-anchor"

        # Defence (team)
        self._tackles_path = "/3_DEFENCE_01#tabs-wrapper-anchor"
        self._interceptions_path = "/3_DEFENCE_02#tabs-wrapper-anchor"
        self._blocks_path = "/3_DEFENCE_03#tabs-wrapper-anchor"

    def scrape_team_data(self, season, matchday, match_url):
        """ Scrape team data and store in MatchData object """

        print "preparing to scrape team data"
        self._match_url = match_url

        # MATCH SUMMARY
        home_id, away_id = self._find_team_ids()
        match_summary = self._scrape_match_summary()

        # Create home data obj and start plugging in the summary stats
        home_team_data = TeamMatchData(match_summary[MatchSummary.HOME_TEAM], HostingStatus.HOME)
        home_team_data.goals = match_summary[MatchSummary.HOME_GOALS]
        home_team_data.fouls = match_summary[MatchSummary.HOME_FOULS]
        home_team_data.possession_pct = match_summary[MatchSummary.HOME_POSSESSION]

        # Create away data obj and start plugging in the summary stats
        away_team_data = TeamMatchData(match_summary[MatchSummary.AWAY_TEAM], HostingStatus.AWAY)
        away_team_data.goals = match_summary[MatchSummary.AWAY_GOALS]
        away_team_data.fouls = match_summary[MatchSummary.AWAY_FOULS]
        away_team_data.possession_pct = match_summary[MatchSummary.AWAY_POSSESSION]

        home_team_data = self._scrape_team_data(home_team_data, home_id)
        away_team_data = self._scrape_team_data(away_team_data, away_id)

        match_data = MatchData(season, matchday, home_team_data, away_team_data)
        match_data.display_match_statistics()

        print "\n* done parsing match"
        return match_data

    def _scrape_team_data(self, team_data, team_id):
        """ Scrapes and parses attack, defence, shot, and pass data, stores in TeamMatchData object """

        # ATTACK
        team_data.crosses_successful, team_data.crosses_failed = \
            self._scrape_data(team_id, self._crosses_path, 'line')
        team_data.take_ons_successful, team_data.take_ons_failed = \
            self._scrape_data(team_id, self._takeons_path, 'image')
        team_data.corners_successful, team_data.corners_failed = \
            self._scrape_data(team_id, self._corners_path, 'line')

        # DEFENCE
        team_data.tackles_successful, team_data.tackles_failed = \
            self._scrape_data(team_id, self._tackles_path, 'image')
        null, team_data.interceptions = self._scrape_data(team_id, self._interceptions_path, 'image')
        null, team_data.blocks = self._scrape_data(team_id, self._blocks_path, 'image')

        # SHOTS
        team_data.shot_attempts = self._scrape_shots_data(team_id, team_data.team_name, self._shots_path)
        team_data.penalty_attempts = self._scrape_shots_data(team_id, team_data.team_name, self._penalties_path)
        team_data.free_kick_attempts = self._scrape_shots_data(team_id, team_data.team_name, self._free_kicks_path)

        # PASSES IN AREAS OF FIELD
        team_data.defensive_third_passes_successful, team_data.defensive_third_passes_failed = \
            self._scrape_data(team_id, self._def_third_passes_path, 'line')
        team_data.middle_third_passes_successful, team_data.middle_third_passes_failed = \
            self._scrape_data(team_id, self._mid_third_passes_path, 'line')
        team_data.attacking_third_passes_successful, team_data.attacking_third_passes_failed = \
            self._scrape_data(team_id, self._att_third_passes_path, 'line')

        # PASS DIRECTIONS
        team_data.backward_passes_successful, team_data.backward_passes_failed = \
            self._scrape_data(team_id, self._backward_passes_path, 'line')
        team_data.square_passes_successful, team_data.square_passes_failed = \
            self._scrape_data(team_id, self._square_passes_path, 'line')
        team_data.forward_passes_successful, team_data.forward_passes_failed = \
            self._scrape_data(team_id, self._forward_passes_path, 'line')

        # PASS DISTANCES
        team_data.short_passes_successful, team_data.short_passes_failed = \
            self._scrape_data(team_id, self._short_passes_path, 'line')
        team_data.long_passes_successful, team_data.long_passes_failed = \
            self._scrape_data(team_id, self._long_passes_path, 'line')

        team_data.chances_created_open_play, null = \
            self._scrape_data(team_id, self._chances_created_open_play_path, 'line')

        return team_data

    def _find_team_ids(self):
        """ Finds the team IDs to be able to visit each page """

        url = self._match_url + self._summary_path
        response = urllib2.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html)

        # The charts on the match summary page contain a link to the home team stats; we can get the home id from there
        charts = soup.find_all('div', id='charts')[0]
        chart_links = charts('a')
        home_team_stats_link = chart_links[0]['href']
        home_id = home_team_stats_link.split('/')[6]

        # We need to travel to the home team stats page to get the away team id
        url = 'http://www.fourfourtwo.com' + home_team_stats_link
        response = urllib2.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html)

        teams_list = soup.find_all('ul', id='statzone_pitch_team_filter')[0]
        away_junk = teams_list.find_all('li', class_='last')[0]
        away_id = away_junk.find_all('a')[0]['href'].split('/')[6]

        return home_id, away_id


    def _scrape_match_summary(self):
        """ Scrapes and parses the match summary page. """

        url = self._match_url + self._summary_path
        response = urllib2.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html)

        # TEAMS
        home_team = soup.find_all('span', class_='home-head')[0].get_text().replace(' ', '')
        away_team = soup.find_all('span', class_='away-head')[0].get_text().replace(' ', '')
        home_team = home_team.strip()
        away_team = away_team.strip()

        # SCORE
        score_text = soup.find_all('span', class_='score')[0].get_text().replace(' ', '')
        score = score_text.split('-')
        home_goals = score[0].strip()
        away_goals = score[1].strip()

        # POSSESSION
        possession_data = soup.find_all(id='summary_possessions')[0]
        possession_summaries = possession_data.find_all('text')
        home_possession = possession_summaries[0].get_text().split('%')[0]
        away_possession = possession_summaries[1].get_text().split('%')[0]

        # FOULS
        foul_data = soup.find_all(id='summary_fouls')[0]
        foul_summaries = foul_data.find_all('text')
        home_fouls = foul_summaries[0].get_text()
        away_fouls = foul_summaries[1].get_text()

        return home_team, away_team, home_goals, away_goals, home_possession, away_possession, home_fouls, away_fouls

    def _scrape_data(self, team, stat_path, html_tag):
        """ Scrapes and parses the given stat for the given team by parsing the given HTML tag. """

        url = self._match_url + self._team_stats_path + team + stat_path
        response = urllib2.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html)

        success = len(soup.find_all(html_tag, class_='success'))
        fail = len(soup.find_all(html_tag, class_='fail'))
        return success, fail

    def _scrape_shots_data(self, team_id, team_name, stat_path):
        """ Scrapes and returns shot data. """

        url = self._match_url + self._team_stats_path + team_id + stat_path
        response = urllib2.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html)

        goals = soup.find_all('line', style='stroke:yellow;stroke-width:3')
        saved = soup.find_all('line', style='stroke:blue;stroke-width:3')
        blocked = soup.find_all('line', style='stroke:darkgrey;stroke-width:3')
        off_target = soup.find_all('line', style='stroke:red;stroke-width:3')

        shots = []

        for attempt in goals:
            origin_x, origin_y, end_x, end_y = self._get_shot_coordinates(attempt)
            shot = ShotData(team_name, ShotResult.GOAL, origin_x, origin_y, end_x, end_y)
            shots.append(shot)

        for attempt in saved:
            origin_x, origin_y, end_x, end_y = self._get_shot_coordinates(attempt)
            shot = ShotData(team_name, ShotResult.SAVED, origin_x, origin_y, end_x, end_y)
            shots.append(shot)

        for attempt in blocked:
            origin_x, origin_y, end_x, end_y = self._get_shot_coordinates(attempt)
            shot = ShotData(team_name, ShotResult.BLOCKED, origin_x, origin_y, end_x, end_y)
            shots.append(shot)

        for attempt in off_target:
            origin_x, origin_y, end_x, end_y = self._get_shot_coordinates(attempt)
            shot = ShotData(team_name, ShotResult.OFF_TARGET, origin_x, origin_y, end_x, end_y)
            shots.append(shot)

        return shots

    def _get_shot_coordinates(self, shot):
        """ Given a shot, returns the (x,y) coordinates of its origin and endpoint. """
        origin_x = shot['x1']
        origin_y = shot['y1']
        end_x = shot['x2']
        end_y = shot['y2']
        return origin_x, origin_y, end_x, end_y