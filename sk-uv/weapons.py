class badpistol:
  name = 'Bad Pistol'
  damage = 1
  energy = 0
  accuracy = 8
  barehandable = False
  cansting = False
  canstick = False
  class crit:
    damage = 15
    chance = 4
class assaultrifle:
  name = 'Assault Rifle'
  damage = 2
  energy = 1
  accuracy = 4
  barehandable = False
  cansting = True
  stingtime = 2
  stingdamage = 1
  canstick = False
  class crit:
    damage = 4
    chance = 5
class blade:
  name = 'Blade'
  damage = 2
  energy = 1
  accuracy = 10
  barehandable = True
  canstick = False
  cansting = False
  class crit:
    chance = 0
class arpro:
  name = 'Assault Rifile Pro'
  damage = 3
  energy = 2
  accuracy = 5
  barehandable = False
  cansting = True
  stingtime = 3
  stingdamage = 2
  canstick = False
  class crit:
    damage = 5
    chance = 5
class brassknuckles:
  name = 'Brass Knuckles'
  damage = 4
  energy = 3
  accuracy = 3
  barehandable = True
  canstick = False
  cansting = False
  class crit:
    damage = 5
    chance = 2
class woodstaff:
  name = 'Wood Staff'
  damage = 3
  energy = 2
  accuracy = 6
  barehandable = True
  canstick = True
  sticktime = 3
  cansting = False
  class crit:
    damage = 5
    chance = 3
class bloodsword:
  name = 'Blood Sword'
  damage = 3
  energy = 0
  accuracy = 10
  barehandable = True
  canstick = False
  cansting = False
  class crit:
    damage = 6
    chance = 4
weapons = {
  'badpistol':badpistol,
  'blade':blade,
  'assaultrifle':assaultrifle,
  'arpro':arpro,
  'brassknuckles':brassknuckles,
  'woodstaff':woodstaff,
  'bloodsword':bloodsword
}