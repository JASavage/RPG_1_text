from random import randint
import time


class Character:
    def __init__ (self):
        self.name = ""
        self.health = 1
        self.health_max = 1
        self.health_regen = float(0)
        self.level = 0
        self.trueEXP = 0
        self.maxEXP = 10
        self.level = 0
        self.trueEXP_add = 2
        self.damage = 1
        self.damage_add = 0
        self.damage_multi = 1
        self.enemy = None
    def do_damage(self):
        self.damage = 1
        self.damage_add = 0
        self.damage_multi = 1
        crit_chance = randint(1, 1000)
        crit_capnull = 150
        crit_capup = 950
        crit_multi = 3
        if crit_chance <= crit_capnull:
            self.damage = 0
        elif crit_chance > crit and crit_chance < crit_capup:
            self.damage = int((self.damage + self.damage_add) * self.damage_multi)
        elif crit_chance >= crit_capup:
            self.damage = int(((self.damage + self.damage_add) * self.damage_multi) * crit_multi)
        print "%s does %d damage to the enemy." % (self.name, self.damage)
        self.health -= self.damage
    def regen_health(self, enemy):
        seconds = 0
        while self.health < self.health_max:
            time_elapsed = time.clock()
            if time_elapsed == seconds:
                seconds = seconds + 1
                self.health += self.health_regen

class Enemy(Character):
    def __init__ (self):
        self.name = ""
        self.health_max = randint(.5(player.health_max, 1.5(player.health))
        self.health = self.health_max       
        self.health_regen = 1
        self.level = player.level
        self.enemy = player
        if self.health_max >= .5(player.health_max) and self.health_max < .75(player.health_max):
                                  self.health_regen = float(1.5)
                                  self.name = "a vampire"
        if self.health_max >= .75(player.health_max) and self.health_max <= player.health_max:
                                  self.health_regen = float(1)
                                  self.name = "a goblin"
        if self.health_max > player.health_max and self.health_max <= 1.5(player.health_max):
                                  self.health_regen = float(.5)
                                  self.name = "an orc"
    def attack(self):
        if self.enemy == None:
            print "Now why would fight something that isn't even there."
        else:
            self.dodamage


class Player(Character):
    def __init__(self):
        Character.__init__(self)
        self.health = 10
        self.health_max = 10
        self.health_regen = 1
    def quit(self):
        print "%s cannot deal with the horrors that he has seen, and commits seppuku." % self.name
        self.health = 0
    def help(self):
        print Commands.keys()
    def stats(self):
        print "Health: %d/%d" % (self.health, self.health_max)
        print "Health regen: %d"
    def explore(self):
        encounter = randint(0,20)
        if encounter >= 5:
            self.enemy = enemy                      
        else:
            print "You walk into a different area, but it pretty much looks the same. You may even be walking in circles."
    def flee(self, enemy):      
        if self.damage <= enemy.damage and self.health <= enemy.health:
            self.enemy = None
            print "You have successfully ditched the enemy."
        else:
            print "At least you tried"
   
    def level_up(self):   
        add_damage_chance = 4
        add_health_chance = 6
        add_regen_chance = 2
        add_defense_chance = 8
        add_test_1 = randint(1,10)
        add_test_2 = randint(1,10)
        add_test_3 = randint(1,10)
        add_test_4 = randint(1,10)
        lvl_damage_add = int(.05(player.damage))
        lvl_defense_add = int(.15(player.defense))
        lvl_regen_add = float(.1)
        lvl_health_add = int(.1(player.health))
        max_EXP_add = 2
        if self.trueEXP >= self.maxExp:
            if lvl_defense_add < 1:
                lvl_defense_add = 1
            if lvl_damage_add < 1:
                lvl_damage_add = 1
            if add_test_1 <= add_damage_chance:
                self.damage += lvl_damage_add
            else:
                self.damage = self.damage
            if add_test_2 >= add_defense:
                self.defense += lvl_damage_add
            else:
                self.defense = self.defense
            if add_test_3 <= add_regen_chance:
                self.health_regen += lvl_regen_add
            else:
                self.health_regen = self.health_regen
            if add_test_4 >= add_health_chance:
                self.health += lvl_health_add
            else:
                self.health = self.health
            self.trueEXP -= self.maxEXP
            self.maxEXP += self.max_EXP_add
            self.max_EXP_add += 2 
            self.level += 1
     def EXP(self):
           EXP_barrier = 10
           arbitrary = 2
           if enemy.health <= 0:
              while self.level <= EXP_barrier:
                  self.trueEXP_add = arbitrary
                  if self.level == EXP_barrier:
                     EXP_barrier += 10
                     arbitrary += 1
              self.true_EXP += self.trueEXP_add
                                  
    Commands = {
  'quit': player.quit,
  'help': player.help,
  'stats': player.stats,
  'explore': player.explore,
  'flee': player.flee,
  'attack': enemy.attack,
  }
 
p = player()
p.name = raw_input("What is your character's name? ")
print "(type help to get a list of actions)\n"
print "%s enters a dark cave, searching for adventure." % p.name
 
while(p.health > 0):
  line = raw_input("> ")
  args = line.split()
  if len(args) > 0:
    commandFound = False
    for c in Commands.keys():
      if args[0] == c[:len(args[0])]:
        Commands[c](p)
        commandFound = True
        break
    if not commandFound:
      print "%s doesn't understand the suggestion." % p.name                              
                                  
                                  
                                  
                                  
                                  
