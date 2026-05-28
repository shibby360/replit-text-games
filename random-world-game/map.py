from replit import db
import numpy
maps = db['maps']
#map key
#u = user
#t = tree
#c = chest
#s = skeleton
#p = pirate
def save():
  db['maps'] = maps
def addkeytomap():
  pass
def add_new_map(usrname):
  maps[usrname] = numpy.zeros((10, 10)).tolist()
  map = maps[usrname]
  for i in range(len(map)):
    for j in range(len(map[i])):
      map[i][j] = {'item':'-', 'island':'none'}
  map[0][0]['item'] = 'u'
  map[0][0]['island'] = 'first'
  map[0][1]['item'] = 't'
  map[0][1]['island'] = 'first'
  maps[usrname] = map
  db['maps'] = maps