buildingtypes = {}
grass = '\x1b[48;2;0;255;0m'
class Building:
  def __init__(self, type, name, func, look, cost, health, otherdata):
    self.type = type
    self.name = name
    self.function = func
    self.look = look
    self.cost = cost
    self.health = health
    self.otherdata = otherdata
    buildingtypes[name] = self

vhalcol = '\x1b[48;2;255;104;62m'
def nofunc(troop):
  pass
Building('villagehall', 'village hall', nofunc, [vhalcol+'^',vhalcol+'|',vhalcol+'-',vhalcol+'-'], 0, 200, {})

def cannonfunc(troop):
  pass
Building('defense', 'cannon', cannonfunc, ['\x1b[48;2;150;150;150mo',grass+'-',grass+'|',grass+'|'], 10, 75, {'damage':20})

def arrowtowerfunc(troop):
  pass
Building('defense', 'arrow tower', arrowtowerfunc, ['\x1b[48;2;171;142;0m<',grass+'-',grass+'|',grass+'|'], 15, 100, {'damage':25})
# double list indexing format is list[y][x]