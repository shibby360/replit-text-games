"""
A module to make avatars and put them in locations, or sort of model real life situatons.
"""
#¯
os = __import__('os')
r = __import__('random')
time = __import__('time')
class Player():
  """
  Create a new player object.\n
  `name`: Name of player.\n
  `b_s_h_lvls`: Must be a list. First element is basketball level, second is soccer level, and third is hockey level.\n
  `speed`: Must be an integer.\n
  `head`: Must be a Appearance.Heads object.\n
  `body`: Must be a Appearance.Bodies object.\n
  `legs`: Must be a Appearance.Legs object.\n
  `accessory`: Must be a Appearance.Accessories object.\n
  `gender`: Specify 'boy' or 'girl'.\n
  """
  def __init__(self, name='', nickname='', b_s_h_lvls=[0, 0, 0], speed=0, head='', body='', legs='', accessory=None, gender='', avatar=''):
    self.personality = ''
    self.name = name
    self.nickname = nickname
    self.basket_lvl, self.soccer_lvl, self.hockey_lvl = b_s_h_lvls
    self.speed = speed
    if avatar == '':
      self.look = 'spce' + head + '\n' + body + 'ha\nspce' + legs + 'la'
      if len(body) == 5:
        self.look = self.look.replace('spce', ' ')
      else:
        self.look = self.look.replace('spce', '')
      if accessory != None:
        if accessory.type == 'hands':
          self.look = self.look.replace('ha', accessory.item)
          self.look = self.look.replace('la', '')
        if accessory.type == 'feet':
          self.look = self.look.replace('la', accessory.item)
          self.look = self.look.replace('ha', '')
      else:
        self.look = self.look.replace('ha', '')
        self.look = self.look.replace('la', '')
    else:
      self.look = avatar
    if body == Appearance.Bodies.tall:
      self.basket_lvl += 2
    if gender.lower() == 'boy':
      self.gen_noun = 'He'
    if gender.lower() == 'girl':
      self.gen_noun = 'She'
  def upgrade(self, sport, howmuch):
    sport = sport.lower()
    if sport == 'basketball':
      self.basket_lvl += howmuch
    elif sport == 'soccer':
      self.soccer_lvl += howmuch
    elif sport == 'hockey':
      self.hockey_lvl += howmuch
    return self
  def display(self):
    if self.gen_noun == 'He':
      gender = 'Boy'
    elif self.gen_noun == 'She':
      gender = 'Girl'
    print('''
Name: {0}
Basketball level: {1}
Soccer level: {2}
Hockey level: {3}
Gender: {4}
Nickname: {5}
Avatar: 
{6}
    '''.format(self.name, self.basket_lvl, self.soccer_lvl, self.hockey_lvl, gender, self.nickname, self.look))
  def call(self, place, player):
    place.addPlayer(player)
    return place
  def __str__(self):
    return self.look
  def toDict(self):
    end = self.__dict__
    end['Return to'] = 'Player'
    return end
  def setPersonailty(self):
    def func(f):
      self.personality = f()
    return func
class Appearance:
  """
  The Appearances Library.
  """
  class Heads:
    def __str__(self):
      return self.norm
    norm = ': |'
    talking = ': O'
    bruh = '-_-'
    angry = '>:('
    sad = ': ('
    surprised = 'O.O'
    class emojis:
      monkey = '🐵'
  class Bodies:
    def __str__(self):
      return self.norm
    norm = '\|/'
    fat = '\|_|/'
    tall = ' |\n\|/'
    floppy = '~|~'
  class Legs:
    def __str__(self):
      return self.norm
    norm = '/ \\'
    block = '| |'
  class Accessories:
    class game_controller:
      def __str__(self):
        return self.item
      item = '🎮'
      type = 'hands'
    class soccer_ball:
      def __str__(self):
        return self.item
      item = '⚽'
      type = 'feet'
    class phone:
      def __str__(self):
        return self.item
      item = '📱'
      type = 'hands'
    class basketball:
      def __str__(self):
        return self.item
      item = '🏀'
      type = 'hands'
    class trash:
      def __str__(self):
        return self.item
      item = '🗑'
      type = 'feet'
