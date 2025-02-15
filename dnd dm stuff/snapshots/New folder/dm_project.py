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

































# SECTION 7: Confirm Scores and Transition to Primary Skills Selection
def show_primary_skills_screen(character_data):
    # Clear existing widgets and show primary skills screen
    for widget in window.winfo_children():
        widget.destroy()

    # Placeholder for primary skills selection
    title_label = tk.Label(window, text="Select Your Primary Skills", font=("Arial", 16, "bold"))
    title_label.place(x=200, y=30)

    # Instructions
    instructions_label = tk.Label(window, text="Pick your primary skills based on your class.", font=("Arial", 12))
    instructions_label.place(x=50, y=80)

    # Sample primary skills selection (would need to be updated based on class/race)
    skills = ["Bluff", "Climb", "Diplomacy", "Hide", "Jump", "Listen"]
    skill_checkboxes = {}
    y_position = 130  # Starting Y position for skill checkboxes

    for skill in skills:
        var = tk.IntVar()
        checkbox = tk.Checkbutton(window, text=skill, variable=var)
        checkbox.place(x=50, y=y_position)
        skill_checkboxes[skill] = var  # Store the selected values
        y_position += 30  # Move down for the next checkbox

    # Submit button to proceed to the character sheet
    def on_submit_primary_skills():
        # In this simplified version, we're just proceeding to the character sheet
        show_character_sheet(character_data)

    submit_button = tk.Button(window, text="Submit", font=("Arial", 12), command=on_submit_primary_skills)
    submit_button.place(x=50, y=y_position + 20)


# SECTION 7: Confirm Scores (Updated to go to Primary Skills Selection)
def confirm_scores(character_data, setting, ability_scores):
    if len(ability_scores) != 6:
        messagebox.showerror("Error", "Each ability must have a unique score.")
        return
    
    # Save the ability scores to the character data
    character_data["ability_scores"] = ability_scores
    
    # Show the primary skills selection screen after confirming the scores
    show_primary_skills_screen(character_data)


























# SECTION 8: Skills
def generate_skills_section(character_data):
    """Generates and organizes the skills for a character."""
    # Full D&D 3.5 Skills list
    full_skills_list = [
        "Appraise", "Balance", "Bluff", "Climb",
        "Concentration", "Craft (Alchemy)", "Craft (Armor)",
        "Craft (Weaponsmithing)", "Decipher Script", "Diplomacy",
        "Disable Device", "Disguise", "Escape Artist", "Forgery",
        "Gather Information", "Handle Animal", "Heal", "Hide",
        "Intimidate", "Jump", "Knowledge (Arcana)", 
        "Knowledge (Dungeoneering)", "Knowledge (Engineering)", 
        "Knowledge (Geography)", "Knowledge (History)", 
        "Knowledge (Local)", "Knowledge (Nature)", 
        "Knowledge (Nobility)", "Knowledge (Religion)", 
        "Knowledge (The Planes)", "Listen", "Move Silently", 
        "Open Lock", "Perform (Dance)", "Perform (Sing)", 
        "Profession (Sailor)", "Profession (Cook)", "Ride", 
        "Search", "Sense Motive", "Sleight of Hand", 
        "Spellcraft", "Spot", "Survival", "Swim", 
        "Tumble", "Use Magic Device", "Use Rope"
    ]

    # Split the full list into two columns
    mid_index = len(full_skills_list) // 2
    return [full_skills_list[:mid_index], full_skills_list[mid_index:]]





            
            



















            
            












# SECTION 9: Character Sheet Display (with Skill Modifiers)
def show_character_sheet(character_data):
    # Clear existing widgets
    for widget in window.winfo_children():
        widget.destroy()

    # Title
    title_label = tk.Label(window, text="Character Sheet", font=("Arial", 16, "bold"))
    title_label.place(x=200, y=30)

    # Character Info (Name, Race, Class, Level, Alignment)
    tk.Label(window, text=f"Name: {character_data.get('name', 'Unknown')}", font=("Arial", 12)).place(x=50, y=80)
    tk.Label(window, text=f"Race: {character_data.get('race', 'Unknown')}", font=("Arial", 12)).place(x=50, y=110)
    tk.Label(window, text=f"Class: {character_data.get('class', 'Unknown')}", font=("Arial", 12)).place(x=50, y=140)
    tk.Label(window, text=f"Level: {character_data.get('level', 1)}", font=("Arial", 12)).place(x=50, y=170)
    tk.Label(window, text=f"Alignment: {character_data.get('alignment', 'Neutral')}", font=("Arial", 12)).place(x=50, y=200)

    # Ability Scores Section (Vertical Layout with absolute positioning)
    tk.Label(window, text="Ability Scores:", font=("Arial", 12, "bold")).place(x=50, y=240)
    ability_scores = character_data.get("ability_scores", {})
    y_position = 270  # Starting Y position for ability scores

    abilities = list(ability_scores.keys())
    for ability in abilities:
        tk.Label(window, text=f"{ability}: {ability_scores[ability]}", font=("Arial", 12)).place(x=50, y=y_position)
        y_position += 30  # Adjust the vertical position for the next ability score

    # Skills Section (2-column layout with absolute positioning and modifier boxes)
    tk.Label(window, text="Skills:", font=("Arial", 12, "bold")).place(x=200, y=240)
    skills_columns = generate_skills_section(character_data)

    # Positioning skills in two columns with modifier boxes
    x_offset = 250  # Starting X position for the first column
    y_offset = 240  # Starting Y position for the skills section

    # Create skill labels and entry boxes for modifiers
    skill_entries = {}  # Dictionary to store entry boxes for modifiers
    for col_idx, column_skills in enumerate(skills_columns):
        for row_idx, skill in enumerate(column_skills):
            x_position = x_offset + (col_idx * 250)  # Adjust for the second column
            y_position = y_offset + (row_idx * 20)  # Adjust for vertical spacing
            skill_label = tk.Label(window, text=skill, font=("Arial", 12))
            skill_label.place(x=x_position, y=y_position)

            # Create an entry box for the modifier, adjusted x-position for more spacing
            modifier_entry = tk.Entry(window, font=("Arial", 12), width=5)
            modifier_entry.place(x=x_position + 200, y=y_position - 3)  # Increased the x_offset to add more space

            # Store the entry box in the dictionary for later use (optional)
            skill_entries[skill] = modifier_entry

    # Back Button to go to the main menu
    tk.Button(window, text="Back to Main Menu", command=main_window).place(x=50, y=y_position + 250)

    # This skill_entries dictionary will be used later for calculating and displaying actual skill modifiers






























# SECTION 10: Main Initialization

window = tk.Tk()
window.title("DM Program")
window.geometry(WINDOW_WIDTH)  # Define your window dimensions

def main_window():
    # Set up the main screen/UI for the application
    tk.Label(window, text="Welcome to the D&D 3.5 Character Generator", font=FONT_TITLE).pack(pady=20)
    
    # Button to start the character creation process
    tk.Button(window, text="Create Character", command=lambda: update_frame(lambda: create_character("default"))).pack(pady=10)
    
    # Button to generate a character sheet PDF (you can add logic here to pass the correct character data)
    tk.Button(window, text="Generate Character Sheet", command=lambda: generate_character_sheet(character_data)).pack(pady=10)
    
    # Button to quit the program
    tk.Button(window, text="Quit", command=window.quit).pack(pady=10)

# Call the main window function to display the UI
main_window()

# Start the tkinter event loop to display the window
window.mainloop()