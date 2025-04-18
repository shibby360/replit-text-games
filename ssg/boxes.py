import random as r
def appends(list, one_over):
  for i in range(0, one_over):
    list.append(True)
  for i in range(0, 100-one_over):
    list.append(False)
    
patrs = ['Blake', 'Brownja', 'Tobgat', 'Eulb', 'Eulb Krad', 'Purpy', 'Pinky', 'Relood', 'Ora', 'Yeller']

ihv = ['Relood']

for i in patrs:
  for j in ihv:
    if i == j:
      patrs.remove(i)

a = input('What do you want?: ')
if 'Battle' == a or 'b' == a:
  class patrs:
    og = ['Blake', 'Brownja', 'Tobgat', 'Eulb', 'Eulb Krad', 'Purpy', 'Pinky', 'Relood', 'Ora', 'Yeller']
  print('You are against: ' + r.choice(patrs.og))
elif 'Chest' == a or 'c' == a:
  b = input('Which chest?: ')
  if b == 'Villager' or b == 'v':
    print(r.randint(10, 20), 'coins')
    print(r.randint(0, 10), 'energy')
    print(r.randint(50, 60), 'health')
    print('Bonuses: ')
    keys = r.choice([True, False, False, False, False, False, False, False, False, False])
    if keys:
      print('2 keys')
    charchance = []
    appends(charchance, 20)
    charchance = r.choice(charchance)
    if charchance:
      print('You got: ' + r.choice(patrs))
  elif b == 'Soldier' or b == 's':
    print(r.randint(20, 30), 'coins')
    print(r.randint(10, 20), 'energy')
    print(r.randint(60, 70), 'health')
    print('Bonuses: ')
    keys = r.choice([True, True, False, False, False, False, False, False, False, False])
    if keys:
      print('4 keys')
    charchance = []
    appends(charchance, 15)
    charchance = r.choice(charchance)
    if charchance:
      print('You got: ' + r.choice(patrs))
  elif b == 'Patriot' or b == 'p':
    print(r.randint(30, 40), 'coins')
    print(r.randint(20, 30), 'energy')
    print(r.randint(70, 80), 'health')
    print('Bonuses: ')
    keys = r.choice([True, True, True, False, False, False, False, False, False, False])
    if keys:
      print('6 keys')
    charchance = []
    appends(charchance, 10)
    charchance = r.choice(charchance)
    if charchance:
      print('You got: ' + r.choice(patrs))
    gems = r.choice([True, False, False, False, False, False, False, False, False, False])
    if gems:
      print(r.randint(5, 10), 'gems')
  elif b == 'King' or b == 'k':
    print(r.randint(40, 50), 'coins')
    print(r.randint(30, 40), 'energy')
    print(r.randint(80, 90), 'health')
    print('Bonuses: ')
    keys = r.choice([True, True, True, True, False, False, False, False, False, False])
    if keys:
      print('8 keys')
    charchance = []
    appends(charchance, 5)
    charchance = r.choice(charchance)
    if charchance:
      print('You got: ' + r.choice(patrs))
    gems = r.choice([True, True, False, False, False, False, False, False, False, False])
    if gems:
      print(r.randint(15, 20), 'gems')
  elif b == 'Element' or b == 'e':
    print(r.randint(100, 200), 'coins')
    print(r.randint(80, 160), 'energy')
    print(r.randint(180, 360), 'health')
    print('Bonuses: ')
    keys = r.choice([True, True, True, True, True, True, True, False, False, False])
    if keys:
      print('32 keys')
    print('You got: ' + r.choice(patrs))
    gems = r.choice([True, True, True, True, True, False, False, False, False, False])
    if gems:
      print(r.randint(40, 80), 'gems')