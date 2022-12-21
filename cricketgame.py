class Player:
    def __init__(self, name, runs=0, balls_faced=0, wickets=0):
        self.name = name
        self.runs = runs
        self.balls_faced = balls_faced
        self.wickets = wickets

    def get_batting_average(self):
        if self.balls_faced > 0:
            return self.runs / self.balls_faced
        return 0

class Team:
    def __init__(self, name, players):
        self.name = name
        self.players = players
        self.score = 0
        self.wickets = 0

    def get_team_score(self):
        return self.score

    def get_team_wickets(self):
        return self.wickets

    def get_team_average(self):
        total_balls_faced = 0
        total_runs = 0
        for player in self.players:
            total_balls_faced += player.balls_faced
            total_runs += player.runs
        if total_balls_faced > 0:
            return total_runs / total_balls_faced
        return 0

class CricketGame:
    def __init__(self, team1, team2, overs):
        self.team1 = team1
        self.team2 = team2
        self.overs = overs
        self.current_inning = 1
        self.current_over = 0
        self.current_team = team1
        self.current_striker = self.current_team.players[0]
        self.non_striker = self.current_team.players[1]
        self.bowler = self.team2.players[0]

    def play_ball(self):
        runs_scored = 0
        # simulate the ball being bowled and runs being scored
        self.current_team.score += runs_scored
        self.current_striker.runs += runs_scored
        self.current_striker.balls_faced += 1
        if runs_scored % 2 == 1:
            # switch strike if runs scored is odd
            self.current_striker, self.non_striker = self.non_striker, self.current_striker
        if runs_scored == 4 or runs_scored == 6:
            # switch strike if runs scored is 4 or 6
            self.current_striker, self.non_striker = self.non_striker, self.current_striker
        self.current_over += 1
        if self.current_over > self.overs:
            # end of over, switch teams
            self.current_inning += 1
            self.current_over = 0
            if self.current_inning > 2:
                # end of game
                return
            self.current_team = self.team2
            self.bowler = self.team1.players[0]
            self.current_striker = self.current_team.players[0]
            self.non_striker = self.current_team.players[1]

# create the players
player1 = Player("player 1")
player2 = Player("player 2")
player3 = Player("player 3")
