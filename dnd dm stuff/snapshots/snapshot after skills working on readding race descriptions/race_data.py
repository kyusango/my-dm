# Updates to race_data to include skill_modifiers
def update_race_data_for_skills():
    """Update race_data with skill modifiers."""
    race_data = {
        "Elf": {
            "description": "Elves are known for their grace and intelligence, as well as their keen senses.",
            "male": "Slim build, angular features, keen eyes.",
            "female": "Slim build, angular features, sharp ears.",
            "level_adjustment": 0,
            "skill_modifiers": {
                "Spot": 2,
                "Listen": 2
            }
        },
        "Dwarf": {
            "description": "Dwarves are sturdy and strong, with a knack for stonework and metallurgy.",
            "male": "Stocky build, long beards, strong arms.",
            "female": "Stocky build, braided hair, strong arms.",
            "level_adjustment": 0,
            "skill_modifiers": {
                "Appraise": 2
            }
        },
        "Halfling": {
            "description": "Halflings are nimble and resourceful, known for their cheerful demeanor.",
            "male": "Small, agile, curly hair.",
            "female": "Small, agile, cheerful expression.",
            "level_adjustment": 0,
            "skill_modifiers": {
                "Move Silently": 2
            }
        },
        "Human": {
            "description": "Humans are versatile and adaptable, excelling in a variety of fields.",
            "male": "Varied build, determined expression.",
            "female": "Varied build, determined expression.",
            "level_adjustment": 0,
            "skill_modifiers": {}
        },
        "Gnome": {
            "description": "Gnomes are inventive and curious, known for their illusion magic.",
            "male": "Short, stocky, often with a mischievous smile.",
            "female": "Short, stocky, often with bright eyes.",
            "level_adjustment": 0,
            "skill_modifiers": {
                "Craft": 2,
                "Alchemy": 2
            }
        },
        "Half-Elf": {
            "description": "Half-Elves are versatile, blending the grace of elves with the adaptability of humans.",
            "male": "Slender build, slightly pointed ears.",
            "female": "Slender build, elegant features.",
            "level_adjustment": 0,
            "skill_modifiers": {
                "Diplomacy": 2,
                "Gather Information": 2
            }
        },
        "Half-Orc": {
            "description": "Half-Orcs are strong and resilient, inheriting traits from their orc heritage.",
            "male": "Muscular build, prominent tusks.",
            "female": "Muscular build, strong features.",
            "level_adjustment": 0,
            "skill_modifiers": {
                "Intimidate": 2
            }
        },
        "Goblin": {
            "description": "Goblins are sneaky and agile, often underestimated for their cunning.",
            "male": "Small, wiry, sharp features.",
            "female": "Small, wiry, sharp features.",
            "level_adjustment": 0,
            "skill_modifiers": {
                "Hide": 4
            }
        },
        "Orc": {
            "description": "Orcs are brutish and strong, often feared for their ferocity in battle.",
            "male": "Large build, prominent tusks, fierce expression.",
            "female": "Large build, fierce expression.",
            "level_adjustment": 0,
            "skill_modifiers": {
                "Strength": 2
            }
        },
        "Svirfneblin": {
            "description": "Deep Gnomes are reclusive and highly skilled in stealth and stonecraft.",
            "male": "Short, wiry, earthy colors.",
            "female": "Short, wiry, earthy colors.",
            "level_adjustment": 1,
            "skill_modifiers": {
                "Hide": 4,
                "Move Silently": 2
            }
        },
        "Tiefling": {
            "description": "Tieflings are marked by their infernal heritage, with cunning and charisma.",
            "male": "Slim build, horns, and a tail.",
            "female": "Slim build, horns, and a tail.",
            "level_adjustment": 1,
            "skill_modifiers": {
                "Bluff": 2,
                "Hide": 2
            }
        },
        "Aasimar": {
            "description": "Aasimar are descended from celestial beings, radiating divine energy.",
            "male": "Tall, glowing aura, noble features.",
            "female": "Tall, glowing aura, noble features.",
            "level_adjustment": 1,
            "skill_modifiers": {
                "Diplomacy": 2,
                "Spot": 2
            }
        },
        "Dragonborn": {
            "description": "Dragonborn are proud and honorable, embodying draconic traits.",
            "male": "Dragon-like features, scales, and strong build.",
            "female": "Dragon-like features, scales, and strong build.",
            "level_adjustment": 0,
            "skill_modifiers": {
                "Intimidate": 2
            }
        },
        "Warforged": {
            "description": "Warforged are living constructs, designed for durability and utility.",
            "male": "Metallic body, sturdy build.",
            "female": "Metallic body, sturdy build.",
            "level_adjustment": 0,
            "skill_modifiers": {
                "Craft": 2
            }
        },
        "Kobold": {
            "description": "Kobolds are small and clever, often underestimated.",
            "male": "Small, reptilian, quick movements.",
            "female": "Small, reptilian, quick movements.",
            "level_adjustment": 0,
            "skill_modifiers": {
                "Trapmaking": 2
            }
        }
    }
    return race_data

# Ensure race_data is available when the program runs
race_data = update_race_data_for_skills()