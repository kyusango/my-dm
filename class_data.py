
class_data = {
    "Barbarian": {
        "description": "Barbarians are primal warriors who channel their rage and physical prowess to dominate the battlefield.",
    "subclasses": [
        {"name": "Berserker", "description": "Specializes in raw damage and reckless attacks."},
        {"name": "Totem Warrior", "description": "Draws strength from animal totems, gaining unique abilities."}
    ],
    "weapon_proficiencies": ["Simple weapons", "Martial weapons"],
    "armor_proficiencies": ["Light armor", "Medium armor", "Shields (except tower shields)"],
    "features": [
        {"name": "Rage", "description": "Enter a state of primal fury, gaining bonuses to Strength, Constitution, and Will saves.", "level": 1, "scaling": {1: "1/day", 4: "2/day", 8: "3/day", 12: "4/day", 16: "5/day", 20: "6/day"}},
        {"name": "Fast Movement", "description": "Gain a +10 ft bonus to base speed when not wearing heavy armor.", "level": 1},
        {"name": "Uncanny Dodge", "description": "Retain Dexterity bonus to AC even when flat-footed.", "level": 2},
        {"name": "Trap Sense", "description": "Gain a bonus on Reflex saves and AC against traps.", "level": 3, "scaling": {3: "+1", 6: "+2", 9: "+3", 12: "+4", 15: "+5", 18: "+6"}},
        {"name": "Improved Uncanny Dodge", "description": "Cannot be flanked except by a rogue of four or more levels higher.", "level": 5},
        {"name": "Damage Reduction", "description": "Gain DR X/—, reducing damage from attacks.", "level": 7, "scaling": {7: "1", 10: "2", 13: "3", 16: "4", 19: "5"}}
    ],
    "skill_modifiers": {
        "Intimidate": 2,
        "Survival": 2
    },
    "class_skills": [
        "Climb", "Craft", "Handle Animal", "Intimidate", "Jump", "Listen", "Ride", "Survival", "Swim"
    ],
    "skill_points_per_level": 4,  # Add Intelligence modifier to this
    "hit_die": "d12",
    "bab_progression": "Full",  # +1 per level
    "saving_throws": {
        "Fortitude": "Good",  # +2 at level 1
        "Reflex": "Poor",  # +0 at level 1
        "Will": "Poor"  # +0 at level 1
    },
    "leveling": {
        "milestone": True,  # Leveling is based on milestones
        "hit_points": "Roll d12 or take average (6.5 rounded up) + Constitution modifier",
        "skill_points": "4 + Intelligence modifier per level",
        "feature_unlocks": "Automatically grants class features at the appropriate levels",
        "bab_progression_formula": "Level * 1",
        "saving_throw_progression": {
            "Good": "+2 base at level 1, +1 every even level",
            "Poor": "+0 base at level 1, +1 every three levels"
        }
    }
    },
    "Bard": {
        "description": "Bards are versatile performers who blend magic, music, and lore to inspire allies, confuse enemies, and adapt to any situation.",
    "subclasses": [
        {"name": "Virtuoso", "description": "Focuses on performance and enchantments to manipulate and inspire."},
        {"name": "Skald", "description": "Combines martial prowess and song, excelling in inspiring combat performance."}
    ],
    "weapon_proficiencies": ["Simple weapons", "Longswords", "Rapiers", "Short swords", "Shortbows", "Whips"],
    "armor_proficiencies": ["Light armor", "Shields"],
    "features": [
        {"name": "Bardic Music", "description": "Use music and oration to inspire courage, counter fear, and more.", "level": 1, "scaling": {1: "1/day", 2: "2/day", 4: "3/day", 8: "4/day", 12: "5/day", 16: "6/day", 20: "7/day"}},
        {"name": "Bardic Knowledge", "description": "Add half your level to Knowledge checks for lore and trivia.", "level": 1},
        {"name": "Countersong", "description": "Use music to counter magical effects that depend on sound.", "level": 1},
        {"name": "Fascinate", "description": "Use music to enthrall creatures.", "level": 1, "scaling": {1: "1 target", 6: "2 targets", 12: "3 targets", 18: "4 targets"}},
        {"name": "Inspire Courage", "description": "Boost allies' attack and saving throws against fear and charm effects.", "level": 1, "scaling": {1: "+1", 8: "+2", 14: "+3", 20: "+4"}},
        {"name": "Inspire Competence", "description": "Improve an ally’s skill checks.", "level": 3},
        {"name": "Suggestion", "description": "Use music to influence a creature’s actions as per the spell suggestion.", "level": 6},
        {"name": "Inspire Greatness", "description": "Boost an ally's combat abilities and health.", "level": 9},
        {"name": "Song of Freedom", "description": "Use music to break enchantments on allies.", "level": 12},
        {"name": "Inspire Heroics", "description": "Boost saving throws and AC for allies.", "level": 15},
        {"name": "Mass Suggestion", "description": "Influence multiple creatures' actions as per the spell suggestion.", "level": 18}
    ],
    "skill_modifiers": {
        "Perform": 2,
        "Knowledge (Arcana)": 2
    },
    "class_skills": [
        "Appraise", "Balance", "Bluff", "Climb", "Concentration", "Craft", "Decipher Script", 
        "Diplomacy", "Disguise", "Escape Artist", "Gather Information", "Hide", "Intimidate", 
        "Jump", "Knowledge (Arcana)", "Knowledge (History)", "Knowledge (Local)", 
        "Knowledge (Nobility)", "Listen", "Move Silently", "Perform", "Profession", "Sense Motive", 
        "Sleight of Hand", "Spellcraft", "Swim", "Tumble", "Use Magic Device"
    ],
    "skill_points_per_level": 6,  # Add Intelligence modifier to this
    "hit_die": "d6",
    "bab_progression": "Medium",  # +3/4 per level
    "saving_throws": {
        "Fortitude": "Poor",  # +0 at level 1
        "Reflex": "Good",  # +2 at level 1
        "Will": "Good"  # +2 at level 1
    },
    "leveling": {
        "milestone": True,  # Leveling is based on milestones
        "hit_points": "Roll d6 or take average (3.5 rounded up) + Constitution modifier",
        "skill_points": "6 + Intelligence modifier per level",
        "feature_unlocks": "Automatically grants class features at the appropriate levels",
        "bab_progression_formula": "(Level * 3) // 4",
        "saving_throw_progression": {
            "Good": "+2 base at level 1, +1 every even level",
            "Poor": "+0 base at level 1, +1 every three levels"
        }
    },
    "spellcasting": {
        "type": "Arcane",
        "spontaneous_spells": True,  # Does not require preparation
        "spell_slots": {
            1: [2, 0],  # Level 1: 2 base slots, 0 bonus slots
            2: [3, 1],
            3: [3, 1],
            4: [3, 2],
        },
        "scaling": "Gains new spell levels as they level up, up to 6th-level spells"
    }
},
    "Cleric": {
        "description": "Clerics are divine spellcasters who serve their deity with faith and power, channeling divine energy to heal, protect, or destroy.",
    "subclasses": [
        {"name": "Warpriest", "description": "Combines divine spellcasting with martial prowess, excelling in combat."},
        {"name": "Healing Adept", "description": "Specializes in powerful healing magic and support abilities."}
    ],
    "weapon_proficiencies": ["Simple weapons"],
    "armor_proficiencies": ["Light armor", "Medium armor", "Shields"],
    "features": [
        {"name": "Turn Undead", "description": "Channel divine energy to turn or destroy undead creatures.", "level": 1},
        {"name": "Spontaneous Casting", "description": "Convert prepared spells into healing or inflicting spells.", "level": 1},
        {"name": "Domain Powers", "description": "Gain special abilities and spells based on two chosen domains.", "level": 1},
        {"name": "Divine Health", "description": "Become immune to all diseases.", "level": 3},
        {"name": "Greater Turning", "description": "Use Turn Undead to destroy undead outright (requires domain).", "level": 7}
    ],
    "skill_modifiers": {
        "Knowledge (Religion)": 2,
        "Heal": 2
    },
    "class_skills": [
        "Concentration", "Craft", "Diplomacy", "Heal", "Knowledge (Arcana)", 
        "Knowledge (History)", "Knowledge (Religion)", "Knowledge (The Planes)", 
        "Profession", "Spellcraft"
    ],
    "skill_points_per_level": 2,  # Add Intelligence modifier to this
    "hit_die": "d8",
    "bab_progression": "Medium",  # +3/4 per level
    "saving_throws": {
        "Fortitude": "Good",  # +2 at level 1
        "Reflex": "Poor",  # +0 at level 1
        "Will": "Good"  # +2 at level 1
    },
    "leveling": {
        "milestone": True,  # Leveling is based on milestones
        "hit_points": "Roll d8 or take average (4.5 rounded up) + Constitution modifier",
        "skill_points": "2 + Intelligence modifier per level",
        "feature_unlocks": "Automatically grants class features at the appropriate levels",
        "bab_progression_formula": "(Level * 3) // 4",
        "saving_throw_progression": {
            "Good": "+2 base at level 1, +1 every even level",
            "Poor": "+0 base at level 1, +1 every three levels"
        }
    },
    "spellcasting": {
        "type": "Divine",
        "prepared_spells": True,  # Must prepare spells in advance
        "spell_slots": {
            1: [3, 1],  # Level 1: 3 base slots, 1 domain spell
            2: [3, 1],
            3: [2, 1],
            4: [1, 1],
        },
        "scaling": "Gains new spell levels as they level up, up to 9th-level spells"
    },
    "domains": [
        {"name": "Healing", "description": "Boost healing spells and gain abilities to heal effectively."},
        {"name": "War", "description": "Gain proficiency with martial weapons and increase combat power."},
        {"name": "Sun", "description": "Enhance Turn Undead and gain light-based abilities."},
        {"name": "Travel", "description": "Gain abilities to improve mobility and resist hindrances."}
    ]
},
    "Druid": {
        "description": "Druids are divine spellcasters who draw power from nature, capable of wielding spells, summoning creatures, and transforming into animals.",
    "subclasses": [
        {"name": "Shapeshifter", "description": "Focuses on wild shape abilities, excelling in melee combat."},
        {"name": "Nature Warden", "description": "Specializes in summoning creatures and controlling natural elements."}
    ],
    "weapon_proficiencies": ["Club", "Dagger", "Dart", "Quarterstaff", "Scimitar", "Sickle", "Shortspear", "Sling", "Spear"],
    "armor_proficiencies": ["Light armor", "Medium armor", "Shields (wooden only)"],
    "features": [
        {"name": "Animal Companion", "description": "Gain a loyal animal ally.", "level": 1},
        {"name": "Nature Sense", "description": "Gain a +2 bonus on Knowledge (Nature) and Survival checks.", "level": 1},
        {"name": "Wild Empathy", "description": "Improve the attitude of animals using Diplomacy.", "level": 1},
        {"name": "Woodland Stride", "description": "Move through natural undergrowth without penalty.", "level": 2},
        {"name": "Trackless Step", "description": "Leave no trail in natural surroundings.", "level": 3},
        {"name": "Resist Nature's Lure", "description": "Gain a +4 bonus on saving throws against fey abilities.", "level": 4},
        {"name": "Wild Shape", "description": "Transform into a Small or Medium animal, gaining physical abilities.", "level": 5, "scaling": {5: "1/day", 6: "2/day", 7: "3/day", 8: "Large animal", 9: "4/day", 11: "Tiny animal", 12: "Plant type"}},
        {"name": "Venom Immunity", "description": "Immune to all poisons.", "level": 9},
        {"name": "A Thousand Faces", "description": "Change appearance at will, as if using the alter self spell.", "level": 13},
        {"name": "Timeless Body", "description": "No longer take penalties from aging.", "level": 15}
    ],
    "skill_modifiers": {
        "Knowledge (Nature)": 2,
        "Survival": 2
    },
    "class_skills": [
        "Concentration", "Craft", "Diplomacy", "Handle Animal", "Heal", 
        "Knowledge (Nature)", "Knowledge (Geography)", "Listen", "Profession", 
        "Ride", "Spellcraft", "Spot", "Survival", "Swim"
    ],
    "skill_points_per_level": 4,  # Add Intelligence modifier to this
    "hit_die": "d8",
    "bab_progression": "Medium",  # +3/4 per level
    "saving_throws": {
        "Fortitude": "Good",  # +2 at level 1
        "Reflex": "Poor",  # +0 at level 1
        "Will": "Good"  # +2 at level 1
    },
    "leveling": {
        "milestone": True,  # Leveling is based on milestones
        "hit_points": "Roll d8 or take average (4.5 rounded up) + Constitution modifier",
        "skill_points": "4 + Intelligence modifier per level",
        "feature_unlocks": "Automatically grants class features at the appropriate levels",
        "bab_progression_formula": "(Level * 3) // 4",
        "saving_throw_progression": {
            "Good": "+2 base at level 1, +1 every even level",
            "Poor": "+0 base at level 1, +1 every three levels"
        }
    },
    "spellcasting": {
        "type": "Divine",
        "prepared_spells": True,  # Must prepare spells in advance
        "spell_slots": {
            1: [3, 1],  # Level 1: 3 base slots, 1 domain spell
            2: [3, 1],
            3: [2, 1],
            4: [1, 1],
        },
        "scaling": "Gains new spell levels as they level up, up to 9th-level spells"
    }
},
    "Fighter": {
        "description": "Fighters are masters of martial combat, capable of wielding a wide array of weapons and armor with unmatched skill.",
    "subclasses": [
        {"name": "Weapon Master", "description": "Specializes in a single weapon type, gaining increased attack and damage bonuses."},
        {"name": "Defender", "description": "Focuses on defensive techniques, excelling in armor and shield use to protect allies and themselves."}
    ],
    "weapon_proficiencies": ["Simple weapons", "Martial weapons"],
    "armor_proficiencies": ["All armor (light, medium, and heavy)", "Shields (including tower shields)"],
    "features": [
        {"name": "Bonus Feats", "description": "Gain bonus combat feats at specific levels.", "level": 1, "scaling": {1: "1st level", 2: "2nd level", "every even level": "additional feats"}},
        {"name": "Bravery", "description": "Gain a bonus on saving throws against fear effects.", "level": 2, "scaling": {2: "+1", 6: "+2", 10: "+3", 14: "+4", 18: "+5"}},
        {"name": "Armor Training", "description": "Reduce armor check penalty and increase maximum Dexterity bonus for armor.", "level": 3, "scaling": {3: "-1 ACP, +1 Dex", 7: "-2 ACP, +2 Dex", 11: "-3 ACP, +3 Dex", 15: "-4 ACP, +4 Dex"}},
        {"name": "Weapon Training", "description": "Gain a bonus to attack and damage rolls with weapons from a specific group.", "level": 5, "scaling": {5: "+1", 9: "+2", 13: "+3", 17: "+4"}},
        {"name": "Armor Mastery", "description": "Gain DR 5/- when wearing armor.", "level": 19},
        {"name": "Weapon Mastery", "description": "Always confirm critical hits with a chosen weapon and increase critical multiplier by 1.", "level": 20}
    ],
    "skill_modifiers": {},
    "class_skills": [
        "Climb", "Craft", "Handle Animal", "Intimidate", "Jump", "Ride", "Swim"
    ],
    "skill_points_per_level": 2,  # Add Intelligence modifier to this
    "hit_die": "d10",
    "bab_progression": "Full",  # +1 per level
    "saving_throws": {
        "Fortitude": "Good",  # +2 at level 1
        "Reflex": "Poor",  # +0 at level 1
        "Will": "Poor"  # +0 at level 1
    },
    "leveling": {
        "milestone": True,  # Leveling is based on milestones
        "hit_points": "Roll d10 or take average (5.5 rounded up) + Constitution modifier",
        "skill_points": "2 + Intelligence modifier per level",
        "feature_unlocks": "Automatically grants class features at the appropriate levels",
        "bab_progression_formula": "Level * 1",
        "saving_throw_progression": {
            "Good": "+2 base at level 1, +1 every even level",
            "Poor": "+0 base at level 1, +1 every three levels"
        }
    }    
},
    "Monk": {
        "description": "Monks are masters of martial arts, skilled in unarmed combat and spiritual discipline.",
    "subclasses": [
        {"name": "Way of the Open Hand", "description": "Focuses on precise strikes and controlling the flow of combat."},
        {"name": "Way of the Shadow", "description": "Specializes in stealth and deception, blending martial arts with subterfuge."}
    ],
    "weapon_proficiencies": ["Club", "Crossbow (light)", "Dagger", "Handaxe", "Javelin", "Kama", "Nunchaku", "Quarterstaff", "Sai", "Shuriken", "Sling", "Siangham"],
    "armor_proficiencies": ["None"],  # Monks do not use armor
    "features": [
        {"name": "Unarmed Strike", "description": "Increased unarmed attack damage.", "level": 1, "scaling": {1: "1d6", 4: "1d8", 8: "1d10", 12: "2d6", 16: "2d8", 20: "2d10"}},
        {"name": "Flurry of Blows", "description": "Make multiple unarmed strikes at the cost of accuracy.", "level": 1},
        {"name": "Evasion", "description": "Avoid damage from area effects with a successful Reflex save.", "level": 2},
        {"name": "Still Mind", "description": "Gain a bonus on saving throws against enchantments.", "level": 3},
        {"name": "Ki Strike", "description": "Unarmed attacks count as magical for overcoming resistance.", "level": 4, "scaling": {4: "magic", 10: "lawful", 16: "adamantine"}},
        {"name": "Slow Fall", "description": "Reduce falling damage by level-based increments when near a wall.", "level": 4, "scaling": {4: "20 ft", 8: "40 ft", 12: "60 ft", 16: "80 ft", 20: "Any distance"}},
        {"name": "Purity of Body", "description": "Immune to all diseases, both magical and mundane.", "level": 5},
        {"name": "Wholeness of Body", "description": "Heal a number of hit points equal to twice your Monk level per day.", "level": 7},
        {"name": "Improved Evasion", "description": "Take no damage on a successful Reflex save and half damage on a failure.", "level": 9},
        {"name": "Diamond Body", "description": "Immune to poisons.", "level": 11},
        {"name": "Abundant Step", "description": "Use Dimension Door as a spell-like ability once per day.", "level": 12},
        {"name": "Diamond Soul", "description": "Gain spell resistance equal to 10 + Monk level.", "level": 13},
        {"name": "Quivering Palm", "description": "Create a vibration in the body of a target that can be released to slay them.", "level": 15},
        {"name": "Timeless Body", "description": "No longer take penalties from aging.", "level": 17},
        {"name": "Tongue of the Sun and Moon", "description": "Speak and understand any language.", "level": 17},
        {"name": "Empty Body", "description": "Become ethereal for 1 round per Monk level.", "level": 19},
        {"name": "Perfect Self", "description": "Become a magical creature, gaining damage reduction 10/chaotic.", "level": 20}
    ],
    "skill_modifiers": {},
    "class_skills": [
        "Balance", "Climb", "Concentration", "Craft", "Diplomacy", "Escape Artist", 
        "Hide", "Jump", "Knowledge (Arcana)", "Knowledge (Religion)", 
        "Listen", "Move Silently", "Perform", "Profession", "Sense Motive", 
        "Spot", "Swim", "Tumble"
    ],
    "skill_points_per_level": 4,  # Add Intelligence modifier to this
    "hit_die": "d8",
    "bab_progression": "Medium",  # +3/4 per level
    "saving_throws": {
        "Fortitude": "Good",  # +2 at level 1
        "Reflex": "Good",  # +2 at level 1
        "Will": "Good"  # +2 at level 1
    },
    "leveling": {
        "milestone": True,  # Leveling is based on milestones, not XP
        "hit_points": "Roll d8 or take average (4.5 rounded up) + Constitution modifier",
        "skill_points": "4 + Intelligence modifier per level",
        "feature_unlocks": "Automatically grants class features at the appropriate levels",
        "bab_progression_formula": "(Level * 3) // 4",
        "saving_throw_progression": {
            "Good": "+2 base at level 1, +1 every even level",
            "Poor": "+0 base at level 1, +1 every three levels"
        }
    }
},
"Paladin": {
    "description": "Paladins are holy warriors devoted to righteousness, justice, and the will of their deity, wielding divine power to heal and smite evil.",
    "subclasses": [
        {"name": "Avenger", "description": "Focuses on combat prowess and smiting evil foes."},
        {"name": "Healer", "description": "Specializes in healing and supporting allies with divine powers."}
    ],
    "weapon_proficiencies": ["Simple weapons", "Martial weapons"],
    "armor_proficiencies": ["All armor (light, medium, and heavy)", "Shields (except tower shields)"],
    "features": [
        {"name": "Aura of Good", "description": "Radiates an aura of good, detectable by spells like detect good.", "level": 1},
        {"name": "Detect Evil", "description": "Detect the presence of evil as per the detect evil spell, at will.", "level": 1},
        {"name": "Smite Evil", "description": "Add Charisma bonus to attack and level to damage against an evil target.", "level": 1, "scaling": {1: "1/day", 5: "2/day", 10: "3/day", 15: "4/day", 20: "5/day"}},
        {"name": "Divine Grace", "description": "Add Charisma modifier as a bonus to all saving throws.", "level": 2},
        {"name": "Lay on Hands", "description": "Heal a number of hit points per day equal to Paladin level × Charisma modifier.", "level": 2},
        {"name": "Aura of Courage", "description": "Become immune to fear; allies within 10 ft gain +4 to saves against fear.", "level": 3},
        {"name": "Divine Health", "description": "Become immune to all diseases, both mundane and magical.", "level": 3},
        {"name": "Turn Undead", "description": "Channel divine energy to turn or destroy undead as a Cleric of half Paladin level.", "level": 4},
        {"name": "Special Mount", "description": "Call a divine mount, which grows stronger as the Paladin gains levels.", "level": 5},
        {"name": "Remove Disease", "description": "Cure disease once per week, scaling with level.", "level": 6, "scaling": {6: "1/week", 9: "2/week", 12: "3/week", 15: "4/week", 18: "5/week"}}
    ],
    "skill_modifiers": {
        "Diplomacy": 2,
        "Sense Motive": 2
    },
    "class_skills": [
        "Concentration", "Craft", "Diplomacy", "Handle Animal", "Heal", 
        "Knowledge (Nobility)", "Knowledge (Religion)", "Profession", "Ride", "Sense Motive"
    ],
    "skill_points_per_level": 2,  # Add Intelligence modifier to this
    "hit_die": "d10",
    "bab_progression": "Full",  # +1 per level
    "saving_throws": {
        "Fortitude": "Good",  # +2 at level 1
        "Reflex": "Poor",  # +0 at level 1
        "Will": "Good"  # +2 at level 1
    },
    "leveling": {
        "milestone": True,  # Leveling is based on milestones
        "hit_points": "Roll d10 or take average (5.5 rounded up) + Constitution modifier",
        "skill_points": "2 + Intelligence modifier per level",
        "feature_unlocks": "Automatically grants class features at the appropriate levels",
        "bab_progression_formula": "Level * 1",
        "saving_throw_progression": {
            "Good": "+2 base at level 1, +1 every even level",
            "Poor": "+0 base at level 1, +1 every three levels"
        }
    },
    "spellcasting": {
        "type": "Divine",
        "prepared_spells": True,  # Must prepare spells in advance
        "spell_slots": {
            1: [0, 0],  # Level 1: No spell slots
            2: [0, 0],
            3: [0, 0],
            4: [1, 0],  # Level 4: Gains 1 base spell slot
            5: [1, 1],
            6: [1, 1],
            7: [1, 1],
        },
        "scaling": "Gains new spell levels as they level up, up to 4th-level spells"
    }
},
    "Ranger": {
        "description": "Rangers are skilled hunters and trackers, capable of surviving in the wild and excelling in combat, especially against their chosen enemies.",
    "subclasses": [
        {"name": "Archer", "description": "Specializes in ranged combat, excelling with bows and precision attacks."},
        {"name": "Beast Master", "description": "Focuses on enhancing their bond with animal companions and controlling creatures."}
    ],
    "weapon_proficiencies": ["Simple weapons", "Martial weapons"],
    "armor_proficiencies": ["Light armor", "Shields (except tower shields)"],
    "features": [
        {"name": "Favored Enemy", "description": "Gain bonuses against a specific type of creature.", "level": 1, "scaling": {1: "+2", 5: "+4", 10: "+6", 15: "+8", 20: "+10"}},
        {"name": "Track", "description": "Gain the Track feat for free.", "level": 1},
        {"name": "Wild Empathy", "description": "Improve the attitude of animals using Diplomacy.", "level": 1},
        {"name": "Combat Style", "description": "Choose a combat style (Archery or Two-Weapon Fighting) for bonus feats.", "level": 2},
        {"name": "Endurance", "description": "Gain the Endurance feat for free.", "level": 3},
        {"name": "Animal Companion", "description": "Gain an animal companion to assist you in and out of combat.", "level": 4},
        {"name": "Improved Combat Style", "description": "Gain additional feats based on your chosen combat style.", "level": 6},
        {"name": "Woodland Stride", "description": "Move through natural undergrowth without penalty.", "level": 7},
        {"name": "Swift Tracker", "description": "Track enemies at normal speed.", "level": 8},
        {"name": "Evasion", "description": "Avoid damage from area effects with a successful Reflex save.", "level": 9},
        {"name": "Combat Style Mastery", "description": "Gain mastery feats for your chosen combat style.", "level": 11},
        {"name": "Camouflage", "description": "Hide without cover in natural environments.", "level": 13},
        {"name": "Hide in Plain Sight", "description": "Hide even when observed in natural terrain.", "level": 17}
    ],
    "skill_modifiers": {
        "Survival": 2,
        "Knowledge (Nature)": 2
    },
    "class_skills": [
        "Climb", "Concentration", "Craft", "Handle Animal", "Heal", "Hide", 
        "Knowledge (Dungeoneering)", "Knowledge (Geography)", "Knowledge (Nature)", 
        "Listen", "Move Silently", "Profession", "Ride", "Search", "Spot", 
        "Survival", "Swim", "Use Rope"
    ],
    "skill_points_per_level": 6,  # Add Intelligence modifier to this
    "hit_die": "d8",
    "bab_progression": "Full",  # +1 per level
    "saving_throws": {
        "Fortitude": "Good",  # +2 at level 1
        "Reflex": "Good",  # +2 at level 1
        "Will": "Poor"  # +0 at level 1
    },
    "leveling": {
        "milestone": True,  # Leveling is based on milestones
        "hit_points": "Roll d8 or take average (4.5 rounded up) + Constitution modifier",
        "skill_points": "6 + Intelligence modifier per level",
        "feature_unlocks": "Automatically grants class features at the appropriate levels",
        "bab_progression_formula": "Level * 1",
        "saving_throw_progression": {
            "Good": "+2 base at level 1, +1 every even level",
            "Poor": "+0 base at level 1, +1 every three levels"
        }
    },
    "spellcasting": {
        "type": "Divine",
        "prepared_spells": True,  # Must prepare spells in advance
        "spell_slots": {
            1: [0, 1],  # Level 1: 0 base slots, 1 bonus slot
            2: [1, 1],
            3: [1, 1],
            4: [1, 1],
        },
        "scaling": "Gains new spell levels as they level up, up to 4th-level spells"
    }
},
    "Rogue": {
        "description": "Rogues are versatile and cunning adventurers skilled in stealth, traps, and precision strikes.",
    "subclasses": [
        {"name": "Thief", "description": "Focuses on stealth, sleight of hand, and acquiring treasure."},
        {"name": "Assassin", "description": "Excels in precision strikes, poison use, and stealthy eliminations."}
    ],
    "weapon_proficiencies": ["Simple weapons", "Hand crossbows", "Rapiers", "Short swords", "Shortbows"],
    "armor_proficiencies": ["Light armor"],
    "features": [
        {"name": "Sneak Attack", "description": "Deal extra damage to flanked or flat-footed opponents.", "level": 1, "scaling": {1: "+1d6", 3: "+2d6", 5: "+3d6", 7: "+4d6", 9: "+5d6", 11: "+6d6", 13: "+7d6", 15: "+8d6", 17: "+9d6", 19: "+10d6"}},
        {"name": "Trapfinding", "description": "Locate and disable traps with a DC over 20.", "level": 1},
        {"name": "Evasion", "description": "Avoid damage from area effects with a successful Reflex save.", "level": 2},
        {"name": "Trap Sense", "description": "Gain a bonus on Reflex saves and AC against traps.", "level": 3, "scaling": {3: "+1", 6: "+2", 9: "+3", 12: "+4", 15: "+5", 18: "+6"}},
        {"name": "Uncanny Dodge", "description": "Retain Dexterity bonus to AC even when flat-footed.", "level": 4},
        {"name": "Improved Uncanny Dodge", "description": "Cannot be flanked except by a rogue of four or more levels higher.", "level": 8},
        {"name": "Special Abilities", "description": "Gain a special ability such as Crippling Strike or Defensive Roll.", "level": 10, "scaling": {"every 3 levels": "Gain one additional special ability"}}
    ],
    "skill_modifiers": {
        "Disable Device": 2,
        "Stealth": 2
    },
    "class_skills": [
        "Appraise", "Balance", "Bluff", "Climb", "Craft", "Decipher Script", 
        "Diplomacy", "Disable Device", "Escape Artist", "Forgery", 
        "Gather Information", "Hide", "Intimidate", "Jump", 
        "Knowledge (Local)", "Listen", "Move Silently", "Open Lock", 
        "Perform", "Profession", "Search", "Sense Motive", 
        "Sleight of Hand", "Spot", "Swim", "Tumble", "Use Magic Device", "Use Rope"
    ],
    "skill_points_per_level": 8,  # Add Intelligence modifier to this
    "hit_die": "d6",
    "bab_progression": "Medium",  # +3/4 per level
    "saving_throws": {
        "Fortitude": "Poor",  # +0 at level 1
        "Reflex": "Good",  # +2 at level 1
        "Will": "Poor"  # +0 at level 1
    },
    "leveling": {
        "milestone": True,  # Leveling is based on milestones
        "hit_points": "Roll d6 or take average (3.5 rounded up) + Constitution modifier",
        "skill_points": "8 + Intelligence modifier per level",
        "feature_unlocks": "Automatically grants class features at the appropriate levels",
        "bab_progression_formula": "(Level * 3) // 4",
        "saving_throw_progression": {
            "Good": "+2 base at level 1, +1 every even level",
            "Poor": "+0 base at level 1, +1 every three levels"
        }
    }
},
    "Sorcerer": {
        "description": "Sorcerers are innate arcane spellcasters who harness magic through natural talent rather than study, excelling in flexibility and raw magical power.",
    "subclasses": [
        {"name": "Draconic Bloodline", "description": "Gains abilities and traits from a draconic ancestor."},
        {"name": "Wild Mage", "description": "Focuses on unpredictable and chaotic magic, with effects that vary wildly."}
    ],
    "weapon_proficiencies": ["Simple weapons"],
    "armor_proficiencies": ["None"],  # Sorcerers do not use armor
    "features": [
        {"name": "Summon Familiar", "description": "Gain a magical companion that provides bonuses and abilities.", "level": 1},
        {"name": "Arcane Spells", "description": "Cast arcane spells spontaneously, without needing preparation.", "level": 1},
        {"name": "Bonus Feats", "description": "Gain a bonus metamagic or item creation feat at specific levels.", "level": 5, "scaling": {"every 5 levels": "1 bonus feat"}}
    ],
    "skill_modifiers": {
        "Spellcraft": 2,
        "Knowledge (Arcana)": 2
    },
    "class_skills": [
        "Bluff", "Concentration", "Craft", "Knowledge (Arcana)", "Profession", "Spellcraft"
    ],
    "skill_points_per_level": 2,  # Add Intelligence modifier to this
    "hit_die": "d4",
    "bab_progression": "Poor",  # +1/2 per level
    "saving_throws": {
        "Fortitude": "Poor",  # +0 at level 1
        "Reflex": "Poor",  # +0 at level 1
        "Will": "Good"  # +2 at level 1
    },
    "leveling": {
        "milestone": True,  # Leveling is based on milestones
        "hit_points": "Roll d4 or take average (2.5 rounded up) + Constitution modifier",
        "skill_points": "2 + Intelligence modifier per level",
        "feature_unlocks": "Automatically grants class features at the appropriate levels",
        "bab_progression_formula": "(Level * 1) // 2",
        "saving_throw_progression": {
            "Good": "+2 base at level 1, +1 every even level",
            "Poor": "+0 base at level 1, +1 every three levels"
        }
    },
    "spellcasting": {
        "type": "Arcane",
        "spontaneous_spells": True,  # Does not require preparation
        "spell_slots": {
            1: [5, 3],  # Level 1: 5 base slots, 3 bonus spells known
            2: [6, 4],
            3: [6, 5],
            4: [6, 6],
        },
        "scaling": "Gains new spell levels as they level up, up to 9th-level spells",
        "spells_known": {
            1: 4,  # Level 1: 4 spells known
            2: 5,
            3: 6,
            4: 7,
            "each level": "+1 spell known"
        }
    }
},
    "Wizard": {
        "description": "Wizards are scholarly arcane spellcasters who wield vast magical power through study and preparation.",
    "subclasses": [
        {"name": "Evoker", "description": "Specializes in destructive and combat-focused spells."},
        {"name": "Illusionist", "description": "Excels in creating illusions and manipulating perceptions."}
    ],
    "weapon_proficiencies": ["Club", "Dagger", "Heavy Crossbow", "Light Crossbow", "Quarterstaff"],
    "armor_proficiencies": ["None"],  # Wizards do not use armor
    "features": [
        {"name": "Arcane Spells", "description": "Cast arcane spells with preparation and a spellbook.", "level": 1},
        {"name": "Familiar", "description": "Gain a magical companion that grants bonuses and abilities.", "level": 1},
        {"name": "Scribe Scroll", "description": "Gain the Scribe Scroll feat for free at level 1.", "level": 1},
        {"name": "Bonus Feats", "description": "Gain a bonus metamagic or item creation feat at every 5th level.", "level": 5, "scaling": {"every 5 levels": "1 bonus feat"}}
    ],
    "skill_modifiers": {
        "Spellcraft": 2,
        "Knowledge (Arcana)": 2
    },
    "class_skills": [
        "Concentration", "Craft", "Decipher Script", "Knowledge (All)", 
        "Profession", "Spellcraft"
    ],
    "skill_points_per_level": 2,  # Add Intelligence modifier to this
    "hit_die": "d4",
    "bab_progression": "Poor",  # +1/2 per level
    "saving_throws": {
        "Fortitude": "Poor",  # +0 at level 1
        "Reflex": "Poor",  # +0 at level 1
        "Will": "Good"  # +2 at level 1
    },
    "leveling": {
        "milestone": True,  # Leveling is based on milestones
        "hit_points": "Roll d4 or take average (2.5 rounded up) + Constitution modifier",
        "skill_points": "2 + Intelligence modifier per level",
        "feature_unlocks": "Automatically grants class features at the appropriate levels",
        "bab_progression_formula": "(Level * 1) // 2",
        "saving_throw_progression": {
            "Good": "+2 base at level 1, +1 every even level",
            "Poor": "+0 base at level 1, +1 every three levels"
        }
    },
    "spellcasting": {
        "type": "Arcane",
        "prepared_spells": True,  # Requires preparation
        "spell_slots": {
            1: [3, 1],  # Level 1: 3 base slots, 1 bonus slot for Intelligence
            2: [4, 2],
            3: [4, 2],
            4: [4, 3],
        },
        "scaling": "Gains new spell levels as they level up, up to 9th-level spells",
        "spellbook": "Contains all known spells. New spells can be learned and added."
    }
},
    "Artificer": {
        "description": "Artificers are magical engineers who craft and manipulate magical items, blending technology and magic through their ingenuity.",
    "subclasses": [
        {"name": "Runesmith", "description": "Specializes in crafting powerful magical runes and glyphs."},
        {"name": "Battle Smith", "description": "Focuses on enhancing weapons and armor for combat."}
    ],
    "weapon_proficiencies": ["Simple weapons"],
    "armor_proficiencies": ["Light armor", "Medium armor", "Shields (except tower shields)"],
    "features": [
        {"name": "Artificer Knowledge", "description": "Make checks to identify magical items.", "level": 1},
        {"name": "Craft Reserve", "description": "Gain a pool of points to reduce the XP cost of crafting items.", "level": 1, "scaling": {1: 20, 2: 40, 3: 60, 4: 80, 5: 100, "each level": "+20"}},
        {"name": "Item Creation", "description": "Gain a bonus to crafting magical items.", "level": 1},
        {"name": "Infusions", "description": "Temporarily imbue items with magical effects.", "level": 1},
        {"name": "Disable Trap", "description": "Use Disable Device to disable magical traps.", "level": 1},
        {"name": "Bonus Feats", "description": "Gain item creation or metamagic feats at specific levels.", "level": 4, "scaling": {"every 4 levels": "1 bonus feat"}},
        {"name": "Retain Essence", "description": "Recover XP when disassembling magical items.", "level": 5},
        {"name": "Craft Homunculus", "description": "Create a magical construct to assist you.", "level": 4},
        {"name": "Metamagic Infusion", "description": "Apply metamagic effects to infused items without increasing casting time.", "level": 11}
    ],
    "skill_modifiers": {
        "Use Magic Device": 2,
        "Craft": 2
    },
    "class_skills": [
        "Appraise", "Concentration", "Craft (All)", "Disable Device", "Knowledge (Arcana)", 
        "Knowledge (Architecture and Engineering)", "Knowledge (Dungeoneering)", 
        "Profession", "Search", "Spellcraft", "Use Magic Device"
    ],
    "skill_points_per_level": 4,  # Add Intelligence modifier to this
    "hit_die": "d6",
    "bab_progression": "Medium",  # +3/4 per level
    "saving_throws": {
        "Fortitude": "Poor",  # +0 at level 1
        "Reflex": "Poor",  # +0 at level 1
        "Will": "Good"  # +2 at level 1
    },
    "leveling": {
        "milestone": True,  # Leveling is based on milestones
        "hit_points": "Roll d6 or take average (3.5 rounded up) + Constitution modifier",
        "skill_points": "4 + Intelligence modifier per level",
        "feature_unlocks": "Automatically grants class features at the appropriate levels",
        "bab_progression_formula": "(Level * 3) // 4",
        "saving_throw_progression": {
            "Good": "+2 base at level 1, +1 every even level",
            "Poor": "+0 base at level 1, +1 every three levels"
        }
    },
    "spellcasting": {
        "type": "Infusion",
        "prepared_spells": True,  # Must prepare infusions in advance
        "spell_slots": {
            1: [2, 0],  # Level 1: 2 base slots, 0 bonus slots
            2: [3, 1],
            3: [4, 1],
            4: [4, 2],
        },
        "scaling": "Infusions improve in power as the Artificer levels up"
    }
},
    "Psion": {
        "description": "Psions are masters of mental energy, harnessing the power of their minds to manipulate reality and perform extraordinary feats.",
    "subclasses": [
        {"name": "Telepath", "description": "Specializes in mind-affecting powers and mental domination."},
        {"name": "Kineticist", "description": "Focuses on manipulating physical forces and energy."}
    ],
    "weapon_proficiencies": ["Simple weapons"],
    "armor_proficiencies": ["None"],  # Psions do not use armor
    "features": [
        {"name": "Discipline Focus", "description": "Gain additional powers and bonuses in your chosen discipline.", "level": 1},
        {"name": "Power Points", "description": "Psionic energy used to manifest powers.", "level": 1, "scaling": {1: 2, 2: 6, 3: 11, 4: 17, 5: 25, 6: 35, 7: 46, 8: 58, 9: 72, 10: 88, "each level": "add appropriate progression"}},
        {"name": "Psionic Powers", "description": "Learn and manifest psionic powers based on your level.", "level": 1},
        {"name": "Bonus Feats", "description": "Gain bonus psionic or metapsionic feats.", "level": 1, "scaling": {"every 5 levels": "1 bonus feat"}}
    ],
    "skill_modifiers": {
        "Concentration": 2,
        "Knowledge (Psionics)": 2
    },
    "class_skills": [
        "Autohypnosis", "Concentration", "Craft", "Knowledge (Psionics)", 
        "Profession", "Psicraft", "Use Psionic Device"
    ],
    "skill_points_per_level": 2,  # Add Intelligence modifier to this
    "hit_die": "d4",
    "bab_progression": "Poor",  # +1/2 per level
    "saving_throws": {
        "Fortitude": "Poor",  # +0 at level 1
        "Reflex": "Poor",  # +0 at level 1
        "Will": "Good"  # +2 at level 1
    },
    "leveling": {
        "milestone": True,  # Leveling is based on milestones
        "hit_points": "Roll d4 or take average (2.5 rounded up) + Constitution modifier",
        "skill_points": "2 + Intelligence modifier per level",
        "feature_unlocks": "Automatically grants class features at the appropriate levels",
        "bab_progression_formula": "(Level * 1) // 2",
        "saving_throw_progression": {
            "Good": "+2 base at level 1, +1 every even level",
            "Poor": "+0 base at level 1, +1 every three levels"
        }
    },
    "psionics": {
        "type": "Psionic",
        "power_points": {
            1: 2,  # Level 1: 2 power points
            2: 6,
            3: 11,
            4: 17,
            "scaling": "Increases based on level progression"
        },
        "powers_known": {
            1: 2,  # Level 1: 2 powers known
            2: 3,
            3: 5,
            4: 7,
            "scaling": "Increases based on level progression"
        },
        "manifesting": "Powers are fueled by power points and scale dynamically."
    }
},
    "Psychic Warrior": {
        "description": "Psychic Warriors are martial combatants who blend psionic power with physical prowess, using mental energy to enhance their combat abilities.",
    "subclasses": [
        {"name": "Soulblade", "description": "Focuses on creating and wielding psionic blades."},
        {"name": "Iron Mind", "description": "Specializes in resilience and defensive psionic techniques."}
    ],
    "weapon_proficiencies": ["Simple weapons", "Martial weapons"],
    "armor_proficiencies": ["Light armor", "Medium armor", "Shields (except tower shields)"],
    "features": [
        {"name": "Power Points", "description": "Psionic energy used to manifest powers.", "level": 1, "scaling": {1: 2, 2: 4, 3: 7, 4: 11, 5: 16, 6: 22, 7: 29, 8: 37, 9: 46, 10: 56, "each level": "add appropriate progression"}},
        {"name": "Psionic Powers", "description": "Learn and manifest psionic powers based on your level.", "level": 1},
        {"name": "Bonus Feats", "description": "Gain bonus psionic or combat feats.", "level": 1, "scaling": {"every 3 levels": "1 bonus feat"}},
        {"name": "Warrior’s Path", "description": "Choose a path that grants specialized psionic and combat abilities.", "level": 3},
        {"name": "Expanded Knowledge", "description": "Learn an additional psionic power from any discipline.", "level": 5, "scaling": {"every 5 levels": "1 additional power"}}
    ],
    "skill_modifiers": {
        "Concentration": 2,
        "Autohypnosis": 2
    },
    "class_skills": [
        "Autohypnosis", "Climb", "Concentration", "Craft", "Jump", 
        "Knowledge (Psionics)", "Listen", "Profession", "Ride", 
        "Spot", "Swim", "Tumble"
    ],
    "skill_points_per_level": 2,  # Add Intelligence modifier to this
    "hit_die": "d8",
    "bab_progression": "Medium",  # +3/4 per level
    "saving_throws": {
        "Fortitude": "Good",  # +2 at level 1
        "Reflex": "Poor",  # +0 at level 1
        "Will": "Good"  # +2 at level 1
    },
    "leveling": {
        "milestone": True,  # Leveling is based on milestones
        "hit_points": "Roll d8 or take average (4.5 rounded up) + Constitution modifier",
        "skill_points": "2 + Intelligence modifier per level",
        "feature_unlocks": "Automatically grants class features at the appropriate levels",
        "bab_progression_formula": "(Level * 3) // 4",
        "saving_throw_progression": {
            "Good": "+2 base at level 1, +1 every even level",
            "Poor": "+0 base at level 1, +1 every three levels"
        }
    },
    "psionics": {
        "type": "Psionic",
        "power_points": {
            1: 2,  # Level 1: 2 power points
            2: 4,
            3: 7,
            4: 11,
            "scaling": "Increases based on level progression"
        },
        "powers_known": {
            1: 1,  # Level 1: 1 power known
            2: 2,
            3: 3,
            4: 4,
            "scaling": "Increases based on level progression"
        },
        "manifesting": "Powers are fueled by power points and scale dynamically."
    }
},
    "Soulknife": {
        "description": "Soulknives are psionic warriors who channel their mental energy into powerful, customizable weapons known as mind blades.",
    "subclasses": [
        {"name": "Mind Slayer", "description": "Specializes in enhancing and using the mind blade for devastating attacks."},
        {"name": "Blade Shaper", "description": "Focuses on altering the mind blade’s form and imbuing it with unique effects."}
    ],
    "weapon_proficiencies": ["Simple weapons"],
    "armor_proficiencies": ["Light armor", "Medium armor", "Shields (except tower shields)"],
    "features": [
        {"name": "Mind Blade", "description": "Manifest a weapon made of psionic energy.", "level": 1},
        {"name": "Throw Mind Blade", "description": "Hurl your mind blade as a ranged weapon.", "level": 2},
        {"name": "Mind Blade Enhancement", "description": "Imbue the mind blade with magical properties.", "level": 3, "scaling": {3: "+1 enhancement", 6: "+2 enhancement", 9: "+3 enhancement", 12: "+4 enhancement", 15: "+5 enhancement"}},
        {"name": "Free Draw", "description": "Manifest your mind blade as a free action.", "level": 5},
        {"name": "Shape Mind Blade", "description": "Alter the mind blade’s form (e.g., dual weapons, reach weapons).", "level": 7},
        {"name": "Bladewind", "description": "Strike all enemies within reach with a single attack.", "level": 9},
        {"name": "Multiple Throw", "description": "Throw multiple mind blades in a single round.", "level": 13},
        {"name": "Improved Mind Blade", "description": "Further enhance your mind blade’s magical properties.", "level": 17}
    ],
    "skill_modifiers": {
        "Concentration": 2,
        "Autohypnosis": 2
    },
    "class_skills": [
        "Autohypnosis", "Balance", "Climb", "Concentration", "Craft", 
        "Hide", "Jump", "Listen", "Move Silently", "Profession", 
        "Spot", "Tumble"
    ],
    "skill_points_per_level": 4,  # Add Intelligence modifier to this
    "hit_die": "d10",
    "bab_progression": "Full",  # +1 per level
    "saving_throws": {
        "Fortitude": "Good",  # +2 at level 1
        "Reflex": "Good",  # +2 at level 1
        "Will": "Poor"  # +0 at level 1
    },
    "leveling": {
        "milestone": True,  # Leveling is based on milestones
        "hit_points": "Roll d10 or take average (5.5 rounded up) + Constitution modifier",
        "skill_points": "4 + Intelligence modifier per level",
        "feature_unlocks": "Automatically grants class features at the appropriate levels",
        "bab_progression_formula": "Level * 1",
        "saving_throw_progression": {
            "Good": "+2 base at level 1, +1 every even level",
            "Poor": "+0 base at level 1, +1 every three levels"
        }
    },
    "psionics": {
        "type": "Psionic",
        "manifesting": "Mind Blade abilities are fueled by psionic energy but do not use traditional power points."
    }
}
    }
