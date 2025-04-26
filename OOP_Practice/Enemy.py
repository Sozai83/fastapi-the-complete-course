import random


class Enemy:
    ## Constructor for the Enemy class when initializing an enemy object.
    ## Self referts to the instance of the class itself.
    def __init__(self, type_of_enemy, health = 10, attack_damage = 1):
        self.__type_of_enemy: str = type_of_enemy
        self.health_points: int = health
        self.attack_damage: int = attack_damage

    def get_type_of_enemy(self):
        return self.__type_of_enemy
    
    """"
    As I don't want to change the type of enemy after it has been created, I will not use this setter method.
    def set_type_of_enemy(self, type_of_enemy):
        self.__type_of_enemy = type_of_enemy
    """

    def talk(self):
        print(f"I am a {self.get_type_of_enemy()}. Be prepared to fight!")

    def walk_forward(self):
        print(f"{self.get_type_of_enemy()} moves closer to you!")

    def attack(self):
        print(f"{self.get_type_of_enemy()} attacks you for {self.attack_damage} damage!")

    def special_attack(self):
        print(f"{self.get_type_of_enemy()} has no special attack!")

class Zombie(Enemy):
    def __init__(self, health = 10, attack_damage = 1):
        super().__init__("Zombie", health, attack_damage)

    def talk(self):
        print("Braaaains...")

    def spread_disease(self):
        print("You have been infected with a zombie virus!")

    def special_attack(self):
        did_special_attack = random.random() < 0.5
        if did_special_attack:
            self.health_points += 2
            print(f"{self.get_type_of_enemy()} has healed itself for 2 health points!")

class Ogure(Enemy):
    def __init__(self, health = 10, attack_damage = 1):
        super().__init__("Ogre", health, attack_damage)

    def talk(self):
        print("Me smash!")
    
    def special_attack(self):
        did_special_attack = random.random() < 0.2
        if did_special_attack:
            self.attack_damage += 4
            print(f"{self.get_type_of_enemy()} has increased its attack damage by 4 points!")