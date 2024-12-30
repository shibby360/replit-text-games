import random as r
class miner:
  health = 10
  damage = 2
  accuracy = 4
  name = 'Miner'
  canstick = False
  cansting = False
  class crit:
    damage = 3
    chance = 3
class snowman:
  health = 10
  damage = 3
  accuracy = 3
  name = 'Snowman'
  canstick = True
  sticktime = 2
  cansting = False
  class crit:
    damage = 4
    chance = 3
class goblin:
  health = 9
  damage = 1
  accuracy = 2.5
  name = 'Goblin'
  canstick = False
  cansting = True
  stingtime = 2
  stingdmg = 1
  class crit:
    damage = 2
    chance = 2
def grabenemy():
  enemies = {
    'miner':miner,
    'snowman':snowman,
    'goblin':goblin
  }
  return enemies[r.choice(list(enemies.keys()))]