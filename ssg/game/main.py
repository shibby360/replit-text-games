import os
import random as r
try:
  import ShdwDB
except ModuleNotFoundError:
  os.system('pip install ShdwDB')
  os.system('clear')
  import ShdwDB
import boxs
import patrs
def mergelists(list1, list2) -> list:
  for ite in list2:
    if ite not in list1:
      list1.append(ite)
  return list1
def reset(user, *resets) -> None:
  for reset in resets:
    userDB.set(user, reset, type(userDB.get_value(user, reset))())
  userDB.save(kts)
kts = 'stats'
userDB = ShdwDB.retrieve('User stats', kts)
userDB.autosave = True
userDB.def_val = 0
userDB.kts = kts

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
    userDB.set(name, 'Patriots', [])
    userDB.set(name, 'Soldiers', [])
    userDB.set(name, 'ancmnts',  [])
    userDB.set(name, 'share market', {'shares':1, 'share worth':1})
    attrs = userDB.get_column(name)
prof(name)
def getdict(item):
  return item.__dict__
def roundup(float):
  float = str(float).split('.')[0]
  float = int(float)
  return float + 1
def viewprof(attrs):
  print('Patriots: ' + str(attrs['Patriots']))
  print('Soldiers: ' + str(attrs['Soldiers']))
  print('Coins: ' + str(attrs['coins']))
  print('Energy: ' + str(attrs['energy']))
  print('Health: ' + str(attrs['health']))
  print('Keys: ' + str(attrs['keys']))
  print('Gems: ' + str(attrs['gems']))
  print('Medals: ' + str(attrs['Medals']))
def setall(key, value):
  for dat in userDB:
    userDB.data[dat][key] = value
  userDB.save(kts)
