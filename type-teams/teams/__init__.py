class Guy:
  def __init__(self, name, ability, damage, health, role):
    self.name = name
    self.ability = ability
    self.damage = damage
    self.health = health
    self.data = self.__dict__
    self.role = role
  def copy(self, name):
    return type(name, (), self.__dict__)
class Master:
  def __init__(self, *mems):
    self.mems = mems
    self.memdict = {}
    for mem in mems:
      self.memdict[mem.name] = mem
    self.offenders = {}
    for mem in mems:
      if mem.role == 'Offense':
        self.offenders[mem.name] = mem
    self.supports = {}
    for mem in mems:
      if mem.role == 'Support':
        self.supports[mem.name] = mem
    self.medic = {}
    for mem in mems:
      if mem.role == 'Medic':
        self.medic['Medic'] = mem