class Place():
  """
  Create a new place object.\n
  `players`: Must be a list of player objects.\n
  `sport`: Must be a string. Either hockey, soccer, basketball or racing.\n
  `type`: Type of place(Ct, Cir, etc).\n
  `name`: Name of place.\n
  """
  def __init__(self, players=[], sport='', type='', name=''):
    self.players = players
    self.sport = sport.lower()
    self.type = type
    self.name = name
    self.fullname = name + ' ' + type + '.'
  def addPlayer(self, player):
    self.players.append(player)
    return self
  def remPlayer(self, player):
    self.players.remove(player)
    return self
  def changeSport(self, sport):
    self.sport = sport
    return self
  def desertify(self):
    self.players = []
  def __str__(self):
    return self.fullname
  def play_out(self):
    if self.players != []:
      topsym = ''
      topr = ''
      avatar = ''
      for player in self.players:
        os.system('clear')
        topr += player.name + '(aka {})'.format(player.nickname)
        avatar += player.look + '\n'
        print('Setting: ' + self.fullname)
        if self.sport == 'basketball':
          topsym = '''
 _
|_|-O
 |
 |
 |
_|_
          '''
          print(topsym)
          print('\n\n')
          print(avatar)
          print('\n\n')
          if player.basket_lvl <= 3:
            topr += ' shot the 2 and failed. He/She repatedly shoots and failed.newline'
          elif player.basket_lvl > 3 and player.basket_lvl <= 6:
            topr += ' shot the 2 and made! He/She drives out... Goes for the 3... and {}s!newline'.format(r.choice(['misse', 'make']))
          elif player.basket_lvl > 6:
            topr += ' shoots the 3 and makes! He/She goes for another 3 and makes! What a player!newline'
        if self.sport == 'soccer':
          topsym = ' __       __\n/           \\\n|           |'
          print(topsym)
          print('\n\n')
          print(avatar)
          print('\n\n')
          if player.soccer_lvl <= 3:
            topr += ' shoots the closest goal ever... and fails. He gets the ball back... and fails.newline'
          elif player.soccer_lvl > 3 and player.soccer_lvl <= 6:
            topr += ' shoots from a moderate distance... He/She {}s! newline'.format(r.choice(['misse', 'make']))
          elif player.soccer_lvl > 6:
            topr += ' jukes the opossing team, literally breaks their ankles, does a rainbow and makes the most epic shot ever.newline'
        if self.sport == 'hockey':
          topsym = '''
 __        __     \ \n/            \     \ \n|            |      \__ \n
'''
          print(topsym)
          print('\n\n')
          print(avatar)
          print('\n\n')
          if player.hockey_lvl <= 3:
            topr += ' shoots the closest goal ever... and fails. He gets the puck back... and fails.newline'
          elif player.hockey_lvl > 3 and player.hockey_lvl <= 6:
            topr += ' shoots from a moderate distance... He/She {}s!newline '.format(r.choice(['misse', 'make']))
          elif player.hockey_lvl > 6:
            topr += ' jukes the opossing team, literally breaks their ankles, and makes the most epic shot ever.newline'
        if self.sport == 'racing':
          topsym = '''
 _         
| |                    O
| |                    |
| |                    |
| |                    |
| |                    |
|_|                    O
          '''
          print(topsym)
          print('\n\n')
          print(avatar)
          print('\n\n')
          if player.speed <= 3:
            topr += ' is running and miserably lost.newline'
          elif player.speed > 3 and player.speed <= 6:
            topr += ' is running... he is speeding real fast... and got {}th place!newline'.format(round(len(self.players)/2))
          elif player.speed > 6:
            topr += ' speeds right to the finish line and breaks the sound barrier coming back!!!newline'
        print(topr.replace('newline', '\n').replace('He/She', player.gen_noun) + '\n')
        time.sleep(3)
    else:
      print('Add some players!')
  def toDict(self):
    end = self.__dict__
    end['Return to'] = 'Place'
    return end
class Master():
  def __init__(self):
    pass
  def createPlace(self, dict):
    return Place(dict['players'], dict['sport'], dict['type'], dict['name'])
  def createPlayer(self, dict):
    if dict['gen_noun'] == 'He':
      gen = 'boy'
    elif dict['gen_noun'] == 'She':
      gen = 'girl'
    return Player(dict['name'], dict['nickname'], [dict['basket_lvl'], dict['soccer_lvl'], dict['hockey_lvl']], dict['speed'], gender=gen, avatar=dict['look'])
  def movePlayer(self, player, oldPlace, newPlace):
    oldPlace.remPlayer(player)
    newPlace.addPlayer(player)
  def all(self, list, item):
    if item == Player:
      for i in list:
        i.display()
    if item == Place:
      for i in list:
        i.play_out()
def clear():
  os.system('clear')
def itemConverter(dict):
  if dict['Return to'] == 'Player':
    if dict['gen_noun'] == 'He':
      gen = 'boy'
    elif dict['gen_noun'] == 'She':
      gen = 'girl'
    return Player(dict['name'], dict['nickname'], [dict['basket_lvl'], dict['soccer_lvl'], dict['hockey_lvl']], dict['speed'], gender=gen, avatar=dict['look'])
  if dict['Return to'] == 'Place':
    return Place(dict['players'], dict['sport'], dict['type'], dict['name'])
def sourceCode():
  return open('playing.py').read()