class Hero:
    def __init__(self, name, health_points, attack_damage, weapon=None):
        self.__type_of_hero = name
        self.health_points = health_points
        self.attack_damage = attack_damage
        self.weapon = weapon

    def get_type_of_hero(self):
        return self.__type_of_hero
    
    def equip_weapon(self):
        if self.weapon:
            self.attack_damage += self.weapon.damage
            self.is_weapon_equipped = True
            print(f"{self.get_type_of_hero()} equips a {self.weapon.get_weapon_type()}!")
        else:
            print(f"{self.get_type_of_hero()} has no weapon to equip!")


    def attack(self):
        print(f"{self.get_type_of_hero()} attacks for {self.attack_damage} damage!")


class Weapon:
    def __init__(self, weapon_type, damage):
        self.__weapon_type = weapon_type
        self.damage = damage

    def get_weapon_type(self):
        return self.__weapon_type