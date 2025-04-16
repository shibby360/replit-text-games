# made in 2021 ish

import playing
master = playing.Master()
shiv = playing.Player('Shiv', 'Gorilla', [4, 4, 1], 2, playing.Appearance.Heads.angry, playing.Appearance.Bodies.norm, playing.Appearance.Legs.norm, None, 'boy')
pranav = playing.Player('Pranav', 'Tallboi', [10, 3, 2], 4, playing.Appearance.Heads.bruh, playing.Appearance.Bodies.tall, playing.Appearance.Legs.norm, None, 'boy')
abi = playing.Player('Abhiram', 'Flabs', [5, 10, 6], 1, playing.Appearance.Heads.talking, playing.Appearance.Bodies.fat, playing.Appearance.Legs.block, playing.Appearance.Accessories.phone, 'boy')
ronnie = playing.Player('Ronell', 'Ronnie boi', [8, 7, 5], 9, playing.Appearance.Heads.norm, playing.Appearance.Bodies.norm, playing.Appearance.Legs.norm, playing.Appearance.Accessories.game_controller, 'boy')
akhil = playing.Player('Akhil', 'Akool', [8, 10, 8], 7, playing.Appearance.Heads.norm, playing.Appearance.Bodies.norm, playing.Appearance.Legs.norm, playing.Appearance.Accessories.soccer_ball, 'boy')
baboon = playing.Player('Varun', 'Abusity, Baboon', [8, 8, 8], 8, playing.Appearance.Heads.emojis.monkey, playing.Appearance.Bodies.norm, playing.Appearance.Legs.norm, None, 'boy')
anish = playing.Player('Anish', 'Squid', [3, 4, 2], 10, playing.Appearance.Heads.norm, playing.Appearance.Bodies.floppy, playing.Appearance.Legs.norm, None, 'boy')
advay = playing.Player('Advay', 'SAM', [-5, 4, 4], 6, playing.Appearance.Heads.norm, playing.Appearance.Bodies.norm, playing.Appearance.Legs.norm, playing.Appearance.Accessories.trash, 'boy')
hammy = playing.Player('Hamza', 'Azmah', [8, 0, 2], 7, playing.Appearance.Heads.norm, playing.Appearance.Bodies.norm, playing.Appearance.Legs.norm, playing.Appearance.Accessories.basketball, 'boy')
gang = [shiv, pranav, ronnie, akhil, baboon, anish, advay, hammy]
medehall = playing.Place(gang, 'soccer', 'Ct', 'Mendenhall')
brent = playing.Place(gang, 'racing', 'Ct', 'Brent')
parkpl = playing.Place(gang, 'basketball', 'Pl', 'Park')
places = [brent, medehall, parkpl]
shiv.call(brent, abi)

@shiv.setPersonailty()
def shivset():
  return 'KODER'
  
master.all(gang, playing.Player)

input('Press ENTER to continue.\n')