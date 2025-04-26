from Enemy import *
from Hero import *

def battle(e1: Enemy, e2: Enemy):
    e1.talk()
    e2.talk()

    while e1.health_points > 0 and e2.health_points > 0:
        print("------------------------------")
        e1.special_attack()
        e2.special_attack()

        print(f"{e1.get_type_of_enemy()} health: {e1.health_points} HP left")
        print(f"{e2.get_type_of_enemy()} health: {e2.health_points} HP left")

        e1.attack()
        e2.health_points -= e1.attack_damage
        e2.attack()
        e1.health_points -= e2.attack_damage

    print("------------------------------")

    if e1.health_points > 0:
        print(f"{e1.get_type_of_enemy()} wins!")
    else:
        print(f"{e2.get_type_of_enemy()} wins!")
        

def hero_battle(hero: Hero, enemy: Enemy):
    while hero.health_points > 0 and enemy.health_points > 0:
        print("------------------------------")
        enemy.special_attack()
        enemy.attack()
        hero.health_points -= enemy.attack_damage
        print(f"{hero.get_type_of_hero()} health: {hero.health_points} HP left")

        hero.attack()
        enemy.health_points -= hero.attack_damage
        print(f"{enemy.get_type_of_enemy()} health: {enemy.health_points} HP left")

    print("------------------------------")

    
    if hero.health_points > 0:
        print(f"{hero.get_type_of_hero()} wins!")
    else:
        print(f"{enemy.get_type_of_enemy()} wins!")
        


zombie = Zombie(10, 1)
ogre = Ogure(20, 3)

hero = Hero("Hero", 20, 5, Weapon("Sword", 3))
hero.equip_weapon()
hero_battle(hero, ogre)