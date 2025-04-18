"""
SSG Patriots
"""
import pwrs
class Patriot:
  def __init__(self, name, health, cost, cost_unit, boardspeed, boardspecial_ability, swordchuckable, swordspecial_ability, sworddamage, shielddurability, shieldspecial_ability, gunrange, gunspecial_ability, gundamage, powername):
    self.name = name
    self.health = health
    self.cost = cost
    self.cost_unit = cost_unit
    self.board = self.Board(boardspeed, boardspecial_ability)
    self.sword = self.Sword(swordchuckable, swordspecial_ability, sworddamage)
    self.shield = self.Shield(shielddurability, shieldspecial_ability)
    self.gun = self.Gun(gunrange, gunspecial_ability, gundamage)
    self.max_damage = self.sword.damage + self.gun.damage
    self.power = pwrs.Power(powername, self)
  class Board:
    def __init__(self, speed, special_ability):
      self.speed = speed
      self.special_ability = special_ability
  class Sword:
    def __init__(self, chuckable, special_ability, damage):
      self.chuckable = chuckable
      self.special_ability = special_ability
      self.damage = damage
  class Shield:
    def __init__(self, durability, special_ability):
      self.durability = durability
      self.special_ability = special_ability
  class Gun:
    def __init__(self, range, special_ability, damage):
      self.range = range
      self.special_ability = special_ability
      self.damage = damage
blake = Patriot('Blake', 150, 45, 'keys', 5, 'Kradness', False, 'Extended range', 45, 15, 'Entire body defense', 8, 'Double bullets', 65, 'Darkus')
brownja = Patriot('Brownja', 125, 30, 'keys', 3, 'Sword and shield attached', False, 'Upgraded damage', 55, 10, 'Chuckable', 0, 'coins', 0, 'Ninja')
tobgat = Patriot('Tobgat', 125, 30, 'keys', 3, 'None', False, 'None', 55, 10, 'None', 6, 'Robo bullets', 55, 'Robo')
eulb = Patriot('Eulb', 125, 30, 'keys', 3, 'Swirl power', False, 'Swirling Sword', 55, 10, 'Chuckable', 6, 'Merging bullets', 55, 'Bluer')
eulb_krad = Patriot('Eulb Krad', 125, 30, 'keys', 3, 'Swirl power', False, 'Swirling Sword', 55, 10, 'Chuckable', 6, 'Merging Krad bullets', 55, 'Dark Bluer')
pinky = Patriot('Pinky', 125, 30, 'keys', 3, 'Splitters', False, 'Splitting Sword', 55, 10, 'Chuckable', 6, 'Quadruple Mini bullets', 55, 'Pinkifier')
purpy = Patriot('Purpy', 125, 30, 'keys', 3, 'Splitters', False, 'Splitting Sword', 55, 10, 'Chuckable', 6, 'Quadruple Mini Krad bullets', 55, 'Purplifier')
relood = Patriot('Relood', 175, 50, 'keys', 8, 'Super speed', True, 'None', 60, 20, 'None', 8, 'Double guns', 60, 'Blood Blast')
ora = Patriot('Ora', 125, 30, 'keys', 3, 'Stretchy', False, 'Stretchy', 55, 10, 'Stretchy', 10, 'Stretchy', 55, 'Super Stretch')
yeller = Patriot('Yeller', 100, 30, 'keys', 1, 'Screaming', False, 'Loudness', 45, 10, 'Chuckable', 3, 'Sound guns', 45, 'Screamer')
class Soldier:
  def __init__(self, name, ability):
    self.name = name
    self.level = 1
    self.ability = 'None'
    self._ability = ability
    self.weapon = 'None'
  def upgrade(self):
    self.level += 1
    if self.level == 2:
      self.ability = self._ability
    elif self.level == 3:
      pass
    elif self.level == 4:
      pass
      self.weapon = 'Sword+Shield'