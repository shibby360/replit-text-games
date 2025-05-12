# i didn't make this :(
# used this for the 'getch()' function: 
# https://stackoverflow.com/questions/510357/ python-read-a-single-character-from-the-user

from getchar import _Getch
import os, time, random, cursor

getch = _Getch()
cursor.show()

white = "\033[0;97m"
red = "\033[0;31m"
b_red = "\033[1;31m"
yellow = "\033[0;93m"
b_yellow = "\033[1;93m"
green = "\033[0;32m"
cyan = "\033[0;96m"
b_cyan = "\033[1;96m"
purple = "\033[0;35m"
b_purple = "\033[1;95m"

# thanks Stack Overflow :)
#https://stackoverflow.com/questions/6667201/ how-to-define-a-two-dimensional-array-in-python
grid = [['0' for x in range(15)] for y in range(15)]



class Entity:
  class Bullet:
    def __init__(self, x, y, orient):
      self.x = x
      self.y = y
      self.orient = orient

      #self.bullets = []

    def move(self):
      grid[self.y][self.x] = '0'

      if self.orient == 1 and self.y > 0:
        self.y -= 1
      elif self.orient == 2 and self.x < len(grid[0]) - 1:
        self.x += 1
      elif self.orient == 3 and self.y < len(grid) - 1:
        self.y += 1
      elif self.orient == 4 and self.x > 0:
        self.x -= 1
      else:
        return True
      
      return False
  
  def __init__(self, syb, x, y, ety_clr, blt_clr, hp):
    self.bullets = []

    self.syb = syb

    self.x = x
    self.y = y

    self.ety_clr = ety_clr
    self.blt_clr = blt_clr

    self.hp = hp

  def display(self):
    grid[self.y][self.x] = self.ety_clr + self.syb

    for a in self.bullets:
      grid[a.y][a.x] = self.blt_clr + '.'

  def moveBullets(self):
    for a in self.bullets:
      if a.move():
        self.bullets.remove(a)

class Player(Entity):
  def __init__(self, syb, x, y, ety_clr, blt_clr, hp):
    Entity.__init__(self, syb, x, y, ety_clr, blt_clr, hp)

    self.orient = 0

  def move(self, x, y, orient):
    grid[self.y][self.x] = '0'
    self.orient = orient

    self.x += x
    self.y += y

  def newShot(self):
    self.bullets.append(self.Bullet(self.x, self.y, self.orient))

class Enemy(Entity):
  def __init__(self, syb, x, y, ety_clr, blt_clr, hp):
    Entity.__init__(self, syb, x, y, ety_clr, blt_clr, hp)

  def move(self, x, y, rof):
    if self.x > x and self.y < y:
      grid[self.y][self.x] = '0'

      if self.x - 3 > x and self.y + 3 < y:
        if self.x - x > y - self.y and grid[self.y][self.x - 1] == '0':
          self.x -= 1
        elif self.x - x < y - self.y and grid[self.y + 1][self.x] == '0':
          self.y += 1
      else:
        if self.x - x < y - self.y and grid[self.y][self.x - 1] == '0':
          self.x -= 1
        elif self.x - x > y - self.y and grid[self.y + 1][self.x] == '0':
          self.y += 1
    elif self.x < x and self.y < y:
      grid[self.y][self.x] = '0'

      if self.x + 3 < x and self.y + 3 < y:
        if x - self.x > y - self.y and grid[self.y][self.x + 1] == '0':
          self.x += 1
        elif x - self.x < y - self.y and grid[self.y + 1][self.x] == '0':
          self.y += 1
      else:
        if x - self.x < y - self.y and grid[self.y][self.x + 1] == '0':
          self.x += 1
        elif x - self.x > y - self.y and grid[self.y + 1][self.x] == '0':
          self.y += 1
    elif self.x < x and self.y > y:
      grid[self.y][self.x] = '0'

      if self.x + 3 < x and self.y - 3 > y:
        if x - self.x > self.y - y and grid[self.y][self.x + 1] == '0':
          self.x += 1
        elif x - self.x < self.y - y and grid[self.y - 1][self.x] == '0':
          self.y -= 1
      else:
        if x - self.x < self.y - y and grid[self.y][self.x + 1] == '0':
          self.x += 1
        elif x - self.x > self.y - y and grid[self.y - 1][self.x] == '0':
          self.y -= 1
    elif self.x > x and self.y > y:
      grid[self.y][self.x] = '0'

      if self.x - 3 > x and self.y - 3 > y:
        if self.x - x > self.y - y and grid[self.y][self.x - 1] == '0':
          self.x -= 1
        elif self.x - x < self.y - y and grid[self.y - 1][self.x] == '0':
          self.y -= 1
      else:
        if self.x - x < self.y - y and grid[self.y][self.x - 1] == '0':
          self.x -= 1
        elif self.x - x > self.y - y and grid[self.y - 1][self.x] == '0':
          self.y -= 1
    elif self.x == x and self.y < y and random.randint(0, rof) == 0:
      self.bullets.append(self.Bullet(self.x, self.y, 3))
    elif self.x == x and self.y > y and random.randint(0, rof) == 0:
      self.bullets.append(self.Bullet(self.x, self.y, 1))
    elif self.x < x and self.y == y and random.randint(0, rof) == 0:
      self.bullets.append(self.Bullet(self.x, self.y, 2))
    elif self.x > x and self.y == y and random.randint(0, rof) == 0:
      self.bullets.append(self.Bullet(self.x, self.y, 4))
    
    grid[self.y][self.x] = self.ety_clr + self.syb



