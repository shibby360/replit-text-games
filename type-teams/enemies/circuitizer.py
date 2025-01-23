damage = 60
health = 210
def copy(name):
  return type(name, (), {'damage':damage, 'health':health})