# SECTION 1: Data Imports
from race_data import race_data
from class_data import class_data
from collections import Counter
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import random
import tkinter as tk
from tkinter import messagebox




WINDOW_WIDTH = "600x400"  # Added this line to define the window width
FONT_TITLE = ("Arial", 16)
FONT_LABEL = ("Arial", 12)




























# SECTION 2: PDF Generation Functions
def generate_character_sheet(character_data, file_name="character_sheet.pdf"):
    """Generates a PDF character sheet."""
    c = canvas.Canvas(file_name, pagesize=letter)
    c.setFont("Helvetica-Bold", 14)

    # Title
    c.drawString(200, 750, "D&D 3.5 Character Sheet")

    # Basic Info
    c.setFont("Helvetica", 12)
    c.drawString(50, 720, f"Name: {character_data.get('name', 'Unknown')}")
    c.drawString(250, 720, f"Race: {character_data.get('race', 'Unknown')}")
    c.drawString(400, 720, f"Class: {character_data.get('class', 'Unknown')}")
    c.drawString(50, 700, f"Level: {character_data.get('level', 1)}")
    c.drawString(250, 700, f"Alignment: {character_data.get('alignment', 'Neutral')}")

    # Ability Scores
    y_position = 660
    c.drawString(50, y_position, "Ability Scores:")
    for ability, score in character_data.get("ability_scores", {}).items():
        y_position -= 20
        c.drawString(70, y_position, f"{ability}: {score}")

    # Generate and Render Skills Section
    skills_columns = generate_skills_section(character_data)
    render_skills_on_pdf(c, skills_columns)

    # Finalize PDF
    c.save()
    messagebox.showinfo("PDF Saved", f"Character sheet saved as {file_name}")





























# SECTION 3: Utility Functions
def update_frame(new_frame):
    """Clears the current window frame and sets up the new one."""
    for widget in window.winfo_children():
        widget.destroy()
    new_frame()

def roll_dice(num_dice, num_sides):
    """Rolls a specified number of dice with the given number of sides."""
    return [random.randint(1, num_sides) for _ in range(num_dice)]





























# SECTION 4: Character Creation UI
def create_character(setting):
    def submit_character():
        # Ensure all fields are filled before submitting
        if not name_entry.get() or not gender_var.get() or not race_var.get() or not class_var.get():
            messagebox.showerror("Error", "Please fill in all fields.")
            return
        # Store character data
        character_data = {
            "name": name_entry.get(),
            "gender": gender_var.get(),
            "race": race_var.get(),
            "class": class_var.get(),
            "subclass": subclass_var.get(),
            "level": 1,
            "alignment": "Neutral Neutral",
        }
        update_frame(lambda: allocate_ability_scores(character_data, setting))

    def update_description():
        # Get race description
        race_desc = race_data.get(race_var.get(), {}).get("description", "")

        # Get class and subclass descriptions
        class_selected = class_var.get()
        subclass_selected = subclass_var.get()
        class_desc = ""
        subclass_desc = ""

        # Fetch class description
        if class_selected in class_data:
            class_desc = class_data[class_selected].get("description", "")

        # Fetch subclass description
        if class_selected in class_data:
            for subclass in class_data[class_selected].get("subclasses", []):
                if subclass["name"] == subclass_selected:
                    subclass_desc = subclass["description"]

        # Update description text
        desc_text.set(
            f"Race: {race_desc}\nClass: {class_desc}\nSubclass: {subclass_desc}"
        )

    # User Interface for Name, Gender, Race, Class
    tk.Label(window, text="Character Creation", font=FONT_TITLE).pack(pady=20)
    tk.Label(window, text="Character Name:", font=FONT_LABEL).pack()
    name_entry = tk.Entry(window)
    name_entry.pack(pady=5)

    tk.Label(window, text="Gender:", font=FONT_LABEL).pack()
    gender_var = tk.StringVar(value="") 
    gender_menu = tk.OptionMenu(window, gender_var, "Male", "Female", "Other")
    gender_menu.pack(pady=5)

    tk.Label(window, text="Race:", font=FONT_LABEL).pack()
    race_var = tk.StringVar(value="")
    race_menu = tk.OptionMenu(window, race_var, *race_data.keys())  # Populate with race options from race_data
    race_menu.pack(pady=5)
    race_var.trace_add("write", lambda *args: update_description())  # Update description on race change

    tk.Label(window, text="Class:", font=FONT_LABEL).pack()
    class_var = tk.StringVar(value="")
    class_menu = tk.OptionMenu(window, class_var, *class_data.keys())  # Populate with class options from class_data
    class_menu.pack(pady=5)
    class_var.trace_add("write", lambda *args: update_subclasses(class_var, subclass_var, subclass_menu))  # Update subclasses
    class_var.trace_add("write", lambda *args: update_description())  # Update description on class change

    # Define subclass_menu here
    subclass_var = tk.StringVar(value="")
    subclass_menu = tk.OptionMenu(window, subclass_var, "")  # Initially empty, will populate with subclasses
    subclass_menu.pack(pady=5)

    # Call update_subclasses when class selection changes
    tk.Label(window, text="Subclass:", font=FONT_LABEL).pack()
    subclass_var.trace_add("write", lambda *args: update_description())  # Update description on subclass change

    # Define desc_text as a StringVar before calling update_description
    desc_text = tk.StringVar()
    tk.Label(window, textvariable=desc_text, font=FONT_LABEL, wraplength=500, justify="left").pack(pady=10)

    tk.Button(window, text="Next", command=submit_character).pack(pady=20)
    
    
    





















