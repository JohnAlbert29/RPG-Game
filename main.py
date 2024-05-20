import tkinter as tk
from tkinter import messagebox, ttk
from character import Character
from data import CLASSES, WEAPONS, ABILITIES

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
    ability_combobox.config(values=ABILITIES.get(class_choice, []))
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
class_combobox = ttk.Combobox(root, values=list(CLASSES.values()), font=("Helvetica", 12), state="readonly")
class_combobox.pack(pady=10)
class_combobox.bind("<<ComboboxSelected>>", submit_class)

tk.Label(root, text="Select Weapon:", font=("Helvetica", 12)).pack(pady=10)
weapon_combobox = ttk.Combobox(root, values=list(WEAPONS.values()), font=("Helvetica", 12), state="readonly")
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
