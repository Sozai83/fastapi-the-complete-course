from Enemy import *

enemy = Enemy("Goblin", 20, 3)

print(enemy.get_type_of_enemy())

enemy.talk()
enemy.walk_forward()
enemy.attack()