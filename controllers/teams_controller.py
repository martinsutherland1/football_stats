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
    win_percentage = team.calculaate_win_percentage()

    return render_template("teams/show.html", win_percentage=win_percentage, team=team, points_per_game=points_per_game, goals_per_game=goals_per_game, goals_v_per_game=goals_v_per_game)

@team_blueprint.route("/teams/new_team", methods=['GET'])
def new():
    teams = team_repository.select_all()
   
    return render_template("teams/new.html", teams=teams)

@team_blueprint.route("/teams", methods=['POST'])
def create():
    name = request.form["name"]
    matches = request.form["matches"]
    won = request.form["won"]
    points = request.form["points"]
    goals_for = request.form["goals_for"]
    goals_against = request.form["goals_against"]
    team = Team(name, matches, won, points, goals_for, goals_against)
    team_repository.save(team)
    return redirect("/teams")

@team_blueprint.route("/teams/<id>/delete", methods=["post"])
def delete(id):
    team = team_repository.delete(id)
    return redirect("/teams")

@team_blueprint.route("/teams/<id>/edit")
def edit(id):
    team = team_repository.select(id)
    return render_template("teams/edit.html", team=team)

@team_blueprint.route("/teams/<id>", methods=['POST'])
def update(id):
    name = request.form["name"]
    matches = request.form["matches"]
    won = request.form["won"]
    points = request.form["points"]
    goals_for = request.form["goals_for"]
    goals_against = request.form["goals_against"]
    
    team = Team(name, matches, won, points, goals_for, goals_against, id)
    team_repository.update(team)
    return redirect(f"/teams")