# SECTION 5: Update Subclasses Function
def update_subclasses(class_var, subclass_var, subclass_menu):
    selected_class = class_var.get()
    if selected_class in class_data:
        subclasses = class_data[selected_class].get("subclasses", [])
        if subclasses:
            subclass_var.set(subclasses[0]["name"])  # Set the first subclass as default
        subclass_menu["menu"].delete(0, "end")  # Clear the existing menu
        for subclass in subclasses:
            subclass_menu["menu"].add_command(label=subclass["name"], command=tk._setit(subclass_var, subclass["name"]))
    else:
        subclass_var.set("")
        subclass_menu["menu"].delete(0, "end")































# SECTION 6: Ability Scores and Allocation
def allocate_ability_scores(character_data, setting):
    # Roll six ability scores using 4d6, drop the lowest, and sort the scores
    scores = [sum(sorted(roll_dice(4, 6))[1:]) for _ in range(6)]
    scores.sort(reverse=True)  # Sort scores in descending order

    ability_scores = {}
    abilities = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]

    def update_dropdowns():
        assigned_counts = Counter(ability_scores.values())
        for idx, var in enumerate(score_vars):
            current_value = var.get()
            remaining_scores = []
            temp_counts = Counter(scores) - assigned_counts

            for score, count in temp_counts.items():
                remaining_scores.extend([str(score)] * count)

            if current_value.isdigit():
                remaining_scores.append(current_value)
            remaining_scores = sorted(set(remaining_scores), key=lambda x: int(x))

            menu = dropdowns[idx]["menu"]
            menu.delete(0, "end")
            for score in remaining_scores:
                menu.add_command(label=score, command=tk._setit(var, score))

    def on_score_change(*args):
        for idx, var in enumerate(score_vars):
            if var.get().isdigit():
                ability_scores[abilities[idx]] = int(var.get())
            else:
                ability_scores.pop(abilities[idx], None)
        update_dropdowns()

    tk.Label(window, text=f"Rolled Scores: {', '.join(map(str, scores))}", font=FONT_LABEL).pack(pady=10)

    score_vars = []
    dropdowns = []

    for ability in abilities:
        tk.Label(window, text=ability, font=FONT_LABEL).pack()
        var = tk.StringVar(value="Select a score")
        dropdown = tk.OptionMenu(window, var, *map(str, scores))
        dropdown.pack()
        score_vars.append(var)
        dropdowns.append(dropdown)
        var.trace_add("write", on_score_change)

    tk.Button(window, text="Confirm", command=lambda: confirm_scores(character_data, setting, ability_scores)).pack(pady=20)

































# SECTION 7: Confirm Scores
def confirm_scores(character_data, setting, ability_scores):
    if len(ability_scores) != 6:
        messagebox.showerror("Error", "Each ability must have a unique score.")
        return
    character_data["ability_scores"] = ability_scores
    generate_character_sheet(character_data)  # Generate the character sheet
    messagebox.showinfo(
        "Character Created",
        f"Your character {character_data['name']} is a {character_data['gender']} {character_data['race']} {character_data['class']} ({character_data['subclass']}) in a {setting} world.\n\nAbility Scores:\n" + "\n".join([f"{ability}: {score}" for ability, score in ability_scores.items()])
    )
    save_game(character_data, setting)
    update_frame(main_window)


























