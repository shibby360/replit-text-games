import random as rand
import json
import os
import idgen
import heros
import bases
import enemys
import weapons
import requests
url = 'https://replit-game-data.vercel.app/skuv'
def save():
  db[userid] = userdata
  requests.post(url + '/save?userid='+userid[::-1], data={'userdata':json.dumps(db[userid])})
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
db = requests.get(url+'/getdata').json()
c = input('[r]eturning or [n]ew player?: ')
if c == 'n':
  u = input('username?: ')
  p = input('password?: ')
  unms = []
  for i in db:
    unms.append(db[i]['username'])
  if u in unms:
    print('username taken')
    exit()
  ids = db.keys()
  uid = idgen.gen()
  while uid in ids:
    uid = idgen.gen()
  db[uid] = {
    'username':u,
    'password':p,
    'base':'shack',
    'bases':{'shack':1},
    'hero':'knight',
    'heroes':{'knight':1},
    'coins':0,
    'basehealth':bases.bases['shack'].health
  }
  userid = uid
  userdata = db[uid]
if c == 'r':
  u = input('username?: ')
  p = input('password?: ')
  unms = {}
  for i in db:
    unms[db[i]['username']] = i
  if u in unms:
    if db[unms[u]]['password'] == p:
      print('wsg!')
      continu()
      userid = unms[u]
      userdata = db[userid]
    else:
      print('incorrect password')
      exit()
  else:
    print('username not found')
    exit()
