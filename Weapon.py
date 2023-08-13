class Weapon:

    # Constructor
    def __init__(self, weapon_name, weapon_type, weapon_class, damage) -> None:
        self.weapon_name = weapon_name
        self.weapon_type = weapon_type
        self.weapon_class = weapon_class
        self.damage = damage
    
    # Getters and Setters
    def get_weapon_name(self):
        return self.weapon_name
    
    def set_weapon_name(self, weapon_name):
        self.weapon_name = weapon_name

    def get_weapon_type(self):
        return self.weapon_type
    
    def set_weapon_type(self, weapon_type):
        self.weapon_type = weapon_type

    def get_weapon_class(self):
        return self.weapon_class
    
    def set_weapon_class(self, weapon_class):
        self.weapon_class = weapon_class

    def get_damage(self):
        return self.damage
    
    def set_damage(self, damage):
        self.damage = damage
    
