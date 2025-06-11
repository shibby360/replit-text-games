import requests, buildings as bldg, troops as trp
import json
import random as rand
import os
dataurl = 'https://replit-game-data.vercel.app/text-vil'
signlog = input('[r]eturning or [n]ew player? ')
if signlog == 'r':
  udata = requests.get(dataurl + '/data', data={
    'username':input('username: '), 
    'password':input('password: ')
  }).json()
  if 'msg' in udata and udata['msg'] == 'incorrect':
    print('incorrect login')
    exit()
elif signlog == 'n':
  udata = requests.get(dataurl + '/makeacc', data={
    'username':input('username: '),
    'password':input('password: ')
  }).json()
else:
  exit()
userid = list(udata.keys())[0]
udata = list(udata.values())[0]
def save():
  requests.post(dataurl + '/save', data={
    'userdata':json.dumps(udata),
    'userid':userid[::-1]
  })

def randprob(prob):
  lst = []
  prob = int(prob * 10)
  for i in range(prob):
    lst.append(True)
  for i in range(100-prob):
    lst.append(False)
  return rand.choice(lst)
def continu():
  input('[enter/return]')
def village(buildings, selected=None):
  basechar = '.'
  end = [[basechar + ' ']*10]
  newend = [ele.copy() for ele in end for _ in range(10)]
  endstr = ''
  for i in buildings:
    curbld = buildings[i]
    bldobj = bldg.buildingtypes[curbld['type']]
    reset = '\x1b[0m'
    ending = ' '+reset
    if not curbld['dead']:
      newend[curbld['y']][curbld['x']] = bldobj.look[0]+ending
      newend[curbld['y']][curbld['x']+1] = bldobj.look[1]+ending
      newend[curbld['y']+1][curbld['x']] = bldobj.look[2]+ending
      newend[curbld['y']+1][curbld['x']+1] = bldobj.look[3]+ending
    else:
      newend[curbld['y']][curbld['x']] = 'X '
      newend[curbld['y']][curbld['x']+1] = 'X '
      newend[curbld['y']+1][curbld['x']] = 'X '
      newend[curbld['y']+1][curbld['x']+1] = 'X '
  for i in newend:
    for j in i:
      endstr += j
    endstr += '\n'
  return endstr
def troopoverview(troops):
  end = ''
  for i in troops:
    end += '  '+i+': '+str(troops[i])
  return end

