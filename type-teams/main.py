import os
import random as r
import replit.database.database as dber
try:
  import shdwdb
except ModuleNotFoundError:
  os.system('pip install shdwdb')
  import shdwdb
os.system('clear')
kts = 'stats'
userDB = ShdwDB.retrieve('User stats', kts)
userDB.kts = kts
userDB.autosave = True
userDB.def_val = 0

import teams.hot as hot
import teams.transform as transform
import teams.storm as storm
import teams.secreteam as secreteam
import enemies.massdark as massdark
import enemies.circuitizer as circuitizer
name = input('Name?: ')
pwd = input('Password?: ')
def auth(name, pwd):
  if name+'-password' in ShdwDB.db:
    if ShdwDB.db[name+'-password'] == pwd:
      pass
    else:
      print('Invaid authorization.')
      exit()
  else:
    ShdwDB.db[name+'-password'] = pwd
auth(name, pwd)
attrs = None
def prof(name):
  global attrs
  try:
    attrs = userDB.get_column(name)
  except KeyError:
    userDB.add_column(name)
    userDB.set(name, 'Teams in', [])
    userDB.set(name, 'Teams damaged', [])
    userDB.set(name, 'energy', 500)
    attrs = userDB.get_column(name)
  for attr in attrs:
    if type(attrs[attr]) in [dber.ObservedList, dber.ObservedDict]:
      attrs[attr] = attrs[attr].value
prof(name)

codetoteamin = {'123+':'Hot', '456+789':'Transform', '0-0':'Storm', '++++':'Secreteam'}
codetoteamout = {'-321':'Hot', '987-654':'Transform', '+0+':'Storm', '--':'Secreteam'}
class JSON:
  def __init__(self, dicti):
    for d in dicti:
      setattr(self, d, dicti[d])
  def __getitem__(self, key):
    return self.__dict__[key]
  def __setitem__(self, key, value):
    self.__dict__[key] = value
_ = JSON({'k':'g', 'r':'e'})
while True:
  os.system('clear')
  print('Coins:', attrs['coins'])
  print('Teams in:', attrs['Teams in'])
  print('Teams damaged:', attrs['Teams damaged'])
  print('Energy:', attrs['energy'])
  choice = input(
    """[1]Battle
[2]Shop
[3]Call a team in
[4]Call a team out
[5]Exit
Which one?: """
  )
  if choice == '1':
    if not attrs['Teams in'] or 10 > attrs['energy']:
      continue
    Teams_in = attrs['Teams in']
    team = input(f'Choose your team{Teams_in}: ')
    while team not in Teams_in:
      team = input(f'Choose your team{Teams_in}: ')
    master = eval(team.lower() + '.master')
    mem = input(f'Which offender{list(master.offenders)}?: ')
    while mem not in master.offenders:
      mem = input(f'Which offender{list(master.offenders)}?: ')
    mem = master.memdict[mem].copy('mem')
    enemy = r.choice([massdark, circuitizer])
    enemy = enemy.copy('enemy')
    enemycanatk = True
    while True:
      os.system('clear')
      print('Your Health:', mem.health)
      print('Enemy Health:', enemy.health)
      bchoice = input("""[1]Attack
[2]Call Medic
[3]Chill
Which one?: """)
      if bchoice == '1':
        userDB.set(name, 'energy', attrs['energy']-10)
        sbchoice = input('Would you like to call in a support(y/n)?: ').lower()
        if 30 > attrs['energy'] and sbchoice != 'n':
          print('Cannot call the support.')
          sbchoice = 'n'
        dmg = mem.damage
        if mem.name == 'Bull':
          userDB.set(name, 'energy', attrs['energy']-30)
        if sbchoice == 'y':
          userDB.set(name, 'energy', attrs['energy']-30)
          support = input(f'Pick your support{list(master.supports)}: ')
          while support not in master.supports:
            support = input(f'Pick your support{list(master.supports)}: ')
          support = master.supports[support]
          if support.name == 'Ember':
            dmg += hot.ember.damage
          elif support.name == 'Power up':
            dmg += dmg*(transform.powerup.damage/100)
          elif support.name == 'Cloak':
            enemycanatk = False
            if mem.name == 'Ram':
              enemy.health -= transform.cloak.damage
          elif support.name == 'Cloud':
            enemycanatk = False
          elif support.name == 'Thunder':
            dmg += storm.thunder.damage
            enemycanatk = False
        enemy.health -= dmg
        if enemycanatk:
          mem.health -= enemy.damage
      if bchoice == '2':
        mem.health += master.medic['Medic'].damage
        print('\x1b[0;32mHealed!\x1b[0m')
        input()
      if mem.health <= 0:
        print('You lose...')
        Teams_in_ = attrs['Teams in'][:]
        Teams_in_.remove(team)
        userDB.set(name, 'Teams in', Teams_in_)
        dmgdtms = userDB.get_value(name, 'Teams damaged')[:]
        dmgdtms.append(team)
        userDB.set(name, 'Teams damaged', dmgdtms)
        input()
        break
      elif enemy.health <= 0:
        print('You win!!!')
        userDB.set(name, 'energy', attrs['energy']+100)
        userDB.set(name, 'coins', attrs['coins']+30)
        input()
        break
  elif choice == '2':
    while True:
      os.system('clear')
      print('Coins:', attrs['coins'])
      schoice = input("""[1]Buy Energy
[2]Exit Shop
Which one?: """)
      if schoice == '1':
        amnt = int(input('How much energy do you want to buy?: '))
        shopbuyeneryn = input('Buy for \x1b[0;33m{} coins(y/n)?: \x1b[0m'.format(amnt*2))
        if shopbuyeneryn == 'y':
          userDB.set(name, 'coins', attrs['coins']-amnt*2)
          userDB.set(name, 'energy', attrs['energy']+amnt)
      elif schoice == '2':
        userDB.save(kts)
        break
  elif choice == '3':
    code = input('Code?: ')
    if code in codetoteamin:
      if codetoteamin[code] not in attrs['Teams in']:
        userDB.set(name, 'Teams in', userDB.get_value(name, 'Teams in')+[codetoteamin[code]])
        userDB.set(name, 'energy', attrs['energy']-150)
  elif choice == '4':
    code = input('Code?: ')
    if code in codetoteamout:
      if codetoteamout[code] in attrs['Teams in']:
        inteams = attrs['Teams in'][:]
        inteams.remove(codetoteamout[code])
        userDB.set(name, 'Teams in', inteams)
      elif codetoteamout[code] in attrs['Teams damaged']:
        dmgdteams = attrs['Teams damaged'][:]
        dmgdteams.remove(codetoteamout[code])
        userDB.set(name, 'Teams damaged', dmgdteams)
  elif choice == '5':
    userDB.save(kts)
    break
  userDB.save(kts)