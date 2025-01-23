import teams
fire = teams.Guy('Fire', 'Create fire from hand', 40, 100, 'Offense')
burn = teams.Guy('Burn', 'Burn anything he wants by touching it(Helps teammates)', 35, 100, 'Medic')
heat = teams.Guy('Heat', 'Constantly burning hot(Normal body temperature: 140 F)', 45, 100, 'Offense')
lava = teams.Guy('Lava', 'Made from rock; can turn into lava whenever wanted', 60, 100, 'Offense')
ember = teams.Guy('Ember', 'Can upgrade anyone\'s attacks by 30 damage', 30, 100, 'Support')
master = teams.Master(fire, burn, heat, lava, ember)