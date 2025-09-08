import json
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from main import CharacterCreator, item_db



root = tk.Tk()
root.title("VFTD Character Sheet")
root.geometry("600x400")

# Theme
root.tk.call("source", "Azure-ttk-theme-main/azure.tcl")
style = ttk.Style(root)
style.theme_use("azure-dark")
root.tk.call("set_theme", "dark")



# Main info (Name, Class, Race, Level)
main_info_frame = tk.LabelFrame(root, text="Character Info", padx=8, pady=4)
main_info_frame.pack(pady=4, fill="x")
name_label = tk.Label(main_info_frame, text="Name: --")
name_label.grid(row=0, column=0, sticky="w")
class_label = tk.Label(main_info_frame, text="Class: --")
class_label.grid(row=0, column=1, sticky="w", padx=10)
race_label = tk.Label(main_info_frame, text="Race: --")
race_label.grid(row=0, column=2, sticky="w", padx=10)
level_label = tk.Label(main_info_frame, text="Level: --")
level_label.grid(row=0, column=3, sticky="w", padx=10)

# HP, Grit, Sanity
stats_frame = tk.LabelFrame(root, text="Stats", padx=8, pady=4)
stats_frame.pack(pady=4, fill="x")
hp_label = tk.Label(stats_frame, text="HP: --")
hp_label.grid(row=0, column=0, sticky="w")
grit_label = tk.Label(stats_frame, text="Grit: --")
grit_label.grid(row=0, column=1, sticky="w", padx=10)
sanity_label = tk.Label(stats_frame, text="Sanity: --")
sanity_label.grid(row=0, column=2, sticky="w", padx=10)

# Spirit Bond
spirit_frame = tk.LabelFrame(root, text="Spirit Bond", padx=8, pady=4)
spirit_frame.pack(pady=4, fill="x")
spirit_bond_label = tk.Label(spirit_frame, text="Spirit Bond: --")
spirit_bond_label.pack(anchor="w")
spirit_desc_label = tk.Label(spirit_frame, text="Spirit Bond Description: --", wraplength=500, justify="left")
spirit_desc_label.pack(anchor="w")

# Update function for these boxes
def update_character_info_boxes(character):
    name_label.config(text=f"Name: {character.name}")
    class_label.config(text=f"Class: {character.character_class}")
    race_label.config(text=f"Race: {character.character_race}")
    level_label.config(text=f"Level: {character.level}")
    hp_label.config(text=f"HP: {character.hit_points}")
    grit_label.config(text=f"Grit: {character.grit}")
    sanity_label.config(text=f"Sanity: {character.sanity}")
    spirit_bond_label.config(text=f"Spirit Bond: {character.spirit_bond}")
    spirit_desc_label.config(text=f"Spirit Bond Description: {character.spirit_bond_description}")


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
create_btn = tk.Button(root, text="Create Character", command=lambda: create_character())
create_btn.pack(pady=10)

# Ability score boxes
abilities_frame = tk.Frame(root)
abilities_frame.pack(pady=5)

ability_names = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]
ability_score_labels = []
ability_mod_labels = []

for i, abbr in enumerate(ability_names):
    box = tk.Frame(abilities_frame, relief="groove", borderwidth=2, padx=4, pady=2)
    box.grid(row=0, column=i, padx=3)
    lbl_name = tk.Label(box, text=abbr, font=("Arial", 9, "bold"))
    lbl_name.pack()
    lbl_score = tk.Label(box, text="--", font=("Arial", 12))
    lbl_score.pack()
    lbl_mod = tk.Label(box, text="(--)")
    lbl_mod.pack()
    ability_score_labels.append(lbl_score)
    ability_mod_labels.append(lbl_mod)


def update_ability_scores_display(character):
    if hasattr(character, "ability_scores") and hasattr(character, "mods"):
        for i in range(6):
            score = character.ability_scores[i]
            mod = character.mods[i]
            mod_str = f"+{mod}" if mod >= 0 else str(mod)
            ability_score_labels[i].config(text=str(score))
            ability_mod_labels[i].config(text=f"({mod_str})")
    else:
        for lbl in ability_score_labels + ability_mod_labels:
            lbl.config(text="--")



# Inventory Management
def add_item_to_character():
    character = getattr(root, "current_character", None)
    if character is None:
        messagebox.showerror("Error", "No character to add items to.")
        return
    item_name = item_name_entry.get()
    item_qty = item_qty_entry.get()
    try:
        item_qty = int(item_qty)
    except ValueError:
        item_qty = 0
    try:
        character.add_item(
            item_name,
            item_qty,
            item_db=item_db,
            load=custom_load_entry.get() if custom_load_entry.get() else None,
            durability=custom_durability_entry.get() if custom_durability_entry.get() else None
        )
        update_inventory_display(character)
        item_name_entry.delete(0, tk.END)
        item_qty_entry.delete(0, tk.END)
        custom_load_entry.delete(0, tk.END)
        custom_durability_entry.delete(0, tk.END)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def update_inventory_display(character):
    inventory_listbox.delete(0, tk.END)
    for item_name, item_info in character.inventory.items():
        inventory_listbox.insert(
            tk.END,
            f"{item_name} (x{item_info['quantity']}) [Load: {item_info['load']}, Durability: {item_info['durability']}]"
        )

