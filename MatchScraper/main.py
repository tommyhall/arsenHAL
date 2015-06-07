__author__ = 'tom'

# This is the program entry point
# Creates a list of matches to scrape, sends to the match scraper

# TODO: your current method of getting # goals does not account for own-goals
# TODO: scrape and store player data

import os
from MatchScraper import MatchScraper


def get_matchday_dict(data_directory):
    """ Creates a dictionary of season -> matchday_list """
    matchday_dict = {}
    for root, dirs, files in os.walk(os.path.join(os.getcwd(), data_directory)):
        for season in dirs:
            matchdays_list = [match for match in os.listdir(os.path.abspath(os.path.join(os.getcwd(), data_directory, season)))]
            matchday_dict[season] = matchdays_list
    return matchday_dict


def get_matches_list(matchday_path):
    """ Given the file path of a matchday, return the list of match URLs """
    with open(matchday_path, 'r') as matchday_file:
        matches = matchday_file.read().splitlines()
    matchday_file.close()
    return matches


def scrape_data():
    """ Scrapes all match data """

    match_scraper = MatchScraper()
    data_directory = '_match_report_data'
    matchday_dict = get_matchday_dict(data_directory)

    for season, matchdays in matchday_dict.iteritems():
        print "SEASON:", season

        for matchday in matchdays:
            print "MATCHDAY:", matchday
            matchday_path = os.path.join(os.getcwd(), data_directory, season, matchday)
            matches_list = get_matches_list(matchday_path)

            for match_url in matches_list:
                match_scraper.scrape_team_data(match_url)


scrape_data()