player = Player('x', 7, 7, green, cyan, 3)

rounds = 1
waves = [ 0, 0, 0, 0, 0 ]

enemies = []

enemies.append(Enemy('e', 0, 0, red, yellow, 3))
enemies.append(Enemy('e', 0, 14, red, yellow, 3))
enemies.append(Enemy('e', 14, 14, red, yellow, 3))
enemies.append(Enemy('e', 14, 0, red, yellow, 3))


def displayGrid():
  for a in grid:
    for b in a:
      print(white + b, end = " ")
    print()


choice = "4"

while choice != "3":
  os.system("clear")
  choice = input("ASCII Shooter\n\n1) How to Play\n2) Extra Notes\n3) Play Game\n\n")

  if choice == "1":
    input("\nYou are the green 'x'. Use WASD to move, and SPACE to shoot. Avoid enemy bullets and fire back. If an enemy turns yellow, they are at one health. You have three health. Don't die. Make it past Round 5, and you win! And remember, enemies and bullets only move when you move, so play strategically. Good luck!\n\nPress enter to continue ")
  elif choice == "2":
    input("\nCheck it out on GitHub for a more in depth overview of this game: https://github.com/DynamicSquid/ASCII-Shooter\n\nI also might make a way better v2 if this project does well. Let me know in the comments what you guys think!\n\nPress enter to continue ")
  elif choice == "3":
    cursor.hide()



