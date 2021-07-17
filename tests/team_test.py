import unittest
from models.team import Team

class TestTeam(unittest.TestCase):

    def setUp(self):
        self.team = Team("Rangers", 38, 102, 92, 13)

    def test_team_has_name(self):
        self.assertEqual("Rangers", self.team.name)
    
    def test_team_has_name(self):
        self.assertEqual("Rangers", self.team.name

    