class knight:
  name = 'Knight'
  weapon = 'badpistol'
  energy = 200
  health = 7
  l1cosm = '\033[38;2;113;121;126m'
  l2cosm = '🪖  '
  canstick = False
  cansting = False
  meleebuff = False
  class skill:
    cd = 3
    dur = 5
    canstick = False
    cansting = False
    def skill(weapon, pl):
      print('DUAL WIELD')
      return {'damage':0, 'energyused':0}
    def skilling(weapon, pl):
      energyused = weapon.energy * 2
      if pl >= 10:
        energyused -= 10
      return {'damage':(weapon.damage + pl) * 2, 'energyused':energyused}
class rogue:
  name = 'Rogue'
  weapon = 'blade'
  energy = 180
  health = 5
  cost = 25
  l1cosm = '\033[38;2;173;216;230m'
  l2cosm = '🗡️  '
  canstick = False
  cansting = False
  meleebuff = False
  class skill:
    cd = 4
    def skill(weapon, pl):
      print('DAMAGE BURST')
      return {'damage':weapon.damage*(3 + pl), 'energyused':weapon.energy*(3 + pl)}
class bodybuilder:
  name = 'Body Builder'
  weapon = 'brassknuckles'
  energy = 100
  health = 8
  cost = 100
  l1cosm = '\033[38;2;255;203;164m'
  l2cosm = '💪 '
  canstick = False
  cansting = False
  meleebuff = False
  class skill:
    cd = 5
    def skill(weapon, pl):
      print('KABOOSH')
      return {'damage':3*pl, 'energyused':4*pl}
class witch:
  name = 'Witch'
  weapon = 'woodstaff'
  energy = 200
  health = 5
  cost = 150
  l1cosm = '\033[38;2;255;0;255m'
  l2cosm = '🪄  '
  canstick = False
  cansting = True
  stingtime = 3
  stingdamage = 2
  meleebuff = False
  class skill:
    cd = 5
    def skill(weapon, pl):
      print('ENEMY SHOCKED')
      return {'damage':2*pl, 'energyused':pl*2}
class assassin:
  name = 'Assassin'
  weapon = 'bloodsword'
  energy = 100
  health = 5
  cost = 50
  l1cosm = '\033[38;2;255;0;0m'
  l2cosm = '⚔️  '
  canstick = False
  cansting = False
  meleebuff = True
  class skill:
    cd = 3
    def skill(weapon, pl):
      damage = 0
      if weapon.barehandable:
        damage = weapon.crit.damage+pl
        print(f'{weapon.name.upper()} SLASH')
      else:
        damage = pl+3
        print('BAREHAND SLASH')
      return {'damage':damage, 'energyused':0}
heros = {
  'knight':knight,
  'rogue':rogue,
  'bodybuilder':bodybuilder,
  'witch':witch,
  'assassin':assassin
}
def getcosm(hero, pl):
  cosm = ''
  if type(hero) == str:
    hero = heros[hero]
  if pl >= 11:
    cosm += hero.l1cosm
  if pl >= 12:
    cosm += hero.l2cosm
  return cosm