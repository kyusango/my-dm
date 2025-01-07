
class_data = {
    "Barbarian": {
        "description": "Barbarians are primal warriors who channel their rage and physical prowess to dominate the battlefield.",
        "subclasses": [
            {"name": "Berserker", "description": "Focused on rage and brutal attacks, known for their frenzy and overwhelming damage."},
            {"name": "Totem Warrior", "description": "Focuses on spiritual connection with animal totems, gaining enhanced abilities."}
        ],
        "weapon_proficiencies": ["Simple weapons", "Martial weapons"],
        "armor_proficiencies": ["Light armor", "Medium armor", "Shields"],
        "features": ["Rage", "Unarmored Defense"]
    },
    "Bard": {
        "description": "Bards are charismatic performers and versatile spellcasters, blending music, lore, and magic to inspire allies and manipulate foes.",
        "subclasses": [
            {"name": "College of Lore", "description": "A jack-of-all-trades bard, excelling in knowledge, magic, and support."},
            {"name": "College of Valor", "description": "A warrior bard who inspires bravery and combats foes through both combat and magic."}
        ],
        "weapon_proficiencies": ["Simple weapons", "Hand crossbows", "Longswords", "Rapiers", "Shortswords"],
        "armor_proficiencies": ["Light armor"],
        "features": ["Spellcasting", "Bardic Inspiration"]
    },
    "Cleric": {
        "description": "Clerics are devout champions of their deities, wielding divine power to heal, protect, and smite their enemies.",
        "subclasses": [
            {"name": "Life Domain", "description": "Focuses on healing, vitality, and bringing life to the world."},
            {"name": "Light Domain", "description": "Focuses on radiant energy and the forces of good to banish darkness and evil."},
            {"name": "Trickery Domain", "description": "Focuses on deception, stealth, and illusion to deceive enemies and aid allies."}
        ],
        "weapon_proficiencies": ["Simple weapons"],
        "armor_proficiencies": ["Light armor", "Medium armor", "Shields"],
        "features": ["Spellcasting", "Divine Domain"]
    },
    "Druid": {
        "description": "Druids are keepers of the natural order, channeling the primal forces of nature to protect the wilderness and those who depend on it.",
        "subclasses": [
            {"name": "Circle of the Land", "description": "Draws power from natural environments, gaining abilities related to the terrain they call home."},
            {"name": "Circle of the Moon", "description": "A shapeshifting druid that transforms into more powerful beasts in combat."}
        ],
        "weapon_proficiencies": ["Clubs", "Daggers", "Darts", "Javelins", "Maces", "Quarterstaffs", "Scimitars", "Sickles", "Slings", "Spears"],
        "armor_proficiencies": ["Light armor", "Medium armor", "Shields"],
        "features": ["Spellcasting", "Wild Shape"]
    },
    "Fighter": {
        "description": "Fighters are skilled warriors trained in combat and weaponry.",
        "subclasses": [
            {"name": "Champion", "description": "A master of combat and physical prowess, excelling at improving critical strikes and fighting techniques."},
            {"name": "Battle Master", "description": "A tactician who specializes in battlefield control, using combat maneuvers to gain the advantage."}
        ],
        "weapon_proficiencies": ["All simple weapons", "All martial weapons"],
        "armor_proficiencies": ["All armor", "Shields"],
        "features": ["Second Wind", "Action Surge"]
    },
    "Monk": {
        "description": "Monks are martial artists who channel their inner strength.",
        "subclasses": [
            {"name": "Way of the Open Hand", "description": "A monk focused on unarmed strikes and martial discipline, capable of manipulating the bodies of their foes."},
            {"name": "Way of the Shadow", "description": "A monk specializing in stealth, deception, and shadow magic, blending martial arts with supernatural powers to move unseen and strike swiftly."}
        ],
        "weapon_proficiencies": ["Club", "Crossbow (light)", "Dagger", "Handaxe", "Javelin", "Kama", "Nunchaku", "Quarterstaff", "Sai", "Shuriken", "Siangham", "Sling"],
        "armor_proficiencies": ["None"],
        "features": ["Unarmored Defense", "Martial Arts"]
    },
    "Paladin": {
        "description": "Paladins are holy warriors devoted to righteousness and justice.",
        "subclasses": [
            {"name": "Oath of Devotion", "description": "A paladin who devotes themselves to honor, righteousness, and the protection of others."},
            {"name": "Oath of Vengeance", "description": "A paladin consumed by the need to avenge wrongs and punish evildoers."}
        ],
        "weapon_proficiencies": ["All simple weapons", "All martial weapons"],
        "armor_proficiencies": ["All armor", "Shields"],
        "features": ["Divine Sense", "Lay on Hands"]
    },
    "Ranger": {
        "description": "Rangers are skilled hunters and trackers who excel in ranged combat.",
        "subclasses": [
            {"name": "Hunter", "description": "A master of tracking and hunting, skilled at dealing damage to specific enemies."},
            {"name": "Beast Master", "description": "A ranger who forms a bond with an animal companion, relying on teamwork and loyalty."}
        ],
        "weapon_proficiencies": ["All simple weapons", "All martial weapons"],
        "armor_proficiencies": ["Light armor", "Medium armor", "Shields"],
        "features": ["Favored Enemy", "Natural Explorer"]
    },
    "Rogue": {
        "description": "Rogues are cunning and agile, excelling in stealth and precision strikes.",
        "subclasses": [
            {"name": "Thief", "description": "A rogue who specializes in stealing, sneaking, and getting in and out of places undetected."},
            {"name": "Assassin", "description": "A deadly rogue trained in silent killings, specializing in sneak attacks and poisons."}
        ],
        "weapon_proficiencies": ["All simple weapons", "Hand crossbow", "Rapier", "Shortbow", "Short sword"],
        "armor_proficiencies": ["Light armor"],
        "features": ["Sneak Attack", "Thieves' Cant"]
    },
    "Sorcerer": {
        "description": "Sorcerers are arcane spellcasters who rely on innate magic ability.",
        "subclasses": [
            {"name": "Draconic Bloodline", "description": "A sorcerer with the blood of dragons, gaining powers tied to elemental forces and resilience."},
            {"name": "Shadow Bloodline", "description": "A sorcerer with the blood of shadow creatures, capable of manipulating darkness and controlling shadows."}
        ],
        "weapon_proficiencies": ["Club", "Dagger", "Quarterstaff", "Crossbow (light or heavy)"],
        "armor_proficiencies": ["None"],
        "features": ["Spellcasting", "Sorcerous Origin"]
    },
    "Wizard": {
        "description": "Wizards are spellcasters who rely on intelligence and arcane knowledge.",
        "subclasses": [
            {"name": "School of Abjuration", "description": "A wizard who specializes in protective magic, creating shields and defenses."},
            {"name": "School of Evocation", "description": "A wizard who focuses on creating powerful blasts of magic to damage foes."},
            {"name": "School of Illusion", "description": "A wizard who focuses on tricking the senses and creating illusions to deceive enemies."}
        ],
        "weapon_proficiencies": ["Club", "Dagger", "Quarterstaff", "Crossbow (light or heavy)"],
        "armor_proficiencies": ["None"],
        "features": ["Spellcasting", "Arcane Recovery"]
    },
    "Artificer": {
        "description": "Artificers are masters of infusing magic into objects and crafting magical items.",
        "subclasses": [
            {"name": "Alchemist", "description": "Focuses on creating potions, bombs, and other magical items to support the party."},
            {"name": "Artillerist", "description": "An artificer who specializes in creating ranged weapons and mechanical constructs to deal damage."},
            {"name": "Battle Smith", "description": "A warrior-like artificer who builds a mechanical companion and uses magic to enhance their own combat abilities."}
        ],
        "weapon_proficiencies": ["All simple weapons", "Hand crossbow", "Light crossbow", "Heavy crossbow"],
        "armor_proficiencies": ["Light armor", "Medium armor"],
        "features": ["Spellcasting", "Infuse Magic"]
    },
    "Psion": {
        "description": "Psions are mentalists who channel psionic energy to shape reality.",
        "subclasses": [
            {"name": "Telepath", "description": "Focuses on manipulating minds, reading thoughts, and dominating foes."},
            {"name": "Kineticist", "description": "Specializes in using mental energy to move and shape objects, create force blasts, and control elements."},
            {"name": "Nomad", "description": "A psion who manipulates space and time, capable of teleporting and controlling the battlefield."}
        ],
        "weapon_proficiencies": ["Club", "Dagger", "Quarterstaff", "Crossbow (light or heavy)"],
        "armor_proficiencies": ["None"],
        "features": ["Psionic Powers", "Telepathic Bond"]
    },
    "Psychic Warrior": {
        "description": "Psychic Warriors combine psionics with martial prowess to dominate the battlefield.",
        "subclasses": [
            {"name": "Bodyguard", "description": "Focuses on protecting others using psychic energy to bolster defenses and defend allies."},
            {"name": "Wilder", "description": "A more erratic psychic warrior who gains unrestrained psionic abilities at the cost of unpredictability."}
        ],
        "weapon_proficiencies": ["All simple weapons", "All martial weapons"],
        "armor_proficiencies": ["Light armor", "Medium armor"],
        "features": ["Psionic Combat", "Martial Training"]
    },
    "Soulknife": {
        "description": "Soulknives manifest blades of psionic energy to strike their foes.",
        "subclasses": [
            {"name": "Blade Adept", "description": "Focuses on enhancing their psychic blade and fighting techniques to deal damage and defend."},
            {"name": "Knife Master", "description": "Specializes in using multiple psychic blades and taking down opponents quickly."}
        ],
        "weapon_proficiencies": ["All simple weapons", "Mind blade"],
        "armor_proficiencies": ["Light armor"],
        "features": ["Psychic Blade", "Telekinetic Strike"]
    }
}
