import json
import re
import time
import sys

from bs4 import BeautifulSoup

from scripts.offices.BettingOffice import BettingOffice
from scripts.offices.Match import Match

live_score_url = "https://www.pinnacle.com/cs/"


class Pinnacle(BettingOffice):

    def __init__(self):
        super().__init__(live_score_url)

    def parse_matches(self):
        print("test")

