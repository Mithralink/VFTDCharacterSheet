import json
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, simpledialog
from main import CharacterCreator, item_db
import os



CHARACTER_DIR = "characters"
os.makedirs(CHARACTER_DIR, exist_ok=True)



root = tk.Tk()
root.title("VFTD Character Sheet")
root.geometry("600x400")

# Theme
root.tk.call("source", "Azure-ttk-theme-main/azure.tcl")
style = ttk.Style(root)
style.theme_use("azure-dark")
root.tk.call("set_theme", "dark")



# Main character info (Name, Class, Race, Level)
main_info_frame = tk.LabelFrame(root, text="Character Info", padx=8, pady=4)
main_info_frame.pack(pady=4, fill="x")
name_label = tk.Label(main_info_frame, text="Name: --")
name_label.grid(row=0, column=0, sticky="w")
class_label = tk.Label(main_info_frame, text="Class: --")
class_label.grid(row=0, column=1, sticky="w", padx=10)
archetype_label = tk.Label(main_info_frame, text="Archetype: --")
archetype_label.grid(row=0, column=2, sticky="w", padx=10)
race_label = tk.Label(main_info_frame, text="Race: --")
race_label.grid(row=0, column=3, sticky="w", padx=10)
level_label = tk.Label(main_info_frame, text="Level: --")
level_label.grid(row=0, column=4, sticky="w", padx=10)

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
    stat_labels["hp_label"].config(text=f"{character.hit_points}")
    stat_labels["grit_label"].config(text=f"{character.grit}")
    stat_labels["sanity_label"].config(text=f"{character.sanity}")
    spirit_bond_label.config(text=f"Spirit Bond: {character.spirit_bond}")
    spirit_desc_label.config(text=f"Spirit Bond Description: {character.spirit_bond_description}")
    archetype_label.config(text=f"Archetype: {character.archetype}")



# Define dropdown options
class_options = ["Warrior", "Rogue", "Sartor", "Zealot", "Dungeoneer"]
race_options = ["Fjoran", "Shaelarae", "Talii", "Human", "Bassyrikin"]
spirit_bond_options = [
    "Vulkjoran", "Korvyran", "Akathian", "Fean", "Unbound", "Bassyric", "Silean"
]
class_archetypes = {
    "Warrior": [
        "barbarian", "caestus", "fighter", "knight", "ward", "pirate", "ranger", "scarsan"
    ],
    "Rogue": [
        "acrobat", "assassin", "bandit", "pirate", "thief", "scarsan"
    ],
    "Sartor": [
        "cometologist ", "doorlock", "elementalist", "maester", "sorcerer", "warlock", "sanctioned sartor"
    ],
    "Zealot": [
        "silean", "crusader", "bassyric", "desert fean", "vulkjoran", "lost akathian", "oracle", "apostle of korvyre"
    ],
    "Dungeoneer": [
        "censerer", "alchemist", "archaeologist", "barber surgeon", "engineer",
        "expeditioner", "explorer", "field researcher", "scarsan"
    ],
}

input_frame = tk.Frame(root)
input_frame.pack(pady=10)

archetype_var = tk.StringVar()
archetype_entry = ttk.Combobox(input_frame, textvariable=archetype_var, values=[], state="readonly")

fields = [
    ("Name:", tk.Entry(input_frame)),
    ("Class:", ttk.Combobox(input_frame, values=class_options, state="readonly")),
    ("Archetype:", archetype_entry),
    ("Level:", tk.Entry(input_frame)),
    ("Race:", ttk.Combobox(input_frame, values=race_options, state="readonly")),
    ("Spirit Bond:", ttk.Combobox(input_frame, values=spirit_bond_options, state="readonly")),
]


def update_archetype_options(event=None):
    selected_class = class_entry.get()
    archetypes = class_archetypes.get(selected_class, [])
    archetype_entry["values"] = archetypes
    archetype_var.set("")  # Clear selection



