from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.team import Team
import repositories.team_repository as team_repository

team_blueprint = Blueprint("teams", __name__)

@team_blueprint.route("/teams")
def teams():
    teams = team_repository.select_all()
    
    return render_template("teams/index.html", teams=teams)

@team_blueprint.route("/teams/<id>")
def show(id):
    team = team_repository.select(id)
    points_per_game = team.calculate_points_per_game()
    goals_per_game = team.calculate_goals_per_game()
    goals_v_per_game = team.calculate_goals_against_per_game()
    percentage_won = team.calculate_percentage_games_won()
    


    return render_template("teams/show.html", percentage_won=percentage_won, team=team, points_per_game=points_per_game, goals_per_game=goals_per_game, goals_v_per_game=goals_v_per_game)