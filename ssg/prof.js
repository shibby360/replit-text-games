function Mini_SSG_Prof() {
    this.soldiers = {
      'Dark':{'level':0},
      'Shade':{'level':0},
      'Shapeshift':{'level':0},
      'Night_mult':{'level':0},
      'Dim':{'level':0},
      'Obscurer':{'level':0},
      'Copy':{'level':0},
      '_2D':{'level':0},
      'Fake_Attack':{'level':0},
      'Elongate':{'level':0}
    }
    this.upgradesoldier = function(who) {
      if(this.soldiers[who].level != 4) {  
        this.soldiers[who].level += 1
      } else {
        console.log('Not upgradeable')
      }
    }
    this.unlocksoldier = function(who) {
      if(this.soldiers[who].level == 0) {
        this.soldiers[who].level = 1
      } else {
        console.log('Already Unlocked')
      }
    }
    this.soldiers['Dark'].ability = 'None'
    this.soldiers['Shade'].ability = 'Disappear for a short time'
    this.soldiers['Shapeshift'].ability = 'Change body into anything not living'
    this.soldiers['Night_mult'].ability = 'Make multiples of himself'
    this.soldiers['Dim'].ability = 'Posess someone and dim their vision; dimming vision turns off special abilities'
    this.soldiers['Obscurer'].ability = 'Blur someone completely and stop them from doing anything'
    this.soldiers['Copy'].ability = 'Make a weak copy of himself'
    this.soldiers['_2D'].ability = 'Make himself completely flat'
    this.soldiers['Fake_Attack'].ability = 'Look like he is one place but be another'
    this.soldiers['Elongate'].ability = 'Be as long as he wants'
    //End of soldiers
  
  
    this.patriots = ['Trainer']
    this.getpatr = function(who) {
      this.patriots[this.patriots.length] = who
    }
    this.patrweaps = {
      'Trainer':'Sword, Shield, Gun'
    }
    this.addpatrweap = function(patr, weap) {
      this.patrweaps[patr] += weap
    }
    //End of patriots
  }
  
  var Shiv_prof = new Mini_SSG_Prof()
  
  
  Shiv_prof.unlocksoldier('Dark')
  for(var i = 0; i < 3; i++) {
    Shiv_prof.upgradesoldier('Dark')
  }
  Shiv_prof.getpatr('Relood')
  Shiv_prof.addpatrweap('Relood', 'Sword, Shield, Gun')