# Place fields in grid, wrap after 5 fields (2 columns per field: label and entry)
for i, (label_text, entry) in enumerate(fields):
    row = i // 5  # 5 fields per row
    col = (i % 5) * 2
    tk.Label(input_frame, text=label_text).grid(row=row, column=col, padx=5, pady=5)
    entry.grid(row=row, column=col+1, padx=5, pady=5)

# Assign entry variables for use in create_character
name_entry = fields[0][1]
class_entry = fields[1][1]
archetype_entry = fields[2][1]
level_entry = fields[3][1]
race_entry = fields[4][1]
spirit_bond_entry = fields[5][1]

class_entry.bind("<<ComboboxSelected>>", update_archetype_options)

# Sidebar for main actions
sidebar_frame = tk.LabelFrame(root, text="Character Creation", padx=8, pady=4)
sidebar_frame.pack(side="left", fill="y", padx=8, pady=8)

# Create Character button below the input fields
create_btn = tk.Button(sidebar_frame, text="Create New Character", command=lambda: create_character())
create_btn.pack(pady=6, fill="x")

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

# HP, Grit, Sanity boxes
stats_boxes_frame = tk.Frame(root)
stats_boxes_frame.pack(pady=5)

stat_names = [("HP", "hp_label"), ("Grit", "grit_label"), ("Sanity", "sanity_label")]
stat_labels = {}

for i, (stat, varname) in enumerate(stat_names):
    box = tk.Frame(stats_boxes_frame, relief="groove", borderwidth=2, padx=8, pady=4)
    box.grid(row=0, column=i, padx=10)
    lbl_name = tk.Label(box, text=stat, font=("Arial", 9, "bold"))
    lbl_name.pack()
    lbl_value = tk.Label(box, text="--", font=("Arial", 12))
    lbl_value.pack()
    stat_labels[varname] = lbl_value

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
    inventory_tree.delete(*inventory_tree.get_children())
    for item_name, item_info in character.inventory.items():
        inventory_tree.insert(
            "",
            "end",
            iid=item_name,
            values=(
                item_name,
                item_info["quantity"],
                item_info["load"],
                item_info["durability"]
            )
        )

def delete_selected_item():
    character = getattr(root, "current_character", None)
    if character is None:
        messagebox.showerror("Error", "No character loaded.")
        return
    selected = inventory_tree.selection()
    if not selected:
        messagebox.showerror("Error", "No item selected.")
        return
    item_name = selected[0]
    if item_name in character.inventory:
        del character.inventory[item_name]
        update_inventory_display(character)

def on_treeview_double_click(event):
    # Get the current character
    character = getattr(root, "current_character", None)
    if character is None:
        return
    # Identify the clicked region
    region = inventory_tree.identify("region", event.x, event.y)
    if region != "cell":
        return
    row_id = inventory_tree.identify_row(event.y)
    col = inventory_tree.identify_column(event.x)
    if not row_id or not col:
        return
    # Column number and column name conversion
    col_num = int(col.replace("#", "")) - 1
    columns = ["Item Name", "Quantity", "Load", "Durability"]
    col_name = columns[col_num]
    x, y, width, height = inventory_tree.bbox(row_id, col)
    value = inventory_tree.set(row_id, col_name)
    # Overlay for an entry widget
    entry = tk.Entry(inventory_tree)
    entry.place(x=x, y=y, width=width, height=height)
    entry.insert(0, value)
    entry.focus_set()

    # Save logic
    def save_edit(event=None):
        new_value = entry.get()
        entry.destroy()
        if col_name == "Item Name":
            if new_value and new_value != row_id:
                if new_value in character.inventory:
                    messagebox.showerror("Error", f"An item named '{new_value}' already exists.")
                    return
                character.inventory[new_value] = character.inventory.pop(row_id)
                update_inventory_display(character)
                inventory_tree.selection_set(new_value)
        else:
            try:
                if col_name in ["Quantity", "Load", "Durability"]:
                    if new_value == "":
                        return
                    new_value = int(new_value)
                character.inventory[row_id][col_name.lower()] = new_value
                update_inventory_display(character)
                inventory_tree.selection_set(row_id)
            except Exception as e:
                messagebox.showerror("Error", f"Invalid value: {e}")

    # Bind save logic to events
    entry.bind("<Return>", save_edit)
    entry.bind("<FocusOut>", save_edit)

