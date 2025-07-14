import tkinter as tk
from tkinter import ttk
from main import CharacterCreator  # Assuming your creation logic is in main.py

def create_character():
    name = name_entry.get()
    character_class = class_entry.get()
    level_str = level_entry.get()
    try:
        level = int(level_str)
    except ValueError:
        level = ""
    character_race = race_entry.get().lower()  # Apply .lower() to race input
    spirit_bond = spirit_bond_entry.get().lower()
    creator = CharacterCreator()
    character = creator.create_character(
        name, [], level, character_race, character_class, "", "", "", "", "", "", spirit_bond
    )
    if hasattr(character, "get_summary"):
        info = character.get_summary()
    else:
        info = (
            f"Name: {character.name}\n"
            f"Class: {character.character_class}\n"
            f"Race: {character.character_race}\n"
            f"Spirit Bond: {character.spirit_bond}\n"
            f"{character.spirit_bond_description}"
        )
    character_info_label.config(text=info)

root = tk.Tk()
root.title("VFTD Character Sheet")
root.geometry("600x400")

# Create a frame to hold the input fields horizontally and wrap after 5 fields
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

# Define dropdown options
class_options = ["Warrior", "Rogue", "Sartor", "Zealot", "Dungeoneer"]
race_options = ["Fjoran", "Shaelarae", "Talii", "Human", "Bassyrikin"]
spirit_bond_options = [
    "Vulkjoran", "Korvyran", "Akathian", "Fean", "Unbound", "Bassyric", "Silean"
]

# Define fields and their entries
fields = [
    ("Name:", tk.Entry(input_frame)),
    ("Class:", ttk.Combobox(input_frame, values=class_options)),
    ("Level:", tk.Entry(input_frame)),
    ("Race:", ttk.Combobox(input_frame, values=race_options)),
    ("Spirit Bond:", ttk.Combobox(input_frame, values=spirit_bond_options)),
]

# Place fields in grid, wrap after 5 fields (2 columns per field: label and entry)
for i, (label_text, entry) in enumerate(fields):
    row = i // 5  # 5 fields per row
    col = (i % 5) * 2
    tk.Label(input_frame, text=label_text).grid(row=row, column=col, padx=5, pady=5)
    entry.grid(row=row, column=col+1, padx=5, pady=5)

# Assign entry variables for use in create_character
name_entry = fields[0][1]
class_entry = fields[1][1]
level_entry = fields[2][1]
race_entry = fields[3][1]
spirit_bond_entry = fields[4][1]

# Create Character button below the input fields
create_btn = tk.Button(root, text="Create Character", command=create_character)
create_btn.pack(pady=10)

character_info_label = tk.Label(root, text="", justify="left", wraplength=400)
character_info_label.pack()

root.mainloop()