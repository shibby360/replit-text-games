import teams
bull = teams.Guy('Bull', 'Transform into a bull', 110, 100, 'Offense')
ram = teams.Guy('Ram', 'Transform into a ram', 100, 100, 'Offense')
powerup = teams.Guy('Power Up', 'Transform into an energy ball which increases damage by 10%', 10, 100, 'Support')
medkit = teams.Guy('Medkit', 'Transform into a medical kit', 40, 100, 'Medic')
cloak = teams.Guy('Cloak', 'Transform into an invisicloak', 10, 100, 'Support')
master = teams.Master(bull, ram, medkit, powerup, cloak)