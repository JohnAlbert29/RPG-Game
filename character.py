class Character:
    def __init__(self):
        self.char_class = ""
        self.char_weapon = ""
        self.char_ability = []

    def set_class(self, x: int) -> str:
        classes = {
            1: "Wizard",
            2: "Knight",
            3: "Archer",
            4: "Assassin"
        }
        self.char_class = classes.get(x, None)
        if not self.char_class:
            return "Invalid Input"
        return self.char_class

    def set_weapon(self, y: int) -> str:
        weapons = {
            1: "Wizard Staff",
            2: "Sword",
            3: "Bow & Arrow",
            4: "Katar"
        }
        self.char_weapon = weapons.get(y, None)
        if not self.char_weapon:
            return "Invalid Input"
        return self.char_weapon

    def set_ability(self, x: int, z: int) -> str:
        abilities = {
            1: ["Energy Ball", "Dragons Breath", "Crowns of Flame", "Hail Storm"],
            2: ["Fire Slash", "Power Slash", "Gigantic Storm", "Chaotic Disaster"],
            3: ["Take Aim", "Quick Shot", "Blazing Arrow", "Frost Arrow"],
            4: ["Cloaking", "Enchant Poison", "Sonic Acceleration", "Meteor Assault"]
        }
        ability_list = abilities.get(x, None)
        if not ability_list:
            return "Invalid Class Input"
        try:
            return ability_list[z]
        except IndexError:
            return "Invalid Ability Input"
