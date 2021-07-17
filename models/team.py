class Team:
    def __init__(self, name, matches, points, goals_for, goals_against, id = None):
        self.name = name
        self.matches = matches
        self.points = points
        self.goals_for = goals_for
        self.goals_against = goals_against
        self.id = id

    

    def calculate_points_per_game(self):
        total = self.points / self.matches
        return round(total, 3)
        
    
    def calculate_goals_per_game(self):
        total = self.goals_for / self.matches
        return round(total, 3)
    
    def calculate_goals_against_per_game(self):
        total = self.goals_against / self.matches
        return round(total, 3)
    
    def calculate_percentage_games_won(self):
        return self.points % self.matches