notebook = ttk.Notebook(root)
notebook.pack(expand=1, fill="both")
inventory_tab = tk.Frame(notebook)
notebook.add(inventory_tab, text="Inventory")
inventory_section = tk.Frame(inventory_tab)
inventory_section.pack(pady=5)

inventory_tree = ttk.Treeview(
    inventory_section,
    columns=("Item Name", "Quantity", "Load", "Durability"),
    show="headings",
    selectmode="browse",
    height=8
)
inventory_tree.heading("Item Name", text="Item Name")
inventory_tree.heading("Quantity", text="Quantity")
inventory_tree.heading("Load", text="Load")
inventory_tree.heading("Durability", text="Durability")
inventory_tree.column("Quantity", width=70, anchor="center")
inventory_tree.column("Load", width=70, anchor="center")
inventory_tree.column("Durability", width=90, anchor="center")
inventory_tree.pack(side="left", padx=5)

inventory_input_frame = tk.Frame(inventory_section)
inventory_input_frame.pack(side="left", padx=5, fill="y")


inventory_tree.bind("<Double-1>", on_treeview_double_click)

# Adding an item

item_name_entry = tk.Entry(inventory_input_frame)
item_name_entry.pack(pady=2)
item_name_entry.insert(0, "Item Name")

item_qty_entry = tk.Entry(inventory_input_frame)
item_qty_entry.pack(pady=2)
item_qty_entry.insert(0, "Quantity")

custom_load_entry = tk.Entry(inventory_input_frame)
custom_load_entry.pack(pady=2)
custom_load_entry.insert(0, "Load (custom)")

custom_durability_entry = tk.Entry(inventory_input_frame)
custom_durability_entry.pack(pady=2)
custom_durability_entry.insert(0, "Durability (custom)")

add_item_btn = tk.Button(inventory_input_frame, text="Add Item", command=add_item_to_character)
add_item_btn.pack(pady=2)

# Deleting an item
delete_item_btn = tk.Button(inventory_input_frame, text="Delete Item", command=delete_selected_item, state="disabled")
delete_item_btn.pack(pady=2)

def on_inventory_select(event):
    selected = inventory_tree.selection()
    if selected:
        delete_item_btn.config(state="normal")
    else:
        delete_item_btn.config(state="disabled")

inventory_tree.bind("<<TreeviewSelect>>", on_inventory_select)


# Notes tab
notes_tab = tk.Frame(notebook)
notebook.add(notes_tab, text="Notes")
notes_notebook = ttk.Notebook(notes_tab)
notes_notebook.pack(expand=1, fill="both", padx=5, pady=5)

general_notes_tab = tk.Frame(notes_notebook)
session_notes_tab = tk.Frame(notes_notebook)
ally_npc_notes = tk.Frame(notes_notebook)
enemy_npc_notes = tk.Frame(notes_notebook)
goals_notes = tk.Frame(notes_notebook)
backstory_tab = tk.Frame(notes_notebook)

notes_notebook.add(general_notes_tab, text="General")
notes_notebook.add(session_notes_tab, text="Session")
notes_notebook.add(ally_npc_notes, text="Allies")
notes_notebook.add(enemy_npc_notes, text="Enemies")
notes_notebook.add(goals_notes, text="Goals")
notes_notebook.add(backstory_tab, text="Backstory")

general_text = tk.Text(general_notes_tab, wrap="word")
general_text.pack(expand=1, fill="both", padx=10, pady=10)

session_text = tk.Text(session_notes_tab, wrap="word")
session_text.pack(expand=1, fill="both", padx=10, pady=10)