# SECTION 10: Skills
def generate_skills_section(character_data):
    """Generates and organizes the skills for a character."""
    # Full D&D 3.5 Skills list
    full_skills_list = [
        "Appraise (Int)", "Balance (Dex)", "Bluff (Cha)", "Climb (Str)",
        "Concentration (Con)", "Craft (Alchemy) (Int)", "Craft (Armor) (Int)",
        "Craft (Weaponsmithing) (Int)", "Decipher Script (Int)", "Diplomacy (Cha)",
        "Disable Device (Int)", "Disguise (Cha)", "Escape Artist (Dex)", "Forgery (Int)",
        "Gather Information (Cha)", "Handle Animal (Cha)", "Heal (Wis)", "Hide (Dex)",
        "Intimidate (Cha)", "Jump (Str)", "Knowledge (Arcana) (Int)", 
        "Knowledge (Dungeoneering) (Int)", "Knowledge (Engineering) (Int)", 
        "Knowledge (Geography) (Int)", "Knowledge (History) (Int)", 
        "Knowledge (Local) (Int)", "Knowledge (Nature) (Int)", 
        "Knowledge (Nobility) (Int)", "Knowledge (Religion) (Int)", 
        "Knowledge (The Planes) (Int)", "Listen (Wis)", "Move Silently (Dex)", 
        "Open Lock (Dex)", "Perform (Dance) (Cha)", "Perform (Sing) (Cha)", 
        "Profession (Sailor) (Wis)", "Profession (Cook) (Wis)", "Ride (Dex)", 
        "Search (Int)", "Sense Motive (Wis)", "Sleight of Hand (Dex)", 
        "Spellcraft (Int)", "Spot (Wis)", "Survival (Wis)", "Swim (Str)", 
        "Tumble (Dex)", "Use Magic Device (Cha)", "Use Rope (Dex)"
    ]

    # Split the full list into two columns
    mid_index = len(full_skills_list) // 2
    return [full_skills_list[:mid_index], full_skills_list[mid_index:]]

def render_skills_on_pdf(canvas_obj, skills_columns):
    """Renders skills on the PDF in two columns, with spaces for skill modifiers."""
    # Table settings
    table_x_start = 180  # Leftmost starting position
    table_y_start = 630  # Topmost starting position
    column_width = 210  # Width of each column
    row_height = 20  # Height of each row
    modifier_box_width = 30  # Width of the skill modifier box
    vertical_offset = 5  # Final vertical offset for alignment

    canvas_obj.setFont("Helvetica", 10)

    # Draw table with modifier spaces
    for col_idx, column_skills in enumerate(skills_columns):
        for row_idx, skill in enumerate(column_skills):
            x_skill = table_x_start + (col_idx * column_width) + 10
            x_modifier = x_skill + column_width - modifier_box_width - 10
            y_position = table_y_start - (row_idx * row_height) - 15

            # Draw skill name
            canvas_obj.drawString(x_skill, y_position, skill)

            # Draw box for modifier
            canvas_obj.rect(x_modifier, y_position + vertical_offset - 10, modifier_box_width, 15)

    # Draw the full table borders
    table_width = column_width * 2
    table_height = len(skills_columns[0]) * row_height
    canvas_obj.setStrokeColorRGB(0, 0, 0)  # Black color for table borders
    canvas_obj.rect(table_x_start, table_y_start - table_height, table_width, table_height)
    canvas_obj.line(
        table_x_start + column_width,
        table_y_start,
        table_x_start + column_width,
        table_y_start - table_height
    )




            
            














            
            












# SECTION 8: Main Window
def main_window():
    def select_setting():
        def choose_setting(setting):
            update_frame(lambda: create_character(setting))

        update_frame(lambda: [
            tk.Label(window, text="Choose a Setting", font=FONT_TITLE).pack(pady=20),
            tk.Button(window, text="Fantasy", width=20, command=lambda: choose_setting("Fantasy")).pack(pady=10),
            tk.Button(window, text="Sci-fi", width=20, command=lambda: choose_setting("Sci-fi")).pack(pady=10),
            tk.Button(window, text="Horror", width=20, command=lambda: choose_setting("Horror")).pack(pady=10)
        ])

    tk.Label(window, text="Welcome to the DM Program!", font=FONT_TITLE).pack(pady=20)
    tk.Button(window, text="New Game", width=20, command=select_setting).pack(pady=20)



























# SECTION 9: Main Initialization
window = tk.Tk()
window.title("DM Program")
window.geometry(WINDOW_WIDTH)

main_window()
window.mainloop()
