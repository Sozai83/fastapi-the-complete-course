from Enemy import *

enemy = Enemy("Goblin", 20, 3)

print(enemy.get_type_of_enemy())

enemy.talk()
enemy.walk_forward()
enemy.attack()

zombie = Zombie(15, 2)
zombie.talk()
zombie.walk_forward()
zombie.attack()
zombie.spread_disease()

ogre = Ogure(25, 5)
ogre.talk()
ogre.walk_forward()
ogre.attack()