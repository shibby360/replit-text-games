class Sword:
  def __init__(self, plydata):
    data = dict(plydata).copy()
    self.damage = data['level'] * 3
sories = {
  'sword':Sword
}