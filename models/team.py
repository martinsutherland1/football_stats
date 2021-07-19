class Team:
    def __init__(self, name, matches, won, points, goals_for, goals_against, id = None):
        self.name = name
        self.matches = matches
        self.won = won
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

    def calculaate_win_percentage(self):
        total =  (self.won / self.matches) * 100
        return round(total)

    

    
    