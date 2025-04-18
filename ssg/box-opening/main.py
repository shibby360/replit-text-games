import os
try:
  import ShdwDB
except ModuleNotFoundError:
  os.system('pip install ShdwDB')
  os.system('clear')
  import ShdwDB 
#from replit import db
import items
def mergelists(list1, list2):
  for ite in list2:
    if ite not in list1:
      list1.append(ite)
  return list1
def reset(user, *resets):
  for reset in resets:
    userDB.set(user, reset, type(userDB.get_value(user, reset))())
  userDB.save(kts)

kts = 'stats'
userDB = ShdwDB.retrieve('User stats', kts)
#userDB = ShdwDB.make('User stats', ['Shdw'], ['coins', 'energy', 'health', 'keys', 'gems', 'Patriots'])
name = input('Name?: ')
userDB.def_val = 0
userDB.autosave = True
try:
  attrs = userDB.get_column(name)
except KeyError:
  userDB.add_column(name)
  attrs = userDB.get_column(name)
while True:
  print('-------\nStats:')
  print('Your Patriots: ' + str(attrs['Patriots']))
  print('Coins: ' + str(attrs['coins']))
  print('Energy: ' + str(attrs['energy']))
  print('Health: ' + str(attrs['health']))
  print('Keys: ' + str(attrs['keys']))
  print('Gems: ' + str(attrs['gems']))
  chestschoosable = []
  for chest in items.chests:
    if chest['unit'] == 'coins':
      if chest['cost'] <= attrs['coins']:
        chestschoosable.append(chest['chest'])
    elif chest['unit'] == 'gems':
      if chest['cost'] <= attrs['gems']:
        chestschoosable.append(chest['chest'])
  b = input(f'Which chest{chestschoosable}?: ')
  if b == 'break':
    userDB.save(kts)
    break
  elif b == 'archive':
    archiveprof = userDB.get_column(name)
    key = input('key?: ')
    svdprfs = ShdwDB.db['archived profiles']
    svdprfs[key] = archiveprof
    ShdwDB.db['archived profiles'] = svdprfs
    userDB.delete_column(name)
    name = input('New name?: ')
    userDB.add_column(name)
    attrs = userDB.get_column(name)
  while b not in chestschoosable:
    b = input(f'Which chest{chestschoosable}?: ')
  os.system('clear')
  thechest = items.checkchest(b)
  unit = thechest['unit']
  cost = thechest['cost']
  userDB.set(name, unit, attrs[unit]-cost)
  print('-------')
  ret = items.SSGer('c', b, userDB.get_value('Shdw', 'Patriots'))
  userDB.set(name, 'coins', userDB.get_value(name, 'coins')+ret['coins'])
  userDB.set(name, 'energy', userDB.get_value(name, 'energy')+ret['energy'])
  userDB.set(name, 'health', userDB.get_value(name, 'health')+ret['health'])
  if 'keys' in ret:
    userDB.set(name, 'keys', userDB.get_value(name, 'keys')+ret['keys'])
  if 'Patriot' in ret:
    userDB.set(name, 'Patriots', mergelists(userDB.get_value(name, 'Patriots'), ret['Patriot']))
  if 'gems' in ret:
    userDB.set(name, 'gems', userDB.get_value(name, 'gems')+ret['gems'])
  userDB.save(kts)

#Add merge function to Shdw