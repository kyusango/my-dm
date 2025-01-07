magical_items = [
    {
        "name": "Dagger of Venom",
        "description": "A dagger that can be coated with poison once per day, dealing an additional 2d10 poison damage on a hit (DC 15 Constitution save negates).",
        "properties": ["+1 to attack and damage rolls", "Poison effect once per day"],
        "rarity": "Rare",
        "cost": 2500,
        "attunement": True
    },
    {
        "name": "Lightbringer",
        "description": "A mace that glows like a torch and deals an additional 1d6 radiant damage to undead.",
        "properties": ["Glows like a torch", "+1 to attack and damage rolls", "1d6 radiant damage to undead"],
        "rarity": "Uncommon",
        "cost": 1500,
        "attunement": True
    },
    {
        "name": "Glamoured Studded Leather",
        "description": "This armor can change its appearance to resemble any other outfit or armor while maintaining its protective qualities.",
        "properties": ["+1 to AC", "Change appearance as a bonus action"],
        "rarity": "Rare",
        "cost": 3000,
        "attunement": True
    },
    {
        "name": "Cloak of Protection",
        "description": "Grants a +1 bonus to AC and saving throws while worn.",
        "properties": ["+1 AC", "+1 saving throws"],
        "rarity": "Uncommon",
        "cost": 2000,
        "attunement": True
    },
    {
        "name": "Potion of Light Healing",
        "description": "Restores 1d4+1 hit points when consumed.",
        "properties": ["Restores hit points"],
        "rarity": "Common",
        "cost": 25,
        "attunement": False
    },
    {
        "name": "Potion of Healing",
        "description": "Restores 2d4+2 hit points when consumed.",
        "properties": ["Restores hit points"],
        "rarity": "Common",
        "cost": 50,
        "attunement": False
    },
    {
        "name": "Potion of Major Healing",
        "description": "Restores 4d4+4 hit points when consumed.",
        "properties": ["Restores hit points"],
        "rarity": "Uncommon",
        "cost": 150,
        "attunement": False
    },
    {
        "name": "Scroll of 'Spell'",
        "description": "A scroll containing a spell that can be cast once without expending a spell slot.",
        "properties": ["Casts a specific spell"],
        "rarity": "Varies by spell level",
        "cost": "Varies",
        "attunement": False
    },
    {
        "name": "Ring of Jumping",
        "description": "Grants the wearer the effects of the Jump spell without requiring concentration.",
        "properties": ["Triple jump distance"],
        "rarity": "Uncommon",
        "cost": 2000,
        "attunement": True
    },
    {
        "name": "Ring of Warmth",
        "description": "Grants resistance to cold damage and prevents harm from extreme cold.",
        "properties": ["Resistance to cold damage", "Protection from extreme cold"],
        "rarity": "Uncommon",
        "cost": 1500,
        "attunement": True
    },
    {
        "name": "Ring of Swimming",
        "description": "Grants a swimming speed of 40 feet.",
        "properties": ["Swimming speed of 40 feet"],
        "rarity": "Uncommon",
        "cost": 1500,
        "attunement": False
    },
    {
        "name": "Amulet of Health",
        "description": "Sets the wearer's Constitution score to 19, overriding lower scores.",
        "properties": ["Sets Constitution to 19"],
        "rarity": "Rare",
        "cost": 6000,
        "attunement": True
    },
    {
        "name": "Boots of Striding and Springing",
        "description": "Doubles the wearer's walking speed, triples jump distance, and prevents exhaustion from traveling.",
        "properties": ["Double walking speed", "Triple jump distance", "No exhaustion from travel"],
        "rarity": "Uncommon",
        "cost": 3000,
        "attunement": True
    },
    {
        "name": "Hat of Disguise",
        "description": "Allows the wearer to cast Disguise Self at will.",
        "properties": ["Casts Disguise Self at will"],
        "rarity": "Uncommon",
        "cost": 2000,
        "attunement": True
    },
    {
        "name": "Luckstone",
        "description": "Grants a +1 bonus to ability checks and saving throws.",
        "properties": ["+1 ability checks", "+1 saving throws"],
        "rarity": "Uncommon",
        "cost": 3000,
        "attunement": True
    },
    {
        "name": "Wand of 'Spell'",
        "description": "A wand containing a spell that can be cast multiple times, consuming charges.",
        "properties": ["Casts a specific spell", "Regains 1d6+1 charges daily"],
        "rarity": "Varies by spell level",
        "cost": "Varies",
        "attunement": False
    },
    {
        "name": "Sword of Flame",
        "description": "A longsword that deals an additional 1d6 fire damage on a successful hit.",
        "properties": ["+1 to attack and damage rolls", "1d6 fire damage"],
        "rarity": "Uncommon",
        "cost": 3000,
        "attunement": True
    },
    {
        "name": "Immovable Rod",
        "description": "This flat iron rod has a button on one end. Pressing the button causes the rod to become magically fixed in place, defying gravity and remaining stationary until the button is pressed again. It can hold up to 8,000 pounds of weight; exceeding this weight causes the rod to deactivate and fall. A creature can use an action to make a DC 30 Strength check, moving the fixed rod up to 10 feet on a success.",
        "properties": ["Magically fixes in place when activated", "Supports up to 8,000 pounds", "Can be moved with a DC 30 Strength check"],
        "rarity": "Uncommon",
        "cost": 5000,
        "attunement": False
    },
    {
        "name": "Broom of Flying",
        "description": "This wooden broom, weighing 3 pounds, functions as a mundane broom until you stand astride it and speak its command word. It then hovers beneath you, allowing you to ride it through the air. It has a flying speed of 50 feet. The broom can carry up to 400 pounds, but its flying speed decreases to 30 feet while carrying over 200 pounds. The broom ceases hovering when you land. Additionally, you can command the broom to travel to a familiar location within 1 mile, and it will return to you upon command, provided it's still within 1 mile.",
        "properties": ["Flying speed of 50 feet (reduced to 30 feet when carrying over 200 pounds)", "Can carry up to 400 pounds", "Can be commanded to travel to a familiar location within 1 mile and return"],
        "rarity": "Uncommon",
        "cost": 8000,
        "attunement": False
    },
    {
    "name": "Pearl of Power",
    "description": (
        "This pearl allows a spellcaster to recover one expended spell slot. "
        "The recovered spell slot must be of 3rd level or lower. The pearl can only be used once per day."
    ),
    "properties": ["Restores one spell slot of up to 3rd level", "Usable once per day"],
    "rarity": "Uncommon",
    "cost": 6000,
    "attunement": True
    },
    {
    "name": "Alchemy Jug",
    "description": "A magical container capable of producing various liquids, such as water, oil, or wine, once per day.",
    "properties": ["Produces liquids", "Reusable"],
    "rarity": "Uncommon",
    "cost": 2500,
    "attunement": False
    },
    {
    "name": "Amulet of Proof Against Detection and Location",
    "description": "A protective amulet that prevents you from being detected or located by divination magic.",
    "properties": ["Blocks divination magic"],
    "rarity": "Rare",
    "cost": 5000,
    "attunement": True
    },
    {
    "name": "Bag of Holding",
    "description": "A magical bag that holds far more than its exterior size suggests, capable of carrying up to 500 lbs.",
    "properties": ["Extra-dimensional storage"],
    "rarity": "Uncommon",
    "cost": 4000,
    "attunement": False
    },
    {
    "name": "Bead of Force",
    "description": "A small bead that explodes into a forceful sphere, trapping creatures and dealing damage.",
    "properties": ["Force explosion", "Traps creatures"],
    "rarity": "Rare",
    "cost": 3000,
    "attunement": False
    },
    {
    "name": "Boots of Elvenkind",
    "description": "Boots that allow the wearer to move silently and without trace.",
    "properties": ["Advantage on Stealth checks"],
    "rarity": "Uncommon",
    "cost": 2500,
    "attunement": False
    },
    {
    "name": "Boots of the Winterlands",
    "description": "Boots that provide resistance to cold damage and allow travel in icy terrain.",
    "properties": ["Cold resistance", "Ignore difficult terrain"],
    "rarity": "Uncommon",
    "cost": 5000,
    "attunement": False
    },
    {
    "name": "Bottle of Air",
    "description": "A magical bottle that provides fresh air to the user, allowing them to breathe in any environment.",
    "properties": ["Breathable air supply"],
    "rarity": "Uncommon",
    "cost": 3000,
    "attunement": False
    },
    {
    "name": "Bracers of Archery",
    "description": "Bracers that enhance ranged attacks with bows.",
    "properties": ["+2 to attack and damage rolls with bows"],
    "rarity": "Uncommon",
    "cost": 4000,
    "attunement": True
    },
    {
    "name": "Cape of the Mountebank",
    "description": "A cape that allows the wearer to use Dimension Door once per day.",
    "properties": ["Casts Dimension Door"],
    "rarity": "Rare",
    "cost": 8000,
    "attunement": True
    },
    {
    "name": "Cloak of Elvenkind",
    "description": "A cloak that grants advantage on Stealth checks by blending into the environment.",
    "properties": ["Advantage on Stealth checks"],
    "rarity": "Uncommon",
    "cost": 2500,
    "attunement": False
    },
    {
    "name": "Deck of Illusions",
    "description": "A deck of cards that creates illusory creatures when drawn and thrown.",
    "properties": ["Illusions of creatures"],
    "rarity": "Rare",
    "cost": 3000,
    "attunement": False
    },
    {
    "name": "Driftglobe",
    "description": "A magical light orb that floats and follows the user, emitting bright or dim light on command.",
    "properties": ["Light source", "Follows commands"],
    "rarity": "Uncommon",
    "cost": 2000,
    "attunement": False
    },
    {
    "name": "Dust of Disappearance",
    "description": "A magical dust that renders creatures and objects invisible for a short duration.",
    "properties": ["Grants invisibility"],
    "rarity": "Uncommon",
    "cost": 3000,
    "attunement": False
    },
    {
    "name": "Dust of Dryness",
    "description": "A magical dust that absorbs large quantities of water, storing it in a small pellet.",
    "properties": ["Absorbs water", "Creates a pellet"],
    "rarity": "Uncommon",
    "cost": 3000,
    "attunement": False
    },
    {
    "name": "Dust of Sneezing and Choking",
    "description": "A magical dust that causes creatures to sneeze uncontrollably, incapacitating them.",
    "properties": ["Incapacitate creatures", "Area effect"],
    "rarity": "Rare",
    "cost": 4000,
    "attunement": False
},
{
    "name": "Gem of Brightness",
    "description": "A gem that emits bright light or a blinding flash, capable of stunning creatures.",
    "properties": ["Emits bright light", "Stuns creatures"],
    "rarity": "Uncommon",
    "cost": 5000,
    "attunement": False
},
{
    "name": "Gem of Seeing",
    "description": "A gem that allows the user to see through illusions and invisibility for a short duration.",
    "properties": ["See through illusions", "Reveal invisibility"],
    "rarity": "Rare",
    "cost": 12000,
    "attunement": True
},
{
    "name": "Gloves of Missile Snaring",
    "description": "Gloves that allow the wearer to catch or deflect ranged attacks.",
    "properties": ["Catch missiles", "Reduce damage"],
    "rarity": "Uncommon",
    "cost": 4000,
    "attunement": True
},
{
    "name": "Gloves of Swimming and Climbing",
    "description": "Gloves that enhance swimming and climbing abilities.",
    "properties": ["Boost swimming", "Boost climbing"],
    "rarity": "Uncommon",
    "cost": 2500,
    "attunement": False
},
{
    "name": "Goggles of Night",
    "description": "Goggles that grant darkvision up to 60 feet.",
    "properties": ["Grant darkvision"],
    "rarity": "Uncommon",
    "cost": 3000,
    "attunement": False
},
{
    "name": "Heward's Handy Haversack",
    "description": "A magical backpack with extra-dimensional spaces for carrying items.",
    "properties": ["Extra-dimensional storage", "Organized compartments"],
    "rarity": "Rare",
    "cost": 2000,
    "attunement": False
},
{
    "name": "Horseshoes of Speed",
    "description": "Horseshoes that increase the speed of a mounted creature.",
    "properties": ["+30 feet speed"],
    "rarity": "Rare",
    "cost": 3000,
    "attunement": False
},
{
    "name": "Horseshoes of a Zephyr",
    "description": "Horseshoes that allow a mount to hover slightly above the ground.",
    "properties": ["Hover above the ground", "No difficult terrain"],
    "rarity": "Rare",
    "cost": 6000,
    "attunement": False
},
{
    "name": "Instant Fortress",
    "description": "A small cube that transforms into a sturdy fortress on command.",
    "properties": ["Creates a fortress", "Durable structure"],
    "rarity": "Rare",
    "cost": 50000,
    "attunement": False
},
{
    "name": "Ioun Stone (Absorption)",
    "description": "A stone that absorbs spell levels cast at the wearer, preventing the effects.",
    "properties": ["Absorbs up to 50 spell levels"],
    "rarity": "Very Rare",
    "cost": 25000,
    "attunement": True
},
{
    "name": "Ioun Stone (Agility)",
    "description": "A stone that increases the user's Dexterity by +2, up to a maximum of 20.",
    "properties": ["+2 Dexterity (max 20)"],
    "rarity": "Rare",
    "cost": 8000,
    "attunement": True
},
{
    "name": "Ioun Stone (Fortitude)",
    "description": "A stone that increases the user's Constitution by +2, up to a maximum of 20.",
    "properties": ["+2 Constitution (max 20)"],
    "rarity": "Rare",
    "cost": 8000,
    "attunement": True
},
{
    "name": "Ioun Stone (Insight)",
    "description": "A stone that increases the user's Wisdom by +2, up to a maximum of 20.",
    "properties": ["+2 Wisdom (max 20)"],
    "rarity": "Rare",
    "cost": 8000,
    "attunement": True
},
{
    "name": "Ioun Stone (Leadership)",
    "description": "A stone that increases the user's Charisma by +2, up to a maximum of 20.",
    "properties": ["+2 Charisma (max 20)"],
    "rarity": "Rare",
    "cost": 8000,
    "attunement": True
},
{
    "name": "Ioun Stone (Protection)",
    "description": "A stone that grants a +1 bonus to AC.",
    "properties": ["+1 AC"],
    "rarity": "Rare",
    "cost": 7500,
    "attunement": True
},
{
    "name": "Ioun Stone (Regeneration)",
    "description": "A stone that slowly restores hit points over time, healing 1 hit point every 10 minutes.",
    "properties": ["Regenerate 1 HP every 10 minutes"],
    "rarity": "Very Rare",
    "cost": 15000,
    "attunement": True
},
{
    "name": "Iron Bands of Bilarro",
    "description": "A magical restraint that binds a creature on command.",
    "properties": ["Restrains creatures", "Strength check DC 20 to break free"],
    "rarity": "Rare",
    "cost": 5000,
    "attunement": False
},
{
    "name": "Lantern of Revealing",
    "description": "A lantern that reveals invisible creatures and objects within its light.",
    "properties": ["Reveals invisibility", "30-foot radius"],
    "rarity": "Uncommon",
    "cost": 2000,
    "attunement": False
},
{
    "name": "Nolzur's Marvelous Pigments",
    "description": "Magical pigments that create real, functional objects when applied.",
    "properties": ["Creates objects", "Limited by user’s imagination and volume of pigment"],
    "rarity": "Very Rare",
    "cost": 4000,
    "attunement": False
},
{
    "name": "Portable Hole",
    "description": "A cloth that creates a temporary, extra-dimensional storage space.",
    "properties": ["Extra-dimensional storage", "6-foot diameter and 10-foot depth"],
    "rarity": "Rare",
    "cost": 8000,
    "attunement": False
},
{
    "name": "Quiver of Ehlonna",
    "description": "A magical quiver that can hold multiple types of ammunition and weapons.",
    "properties": ["Stores arrows, bolts, and javelins", "Organized storage"],
    "rarity": "Uncommon",
    "cost": 2000,
    "attunement": False
},
{
    "name": "Ring of Feather Falling",
    "description": "A ring that prevents the wearer from taking damage from falling.",
    "properties": ["Prevents fall damage"],
    "rarity": "Rare",
    "cost": 4000,
    "attunement": True
},
{
    "name": "Ring of Free Action",
    "description": "A ring that prevents the wearer from being restrained or slowed by magical effects.",
    "properties": ["Immunity to restrain effects", "Unaffected by difficult terrain"],
    "rarity": "Rare",
    "cost": 5000,
    "attunement": True
},
{
    "name": "Ring of Regeneration",
    "description": "A ring that restores hit points over time and reattaches severed limbs.",
    "properties": ["Restores 1 hit point every 10 minutes", "Reattaches severed limbs"],
    "rarity": "Very Rare",
    "cost": 20000,
    "attunement": True
},
{
    "name": "Ring of Resistance",
    "description": "A ring that grants resistance to a specific type of damage.",
    "properties": ["Resistance to chosen damage type"],
    "rarity": "Rare",
    "cost": 6000,
    "attunement": True
},
{
    "name": "Robe of Eyes",
    "description": "A robe covered in magical eyes that grant enhanced perception and sight.",
    "properties": ["See in all directions", "Advantage on Perception checks", "Detect invisible creatures"],
    "rarity": "Rare",
    "cost": 12000,
    "attunement": True
},
{
    "name": "Robe of Stars",
    "description": "A robe that allows the wearer to cast magic missiles and provides resistance to radiant damage.",
    "properties": ["6 charges of Magic Missile per day", "Resistance to radiant damage"],
    "rarity": "Very Rare",
    "cost": 15000,
    "attunement": True
}
]
