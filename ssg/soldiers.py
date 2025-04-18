#Soldier Name : Soldier Level
def upgrade(who):
  if soldiers[who] != 4:  
    soldiers[who] += 1
  else:
    print('Not upgradeable')
def unlock(who):
  if soldiers[who] == 0:
    soldiers[who] = 1
  else:
    print('Already Unlocked')
#10 points to lvl 2, 20 points to 3, 30 points to 4
'''
Earnings:
Level 1: Base; Nothing
Level 2: Soldier Power
Level 3: Brownja Energy
Level 4: Brownja Energy and Weapon
'''
#Point cost is that many coins
def init(self, __):
  self.__ = __
soldiers = {
  'Dark':0,
  'Shade':0,
  'Shapeshift':0,
  'Night mult':0,
  'Dim':0,
  'Obscurer':0,
  'Copy':0,
  '2D':0,
  'Fake Attack':0,
  'Elongate':0,
  '__init__':init
}
unlock('Dark')
for i in range(0, 3):
  upgrade('Dark')