r = __import__('random')
__import__('os').system('clear')
class Move():
  def __init__(self, name, num, type):
    self.name = name
    self.type = type
    if type == 'attack':
      self.damage = num
      self.defense = 0
    if type == 'defense':
      self.defense = num
      self.damage = 0

class Hero():
  def __init__(self, name, health, moves):
    self.name = name
    self.health = health
    self.moves = moves
    self.defense = 0
    self.guarded = False
    self.guard = None
  def atk(self, enemy, move=None):
    if self.guarded:
      self.guard.atk(player=self, enemy=enemy, move=guardmove)
      return
    if move == None:
      move = r.choice(self.moves)
    if move not in self.moves:
      raise ValueError('Move used not usable.')
    if move.damage - enemy.defense <= 0:
      thedmg = 0
    else:
      thedmg = move.damage - enemy.defense
    print(self.name + ' attacked {} with {} and did {} damage.'.format(enemy.name, move.name, thedmg))
    self.defense += move.defense
    if thedmg != 0:
      if enemy.defense != 0:
        enemy.defense -= move.damage
        if enemy.defense <= 0:
          enemy.defense = 0
      else:
        enemy.health -= move.damage
  def isalive(self):
    return self.health > 0

class Guard():
  def __init__(self, health):
    self.health = health
  def atk(self, player, enemy, move):
    if move.damage - enemy.defense <= 0:
      thedmg = 0
    else:
      thedmg = move.damage - enemy.defense
    print(player.name + '\'s guard attacked {} with {} and did {} damage.'.format(enemy.name, move.name, thedmg))
    if thedmg != 0:
      if enemy.defense != 0:
        enemy.defense -= move.damage
        if enemy.defense <= 0:
          enemy.defense = 0
      else:
        enemy.health -= move.damage

akatk = Move('AKATK', 75, 'attack')
dfnser = Move('SHIELDE', 50, 'defense')
swrd = Move('SWORDD', 100, 'attack')
hmr = Move('HAMMMER OF DEATH', 200, 'attack')
wall = Move('WALLL', 250, 'defense')
guardmove = Move('Stab', 50, 'attack')
hro = Hero('hro', 150, [akatk, swrd, hmr, hmr, hmr])
enmy = Hero('enmy', 175, [dfnser, wall])
g1 = Guard(50)
g2 = Guard(100)
g3 = Guard(150)
brkr = False
while True:
  todo = input(
"""
[1]Attack
[2]Chill
[3]Get Guard
"""
  )
  if todo == '1':
    if hro.isalive():  hro.atk(enmy)
    else:
      print(hro.name + ' died.')
      brkr = True
  if todo == '3':
    grd = eval('g' + input('Number 1-3: '))
    hro.defense += grd.health
    hro.guard = grd
    hro.guarded = True
  if enmy.isalive():  enmy.atk(hro)
  else:
    print(enmy.name + ' died.')
    brkr = True
  if brkr:  break