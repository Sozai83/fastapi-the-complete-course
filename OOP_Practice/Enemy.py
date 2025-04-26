class Enemy:
    ## Constructor for the Enemy class when initializing an enemy object.
    ## Self referts to the instance of the class itself.
    def __init__(self, type_of_enemy, health = 10, attack_damage = 1):
        self.type_of_enemy: str = type_of_enemy
        self.health_points: int = health
        self.attack_damage: int = attack_damage

    def talk(self):
        print(f"I am a {self.type_of_enemy}. Be prepared to fight!")

    def walk_forward(self):
        print(f"{self.type_of_enemy} moves closer to you!")

    def attack(self):
        print(f"{self.type_of_enemy} attacks you for {self.attack_damage} damage!")