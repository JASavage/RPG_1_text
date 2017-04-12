from random import randint

class Item:
  def __init__(Item):
    item.damage = 0
    item.defense = 0
    item.health_regen = 0
    item.health_max = 0
    item.rarity = 0
  def increase_damage(Item, rarity):
    item.damage = item.damage + damage_add
  def increase_defense(Item, rarity):
    item.defense = item.defense + defense_add
  def increase_health_regen(Item, rarity):
    item.health_regen = item.health_regen + health_regen_add
  def increase_health_max(Item, rarity):
    item.health_max += health_max_add
    
class rarity(Item):
  def __init__(Item):
    
    if player_level <= 10:
      item.rarity = randint(1, 10)
      
    elif player_level > 10 and player_level <= 25:
      item.rarity = randint(11, 25)
      
    elif player_level > 25 and player_level <= 50:
      item.rarity = randint(26, 50)
      
    elif player_level > 50 and player_level <= 75:
      item.rarity = randint(51, 75)
      
    elif player_level > 75 and player_level <= 100:
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
  
    
