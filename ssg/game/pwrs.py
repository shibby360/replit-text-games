class Power:
  def __init__(self, name, basepatr):
    self.name = name
    self.basepatr = basepatr
    self.damage = basepatr.max_damage*2