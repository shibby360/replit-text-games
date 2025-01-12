# made in 2020-2021
import time as t, random as r, os as o
import pyfiglet
def win():
  b = pyfiglet.Figlet(font='standard')
  c = b.renderText('YOU WON!')
  print(c)
name = input("What is your name? ")
ready = input("Hello {0}. You are in a water gun war. Are you ready(y/n)? ".format(name))
Orange = "\033[0;33m"
Red = "\033[0;31m"
def clear():
  o.system('cls' if o.name == 'nt' else "printf '\033c'")
def ScaredyCatError(str):
  print("(Read Error)")
  print(Red+"Traceback (most recent call last):")
  print(Red+"  File \"{0}\", line brain, in <SomeCell>".format(name))
  print(Red+"    Hello {0}. You are in a water gun war. Are you ready(y/n)? {1}".format(name, ready))
  print(Red+"ScaredyCatError: {0}".format(str))
if 'y' in ready or 'Y' in ready:
  print("Lets go.")
  t.sleep(1)
  clear()
  guns = ['Four sprayer', 'Four sprayer', 'Pumper', 'One spray', 'Hose']
  gun = ['Four sprayer', 'Four sprayer', 'Hose']
  gun = r.choice(gun)
  print("Your gun is the {0}.".format(gun))
  points = 0
  lives = 3
  if gun == 'Four sprayer':
    Four_sprayer = {1: "Handle", 0.25: "Shoot", 3: "Range"}
    play_ammo = 1
    print("You can handle 1 liter. You shoot 1/4 of a liter every time you shoot. Your range is 3.")
    fospstart = int(input("You have 0 liters. Do you wish to \n[1]Get your fill\n[2]Load out\n"))
    if fospstart == 1:
      print("You have all your ammo.")
      shootchoi = int(input("There is a person nearby! He is in front of you! Do you..\n[1]Shoot\n[2]Run away\n"))
      if shootchoi == 1:
        print("You have blasted the person in front of you! You got them in the front! #Proskillz. ")
        points += 3
        play_ammo -= 0.25
        print("You now have {0} points. You have {1} ammo. You also have {2} lives.".format(points, play_ammo, lives))
        print('You now are hiding. You see someone in the range of 6. Do you...')
        hidshotchoi = int(input('[1]Shoot\n[2]Stay hidden\n'))
        if hidshotchoi == 1:
          print('You shot, but your range is too small! The enemy found you and you got hit! You have...\nLOST.')
        if hidshotchoi == 2:
          print('You stay hidden. You see someone coming towards you. You figure out they want to camp. Do you...')
          campshocho = int(input('[1]Run away\n[2]Shoot when he comes\n'))
          if campshocho == 1:
            print('He has spotted you! He runs to blast you! You turn around to get him, but you are out of range and he hits you! ', end='')
            lives -= lives
            print('You have...\nLOST.')
          if campshocho == 2:
            print('You blast the kid!', end=' ')
            play_ammo -= 0.25
            points += 3
            print('You now have {0} points and {1} ammo. You are waiting to get some points. You then see someone lying on the floor. Do you...'.format(points, play_ammo))
            lyingshocho = int(input('[1]Shoot\n[2]Stay\n'))
            if lyingshocho == 1:
              print('You foul the other player becasue you hit them in the head. You lost 4 points.', end=' ')
              points -= 4
              print('You now have {0} points. The other player gets enraged and chases after you and as you turn back to shoot, he sprays you right on the front. '.format(points), end='')
              lives -= lives
              print('You have...\nLOST.')
            if lyingshocho == 2:
              print('You stay hidden. There is a huge spray fest going on. You quickly spray someone and get 3 points.', end=' ')
              points += 3
              print('There now is 1 person left. You quickly get him in the legs.')
              win()
              print('Points: ' + str(points))
              print('Remaining lives: ' + str(lives))
      if shootchoi == 2:
        lives -= 2
        print('You got blasted in the back! You now have {0} lives.'.format(lives))
        print('You run out. There is a camper right next to the gate! You jump up to dodge, but it hits you in the feet! ', end='')
        lives -= 1
        print('You have...\nLOST.')
    if fospstart == 2:
      print("You load out into the fighting area. You get blasted by the opposite team. They each shoot you. You have lost all your lives. You have..")
      lives -= lives
      print("LOST.")
  if gun == 'Pumper':
    Pumper = {1.5: "Handle", 0.5:"Shoot", 6:"Range"}
    pstart = int(input('Do you want to load out with a filled gun or not full?\n[1]Fill\n[2]Not Filled\n'))
    if pstart == 1:
      print("Do you wish to pump?")
      pumpchoi = int(input())
    if pstart == 2:
      print('As you load out you get sprayed on the front.', end=' ')
      lives -= 3
      print('You have...\nLOST.')
  if gun == 'One Spray':
    One_Spray = {}
  if gun == 'Hose':
    print('3..')
    t.sleep(1)
    print('2..')
    t.sleep(1)
    print('1..')
    t.sleep(1)
    print('When the game starts you full blast everyone and get a point horde.')
    points += 5 * 3
    win()
else:
  ScaredyCatError("You do not like getting wet. You are a SCAREDY CAT!")