def delete_selected_item():
    character = getattr(root, "current_character", None)
    if character is None:
        messagebox.showerror("Error", "No character loaded.")
        return
    selection = inventory_listbox.curselection()
    if not selection:
        messagebox.showerror("Error", "No item selected.")
        return
    # Get the item name from the selected line
    selected_text = inventory_listbox.get(selection[0])
    item_name = selected_text.split(" (x")[0]
    if item_name in character.inventory:
        del character.inventory[item_name]
        update_inventory_display(character)

inventory_section = tk.Frame(root)
inventory_section.pack(pady=5)

# Inventory list on the left
inventory_listbox = tk.Listbox(inventory_section, width=50)
inventory_listbox.pack(side="left", padx=5)

# Input and button on the right
inventory_input_frame = tk.Frame(inventory_section)
inventory_input_frame.pack(side="left", padx=5, fill="y")

item_name_entry = tk.Entry(inventory_input_frame)
item_name_entry.pack(pady=2)
item_name_entry.insert(0, "Item Name")

item_qty_entry = tk.Entry(inventory_input_frame)
item_qty_entry.pack(pady=2)
item_qty_entry.insert(0, "Quantity")

add_item_btn = tk.Button(inventory_input_frame, text="Add Item", command=add_item_to_character)
add_item_btn.pack(pady=2)

custom_load_entry = tk.Entry(inventory_input_frame)
custom_load_entry.pack(pady=2)
custom_load_entry.insert(0, "Load (custom)")

custom_durability_entry = tk.Entry(inventory_input_frame)
custom_durability_entry.pack(pady=2)
custom_durability_entry.insert(0, "Durability (custom)")

delete_item_btn = tk.Button(inventory_input_frame, text="Delete Item", command=delete_selected_item)
delete_item_btn.pack(pady=2)



def create_character():
    name = name_entry.get()
    character_class = class_entry.get()
    level_str = level_entry.get()
    try:
        level = int(level_str)
    except ValueError:
        level = ""
    character_race = race_entry.get().lower()  # Apply .lower() to race input
    spirit_bond = spirit_bond_entry.get()
    creator = CharacterCreator()
    character = creator.create_character(
        name, [], level, character_race, character_class, "", "", "", "", "", "", spirit_bond
    )
    root.current_character = character # Store for inventory use
    update_character_info_boxes(character)
    update_inventory_display(character)
    update_ability_scores_display(character)



# Load character
def load_character():
    file_path = filedialog.askopenfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
    if not file_path:
        return
    try:
        with open(file_path, "r") as f:
            char_data = json.load(f)
        # Create a new Character instance from loaded data
        creator = CharacterCreator()
        # You may need to adjust this if your CharacterCreator expects different arguments
        character = creator.create_character(
            char_data.get("name", ""),
            char_data.get("ability_scores", []),
            char_data.get("level", ""),
            char_data.get("character_race", ""),
            char_data.get("character_class", ""),
            char_data.get("hit_points", ""),
            "", "", "", "", "",  # mods, sanity, grit, prof, hit_dice (let Character handle defaults)
            char_data.get("spirit_bond", "")
        )
        # Restore inventory if present
        if "inventory" in char_data:
            character.inventory = char_data["inventory"]
        root.current_character = character
        # Update UI fields
        name_entry.delete(0, tk.END)
        name_entry.insert(0, char_data.get("name", ""))
        class_entry.set(char_data.get("character_class", ""))
        level_entry.delete(0, tk.END)
        level_entry.insert(0, str(char_data.get("level", "")))
        race_entry.set(char_data.get("character_race", "").capitalize())
        spirit_bond_entry.set(char_data.get("spirit_bond", ""))
        # Update summary and inventory display
        if hasattr(character, "get_summary"):
            info = character.get_summary()
        else:
            info = f"Name: {character.name}\nClass: {character.character_class}\nRace: {character.character_race}\nSpirit Bond: {character.spirit_bond}\n{character.spirit_bond_description}"
        update_character_info_boxes(character)
        update_inventory_display(character)
        update_ability_scores_display(character)
        messagebox.showinfo("Success", f"Character loaded from {file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load character: {e}")

load_btn = tk.Button(root, text="Load Character", command=load_character)
load_btn.pack(pady=5)



# Save character to JSON
def save_character():
    character = getattr(root, "current_character", None)
    if character is None:
        messagebox.showerror("Error", "No character to save.")
        return
    # Convert character to dict (implement to_dict if needed)
    if hasattr(character, "to_dict"):
        char_data = character.to_dict()
    else:
        # Fallback: use __dict__ (may need adjustment for nested objects)
        char_data = character.__dict__
    file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
    if file_path:
        with open(file_path, "w") as f:
            json.dump(char_data, f, indent=4) # Write JSON from character sheet
        messagebox.showinfo("Success", f"Character saved to {file_path}")

save_btn = tk.Button(root, text="Save Character", command=save_character)
save_btn.pack(pady=5)


root.mainloop()