trooptypes = {}
class Troop:
  def __init__(self, name, func, health, damage, cost, otherdata):
    self.name = name
    self.func = func
    self.health = health
    self.damage = damage
    self.cost = cost
    self.otherdata = otherdata
    trooptypes[name] = self

def knightfunc(opponent):
  pass
Troop('knight', knightfunc, 20, 10, 1, {})