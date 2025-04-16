rawoppname = input('Opponent?: ')
if rawoppname == '':
  rawoppname = 'Evil drak'
opphealth = int(input('Opponent health?: '))
oppmedhealth = opphealth + int('1' + str('0' * (len(str(opphealth)) - 1)))
oppblindedness = 0
opprockness = 0
oppbravery = round(opphealth/2)
if oppbravery > 100:
  oppbravery = 100
opponent = '\x1b[1m'+rawoppname+'\x1b[0m'
health = int(input('Your health?: '))
medhealth = health + int('1' + str('0' * (len(str(health)) - 1)))
class light:
  spec_effect = 'blind'
  def norm(power):
    print(opponent + ' has been blinded for ' + str(power * 2) + ' seconds and taken ' + str(power) + ' damage.')
    global opphealth
    global oppblindedness
    opphealth -= power
    oppblindedness += power * 2
  def air(power, amount):
    print('You released ' + str(amount) + ' air.')
    global opphealth
    global oppblindedness
    global health
    opphealth -= power
    if power >= 40:
      oppblindedness += amount
      print(opponent + ' has been blinded for ' + str(amount) + ' seconds.')
    if power >= 100:
      health += amount
      print('You healed ' + str(amount) + ' health.')
  def sun(timeofday, weather='sunny', onsun=False):
    #Time of day values: morning, afternoon, evening, night
    #Weather values: sunny, cloudy, rainy
    global opphealth
    global oppblindedness
    global oppmedhealth
    if onsun:
      opphealth -= (opphealth - 20)
      oppmedhealth -= (oppmedhealth - 20)
    else:
      if weather == 'sunny':
        if timeofday not in ['morning', 'afternoon', 'evening', 'night']:
          raise ValueError('Time of day not supported. Use morning, afternoon, evening, or night')
        print(opponent + ' has taken ', end='')
        if timeofday == 'morning':
          print(150, end=' ')
          opphealth -= 150
          oppblindedness += 75
        elif timeofday == 'afternoon':
          print(200, end=' ')
          opphealth -= 200
          oppblindedness += 100
        elif timeofday == 'evening':
          print(100, end=' ')
          opphealth -= 100
          oppblindedness += 50
        elif timeofday == 'night':
          print(0, end=' ')
          opphealth -= 0
          oppblindedness -= 0
        print('damage.')
      elif weather == 'cloudy':
        print('The sun is not out!')
      elif weather == 'rainy':
        print('It\'s raining!')
        water.norm(20)
  def medicine(power, amount):
    print('You realeased ' + str(amount) + ' medicine.')
    print('You have healed ' + str(power * 2) + '.')
    global health
    health += power
    if power >= 90:
      print('You got ' + str(amount * 2) + ' medical health.')
      global medhealth
      medhealth += amount
  def life():
    global health
    global medhealth
    print('You gained ' + str(health + (health * 0.5)) + ' health.')
    print('You gained ' + str(medhealth + (medhealth * 0.5)) + ' medical health.')
    health += health * 0.5
    medhealth += medhealth * 0.5
  elements = ['air', 'sun', 'medicine', 'life']
  def spec(power):
    print('You specialed ' + opponent + '.')
    subber = int('1' + ('0' * len(str(power))))
    global opphealth
    global oppmedhealth
    global oppblindedness
    opphealth -= (subber - power)
    oppmedhealth -= (subber - power) * 2
    oppblindedness += power
  def super(power):
    global oppblindedness
    print('You supered ' + opponent + '.')
    oppblindedness += power * 4
    light.air(power, 300)
    light.sun('afternoon')
  eles = [air, sun, medicine, life]
