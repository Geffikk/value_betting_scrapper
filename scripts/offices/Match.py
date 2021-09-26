class Match:
    def __init__(self):
        self.match = {}
        self.home = {}
        self.away = {}
        self.draw = {}
        self.derived_bets = {}

        self.match["sport"] = ""
        self.match["home"] = self.home
        self.match["away"] = self.away
        self.match["draw"] = self.draw
        self.match["derived_bets"] = self.derived_bets
