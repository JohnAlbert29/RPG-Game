import tkinter as tk
from tkinter import messagebox, ttk

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

def submit_class(event):
    class_choice = class_combobox.current() + 1
    char_class = character.set_class(class_choice)
    if char_class == "Invalid Input":
        messagebox.showerror("Error", "Invalid class input. Please choose a valid class.")
    else:
        character.char_class = char_class
        update_abilities(class_choice)
        display_selections()

def submit_weapon(event):
    weapon_choice = weapon_combobox.current() + 1
    char_weapon = character.set_weapon(weapon_choice)
    if char_weapon == "Invalid Input":
        messagebox.showerror("Error", "Invalid weapon input. Please choose a valid weapon.")
    else:
        character.char_weapon = char_weapon
        display_selections()

def submit_ability():
    ability_choice = ability_combobox.current()
    class_choice = class_combobox.current() + 1
    ability_name = character.set_ability(class_choice, ability_choice)
    if ability_name == "Invalid Class Input" or ability_name == "Invalid Ability Input":
        messagebox.showerror("Error", "Invalid ability input. Please choose a valid ability for your class.")
    else:
        if ability_name not in abilities:
            abilities.append(ability_name)
            ability_listbox.insert(tk.END, ability_name)
            if len(abilities) == 3:
                ability_combobox.config(state=tk.DISABLED)
            display_selections()

def update_abilities(class_choice):
    abilities_dict = {
        1: ["Energy Ball", "Dragons Breath", "Crowns of Flame", "Hail Storm"],
        2: ["Fire Slash", "Power Slash", "Gigantic Storm", "Chaotic Disaster"],
        3: ["Take Aim", "Quick Shot", "Blazing Arrow", "Frost Arrow"],
        4: ["Cloaking", "Enchant Poison", "Sonic Acceleration", "Meteor Assault"]
    }
    ability_combobox.config(values=abilities_dict.get(class_choice, []))
    ability_combobox.current(0)
    ability_combobox.config(state=tk.NORMAL)

def display_selections():
    selections = f"You are a(n) {character.char_class}\n" \
                 f"With a weapon of {character.char_weapon}\n" \
                 f"And have the powers of {', '.join(abilities)}"
    selection_label.config(text=selections)

def start_character():
    if character.char_class and character.char_weapon and len(abilities) == 3:
        selections = f"You are a(n) {character.char_class}\n" \
                     f"With a weapon of {character.char_weapon}\n" \
                     f"And have the powers of {', '.join(abilities)}"
        messagebox.showinfo("Character Complete", selections)
    else:
        messagebox.showerror("Error", "Please complete all selections before starting.")

character = Character()
abilities = []

root = tk.Tk()
root.title("Character Creation")
root.geometry("400x500")

tk.Label(root, text="Select Class:", font=("Helvetica", 12)).pack(pady=10)
class_combobox = ttk.Combobox(root, values=["Wizard", "Knight", "Archer", "Assassin"], font=("Helvetica", 12), state="readonly")
class_combobox.pack(pady=10)
class_combobox.bind("<<ComboboxSelected>>", submit_class)

tk.Label(root, text="Select Weapon:", font=("Helvetica", 12)).pack(pady=10)
weapon_combobox = ttk.Combobox(root, values=["Wizard Staff", "Sword", "Bow & Arrow", "Katar"], font=("Helvetica", 12), state="readonly")
weapon_combobox.pack(pady=10)
weapon_combobox.bind("<<ComboboxSelected>>", submit_weapon)

tk.Label(root, text="Select Ability:", font=("Helvetica", 12)).pack(pady=10)
ability_combobox = ttk.Combobox(root, values=[], font=("Helvetica", 12), state="disabled")
ability_combobox.pack(pady=10)
tk.Button(root, text="Submit Ability", command=submit_ability, font=("Helvetica", 12)).pack(pady=10)

tk.Label(root, text="Selected Abilities:", font=("Helvetica", 12)).pack(pady=10)
ability_listbox = tk.Listbox(root, font=("Helvetica", 12), height=6)
ability_listbox.pack(pady=10)

selection_label = tk.Label(root, text="", font=("Helvetica", 12), wraplength=300, justify="left")
selection_label.pack(pady=20)

tk.Button(root, text="Start", command=start_character, font=("Helvetica", 12)).pack(pady=10)

root.mainloop()