class dark:
  spec_effect = 'stone'
  def norm(power):
    print(opponent + ' has been turned to stone with rock levels of ' + str(power * 2) + '. ' + opponent + ' has also taken ' + str(power) + ' damage.')
    global opphealth
    global opprockness
    opphealth -= power
    opprockness += power * 2
  def smoke(power, amount):
    print('You realeased ' + str(amount) + ' smoke.')
    print(opponent + ' has taken ' + str(power) + ' damage.')
    global opphealth
    opphealth -= power
    if power >= 70:
      print(opponent + ' lost ' + str(amount) + ' medical health.')
      global oppmedhealth
      oppmedhealth -= amount
  def moon(onmoon=False):
    print(opponent + ' took 150 damage.')
    global opphealth
    opphealth -= 150
    if onmoon:
      print(opponent + ' lost 150 medical health.')
      global oppmedhealth
      oppmedhealth -= 150
  def venom(power, amount):
    print('You realeased ' + str(amount) + ' venom.')
    print(opponent + ' has taken ' + str(power * 2) + ' damage.')
    global opphealth
    opphealth -= power
    if power >= 130:
      print(opponent + ' lost ' + str(amount * 2) + ' medical health.')
      global oppmedhealth
      oppmedhealth -= amount
  def ghost():
    print(opponent + ' has been haunted.')
    global opphealth
    global oppbravery
    tax = (0.5 * opphealth)
    if tax < 200:
      tax = 200
    if tax > 500:
      oppbravery -= 10
    opphealth -= tax - oppbravery
    global oppmedhealth
    medtax = (0.3 * oppmedhealth)
    if medtax < 400:
      medtax = 400
    oppmedhealth -= medtax - oppbravery
  elements = ['smoke', 'moon', 'venom', 'ghost']
  def spec(power):
    print('You specialed ' + opponent + '.')
    subber = int('1' + ('0' * len(str(power))))
    global opphealth
    global oppmedhealth
    global opprockness
    opphealth -= (subber - power)
    oppmedhealth -= (subber - power) * 2
    opprockness += power
  def super(power):
    global opprockness
    print('You supered ' + opponent + '.')
    opprockness += power * 4
    dark.smoke(power, 3000)
    dark.moon(True)
class flower:
  def norm(power):
    global opphealth
    global oppmedhealth
    print('Flower Power!')
    
class fire:
  def norm(power):
    if power > 15:
      raise ValueError('Too much power.')
    global opphealth
    print('You burned ' + opponent + '.')
    opphealth -= power * 5
  def heat(power):
    if power > 15:
      raise ValueError('Too much power.')
    print('You made it hot!')
    global opphealth
    opphealth -= power
  def ember(power):
    if power > 100:
      raise ValueError('Too much power.')
    print('Ember attack!')
    global opphealth
    opphealth -= (power / 5) * 3
  def spec(power):
    if power > 30:
      raise ValueError('Too much power.')
    global opphealth
    global oppmedhealth
    opphealth -= power * 4
    oppmedhealth -= power * 2
  comps = ['heat', 'ember']
class water:
  def norm(power):
    if power > 20:
      raise ValueError('Too much power.')
    global opphealth
    print('You washed ' + opponent + '.')
    opphealth -= power + 100
  def cool(power):
    if power > 20:
      raise ValueError('Too much power.')
    print('You made it cold!')
    global opphealth
    global opprockness
    opphealth -= power
    opprockness += 10
  def spec(power):
    if power > 40:
      raise ValueError('Too much power.')
    global opphealth
    global oppmedhealth
    opphealth -= power * 4 + 100
    oppmedhealth -= power * 2 + 100
  comps = ['cool']
class earth:
  def norm(power):
    if power > 25:
      raise ValueError('Too much power.')
    print('Earth Slam!')
    global opphealth
    opphealth -= 100 + power
  def breaker(power):
    if power < 15 or power > 30:
      raise ValueError('Invalid power.')
    print('BREAKER!!!')
    global opphealth
    opphealth -= 100 + power * 5
  def spec(power):
    if power > 50:
      raise ValueError('Too much power.')
    print('Earth power!')
    global opphealth
    global opprockness
    opphealth -= power * 6 + 500
    opprockness += power
  comps = ['breaker']
class opp:#Aka normal dude
  def atk():
    global health
    health -= 250
  def inc_dfns():
    global opphealth
    opphealth += 200
  def medatk():
    global medhealth
    medhealth -= 150
  def med_dfns():
    global oppmedhealth
    oppmedhealth += 100
def sonar(who):
  if who == 'me':
    stats = {
      'health':health, 
      'medical health':medhealth
    }
  if who == 'opp':
    stats = {
      'name':rawoppname,
      'health':opphealth,
      'medical health':oppmedhealth,
      'blindedness':oppblindedness,
      'rockness':opprockness,
      'bravery':oppbravery
    }
  return stats

def battle():
  global medhealth
  global oppmedhealth
  while oppmedhealth > 0 and medhealth > 0:
    cmd = input('What attack?: ')
    eval(cmd)
    if opprockness >= 5000:
      print('Opponent is pure stone! You crack it!')
      break
    if oppblindedness >= 5000:
      print('Opponent\'s vision is gone! You kill it!')
      break
    if health <= 0:
      medhealth -= 10
    if opphealth <= 0:
      oppmedhealth -= 10
    if oppbravery <= 0:
      oppmedhealth -= 5
    if 'sonar' not in cmd:
      opp.atk()
      opp.inc_dfns()
      opp.medatk()
      opp.med_dfns()
    else:
      print(eval(cmd))
  if oppmedhealth <= 0:
    print('Opponent died.')
  if medhealth <= 0:
    print('You died.')