# game loop
while True:

  # mo' enemies!

  if rounds == 1 and len(enemies) == 2 and waves[0] == 0:
    enemies.append(Enemy('e', 7, 0, red, yellow, 3))
    enemies.append(Enemy('e', 7, 14, red, yellow, 3))
    waves[0] = 1
  elif rounds == 2 and len(enemies) == 0 and waves[1] == 0:
    enemies.append(Enemy('s', 0, 7, purple, yellow, 2))
    enemies.append(Enemy('s', 14, 6, purple, yellow, 2))
    waves[1] = 1
  elif rounds == 2 and len(enemies) == 1 and waves[1] == 1:
    enemies.append(Enemy('s', 7, 0, purple, yellow, 2))
    enemies.append(Enemy('s', 7, 14, purple, yellow, 2))
    waves[1] = 2
  elif rounds == 2 and len(enemies) == 1 and waves[1] == 2:
    enemies.append(Enemy('e', 7, 0, red, yellow, 3))
    enemies.append(Enemy('e', 7, 14, red, yellow, 3))
    enemies.append(Enemy('s', 0, 3, purple, yellow, 2))
    enemies.append(Enemy('s', 14, 12, purple, yellow, 2))
    waves[1] = 3
  elif rounds == 3 and len(enemies) == 0 and waves[2] == 0:
    enemies.append(Enemy('k', 0, 0, b_red, yellow, 5))
    enemies.append(Enemy('k', 14, 14, b_red, yellow, 5))
    waves[2] = 1
  elif rounds == 3 and len(enemies) == 1 and waves[2] == 1:
    enemies.append(Enemy('k', 0, 14, b_red, yellow, 5))
    enemies.append(Enemy('k', 14, 0, b_red, yellow, 5))
    waves[2] = 2
  elif rounds == 3 and len(enemies) == 2 and waves[2] == 2:
    enemies.append(Enemy('e', 0, 0, red, yellow, 5))
    enemies.append(Enemy('e', 5, 0, red, yellow, 5))
    enemies.append(Enemy('e', 9, 0, red, yellow, 5))
    enemies.append(Enemy('e', 14, 0, red, yellow, 5))
    enemies.append(Enemy('s', 5, 14, purple, yellow, 2))
    enemies.append(Enemy('s', 9, 14, purple, yellow, 2))
    waves[2] = 3
  elif rounds == 4 and len(enemies) == 0 and waves[3] == 0:
    enemies.append(Enemy('s', 0, 0, purple, yellow, 2))
    enemies.append(Enemy('s', 14, 0, purple, yellow, 2))
    enemies.append(Enemy('s', 0, 14, purple, yellow, 2))
    enemies.append(Enemy('s', 14, 14, purple, yellow, 2))
    waves[3] = 1
  elif rounds == 4 and len(enemies) == 3 and waves[3] == 1:
    enemies.append(Enemy('s', 0, 7, purple, yellow, 2))
    waves[3] = 2
  elif rounds == 4 and len(enemies) == 3 and waves[3] == 2:
    enemies.append(Enemy('s', 7, 0, purple, yellow, 2))
    waves[3] = 3
  elif rounds == 4 and len(enemies) == 3 and waves[3] == 3:
    enemies.append(Enemy('s', 14, 7, purple, yellow, 2))
    waves[3] = 4
  elif rounds == 4 and len(enemies) == 3 and waves[3] == 4:
    enemies.append(Enemy('s', 7, 14, purple, yellow, 2))
    waves[3] = 5
  elif rounds == 4 and len(enemies) == 0 and waves[3] == 5:
    enemies.append(Enemy('k', 0, 0, b_red, yellow, 5))
    enemies.append(Enemy('k', 14, 0, b_red, yellow, 5))
    enemies.append(Enemy('k', 0, 14, b_red, yellow, 5))
    enemies.append(Enemy('k', 14, 14, b_red, yellow, 5))
    waves[3] = 6
  elif rounds == 5 and len(enemies) == 0 and waves[4] == 0:
    enemies.append(Enemy('E', 0, 0, b_purple, yellow, 5))
    enemies.append(Enemy('E', 14, 14, b_purple, yellow, 5))
    enemies.append(Enemy('Q', 0, 14, b_yellow, yellow, 6))
    enemies.append(Enemy('Q', 14, 0, b_yellow, yellow, 6))
    waves[4] = 1
  elif rounds == 5 and len(enemies) == 0 and waves[4] == 1:
    enemies.append(Enemy('Ω', 7, 7, b_cyan, red, 20))
    waves[4] = 2


  os.system("clear")


  # display stuff

  player.display()

  for a in enemies:
    a.display()

  displayGrid()


  # move entities

  key = getch()

  if key == 'w' and player.y > 0:
    player.move(0, -1, 1)
  elif key == 'a' and player.x > 0:
    player.move(-1, 0, 4)
  elif key == 's' and player.y < len(grid) - 1:
    player.move(0, 1, 3)
  elif key == 'd' and player.x < len(grid[0]) - 1:
    player.move(1, 0, 2)
  elif key == ' ':
    player.newShot()

  for a in enemies:
    if rounds < 4 and random.randint(1, 3) == 1:
      a.move(player.x, player.y, 3)
    elif rounds > 3 and waves[4] != 1 and random.randint(1, 2) == 1:
      a.move(player.x, player.y, 2)
    elif rounds == 5 and waves[4] == 1:
      a.move(player.x, player.y, 1)


  # move bullets

  player.moveBullets()

  for a in enemies:
    a.moveBullets()


  # check if player or enemy is hit

  for a in player.bullets:
    for b in enemies:
      if a.x == b.x and a.y == b.y:
        player.bullets.remove(a)

        b.hp -= 1

        if b.hp == 1:
          b.ety_clr = yellow

        if b.hp == 0:
          grid[b.y][b.x] = '0'
          enemies.remove(b)

          if len(enemies) == 0 and waves[4] != 1:
            rounds += 1

            if rounds == 6:
              print("You win! Well done! Take a screenshot and post it in the comments. Thanks for playing :)")
              exit()

            print("Round " + str(rounds))
            time.sleep(3)

            player.bullets.clear()

  for a in enemies:
    for b in a.bullets:
      if b.x == player.x and b.y == player.y:
        player.hp -= 1

        for c in range(6):
          os.system("clear")

          for a in enemies:
            a.display()

          player.display()

          displayGrid()

          if c % 2 == 0:
            print("You were hit!")
          
          time.sleep(0.5)

        for c in player.bullets:
          grid[c.y][c.x] = '0'

        player.bullets.clear()

        for c in enemies:
          for d in c.bullets:
            grid[d.y][d.x] = '0'

          c.bullets.clear()

        if player.hp == 0:
          print("You died!")
          exit()