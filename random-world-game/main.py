from replit import db
import random as r
import time as t
newmap = map
import map
import format
import axesories as stuff
def cls():
  __import__('os').system('clear')
ret = input('Are you returning[r] or creating a new account[c]?: ')
def addkeytoall(key, val):
  for i in db:
    if i != 'maps':
      db[i][key] = val
if ret == 'r':
  usr = input('Username?: ')
  pwd = input('Password?: ')
  if db[usr]['pwd'] != pwd:
    print('Invalid credentials.')
    exit()
  else:
    userdata = db[usr]
elif ret == 'c':
  usr = input('Username?: ')
  pwd = input('Password?: ')
  if usr in db:
    print('User exists.')
    exit()
  else:
    db[usr] = {
      'pwd':pwd,
      'wood':0,
      'level':1,
      'coins':0,
      'tut_comp':False,
      'pir_pres':False,
      'pos':(0,0),
      'axesories':[]
    }
    userdata = db[usr]
    map.add_new_map(usr)
def save():
  db[usr] = userdata
def entcon():
  input('[Enter] to continue')
uc = '0'
while uc != '9':
  cls()
  print('Stats')
  print('Wood:', userdata['wood'])
  print('Coins:', userdata['coins'])
  print('Position:', userdata['pos'].value)
  print('Island:', db['maps'][usr][userdata['pos'][1]][userdata['pos'][0]]['island'])
  print('Level:', userdata['level'])
  print('Accessories:', ', '.join(userdata['axesories']))
  format.format(db['maps'][usr], db['maps'][usr][userdata['pos'][1]][userdata['pos'][0]]['island'], 'item')
  print()
  uc = input('''Pick an option:
[1]Tutorial
[2]Move
[3]Build
[4]Wait
[5]Teleport
[6]Bridge islands
[7]Break spot
[8]Shop
[9]Exit
''')
  if uc == '1':
    if userdata['tut comp']:
      continue
    print('You are a lonely little person.')
    t.sleep(1)
    print('On a lonely little island.')
    t.sleep(1)
    print('That has two blocks of space, you and a tree.')
    t.sleep(1)
    td = input('Press [t](then enter) to break the tree(with your fists): ')
    while td != 't':
      td = input('Press [t](then enter) to break the tree(with your fists): ')
    del td
    userdata['wood'] += 1
    db['maps'][usr][0][1]['item'] = '-'
    print('You gained some wood!')
    # userdata['tut_comp'] = True
    entcon()
  elif uc == '2':
    dir = input('Press [r]ight, [l]eft, [d]own, or [u]p: ')
    pos = userdata['pos']
    map = db['maps'][usr]
    itemfound = '-'
    if dir == 'r' and pos[0] != 9 and map[pos[1]][pos[0]+1]['island'] != 'none':
      if map[pos[1]][pos[0]+1]['item'] != '-':
        itemfound = map[pos[1]][pos[0]+1]['item']
      else:
        map[pos[1]][pos[0]+1]['item'] = 'u'
        map[pos[1]][pos[0]]['item'] = '-'
        pos[0] += 1
    elif dir == 'l' and pos[0] != 0 and map[pos[1]][pos[0]-1]['island'] != 'none':
      if map[pos[1]][pos[0]-1]['item'] != '-':
        itemfound = map[pos[1]][pos[0]-1]['item']
      else:
        map[pos[1]][pos[0]-1]['item'] = 'u'
        map[pos[1]][pos[0]]['item'] = '-'
        pos[0] -= 1
    elif dir == 'd' and pos[1] != 9 and map[pos[1]+1][pos[0]]['island'] != 'none':
      if map[pos[1]+1][pos[0]]['item'] != '-':
        itemfound = map[pos[1]+1][pos[0]]['item']
      else:
        map[pos[1]+1][pos[0]]['item'] = 'u'
        map[pos[1]][pos[0]]['item'] = '-'
        pos[1] += 1
    elif dir == 'u' and pos[1] != 0 and map[pos[1]-1][pos[0]]['island'] != 'none':
      if map[pos[1]-1][pos[0]]['item'] != '-':
        itemfound = map[pos[1]-1][pos[0]]['item']
      else:
        map[pos[1]-1][pos[0]]['item'] = 'u'
        map[pos[1]][pos[0]]['item'] = '-'
        pos[1] -= 1
    if itemfound == 't':
      print('You found a tree!')
      td = input('Press [t] to break the tree(with your fists): ')
      while td != 't':
        td = input('Press [t] to break the tree(with your fists): ')
      del td
      userdata['wood'] += 1
    elif itemfound == 'c':
      print('You found a chest!')
      td = input('Press [c] to open the chest: ')
      while td != 'c':
        td = input('Press [c] to open the chest: ')
      del td
      userdata['coins'] += 5
    elif itemfound == 's':
      print('You found a skeleton...')
      health = userdata['level'] * 10
      skhlth = r.randint(1, userdata['level']+1) * 12
      while health > 0 and skhlth > 0:
        cls()
        print('Your health:', health)
        print('Skeleton health:', skhlth)
        print('Press')
        uac = input('[A]ttack\n[R]un\n').lower()
        if uac == 'a':
          if 'sword' in userdata['axesories']:
            dmg = stuff.sories['sword'](userdata).damage
          else:
            dmg = userdata['level'] * r.randint(1, 5)
          skhlth -= dmg
          print('You inflicted', dmg, 'damage.')
          if skhlth <= 0 or skhlth == 1:
            break
          ndmg = r.randint(1, skhlth//2)
          health -= ndmg
          print('You took', ndmg, 'damage.')
          entcon()
      if health <= 0:
        print('You lost.')
      if skhlth <= 0 or skhlth == 1:
        print('You won!')
        cns = r.randint(1, userdata['level'])
        print('You gained 1 level!')
        print('You gained', cns, 'coins!')
        userdata['level'] += 1
        userdata['coins'] += cns
      entcon()
    elif itemfound == 'p':
      print('You found a pirate...')
      health = userdata['level'] * 10
      prhlth = r.randint(userdata['level']-2, userdata['level']+5) * 11
      while health > 0 and prhlth > 0:
        cls()
        print('Your health:', health)
        print('Pirate health:', prhlth)
        print('Press [Enter] to attack')
        input()
        dmg = userdata['level'] * r.randint(7, 12)
        prhlth -= dmg
        print('You inflicted', dmg, 'damage.')
        if prhlth <= 0:
          break
        ndmg = userdata['level'] * r.randint(5, 10)
        health -= ndmg
        print('You took', ndmg, 'damage.')
        entcon()
      if health <= 0:
        print('You lost.')
        print('You lost 10 coins.')
        print('You lost 1 level.')
        print('You lost 1 wood.')
        userdata['coins'] -= 10
        if userdata['coins'] < 0:
          userdata['coins'] = 0
        userdata['wood'] -= 1
        if userdata['wood'] < 0:
          userdata['wood'] = 0
        userdata['level'] -= 1
      if prhlth <= 0:
        print('You won!')
        cns = r.randint(1, userdata['level'])
        print('You gained 1 level!')
        print('You gained', cns, 'coins!')
        print('You gained 2 wood!')
        userdata['level'] += 1
        userdata['coins'] += cns
        userdata['wood'] += 2
      userdata['pir_pres'] = False
      entcon()
    if itemfound != '-':
      if dir == 'r':
        map[pos[1]][pos[0]+1]['item'] = 'u'
        map[pos[1]][pos[0]]['item'] = '-'
        pos[0] += 1
      elif dir == 'l':
        map[pos[1]][pos[0]-1]['item'] = 'u'
        map[pos[1]][pos[0]]['item'] = '-'
        pos[0] -= 1
      elif dir == 'd':
        map[pos[1]+1][pos[0]]['item'] = 'u'
        map[pos[1]][pos[0]]['item'] = '-'
        pos[1] += 1
      elif dir == 'u':
        map[pos[1]-1][pos[0]]['item'] = 'u'
        map[pos[1]][pos[0]]['item'] = '-'
        pos[1] -= 1
    userdata['pos'] = pos
    maps = db['maps']
    maps[usr] = map
    db['maps'] = maps
    del maps
  elif uc == '3':
    if userdata['wood'] == 0:
      print('Not enough wood.')
      entcon()
      continue
    dir = input('Direction([r]ight, [l]eft, [d]own, [u]p)?: ')
    isle = input('[n]ew island or build on [c]urrent island?: ')
    if isle == 'n':
      islename = input('Name of island?: ')
    add = lambda i:i+1
    sub = lambda i:i-1
    ind = None
    pos = userdata['pos']
    map = db['maps'][usr]
    if dir == 'r':
      fnc = add
      ind = 0
    elif dir == 'l':
      ind = 0
      fnc = sub
    elif dir == 'd':
      ind = 1
      fnc = add
    elif dir == 'u':
      ind = 1
      fnc = sub
    if ind == 0:
      if map[pos[1]][fnc(pos[0])]['item'] == '-' and map[pos[1]][fnc(pos[0])]['island'] == 'none':
        if isle == 'n':
          map[pos[1]][fnc(pos[0])]['island'] = islename
        elif isle == 'c':
          map[pos[1]][fnc(pos[0])]['island'] = db['maps'][usr][userdata['pos'][1]][userdata['pos'][0]]['island']
        userdata['wood'] -= 1
      else:
        print('Cannot build. Could be because there is already land there, try to move there for more info.')
        entcon()
    elif ind == 1:
      if map[fnc(pos[1])][pos[0]]['item'] == '-' and map[fnc(pos[1])][pos[0]]['island'] == 'none':
        if isle == 'n':
          map[fnc(pos[1])][pos[0]]['island'] = islename
        elif isle == 'c':
          map[fnc(pos[1])][pos[0]]['island'] = db['maps'][usr][userdata['pos'][1]][userdata['pos'][0]]['island']
        userdata['wood'] -= 1
      else:
        print('Cannot build. Could be because there is already land there, try to move there for more info.')
        entcon()
    userdata['pos'] = pos
    maps = db['maps']
    maps[usr] = map
    db['maps'] = maps
    del maps
  elif uc == '4':
    pos = userdata['pos']
    zmap = db['maps'][usr]
    if userdata['pir_pres']:
      p1 = None
      p2 = None
      brk = 0
      for i in range(len(zmap)):
        for j in range(len(zmap[i])):
          if zmap[i][j]['item'] == 'p':
            p1 = i
            p2 = j
            brk = 1
            break
        if brk: break
      zmap[p1][p2]['item'] = '-'
      ind1 = r.randint(0, 9)
      ind2 = r.randint(0, 9)
      while ind1 == p1 or ind2 == p2 or zmap[ind1][ind2]['item'] == 'u':
        ind1 = r.randint(0, 9)
        ind2 = r.randint(0, 9)
      zmap[ind1][ind2]['item'] = 'p'
    else:
      nop = int(r.choice('001'))
      if nop:
        ind1 = r.randint(0, 9)
        ind2 = r.randint(0, 9)
        iters = 0
        #prevents items from spawning on islands: zmap[ind1][ind2]['island'] == 'none'
        while zmap[ind1][ind2]['item'] in ['u', 't', 'c', 's', 'p']:
          if iters == 100:
            break
          ind1 = r.randint(0, 9)
          ind2 = r.randint(0, 9)
          iters += 1
        zmap[ind1][ind2]['item'] = r.choice('tcs')
      elif not nop and userdata['level'] >= 10:
        ind1 = r.randint(0, 9)
        ind2 = r.randint(0, 9)
        iters = 0
        while zmap[ind1][ind2]['island'] != 'none' or zmap[ind1][ind2]['item'] == 'u':
          if iters == 100:
            break
          ind1 = r.randint(0, 9)
          ind2 = r.randint(0, 9)
          iters += 1
        zmap[ind1][ind2]['item'] = 'p'
        userdata['pir_pres'] = True
    userdata['pos'] = pos
    maps = db['maps']
    maps[usr] = zmap
    db['maps'] = maps
    del maps
  elif uc == '5':
    x = int(input('x?: '))
    y = int(input('y?: '))
    zmap = db['maps'][usr]
    if x > 9 or y > 9:
      print('Too far.')
      entcon()
    while zmap[y][x]['island'] == 'none' or zmap[y][x]['item'] in ['t', 'c', 's', 'p']:
      x = int(input('x?: '))
      y = int(input('y?: '))
    zmap[userdata['pos'][1]][userdata['pos'][0]]['item'] = '-'
    userdata['pos'][0] = x
    userdata['pos'][1] = y
    zmap[y][x]['item'] = 'u'
    maps = db['maps']
    maps[usr] = zmap
    db['maps'] = maps
    del maps
  elif uc == '6':
    x = userdata['pos'][0]
    y = userdata['pos'][1]
    zmap = db['maps'][usr]
    currisland = zmap[y][x]['island']
    bridgeisland = input(f'What island would you like to bridge {currisland} with?: ')
    newname = input('Under what name?: ')
    for i in range(len(zmap)):
      for j in range(len(zmap[i])):
        if zmap[i][j]['island'] in [currisland, bridgeisland]:
          zmap[i][j]['island'] = newname
    maps = db['maps']
    maps[usr] = zmap
    db['maps'] = maps
    del maps
    entcon()
  elif uc == '7':
    userdata['wood'] += 1
    x = userdata['pos'][0]
    y = userdata['pos'][1]
    zmap = db['maps'][usr]
    zmap[y][x]['island'] = 'none' # bookmark
    maps = db['maps']
    maps[usr] = zmap
    db['maps'] = maps
    del maps
    entcon()
  elif uc == '8':
    usc = '0'
    while usc != '2':
      cls()
      usc = input('''Choose one:
[1]Buy sword(100 coins)
[2]Exit
''')
      if usc == '1':
        if 'sword' in userdata['axesories']:
          print('You already have a sword.')
          entcon()
          continue
        elif userdata['coins'] < 100:
          print('Not enough coins.')
          entcon()
          continue
        else:
          b = input('Buy sword(y/n)?:')
          if b == 'y':
            userdata['coins'] -= 100
            userdata['axesories'].append('sword')
            entcon()
          else:
            continue
  save()