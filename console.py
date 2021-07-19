import pdb

from models.team import Team

import repositories.team_repository as team_repository

rangers = Team("Rangers", 38, 32, 102, 92, 13)
team_repository.save(rangers)

celtic = Team("Celtic", 38, 22, 77, 78, 29)
team_repository.save(celtic)

hibs = Team("Hibernian", 38, 18, 63, 48, 35)
team_repository.save(hibs)

aberdeen = Team("Aberdeen", 38, 15, 56, 36, 38)
team_repository.save(aberdeen)

st_johnstone = Team("St. Johnstone", 38, 11, 45, 36, 46)
team_repository.save(st_johnstone)

livingston = Team("Livingston", 38, 12, 45, 42, 54)
team_repository.save(livingston)

st_mirren = Team("St. Mirren", 38, 11, 45, 37, 45)
team_repository.save(st_mirren)

motherwell = Team("Motherwell", 38, 12, 45, 39, 55)
team_repository.save(motherwell)

dundee_utd = Team("Dundee United", 38, 10, 44, 32, 50)
team_repository.save(dundee_utd)

ross_county = Team("Ross County", 38, 11, 39, 35, 66)
team_repository.save(ross_county)

killie = Team("Kilmarnock", 38, 10, 36, 43, 54)
team_repository.save(killie)

hamilton = Team("Hamilton Academical", 38, 7, 30, 34, 67)
team_repository.save(hamilton)

pdb.set_trace()