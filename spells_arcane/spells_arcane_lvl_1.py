arcane_spells_level_1 = [
    {
        "name": "Magic Missile",
        "description": "Create magical darts of force that automatically hit and deal 1d4+1 damage each.",
        "components": ["V", "S"],
        "range": "100 ft + 10 ft/level",
        "duration": "Instantaneous",
        "school": "Evocation",
        "scaling": "One additional missile for every two caster levels beyond 1st (maximum 5 missiles)."
    },
    {
        "name": "Shield",
        "description": "Invisible shield grants +4 AC bonus and immunity to Magic Missile.",
        "components": ["V", "S"],
        "range": "Personal",
        "duration": "1 minute/level",
        "school": "Abjuration"
    },
    {
        "name": "Mage Armor",
        "description": "Subject gains a +4 armor bonus to AC.",
        "components": ["V", "S", "M"],
        "range": "Touch",
        "duration": "1 hour/level (D)",
        "school": "Conjuration"
    },
    {
        "name": "Burning Hands",
        "description": "A cone of flame deals 1d4 fire damage per caster level (maximum 5d4).",
        "components": ["V", "S"],
        "range": "15 ft",
        "duration": "Instantaneous",
        "school": "Evocation"
    },
    {
        "name": "Color Spray",
        "description": "A cone of colors blinds, stuns, or knocks unconscious creatures with low hit dice.",
        "components": ["V", "S", "M"],
        "range": "15 ft",
        "duration": "Instantaneous",
        "school": "Illusion"
    },
    {
        "name": "Identify",
        "description": "Determine properties of a single magic item or effect.",
        "components": ["V", "S", "M"],
        "range": "Touch",
        "duration": "Instantaneous",
        "school": "Divination"
    },
    {
        "name": "Charm Person",
        "description": "Makes one humanoid creature regard you as a friendly acquaintance.",
        "components": ["V", "S"],
        "range": "25 ft + 5 ft/2 levels",
        "duration": "1 hour/level",
        "school": "Enchantment"
    },
    {
        "name": "Feather Fall",
        "description": "Target creature or object falls slowly to the ground.",
        "components": ["V"],
        "range": "Close (25 ft + 5 ft/2 levels)",
        "duration": "1 round/level",
        "school": "Transmutation",
        "activation": "Immediate action"
    },
    {
        "name": "Silent Image",
        "description": "Creates a visual illusion of an object, creature, or force, as visualized by you.",
        "components": ["V", "S", "M"],
        "range": "Long (400 ft + 40 ft/level)",
        "duration": "Concentration",
        "school": "Illusion"
    },
    {
        "name": "Grease",
        "description": "Make a surface or object slippery. Creatures in the area may fall or drop held items.",
        "components": ["V", "S", "M"],
        "range": "Close (25 ft + 5 ft/2 levels)",
        "duration": "1 round/level",
        "school": "Conjuration"
    }
]