from random import randint
import time

print """You are running as fast as possible, away from something, but you can't remember what.
You see a door, as you approach, it speaks. "Warning, opening this door means you are entering the Labyrinth Dimension.
You will never leave or die. There is only one exit." You don't care. As you are about to open the door someone stops you.
He gives you a book. This book has a map of all explored areas of the Labyrinth. As the next one to enter you are expected to continue this tradition.
When you eventually give up, and when you do this book will duplicate and leave you."""
class Character:
    def __init__ (self):
        self.name = ""
        self.health = 1
        self.health_max = 1
        self.health_regen = float(0)
    def do_damage(self, enemy):
        damage = 1
        damage_add = 0
        damage_multi = float(1)
        crit_chance = randint(1, 1000)
        crit_capnull = 150
        crit_capup = 950
        crit_multi = float(3)
        if crit_chance <= crit_capnull:
            damage = 0
        elif crit_chance > crit and crit_chance < crit_capup:
            damage = int((damage + damage_add) * damage_multi)
        elif crit_chance >= crit_capup:
            damage = int(((damage + damage_add) * damage_multi) * crit_multi)
        print "%s does %d damage to the enemy." % (self.name, damage)
        if enemy.health == 0:
            trueEXP += 2
        return enemy.health <= 0
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
        if self.health_max >= .5(player.health_max) and self.health_max < .75(player.health_max):
                                  self.health_regen = float(1.5)
                                  self.name = "a vampire"
        if self.health_max >= .75(player.health_max) and self.health_max <= player.health_max:
                                  self.health_regen = float(1)
                                  self.name = "a goblin"
        if self.health_max > player.health_max and self.health_max <= 1.5(player.health_max):
                                  self.health_regen = float(.5)
                                  self.name = "an orc"
        
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
        print "Health regen: %d" % self.health_regen
    def explore(self):
        vampire_chance = 2
        goblin_chance = 5
        orc_chance = 7
        encounter = randint(1,10)
        if encounter = vampire_chance:
            self.vampire = Vampire(self)
            print "You encounter a Vampire"
        elif encounter = goblin_chance:
            self.goblin = Goblin(self)
            print "You encounter a Goblin"
        elif encounter = orc_chance:
            self.orc = Orc(self)
            print "You encounter an Orc"
        else:
            print "You walk into a different area, but it pretty much looks the same. You may even be walking in circles."
    def flee(self):      
        if self.damage <= enemy.damage and self.health <= enemy.health:
            self.enemy = None
            print "You have successfully ditched the enemy."
        else:
            print "Fleeing is not allowed especially since you can win."
    def attack(self):
        if self.enemy == None:
            print "Now why would fight something that isn't even there."
        else:

                                  
class Item:
  def __init__(Item):
    item.damage = 0
    item.defense = 0
    item.health_regen = 0
    item.rarity = 0
  def increase_damage(Item, rarity):
    item.damage = item.damage + damage_add
  def increase_defense(Item, rarity):
    item.defense = item.defense + defense_add
  def increase_health_regen(Item, rarity):
    item.health_regen = item.health_regen + health_regen_add
    
class rarity(Item):
  def __init__(Item):
    
    if player_level < 10:
      item.rarity = randint(1, 10)
      
    elif player_level > 10 and player_level < 25:
      item.rarity = randint(11, 25)
      
    elif player_level > 25 and player_level < 50:
      item.rarity = randint(26, 50)
      
    elif player_level > 50 and player_level < 75:
      item.rarity = randint(51, 75)
      
    elif player_level > 75 and player_level < 100:
      item.rarity = randint(76, 100)
    
  def rarity_add(Item):
    
    damage_add = item.rarity
    defense_add = item.rarity
    
  def level_up:
    add_damage_chance = 4
    add_health_chance = 6
    add_regen_chance = 2
    add_defense_chance = 8
    add_test_1 = randint(1,10)
    add_test_2 = randint(1,10)
    add_test_3 = randint(1,10)
    add_test_4 = randint(1,10)
    Player.__init__
    lvl_damage_add = int(.05(player.damage))
    lvl_defense_add = int(.15(player.defense))
    lvl_regen_add = float(.1)
    lvl_health_add = int(.1(player.health))
    max_EXP_add = 2
    while trueEXP >= maxExp:
      if lvl_defense_add < 1:
        lvl_defense_add = 1
      if lvl_damage_add < 1:
        lvl_damage_add = 1
      if add_test_1 <= add_damage_chance:
        player.damage += lvl_damage_add
      else:
        player.damage = player.damage
      if add_test_2 >= add_defense:
        player.defense += lvl_damage_add
      else:
        player.defense = player.defense
      if add_test_3 <= add_regen_chance:
        player.health_regen += lvl_regen_add
      else:
        player.health_regen = player.health_regen
      if add_test_4 >= add_health_chance:
        player.health += lvl_health_add
      else:
        player.health = player.health
      trueEXP -= maxEXP
      maxEXP += max_EXP_add
      max_EXP_add += 2
  
    