save()
run = 1
prechosen = False
while run:
  os.system('clear')
  heroinuse = heros.heros[userdata['hero']]
  baseinuse = bases.bases[userdata['base']]
  print('*You have to press enter after your press a key, you can\'t just press the key*')
  print(f'Coins: {userdata["coins"]}')
  pl = userdata["heroes"][userdata["hero"]]
  basepl = userdata['bases'][userdata['base']]
  if pl >= 10:
    print('\033[0;33m', end='')
  print(f'Hero: {heros.getcosm(heroinuse, pl)}{heroinuse.name}, {pl}\033[0m')
  if basepl >= 10:
    print('\033[0;33m', end='')
  print(f'Base: {bases.getcosm(baseinuse, basepl)}{baseinuse.name}, {basepl}\033[0m')
  print(f'Base health: {userdata["basehealth"]}/{baseinuse.health*basepl}')
  if not prechosen:
    cho = input('[1]Come out of base\n[2]Switch Hero\n[3]Upgrade Hero\n[4]Switch base\n[5]Upgrade base\n[6]Heal base\n[7]Shop\n[8]Exit\n')
  else:
    prechosen = False
  if cho == '1':
    bacho = ''
    stage = 0
    room = 1
    currweapon = weapons.weapons[heroinuse.weapon]
    energy = heroinuse.energy + ((pl-1)*50)
    while bacho != 'e':
      enemy = enemys.grabenemy()
      enmhealth = enemy.health + stage
      health = heroinuse.health + (pl-1)*2
      skillcdat = 0
      skilldurat = 0
      stuck = False
      stickleft = 0
      stung = False
      stingleft = 0
      stingdamage = 0
      enmstuck = False
      enmstickleft = 0
      enmstung = False
      enmstingleft = 0
      enmstingdamage = 0
      try:
        skilldur = heroinuse.skill.dur
      except AttributeError:
        skilldur = 0
      print(f'You encountered a(n) {enemy.name}!')
      continu()
      while enmhealth > 0 and health > 0 and bacho != 'e':
        os.system('clear')
        print(f'Level {stage+1}-{room}')
        if stuck:
          print('You\'re stuck!')
          print(f'Time left: {stickleft}/{enemy.sticktime}')
        if stung:
          print('You\'ve been stung!')
          print(f'Time left: {stingleft}/{enemy.stingtime}')
          print(f'{stingdamage} damage per turn')
        print(f'{enemy.name} health: {enmhealth}')
        print(f'❤️  \033[31mHealth: {health}/{heroinuse.health + (pl-1)*2}\033[0m')
        print(f'⚡ \033[34mEnergy: {energy}/{heroinuse.energy + (pl-1)*50}\033[0m')
        print(f'Weapon: {currweapon.name}')
        if skilldurat > 0:
          print(f'Skill duration: {skilldurat}/{skilldur}')
        elif skillcdat <= heroinuse.skill.cd and skillcdat != 0:
          print(f'Skill cooldown: {skillcdat}/{heroinuse.skill.cd}')
        if not stuck:
          promptstr = '[a]Attack'
          if skillcdat == 0 and skilldurat == 0:
            promptstr += '\n[s]Skill'
          promptstr += '\n[d]Dodge'
          promptstr += '\n[b]Barehand'
        if stuck:
          promptstr = '[c]Continueee'
        promptstr += '\n[e]Exit'
        bacho = input(promptstr + '\n')
        print(heros.getcosm(heroinuse, pl), end='')
        if bacho == 'a' and not stuck:
          if skillcdat > 0 and skilldurat == 0:
            skillcdat -= 1
          if skilldurat > 0:
            skilldurat -= 1
            skillingdata = heroinuse.skill.skilling(currweapon, pl)
            if skillingdata['energyused'] > energy:
              print('Not enought energy')
            else:
              if skillingdata['damage'] != 0:
                enmhealth -= skillingdata['damage']
                print(f'{skillingdata["damage"]} damage')
              if skillingdata['energyused'] != 0:
                energy -= skillingdata['energyused']
                print(f'You used {skillingdata["energyused"]} energy')
              if heroinuse.skill.canstick:
                print(f'You stuck the {enemy.name}!')
                enmstuck = True
                enmstickleft = heroinuse.skill.sticktime
              if heroinuse.skill.cansting:
                print(f'You stung the {enemy.name}!')
                enmstung = True
                enmstingleft = heroinuse.skill.stingtime
                enmstingdamage = heroinuse.skill.stingdamage
          else:
            if currweapon.energy > energy:
              print('Not enough energy')
            else:
              if randprob(currweapon.accuracy):
                if randprob(currweapon.crit.chance):
                  enmhealth -= currweapon.crit.damage
                  print(f'Critical hit! You dealt {currweapon.crit.damage} damage!')
                  if currweapon.canstick:
                    print(f'You stuck the {enemy.name}!')
                    enmstuck = True
                    enmstickleft = currweapon.sticktime
                  if currweapon.cansting:
                    print(f'You stung the {enemy.name}!')
                    enmstung = True
                    enmstingleft = currweapon.stingtime
                    enmstingdamage = currweapon.stingdamage
                else:
                  enmhealth -= currweapon.damage
                  print(f'You dealt {currweapon.damage} damage!')
                energy -= currweapon.energy
              else:
                print('You missed :(')
          if heroinuse.meleebuff and currweapon.barehandable:
            enmhealth -= 1
            print('You dealt an extra 1 damage with your barehand buff!')
            bacho = 'd'
        elif bacho == 's' and skillcdat == 0 and skilldurat == 0 and not stuck:
          skillusedinfo = heroinuse.skill.skill(currweapon, pl)
          if skillusedinfo:
            if skillusedinfo['energyused'] > energy:
              print('Not enought energy')
            else:
              if skillusedinfo['damage'] != 0:
                enmhealth -= skillusedinfo['damage']
                print(f'{skillusedinfo["damage"]} damage')
              if skillusedinfo['energyused'] != 0:
                energy -= skillusedinfo['energyused']
                print(f'You used {skillusedinfo["energyused"]} energy')
              if heroinuse.canstick:
                print(f'You stuck the {enemy.name}!')
                enmstuck = True
                enmstickleft = heroinuse.sticktime
              if heroinuse.cansting:
                print(f'You stung the {enemy.name}!')
                enmstung = True
                enmstingleft = heroinuse.stingtime
                enmstingdamage = heroinuse.stingdamage
              skilldurat = skilldur
              skillcdat = heroinuse.skill.cd
        elif bacho == 'd' and not stuck:
          if skillcdat > 0:
            skillcdat -= 1
        elif bacho == 'b' and not stuck:
          if currweapon.barehandable:
            if currweapon.energy <= energy:
              energy -= currweapon.energy
              enmhealth -= currweapon.damage
              print(f'You dealt {currweapon.damage} damage!')
            else:
              enmhealth -= currweapon.damage - 1
              print(f'You dealt {currweapon.damage-1} damage!')
              bacho = 'd'
          else:
            enmhealth -= 3
            print('You dealt 3 damage!')
            bacho = 'd'
          if heroinuse.meleebuff:
            print('You dealt an extra 1 damage with your barehand buff!')
            enmhealth -= 1
        elif bacho == 'c' and stuck:
          print('Continueingg')
          stickleft -= 1
          if stickleft == 0:
            stuck = False
        elif bacho == 'e':
          if userdata['basehealth'] <= 0:
            if stage >= basepl/2:
              userdata['basehealth'] = baseinuse.health*basepl
            else:
              print('You can\'t exit yet...')
              bacho = ''
          else:
            pass
          print('\033[0m')
          continu()
          continue
        if enmstung:
          print('Enemy is stung...')
          print(f'The {enemy.name} took {enmstingdamage} damage from the sting!')
          enmhealth -= enmstingdamage
          enmstingleft -= 1
          if enmstingleft == 0:
            enmstung = False
        continu()
        print('\033[0m', end='')
        if enmstuck:
          print('Enemy is stuck...')
          print(f'Turns left: {enmstickleft}')
          enmstickleft -= 1
          if enmstickleft == 0:
            enmstuck = False
        if randprob(1 if bacho == 'd' else enemy.accuracy) and not enmstuck:
          if randprob(enemy.crit.chance):
            health -= enemy.crit.damage + stage
            print(f'The {enemy.name} crit you({enemy.crit.damage + stage} dmg)!')
            if enemy.canstick:
              stuck = True
              stickleft = enemy.sticktime
              print(f'The {enemy.name} stuck you!')
            if enemy.cansting:
              stung = True
              stingleft = enemy.stingtime
              stingdamage = enemy.stingdmg
              print(f'The {enemy.name} stung you!')
          else:
            health -= enemy.damage + stage
            print(f'The {enemy.name} hit you({enemy.damage + stage} dmg)!')
        else:
          if not enmstuck:
            print('Enemy missed.')
        if stung:
          health -= enemy.stingdmg
          print(f'{enemy.stingdmg} dmg from the sting!')
          stingleft -= 1
          if stingleft == 0:
            stung = False
        continu()
      if enmhealth <= 0:
        print('Enemy died.')
        userdata['coins'] += 5 + stage
        print(f'You gained {5+stage} coins.')
        if room == 2:
          print('Chest room!')
          openchest = input('Open chest[o]?:')
          if openchest == 'o':
            coinsinchest = rand.randint(stage+room, stage*3+room)
            print(f'• You got {coinsinchest} coins')
            userdata['coins'] += coinsinchest
            energyinchest = rand.randint(stage+room, stage*3+room)
            print(f'• You got {energyinchest} energy')
            energy += energyinchest
            droppedweapon = rand.choice(list(weapons.weapons.keys()))
            while weapons.weapons[droppedweapon].name == currweapon.name:
              droppedweapon = rand.choice(list(weapons.weapons.keys()))
            print('You found a(n)', weapons.weapons[droppedweapon].name+'!')
            dopickupweapon = input('Pick it up[p]?')
            if dopickupweapon == 'p':
              currweapon = weapons.weapons[droppedweapon]
        room += 1
        energy += stage
        if energy > heroinuse.energy + (pl-1)*50:
          energy = heroinuse.energy + (pl-1)*50
        if room == 4:
          room = 1
          stage += 1
        continu()
      if health <= 0:
        print('you died...')
        continu()
        bacho = 'e'
        continue
  elif cho == '2':
    print('All heroes:')
    allheroes = userdata['heroes']
    allheronames = [heros.heros[hero].name for hero in allheroes]
    print(', '.join(allheronames))
    choice = input('Select:\n').lower().replace(' ', '')
    if choice not in userdata['heroes']:
      print('Not a hero')
      continu()
    else:
      userdata['hero'] = choice.lower().replace(' ', '')
  elif cho == '3':
    if pl >= 12:
      print('Hero is maxed')
      continu()
      continue
    print('Your hero: ' + heroinuse.name)
    print(f'Power {pl}')
    upgrade = input(f'Upgrade[u] for {pl*25} coins?: ')
    if upgrade == 'u':
      if userdata['coins'] >= pl*25:
        userdata['coins'] -= pl*25
        userdata["heroes"][userdata["hero"]] += 1
      else:
        print('Not enough coins')
        continu()
  elif cho == '4':
    print('All bases:')
    allbases = userdata['bases']
    allbasenames = [bases.bases[base].name for base in allbases]
    print(', '.join(allbasenames))
    choice = input('Select:\n').lower().replace(' ', '')
    if choice not in userdata['bases']:
      print('Not a base')
      continu()
    else:
      userdata['base'] = choice.lower().replace(' ', '')
    basehealthpercent = userdata['basehealth'] / (baseinuse.health*basepl)
    userdata['basehealth'] = int(basehealthpercent * (bases.bases[userdata['base']].health*basepl))
  elif cho == '5':
    if basepl >= 12:
      print('Base is maxed')
      continu()
      continue
    print('Your base: ' + baseinuse.name)
    print(f'Power {basepl}')
    upgrade = input(f'Upgrade[u] for {userdata["bases"][userdata["base"]]*25} coins?: ')
    if upgrade == 'u':
      if userdata['coins'] >= basepl*25:
        userdata['coins'] -= basepl*25
        userdata["bases"][userdata["base"]] += 1
      else:
        print('Not enough coins')
        continu()
  elif cho == '6':
    baseheal = input('How much do you want to heal your base?: ')
    basehealisint = True
    try:
      int(baseheal)
    except:
      print('Not a number')
      basehealisint = False
      continue
    if basehealisint:
      for i in range(0, int(baseheal)):
        if userdata['basehealth'] >= baseinuse.health*basepl:
          userdata['basehealth'] = baseinuse.health*basepl
          print('Fully healed')
          continu()
          break
        if userdata['coins'] <= 0:
          userdata['coins'] = 0
          print(f'Not enough coins, healed as much as possible({i} points)')
          continu()
          break
        userdata['basehealth'] += 1
        userdata['coins'] -= 1
  elif cho == '7':
    print('Shop')
    allheroes = list(heros.heros.keys())
    def filterheroes(heroname):
      return not heroname in userdata['heroes']
    allheroesnew = list(filter(filterheroes, allheroes))
    heronamesandcosts = [f'{heros.heros[hero].name}({heros.heros[hero].cost}, Hero)' for hero in allheroesnew]
  
    allbases = list(bases.bases.keys())
    def filterbases(basename):
      return not basename in userdata['bases']
    allbasesnew = list(filter(filterbases, allbases))
    basenamesandcosts = [f'{bases.bases[base].name}({bases.bases[base].cost}, Base)' for base in allbasesnew]

    fullshop = heronamesandcosts + basenamesandcosts
    if fullshop == []:
      continue
    print(', '.join(fullshop))
    shopchoice = input('Select(enter/return to exit):\n').lower()
    shopchoiceid = shopchoice.replace(' ', '')
    if shopchoice.lower() in [heros.heros[x].name.lower() for x in allheroesnew]:
      if userdata['coins'] >= heros.heros[shopchoiceid].cost:
        userdata['coins'] -= heros.heros[shopchoiceid].cost
        userdata['heroes'][shopchoiceid] = 1
    elif shopchoice.lower() in [bases.bases[x].name.lower() for x in allbasesnew]:
      if userdata['coins'] >= bases.bases[shopchoiceid].cost:
        userdata['coins'] -= bases.bases[shopchoiceid].cost
        userdata['bases'][shopchoiceid] = 1
    else:
      print('Not in the shop!')
      continu()
  elif cho == '8':
    print('Saved')
    run = 0
    continue
  if randprob(5) and (cho not in ['4', '5', '6']):
    enemy = enemys.grabenemy()
    print(f'A {enemy.name} came!')
    userdata['basehealth'] -= enemy.damage+basepl
    print(f'Your base took {enemy.damage+basepl} damage')
    if userdata['basehealth'] <= 0:
      userdata['basehealth'] = 0
      prechosen = True
      cho = '1'
      print('Your base was knocked out...')
    continu()
  save()