ally_text = tk.Text(ally_npc_notes, wrap="word")
ally_text.pack(expand=1, fill="both", padx=10, pady=10)

enemy_text = tk.Text(enemy_npc_notes, wrap="word")
enemy_text.pack(expand=1, fill="both", padx=10, pady=10)

goals_text = tk.Text(goals_notes, wrap="word")
goals_text.pack(expand=1, fill="both", padx=10, pady=10)

backstory_text = tk.Text(backstory_tab, wrap="word")
backstory_text.pack(expand=1, fill="both", padx=10, pady=10)




def create_character():
    # Prompt for confirmation before wiping
    if messagebox.askyesno("Confirm", "Are you sure you want to wipe the current character and notes?"):
        name = name_entry.get()
        character_class = class_entry.get()
        archetype = archetype_entry.get()
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
        character.archetype = archetype
        root.current_character = character # Store for inventory use
        update_character_info_boxes(character)
        update_inventory_display(character)
        update_ability_scores_display(character)

        general_text.delete("1.0", "end")
        session_text.delete("1.0", "end")
        ally_text.delete("1.0", "end")
        enemy_text.delete("1.0", "end")
        goals_text.delete("1.0", "end")
        backstory_text.delete("1.0", "end")
    else:
        return



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
        archetype = char_data.get("archetype", "")
        character.archetype = archetype
        archetype_entry.set(archetype)
        root.current_character = character
        # Update UI fields
        name_entry.delete(0, tk.END)
        name_entry.insert(0, char_data.get("name", ""))
        class_entry.set(char_data.get("character_class", ""))
        level_entry.delete(0, tk.END)
        level_entry.insert(0, str(char_data.get("level", "")))
        race_entry.set(char_data.get("character_race", "").capitalize())
        spirit_bond_entry.set(char_data.get("spirit_bond", ""))
        # Load notes
        notes = char_data.get("notes", {})
        general_text.delete("1.0", "end")
        general_text.insert("1.0", notes.get("general", ""))
        session_text.delete("1.0", "end")
        session_text.insert("1.0", notes.get("session", ""))
        ally_text.delete("1.0", "end")
        ally_text.insert("1.0", notes.get("allies", ""))
        enemy_text.delete("1.0", "end")
        enemy_text.insert("1.0", notes.get("enemies", ""))
        goals_text.delete("1.0", "end")
        goals_text.insert("1.0", notes.get("goals", ""))
        backstory_text.delete("1.0", "end")
        backstory_text.insert("1.0", notes.get("backstory", ""))
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

load_btn = tk.Button(sidebar_frame, text="Load Character", command=load_character)
load_btn.pack(pady=6, fill="x")



# Save character to JSON
def save_character():
    character = getattr(root, "current_character", None)
    if character is None:
        messagebox.showerror("Error", "No character to save.")
        return
    if hasattr(character, "to_dict"):
        char_data = character.to_dict()
    else:
        char_data = character.__dict__
    char_data["archetype"] = getattr(character, "archetype", "")
    char_data["notes"] = {
        "general": general_text.get("1.0", "end-1c"),
        "session": session_text.get("1.0", "end-1c"),
        "allies": ally_text.get("1.0", "end-1c"),
        "enemies": enemy_text.get("1.0", "end-1c"),
        "goals": goals_text.get("1.0", "end-1c"),
        "backstory": backstory_text.get("1.0", "end-1c"),
    }
    default_name = getattr(character, "name", "character") or "character"
    file_path = filedialog.asksaveasfilename(
        defaultextension=".json",
        filetypes=[("JSON files", "*.json")],
        initialfile=f"{default_name}.json",
        initialdir=CHARACTER_DIR
    )
    if file_path:
        with open(file_path, "w") as f:
            json.dump(char_data, f, indent=4)
        messagebox.showinfo("Success", f"Character saved to {file_path}")

save_btn = tk.Button(sidebar_frame, text="Save Character", command=save_character)
save_btn.pack(pady=6, fill="x")


root.mainloop()