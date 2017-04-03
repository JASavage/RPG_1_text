from random import randint

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
    
  
  
    
