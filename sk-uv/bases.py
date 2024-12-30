class shack:
  name = 'Shack'
  health = 25
  # damage = 25
  l1cosm = '\033[38;2;210;180;140m'
  l2cosm = '🛖  '
class house:
  name = 'House'
  health = 50
  # damage = 100
  cost = 50
  l1cosm = '\033[38;2;203;190;181m'
  l2cosm = '🏠 '
bases = {
  'shack':shack,
  'house':house
}
def getcosm(base, pl):
  cosm = ''
  if type(base) == str:
    base = bases[base]
  if pl >= 11:
    cosm += base.l1cosm
  if pl >= 12:
    cosm += base.l2cosm
  return cosm