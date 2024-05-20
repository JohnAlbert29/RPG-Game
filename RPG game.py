import os

os.system('cls' if os.name == 'nt' else 'clear')

class Character:
    def __init__(self, char_class: str = "", char_weapon: str = "", char_ability: list = None):
        self.char_class = char_class
        self.char_weapon = char_weapon
        self.char_ability = char_ability if char_ability is not None else []

    def set_class(self, x: int) -> str:
        classes = {
            1: "Wizard",
            2: "Knight",
            3: "Archer",
            4: "Assassin"
        }
        self.char_class = classes.get(x, None)
        if not self.char_class:
            print("Invalid Input")
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
            print("Invalid Input")
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
            print("Invalid Class Input")
            return ""
        try:
            return ability_list[z]
        except IndexError:
            print("Invalid Ability Input")
            return ""

character = Character()

print("Class Selection:\n")
print("""1. Wizard
2. Knight
3. Archer
4. Assassin""")
x = int(input("Choose the class of your Character: "))
char_class = character.set_class(x)
if not char_class:
    exit()

print("\nPick your weapon!")
print("""1. Wizard Staff
2. Sword
3. Bow & Arrow
4. Katar""")
y = int(input("Choose the weapon of your Character: "))
char_weapon = character.set_weapon(y)
if not char_weapon:
    exit()

print("""\nFor WIZARD: 
    0. Energy Ball
    1. Dragons Breath
    2. Crowns of Flame
    3. Hail Storm

For KNIGHT:
    0. Fire Slash
    1. Power Slash
    2. Gigantic Storm
    3. Chaotic Disaster

For ARCHER:
    0. Take Aim
    1. Quick Shot
    2. Blazing Arrow
    3. Frost Arrow

For ASSASSIN:
    0. Cloaking
    1. Enchant Poison
    2. Sonic Acceleration
    3. Meteor Assault\n""")

print(f"Grant {char_class}'s three abilities:")
abilities = []
for i in range(3):
    ability = int(input(f"Pick ability {i+1}: "))
    ability_name = character.set_ability(x, ability)
    if ability_name:
        abilities.append(ability_name)
    else:
        exit()

print(f"\nYou are a(n) {char_class}")
print(f"With a weapon of {char_weapon}")
print(f"And have the powers of {', '.join(abilities)}")