while True:
  os.system('clear')
  #print('\x1b[0;34mBETA\x1b[0m')
  if attrs['ancmnts']:
    for ancmnt in attrs['ancmnts']:
      print(ancmnt)
    input()
  viewprof(attrs)
  print('-------')
  print('[1]Battle\n[2]Shop\n[3]Exit\n[4]Delete account\n[5]Switch Account\n[6]Go to Share market\n[7]View a profile\n[8]Create a gift card\n[9]Redeem a gift card')
  choice = input('Which one?: ')
  os.system('clear')
  if choice == '1':
    if attrs['Patriots'] == []:
      print('You cannot battle.')
      input()
      continue
    patrchose = eval('patrs.' + input('Which patriot{}?: '.format(attrs['Patriots'])).lower().replace(' ', '_'))
    if patrchose.name not in attrs['Patriots']:
      print('Invalid Patriot.')
      input()
      continue
    hlth = patrchose.health
    backuphlth = attrs['health']
    opnt = boxs.SSGer('b')
    opnt = eval('patrs.' + opnt.lower().replace(' ', '_'))
    opphlth = opnt.health
    distance = 5
    shotstook = 0
    soldier = False
    while hlth > 0 and opphlth > 0:
      print('Your health:', hlth)
      print('Opponent health:', opphlth)
      valids = ['move']
      if distance <= patrchose.gun.range and distance >= 0:
        print('• Gun')
        valids.append('gun')
      if patrchose.name != 'Ora':
        if distance <= 3 and distance >= 0:
          print('• Sword')
          valids.append('sword')
          if attrs['energy'] >= 250:
            print('• Max')
            valids.append('max')
      else:
        print('• Sword')
        valids.append('sword')
        if attrs['energy'] >= 250:
          print('• Max')
          valids.append('max')
      if attrs['energy'] > 500:
        print('• Power up')
        valids.append('power up')
      if not soldier:
        print('• Add soldier(soldier)')
        valids.append('solider')
      print('• Move')
      which = input('Which one?: ').lower()
      if which in valids:
        dodgeable = True
        if which == 'gun':
          end = patrchose.gun.damage
          if patrchose.name == 'Blake':
            end *= 2
          elif patrchose.name == 'Brownja':
            end = patrchose.sword.damage
          elif patrchose.name == 'Tobgat':
            optn = input('Do you want to shoot or control?: ').lower()
            if optn[0] == 's':
              pass
            elif optn[0] == 'c':
              battery = 100
              while battery > 0:
                optn = input(f'🔋 Battery: {battery}%\nOptions:\n[1]Move opponent forward\n[2]Move opponent backward\n[3]Shoot\n[4]Exit control\n: ')
                if optn == '1':
                  distance -= 1
                  battery -= 10
                elif optn == '2':
                  distance += 1
                  battery -= 10
                elif optn == '3':
                  battery -= 100
                elif optn == '4':
                  break
          elif patrchose.name == 'Eulb Krad':
            optn = input('Leave or merge?: ').lower()
            if optn[0] == 'l':
              pass
            elif optn[0] == 'm':
              end += 40
            end += 20
          elif patrchose.name == 'Pinky':
            div = r.randint(1, 4)
            print(div, 'bullets were shot.')
            if div != 4:
              dodgeable = False
            end *= 1/div
            end = int(end)
          elif patrchose.name == 'Purpy':
            div = r.randint(1, 4)
            print(div, 'bullets were shot.')
            if div != 4:
              dodgeable = False
            end *= 1/div
            end = int(end)
            end += 50
          elif patrchose.name == 'Eulb':
            optn = input('Leave or merge?: ').lower()
            if optn[0] == 'l':
              pass
            elif optn[0] == 'm':
              end += 40
          elif patrchose.name == 'Relood':
            end += 50
            dodgeable = False
          elif patrchose.name == 'Ora':
            dodgeable = False
          elif patrchose.name == 'Yeller':
            pass
          if dodgeable:
            end -= opnt.shield.durability
          opphlth -= end
        elif which == 'sword':
          end = patrchose.sword.damage
          if patrchose.name == 'Blake':
            end += 20
          elif patrchose.name == 'Brownja':
            optn = input('Would you like to upgrade(y/n)?: ').lower()
            if optn == 'y':
              shotstook += 1
              end += 50
          elif patrchose.name == 'Tobgat':
            pass
          elif patrchose.name == 'Eulb Krad':
            dodgeable = False
            end += 30
          elif patrchose.name == 'Purpy':
            end /= r.randint(1, 4)
            end += 30
          elif patrchose.name == 'Pinky':
            end /= r.randint(1, 4)
          elif patrchose.name == 'Eulb':
            dodgeable = False
          elif patrchose.name == 'Relood':
            print('\x1b[0;31mYAHHHHH!\x1b[0m')
          elif patrchose.name == 'Ora':
            dodgeable = False
          elif patrchose.name == 'Yeller':
            end += 10
          if dodgeable:
            end -= opnt.shield.durability
          opphlth -= end
        elif which == 'max':
          end = patrchose.max_damage
          attrs['energy'] -= 250
          if patrchose.name == 'Relood':
            end += 50
          if dodgeable:
            end -= opnt.shield.durability
          opphlth -= end
        elif which == 'power up':
          print('Powered up to...')
          attrs['energy'] -= 500
          print(patrchose.power.name.upper() + '!')
          opphlth -= patrchose.power.damage
          enemycanatk = False
          input()
        elif which == 'move':
          direc = input('Forward or backward(f or b)?: ')
          if direc == 'f':
            print('You moved forward.')
            distance -= patrchose.board.speed/2
          elif direc == 'b':
            print('You moved backward.')
            distance += patrchose.board.speed/2
        shotstook += 1
        oppwhich = r.choice(valids)
        #oppmove
        if oppwhich == 'gun':
          hlth -= opnt.gun.damage
        elif oppwhich == 'sword':
          hlth -= opnt.sword.damage
        elif oppwhich == 'max':
          end = opnt.max_damage
          if opnt.name == 'Relood':
            end += 50
          hlth -= end
        elif oppwhich == 'move':
          direc = r.choice('fb')
          if direc == 'f':
            print('Opponent moved forward.')
            distance -= opnt.board.speed/2
          elif direc == 'b':
            print('Opponent moved backward.')
            distance += opnt.board.speed/2
        distance = abs(distance)
        if distance > 10:
          distance = 10
        continue
      print('Invalid action.')
    if hlth <= 0 and opphlth <= 0:
      print('Draw')
      input()
    elif hlth <= 0:
      print('You lose...')
      userDB.set(name, 'Medals', userDB.get_value(name, 'Medals')-3)
      input()
    elif opphlth <= 0:
      print('You win!')
      userDB.set(name, 'Medals', userDB.get_value(name, 'Medals')+8)
      if shotstook <= 5 and hlth >= 35:
        userDB.set(name, 'Medals', userDB.get_value(name, 'Medals')+8)
        userDB.set(name, 'gems', userDB.get_value(name, 'gems')+4)
      elif shotstook <= 5:
        userDB.set(name, 'Medals', userDB.get_value(name, 'Medals')+4)
        userDB.set(name, 'gems', userDB.get_value(name, 'gems')+2)
      elif hlth >= 35:
        userDB.set(name, 'Medals', userDB.get_value(name, 'Medals')+2)
        userDB.set(name, 'gems', userDB.get_value(name, 'gems')+1)
      input()
    if attrs['Medals'] >= 10:
      userDB.set(name, 'Soldiers', mergelists(attrs['Soldiers'], ['Dark']))
    if attrs['Medals'] >= 100:
      userDB.set(name, 'Soldiers', mergelists(attrs['Soldiers'], ['Shade']))
    if attrs['Medals'] >= 1000:
      userDB.set(name, 'Soldiers', mergelists(attrs['Soldiers'], ['Shapeshift']))
    if attrs['Medals'] >= 2000:
      userDB.set(name, 'Soldiers', mergelists(attrs['Soldiers'], ['Night mult']))
    if attrs['Medals'] >= 3000:
      userDB.set(name, 'Soldiers', mergelists(attrs['Soldiers'], ['Dim']))
    if attrs['Medals'] >= 4000:
      userDB.set(name, 'Soldiers', mergelists(attrs['Soldiers'], ['Obscurer']))
    if attrs['Medals'] >= 5000:
      userDB.set(name, 'Soldiers', mergelists(attrs['Soldiers'], ['Copy']))
    if attrs['Medals'] >= 6000:
      userDB.set(name, 'Soldiers', mergelists(attrs['Soldiers'], ['2D']))
    if attrs['Medals'] >= 7000:
      userDB.set(name, 'Soldiers', mergelists(attrs['Soldiers'], ['Fake Attack']))
    if attrs['Medals'] >= 8000:
      userDB.set(name, 'Soldiers', mergelists(attrs['Soldiers'], ['Elongate']))
    if not attrs['Collected 10K reward'] and attrs['Medals'] >= 10000:
      input('Collect 10K Element Chest(Enter)...')
      os.system('clear')
      print('-------')
      ret = boxs.SSGer('c', 'e', userDB.get_value(name, 'Patriots'))
      userDB.set(name, 'coins', userDB.get_value(name, 'coins')+ret['coins'])
      userDB.set(name, 'energy', userDB.get_value(name, 'energy')+ret['energy'])
      userDB.set(name, 'health', userDB.get_value(name, 'health')+ret['health'])
      if 'keys' in ret:
        userDB.set(name, 'keys', userDB.get_value(name, 'keys')+ret['keys'])
      if 'Patriot' in ret:
        userDB.set(name, 'Patriots', mergelists(userDB.get_value(name, 'Patriots'), ret['Patriot']))
      if 'gems' in ret:
        userDB.set(name, 'gems', userDB.get_value(name, 'gems')+ret['gems'])
      input('----\nPress ENTER To continue\n')
  elif choice == '2':
    print('Shop')
    print('Coins:', attrs['coins'])
    print('Keys:', attrs['keys'])
    print('Gems:', attrs['gems'])
    print('[1]Chest\n[2]Increase Share worth\n[3]Decrease Share worth\n[4]Exit Shop')
    shopchoice = input('Which one?: ')
    os.system('clear')
    if shopchoice == '1':
      chestschoosable = ['']
      for chest in boxs.chests:
        if chest['unit'] == 'coins':
          if chest['cost'] <= attrs['coins']:
            chestschoosable.append(chest['chest'])
        elif chest['unit'] == 'gems':
          if chest['cost'] <= attrs['gems']:
            chestschoosable.append(chest['chest'])
      chchoos = chestschoosable
      chchoos.remove('')
      b = input(f'Which chest{chchoos}?: ')
      while b not in chchoos:
        b = input(f'Which chest{chchoos}?: ')
      os.system('clear')
      thechest = boxs.checkchest(b)
      unit = thechest['unit']
      cost = thechest['cost']
      if cost > attrs[unit]:
        print('Too much cost.')
        input()
        continue
      userDB.set(name, unit, attrs[unit]-cost)
      print('-------')
      ret = boxs.SSGer('c', b, userDB.get_value(name, 'Patriots'))
      userDB.set(name, 'coins', userDB.get_value(name, 'coins')+ret['coins'])
      userDB.set(name, 'energy', userDB.get_value(name, 'energy')+ret['energy'])
      userDB.set(name, 'health', userDB.get_value(name, 'health')+ret['health'])
      if 'keys' in ret:
        userDB.set(name, 'keys', userDB.get_value(name, 'keys')+ret['keys'])
      if 'Patriot' in ret:
        userDB.set(name, 'Patriots', mergelists(userDB.get_value(name, 'Patriots'), ret['Patriot']))
      if 'gems' in ret:
        userDB.set(name, 'gems', userDB.get_value(name, 'gems')+ret['gems'])
      input('----\nPress ENTER To continue\n')
    elif shopchoice == '2':
      worthinc = int(input('By how much would you like to \nincrease your share worth?: '))
      if worthinc * 2 > attrs['coins']:
        print('You cannot purchase that much share worth.')
        continue
      print('That is \x1b[0;33m{0} coins.\x1b[0m'.format(worthinc*2))
      cont = input('Would you like to purchase(y/n)?: ').lower()
      if cont.startswith('y'):
        userDB.set(name, 'coins', userDB.get_value(name, 'coins')-worthinc*2)
        userDB.data[name]['share market']['share worth'] += worthinc
    elif shopchoice == '3':
      worthdec = int(input('By how much would you like to \ndecrease you share worth?: '))
      userDB.set(name, 'coins', userDB.get_value(name, 'coins')+roundup(worthdec/2))
      userDB.data[name]['share market']['share worth'] -= worthdec
  elif choice == '3':
    userDB.save(kts)
    break
  elif choice == '4':
    yn = input('Are you sure you want to do this(Y for yes and N for no)?').lower()
    if yn == 'y':
      userDB.delete_column(name)
      del ShdwDB.db[name+'-password']
      userDB.save(kts)
      break
  elif choice == '5':
    name = input('Name?: ')
    pwd = input('Password?: ')
    auth(name, pwd)
    prof(name)
  elif choice == '6':
    stockattrs = userDB.get_value(name, 'share market')
    while True:
      os.system('clear')
      print('Shares: ' + str(stockattrs['shares']))
      print('Share worth: ' + str(stockattrs['share worth']))
      stockchoice = input('[1]Buy shares\n[2]Exit market\nWhich one?: ')
      if stockchoice == '1':
        for dat in userDB:
          if dat != name:
            print('\n', end='')
            print(dat)
            print('Shares:', userDB.data[dat]['share market']['shares'])
            print('Share worth:', userDB.data[dat]['share market']['share worth'])
            print('Coins:', userDB.data[dat]['coins'])
            print('Energy:', userDB.data[dat]['energy'])
            print('Health:', userDB.data[dat]['health'], end='')
            print('\n')
        who = input('Who\'s shares do you want to buy?: ')
        if who == '':
          continue
        howmany = int(input('How many shares do you want to buy?: '))
        cost = howmany * userDB.data[who]['share market']['share worth']
        if cost > attrs['coins'] or howmany <= 0:
          print('You cannot buy that many shares.')
          input()
        else:
          userDB.set(name, 'coins', userDB.get_value(name, 'coins')-cost)
          userDB.data[name]['share market']['shares'] += roundup(howmany/2)
          userDB.data[who]['share market']['shares'] -= howmany
          if userDB.data[who]['share market']['shares'] == 0:
            userDB.data[who]['ancmnts'] += ['{0} bought all your shares!'.format(name)]
            userDB.data[name]['coins'] += userDB.data[who]['coins']
            userDB.data[who]['coins'] = 0
            userDB.data[name]['energy'] += userDB.data[who]['energy']
            userDB.data[who]['energy'] = 0
            userDB.data[name]['health'] += userDB.data[who]['health']
            userDB.data[who]['health'] = 0
            userDB.data[who]['share market']['shares'] = 1
      elif stockchoice == '2':
        break
      userDB.save(kts)
  elif choice == '7':
    profname = input('Who\'s profile would you like to view?: ')
    viewprof(userDB.get_column(profname))
    input()
  elif choice == '8':
    giftcards = ShdwDB.db['giftcards']
    amnt = int(input('Amount(Just number)?: '))
    unit = input('Unit(coins, gems, keys, etc.)?: ').lower()
    if amnt > attrs[unit]:
      print('You can not give this much!')
      input()
      continue
    userDB.set(name, unit, attrs[unit]-amnt)
    def gencode():
      let1 = r.choice('abcdefghijklmnopqrstuvwxyz')
      let2 = r.choice('1234567890')
      let3 = r.choice('abcdefghijklmnopqrstuvwxyz')
      let4 = r.choice('1234567890')
      let5 = r.choice('1234567890')
      return let1+let2+let3+let4+let5
    giftcodes = []
    for giftcard in giftcards:
      giftcodes.append(giftcard['redeemcode'])
    code = gencode()
    while code in giftcodes:
      code = gencode()
    newmnt = str(amnt) + ' '
    giftcards.append({'from':name, 'redeemcode':code, 'amount':newmnt + unit})
    print(f'https://SSG-The-game-gift-cards.shivankchhaya.repl.co?redeemcode={code}&from={name}&amount={newmnt + unit}')
    ShdwDB.db['giftcards'] = giftcards
    input()
  elif choice == '9':
    redeemcode = input('Redeem code?: ')
    giftcards = ShdwDB.db['giftcards']
    for giftcard in giftcards:
      if giftcard['redeemcode'] == redeemcode:
        if giftcard['from'] == name:
          print('You created this gift card!')
          input()
          continue
        else:
          amnt = int(giftcard['amount'].split()[0])
          unit = giftcard['amount'].split()[1]
          userDB.set(name, unit, attrs[unit]+amnt)
          print('Redeemed you gift card!')
          input()
          giftcards.remove(giftcard)
          ShdwDB.db['giftcards'] = giftcards
          continue
  userDB.set(name, 'ancmnts', [])
  userDB.save(kts)