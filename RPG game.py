import os

os.system('cls')

class Character:
    def __int__(self, charClass: str, charWeapon: str, charAbility: str):
        self.setcharClass = charClass
        self.setcharWeapon = charWeapon
        self.setcharAbility = charAbility

  
  
    def SetClass(self, x):
        if x == 1:
            self.setcharClass = "Wizard"
            return self.setCharClass
        elif x == 2:
            self.setcharClass = "Knight"
            return self.setcharClass
        elif x == 3:
            self.setcharClass = "Archer"
            return self.setcharClass
        elif x == 4:
            self.setcharClass = "Assasin"
            return self.setcharClass
        else:
            print("Invalid Input")

    
    
    def SetWeapon(self, y):
        if y == 1:
            self.setcharWeapon = "Wizard Staff"
            return self.setcharWeapon
        elif y == 2:
            self.setcharWeapon = "Sword"
            return self.setcharWeapon
        elif y == 3:
            self.setcharWeapon = "Bow & Arrow"
            return self.setcharWeapon
        elif y == 4:
            self.setcharWeapon = "Katar"
            return self.setcharWeapon
        else:
            print("Invalid Input")

   
   
   
    def SetAbility(self, x, z):
        if x == 1:
            self.wizard = ["Energy Ball", "Dragons Breath", "Crowns of Flame", "Hail Storm"]
            return self.wizard[z]
        elif x == 2:
            self.knight = ["Fire Slash", "Power Slash", "Gigantic Storm", "Chaotic Disaster"]
            return self.knight[z]
        elif x == 3: 
            self.archer = ["Take Aim", "Quick Shot", "Blazing Arrow", "Frost Arrow"]
            return self.archer[z]
        elif x == 4:
            self.assassin = ["Cloaking", "Enchant Poison", "Sonic Acceleration", "Meteor Assault"]
            return self.assassin[z]
        else:
            print("Invalid Input")


character = Character()
print("Class Selection:\n")
print("""1 Wizard
 2 Knight
 3 Archer
 4 Assassin""")
x = int(input("class of your Character: "))
character.SetClass(x)

print("\npick your weapon!")
print(""" 1 Wizard Staff
 2 Sword
 3 Bow & Arrow
 4 Katar""")
y = int(input("Choose the weapon of your Character: "))
character.SetWeapon(y)

print("""\nFor WIZARD: 
    0 Energy Ball
    1 Dragons Breath
    2 Crowns of Flame
    3 Hail Storm

For KNIGHT:
    0 Fish Slash
    1 Power Slash
    2 Gigantic Storm
    3 Chaotic Disaster

For ARCHER:
    0 Take Aim
    1 Quick Shot
    2 Blazing Arrow
    3 Frost Arrow

For ASSASSIN:
    0 Cloaking
    1 Enchant Poison
    2 Sonic Acceleration
    3 Meteor Assault\n""")

print("Grant "+ character.SetClass(x)+  "'s three abilities: ")
ability1 = int(input("pick your ability 1: "))
character.SetAbility(x, ability1)
ability2 = int(input("pick your ability 2: "))
character.SetAbility(x, ability2)
ability3 = int(input("pick your ability 3: "))
character.SetAbility(x, ability3)

print("\nYou are/an", (character.SetClass(x)))
print("has a weapon of", (character.SetWeapon(y)))
print("and has the power of", character.SetAbility(x, ability1) + ",", character.SetAbility(x, ability2)+ ", and", character.SetAbility(x, ability3))
