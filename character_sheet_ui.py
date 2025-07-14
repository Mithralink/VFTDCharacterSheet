import tkinter as tk
from main import CharacterCreator  # Assuming your creation logic is in main.py

def create_character():
    name = name_entry.get()
    character_class = class_entry.get()
    creator = CharacterCreator()
    character = creator.create_character(
        name, [], "", "", character_class, "", "", "", "", "", "", ""
    )
    if hasattr(character, "get_summary"):
        info = character.get_summary()
    else:
        info = (
            f"Name: {character.name}\n"
            f"Class: {character.character_class}\n"
            f"Spirit Bond: {character.spirit_bond}\n"
            f"{character.spirit_bond_description}"
        )
    character_info_label.config(text=info)

root = tk.Tk()
root.title("VFTD Character Sheet")
root.geometry("600x400")

tk.Label(root, text="Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Class:").pack()
class_entry = tk.Entry(root)
class_entry.pack()

tk.Button(root, text="Create Character", command=create_character).pack()

character_info_label = tk.Label(root, text="", justify="left", wraplength=400)
character_info_label.pack()

root.mainloop()