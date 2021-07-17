import pdb

from models.team import Team

import repositories.team_repository as team_repository

rangers = Team("Hibernian", 38, 102, 92, 13)
team_repository.save(rangers)

pdb.set_trace()