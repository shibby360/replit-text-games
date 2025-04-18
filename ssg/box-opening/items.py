r = __import__('random')
def appends(list, percent):
  for i in range(0, percent):
    list.append(True)
  for i in range(0, 100-percent):
    list.append(False)
#a = input('What do you want?: ')
nchest = {'chest':'n', 'cost':0, 'unit':'coins'}
vchest = {'chest':'v', 'cost':40, 'unit':'coins'}
schest = {'chest':'s', 'cost':80, 'unit':'coins'}
pchest = {'chest':'p', 'cost':160, 'unit':'coins'}
kchest = {'chest':'k', 'cost':40, 'unit':'gems'}
echest = {'chest':'e', 'cost':160, 'unit':'gems'}
chests = [nchest, vchest, schest, pchest, kchest, echest]
def SSGer(a, b=False, ihv=[]):
  class patrs:
    og = ['Blake', 'Brownja', 'Tobgat', 'Eulb', 'Eulb Krad', 'Purpy', 'Pinky', 'Relood', 'Ora', 'Yeller']
  for i in patrs.og:
    for j in ihv:
      if i == j:
        patrs.og.remove(i)
  if 'Battle' == a or 'b' == a:
    print('You are against: ' + r.choice(patrs.og))
  elif 'Chest' == a or 'c' == a:
    if not b:
      b = input('Which chest?: ')
    if b == 'Normal' or b == 'n':
      cnsstrt = 0
      cnsend = 10
      enrgystrt = 0
      enrgyend = 10
      hlthstrt = 40
      hlthend = 50
      keyslist = [False, False, False, False, False, False, False, False, False, False]
      keyamount = 0
      charchance_percent = 0
    elif b == 'Villager' or b == 'v':
      cnsstrt = 10
      cnsend = 20
      enrgystrt = 0
      enrgyend = 10
      hlthstrt = 50
      hlthend = 60
      keyslist = [True, False, False, False, False, False, False, False, False, False]
      keyamount = 2
      charchance_percent = 5
    elif b == 'Soldier' or b == 's':
      cnsstrt = 20
      cnsend = 30
      enrgystrt = 10
      enrgyend = 20
      hlthstrt = 60
      hlthend = 70
      keyslist = [True, True, False, False, False, False, False, False, False, False]
      keyamount = 4
      charchance_percent = 7
    elif b == 'Patriot' or b == 'p':
      cnsstrt = 30
      cnsend = 40
      enrgystrt = 20
      enrgyend = 30
      hlthstrt = 70
      hlthend = 80
      keyslist = [True, True, True, False, False, False, False, False, False, False]
      keyamount = 6
      charchance_percent = 10
      gemchance = [True, False, False, False, False, False, False, False, False, False]
      gems1 = 5
      gems2 = 10
    elif b == 'King' or b == 'k':
      cnsstrt = 40
      cnsend = 50
      enrgystrt = 30
      enrgyend = 40
      hlthstrt = 80
      hlthend = 90
      keyslist = [True, True, True, True, False, False, False, False, False, False]
      keyamount = 8
      charchance_percent = 20
      gemchance = [True, True, False, False, False, False, False, False, False, False]
      gems1 = 15
      gems2 = 20
    elif b == 'Element' or b == 'e':
      cnsstrt = 100
      cnsend = 200
      enrgystrt = 80
      enrgyend = 160
      hlthstrt = 180
      hlthend = 360
      keyslist = [True, True, True, True, True, True, True, False, False, False]
      keyamount = 8
      charchance_percent = 100
      gemchance = [True, True, True, True, True, False, False, False, False, False]
      gems1 = 40
      gems2 = 80
    end = {}
    print(cns := r.randint(cnsstrt, cnsend), 'coins')
    print(enrgy := r.randint(enrgystrt, enrgyend), 'energy')
    print(hlth := r.randint(hlthstrt, hlthend), 'health')
    end['coins'] = cns
    end['energy'] = enrgy
    end['health'] = hlth
    print('Bonuses: ')
    keys = r.choice(keyslist)
    if keys:
      print(f'{keyamount} keys')
      end['keys'] = keyamount
    charchance = []
    appends(charchance, charchance_percent)
    charchance = r.choice(charchance)
    if charchance:
      print('You got: ' + (patr := r.choice(patrs.og)))
      end['Patriot'] = [patr]
    if b in ['Patriot', 'King', 'Element'] or b in ['p', 'k', 'e']:
      gems = r.choice(gemchance)
      if gems:
        print(gemsgot := r.randint(gems1, gems2), 'gems')
        end['gems'] = gemsgot
    return end

def checkchest(chest):
  if len(chest) == 0:
    return nchest 
  elif len(chest) == 1:
    end = chest
  else:
    end = chest[0].upper()
  for i in chests:
    if i['chest'] == end:
      return i