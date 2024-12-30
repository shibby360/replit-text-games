import random as r
import time
import os
def prep():
  time.sleep(1)
  os.system('clear')
def Line(num):
  import os
  return open(os.path.basename(__file__)).readlines()[num-1].strip()
#Get class name: str(*CLASSNAME*)[17:-2].title()
#Weapon stats
class sword:
  type = 'attack'
  lvl = 1
  cost = 50
  def dmg():
    return sword.lvl * 50
  def dfns(): 
    return sword.lvl * 0
  def stmna_up(): 
    return sword.lvl * 0
  def energy_drain(): 
    return 25
class katana:
  type = 'attack'
  lvl = 1
  cost = 75
  def dmg():
    return katana.lvl * 100
  def dfns(): 
    return katana.lvl * 25
  def stmna_up():
    return katana.lvl * 0
  def energy_drain(): 
    return 75
class shield:
  type = 'defense'
  lvl = 1
  cost = 75
  def dmg():
    return shield.lvl * 0
  def dfns(): 
    return shield.lvl * 50
  def stmna_up(): 
    return shield.lvl * 0
  def energy_drain(): 
    return 25
class wall:
  type = 'defense'
  lvl = 1
  cost = 100
  def dmg():
    return wall.lvl * 25
  def dfns(): 
    return wall.lvl * 100
  def stmna_up(): 
    return wall.lvl * 0
  def energy_drain(): 
    return 75
class booster:
  type = 'stamina'
  lvl = 1
  cost = 100
  def dmg():
    return booster.lvl * 0
  def dfns(): 
    return booster.lvl * 0
  def stmna_up():
    return booster.lvl * 50
  def energy_drain(): 
    return 25
class ultra_speed:
  type = 'stamina'
  lvl = 1
  cost = 125
  def dmg():
    return ultra_speed.lvl * 25
  def dfns():
    return ultra_speed.lvl * 25
  def stmna_up():
    return ultra_speed.lvl * 100
  def energy_drain():
    return 75
class none:
  type = '?'
  lvl = 1
  cost = 0
  def dmg():
    return none.lvl * 0
  def dfns():
    return none.lvl * 0
  def stmna_up():
    return none.lvl * 0
  def energy_drain():
    return 0
weaps = [sword, katana, shield, wall, booster, ultra_speed]

#Player stats
class player:
  lvl = 1
  health = 300
  name = input('Name?: ')
  weapon = r.choice(weaps)
  stamna = 2
  energy = 100
  lives = 4
  def levelup():
    player.lvl += 1
    player.base.lvl += 1
    player.weapon.lvl += 1
    player.set()
    player.base.set()
  def set():
    player.stamna = player.lvl * 2
    player.energy = player.lvl * 100
    player.health = player.lvl * 300
  class base:
    lvl = 1
    armor = lvl * 200
    def gundmg():
      return player.base.lvl * 50
    def set():
      player.base.armor = player.lvl * 200

#Enemy's stats
'''Enemy Weapons'''
class gun:
  type = 'attack'
  def dmg():
    return 100
  def dfns():
    return 25
  def stmna_up():
    return 0
  def energy_drain():
    return 50
class whip:
  type = 'attack'
  def dmg():
    return 150
  def dfns():
    return 50
  def stmna_up():
    return 25
  def energy_drain():
    return 125
class file:
  type = 'defense'
  def dmg():
    return 150
  def dfns():
    return 150
  def stmna_up():
    return 50
  def energy_drain():
    return 250
'''Enemies'''
class _404:
  lvl = 25
  weapon = gun
  stamna = 2 * lvl
  energy = 100 * lvl
  health = 4 * lvl
  def set():
    _404.stamna = 2 * _404.lvl
    _404.energy = 100 * _404.lvl
    _404.health = 4 * _404.lvl
class virus:
  lvl = 25
  weapon = whip
  stamna = 3 * lvl
  energy = 150 * lvl
  health = 6 * lvl
  def set():
    virus.stamna = 3 * virus.lvl
    virus.energy = 150 * virus.lvl
    virus.health = 6 * virus.lvl
class bug:
  weapon = file
  stamna = 125
  energy = 6250
  health = 300
  def set():
    bug.stamna = 125
    bug.energy = 6250
    bug.health = 300
#Arenas
class arena1:
  name = 'Techno Town'
  enemy = _404
class arena2:
  name = 'Gamer Grounds'
  enemy = _404
class arena3:
  name = 'Computer County'
  enemy = virus
class arena4:
  name = 'Software State'
  enemy = virus
class arena5:
  name = 'Internet Island'
  enemy = bug
