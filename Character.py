class Character:

    # Constructor
    def __init__(self, name = '', character_race = '', character_subrace = '', character_class = '', character_subclass = '', strength = 0, dexterity = 0, constitution = 0, intelligence = 0, wisdom = 0, charisma = 0) -> None:
        self.name = name
        self.character_race = character_race
        self.character_subrace = character_subrace
        self.character_class = character_class
        self.character_subclass = character_subclass
        self.strength = strength    
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma

    # Getters and Setters
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
    
    def get_character_race(self):
        return self.character_race
    
    def set_character_race(self, character_race):
        self.character_race = character_race
    
    def get_character_subrace(self):
        return self.character_subrace
    
    def set_character_subrace(self, character_subrace):
        self.character_subrace = character_subrace
    
    def get_character_class(self):
        return self.character_class
    
    def set_character_class(self, character_class):
        self.character_class = character_class
    
    def get_character_subclass(self):
        return self.character_subclass
    
    def set_character_subclass(self, character_subclass):
        self.character_subclass = character_subclass
    
    def get_strength(self):
        return self.strength
    
    def set_strength(self, strength):
        self.strength = strength

    def get_dexterity(self):
        return self.dexterity
    
    def set_dexterity(self, dexterity):
        self.dexterity = dexterity

    def get_constitution(self):
        return self.constitution
    
    def set_constitution(self, constitution):
        self.constitution = constitution

    def get_intelligence(self):
        return self.intelligence

    def set_intelligence(self, intelligence):
        self.intelligence = intelligence
    
    def get_wisdom(self):
        return self.wisdom
    
    def set_wisdom(self, wisdom):
        self.wisdom = wisdom

    def get_charisma(self):
        return self.charisma
    
    def set_charisma(self, charisma):
        self.charisma = charisma