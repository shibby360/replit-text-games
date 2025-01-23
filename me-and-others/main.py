import os
import random as r

persons = []
class Person:
  """
  People.
  """
  def __init__(self, name, item, drink):
    global persons
    self.name = name
    self.item = item
    self.drink = drink
    self.energy = self.drink.energy
    self.abilitiness = self.item.abilitiness
    self.set()
    persons.append(self)
  def energize(self):
    if self.energy >= 10:
      print('⭐ Energized!⭐')
      self.energy += self.drink.energy
    else:
      print('⚠️ Could not energize...⚠️')
      self.energy -= 5
    self.set()
  def grab(self):
    self.abilitiness += self.item.abilitiness
    print(self.item.emoji, self.item.name + '!')
    self.set()
  def attack(self, enemy):
    if self.energy >= 20:
      self.energy -= 20
      self.abilitiness -= 5
      ability = self.abilitiness + 25#Already upped by 5
      if self.energy >= 1500:
        ability += 150
      elif self.energy >= 1000:
        ability += 100
      elif self.energy >= 500:
        ability += 50
    else:
      ability = self.abilitiness
      self.energy -= 5
    enemy.energy -= ability
    self.set()
    enemy.set()
  def set(self):
    self.all = f"""
Name: {self.name}
Item: {self.item.name} {self.item.emoji}
Drink: {self.drink.name}
Energy: {self.energy}
Abilitiness: {self.abilitiness}
"""
  def isdead(self):
    return self.energy <= 0
class Item:
  """
  Items.
  """
  def __init__(self, name, emoji, abilitiness):
    self.name = name
    self.emoji = emoji
    self.abilitiness = abilitiness
class Drink:
  """
  Drinks.
  """
  def __init__(self, name='Water', energy=30):
    self.name = name
    self.energy = energy

shiv = Person('Shiv', Item('Phone', '📱', 40), Drink('Sparkling Water', 30))
person1 = Person('Person1',  Item('Basketball', '🏀', 30), Drink('Gatorade', 40))
anish = Person('Anish', Item('Dorito', '🔺', 10), Drink('Water', 20))
person2 = Person('Person2', Item('Orange', '🍊', 20), Drink('OJ', 40))
person3 = Person('Person3', Item('Bat', '🏏', 10), Drink('Soda', 10))
peoplenames = []
for person in persons:
  peoplenames.append(person.name)

person = input(f'Which person{peoplenames}?: ').lower()
person = eval(person)
attackables = persons
attackables.remove(person)
while True:
  os.system('clear')
  for attackable in attackables:
    if attackable.isdead():
      attackables.remove(attackable)
  if attackables == [] and not person.isdead():
    print('You win!')
    break
  if person.isdead():
    print('You lose...')
    break
  print(person.all+'(You)')
  for attackable in attackables:
    print(attackable.all)
  choice = input('''[1]Attack
[2]Energize
[3]Grab
[4]Chill
[5]Exit
Which one?: ''')
  if choice == '1':
    attackablenames = []
    for attackable in attackables:
      attackablenames.append(attackable.name)
    attackable = eval(input(f'Which person{attackablenames}?: ').lower())
    person.attack(attackable)
  elif choice == '2':
    person.energize()
  elif choice == '3':
    person.grab()
  elif choice == '5':
    break
  input()
  attacker = r.choice(attackables)
  optn = int(r.choice('123'))
  if optn == 1:
    attacker.attack(person)
    print(attacker.name + ' attacked you!')
    input()
  elif optn == 2:
    attacker.grab()
  elif optn == 3:
    attacker.energize()
print(person.all)