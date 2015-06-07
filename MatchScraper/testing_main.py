__author__ = 'tom'

import unittest
from model.TeamMatchData import TeamMatchData
from MatchScraper import MatchScraper
from Enums import HostingStatus, ShotTestData, SetPieceTestData


class TestTeamData(unittest.TestCase):

    def _test_team_data(self, known_data, scraped_data):
        """ Compare our "known" TeamData object with the scraped TeamData object """

        print "\tTesting --> _test_team_data"

        # Match summary
        self.assertEqual(known_data.team_name, scraped_data.team_name,
                         'Names: known = %s, scraped = %s' % (known_data.team_name, scraped_data.team_name))
        self.assertEqual(known_data.hosting_status, scraped_data.hosting_status,
                         'Hosting: known = %s, scraped = %s' % (known_data.hosting_status, scraped_data.hosting_status))
        self.assertEqual(known_data.possession_pct, scraped_data.possession_pct,
                         'Possession: known = %.2f, scraped = %.2f' % (known_data.possession_pct,
                                                                       scraped_data.possession_pct))
        self.assertEqual(known_data.fouls, scraped_data.fouls,
                         'Fouls: known = %i, scraped = %i' % (known_data.fouls, scraped_data.fouls))
        self.assertEqual(known_data.goals, scraped_data.own_goals_awarded() + scraped_data.number_of_goals_scored(),
                         'Goals: known=%i scraped=%i' % (known_data.goals,
                                                         scraped_data.number_of_goals_scored() +
                                                         scraped_data.own_goals_awarded()))

        # Attack
        self.assertEqual(known_data.crosses_successful, scraped_data.crosses_successful,
                         'Crosses successful: known=%i scraped=%i' % (known_data.crosses_successful,
                                                                      scraped_data.crosses_successful))
        self.assertEqual(known_data.crosses_failed, scraped_data.crosses_failed,
                         'Crosses failed: known=%i scraped=%i' % (known_data.crosses_failed,
                                                                  scraped_data.crosses_failed))
        self.assertEqual(known_data.take_ons_successful, scraped_data.take_ons_successful,
                         'Takeons successful: known=%i scraped=%i' % (known_data.take_ons_successful,
                                                                      scraped_data.take_ons_successful))
        self.assertEqual(known_data.take_ons_failed, scraped_data.take_ons_failed,
                         'Takeons failed: known=%i scraped=%i' % (known_data.take_ons_failed,
                                                                  scraped_data.take_ons_failed))
        self.assertEqual(known_data.corners_successful, scraped_data.corners_successful,
                         'Corners successful: known=%i scraped=%i' % (known_data.corners_successful,
                                                                      scraped_data.corners_successful))
        self.assertEqual(known_data.corners_failed, scraped_data.corners_failed,
                         'Corners failed: known=%i scraped=%i' % (known_data.corners_failed,
                                                                  scraped_data.corners_failed))

        # Defence
        self.assertEqual(known_data.tackles_successful, scraped_data.tackles_successful,
                         'Tackles successful: known=%i scraped=%i' % (known_data.tackles_successful,
                                                                      scraped_data.tackles_successful))
        self.assertEqual(known_data.tackles_failed, scraped_data.tackles_failed,
                         'Tackles failed: known=%i scraped=%i' % (known_data.tackles_failed,
                                                                  scraped_data.tackles_failed))
        self.assertEqual(known_data.blocks, scraped_data.blocks,
                         'Blocks: known=%i scraped=%i' % (known_data.blocks, scraped_data.blocks))
        self.assertEqual(known_data.interceptions, scraped_data.interceptions,
                         'Interceptions: known=%i scraped=%i' % (known_data.interceptions, scraped_data.interceptions))

        # Passes
        self.assertEqual(known_data.attacking_third_passes_successful, scraped_data.attacking_third_passes_successful,
                         'Attacking 1/3 successful: known=%i scrape=%i' % (known_data.attacking_third_passes_successful,
                                                                            scraped_data.attacking_third_passes_successful))
        self.assertEqual(known_data.attacking_third_passes_failed, scraped_data.attacking_third_passes_failed,
                         'Attacking 1/3 failed: known=%i scraped=%i' % (known_data.attacking_third_passes_failed,
                                                                        scraped_data.attacking_third_passes_failed))
        self.assertEqual(known_data.middle_third_passes_successful, scraped_data.middle_third_passes_successful,
                         'Middle 1/3 successful: known=%i scraped=%i' % (known_data.middle_third_passes_successful,
                                                                         scraped_data.middle_third_passes_successful))
        self.assertEqual(known_data.middle_third_passes_failed, scraped_data.middle_third_passes_failed,
                         'Middle 1/3 failed: known=%i scraped=%i' % (known_data.middle_third_passes_failed,
                                                                     scraped_data.middle_third_passes_failed))
        self.assertEqual(known_data.defensive_third_passes_successful, scraped_data.defensive_third_passes_successful,
                         'Def 1/3 successful: known=%i scraped=%i' % (known_data.defensive_third_passes_successful,
                                                                      scraped_data.defensive_third_passes_successful))
        self.assertEqual(known_data.defensive_third_passes_failed, scraped_data.defensive_third_passes_failed,
                         'Def 1/3 failed: known=%i scraped=%i' % (known_data.defensive_third_passes_failed,
                                                                  scraped_data.defensive_third_passes_failed))
        self.assertEqual(known_data.forward_passes_successful, scraped_data.forward_passes_successful,
                         'Forward successful: known=%i scraped=%i' % (known_data.forward_passes_successful,
                                                                      scraped_data.forward_passes_successful))
        self.assertEqual(known_data.forward_passes_failed, scraped_data.forward_passes_failed,
                         'Forward failed: known=%i scraped=%i' % (known_data.forward_passes_failed,
                                                                  scraped_data.forward_passes_failed))
        self.assertEqual(known_data.square_passes_successful, scraped_data.square_passes_successful,
                         'Square successful: known=%i scraped=%i' % (known_data.square_passes_successful,
                                                                   scraped_data.square_passes_successful))
        self.assertEqual(known_data.square_passes_failed, scraped_data.square_passes_failed,
                         'Square failed: known=%i scraped=%i' % (known_data.square_passes_failed,
                                                                 scraped_data.square_passes_failed))
        self.assertEqual(known_data.backward_passes_successful, scraped_data.backward_passes_successful,
                         'Back successful: known=%i scraped=%i' % (known_data.backward_passes_successful,
                                                                   scraped_data.backward_passes_successful))
        self.assertEqual(known_data.backward_passes_failed, scraped_data.backward_passes_failed,
                         'Back failed: known=%i scraped=%i' % (known_data.backward_passes_failed,
                                                               scraped_data.backward_passes_failed))
        self.assertEqual(known_data.long_passes_successful, scraped_data.long_passes_successful,
                         'Long successful: known=%i scraped=%i' % (known_data.long_passes_successful,
                                                                   scraped_data.long_passes_successful))
        self.assertEqual(known_data.long_passes_failed, scraped_data.long_passes_failed,
                         'Long failed: known=%i scraped=%i' % (known_data.long_passes_failed,
                                                               scraped_data.long_passes_failed))
        self.assertEqual(known_data.short_passes_successful, scraped_data.short_passes_successful,
                         'Short successful: known=%i scraped=%i' % (known_data.short_passes_successful,
                                                                    scraped_data.short_passes_successful))
        self.assertEqual(known_data.short_passes_failed, scraped_data.short_passes_failed,
                         'Short failed: known=%i scraped=%i' % (known_data.short_passes_failed,
                                                                scraped_data.short_passes_failed))
        self.assertEqual(known_data.chances_created_open_play, scraped_data.chances_created_open_play,
                         'Chances created: known=%i scraped=%i' % (known_data.chances_created_open_play,
                                                                   scraped_data.chances_created_open_play))

    def _test_shot_data(self, known_shots, scraped_data):
        """ Compare our "known" shot data with the scraped data """

        self.assertEqual(known_shots[ShotTestData.GOALS], scraped_data.number_of_goals_scored(),
                         'Goals: known=%i scraped=%i' % (known_shots[ShotTestData.GOALS],
                                                         scraped_data.number_of_goals_scored()))
        self.assertEqual(known_shots[ShotTestData.SAVED], scraped_data.shots_saved(),
                         'Saved: known=%i scraped=%i' % (known_shots[ShotTestData.SAVED],
                                                         scraped_data.shots_saved()))
        self.assertEqual(known_shots[ShotTestData.ON_TARGET], scraped_data.shots_on_target(),
                         'On target: known=%i scraped=%i' % (known_shots[ShotTestData.ON_TARGET],
                                                             scraped_data.shots_on_target()))
        self.assertEqual(known_shots[ShotTestData.BLOCKED], scraped_data.shots_blocked(),
                         'Blocked: known=%i scraped=%i' % (known_shots[ShotTestData.BLOCKED],
                                                           scraped_data.shots_blocked()))
        self.assertEqual(known_shots[ShotTestData.OFF_TARGET], scraped_data.shots_off_target(),
                         'Off target: known=%i scraped=%i' % (known_shots[ShotTestData.OFF_TARGET],
                                                              scraped_data.shots_off_target()))
        self.assertEqual(known_shots[ShotTestData.LEFT], scraped_data.shots_from_left_of_goal(),
                         'From left: known=%i scraped=%i' % (known_shots[ShotTestData.LEFT],
                                                             scraped_data.shots_from_left_of_goal()))
        self.assertEqual(known_shots[ShotTestData.CENTRE], scraped_data.shots_from_centre_of_goal(),
                         'From centre: known=%i scraped=%i' % (known_shots[ShotTestData.CENTRE],
                                                               scraped_data.shots_from_centre_of_goal()))
        self.assertEqual(known_shots[ShotTestData.RIGHT], scraped_data.shots_from_right_of_goal(),
                         'From right: known=%i scraped=%i' % (known_shots[ShotTestData.RIGHT],
                                                              scraped_data.shots_from_right_of_goal()))
        self.assertEqual(known_shots[ShotTestData.OUTSIDE_EIGHTEEN], scraped_data.shots_outside_eighteen_yard_box(),
                         'Outside 18: known=%i scraped=%i' % (known_shots[ShotTestData.OUTSIDE_EIGHTEEN],
                                                              scraped_data.shots_outside_eighteen_yard_box()))
        self.assertEqual(known_shots[ShotTestData.INSIDE_EIGHTEEN], scraped_data.shots_inside_eighteen_yard_box(),
                         'Inside 18: known=%i scraped=%i' % (known_shots[ShotTestData.INSIDE_EIGHTEEN],
                                                             scraped_data.shots_inside_eighteen_yard_box()))
        self.assertEqual(known_shots[ShotTestData.INSIDE_SIX], scraped_data.shots_inside_six_yard_box(),
                         'Inside 6: known=%i scraped=%i' % (known_shots[ShotTestData.INSIDE_SIX],
                                                            scraped_data.shots_inside_six_yard_box()))

    def _test_set_piece_shot_data(self, known_shots, scraped_data):
        self.assertEqual(known_shots[SetPieceTestData.FREE_KICK_GOALS], scraped_data.free_kick_goals(),
                         'FK goals: known=%i scraped=%i' % (known_shots[SetPieceTestData.FREE_KICK_GOALS],
                                                            scraped_data.free_kick_goals()))
        self.assertEqual(known_shots[SetPieceTestData.FREE_KICKS_ON_TARGET], scraped_data.free_kicks_on_target(),
                         'FK on target: known=%i scraped=%i' % (known_shots[SetPieceTestData.FREE_KICKS_ON_TARGET],
                                                                scraped_data.free_kicks_on_target()))
        self.assertEqual(known_shots[SetPieceTestData.FREE_KICK_ATTEMPTS], scraped_data.total_free_kick_attempts(),
                         'FK attempts: known=%i scraped=%i' % (known_shots[SetPieceTestData.FREE_KICK_ATTEMPTS],
                                                               scraped_data.total_free_kick_attempts()))
        self.assertEqual(known_shots[SetPieceTestData.PENALTY_GOALS], scraped_data.penalty_goals(),
                         'Penalty goals: known=%i scraped=%i' % (known_shots[SetPieceTestData.PENALTY_GOALS],
                                                                 scraped_data.penalty_goals()))
        self.assertEqual(known_shots[SetPieceTestData.PENALTY_MISSES], scraped_data.penalties_missed(),
                         'Penalties missed: known=%i scraped=%i' % (known_shots[SetPieceTestData.PENALTY_MISSES],
                                                                    scraped_data.penalties_missed()))
        self.assertEqual(known_shots[SetPieceTestData.PENALTY_ATTEMPTS], scraped_data.total_penalty_attempts(),
                         'Penalty attempts: known=%i scraped=%i' % (known_shots[SetPieceTestData.PENALTY_ATTEMPTS],
                                                                    scraped_data.total_penalty_attempts()))

    def test_everton_v_qpr(self):
        """  Everton 3 - 1 QPR 2014/2015 """

        print "*** Testing --> Everton 3-1 QPR"
        test_url = "http://www.fourfourtwo.com/statszone/8-2014/matches/755457"
        match_scraper = MatchScraper()
        match_data = match_scraper.scrape_team_data(None, None, test_url)
        print "\tTesting --> done scraping match data"

        # Create a Everton team data with the known values
        home_team_data = TeamMatchData("Everton", HostingStatus.HOME)
        # set known summary stats
        home_team_data.possession_pct = 53.5
        home_team_data.fouls = 11
        home_team_data.goals = 3
        # set known attack values
        home_team_data.crosses_successful = 3
        home_team_data.crosses_failed = 4
        home_team_data.take_ons_successful = 14
        home_team_data.take_ons_failed = 15
        home_team_data.corners_successful = 1
        home_team_data.corners_failed = 0
        # set known defence values
        home_team_data.tackles_successful = 31
        home_team_data.tackles_failed = 12
        home_team_data.blocks = 4
        home_team_data.interceptions = 8
        # passes
        home_team_data.attacking_third_passes_successful = 66
        home_team_data.attacking_third_passes_failed = 37
        home_team_data.middle_third_passes_successful = 206
        home_team_data.middle_third_passes_failed = 45
        home_team_data.defensive_third_passes_successful = 98
        home_team_data.defensive_third_passes_failed = 2
        home_team_data.forward_passes_successful = 179
        home_team_data.forward_passes_failed = 250 - 179
        home_team_data.square_passes_successful = 50
        home_team_data.square_passes_failed = 10
        home_team_data.backward_passes_successful = 141
        home_team_data.backward_passes_failed = 3
        home_team_data.long_passes_successful = 21
        home_team_data.long_passes_failed = 28
        home_team_data.short_passes_successful = 349
        home_team_data.short_passes_failed = 405 - 349
        home_team_data.chances_created_open_play = 10

        # Create a QPR team with known values
        away_team_data = TeamMatchData("QueensParkRangers", HostingStatus.AWAY)
        # set known summary stats
        away_team_data.possession_pct = 46.5
        away_team_data.fouls = 12
        away_team_data.goals = 1
        # set known attack values
        away_team_data.crosses_successful = 2
        away_team_data.crosses_failed = 19
        away_team_data.take_ons_successful = 12
        away_team_data.take_ons_failed = 20
        away_team_data.corners_successful = 4
        away_team_data.corners_failed = 4
        # set known defence values
        away_team_data.tackles_successful = 21
        away_team_data.tackles_failed = 14
        away_team_data.blocks = 4
        away_team_data.interceptions = 7
        # passes
        away_team_data.attacking_third_passes_successful = 71
        away_team_data.attacking_third_passes_failed = 31
        away_team_data.middle_third_passes_successful = 171
        away_team_data.middle_third_passes_failed = 207 - 171
        away_team_data.defensive_third_passes_successful = 64
        away_team_data.defensive_third_passes_failed = 7
        away_team_data.forward_passes_successful = 144
        away_team_data.forward_passes_failed = 202 - 144
        away_team_data.square_passes_successful = 56
        away_team_data.square_passes_failed = 12
        away_team_data.backward_passes_successful = 106
        away_team_data.backward_passes_failed = 4
        away_team_data.long_passes_successful = 14
        away_team_data.long_passes_failed = 25
        away_team_data.short_passes_successful = 292
        away_team_data.short_passes_failed = 341 - 292
        away_team_data.chances_created_open_play = 10

        print "\tTesting --> about to run tests on Everton data"
        self._test_team_data(home_team_data, match_data.home_team_data)
        print "\tTesting --> about to run tests on QPR data"
        self._test_team_data(away_team_data, match_data.away_team_data)

        # Everton shots
        home_goals = 2
        home_shots_on_target = 5
        home_shots_blocked = 4
        home_shots_saved = 3
        home_shots_off_target = 4
        home_shots_from_left = 6
        home_shots_from_centre = 1
        home_shots_from_right = 6
        home_shots_outside_eighteen = 10  # one is right on the cusp
        home_shots_inside_eighteen = 3  # one is right on the cusp
        home_shots_inside_six = 1

        home_shot_data = (
            home_goals,
            home_shots_saved,
            home_shots_on_target,
            home_shots_blocked,
            home_shots_off_target,
            home_shots_from_left,
            home_shots_from_centre,
            home_shots_from_right,
            home_shots_outside_eighteen,
            home_shots_inside_eighteen,
            home_shots_inside_six,
        )

        # Everton free kicks
        home_free_kick_goals = 1
        home_free_kicks_on_target = 1
        home_free_kick_attempts = 2

        # Everton penalties
        home_penalty_goals = 0
        home_penalty_misses = 0
        home_penalty_attempts = 0

        home_set_piece_shot_data = (
            home_penalty_goals,
            home_penalty_misses,
            home_penalty_attempts,
            home_free_kick_goals,
            home_free_kicks_on_target,
            home_free_kick_attempts
        )

        # qpr shots
        away_goals = 1
        away_shots_on_target = 4
        away_shots_blocked = 4
        away_shots_saved = 3
        away_shots_off_target = 9
        away_shots_from_left = 9
        away_shots_from_centre = 6
        away_shots_from_right = 2
        away_shots_outside_eighteen = 12
        away_shots_inside_eighteen = 5
        away_shots_inside_six = 1

        away_shot_data = (
            away_goals,
            away_shots_saved,
            away_shots_on_target,
            away_shots_blocked,
            away_shots_off_target,
            away_shots_from_left,
            away_shots_from_centre,
            away_shots_from_right,
            away_shots_outside_eighteen,
            away_shots_inside_eighteen,
            away_shots_inside_six,
        )

        # qpr free kicks
        away_free_kick_goals = 0
        away_free_kicks_on_target = 0
        away_free_kick_attempts = 0

        # qpr penalties
        away_penalty_goals = 0
        away_penalty_misses = 0
        away_penalty_attempts = 0

        away_set_piece_shot_data = (
            away_penalty_goals,
            away_penalty_misses,
            away_penalty_attempts,
            away_free_kick_goals,
            away_free_kicks_on_target,
            away_free_kick_attempts
        )

        print "\tTesting --> about to run tests on Everton shots"
        self._test_shot_data(home_shot_data, match_data.home_team_data)
        print "\tTesting --> about to run test on Everton set-piece shots"
        self._test_set_piece_shot_data(home_set_piece_shot_data, match_data.home_team_data)
        print "\tTesting --> about to run tests on qpr shots"
        self._test_shot_data(away_shot_data, match_data.away_team_data)
        print "\tTesting --> about to run tests on qpr set-piece shots"
        self._test_set_piece_shot_data(away_set_piece_shot_data, match_data.away_team_data)

        print "Done testing this match."

    def test_liverpool_v_sunderland(self):
        """ Liverpool 0 - 0 Sunderland 2014/2015"""

        print "*** Testing --> Liverpool 0-0 Sunderland"
        test_url = "http://www.fourfourtwo.com/statszone/8-2014/matches/755445"
        match_scraper = MatchScraper()
        match_data = match_scraper.scrape_team_data(None, None, test_url)
        print "\tTesting --> done scraping match data"

        # Create a Liverpool team data with the known values
        home_team_data = TeamMatchData("Liverpool", HostingStatus.HOME)
        # set known summary stats
        home_team_data.possession_pct = 53.4
        home_team_data.fouls = 12
        home_team_data.goals = 0
        # set known attack values
        home_team_data.crosses_successful = 4
        home_team_data.crosses_failed = 25
        home_team_data.take_ons_successful = 17
        home_team_data.take_ons_failed = 14
        home_team_data.corners_successful = 2
        home_team_data.corners_failed = 3
        # set known defence values
        home_team_data.tackles_successful = 24
        home_team_data.tackles_failed = 6
        home_team_data.blocks = 2
        home_team_data.interceptions = 20
        # passes
        home_team_data.attacking_third_passes_successful = 151
        home_team_data.attacking_third_passes_failed = 196 - 151
        home_team_data.middle_third_passes_successful = 166
        home_team_data.middle_third_passes_failed = 197 - 166
        home_team_data.defensive_third_passes_successful = 54
        home_team_data.defensive_third_passes_failed = 2
        home_team_data.forward_passes_successful = 192
        home_team_data.forward_passes_failed = 253 - 192
        home_team_data.square_passes_successful = 86
        home_team_data.square_passes_failed = 10
        home_team_data.backward_passes_successful = 93
        home_team_data.backward_passes_failed = 7
        home_team_data.long_passes_successful = 12
        home_team_data.long_passes_failed = 9
        home_team_data.short_passes_successful = 359
        home_team_data.short_passes_failed = 428 - 359
        home_team_data.chances_created_open_play = 13

        # Create a Palace team with known values
        away_team_data = TeamMatchData("Sunderland", HostingStatus.AWAY)
        # set known summary stats
        away_team_data.possession_pct = 46.6
        away_team_data.fouls = 15
        away_team_data.goals = 0
        # set known attack values
        away_team_data.crosses_successful = 1
        away_team_data.crosses_failed = 14
        away_team_data.take_ons_successful = 6
        away_team_data.take_ons_failed = 9
        away_team_data.corners_successful = 4
        away_team_data.corners_failed = 3
        # set known defence values
        away_team_data.tackles_successful = 18
        away_team_data.tackles_failed = 17
        away_team_data.blocks = 7
        away_team_data.interceptions = 22
        # passes
        away_team_data.attacking_third_passes_successful = 82
        away_team_data.attacking_third_passes_failed = 119 - 82
        away_team_data.middle_third_passes_successful = 167
        away_team_data.middle_third_passes_failed = 212 - 167
        away_team_data.defensive_third_passes_successful = 66
        away_team_data.defensive_third_passes_failed = 5
        away_team_data.forward_passes_successful = 155
        away_team_data.forward_passes_failed = 226 - 155
        away_team_data.square_passes_successful = 50
        away_team_data.square_passes_failed = 12
        away_team_data.backward_passes_successful = 110
        away_team_data.backward_passes_failed = 4
        away_team_data.long_passes_successful = 22
        away_team_data.long_passes_failed = 24
        away_team_data.short_passes_successful = 293
        away_team_data.short_passes_failed = 356 - 293
        away_team_data.chances_created_open_play = 2

        print "\tTesting --> about to run tests on Liverpool data"
        self._test_team_data(home_team_data, match_data.home_team_data)
        print "\tTesting --> about to run tests on Sunderland data"
        self._test_team_data(away_team_data, match_data.away_team_data)

        # Liverpool shots
        home_goals = 0
        home_shots_on_target = 2
        home_shots_blocked = 7  # I only actually see 6, but it looks like one was blocked very far out
        home_shots_saved = 2
        home_shots_off_target = 6
        home_shots_from_left = 6
        home_shots_from_centre = 2
        home_shots_from_right = 7  # I only actually see 6, but one was from very far out (blocked)
        home_shots_outside_eighteen = 9  # Again, only see 8
        home_shots_inside_eighteen = 6
        home_shots_inside_six = 0

        home_shot_data = (
            home_goals,
            home_shots_saved,
            home_shots_on_target,
            home_shots_blocked,
            home_shots_off_target,
            home_shots_from_left,
            home_shots_from_centre,
            home_shots_from_right,
            home_shots_outside_eighteen,
            home_shots_inside_eighteen,
            home_shots_inside_six,
        )

        # Liverpool free kicks
        home_free_kick_goals = 0
        home_free_kicks_on_target = 0
        home_free_kick_attempts = 1

        # Liverpool penalties
        home_penalty_goals = 0
        home_penalty_misses = 0
        home_penalty_attempts = 0

        home_set_piece_shot_data = (
            home_penalty_goals,
            home_penalty_misses,
            home_penalty_attempts,
            home_free_kick_goals,
            home_free_kicks_on_target,
            home_free_kick_attempts
        )

        # Sunderland shots
        away_goals = 0
        away_shots_on_target = 1
        away_shots_blocked = 2
        away_shots_saved = 1
        away_shots_off_target = 4
        away_shots_from_left = 4
        away_shots_from_centre = 3
        away_shots_from_right = 0
        away_shots_outside_eighteen = 4
        away_shots_inside_eighteen = 3
        away_shots_inside_six = 0

        away_shot_data = (
            away_goals,
            away_shots_saved,
            away_shots_on_target,
            away_shots_blocked,
            away_shots_off_target,
            away_shots_from_left,
            away_shots_from_centre,
            away_shots_from_right,
            away_shots_outside_eighteen,
            away_shots_inside_eighteen,
            away_shots_inside_six,
        )

        # Sunderland free kicks
        away_free_kick_goals = 0
        away_free_kicks_on_target = 0
        away_free_kick_attempts = 0

        # Sunderland penalties
        away_penalty_goals = 0
        away_penalty_misses = 0
        away_penalty_attempts = 0

        away_set_piece_shot_data = (
            away_penalty_goals,
            away_penalty_misses,
            away_penalty_attempts,
            away_free_kick_goals,
            away_free_kicks_on_target,
            away_free_kick_attempts
        )

        print "\tTesting --> about to run tests on Liverpool shots"
        self._test_shot_data(home_shot_data, match_data.home_team_data)
        print "\tTesting --> about to run test on Liverpool set-piece shots"
        self._test_set_piece_shot_data(home_set_piece_shot_data, match_data.home_team_data)
        print "\tTesting --> about to run tests on Sunderland shots"
        self._test_shot_data(away_shot_data, match_data.away_team_data)
        print "\tTesting --> about to run tests on Sunderland set-piece shots"
        self._test_set_piece_shot_data(away_set_piece_shot_data, match_data.away_team_data)

        print "Done testing this match."


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestTeamData))
    unittest.TextTestRunner().run(suite)