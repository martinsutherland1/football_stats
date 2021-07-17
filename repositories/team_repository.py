from db.run_sql import run_sql

from models.team import Team



def save(team):
    sql = "INSERT INTO teams (name, matches, points, goals_for, goals_against) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [team.name, team.matches, team.points, team.goals_for, team.goals_against]
    results = run_sql(sql, values)
    team.id = results[0]['id']
    return team


def select_all():
    teams = []

    sql = "SELECT * FROM teams"
    results = run_sql(sql)
    for row in results:
        team = Team(row["name"], row["matches"], row["points"],row["goals_for"], row["goals_against"], row["id"])
        teams.append(team)
    return teams


def select(id):
    team = None
    sql = "SELECT * FROM teams WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        team = Team(result["name"], result["matches"], result["points"], result["goals_for"], result["goals_against"], result["id"])
    return team


def delete_all():
    sql = "DELETE FROM teams"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM teams WHERE id = %s"
    values = [id]
    run_sql(sql, values)


# def get_by_class(gym_class):
#     sql = "SELECT members.* FROM members INNER JOIN sessions ON members.id = sessions.member_id WHERE sessions.gym_class_id = %s"
#     values = [gym_class.id]
#     results = run_sql(sql, values)

#     members = []

#     for row in results:
#         member = Member(row['name'], row['age'], row['membership_id'], row['id'])
#         members.append(member)

#     return members


def update(team):
    sql = "UPDATE teams SET (name, matches, points, goals_for, goals_against) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [team.name, team.matches, team.points, team.goals_for, team.goals_against]
    results = run_sql(sql, values)