arena = arena1
arenanum = 1
wins = 0
arena_new_old = 'new'
coins = 0
while True:
  prep()
  if arenanum == 1:
    arena = arena1
  elif arenanum == 2:
    arena = arena2
  elif arenanum == 3:
    arena = arena3
  elif arenanum == 4:
    arena = arena4
  elif arenanum == 5:
    arena = arena5
  else:
    print('You completed the game!')
    f = open('People who completed the game.txt', 'a')
    f.write(player.name + ' completed the game')
    f.close()
    break
  print('You are in ' + arena.name)
  print('You are level', player.lvl)
  print('You are fighting ' + str(arena.enemy)[17:-2].title())
  print('Your weapon is: ' + str(player.weapon)[17:-2].title())
  print('You have', wins, 'wins.')
  print('You have', player.lives, 'lives.')
  print('You have', coins, 'coins.')
  print('You are at your base.')
  basechoice = input('What would you like to do?: \n[1]Come out of your base\n[2]Stay in your base\n[3]Change your weapon\n[4]Upgrade\n: ')
  if basechoice == '1':
    print('You are out of your base.')
    isenemy = r.choice([True, False])
    if isenemy:
      print('It is time to fight.')
      while (player.health > 0 and player.base.armor > 0) and arena.enemy.health > 0:
        print('Your health:', player.health)
        print('Enemy health:', arena.enemy.health)
        print('Your base health:', player.base.armor)
        print('Your weapon: ' + str(player.weapon)[17:-2].title())
        print('You are level', player.lvl)
        wheretofight = input('Do you want to attack...\n[1]With your base\n[2]Without your base\nOR\n[3]Summon the HTML(Heroic, Terrorizing, Magnificent Lancers)\n: ')
        if wheretofight == '1':
          print('You have attacked!')
          arena.enemy.health -= player.base.gundmg() - arena.enemy.weapon.dfns()
          print('The enemy has attacked!')
          player.base.armor -= arena.enemy.weapon.dmg() - player.weapon.dfns()
          player.base.armor += 20
        elif wheretofight == '2':
          runningman = input('Do you wish to run(y/n)?: ')
          if runningman == 'y':
            howlong = int(input('How long do you want to run?: '))
            if howlong > player.stamna:
              print('You cannot run that far.')
            else:
              if howlong >= 50:
                print('You have succesfully escaped the fight.')
                break
              else:
                print('You ran away.')
                continue
            prep()
          elif runningman == 'n':
            if player.weapon.energy_drain() > player.energy:
              print('Too much energy required.')
              weaponchangechoice = input('Would you like to change your weapon(y/n)?: ')
              if weaponchangechoice == 'y':
                woepan = eval(input('Which weapon?: ').lower())
                if coins > woepan.cost / 5:
                  player.weapon = woepan
                  coins -= woepan.cost / 5
                else:
                  print('You have too less coins.')
            else:
              if player.weapon.type == 'attack':
                spin = input('Would you like to do spinjitzu(y/n)?: ')
                if spin == 'y':
                  arena.enemy.health -= player.weapon.dmg() * 10
                else:
                  arena.enemy.health -= player.weapon.dmg() - arena.enemy.weapon.dfns()
              else:
                arena.enemy.health -= player.weapon.dmg() - arena.enemy.weapon.dfns()
              print('You have attacked!')
              player.energy -= player.weapon.energy_drain()
            print('The enemy has attacked!')
            player.health -= arena.enemy.weapon.dmg() - player.weapon.dfns()
        elif wheretofight == '3':
          els = ['paragraph', 'anchor', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'header', 'footer']
          fighters = []
          for i in range(10):
            fighters.append(r.choice(els))
          fighters = list(dict.fromkeys(fighters))
          scenes = ['attacked with their margin!', 'defended with their border!', 'set their style to display: none!', 'set their width and height to 75%!']
          for i in fighters:
            print(i, r.choice(scenes))
            time.sleep(1)
        arena.enemy.energy -= arena.enemy.weapon.energy_drain()
        player.energy += 10
        prep()
        player.stamna += player.weapon.stmna_up()
        arena.enemy.stamna += arena.enemy.weapon.stmna_up()
      arena_new_old = 'old'
      if player.health <= 0 or player.base.armor <= 0:#Lose
        player.lives -= 1
        if player.lives == 0:
          print('You died.')
          break
        coins += 25
      if arena.enemy.health <= 0:#Win
        coins += 50
        wins += 1
        if wins % 5 == 0:
          arenanum = (wins / 5) + 1
          arena_new_old = 'new'
        if arena_new_old == 'new' or wins == 1:
          player.levelup()
          if arenanum == 2:
            _404.lvl *= 2
            _404.set()
          elif arenanum == 4:
            virus.lvl *= 2
            virus.set()
        weaponchangechoice = input('Would you like to change your weapon(y/n)?: ')
        if weaponchangechoice == 'y':
          woepan = eval(input('Which weapon?: ').lower())
          if coins > woepan.cost / 5:
            player.weapon = woepan
            coins -= woepan.cost / 5
          else:
            print('You have too less coins.')
        else:
          print('Ok.')
      player.set()
      player.base.set()
      arena.enemy.set()
    else:
      print('No enemies.')
      inchoice = ''
      while inchoice != 'y':
        inchoice = input('Would you like to go back in?: ')
  elif basechoice == '2':
    continue
  elif basechoice == '3':
    weaponchangechoice = input('Would you like to change your weapon(y/n)?: ')
    if weaponchangechoice == 'y':
      woepan = eval(input('Which weapon?: ').lower())
      if coins > woepan.cost / 5:
        player.weapon = woepan
        coins -= woepan.cost / 5
      else:
        print('You have too less coins.')
  elif basechoice == '4':
    if coins >= 20:
      player.levelup()
      coins -= 20
    else:
      print('You have too less coins.')
  else:
    print('Invalid.')