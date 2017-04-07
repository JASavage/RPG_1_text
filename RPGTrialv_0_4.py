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
        self.level = 0
        self.trueEXP = 0
        self.maxEXP = 10
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
        enemy.health -= damage
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
        print "Health regen: %d"
    
    def explore(self):
        encounter = randint(0,20)
        if encounter >= 5:
            self.enemy = Enemy(self)                      
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