run = 1
asktorev = True
while run:
  os.system('clear')
  print('Disclaimers: You have to press enter after pressing a key, you can\'t just press the key\nx and y start at the top left corner from 0 and go out from there\n~~~~~~~~~~~~~~~~~~')
  vhlvl = 0
  for i in udata['buildings']:
    if udata['buildings'][i]['type'] == 'village hall':
      vhlvl = udata['buildings'][i]['level']
  print(udata['username'], vhlvl, sep=', level ')
  print('Mail:')
  print(*udata['mail'], sep='\n')
  print(f'Coins: {udata["coins"]}')
  print('Troops:')
  print(troopoverview(udata['troops']))
  print(village(udata['buildings']))
  if len([x['dead'] for x in udata['buildings'].values() if x['dead']]) == len(udata['buildings'].values()) and asktorev:
    print('looks like all your buildings are destroyed.')
    if input('rebuild them(y/n)? ') == 'y':
      revcost = sum([5*x['level'] for x in udata['buildings'].values()])
      if udata['coins'] >= revcost:
        udata['coins'] -= revcost
        for i in udata['buildings']:
          udata['buildings'][i]['dead'] = False
      else:
        asktorev = False
        print('not enough coins')
        continu()
      save()
      continue
    else:
      asktorev = False
  cho = input('''[1]Attack
[2]Building Shop
[3]Train troops
[4]Rebuild destroyed buildings
[5]Clear mail
[6]Move buildings
[7]Exit\n''')
  if cho == '1':
    toatkcho = ''
    while toatkcho != 'y' and toatkcho != 'e':
      os.system('clear')
      atkdata = requests.get(dataurl + '/attackname', data={
        'userfrom':userid,
      }).json().copy()
      atkid = atkdata['uid']
      del atkdata['uid']
      print(atkdata['username'])
      print(village(atkdata['buildings']))
      print('Your troops:')
      print(troopoverview(udata['troops']))
      toatkcho = input('Attack(y/n/e to exit)? ')
    if toatkcho == 'e':
      continue
    elif toatkcho == 'y':
      os.system('clear')
      print(atkdata['username'])
      print(village(atkdata['buildings']))
      print('Your troops:')
      print(troopoverview(udata['troops']))
      oppbldgs = atkdata['buildings'].copy()
      if len([x['dead'] for x in atkdata['buildings'].values() if x['dead']]) == len(atkdata['buildings'].values()):
        print('all their buildings are destroyed!')
        continu()
        continue
      trpdplycho = ''
      dplydamnt = 0
      troophealthlist = []
      def getdplytroops():
        global trpdplycho, dplydamnt, troophealthlist
        if udata['troops'] == {}:
          print('you have no troops left!')
          continu()
          return 'break'
        trpdplycho = input('pick a troop to deploy(all of them): ')
        while trpdplycho not in udata['troops']:
          trpdplycho = input('pick a troop to deploy(all of them): ')
        dplydamnt = udata['troops'][trpdplycho]
        del udata['troops'][trpdplycho]
        troophealthlist = [trp.trooptypes[x].health for x in [trpdplycho]*dplydamnt]
      getdplytroops()
      killedbuildings = 0
      for bdgid in oppbldgs:
        atkgblg = oppbldgs[bdgid]
        atkgblgobj = bldg.buildingtypes[atkgblg['type']]
        blglvl = atkgblg['level']
        blghealth = atkgblgobj.health * blglvl
        while blghealth > 0 and dplydamnt > 0:
          i = 0
          while i < len(troophealthlist):
            trpobj = trp.trooptypes[trpdplycho]
            blghealth -= trpobj.damage * vhlvl
            if atkgblgobj.type == 'defense':
              troophealthlist[i] -= atkgblgobj.otherdata['damage'] * blglvl
              if troophealthlist[i] <= 0:
                dplydamnt -= 1
                troophealthlist.pop(i)
                continue  # don't increment i, as list shrank
            i += 1
        if blghealth <= 0:
          atkdata['buildings'][bdgid]['dead'] = True
          killedbuildings += atkdata['buildings'][bdgid]['level']
        if dplydamnt <= 0:
          if getdplytroops() == 'break':
            break
        print('Building overview: ', *[f'{x["type"]}: {"Destroyed" if x["dead"] else "Standing"}' for x in atkdata['buildings'].values()], sep='\n')
        continu()
      atkdata['mail'].append('You got attacked by ' + udata['username'])
      udata['coins'] += killedbuildings*10
      print('You got', killedbuildings*10, 'coins')
      print('Their village:')
      print(village(atkdata['buildings']))
      requests.post(dataurl + '/save', data={
        'userdata':json.dumps(atkdata),
        'userid':atkid[::-1]
      })
      continu()
  elif cho == '2':
    allbldgs = list(bldg.buildingtypes.keys()).copy()
    allbldgs.remove('village hall')
    bldgswcosts = [f'{x}({bldg.buildingtypes[x].cost}c)' for x in allbldgs]
    print('pick a bulding: ')
    print(*bldgswcosts, sep=', ')
    bldgcho = input('which one?: ')
    if bldgcho not in [x.name for x in list(bldg.buildingtypes.values())]:
      print('invalid building')
      continu()
      continue
    elif udata['coins'] < bldg.buildingtypes[bldgcho].cost:
      print('not enough coins')
      continu()
      continue
    bldig = requests.get(dataurl + '/newid').text
    occps = []
    x = 0
    y = 0
    for i in udata['buildings']:
      curbld = udata['buildings'][i]
      cx = curbld['x']
      cy = curbld['y']
      occps.append((cx, cy))
      occps.append((cx+1, cy))
      occps.append((cx, cy+1))
      occps.append((cx+1, cy+1))
    while (x, y) in occps:
      x = int(input('x: '))
      y = int(input('y: '))
    udata['buildings'][bldig] = {'type':bldgcho, 'level':1, 'x':x, 'y':y, 'dead':False}
    udata['coins'] -= bldg.buildingtypes[bldgcho].cost
  elif cho == '3':
    alltrps = list(trp.trooptypes.keys()).copy()
    trpswcosts = [f'{x}({trp.trooptypes[x].cost}c)' for x in alltrps]
    print('pick a troop: ')
    print(*trpswcosts, sep=', ')
    trpcho = input('which one?: ')
    numtrp = int(input('how many?: '))
    if trpcho not in [x.name for x in list(trp.trooptypes.values())]:
      print('invalid troop')
      continu()
      continue
    elif udata['coins'] < trp.trooptypes[trpcho].cost*numtrp:
      print('not enough coins')
      continu()
      continue
    prevnumtrp = udata['troops'][trpcho] if trpcho in udata['troops'] else 0
    udata['troops'][trpcho] = prevnumtrp + numtrp
    udata['coins'] -= trp.trooptypes[trpcho].cost * numtrp
  elif cho == '4':
    deadbuildings = [x for x in udata['buildings'] if udata['buildings'][x]['dead']]
    if deadbuildings == []:
      print('none of your buildings are destroyed')
      continu()
      continue
    revcost = sum([5*x['level'] for x in udata['buildings'].values()])
    if udata['coins'] >= revcost:
      udata['coins'] -= revcost
      for i in udata['buildings']:
        udata['buildings'][i]['dead'] = False
    else:
      print('not enough coins')
      continu()
  elif cho == '5':
    udata['mail'] = []
  elif cho == '6':
    os.system('clear')
    print(village(udata['buildings']))
    print('Buildings:')
    for b_id, b in udata['buildings'].items():
      print(f"  {b['type']} at ({b['x']}, {b['y']})")
    bldg_to_move_name = input('Enter the building name to move (or blank to cancel): ')
    if not bldg_to_move_name:
      print('Cancelled.')
      continu()
    try:
      bldg_to_move_x = int(input('Enter the x coordinate of the building to move: '))
      bldg_to_move_y = int(input('Enter the y coordinate of the building to move: '))
    except ValueError:
      print('Invalid coordinates.')
      continu()
      continue
    bldg_to_move = None
    for b_id, b in udata['buildings'].items():
      if b['type'] == bldg_to_move_name and b['x'] == bldg_to_move_x and b['y'] == bldg_to_move_y:
        bldg_to_move = b_id
        break
    if bldg_to_move is None:
      print('No building found with that name and coordinates.')
      continu()
    else:
      occps = []
      for i in udata['buildings']:
        if i == bldg_to_move:
          continue
        curbld = udata['buildings'][i]
        cx = curbld['x']
        cy = curbld['y']
        occps.append((cx, cy))
        occps.append((cx+1, cy))
        occps.append((cx, cy+1))
        occps.append((cx+1, cy+1))
      while True:
        try:
          newx = int(input('New x: '))
          newy = int(input('New y: '))
        except ValueError:
          print('Please enter valid integers.')
          continue
        newspots = [(newx, newy), (newx+1, newy), (newx, newy+1), (newx+1, newy+1)]
        if any(spot in occps for spot in newspots):
          print('That spot collides with another building. Try again.')
          continue
        break
      udata['buildings'][bldg_to_move]['x'] = newx
      udata['buildings'][bldg_to_move]['y'] = newy
      print('Building moved!')
      continu()
  elif cho == '7':
    save()
    exit()
  save()
