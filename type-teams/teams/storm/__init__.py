import teams
cloud = teams.Guy('Cloud', 'Create clouds whenever wanted', 0, 125, 'Support')
lightning = teams.Guy('Lightning', 'Shoot lightning from fingertips', 90, 125, 'Offense')
thunder = teams.Guy('Thunder', 'Create thunder', 20, 125, 'Support')
rain = teams.Guy('Rain', 'Pour rain on enemy(When on teammate, teammate heals', 40, 125, 'Medic')
wind = teams.Guy('Wind', 'Blow wind on anyone', 30, 125, 'Offense')
master = teams.Master(cloud, lightning, thunder, rain, wind)