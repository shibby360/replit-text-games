damage = 70
health = 200
def copy(name):
  return type(name, (), {'damage':damage, 'health':health})