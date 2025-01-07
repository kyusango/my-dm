# Updates to race_data to include skill_modifiers
def update_race_data_for_skills():
    """Update race_data with skill modifiers."""
    race_data = {
        "Elf": {
            "description": """Elves are known for their grace, longevity, and deep connection to magic and nature. Their innate dexterity and intelligence make them natural wizards, rangers, or rogues. Elves often have keen senses, darkvision, and the ability to enter a meditative trance instead of sleep.""",
            "male": """Male elves are elegant, with sharp, angular features and a focus on artistic or martial endeavors.""",
            "female": """Female elves exhibit softer features and often exude beauty and grace, with a deep affinity for nature or magical arts.""",
            "level_adjustment": 0,
            "skill_modifiers": {
                "Spot": 2,
                "Listen": 2
            }
        },
        "Dwarf": {
            "description": """Dwarves are resilient and sturdy, renowned for their craftsmanship and combat prowess. They have natural resistance to poison, proficiency with axes and hammers, and a strong sense of community. Dwarves also possess darkvision, a necessity for life underground.""",
            "male": """Male dwarves are robust, with thick beards that signify status and pride. They excel in crafting and heavy combat roles.""",
            "female": """Female dwarves are similarly stout and strong, often playing key roles in leadership or cultural preservation.""",
            "level_adjustment": 0,
            "skill_modifiers": {
                "Appraise": 2
            }
        },
        "Halfling": {
            "description": """Halflings are small but lucky and brave, known for their cheerful demeanor and nimbleness. Their 'Lucky' trait allows them to avoid critical failures, and their dexterity and charisma make them ideal rogues, bards, or sorcerers.""",
        "male": """Male halflings are practical and curious, often venturing out as adventurers or craftsmen.""",
        "female": """Female halflings are often depicted as meticulous and socially adept, serving as community leaders or diplomats.""",
        "level_adjustment": 0,
            "skill_modifiers": {
                "Move Silently": 2
            }
        },
        "Human": {
            "description": """Humans are the most adaptable and ambitious among the common races, capable of excelling in any class or role. Their ambition and determination make them natural leaders and innovators in any setting.""",
            "male": """Human males are often slightly taller and more muscular, with a strong presence in martial or leadership roles.""",
            "female": """Human females tend to be slightly leaner and are often depicted as resourceful and diplomatic, with equal capability to excel in combat or intellectual pursuits.""",
        "level_adjustment": 0,
            "skill_modifiers": {}
        },
        "Gnome": {
            "description": """Gnomes are clever and inventive, with a natural affinity for illusion magic and mechanical tinkering. They are resistant to mind-affecting magic and possess darkvision, making them ideal wizards, artificers, or bards.""",
            "male": """Male gnomes are often eccentric inventors or alchemists, focused on creation and exploration.""",
            "female": """Female gnomes tend to be artistic or nurturing, blending creativity with practicality in their pursuits.""",
            "level_adjustment": 0,
            "skill_modifiers": {
                "Craft": 2,
                "Alchemy": 2
            }
        },
        "Half-Elf": {
            "description": """Half-elves inherit the grace of their elven lineage and the versatility of their human heritage. They are charismatic and adaptable, with darkvision and resistance to charm. Their innate social skills make them natural bards, sorcerers, or paladins.""",
            "male": """Male half-elves are often athletic and ambitious, balancing physical prowess with social adeptness.""",
            "female": """Female half-elves are graceful and charismatic, often excelling in leadership or diplomatic roles.""",
            "level_adjustment": 0,
            "skill_modifiers": {
                "Diplomacy": 2,
                "Gather Information": 2
            }
        },
        "Half-Orc": {
            "description": """Half-orcs combine the strength and endurance of their orcish heritage with human intelligence and adaptability. They are fierce warriors with darkvision and a savage attack trait that enhances their critical hits.""",
            "male": """Male half-orcs are larger and more physically imposing, often excelling as front-line combatants.""",
            "female": """Female half-orcs are equally strong but may emphasize strategy or leadership within their communities.""",
            "level_adjustment": 0,
            "skill_modifiers": {
                "Intimidate": 2
            }
        },
        "Goblin": {
            "description": """Goblins are cunning and resourceful, with small, wiry bodies. They have nimble escape abilities and darkvision, making them ideal rogues or rangers.""",
            "male": """Male goblins are typically more aggressive and physically active, excelling in combat or sneaky tactics.""",
            "female": """Female goblins are equally cunning but may emphasize strategy, manipulation, or leadership roles.""",
            "level_adjustment": 0,
            "skill_modifiers": {
                "Hide": 4
            }
        },
        "Orc": {
            "description": """Orcs are known for their immense strength and aggressive nature. They have darkvision, relentless endurance, and a cultural emphasis on combat and honor.""",
            "male": """Male orcs are larger and often serve as warriors or tribal leaders.""",
            "female": """Female orcs are just as fierce but may combine combat skills with resource management or strategic planning.""",
            "level_adjustment": 0,
            "skill_modifiers": {
                "Strength": 2
            }
        },
        "Svirfneblin": {
            "description": """Svirfneblin, or Deep Gnomes, are subterranean dwellers with a natural affinity for stealth and survival. They have darkvision and resistance to illusions, making them ideal rogues or wizards.""",
            "male": """Male Svirfneblin are pragmatic and industrious, focusing on mining or crafting.""",
            "female": """Female Svirfneblin often take on leadership or magical roles, excelling in community-focused endeavors.""",
            "level_adjustment": 1,
            "skill_modifiers": {
                "Hide": 4,
                "Move Silently": 2
            }
        },
        "Tiefling": {
            "description": """Tieflings are marked by their infernal heritage, often with horns, tails, and glowing eyes. They possess innate magic, resistance to fire, and high charisma, making them natural warlocks, sorcerers, or bards.""",
            "male": """Male tieflings have sharp, angular features and often exude an intimidating aura.""",
            "female": """Female tieflings are typically more enigmatic or seductive, using their charm and cunning to navigate social and magical challenges.""",
            "level_adjustment": 1,
            "skill_modifiers": {
                "Bluff": 2,
                "Hide": 2
            }
        },
        "Aasimar": {
            "description": """Aasimar are celestial beings with radiant appearances and a strong connection to divine energy. They have resistance to necrotic and radiant damage, darkvision, and the ability to heal others or unleash celestial power.""",
            "male": """Male aasimar are commanding and radiant, often embodying leadership and strength.""",
            "female": """Female aasimar are serene and graceful, with an ethereal beauty that inspires allies and confounds foes.""",
            "level_adjustment": 1,
            "skill_modifiers": {
                "Diplomacy": 2,
                "Spot": 2
            }
        },
        "Dragonborn": {
            "description": """Dragonborn are humanoid descendants of dragons, with scaled skin and a breath weapon unique to their lineage. They have resistance to elemental damage and a natural inclination for strength or charisma.""",
            "male": """Male dragonborn are larger, with pronounced horns or frills, and excel in physical combat.""",
            "female": """Female dragonborn are sleek and refined, often channeling their heritage into magical or strategic endeavors.""",
            "level_adjustment": 0,
            "skill_modifiers": {
                "Intimidate": 2
            }
        },
        "Warforged": {
            "description": """Warforged are living constructs, combining metal and wood, built for resilience and adaptability. They have innate armor, immunity to disease, and do not require food, drink, or sleep.""",
            "male": """Male warforged may adopt masculine traits in their design or behavior, often emphasizing strength and endurance.""",
            "female": """Female warforged might exhibit sleeker designs or nurturing roles, though these are purely aesthetic or self-assigned.""",
            "level_adjustment": 0,
            "skill_modifiers": {
                "Craft": 2
            }
        },
        "Kobold": {
            "description": """Kobolds are small dragonkin with resourceful minds and a pack mentality. They possess darkvision, are sensitive to sunlight, and gain advantages when working in groups.""",
            "male": """Male kobolds often feature larger crests or frills and focus on building or combat roles.""",
            "female": """Female kobolds are more likely to take on leadership, magical, or caretaking roles within their tribes.""",
            "level_adjustment": 0,
            "skill_modifiers": {
                "Trapmaking": 2
            }
        }
    }
    return race_data

# Ensure race_data is available when the program runs
race_data = update_race_data_for_skills()