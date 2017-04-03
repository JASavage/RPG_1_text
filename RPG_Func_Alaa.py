def level_up:
  add_damage_chance = 4
  add_health_chance = 8
  add_healthregen_chance = 2
  add_defense_chance = 6
  add_test_1 = randint(1,10)
  add_test_2 = randint(1,10)
  Player.__init__
  lvl_damage_add = int(.05(player.damage))
  if lvl_damage_add < 1:
    lvl_damage = 1
  if add_test_1 <= add_damage_chance:
    damage += lvl_damage_add
  else:
    damage = damage
  if add_test_1 >= add_defense
