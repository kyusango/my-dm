#-------------------------------------melee combat feats-----------------------------------------
combat_feats_library = [
{
    "name": "Power Attack",
    "type": "Melee Combat",
    "source": "Player's Handbook (D&D 3.5)",
    "description": "You can choose to take a penalty to your attack rolls in exchange for a bonus to your damage rolls.",
    "prerequisites": {"Str": ">= 13"},
    "benefit": "Before making an attack, you can choose to subtract a number from all attack rolls and add the same number to all melee damage rolls. The penalty cannot exceed your base attack bonus.",
    "limitations": "Cannot be applied to ranged weapon attacks.",
    "tags": ["Combat", "Melee"]
    },
{
    "name": "Improved Initiative",
    "type": "Combat",
    "source": "Player's Handbook (D&D 3.5)",
    "description": "You react more quickly than others in combat.",
    "prerequisites": {},
    "benefit": "You gain a +4 bonus on initiative checks.",
    "limitations": "This feat only affects initiative rolls and does not stack with other initiative bonuses from feats.",
    "tags": ["Combat", "Utility"]
    },
{
    "name": "Cleave",
    "type": "Melee Combat",
    "source": "Player's Handbook (D&D 3.5)",
    "description": "You can follow through with a powerful attack to strike another opponent after felling your initial target.",
    "prerequisites": {"Str": ">= 13", "Power Attack": True},
    "benefit": "If you deal enough damage to reduce an opponent to 0 or fewer hit points, you may make an immediate extra melee attack against another creature within reach. The extra attack is with the same weapon and uses the same attack bonus as the attack that dropped the previous creature.",
    "limitations": "You can only cleave once per round.",
    "tags": ["Combat", "Melee"]
    },
{
    "name": "Great Cleave",
    "type": "Melee Combat",
    "source": "Player's Handbook (D&D 3.5)",
    "description": "You can strike multiple opponents in succession after felling each target.",
    "prerequisites": {"Str": ">= 13", "Power Attack": True, "Cleave": True},
    "benefit": "There is no limit to the number of times you can use the Cleave feat per round. As long as you reduce an opponent to 0 or fewer hit points, you may make an immediate extra melee attack against another creature within reach.",
    "limitations": "Each attack must be against a creature within reach and must use the same weapon and attack bonus as the prior attack.",
    "tags": ["Combat", "Melee"]
    },
{
    "name": "Improved Bull Rush",
    "type": "Melee Combat",
    "source": "Player's Handbook (D&D 3.5)",
    "description": "You are skilled at pushing opponents back in melee combat.",
    "prerequisites": {"Str": ">= 13", "Power Attack": True},
    "benefit": "When you perform a bull rush, you do not provoke an attack of opportunity. You also gain a +4 bonus on the Strength check made to push your opponent back.",
    "limitations": "Only applicable to melee combat situations where a bull rush is possible.",
    "tags": ["Combat", "Melee"]
    },
{
    "name": "Improved Sunder",
    "type": "Melee Combat",
    "source": "Player's Handbook (D&D 3.5)",
    "description": "You are skilled at attacking an opponent's weapon or shield in combat.",
    "prerequisites": {"Str": ">= 13", "Power Attack": True},
    "benefit": "When you attempt to sunder an opponent's weapon or shield, you do not provoke an attack of opportunity. You also gain a +4 bonus on the attack roll made to sunder an item.",
    "limitations": "Only applies to melee attacks targeting objects held or worn by opponents.",
    "tags": ["Combat", "Melee"]
    },
{
    "name": "Improved Overrun",
    "type": "Melee Combat",
    "source": "Player's Handbook (D&D 3.5)",
    "description": "You are skilled at knocking opponents down as you move through their space.",
    "prerequisites": {"Str": ">= 13", "Power Attack": True},
    "benefit": "When you attempt to overrun an opponent, the target may not choose to avoid you. You also gain a +4 bonus on the Strength check made to knock the target prone.",
    "limitations": "Only applicable in situations where movement through an opponent's space is allowed.",
    "tags": ["Combat", "Melee"]
    },
{
    "name": "Combat Reflexes",
    "type": "Combat",
    "source": "Player's Handbook (D&D 3.5)",
    "description": "You can make additional attacks of opportunity and react quickly to combat situations.",
    "prerequisites": {},
    "benefit": "You may make a number of additional attacks of opportunity per round equal to your Dexterity modifier. You may also make attacks of opportunity while flat-footed.",
    "limitations": "Only affects attacks of opportunity and requires a high Dexterity modifier to maximize its effect.",
    "tags": ["Combat"]
    },
{
    "name": "Improved Trip",
    "type": "Melee Combat",
    "source": "Player's Handbook (D&D 3.5)",
    "description": "You are skilled at tripping opponents in melee combat.",
    "prerequisites": {"Int": ">= 13", "Combat Expertise": True},
    "benefit": "You do not provoke an attack of opportunity when you attempt to trip an opponent while unarmed. If you successfully trip an opponent, you may immediately make an additional melee attack against that opponent as if you hadn’t used your attack for the trip attempt.",
    "limitations": "Only applies to melee combat and requires Combat Expertise.",
    "tags": ["Combat", "Melee"]
    },
{
    "name": "Improved Disarm",
    "type": "Melee Combat",
    "source": "Player's Handbook (D&D 3.5)",
    "description": "You are skilled at disarming opponents in melee combat.",
    "prerequisites": {"Int": ">= 13", "Combat Expertise": True},
    "benefit": "You do not provoke an attack of opportunity when you attempt to disarm an opponent. You also gain a +4 bonus on your opposed attack roll when attempting to disarm.",
    "limitations": "Only applies to melee combat and requires Combat Expertise.",
    "tags": ["Combat", "Melee"]
    },
{
    "name": "Improved Shield Bash",
    "type": "Melee Combat",
    "source": "Player's Handbook (D&D 3.5)",
    "description": "You can use your shield to attack while retaining its defensive benefits.",
    "prerequisites": {"Shield Proficiency": True},
    "benefit": "When you perform a shield bash, you retain the shield's bonus to your AC.",
    "limitations": "Requires the use of a shield and Shield Proficiency.",
    "tags": ["Combat", "Melee", "Defense"]
    },
{
    "name": "Quick Draw",
    "type": "Combat",
    "source": "Player's Handbook (D&D 3.5)",
    "description": "You can draw weapons faster than normal.",
    "prerequisites": {"Base Attack Bonus": ">= 1"},
    "benefit": "You can draw a weapon as a free action instead of as a move action. You can draw a hidden weapon as a move action.",
    "limitations": "Does not apply to weapons stored in containers such as backpacks.",
    "tags": ["Combat", "Utility"]
    },
{
    "name": "Two-Weapon Fighting",
    "type": "Combat",
    "source": "Player's Handbook (D&D 3.5)",
    "description": "You can fight with a weapon in each hand.",
    "prerequisites": {"Dex": ">= 15"},
    "benefit": "Your penalties on attack rolls for fighting with two weapons are reduced. The penalty for your primary hand is reduced by 2, and the penalty for your off-hand is reduced by 6.",
    "limitations": "Your off-hand weapon must be light unless you have the Ambidexterity feat.",
    "tags": ["Combat", "Melee"]
    },
{
    "name": "Improved Two-Weapon Fighting",
    "type": "Combat",
    "source": "Player's Handbook (D&D 3.5)",
    "description": "You can make an additional attack with your off-hand weapon.",
    "prerequisites": {"Dex": ">= 17", "Two-Weapon Fighting": True, "Base Attack Bonus": ">= 6"},
    "benefit": "You get a second attack with your off-hand weapon, albeit at a -5 penalty.",
    "limitations": "Your off-hand weapon must be light unless you have the Ambidexterity feat.",
    "tags": ["Combat", "Melee"]
    },
{
    "name": "Shield Proficiency",
    "type": "Combat",
    "source": "Player's Handbook (D&D 3.5)",
    "description": "You are skilled in using shields effectively in combat.",
    "prerequisites": {},
    "benefit": "You can use a shield and take only the standard penalties. Without this feat, a character using a shield takes the shield’s armor check penalty on attack rolls and skill checks that involve moving.",
    "limitations": "Does not include tower shields unless you have the Tower Shield Proficiency feat.",
    "tags": ["Combat", "Defensive"]
    },
{
    "name": "Greater Weapon Proficiency",
    "type": "Weapon-Specific",
    "source": "Homebrew/Expanded Rules (D&D 3.5)",
    "description": "You have exceptional skill with a specific weapon, surpassing standard proficiency.",
    "prerequisites": {"Proficiency with weapon": True, "Base Attack Bonus": ">= 12"},
    "benefit": "You gain a +1 bonus to attack rolls with the chosen weapon in addition to any other benefits from proficiency.",
    "limitations": "This feat applies only to one specific weapon. You can take this feat multiple times, each time applying to a different weapon.",
    "tags": ["Combat", "Weapon-Specific"]
    },
{
    "name": "Knock-Down",
    "type": "Melee Combat",
    "source": "Sword and Fist (D&D 3.5)",
    "description": "You can knock your opponents prone when you deal significant damage.",
    "prerequisites": {"Base Attack Bonus": ">= 2", "Improved Trip": True},
    "benefit": "Whenever you deal 10 or more points of damage to your opponent in melee, you can attempt to trip them as a free action.",
    "limitations": "This feat does not grant you a free trip attempt if you cannot reach the target after your melee attack.",
    "tags": ["Combat", "Melee"]
    },
{
    "name": "Improved Charge",
    "type": "Melee Combat",
    "source": "Homebrew/Expanded Rules (D&D 3.5)",
    "description": "You charge with greater precision and effectiveness.",
    "prerequisites": {"Base Attack Bonus": ">= 3"},
    "benefit": "When you charge, you gain a +3 bonus on your attack roll (instead of +2) and reduce the AC penalty to -1 (instead of -2).",
    "limitations": "The benefits apply only during a charge and do not affect other forms of movement or combat.",
    "tags": ["Combat", "Melee"]
    },

#-----------------------------ranged combat feats----------------------------------------------



{
    "name": "Point-Blank Shot",
    "type": "Ranged Combat",
    "source": "Player's Handbook (D&D 3.5)",
    "description": "You are skilled at making well-placed shots with ranged weapons at close range.",
    "prerequisites": {},
    "benefit": "You gain a +1 bonus on attack and damage rolls with ranged weapons against targets within 30 feet.",
    "limitations": "Only applies to ranged attacks within 30 feet.",
    "tags": ["Combat", "Ranged"]
    },
{
    "name": "Precise Shot",
    "type": "Ranged Combat",
    "source": "Player's Handbook (D&D 3.5)",
    "description": "You can shoot or throw ranged weapons at an opponent engaged in melee without penalties.",
    "prerequisites": {"Point-Blank Shot": True},
    "benefit": "You do not take the standard -4 penalty when firing into melee.",
    "limitations": "Requires Point-Blank Shot as a prerequisite.",
    "tags": ["Combat", "Ranged"]
    },
{
    "name": "Improved Precise Shot",
    "type": "Ranged Combat",
    "source": "Player's Handbook (D&D 3.5)",
    "description": "You can make ranged attacks with pinpoint accuracy, ignoring most obstacles.",
    "prerequisites": {"Dex": ">= 19", "Point-Blank Shot": True, "Precise Shot": True, "Base Attack Bonus": ">= 11"},
    "benefit": "Your ranged attacks ignore the AC bonus granted to targets by anything less than total cover and the miss chance granted to targets by anything less than total concealment. Total cover and total concealment still affect your attacks normally.",
    "limitations": "This feat does not negate the miss chance for total concealment or allow attacks against targets with total cover.",
    "tags": ["Combat", "Ranged"]
    },
{
    "name": "Rapid Shot",
    "type": "Ranged Combat",
    "source": "Player's Handbook (D&D 3.5)",
    "description": "You can make an additional ranged attack per round at the cost of accuracy.",
    "prerequisites": {"Dex": ">= 13", "Point-Blank Shot": True},
    "benefit": "When making a full attack action with a ranged weapon, you can make one extra attack per round. All your ranged attacks take a -2 penalty when using this feat.",
    "limitations": "This feat can only be used during a full attack action with a ranged weapon.",
    "tags": ["Combat", "Ranged"]
    },
{
    "name": "Manyshot",
    "type": "Ranged Combat",
    "source": "Player's Handbook (D&D 3.5)",
    "description": "You can fire multiple arrows with a single attack.",
    "prerequisites": {"Dex": ">= 17", "Point-Blank Shot": True, "Rapid Shot": True, "Base Attack Bonus": ">= 6"},
    "benefit": "As a standard action, you can fire two arrows at a single target within 30 feet. Both arrows use the same attack roll (with a -4 penalty) to determine success and deal damage normally. For every 5 points of Base Attack Bonus above +6, you can fire an additional arrow (three arrows at +11, four at +16). Each additional arrow applies an additional -2 penalty to the attack roll.",
    "limitations": "Applies only to bows and not other ranged weapons. Distance limitation is 30 feet.",
    "tags": ["Combat", "Ranged"]
    },
{
    "name": "Far Shot",
    "type": "Ranged Combat",
    "source": "Player's Handbook (D&D 3.5)",
    "description": "You can shoot or throw weapons at greater ranges than normal.",
    "prerequisites": {"Point-Blank Shot": True},
    "benefit": "When using a projectile weapon, such as a bow, its range increment increases by 50%. When using a thrown weapon, its range increment is doubled.",
    "limitations": "Applies only to ranged attacks and does not stack with similar effects that increase range increments.",
    "tags": ["Combat", "Ranged"]
    },
{
    "name": "Shot on the Run",
    "type": "Ranged Combat",
    "source": "Player's Handbook (D&D 3.5)",
    "description": "You can move both before and after making a ranged attack.",
    "prerequisites": {"Dex": ">= 13", "Dodge": True, "Mobility": True, "Point-Blank Shot": True, "Base Attack Bonus": ">= 4"},
    "benefit": "When using the attack action with a ranged weapon, you can move both before and after the attack, provided that your total distance moved does not exceed your speed.",
    "limitations": "You cannot take a full-attack action when using this feat. Applies only to ranged attacks.",
    "tags": ["Combat", "Ranged"]
    },
{
    "name": "Weapon Focus (Ranged)",
    "type": "Weapon-Specific",
    "source": "Player's Handbook (D&D 3.5)",
    "description": "You are especially skilled with a particular ranged weapon.",
    "prerequisites": {"Proficiency with weapon": True, "Base Attack Bonus": ">= 1"},
    "benefit": "You gain a +1 bonus on all attack rolls you make using the selected ranged weapon.",
    "limitations": "You must choose a specific ranged weapon (e.g., longbow, shortbow, or crossbow) when selecting this feat. This feat can be taken multiple times, each time applying to a different ranged weapon.",
    "tags": ["Combat", "Weapon-Specific", "Ranged"]
    },
{
    "name": "Weapon Specialization (Ranged)",
    "type": "Weapon-Specific",
    "source": "Player's Handbook (D&D 3.5)",
    "description": "You deal extra damage with a specific ranged weapon.",
    "prerequisites": {"Fighter Level": ">= 4", "Weapon Focus (Ranged)": True},
    "benefit": "You gain a +2 bonus on all damage rolls you make using the selected ranged weapon.",
    "limitations": "You must choose a specific ranged weapon (e.g., longbow, shortbow, or crossbow) when selecting this feat. This feat can be taken multiple times, each time applying to a different ranged weapon.",
    "tags": ["Combat", "Weapon-Specific", "Ranged"]
    },
{
    "name": "Greater Weapon Focus (Ranged)",
    "type": "Weapon-Specific",
    "source": "Player's Handbook (D&D 3.5)",
    "description": "You are exceptionally skilled with a particular ranged weapon.",
    "prerequisites": {"Fighter Level": ">= 8", "Weapon Focus (Ranged)": True},
    "benefit": "You gain an additional +1 bonus on all attack rolls you make using the selected ranged weapon. This bonus stacks with the bonus from Weapon Focus.",
    "limitations": "You must choose a specific ranged weapon (e.g., longbow, shortbow, or crossbow) when selecting this feat. This feat can be taken multiple times, each time applying to a different ranged weapon.",
    "tags": ["Combat", "Weapon-Specific", "Ranged"]
    },
{
    "name": "Greater Weapon Specialization (Ranged)",
    "type": "Weapon-Specific",
    "source": "Player's Handbook (D&D 3.5)",
    "description": "You deal even more damage with a specific ranged weapon.",
    "prerequisites": {"Fighter Level": ">= 12", "Weapon Specialization (Ranged)": True},
    "benefit": "You gain an additional +2 bonus on all damage rolls you make using the selected ranged weapon. This bonus stacks with the bonus from Weapon Specialization.",
    "limitations": "You must choose a specific ranged weapon (e.g., longbow, shortbow, or crossbow) when selecting this feat. This feat can be taken multiple times, each time applying to a different ranged weapon.",
    "tags": ["Combat", "Weapon-Specific", "Ranged"]
    },
{
    "name": "Quick Draw",
    "type": "Combat",
    "source": "Player's Handbook (D&D 3.5)",
    "description": "You can draw weapons with lightning speed.",
    "prerequisites": {"Base Attack Bonus": ">= 1"},
    "benefit": "You can draw a weapon as a free action instead of as a move action. You can draw a hidden weapon (see Sleight of Hand skill) as a move action.",
    "limitations": "This feat does not apply to retrieving items other than weapons.",
    "tags": ["Combat", "Utility"]
    },
{
    "name": "Deadly Aim",
    "type": "Ranged Combat",
    "source": "Pathfinder Core Rulebook (Adapted for D&D 3.5)",
    "description": "You can trade accuracy for greater damage with ranged weapons.",
    "prerequisites": {"Dex": ">= 13", "Base Attack Bonus": ">= 1"},
    "benefit": "Before making a ranged attack, you can choose to take a penalty on all ranged attack rolls up to your Base Attack Bonus. If you do, you gain a bonus on all ranged damage rolls equal to twice the penalty taken.",
    "limitations": "This feat cannot be used with touch attack spells or effects delivered through ranged weapons.",
    "tags": ["Combat", "Ranged"]
    },
{
    "name": "Clustered Shots",
    "type": "Ranged Combat",
    "source": "Pathfinder Core Rulebook (Adapted for D&D 3.5)",
    "description": "You can pool your ranged attacks to overcome damage reduction.",
    "prerequisites": {"Point-Blank Shot": True, "Precise Shot": True, "Base Attack Bonus": ">= 6"},
    "benefit": "When you use a full attack action with a ranged weapon, total the damage from all hits before applying the target's damage reduction.",
    "limitations": "Applies only to ranged attacks made as part of a full attack action.",
    "tags": ["Combat", "Ranged"]
    },
{
    "name": "Improved Snap Shot",
    "type": "Ranged Combat",
    "source": "Pathfinder Core Rulebook (Adapted for D&D 3.5)",
    "description": "You threaten a larger area with ranged weapons, making it harder for enemies to approach.",
    "prerequisites": {
        "Dex": ">= 15",
        "Point-Blank Shot": True,
        "Snap Shot": True,
        "Base Attack Bonus": ">= 6"
    },
    "benefit": "You increase the range at which you threaten squares with your ranged weapon by an additional 5 feet (to a total of 10 feet). Enemies within this area provoke attacks of opportunity when they take actions that provoke such attacks.",
    "limitations": "This feat does not increase your normal attack range and applies only to attacks of opportunity.",
    "tags": ["Combat", "Ranged"]
    },
{
    "name": "Snap Shot",
    "type": "Ranged Combat",
    "source": "Pathfinder Core Rulebook (Adapted for D&D 3.5)",
    "description": "You can make attacks of opportunity with your ranged weapon.",
    "prerequisites": {
        "Dex": ">= 13",
        "Point-Blank Shot": True,
        "Base Attack Bonus": ">= 6"
    },
    "benefit": "You threaten the area within 5 feet of you with your ranged weapon. You can make attacks of opportunity with your ranged weapon, though these attacks do not provoke attacks of opportunity themselves.",
    "limitations": "You can only threaten adjacent squares with this feat, and it applies only to ranged weapons.",
    "tags": ["Combat", "Ranged"]
    },
{
    "name": "Critical Focus (Ranged)",
    "type": "Combat",
    "source": "Pathfinder Core Rulebook (Adapted for D&D 3.5)",
    "description": "You are adept at landing critical hits with ranged weapons.",
    "prerequisites": {"Base Attack Bonus": ">= 9"},
    "benefit": "You gain a +4 bonus on attack rolls made to confirm critical hits with ranged weapons.",
    "limitations": "Applies only to ranged weapons and does not increase the likelihood of rolling a critical hit.",
    "tags": ["Combat", "Ranged", "Critical"]
    },
{
    "name": "Improved Critical (Ranged)",
    "type": "Weapon-Specific",
    "source": "Player's Handbook (D&D 3.5)",
    "description": "You know how to make critical hits more often with a specific ranged weapon.",
    "prerequisites": {"Proficiency with weapon": True, "Base Attack Bonus": ">= 8"},
    "benefit": "When using the selected ranged weapon, your threat range is doubled. For example, a longbow normally threatens a critical hit on a 20. With this feat, it threatens a critical hit on a 19–20.",
    "limitations": "This effect doesn’t stack with any other effect that expands the threat range of a weapon (such as the keen weapon property). You must choose a specific ranged weapon when selecting this feat.",
    "tags": ["Combat", "Weapon-Specific", "Ranged", "Critical"]
    },
{
    "name": "Pinpoint Targeting",
    "type": "Ranged Combat",
    "source": "Player's Handbook II (D&D 3.5)",
    "description": "You can target a specific point on an opponent, bypassing their armor.",
    "prerequisites": {
        "Dex": ">= 19",
        "Point-Blank Shot": True,
        "Precise Shot": True,
        "Base Attack Bonus": ">= 16"
    },
    "benefit": "As a standard action, you can make a single ranged attack against an opponent. Your target does not gain any armor, natural armor, or shield bonuses to AC against this attack. Other modifiers to AC, such as from Dexterity and deflection bonuses, still apply.",
    "limitations": "This feat can only be used with ranged weapons and applies to a single attack made as a standard action.",
    "tags": ["Combat", "Ranged", "Precision"]
    },
{
    "name": "Bullseye Shot",
    "type": "Ranged Combat",
    "source": "Pathfinder Core Rulebook (Adapted for D&D 3.5)",
    "description": "You take a moment to carefully aim, improving your accuracy with a single ranged attack.",
    "prerequisites": {"Dex": ">= 13", "Base Attack Bonus": ">= 1"},
    "benefit": "As a move action, you can gain a +4 bonus on your next ranged attack roll made before the end of your turn.",
    "limitations": "This feat applies only to a single ranged attack made after the aiming action, and the bonus is lost if no attack is made during the same turn.",
    "tags": ["Combat", "Ranged", "Precision"]
    },
{
    "name": "Parting Shot",
    "type": "Ranged Combat",
    "source": "Pathfinder Core Rulebook (Adapted for D&D 3.5)",
    "description": "You can make a quick ranged attack while retreating from combat.",
    "prerequisites": {"Dex": ">= 13", "Dodge": True, "Mobility": True, "Base Attack Bonus": ">= 6"},
    "benefit": "When you withdraw from a melee opponent, you can make a single ranged attack at your highest attack bonus against that opponent as part of your withdrawal action.",
    "limitations": "This feat can only be used during a withdrawal action and applies to a single ranged attack.",
    "tags": ["Combat", "Ranged", "Tactical"]
    },
{
    "name": "Crossbow Mastery",
    "type": "Ranged Combat",
    "source": "Pathfinder Core Rulebook (Adapted for D&D 3.5)",
    "description": "You are highly skilled with crossbows, enabling faster and more precise use.",
    "prerequisites": {"Dex": ">= 15", "Point-Blank Shot": True, "Rapid Reload": True, "Base Attack Bonus": ">= 6"},
    "benefit": "You can reload any type of crossbow as a free action. In addition, you do not provoke attacks of opportunity when firing a crossbow.",
    "limitations": "This feat applies only to crossbows and does not affect other ranged weapons.",
    "tags": ["Combat", "Ranged", "Weapon-Specific"]
    },
{
    "name": "Weapon Proficiency (Ranged)",
    "type": "Weapon-Specific",
    "source": "Player's Handbook (D&D 3.5)",
    "description": "You are proficient in the use of a specific ranged weapon.",
    "prerequisites": {},
    "benefit": "You make attack rolls with the chosen ranged weapon normally. Without this feat, you take a -4 penalty on attack rolls with the weapon.",
    "limitations": "You must choose one ranged weapon (e.g., longbow, shortbow, or crossbow) to become proficient with. This feat can be taken multiple times, each time applying to a different ranged weapon.",
    "tags": ["Combat", "Weapon-Specific", "Ranged"]
    },
{
    "name": "Disruptive Shot",
    "type": "Ranged Combat",
    "source": "Homebrew/Expanded Rules (D&D 3.5)",
    "description": "Your ranged attacks can interrupt an opponent's spellcasting.",
    "prerequisites": {"Point-Blank Shot": True, "Base Attack Bonus": ">= 6"},
    "benefit": "When you ready a ranged attack to disrupt a spellcaster, you gain a +4 bonus on the attack roll. If your attack hits and the spellcaster fails a Concentration check (DC 10 + damage dealt + spell level), their spell is disrupted.",
    "limitations": "This feat applies only when readying an action to interrupt spellcasting and does not affect other ranged attacks.",
    "tags": ["Combat", "Ranged", "Anti-Magic"]
    },
{
    "name": "Precise Throw",
    "type": "Ranged Combat",
    "source": "Homebrew/Expanded Rules (D&D 3.5)",
    "description": "You can make precise ranged attacks with thrown weapons.",
    "prerequisites": {"Point-Blank Shot": True, "Base Attack Bonus": ">= 3"},
    "benefit": "You can throw weapons at an opponent engaged in melee without taking the standard -4 penalty for ranged attacks into melee.",
    "limitations": "This feat applies only to thrown weapons and does not affect other ranged attacks.",
    "tags": ["Combat", "Ranged", "Thrown"]
    },
{
    "name": "Throw Anything",
    "type": "Ranged Combat",
    "source": "Pathfinder Core Rulebook (Adapted for D&D 3.5)",
    "description": "You are skilled at throwing improvised weapons effectively.",
    "prerequisites": {"Base Attack Bonus": ">= 1"},
    "benefit": "You do not take the -4 penalty for using an improvised weapon as a ranged weapon. Additionally, you gain a +1 bonus on attack rolls with thrown weapons and improvised weapons used as ranged attacks.",
    "limitations": "This feat applies only to thrown weapons or improvised weapons used as ranged attacks.",
    "tags": ["Combat", "Ranged", "Thrown", "Improvised"]
    },
{
    "name": "Point-Blank Master",
    "type": "Ranged Combat",
    "source": "Pathfinder Core Rulebook (Adapted for D&D 3.5)",
    "description": "You are adept at using ranged weapons even in close quarters.",
    "prerequisites": {"Weapon Specialization": True, "Base Attack Bonus": ">= 4"},
    "benefit": "Choose one type of ranged weapon (e.g., longbow, shortbow, or crossbow). You do not provoke attacks of opportunity when firing that type of ranged weapon while threatened.",
    "limitations": "You must choose a specific ranged weapon type when taking this feat. This feat can be taken multiple times, each time applying to a different ranged weapon type.",
    "tags": ["Combat", "Ranged", "Weapon-Specific"]
    },
{
    "name": "Penetrating Shot",
    "type": "Ranged Combat",
    "source": "Pathfinder Core Rulebook (Adapted for D&D 3.5)",
    "description": "Your ranged attacks can hit multiple targets in a line.",
    "prerequisites": {"Point-Blank Shot": True, "Precise Shot": True, "Base Attack Bonus": ">= 6"},
    "benefit": "When you make a single ranged attack, you can target all creatures in a straight line up to your weapon's first range increment. Make a single attack roll and compare the result to each target’s AC individually. Each target takes damage as if hit by the attack.",
    "limitations": "You cannot apply this feat to attacks that involve multiple projectiles (e.g., Manyshot). It works only with ranged weapons firing a single projectile.",
    "tags": ["Combat", "Ranged", "Multi-Target"]
    },
{
    "name": "Ricochet Shot",
    "type": "Ranged Combat",
    "source": "Homebrew/Expanded Rules (D&D 3.5)",
    "description": "You can make ranged attacks that bounce off surfaces to hit targets in cover.",
    "prerequisites": {"Point-Blank Shot": True, "Precise Shot": True, "Base Attack Bonus": ">= 6"},
    "benefit": "When making a ranged attack, you can target a creature in cover by ricocheting the shot off a nearby solid surface. You take a -2 penalty on the attack roll, but the target loses the benefit of cover for the attack (except total cover).",
    "limitations": "This feat applies only to ranged weapons and requires a solid surface within range to ricochet the shot. Cannot bypass total cover.",
    "tags": ["Combat", "Ranged", "Tactical"]
    },
{
    "name": "Coordinated Shot",
    "type": "Ranged Combat",
    "source": "Pathfinder Core Rulebook (Adapted for D&D 3.5)",
    "description": "You excel at making ranged attacks when an ally is threatening your target.",
    "prerequisites": {"Point-Blank Shot": True},
    "benefit": "You gain a +1 bonus on ranged attack rolls against opponents that are threatened by one of your allies. If your ally has this feat, the bonus increases to +2.",
    "limitations": "Applies only to targets that are threatened by at least one ally, and only to ranged attacks.",
    "tags": ["Combat", "Ranged", "Teamwork"]
    },
{
    "name": "Opening Volley",
    "type": "Ranged Combat",
    "source": "Pathfinder Core Rulebook (Adapted for D&D 3.5)",
    "description": "Your ranged attacks improve your subsequent melee strikes.",
    "prerequisites": {"Base Attack Bonus": ">= 1"},
    "benefit": "If you hit an opponent with a ranged attack, you gain a +4 bonus on your next melee attack roll against that opponent. This bonus must be used before the end of your next turn.",
    "limitations": "The bonus applies only to melee attacks and is lost if not used by the end of your next turn.",
    "tags": ["Combat", "Ranged", "Melee Synergy"]
    },
{
    "name": "Volley Shot",
    "type": "Ranged Combat",
    "source": "Homebrew/Expanded Rules (D&D 3.5)",
    "description": "You can target multiple enemies in a single attack with a volley of projectiles.",
    "prerequisites": {
        "Dex": ">= 17",
        "Point-Blank Shot": True,
        "Rapid Shot": True,
        "Base Attack Bonus": ">= 6"
    },
    "benefit": "As a full-round action, you can make a single ranged attack roll and compare it to the AC of up to three creatures within 30 feet of each other. Each creature hit takes normal damage from the attack.",
    "limitations": "This feat applies only to ranged weapons and requires a full-round action. The targets must be within 30 feet of each other, and you must be able to see all of them.",
    "tags": ["Combat", "Ranged", "Multi-Target"]
    },
#-----------------------------------mounted combat feats-------------------------------------------



{
    "name": "Mounted Combat",
    "type": "Mounted Combat",
    "source": "Player's Handbook (D&D 3.5)",
    "description": "You are adept at guiding your mount through combat.",
    "prerequisites": {"Ride skill": ">= 1 rank"},
    "benefit": "Once per round when your mount is hit in combat, you may attempt a Ride check to negate the hit. The hit is negated if your Ride check result is greater than the opponent's attack roll.",
    "limitations": "Applies only when mounted and does not affect attacks against the rider.",
    "tags": ["Combat", "Mounted"]
    },
{
    "name": "Ride-By Attack",
    "type": "Mounted Combat",
    "source": "Player's Handbook (D&D 3.5)",
    "description": "You can move through enemies while making mounted attacks.",
    "prerequisites": {"Mounted Combat": True},
    "benefit": "When you are mounted and use the charge action, you may move, attack, and then move again, continuing your movement in a straight line. Your total movement for the round cannot exceed double your mount's speed.",
    "limitations": "You cannot attack a second time during your movement or change direction after the attack.",
    "tags": ["Combat", "Mounted"]
    },
{
    "name": "Spirited Charge",
    "type": "Mounted Combat",
    "source": "Player's Handbook (D&D 3.5)",
    "description": "You deal extra damage when charging on a mount.",
    "prerequisites": {"Mounted Combat": True, "Ride-By Attack": True},
    "benefit": "When mounted and using the charge action, you deal double damage with a melee weapon (or triple damage with a lance).",
    "limitations": "Applies only to melee attacks made during a mounted charge.",
    "tags": ["Combat", "Mounted"]
    },
{
    "name": "Trample",
    "type": "Mounted Combat",
    "source": "Player's Handbook (D&D 3.5)",
    "description": "You can overrun enemies with your mount.",
    "prerequisites": {"Mounted Combat": True},
    "benefit": "When your mount attempts to overrun an opponent, the target may not choose to avoid you. If your mount knocks the target prone, it may make one hoof attack against the target as a free action.",
    "limitations": "Applies only to mounted overruns and requires your mount to attack.",
    "tags": ["Combat", "Mounted"]
    },
{
    "name": "Mounted Archery",
    "type": "Mounted Combat",
    "source": "Player's Handbook (D&D 3.5)",
    "description": "You are skilled at firing ranged weapons while mounted.",
    "prerequisites": {"Ride Skill": ">= 1 rank", "Mounted Combat": True},
    "benefit": "The penalty you take when using a ranged weapon while mounted is halved: -2 instead of -4 if your mount is taking a double move, and -4 instead of -8 if your mount is running.",
    "limitations": "This feat applies only while mounted and using ranged weapons.",
    "tags": ["Combat", "Mounted", "Ranged"]
    },
{
    "name": "Indomitable Mount",
    "type": "Mounted Combat",
    "source": "Complete Adventurer (D&D 3.5)",
    "description": "You and your mount work together to resist effects that would harm or hinder your mount.",
    "prerequisites": {"Ride Skill": ">= 5 ranks", "Mounted Combat": True},
    "benefit": "Whenever your mount is required to make a saving throw, you can make a Ride check instead of the saving throw. Use your Ride check result in place of the mount’s saving throw result.",
    "limitations": "This benefit applies only if you are actively riding the mount and able to take actions.",
    "tags": ["Combat", "Mounted", "Defensive"]
    },
{
    "name": "Mounted Shield",
    "type": "Mounted Combat",
    "source": "Complete Warrior (D&D 3.5)",
    "description": "You are adept at using a shield to protect both yourself and your mount.",
    "prerequisites": {"Ride Skill": ">= 5 ranks", "Shield Proficiency": True, "Mounted Combat": True},
    "benefit": "You can add your shield’s shield bonus to your mount’s AC, in addition to your own. This benefit lasts until the start of your next turn.",
    "limitations": "This feat applies only when actively using a shield and riding a mount. The shield bonus does not stack with other shield-related feats or effects.",
    "tags": ["Combat", "Mounted", "Defensive"]
    },
{
    "name": "Unseat",
    "type": "Mounted Combat",
    "source": "Complete Warrior (D&D 3.5)",
    "description": "You are skilled at unseating opponents while charging on horseback.",
    "prerequisites": {"Ride Skill": ">= 5 ranks", "Mounted Combat": True, "Spirited Charge": True},
    "benefit": "When charging an opponent while mounted and using a lance, you can attempt to unseat your opponent instead of dealing damage. Make a trip attempt against the target. If the attempt succeeds, the target is knocked prone and dismounted (if applicable).",
    "limitations": "This feat applies only to charge attacks made while mounted and using a lance. You provoke an attack of opportunity if you fail the trip attempt, unless you have the Improved Trip feat.",
    "tags": ["Combat", "Mounted", "Tactical"]
    },
{
    "name": "Born to the Saddle",
    "type": "Mounted Combat",
    "source": "Complete Adventurer (D&D 3.5)",
    "description": "You are particularly skilled at riding and controlling your mount.",
    "prerequisites": {"Ride Skill": ">= 1 rank"},
    "benefit": "You gain a +3 bonus on all Ride checks. Additionally, you can attempt to mount or dismount a steed as a free action, rather than a move action. You also gain a +1 bonus on attack rolls while mounted.",
    "limitations": "This feat applies only when you are mounted. The bonus to attack rolls does not stack with other feats or effects that enhance mounted attack rolls.",
    "tags": ["Combat", "Mounted", "Skill Enhancement"]
    },
{
    "name": "Cavalry Charger",
    "type": "Mounted Combat",
    "source": "Complete Warrior (D&D 3.5)",
    "description": "You excel at devastating charge attacks while mounted.",
    "prerequisites": {
        "Ride Skill": ">= 8 ranks",
        "Mounted Combat": True,
        "Ride-By Attack": True,
        "Spirited Charge": True
    },
    "benefit": """You gain access to three special charge options while mounted: 
        "\n- **Leaping Charge**: If you attempt a jump as part of your charge, you deal an additional +2d6 damage on a successful attack. "
        "\n- **Unstoppable Charge**: If your charge attack successfully hits, your mount can overrun opponents in your path without provoking attacks of opportunity. "
        "\n- **Trample Charge**: If your charge attack successfully hits, your mount can make a hoof attack against the target as a free action.""",
    "limitations": "These benefits apply only during mounted charge attacks and require the proper setup and space to execute.",
    "tags": ["Combat", "Mounted", "Tactical"]
    },
{
    "name": "Improved Mounted Archery",
    "type": "Mounted Combat",
    "source": "Complete Warrior (D&D 3.5)",
    "description": "You are an expert at firing ranged weapons while mounted, even at high speeds.",
    "prerequisites": {
        "Ride Skill": ">= 6 ranks",
        "Mounted Combat": True,
        "Mounted Archery": True
    },
    "benefit": "The penalty you take when using a ranged weapon while your mount is moving is eliminated. If your mount is running, the penalty is halved to -2 instead of -4.",
    "limitations": "This feat applies only while mounted and using ranged weapons.",
    "tags": ["Combat", "Mounted", "Ranged"]
    },
{
    "name": "Improved Overrun (Mounted)",
    "type": "Mounted Combat",
    "source": "Complete Warrior (D&D 3.5)",
    "description": "You are skilled at using your mount to overrun opponents in your path.",
    "prerequisites": {
        "Ride Skill": ">= 4 ranks",
        "Mounted Combat": True
    },
    "benefit": "When using your mount to overrun an opponent, the target cannot choose to avoid you. If your overrun attempt is successful, your mount can immediately make a hoof attack against the target as a free action.",
    "limitations": "This feat applies only to mounted overruns and requires sufficient movement to perform the action.",
    "tags": ["Combat", "Mounted", "Tactical"]
    },
{
    "name": "Improved Charge (Mounted)",
    "type": "Mounted Combat",
    "source": "Complete Warrior (D&D 3.5)",
    "description": "You are highly skilled at delivering devastating charge attacks while mounted.",
    "prerequisites": {
        "Ride Skill": ">= 4 ranks",
        "Mounted Combat": True,
        "Ride-By Attack": True
    },
    "benefit": "When you make a charge attack while mounted, you gain a +4 bonus on attack rolls instead of the normal +2 bonus. Additionally, if your charge attack hits, your mount can make a hoof attack against the target as a free action.",
    "limitations": "This feat applies only to charge attacks made while mounted.",
    "tags": ["Combat", "Mounted", "Tactical"]
    },
{
    "name": "Mounted Maneuver",
    "type": "Mounted Combat",
    "source": "Homebrew/Expanded Rules (D&D 3.5)",
    "description": "You are skilled at executing combat maneuvers while mounted.",
    "prerequisites": {
        "Ride Skill": ">= 6 ranks",
        "Mounted Combat": True
    },
    "benefit": "When you perform a combat maneuver (such as Bull Rush, Grapple, or Trip) while mounted, you gain a +2 bonus on the opposed roll or skill check. Additionally, your mount does not provoke attacks of opportunity when moving into position to perform the maneuver.",
    "limitations": "This feat applies only when you are mounted and performing combat maneuvers.",
    "tags": ["Combat", "Mounted", "Maneuvers"]
    },
{
    "name": "Defensive Rider",
    "type": "Mounted Combat",
    "source": "Homebrew/Expanded Rules (D&D 3.5)",
    "description": "You are skilled at defending yourself and your mount from harm while mounted.",
    "prerequisites": {
        "Ride Skill": ">= 5 ranks",
        "Mounted Combat": True
    },
    "benefit": "You gain a +2 bonus to your mount’s Armor Class against attacks of opportunity provoked by its movement. Additionally, you gain a +1 dodge bonus to your own AC while mounted.",
    "limitations": "This feat applies only while mounted and does not stack with other dodge bonuses.",
    "tags": ["Combat", "Mounted", "Defensive"]
    },
{
    "name": "Combat Riding",
    "type": "Mounted Combat",
    "source": "Homebrew/Expanded Rules (D&D 3.5)",
    "description": "You and your mount move as one, making it harder for enemies to target you.",
    "prerequisites": {
        "Ride Skill": ">= 5 ranks",
        "Mounted Combat": True
    },
    "benefit": "While mounted, you gain a +2 bonus on Ride checks to control your mount in combat. Additionally, your mount gains a +2 dodge bonus to AC against ranged attacks.",
    "limitations": "This feat applies only while mounted. The bonuses apply only in combat situations.",
    "tags": ["Combat", "Mounted", "Skill Enhancement"]
    },
{
    "name": "Coordinated Charge",
    "type": "Mounted Combat",
    "source": "Homebrew/Expanded Rules (D&D 3.5)",
    "description": "You and your mount work together seamlessly to execute powerful charge attacks.",
    "prerequisites": {
        "Ride Skill": ">= 8 ranks",
        "Mounted Combat": True,
        "Spirited Charge": True
    },
    "benefit": "When you make a charge attack while mounted, your mount can make a melee attack against the same target at the end of the charge as a free action. Additionally, you and your mount gain a +2 bonus on attack rolls made during a charge.",
    "limitations": "This feat applies only to mounted charge attacks. The mount’s attack is limited to its natural weapons.",
    "tags": ["Combat", "Mounted", "Tactical"]
    },
{
    "name": "Ride Mastery",
    "type": "Mounted Combat",
    "source": "Homebrew/Expanded Rules (D&D 3.5)",
    "description": "You are highly skilled in riding, allowing you and your mount to perform complex maneuvers with ease.",
    "prerequisites": {
        "Ride Skill": ">= 10 ranks",
        "Mounted Combat": True,
        "Born to the Saddle": True
    },
    "benefit": "You gain a +4 bonus on all Ride checks. Additionally, you and your mount gain a +1 bonus to Reflex saves. You can guide your mount with your knees, allowing you to use both hands for combat without penalty.",
    "limitations": "This feat applies only while mounted. Reflex save bonuses apply only to saves made while you are mounted.",
    "tags": ["Combat", "Mounted", "Skill Enhancement"]
    },
{
    "name": "Battlefield Agility (Mounted)",
    "type": "Mounted Combat",
    "source": "Homebrew/Expanded Rules (D&D 3.5)",
    "description": "You and your mount can move through the chaos of battle with precision and ease.",
    "prerequisites": {
        "Ride Skill": ">= 8 ranks",
        "Mounted Combat": True,
        "Mobility": True
    },
    "benefit": "While mounted, your mount can move through threatened areas and difficult terrain without provoking attacks of opportunity. Additionally, you and your mount gain a +2 bonus to AC against attacks of opportunity provoked by movement.",
    "limitations": "This feat applies only while mounted and does not allow movement through areas of total obstruction.",
    "tags": ["Combat", "Mounted", "Tactical"]
    },
{
    "name": "Horseman’s Bond",
    "type": "Mounted Combat",
    "source": "Homebrew/Expanded Rules (D&D 3.5)",
    "description": "You and your mount share an exceptional bond, allowing you to communicate and coordinate seamlessly.",
    "prerequisites": {
        "Ride Skill": ">= 6 ranks",
        "Mounted Combat": True,
        "Handle Animal Skill": ">= 4 ranks"
    },
    "benefit": "You and your mount gain a +2 bonus on saving throws against fear and compulsion effects. Additionally, you can communicate simple commands to your mount with a free action, even in combat.",
    "limitations": "This feat applies only to your bonded mount and requires an established bond (e.g., a special mount, animal companion, or similarly trained creature).",
    "tags": ["Combat", "Mounted", "Defensive"]
    },
{
    "name": "Riding Sweep",
    "type": "Mounted Combat",
    "source": "Homebrew/Expanded Rules (D&D 3.5)",
    "description": "You are skilled at striking multiple foes in a single mounted pass.",
    "prerequisites": {
        "Ride Skill": ">= 8 ranks",
        "Mounted Combat": True,
        "Cleave": True
    },
    "benefit": "While mounted, if you hit an opponent with a melee attack during a charge, you can make an additional melee attack against another opponent adjacent to your path. The second attack uses the same attack bonus as the first attack, but all attacks made this round take a -2 penalty.",
    "limitations": "This feat applies only during a mounted charge and works with melee attacks only.",
    "tags": ["Combat", "Mounted", "Multi-Target"]
    },
{
    "name": "Mounted Recovery",
    "type": "Mounted Combat",
    "source": "Homebrew/Expanded Rules (D&D 3.5)",
    "description": "You and your mount are skilled at regaining your footing and composure after being knocked down or disrupted.",
    "prerequisites": {
        "Ride Skill": ">= 6 ranks",
        "Mounted Combat": True
    },
    "benefit": "If your mount is knocked prone, you can make a Ride check (DC 15) as an immediate action to allow your mount to stand as a free action without provoking attacks of opportunity. Additionally, you gain a +2 bonus on saving throws to avoid being dismounted.",
    "limitations": "This feat applies only when you are mounted. The benefit to standing requires sufficient movement to stand normally.",
    "tags": ["Combat", "Mounted", "Defensive"]
    },
#-----------------------------------unarmed combat feats-------------------------------------------




{
    "name": "Improved Unarmed Strike",
    "type": "Unarmed Combat",
    "source": "Player's Handbook (D&D 3.5)",
    "description": "You are considered armed even when unarmed.",
    "prerequisites": {},
    "benefit": "Your unarmed strikes can deal lethal damage, and you are considered armed even when unarmed.",
    "limitations": "Does not grant proficiency with specific unarmed combat styles.",
    "tags": ["Combat", "Unarmed"]
    },
{
    "name": "Stunning Fist",
    "type": "Unarmed Combat",
    "source": "Player's Handbook (D&D 3.5)",
    "description": "You can stun opponents with a well-placed unarmed strike.",
    "prerequisites": {"Dex": ">= 13", "Wis": ">= 13", "Improved Unarmed Strike": True, "Base Attack Bonus": ">= 8"},
    "benefit": "You can attempt a stunning attack once per day per level. A stunned opponent cannot take actions, loses any Dexterity bonus to AC, and takes a -2 penalty to AC.",
    "limitations": "Only usable with unarmed strikes and requires a high Dexterity and Wisdom.",
    "tags": ["Combat", "Unarmed"]
    },
{
    "name": "Improved Grapple",
    "type": "Unarmed Combat",
    "source": "Player's Handbook (D&D 3.5)",
    "description": "You are skilled at grappling opponents without exposing yourself to danger.",
    "prerequisites": {"Dex": ">= 13", "Improved Unarmed Strike": True},
    "benefit": "You do not provoke an attack of opportunity when you attempt to grapple a foe. You also gain a +4 bonus on all grapple checks, regardless of whether you started the grapple.",
    "limitations": "Only applies to melee combat involving grappling maneuvers.",
    "tags": ["Combat", "Unarmed"]
    },
{
    "name": "Greater Grapple",
    "type": "Unarmed Combat",
    "source": "Pathfinder Core Rulebook (Adapted for D&D 3.5)",
    "description": (
        "You are exceptionally skilled at maintaining and improving your grappling techniques. "
        "When grappling, you can maintain the grapple as a move action, rather than as a standard action. "
        "This allows you to perform another standard action, such as making an attack or attempting another combat maneuver."
    ),
    "prerequisites": {
        "Dex": ">= 13",
        "Improved Grapple": True,
        "Base Attack Bonus": ">= 6"
    },
    "benefit": "Maintain a grapple as a move action, allowing additional actions during the same turn.",
    "limitations": "You must already have the Improved Grapple feat and meet the prerequisites.",
    "tags": ["Combat", "Unarmed", "Grappling"]
    },
{
    "name": "Pinning Knockout",
    "type": "Unarmed Combat",
    "source": "Homebrew/Expanded Rules (D&D 3.5)",
    "description": (
        "You can knock an opponent unconscious while pinning them in a grapple. "
        "When you successfully maintain a pin against an opponent, you can make an unarmed strike. "
        "If the strike deals damage, the opponent must make a Fortitude save (DC 10 + your base attack bonus + your Strength modifier) or fall unconscious for 1d4 rounds."
    ),
    "prerequisites": {
        "Improved Grapple": True,
        "Greater Grapple": True,
        "Base Attack Bonus": ">= 9"
    },
    "benefit": "Knock an opponent unconscious during a grapple pin if they fail a Fortitude save.",
    "limitations": "This feat can only be used on creatures that can be grappled and are not immune to being unconscious.",
    "tags": ["Combat", "Unarmed", "Grappling"]
    },
{
    "name": "Deflect Arrows",
    "type": "Defensive",
    "source": "Player's Handbook (D&D 3.5)",
    "description": "You can deflect one ranged weapon attack per round.",
    "prerequisites": {"Dex": ">= 13", "Improved Unarmed Strike": True},
    "benefit": "Once per round when you would normally be hit by a ranged weapon attack, you may deflect it so that you take no damage. You must be aware of the attack and not flat-footed. Attempting to deflect a ranged weapon doesn't count as an action.",
    "limitations": "You must have at least one hand free (holding nothing) to use this feat. Magical projectiles cannot be deflected.",
    "tags": ["Combat", "Defensive"]
    },
{
    "name": "Snatch Arrows",
    "type": "Unarmed Combat",
    "source": "Player's Handbook (D&D 3.5)",
    "description": (
        "You are adept at catching ranged weapons aimed at you. "
        "When you successfully deflect an arrow or other ranged weapon with the Deflect Arrows feat, you can catch the weapon instead of merely deflecting it. "
        "If you have a free hand, you can immediately make a ranged attack with the captured weapon, even if it is not your turn."
    ),
    "prerequisites": {
        "Dex": ">= 15",
        "Improved Unarmed Strike": True,
        "Deflect Arrows": True
    },
    "benefit": "Catch and optionally return ranged weapons aimed at you.",
    "limitations": "You must have a free hand to catch and throw the weapon, and you cannot use this feat against magical or oversized projectiles.",
    "tags": ["Combat", "Unarmed", "Defensive"]
    },
{
    "name": "Improved Disarm",
    "type": "Combat Maneuver",
    "source": "Player's Handbook (D&D 3.5)",
    "description": (
        "You are skilled at knocking weapons or objects from an opponent’s grasp. "
        "You do not provoke an attack of opportunity when attempting to disarm an opponent, "
        "and you gain a +4 bonus on your opposed attack roll when making the attempt."
    ),
    "prerequisites": {
        "Int": ">= 13",
        "Combat Expertise": True
    },
    "benefit": "Avoid attacks of opportunity when disarming, and gain a +4 bonus on disarm attempts.",
    "limitations": "This feat applies only to the disarm combat maneuver.",
    "tags": ["Combat", "Maneuver"]
    },
{
    "name": "Greater Disarm",
    "type": "Combat Maneuver",
    "source": "Pathfinder Core Rulebook (Adapted for D&D 3.5)",
    "description": (
        "You are exceptionally skilled at disarming opponents, leaving them vulnerable and unarmed. "
        "Whenever you successfully disarm an opponent, the disarmed weapon or object lands up to 15 feet away from its previous wielder, in a direction of your choice."
    ),
    "prerequisites": {
        "Int": ">= 13",
        "Combat Expertise": True,
        "Improved Disarm": True,
        "Base Attack Bonus": ">= 6"
    },
    "benefit": "Increase the effectiveness of disarm attempts by causing disarmed weapons to land farther away from their wielder.",
    "limitations": "This feat applies only to the disarm combat maneuver.",
    "tags": ["Combat", "Maneuver"]
    },
{
    "name": "Improved Trip",
    "type": "Combat Maneuver",
    "source": "Player's Handbook (D&D 3.5)",
    "description": (
        "You are skilled at knocking opponents to the ground in melee combat. "
        "You do not provoke an attack of opportunity when attempting to trip an opponent, "
        "and you gain a +4 bonus on your Strength check to trip an opponent."
    ),
    "prerequisites": {
        "Int": ">= 13",
        "Combat Expertise": True
    },
    "benefit": "Avoid attacks of opportunity when tripping, and gain a +4 bonus on trip attempts.",
    "limitations": "This feat applies only to the trip combat maneuver.",
    "tags": ["Combat", "Maneuver"]
    },
{
    "name": "Greater Trip",
    "type": "Combat Maneuver",
    "source": "Pathfinder Core Rulebook (Adapted for D&D 3.5)",
    "description": (
        "You excel at knocking your opponents to the ground and exploiting their disadvantage. "
        "Whenever you successfully trip an opponent, that opponent provokes an attack of opportunity from you and any allies who threaten it."
    ),
    "prerequisites": {
        "Int": ">= 13",
        "Combat Expertise": True,
        "Improved Trip": True,
        "Base Attack Bonus": ">= 6"
    },
    "benefit": "Trigger attacks of opportunity from you and your allies when you successfully trip an opponent.",
    "limitations": "This feat applies only to the trip combat maneuver.",
    "tags": ["Combat", "Maneuver"]
    },
{
    "name": "Improved Feint",
    "type": "Combat Maneuver",
    "source": "Player's Handbook (D&D 3.5)",
    "description": (
        "You are skilled at misleading opponents in combat. "
        "You can make a feint as a move action instead of a standard action."
    ),
    "prerequisites": {
        "Int": ">= 13",
        "Combat Expertise": True
    },
    "benefit": "Allows you to feint in combat as a move action.",
    "limitations": "This feat applies only to feint actions performed in combat.",
    "tags": ["Combat", "Maneuver"]
    },
{
    "name": "Ki Throw",
    "type": "Combat Maneuver",
    "source": "Pathfinder Core Rulebook (Adapted for D&D 3.5)",
    "description": (
        "You can throw opponents to the ground or into other creatures with precision. "
        "Whenever you successfully trip an opponent, you can choose to throw them instead. "
        "The opponent lands prone in a square you choose within 10 feet of their original position. "
        "If you throw the opponent into another creature’s space, the second creature must succeed on a Reflex save (DC 10 + your Strength modifier) or fall prone."
    ),
    "prerequisites": {
        "Improved Trip": True,
        "Base Attack Bonus": ">= 6"
    },
    "benefit": "Trip opponents and move them to a space within 10 feet, potentially affecting another creature.",
    "limitations": "This feat applies only to the trip combat maneuver, and the throw must end in a valid square.",
    "tags": ["Combat", "Maneuver", "Tactical"]
    },
{
    "name": "Prone Throw",
    "type": "Combat Maneuver",
    "source": "Homebrew/Expanded Rules (D&D 3.5)",
    "description": (
        "You can quickly recover from a prone position while making an attack. "
        "If you are prone and attacked in melee, you can make an immediate trip attempt against your attacker without provoking an attack of opportunity. "
        "If your trip attempt is successful, you can stand as a free action."
    ),
    "prerequisites": {
        "Dex": ">= 13",
        "Improved Trip": True,
        "Base Attack Bonus": ">= 6"
    },
    "benefit": "Allows you to make a trip attempt as an immediate action while prone and stand if successful.",
    "limitations": "This feat applies only while you are prone and attacked in melee.",
    "tags": ["Combat", "Maneuver", "Defensive"]
    },
{
    "name": "Crushing Blow",
    "type": "Combat Maneuver",
    "source": "Homebrew/Expanded Rules (D&D 3.5)",
    "description": (
        "You deliver devastating blows with overwhelming force. "
        "As a standard action, you can make a single melee attack with a +4 bonus to damage rolls. "
        "If this attack successfully strikes a creature, they must succeed on a Fortitude save (DC 10 + half your character level + your Strength modifier) or be staggered for 1 round."
    ),
    "prerequisites": {
        "Str": ">= 15",
        "Power Attack": True,
        "Base Attack Bonus": ">= 6"
    },
    "benefit": "Deal extra damage and potentially stagger opponents with a single powerful melee attack.",
    "limitations": "This feat requires a standard action and applies only to melee attacks.",
    "tags": ["Combat", "Maneuver", "Powerful Strike"]
    },
{
    "name": "Earth’s Embrace",
    "type": "Combat Maneuver",
    "source": "Complete Warrior (D&D 3.5)",
    "description": (
        "You can crush opponents when you have them in a grapple. "
        "If you succeed in maintaining a grapple and deal damage, you can choose to deal an additional 1d12 damage. "
        "You and your opponent both take a -2 penalty to AC while this ability is active."
    ),
    "prerequisites": {
        "Improved Grapple": True,
        "Base Attack Bonus": ">= 4"
    },
    "benefit": "Deal an additional 1d12 damage during a grapple but suffer a temporary AC penalty.",
    "limitations": "This feat applies only while maintaining a grapple, and both participants suffer the AC penalty.",
    "tags": ["Combat", "Maneuver", "Grappling"]
    },
{
    "name": "Falling Star Strike",
    "type": "Combat Maneuver",
    "source": "Complete Warrior (D&D 3.5)",
    "description": (
        "You can deliver precise strikes that temporarily blind your opponent. "
        "As a standard action, you can make a melee attack. If the attack deals damage, "
        "your target must succeed on a Fortitude save (DC 10 + half your character level + your Wisdom modifier) or be blinded for 1d4 rounds."
    ),
    "prerequisites": {
        "Wis": ">= 15",
        "Improved Unarmed Strike": True,
        "Stunning Fist": True,
        "Base Attack Bonus": ">= 6"
    },
    "benefit": "Inflict blindness on an opponent with a successful melee attack.",
    "limitations": "This feat applies only to melee attacks and requires the use of a standard action.",
    "tags": ["Combat", "Maneuver", "Unarmed"]
    },
{
    "name": "Improved Bull Rush (Unarmed)",
    "type": "Combat Maneuver",
    "source": "Player's Handbook (D&D 3.5)",
    "description": (
        "You are skilled at using your unarmed strikes to push opponents. "
        "You do not provoke an attack of opportunity when performing a bull rush unarmed, "
        "and you gain a +4 bonus on the opposed Strength check to push your opponent back."
    ),
    "prerequisites": {
        "Str": ">= 13",
        "Power Attack": True,
        "Improved Unarmed Strike": True
    },
    "benefit": "Avoid attacks of opportunity and gain a +4 bonus on unarmed bull rush attempts.",
    "limitations": "This feat applies only to bull rush attempts performed unarmed.",
    "tags": ["Combat", "Maneuver", "Unarmed"]
    },
{
    "name": "Elusive Target",
    "type": "Combat Maneuver",
    "source": "Complete Warrior (D&D 3.5)",
    "description": (
        "You are adept at avoiding blows in melee combat, using your agility and awareness to your advantage. "
        "While fighting defensively or using the total defense action, your opponents cannot gain flanking bonuses against you, "
        "and you cannot be the target of an attack of opportunity triggered by your movement."
    ),
    "prerequisites": {
        "Dex": ">= 13",
        "Dodge": True,
        "Mobility": True
    },
    "benefit": "Negate flanking bonuses and avoid attacks of opportunity triggered by movement when fighting defensively.",
    "limitations": "This feat applies only when you are fighting defensively or using the total defense action.",
    "tags": ["Combat", "Defensive", "Maneuver"]
    },
{
    "name": "Chokehold",
    "type": "Combat Maneuver",
    "source": "Complete Warrior (D&D 3.5)",
    "description": (
        "You can incapacitate an opponent by cutting off their air supply. "
        "While grappling, if you succeed in pinning your opponent, you can prevent them from speaking or casting spells with verbal components. "
        "Additionally, the opponent must make a Fortitude save (DC 10 + half your character level + your Strength modifier) each round or fall unconscious for 1d3 rounds."
    ),
    "prerequisites": {
        "Improved Grapple": True,
        "Base Attack Bonus": ">= 6"
    },
    "benefit": "Prevent an opponent from speaking and potentially render them unconscious while pinning.",
    "limitations": "This feat applies only while maintaining a pin during a grapple.",
    "tags": ["Combat", "Maneuver", "Grappling"]
    },
{
    "name": "Flying Kick",
    "type": "Combat Maneuver",
    "source": "Complete Warrior (D&D 3.5)",
    "description": (
        "You can launch yourself into a devastating unarmed strike. "
        "When charging, you can make an unarmed strike at the end of your charge. "
        "If the attack hits, you deal an additional 1d12 points of damage."
    ),
    "prerequisites": {
        "Improved Unarmed Strike": True,
        "Base Attack Bonus": ">= 3"
    },
    "benefit": "Deal an additional 1d12 damage on a successful unarmed strike at the end of a charge.",
    "limitations": "This feat applies only to unarmed strikes made as part of a charge.",
    "tags": ["Combat", "Maneuver", "Unarmed"]
    },
{
    "name": "Improved Overrun (Unarmed)",
    "type": "Combat Maneuver",
    "source": "Player's Handbook (D&D 3.5)",
    "description": (
        "You are adept at using your unarmed combat skills to force your way through opponents. "
        "You do not provoke an attack of opportunity when performing an unarmed overrun attempt, "
        "and your opponent may not choose to avoid you. "
        "Additionally, you gain a +4 bonus on your Strength check to knock your opponent prone."
    ),
    "prerequisites": {
        "Str": ">= 13",
        "Power Attack": True,
        "Improved Unarmed Strike": True
    },
    "benefit": "Avoid attacks of opportunity, prevent opponents from avoiding you, and gain a +4 bonus on overrun attempts.",
    "limitations": "This feat applies only to unarmed overrun attempts.",
    "tags": ["Combat", "Maneuver", "Unarmed"]
    },
#-----------------------------------defensive combat feats------------------------------------------




{
    "name": "Dodge",
    "type": "Defensive",
    "source": "Player's Handbook (D&D 3.5)",
    "description": "You are adept at avoiding attacks.",
    "prerequisites": {"Dex": ">= 13"},
    "benefit": "During your turn, you can designate an opponent and gain a +1 dodge bonus to AC against attacks from that opponent. You can select a new opponent on any turn.",
    "limitations": "You lose the dodge bonus whenever you are denied your Dexterity bonus to AC.",
    "tags": ["Combat", "Defensive"]
    },
{
    "name": "Mobility",
    "type": "Defensive",
    "source": "Player's Handbook (D&D 3.5)",
    "description": "You are adept at moving past opponents without being harmed.",
    "prerequisites": {"Dex": ">= 13", "Dodge": True},
    "benefit": "You gain a +4 dodge bonus to AC against attacks of opportunity caused when you move out of or within a threatened area.",
    "limitations": "You lose this dodge bonus whenever you are denied your Dexterity bonus to AC.",
    "tags": ["Combat", "Defensive"]
    },
{
    "name": "Combat Reflexes",
    "type": "Combat Maneuver",
    "source": "Player's Handbook (D&D 3.5)",
    "description": (
        "You are adept at taking advantage of openings in combat. "
        "You may make a number of additional attacks of opportunity per round equal to your Dexterity modifier. "
        "With this feat, you can also make attacks of opportunity while flat-footed."
    ),
    "prerequisites": {
        "Dex": ">= 13"
    },
    "benefit": "Gain additional attacks of opportunity per round equal to your Dexterity modifier and attack of opportunity capability while flat-footed.",
    "limitations": "You cannot exceed your total attacks of opportunity in a single round.",
    "tags": ["Combat", "Defensive"]
    },
{
    "name": "Iron Will",
    "type": "General",
    "source": "Player's Handbook (D&D 3.5)",
    "description": (
        "Your determination and mental fortitude are exceptional. "
        "You gain a +2 bonus on all Will saving throws."
    ),
    "prerequisites": {},
    "benefit": "Gain a +2 bonus on all Will saving throws.",
    "limitations": "This feat does not stack with other effects that provide a bonus to Will saves.",
    "tags": ["Combat", "Defensive", "Saving Throws"]
    },
{
    "name": "Lightning Reflexes",
    "type": "General",
    "source": "Player's Handbook (D&D 3.5)",
    "description": (
        "You have exceptional reflexes, allowing you to react swiftly to danger. "
        "You gain a +2 bonus on all Reflex saving throws."
    ),
    "prerequisites": {},
    "benefit": "Gain a +2 bonus on all Reflex saving throws.",
    "limitations": "This feat does not stack with other effects that provide a bonus to Reflex saves.",
    "tags": ["Combat", "Defensive", "Saving Throws"]
    },
{
    "name": "Great Fortitude",
    "type": "General",
    "source": "Player's Handbook (D&D 3.5)",
    "description": (
        "Your physical endurance and resilience are extraordinary. "
        "You gain a +2 bonus on all Fortitude saving throws."
    ),
    "prerequisites": {},
    "benefit": "Gain a +2 bonus on all Fortitude saving throws.",
    "limitations": "This feat does not stack with other effects that provide a bonus to Fortitude saves.",
    "tags": ["Combat", "Defensive", "Saving Throws"]
    },
{
    "name": "Toughness",
    "type": "Defensive",
    "source": "Player's Handbook (D&D 3.5)",
    "description": "You are tougher than normal, granting you extra hit points.",
    "prerequisites": {},
    "benefit": "You gain +3 hit points.",
    "limitations": "This feat may be taken multiple times. Its effects stack.",
    "tags": ["Combat", "Defensive"]
    },
{
    "name": "Endurance",
    "type": "Defensive",
    "source": "Player's Handbook (D&D 3.5)",
    "description": "You are capable of performing extended physical tasks and surviving harsh conditions.",
    "prerequisites": {},
    "benefit": "You gain a +4 bonus on the following checks and saves: Swim checks to resist nonlethal damage, Constitution checks to continue running, Constitution checks to avoid nonlethal damage from a forced march, Constitution checks to hold your breath, Constitution checks to avoid nonlethal damage from starvation or thirst, and Fortitude saves to avoid nonlethal damage from hot or cold environments. You can sleep in light or medium armor without becoming fatigued.",
    "limitations": "Does not remove penalties from heavy armor fatigue.",
    "tags": ["Combat", "Defensive"]
    },
{
    "name": "Diehard",
    "type": "Defensive",
    "source": "Player's Handbook (D&D 3.5)",
    "description": "You can remain conscious and continue fighting even when severely wounded.",
    "prerequisites": {"Endurance": True},
    "benefit": "When reduced to between -1 and -9 hit points, you automatically become stable. You do not have to make Constitution checks to remain stable. You can choose to act as if you were disabled, rather than dying. You can take a single move action or standard action each turn, but not both, and you take 1 point of damage after any standard action.",
    "limitations": "You are still unconscious and dying when your hit points drop to -10 or lower.",
    "tags": ["Combat", "Defensive"]
    },
{
    "name": "Improved Evasion",
    "type": "Defensive",
    "source": "Player's Handbook (D&D 3.5)",
    "description": (
        "You are highly adept at avoiding area effects and reducing damage. "
        "You take no damage on a successful Reflex save against attacks that normally deal half damage on a successful save. "
        "Additionally, you only take half damage even if you fail the save."
    ),
    "prerequisites": {
        "Evasion": True
    },
    "benefit": "Negate all damage on a successful Reflex save and take only half damage on a failed save against area attacks.",
    "limitations": "This feat requires that you already possess the Evasion ability.",
    "tags": ["Combat", "Defensive", "Saving Throws"]
    },
{
    "name": "Defensive Combat Training",
    "type": "Defensive",
    "source": "Pathfinder Core Rulebook (Adapted for D&D 3.5)",
    "description": (
        "You have been trained to avoid being caught off-guard in combat. "
        "You treat your base attack bonus as equal to your character level for the purpose of calculating your Combat Maneuver Defense (CMD)."
    ),
    "prerequisites": {},
    "benefit": "Your Combat Maneuver Defense is calculated as if your base attack bonus is equal to your character level.",
    "limitations": "This feat affects only your Combat Maneuver Defense (CMD) and does not alter other combat mechanics.",
    "tags": ["Combat", "Defensive"]
    },
{
    "name": "Improved Feint",
    "type": "Combat Maneuver",
    "source": "Player's Handbook (D&D 3.5)",
    "description": (
        "You are skilled at misleading your opponents in combat. "
        "You can feint in combat as a move action instead of a standard action, "
        "allowing you to deceive opponents and make them lose their Dexterity bonus to AC."
    ),
    "prerequisites": {
        "Int": ">= 13",
        "Combat Expertise": True
    },
    "benefit": "You can feint in combat as a move action, enabling tactical advantages.",
    "limitations": "This feat applies only to feint actions performed in melee combat.",
    "tags": ["Combat", "Maneuver"]
    },
{
    "name": "Improved Parry",
    "type": "Defensive",
    "source": "Homebrew/Expanded Rules (D&D 3.5)",
    "description": "You are adept at deflecting incoming attacks with your weapon.",
    "prerequisites": {"Base Attack Bonus": ">= 6", "Combat Expertise": True},
    "benefit": "You gain a +2 bonus to your attack roll when using a parry attempt to deflect an opponent's melee attack.",
    "limitations": "This feat requires you to forgo one of your attacks during a full-attack action to attempt a parry. Parrying is only effective against melee attacks and does not protect against ranged or magical attacks.",
    "tags": ["Combat", "Defensive"]
    },
{
    "name": "Improved Shield Bash",
    "type": "Combat Maneuver",
    "source": "Player's Handbook (D&D 3.5)",
    "description": (
        "You are skilled at using a shield as an offensive weapon without sacrificing your defensive capabilities. "
        "When you perform a shield bash, you retain the shield's bonus to your AC."
    ),
    "prerequisites": {
        "Shield Proficiency": True
    },
    "benefit": "Perform a shield bash and retain the shield's bonus to your AC.",
    "limitations": "This feat applies only to shield bash attacks.",
    "tags": ["Combat", "Maneuver", "Defensive"]
    },
{
    "name": "Shield Specialization",
    "type": "Defensive",
    "source": "Player's Handbook II (D&D 3.5)",
    "description": "You are especially skilled in using a particular type of shield.",
    "prerequisites": {"Proficiency with shields": True, "Base Attack Bonus": ">= 1"},
    "benefit": "Choose one type of shield (light, heavy, or tower). You gain a +1 bonus to your AC when using the selected shield.",
    "limitations": "The bonus applies only to the chosen shield type. You must already be proficient with the shield type to benefit from this feat.",
    "tags": ["Combat", "Defensive"]
    },
{
    "name": "Greater Shield Specialization",
    "type": "Defensive",
    "source": "Complete Warrior (D&D 3.5)",
    "description": (
        "You are exceptionally skilled at using a shield to defend yourself. "
        "Choose one type of shield (light, heavy, or tower). You gain an additional +2 bonus to your AC when using the selected type of shield."
    ),
    "prerequisites": {
        "Shield Proficiency": True,
        "Shield Specialization": True,
        "Base Attack Bonus": ">= 8"
    },
    "benefit": "Gain an additional +2 bonus to AC when using your selected type of shield.",
    "limitations": "This feat applies only to the chosen shield type and does not stack with other effects granting an AC bonus for shields.",
    "tags": ["Combat", "Defensive"]
    },
{
    "name": "Shield Master",
    "type": "Defensive",
    "source": "Pathfinder Core Rulebook (Adapted for D&D 3.5)",
    "description": (
        "You are highly skilled at using your shield both offensively and defensively. "
        "You do not suffer any penalties on attack rolls when using a shield in your off-hand. "
        "Additionally, you add your shield's enhancement bonus to attack and damage rolls when using it as a weapon."
    ),
    "prerequisites": {
        "Shield Proficiency": True,
        "Improved Shield Bash": True,
        "Two-Weapon Fighting": True,
        "Base Attack Bonus": ">= 11"
    },
    "benefit": "Eliminate attack roll penalties and add your shield's enhancement bonus to attack and damage rolls.",
    "limitations": "This feat applies only when using a shield as a weapon.",
    "tags": ["Combat", "Defensive", "Shield"]
    },
{
    "name": "Combat Expertise",
    "type": "Combat Maneuver",
    "source": "Player's Handbook (D&D 3.5)",
    "description": (
        "You can shift your focus from offense to defense during combat, improving your ability to avoid attacks. "
        "When you use the attack action or full-attack action in melee, you can take a penalty of up to -5 on your attack rolls and add the same number as a dodge bonus to your AC."
    ),
    "prerequisites": {
        "Int": ">= 13"
    },
    "benefit": "Trade attack roll penalties for an equivalent dodge bonus to AC.",
    "limitations": "This feat applies only when using melee attack actions or full-attack actions.",
    "tags": ["Combat", "Defensive", "Maneuver"]
    },
{
    "name": "Improved Combat Expertise",
    "type": "Combat Maneuver",
    "source": "Homebrew/Expanded Rules (D&D 3.5)",
    "description": (
        "You are exceptionally skilled at using your combat techniques to prioritize defense over offense. "
        "When using Combat Expertise, you may take a penalty of up to -10 on your attack rolls and add the same number as a dodge bonus to your AC."
    ),
    "prerequisites": {
        "Int": ">= 15",
        "Combat Expertise": True,
        "Base Attack Bonus": ">= 6"
    },
    "benefit": "Increase the maximum attack penalty for Combat Expertise to -10, gaining an equivalent dodge bonus to AC.",
    "limitations": "This feat applies only when using Combat Expertise during melee attack actions or full-attack actions.",
    "tags": ["Combat", "Defensive", "Maneuver"]
    },
{
    "name": "Improved Cover",
    "type": "Defensive",
    "source": "Homebrew/Expanded Rules (D&D 3.5)",
    "description": (
        "You are skilled at using cover to protect yourself during combat. "
        "When you have cover, increase the AC bonus it provides by +2 and the Reflex save bonus it provides by +1."
    ),
    "prerequisites": {
        "Dex": ">= 13",
        "Dodge": True
    },
    "benefit": "Gain an additional +2 AC bonus and +1 Reflex save bonus when using cover.",
    "limitations": "This feat applies only when you are benefiting from cover in combat.",
    "tags": ["Combat", "Defensive", "Tactical"]
    },
{
    "name": "Improved Damage Reduction",
    "type": "Defensive",
    "source": "Homebrew/Expanded Rules (D&D 3.5)",
    "description": (
        "Your resilience and training allow you to reduce damage more effectively. "
        "Increase your damage reduction (DR) by 2. For example, if you have DR 5/-, it becomes DR 7/-."
    ),
    "prerequisites": {
        "Damage Reduction": True,
        "Base Attack Bonus": ">= 8"
    },
    "benefit": "Increase your existing damage reduction by 2.",
    "limitations": "This feat applies only if you already have damage reduction.",
    "tags": ["Combat", "Defensive"]
    },
{
    "name": "Defensive Strike",
    "type": "Combat Maneuver",
    "source": "Complete Warrior (D&D 3.5)",
    "description": (
        "You are adept at turning defense into offense. "
        "If an opponent attacks you and misses while you are fighting defensively or using total defense, "
        "you gain a +4 bonus on your next attack roll against that opponent on your next turn."
    ),
    "prerequisites": {
        "Int": ">= 13",
        "Combat Expertise": True
    },
    "benefit": "Gain a +4 bonus on attack rolls against opponents who miss you while you are fighting defensively.",
    "limitations": "This bonus applies only to the next attack made against the opponent on your following turn.",
    "tags": ["Combat", "Defensive", "Tactical"]
    },
{
    "name": "Counterstrike",
    "type": "Combat Maneuver",
    "source": "Homebrew/Expanded Rules (D&D 3.5)",
    "description": (
        "You can take advantage of your opponent’s missed attacks. "
        "When an opponent makes a melee attack against you and misses, you can use an attack of opportunity to strike back immediately."
    ),
    "prerequisites": {
        "Dex": ">= 13",
        "Combat Reflexes": True,
        "Base Attack Bonus": ">= 6"
    },
    "benefit": "Make an attack of opportunity against opponents who miss you in melee.",
    "limitations": "This ability can only be used once per missed attack and requires an available attack of opportunity.",
    "tags": ["Combat", "Defensive", "Maneuver"]
    },
{
    "name": "Blind-Fight",
    "type": "Defensive",
    "source": "Player's Handbook (D&D 3.5)",
    "description": "You are skilled at fighting opponents you cannot see.",
    "prerequisites": {},
    "benefit": "In melee, every time you miss because of concealment, you can reroll your miss chance once to see if you actually hit. An invisible attacker gets no advantages related to hitting you in melee. You can move at full speed while blinded.",
    "limitations": "Does not remove the miss chance for ranged attacks against concealed targets.",
    "tags": ["Combat", "Defensive"]
    },
{
    "name": "Improved Blind-Fight",
    "type": "Combat Maneuver",
    "source": "Homebrew/Expanded Rules (D&D 3.5)",
    "description": (
        "Your heightened awareness and training allow you to fight effectively against unseen foes. "
        "You no longer suffer a miss chance when attacking opponents with total concealment, "
        "and you gain a +4 bonus on all opposed Perception checks to detect hidden or invisible creatures."
    ),
    "prerequisites": {
        "Blind-Fight": True,
        "Base Attack Bonus": ">= 6"
    },
    "benefit": "Eliminate the miss chance for attacking opponents with total concealment and gain a +4 bonus on Perception checks to detect hidden creatures.",
    "limitations": "This feat does not allow you to attack creatures you are unaware of, and it does not apply to effects such as blur or displacement.",
    "tags": ["Combat", "Defensive", "Tactical"]
    },
{
    "name": "Combat Awareness",
    "type": "Combat Maneuver",
    "source": "Complete Warrior (D&D 3.5)",
    "description": (
        "You gain heightened situational awareness in combat, allowing you to anticipate your opponent’s actions. "
        "As a swift action, you can make a Sense Motive check opposed by your opponent’s Bluff check. "
        "If successful, you learn your opponent's current hit points and any ongoing conditions affecting them."
    ),
    "prerequisites": {
        "Combat Reflexes": True,
        "Base Attack Bonus": ">= 6",
        "Wis": ">= 13"
    },
    "benefit": "Gain insight into an opponent's status during combat by succeeding on a Sense Motive check.",
    "limitations": "This feat requires a swift action to use and applies only to opponents you can see.",
    "tags": ["Combat", "Awareness", "Maneuver"]
    },
{
    "name": "Combat Stability",
    "type": "Defensive",
    "source": "Homebrew/Expanded Rules (D&D 3.5)",
    "description": (
        "Your training and focus in combat allow you to maintain your stance and composure, even when under pressure. "
        "While in combat, you gain resistance to being knocked prone or otherwise losing your footing."
    ),
    "prerequisites": {
        "Con": ">= 13",
        "Base Attack Bonus": ">= 3"
    },
    "benefit": "You gain advantage on saving throws to avoid being knocked prone or otherwise destabilized in combat.",
    "limitations": "This feat only applies to situations that would cause you to be knocked prone, such as certain combat maneuvers or effects that force you to lose your footing.",
    "tags": ["Combat", "Defensive"]
    },
{
    "name": "Improved Counterspell",
    "type": "Defensive",
    "source": "Player's Handbook (D&D 3.5)",
    "description": (
        "You have honed your ability to counter magic, making you even more effective at disrupting enemy spellcasting. "
        "When you successfully counter a spell, you may immediately cast the same spell back at the caster, provided you have it prepared."
    ),
    "prerequisites": {
        "Counterspell": True,
        "Int": ">= 15",
        "Base Attack Bonus": ">= 5"
    },
    "benefit": "When you successfully counter a spell, you may immediately cast that spell at the original caster, if it is on your spell list and you have it prepared.",
    "limitations": "This feat can only be used with spells that are on your spell list and require you to have them prepared at the time of countering.",
    "tags": ["Magic", "Defensive", "Spellcasting"]
    },
{
    "name": "Uncanny Dodge",
    "type": "Defensive",
    "source": "Player's Handbook (D&D 3.5)",
    "description": (
        "You are able to react to danger before your senses can fully process it, allowing you to avoid some attacks that would normally hit you. "
        "You retain your Dexterity bonus to Armor Class (AC) even if you are caught flat-footed or struck by an invisible attacker."
    ),
    "prerequisites": {
        "Dex": ">= 13",
        "Base Attack Bonus": ">= 4"
    },
    "benefit": "You can retain your Dexterity modifier to AC even when flat-footed or against attacks from invisible creatures.",
    "limitations": "This feat does not apply to situations where you are otherwise unable to react, such as being stunned or held. It also does not apply against attacks made by creatures with total concealment.",
    "tags": ["Combat", "Defensive"]
    },
{
    "name": "Improved Uncanny Dodge",
    "type": "Defensive",
    "source": "Player's Handbook (D&D 3.5)",
    "description": (
        "Your ability to avoid being caught off guard is further refined, allowing you to maintain your defense even in more dangerous situations. "
        "You cannot be flanked by creatures of your level or lower, making it harder for enemies to gain an advantage in combat."
    ),
    "prerequisites": {
        "Uncanny Dodge": True,
        "Base Attack Bonus": ">= 8"
    },
    "benefit": "You cannot be flanked by opponents of your level or lower. This makes it more difficult for enemies to gain combat advantage by positioning themselves to attack from the sides or rear.",
    "limitations": "This feat does not protect you from attacks made by creatures who are higher level or from magical effects that bypass flanking rules.",
    "tags": ["Combat", "Defensive"]
    },
{
    "name": "Evasion",
    "type": "Defensive",
    "source": "Player's Handbook (D&D 3.5)",
    "description": (
        "You are able to avoid the full effects of certain attacks that would otherwise cause you harm. "
        "When you succeed on a Reflex saving throw to avoid damage, you take no damage instead of half damage."
    ),
    "prerequisites": {
        "Dex": ">= 13",
        "Base Attack Bonus": ">= 3"
    },
    "benefit": "If you succeed on a Reflex saving throw to avoid damage, you take no damage instead of half damage.",
    "limitations": "This feat only applies to Reflex saving throws that would normally allow you to avoid or reduce damage, such as from a fireball or similar area-of-effect spell.",
    "tags": ["Combat", "Defensive"]
    },
{
    "name": "Damage Reduction",
    "type": "Defensive",
    "source": "Player's Handbook (D&D 3.5)",
    "description": (
        "Your physical resilience allows you to shrug off some of the damage from attacks. "
        "You reduce the damage dealt to you by a specific amount, making you more durable in combat."
    ),
    "prerequisites": {
        "Con": ">= 13",
        "Base Attack Bonus": ">= 5"
    },
    "benefit": "You reduce all damage dealt to you by a specific amount, typically denoted as DR X/-. For example, DR 5/- would reduce all incoming damage by 5 points, regardless of the source.",
    "limitations": "This feat only applies to damage from physical attacks. It does not reduce damage from energy sources (e.g., fire, cold, electricity) or magical effects unless specified otherwise.",
    "tags": ["Combat", "Defensive"]
},
    {
    "name": "Close-Quarters Combat",
    "type": "Defensive",
    "source": "Sword and Fist (D&D 3.5)",
    "description": "You are adept at resisting grappling attempts.",
    "prerequisites": {"Base Attack Bonus": ">= 3"},
    "benefit": "You can make an attack of opportunity against an opponent who attempts to grapple you, even if the opponent has the Improved Grapple feat or similar ability. If the attack of opportunity deals damage, the grapple attempt fails.",
    "limitations": "This does not prevent grappling attempts from succeeding after the attack of opportunity is resolved.",
    "tags": ["Combat", "Defensive"]
    },
#------------------------------------weapon combat feats-----------------------------------




{
    "name": "Weapon Focus",
    "type": "Weapon-Specific",
    "source": "Player's Handbook (D&D 3.5)",
    "description": "Choose one type of weapon. You are especially skilled with that weapon.",
    "prerequisites": {"Proficiency with weapon": True, "Base Attack Bonus": ">= 1"},
    "benefit": "You gain a +1 bonus on all attack rolls made with the selected weapon.",
    "limitations": "Applies only to the chosen weapon type.",
    "tags": ["Combat", "Weapon-Specific"]
    },
{
    "name": "Weapon Specialization",
    "type": "Weapon-Specific",
    "source": "Player's Handbook (D&D 3.5)",
    "description": "Choose one type of weapon for which you have already selected Weapon Focus. You deal extra damage with that weapon.",
    "prerequisites": {"Fighter level": ">= 4", "Weapon Focus": True},
    "benefit": "You gain a +2 bonus on all damage rolls made with the selected weapon.",
    "limitations": "Applies only to the chosen weapon type and requires Fighter level 4 or higher.",
    "tags": ["Combat", "Weapon-Specific"]
    },
{
    "name": "Greater Weapon Focus",
    "type": "Weapon-Specific",
    "source": "Player's Handbook (D&D 3.5)",
    "description": "Choose one type of weapon for which you have already selected Weapon Focus. You are extraordinarily skilled with that weapon.",
    "prerequisites": {"Fighter level": ">= 8", "Weapon Focus": True},
    "benefit": "You gain an additional +1 bonus on all attack rolls made with the selected weapon.",
    "limitations": "Applies only to the chosen weapon type and requires Fighter level 8 or higher.",
    "tags": ["Combat", "Weapon-Specific"]
    },
{
    "name": "Greater Weapon Specialization",
    "type": "Weapon-Specific",
    "source": "Player's Handbook (D&D 3.5)",
    "description": "Choose one type of weapon for which you have already selected Weapon Specialization. You deal even more damage with that weapon.",
    "prerequisites": {"Fighter level": ">= 12", "Weapon Specialization": True},
    "benefit": "You gain an additional +2 bonus on all damage rolls made with the selected weapon.",
    "limitations": "Applies only to the chosen weapon type and requires Fighter level 12 or higher.",
    "tags": ["Combat", "Weapon-Specific"]
    },
{
    "name": "Improved Critical",
    "type": "Weapon-Specific",
    "source": "Player's Handbook (D&D 3.5)",
    "description": "You know how to strike at your opponent's weak points more effectively with a specific weapon.",
    "prerequisites": {"Proficiency with weapon": True, "Base Attack Bonus": ">= 8"},
    "benefit": "When using the selected weapon, your threat range is doubled. For example, a longsword normally threatens a critical hit on a 19–20. With this feat, it threatens a critical hit on a 17–20.",
    "limitations": "This effect doesn’t stack with any other effect that expands the threat range of a weapon (such as the keen weapon property). You must choose a specific weapon when selecting this feat.",
    "tags": ["Combat", "Weapon-Specific"]
    },
{
    "name": "Weapon Finesse",
    "type": "Combat",
    "source": "Player's Handbook (D&D 3.5)",
    "description": "You are skilled at using agility rather than brute strength to hit with light weapons.",
    "prerequisites": {"Base Attack Bonus": ">= 1"},
    "benefit": "With a light weapon (and certain others, such as a rapier or spiked chain), you may use your Dexterity modifier instead of your Strength modifier on attack rolls.",
    "limitations": "Applies only to attack rolls, not damage rolls. This feat does not apply to weapons that are not light or specified exceptions like rapiers.",
    "tags": ["Combat", "Melee"]
    },
{
    "name": "Exotic Weapon Proficiency",
    "type": "Weapon-Specific",
    "source": "Player's Handbook (D&D 3.5)",
    "description": "You are proficient with a specific exotic weapon.",
    "prerequisites": {"Base Attack Bonus": ">= 1"},
    "benefit": "You make attack rolls with the selected exotic weapon normally. Without this feat, you take a -4 penalty on attack rolls with the weapon.",
    "limitations": "You must choose one exotic weapon to become proficient with. You can take this feat multiple times, each time applying to a different exotic weapon.",
    "tags": ["Combat", "Weapon-Specific"]
    },
{
    "name": "Improved Weapon Proficiency",
    "type": "Combat",
    "source": "Homebrew/Expanded Rules (D&D 3.5)",
    "description": (
        "Your skill with weapons allows you to use them more effectively in combat. "
        "You gain a bonus to your attack rolls with a specific weapon group or category, allowing you to hit more reliably in battle."
    ),
    "prerequisites": {
        "Weapon Proficiency": True,
        "Base Attack Bonus": ">= 5"
    },
    "benefit": "You gain a +1 bonus to attack rolls made with a specific weapon group or category, such as martial weapons, exotic weapons, or ranged weapons.",
    "limitations": "This feat only applies to weapons with which you are proficient, and the bonus only applies to attack rolls, not damage or other combat checks.",
    "tags": ["Combat", "Weapon", "Proficiency"]
    },
{
    "name": "Weapon Proficiency (Specific Weapon)",
    "type": "Combat",
    "source": "Player's Handbook (D&D 3.5)",
    "description": (
        "You gain proficiency with a specific weapon, allowing you to use it effectively in combat. "
        "With this feat, you can use a particular weapon without incurring the normal penalties for using an unfamiliar weapon."
    ),
    "prerequisites": {},
    "benefit": "You become proficient with a specific weapon, such as a longsword, greataxe, or crossbow, enabling you to use it without suffering attack penalties.",
    "limitations": "This feat applies only to a specific weapon of your choice, and you cannot use it to gain proficiency with weapon types you are already proficient with. You must select a new weapon each time you take this feat.",
    "tags": ["Combat", "Weapon", "Proficiency"]
    },
{
    "name": "Weapon Training",
    "type": "Combat",
    "source": "Homebrew/Expanded Rules (D&D 3.5)",
    "description": (
        "Your extensive training with a particular weapon type or category allows you to wield it with greater efficiency. "
        "You gain a bonus to attack rolls and damage rolls when using weapons from a specific group, such as light weapons, heavy weapons, or ranged weapons."
    ),
    "prerequisites": {
        "Base Attack Bonus": ">= 5"
    },
    "benefit": "You gain a +1 bonus to attack rolls and damage rolls when using weapons from a specific weapon group or category, such as swords, axes, or bows.",
    "limitations": "This feat applies only to weapons from the specified category, and the bonus does not stack with other proficiency bonuses for the same weapon type.",
    "tags": ["Combat", "Weapon", "Training"]
    },
{
    "name": "Improved Weapon Training",
    "type": "Combat",
    "source": "Homebrew/Expanded Rules (D&D 3.5)",
    "description": (
        "Your mastery of weapon combat has reached a new level, allowing you to deal even more devastating blows with your chosen weapons. "
        "You gain a greater bonus to attack and damage rolls with weapons from a specific group, making you even more effective in battle."
    ),
    "prerequisites": {
        "Weapon Training": True,
        "Base Attack Bonus": ">= 10"
    },
    "benefit": "You gain an additional +1 bonus to attack rolls and damage rolls when using weapons from the same weapon group or category chosen with the Weapon Training feat, increasing the total bonus to +2.",
    "limitations": "This feat applies only to weapons from the specified category in your Weapon Training feat, and the bonus does not stack with other similar bonuses.",
    "tags": ["Combat", "Weapon", "Training"]
    },
{
    "name": "Weapon Mastery",
    "type": "Combat",
    "source": "Homebrew/Expanded Rules (D&D 3.5)",
    "description": (
        "Your expertise with a specific weapon or weapon group is unparalleled, allowing you to deal devastating blows in combat. "
        "You gain an additional bonus to attack rolls and damage rolls, and your mastery grants you special benefits when using your chosen weapon."
    ),
    "prerequisites": {
        "Improved Weapon Training": True,
        "Base Attack Bonus": ">= 15"
    },
    "benefit": (
        "You gain a +2 bonus to attack rolls and damage rolls when using a weapon from the weapon group you have trained in. "
        "Additionally, once per turn, when you hit with an attack, you can choose to deal an extra 2d6 damage."
    ),
    "limitations": "This feat applies only to the weapon or weapon group chosen with the Weapon Training and Improved Weapon Training feats. The bonus damage from this feat can only be used once per turn, even if you make multiple attacks.",
    "tags": ["Combat", "Weapon", "Mastery"]
    },
{
    "name": "Greater Weapon Mastery",
    "type": "Weapon-Specific",
    "source": "Homebrew/Expanded Rules (D&D 3.5)",
    "description": (
        "Your exceptional skill with a specific weapon allows you to strike with greater precision and power. "
        "You gain bonuses to attack rolls, damage rolls, and critical threat range, making your strikes more effective."
    ),
    "prerequisites": {
        "Base Attack Bonus": ">= 8",
        "Weapon Focus": True,
        "Weapon Specialization": True,
        "Proficiency with weapon": True
    },
    "benefit": (
        "When using the selected weapon, you gain an additional +1 bonus on attack rolls and +2 bonus on damage rolls. "
        "Your critical threat range with the weapon increases by 1 (this stacks with Improved Critical or keen). "
        "Additionally, on a critical hit, you roll an extra die of the weapon's damage."
    ),
    "limitations": (
        "Applies only to the selected weapon. The critical threat range increase does not stack with effects that do not explicitly stack, "
        "such as doubling effects from the keen property."
    ),
    "tags": ["Combat", "Weapon-Specific"]
    },
{
    "name": "Double Weapon Fighting",
    "type": "Combat",
    "source": "Homebrew/Expanded Rules (D&D 3.5)",
    "description": (
        "You are skilled in fighting with double weapons, such as the quarterstaff or two-bladed sword. "
        "Your training allows you to effectively use both ends of the weapon in combat."
    ),
    "prerequisites": {
        "Dex": ">= 15",
        "Two-Weapon Fighting": True,
        "Proficiency with double weapon": True
    },
    "benefit": (
        "When wielding a double weapon, you treat it as if you were fighting with two weapons for the purposes of attack penalties "
        "and off-hand attacks. You can make one extra attack with the off-hand end of the double weapon at your highest attack bonus, "
        "taking penalties as if using Two-Weapon Fighting."
    ),
    "limitations": (
        "The penalties for fighting with two weapons apply to all attacks made with a double weapon unless you have the appropriate feats or abilities to reduce them. "
        "The off-hand end of the weapon must be light unless specified otherwise in the weapon's description."
    ),
    "tags": ["Combat", "Two-Weapon Fighting"]
    },
{
    "name": "Thrown Weapon Focus",
    "type": "Weapon-Specific",
    "source": "Homebrew/Expanded Rules (D&D 3.5)",
    "description": (
        "Your precision with thrown weapons allows you to strike with greater accuracy. "
        "You are especially skilled at using weapons designed for throwing, such as daggers, javelins, or shuriken."
    ),
    "prerequisites": {
        "Base Attack Bonus": ">= 1",
        "Proficiency with thrown weapon": True
    },
    "benefit": (
        "You gain a +1 bonus on all attack rolls made with thrown weapons. This bonus applies to all weapons with the 'thrown' property, "
        "whether they are designed for throwing (e.g., darts, javelins) or improvised as thrown weapons."
    ),
    "limitations": (
        "This feat does not apply to weapons used as melee weapons or to ranged weapons that do not have the thrown property. "
        "It only applies to attacks made within the weapon's normal range increment."
    ),
    "tags": ["Combat", "Ranged", "Weapon-Specific"]
    },
{
    "name": "Improved Thrown Weapon Proficiency",
    "type": "Combat",
    "source": "Homebrew/Expanded Rules (D&D 3.5)",
    "description": (
        "Your expertise with thrown weapons allows you to use them with greater efficiency. "
        "You can throw weapons with increased accuracy at greater distances and with reduced penalties."
    ),
    "prerequisites": {
        "Base Attack Bonus": ">= 4",
        "Thrown Weapon Focus": True,
        "Proficiency with thrown weapon": True
    },
    "benefit": (
        "You can throw weapons at their maximum range increments with only a -1 penalty per increment instead of the usual -2 penalty. "
        "Additionally, when using weapons with the thrown property, you gain a +1 bonus on damage rolls."
    ),
    "limitations": (
        "This feat only applies to weapons with the thrown property and does not affect ranged weapons that do not have this property (e.g., bows, crossbows). "
        "Improvised weapons are not affected unless they are explicitly treated as thrown weapons."
    ),
    "tags": ["Combat", "Ranged", "Weapon-Specific"]
    },
{
    "name": "Weapon Versatility",
    "type": "Combat",
    "source": "Homebrew/Expanded Rules (D&D 3.5)",
    "description": (
        "Your adaptability with weapons allows you to use a weapon in unconventional ways, "
        "switching between different damage types or combat styles as the situation demands."
    ),
    "prerequisites": {
        "Base Attack Bonus": ">= 5",
        "Weapon Focus": True
    },
    "benefit": (
        "When using a weapon for which you have the Weapon Focus feat, you can change the weapon's damage type (bludgeoning, piercing, or slashing) "
        "to a different type as a free action, as long as it makes sense for the weapon's design (e.g., a sword can deal slashing or piercing damage). "
        "Additionally, you can treat the weapon as either one-handed or two-handed for the purposes of Power Attack and other similar feats."
    ),
    "limitations": (
        "This feat only applies to weapons for which you have Weapon Focus. Improvised weapons or weapons with rigid damage types (e.g., crossbows) are not eligible. "
        "The weapon's versatility must align with its structure and functionality (e.g., a longsword can deal slashing or piercing damage, but not bludgeoning)."
    ),
    "tags": ["Combat", "Weapon", "Versatility"]
    },
{
    "name": "Weapon Adaptability",
    "type": "Combat",
    "source": "Homebrew/Expanded Rules (D&D 3.5)",
    "description": (
        "Your skill with weapons allows you to adjust your fighting style on the fly, adapting to new challenges with ease. "
        "This versatility makes you exceptionally dangerous in combat."
    ),
    "prerequisites": {
        "Base Attack Bonus": ">= 6",
        "Weapon Focus": True,
        "Proficiency with weapon": True
    },
    "benefit": (
        "When wielding a weapon for which you have Weapon Focus, you can change your combat style as a swift action. "
        "You may choose one of the following benefits for 1 round:\n"
        "- Gain a +2 bonus to attack rolls.\n"
        "- Gain a +2 bonus to damage rolls.\n"
        "- Gain a +1 bonus to AC while using the weapon defensively."
    ),
    "limitations": (
        "This feat only applies to the selected weapon type for which you have Weapon Focus. "
        "The chosen benefit lasts only for 1 round and must be selected again at the start of your next turn."
    ),
    "tags": ["Combat", "Weapon", "Adaptability"]
    },
{
    "name": "Weapon Defense",
    "type": "Combat",
    "source": "Homebrew/Expanded Rules (D&D 3.5)",
    "description": (
        "You have trained to use your weapon not only for offense but also as a tool for defense. "
        "Your skill allows you to parry and deflect incoming attacks with greater efficiency."
    ),
    "prerequisites": {
        "Base Attack Bonus": ">= 4",
        "Weapon Focus": True,
        "Proficiency with weapon": True
    },
    "benefit": (
        "When wielding a weapon for which you have Weapon Focus, you gain a +1 shield bonus to AC. "
        "If you choose to fight defensively or use the total defense action, this bonus increases to +2."
    ),
    "limitations": (
        "This feat only applies to weapons for which you have Weapon Focus. "
        "The shield bonus does not stack with other shield bonuses (e.g., from an actual shield)."
    ),
    "tags": ["Combat", "Weapon", "Defensive"]
    },
{
    "name": "Improved Weapon Defense",
    "type": "Combat",
    "source": "Homebrew/Expanded Rules (D&D 3.5)",
    "description": (
        "Your mastery of defensive weapon techniques makes you exceptionally skilled at deflecting and parrying attacks. "
        "You can use your weapon to protect yourself more effectively in combat."
    ),
    "prerequisites": {
        "Base Attack Bonus": ">= 8",
        "Weapon Defense": True,
        "Weapon Focus": True,
        "Proficiency with weapon": True
    },
    "benefit": (
        "When wielding a weapon for which you have Weapon Focus, you gain a +2 shield bonus to AC. "
        "If you choose to fight defensively or use the total defense action, this bonus increases to +4."
    ),
    "limitations": (
        "This feat only applies to weapons for which you have Weapon Focus. "
        "The shield bonus does not stack with other shield bonuses (e.g., from an actual shield). "
        "You must be actively wielding the weapon to benefit from this feat."
    ),
    "tags": ["Combat", "Weapon", "Defensive"]
    },
{
    "name": "Versatile Weapon Training",
    "type": "Combat",
    "source": "Homebrew/Expanded Rules (D&D 3.5)",
    "description": (
        "Your extensive training allows you to master multiple weapon types and adapt your combat style to suit different situations. "
        "This versatility makes you proficient with a broader range of weaponry."
    ),
    "prerequisites": {
        "Base Attack Bonus": ">= 6",
        "Weapon Focus": True,
        "Proficiency with at least one weapon": True
    },
    "benefit": (
        "Choose one additional weapon group (e.g., swords, axes, bows) that you are not already proficient with. "
        "You gain proficiency with all weapons in the selected group. "
        "Additionally, you may apply any feat that requires Weapon Focus to all weapons within the selected group."
    ),
    "limitations": (
        "This feat does not grant Weapon Focus itself but allows you to apply existing Weapon Focus-related feats "
        "to other weapons within the same group. Weapon groups must be explicitly defined (e.g., in a supplemental rulebook or homebrew setting)."
    ),
    "tags": ["Combat", "Weapon", "Training"]
    },
{
    "name": "Greater Versatile Weapon Training",
    "type": "Combat",
    "source": "Homebrew/Expanded Rules (D&D 3.5)",
    "description": (
        "Your unparalleled expertise with a variety of weapons allows you to wield an even greater range of weapon types with precision and power. "
        "This mastery extends your combat versatility to its peak."
    ),
    "prerequisites": {
        "Base Attack Bonus": ">= 12",
        "Versatile Weapon Training": True,
        "Weapon Focus": True
    },
    "benefit": (
        "Choose one additional weapon group. You gain proficiency with all weapons in the selected group. "
        "You may also apply any feats that require Weapon Focus (e.g., Weapon Specialization, Greater Weapon Focus) to all weapons within the selected group. "
        "Additionally, you gain a +1 bonus to attack rolls and damage rolls with all weapons from the groups selected through this feat and Versatile Weapon Training."
    ),
    "limitations": (
        "This feat does not grant Weapon Focus itself but extends its benefits to additional weapon groups. "
        "The bonus to attack rolls and damage rolls applies only to weapons within the selected groups."
    ),
    "tags": ["Combat", "Weapon", "Training"]
    },
{
    "name": "Flexible Weapon Use",
    "type": "Combat",
    "source": "Homebrew/Expanded Rules (D&D 3.5)",
    "description": (
        "Your adaptability with weapons allows you to use them in unconventional and creative ways. "
        "This flexibility lets you overcome challenges in combat by altering how you wield your weapons."
    ),
    "prerequisites": {
        "Base Attack Bonus": ">= 4",
        "Weapon Focus": True,
        "Proficiency with weapon": True
    },
    "benefit": (
        "When wielding a weapon for which you have Weapon Focus, you can choose to alter its normal usage as a swift action. "
        "You may:\n"
        "- Use the weapon as if it were a different size category (e.g., treat a one-handed weapon as a light weapon for purposes of Two-Weapon Fighting penalties).\n"
        "- Use the weapon to deal an alternate type of damage (e.g., slashing, piercing, or bludgeoning) if feasible for the weapon's structure.\n"
        "- Gain a +1 bonus to attack rolls when using the weapon as an improvised tool in combat situations."
    ),
    "limitations": (
        "This feat only applies to weapons for which you have Weapon Focus. "
        "The flexibility options must be reasonable for the weapon's design (e.g., a longsword can deal slashing or piercing damage but not bludgeoning). "
        "The benefit for treating a weapon as a different size category does not apply to effects that directly require the weapon's true size."
    ),
    "tags": ["Combat", "Weapon", "Versatility"]
    },
{
    "name": "Polearm Training",
    "type": "Combat",
    "source": "Homebrew/Expanded Rules (D&D 3.5)",
    "description": (
        "You have trained extensively with polearms, mastering their unique reach and versatility in combat. "
        "This training allows you to use polearms more effectively to control the battlefield."
    ),
    "prerequisites": {
        "Base Attack Bonus": ">= 3",
        "Proficiency with polearms": True
    },
    "benefit": (
        "When wielding a polearm (e.g., glaive, halberd, or longspear), you gain the following benefits:\n"
        "- You can use the polearm to make attacks of opportunity against creatures that enter your threatened area, even if they take a 5-foot step.\n"
        "- You gain a +2 bonus on checks made to resist being disarmed while wielding a polearm.\n"
        "- When fighting defensively or using the total defense action, you gain an additional +1 shield bonus to AC."
    ),
    "limitations": (
        "These benefits apply only to weapons classified as polearms. Improvised weapons or weapons not specifically designed as polearms do not qualify. "
        "Attacks of opportunity still follow the usual restrictions and cannot bypass abilities like Mobility or other defensive features."
    ),
    "tags": ["Combat", "Weapon", "Polearm"]
    },
{
    "name": "Flail Training",
    "type": "Combat",
    "source": "Homebrew/Expanded Rules (D&D 3.5)",
    "description": (
        "Your expertise with flails allows you to use their unique properties to disrupt your enemies' defenses. "
        "You have mastered techniques to entangle weapons, bypass shields, and exploit openings in combat."
    ),
    "prerequisites": {
        "Base Attack Bonus": ">= 3",
        "Proficiency with flails": True
    },
    "benefit": (
        "When wielding a flail (e.g., light flail, heavy flail, dire flail), you gain the following benefits:\n"
        "- You can ignore the AC bonus granted by shields when attacking with a flail.\n"
        "- You gain a +2 bonus on trip attempts made with a flail.\n"
        "- When you successfully disarm an opponent, you may immediately make a free attack against that opponent using the flail."
    ),
    "limitations": (
        "These benefits apply only to weapons classified as flails. Improvised weapons or weapons not specifically designed as flails do not qualify. "
        "The free attack after a disarm is limited to a single attack and does not allow further effects such as a cleave."
    ),
    "tags": ["Combat", "Weapon", "Flail"]
    },
{
    "name": "Bow Specialization",
    "type": "Combat",
    "source": "Homebrew/Expanded Rules (D&D 3.5)",
    "description": (
        "Your extensive practice with bows allows you to deal greater damage with ranged attacks. "
        "You have honed your accuracy and power, making you a more lethal archer."
    ),
    "prerequisites": {
        "Base Attack Bonus": ">= 4",
        "Weapon Focus": True,
        "Proficiency with bows": True
    },
    "benefit": (
        "You gain a +2 bonus on damage rolls with all ranged attacks made using bows (e.g., shortbow, longbow, composite bows). "
        "This bonus stacks with other bonuses, such as those from magical enhancements or abilities like Point Blank Shot."
    ),
    "limitations": (
        "This feat only applies to attacks made with bows. It does not apply to crossbows or other ranged weapons. "
        "The bonus does not affect special abilities or effects that deal damage independently of the bow's damage roll."
    ),
    "tags": ["Combat", "Weapon", "Ranged", "Bow"]
    },
{
    "name": "Crossbow Specialization",
    "type": "Combat",
    "source": "Homebrew/Expanded Rules (D&D 3.5)",
    "description": (
        "Your expertise with crossbows allows you to deal increased damage with precise shots. "
        "You have trained extensively with crossbows, making you a more deadly marksman."
    ),
    "prerequisites": {
        "Base Attack Bonus": ">= 4",
        "Weapon Focus": True,
        "Proficiency with crossbows": True
    },
    "benefit": (
        "You gain a +2 bonus on damage rolls with all ranged attacks made using crossbows (e.g., light crossbow, heavy crossbow, hand crossbow). "
        "Additionally, you reduce the loading time for heavy crossbows, allowing you to reload as a move action instead of a full-round action."
    ),
    "limitations": (
        "This feat only applies to attacks made with crossbows. It does not apply to bows or other ranged weapons. "
        "The reduced reloading time does not stack with abilities or items that already reduce reloading time (e.g., Rapid Reload feat)."
    ),
    "tags": ["Combat", "Weapon", "Ranged", "Crossbow"]
    },
{
    "name": "Sword Specialization",
    "type": "Combat",
    "source": "Homebrew/Expanded Rules (D&D 3.5)",
    "description": (
        "Your mastery with swords allows you to strike with precision and force, dealing more damage in combat. "
        "You have refined your skills to maximize the effectiveness of your swordplay."
    ),
    "prerequisites": {
        "Base Attack Bonus": ">= 4",
        "Weapon Focus": True,
        "Proficiency with swords": True
    },
    "benefit": (
        "You gain a +2 bonus on all damage rolls made with swords (e.g., longsword, shortsword, greatsword, scimitar, rapier). "
        "Additionally, when wielding a sword in two hands, you deal an additional +1 damage due to improved leverage and technique."
    ),
    "limitations": (
        "This feat applies only to weapons classified as swords. Improvised weapons or weapons that do not fall under the 'sword' category do not qualify. "
        "The bonus damage when wielding the sword in two hands does not stack with other similar bonuses."
    ),
    "tags": ["Combat", "Weapon", "Melee", "Sword"]
    },
{
    "name": "Axe Mastery",
    "type": "Combat",
    "source": "Homebrew/Expanded Rules (D&D 3.5)",
    "description": (
        "Your expertise with axes allows you to deliver devastating blows with unparalleled precision and force. "
        "You are a master of using axes to cut through armor and defenses."
    ),
    "prerequisites": {
        "Base Attack Bonus": ">= 6",
        "Weapon Focus": True,
        "Weapon Specialization": True,
        "Proficiency with axes": True
    },
    "benefit": (
        "You gain a +2 bonus on attack rolls when confirming critical hits with axes (e.g., handaxe, battleaxe, greataxe). "
        "Additionally, when you score a critical hit with an axe, you deal an extra die of the weapon's damage."
    ),
    "limitations": (
        "This feat applies only to weapons classified as axes. Improvised weapons or weapons that do not fall under the 'axe' category do not qualify. "
        "The extra damage on critical hits does not stack with similar effects, such as the Vorpal property."
    ),
    "tags": ["Combat", "Weapon", "Melee", "Axe"]
    },
{
    "name": "Hammer Expertise",
    "type": "Combat",
    "source": "Homebrew/Expanded Rules (D&D 3.5)",
    "description": (
        "Your extensive training with hammers allows you to wield them with extraordinary precision and strength. "
        "You can use their weight and force to break through defenses and deal devastating blows."
    ),
    "prerequisites": {
        "Base Attack Bonus": ">= 4",
        "Weapon Focus": True,
        "Proficiency with hammers": True
    },
    "benefit": (
        "When wielding a hammer (e.g., warhammer, maul, light hammer), you gain the following benefits:\n"
        "- You deal an additional +2 damage when attacking creatures wearing heavy armor or with natural armor bonuses of +5 or higher.\n"
        "- You gain a +2 bonus on Strength checks to break objects (e.g., doors, walls) when using a hammer.\n"
        "- You can reroll a failed sunder attempt once per round when using a hammer and must take the second result."
    ),
    "limitations": (
        "These benefits apply only to weapons classified as hammers. Improvised weapons or weapons not specifically designed as hammers do not qualify. "
        "The damage bonus applies only to creatures with the specified armor or natural armor thresholds."
    ),
    "tags": ["Combat", "Weapon", "Melee", "Hammer"]
    },
{
    "name": "Spear Specialization",
    "type": "Combat",
    "source": "Homebrew/Expanded Rules (D&D 3.5)",
    "description": (
        "Your mastery with spears allows you to strike with precision and control, leveraging their reach and thrusting power. "
        "You are especially adept at using spears to deliver more effective attacks."
    ),
    "prerequisites": {
        "Base Attack Bonus": ">= 4",
        "Weapon Focus": True,
        "Proficiency with spears": True
    },
    "benefit": (
        "When wielding a spear (e.g., longspear, shortspear, trident), you gain the following benefits:\n"
        "- You deal an additional +2 damage on all attacks made with spears.\n"
        "- When using the Ready action to set a spear against a charge, you deal double damage (this stacks with the standard bonus for setting a spear against a charge).\n"
        "- You gain a +1 bonus to attack rolls when making attacks of opportunity with a spear."
    ),
    "limitations": (
        "These benefits apply only to weapons classified as spears. Improvised weapons or weapons not specifically designed as spears do not qualify. "
        "The bonus damage and special effects do not apply to thrown spear attacks."
    ),
    "tags": ["Combat", "Weapon", "Melee", "Spear"]
    },
{
    "name": "Scimitar Mastery",
    "type": "Combat",
    "source": "Homebrew/Expanded Rules (D&D 3.5)",
    "description": (
        "Your expertise with scimitars allows you to strike with unparalleled speed and precision. "
        "You are adept at exploiting their natural balance and curved blade to deliver deadly critical strikes."
    ),
    "prerequisites": {
        "Base Attack Bonus": ">= 6",
        "Weapon Focus": True,
        "Weapon Specialization": True,
        "Proficiency with scimitars": True
    },
    "benefit": (
        "When wielding a scimitar, you gain the following benefits:\n"
        "- You add +2 to attack rolls when confirming critical hits with a scimitar.\n"
        "- The critical multiplier for your scimitar increases to x3 (instead of the standard x2).\n"
        "- If you score a critical hit, you may immediately make a single additional attack at your highest attack bonus. "
        "This extra attack does not stack with similar effects, such as Cleave or other critical hit-triggered abilities."
    ),
    "limitations": (
        "These benefits apply only to scimitars. Improvised weapons or other curved blades that are not specifically scimitars do not qualify. "
        "The additional attack on a critical hit can only occur once per turn, regardless of how many critical hits are scored."
    ),
    "tags": ["Combat", "Weapon", "Melee", "Scimitar"]
    },
{
    "name": "Unarmed Weapon Training",
    "type": "Combat",
    "source": "Homebrew/Expanded Rules (D&D 3.5)",
    "description": (
        "Your expertise in unarmed combat allows you to turn your body into a formidable weapon. "
        "You have trained extensively in striking techniques, making your unarmed attacks more effective in combat."
    ),
    "prerequisites": {
        "Base Attack Bonus": ">= 3",
        "Improved Unarmed Strike": True
    },
    "benefit": (
        "Your unarmed strikes deal increased damage based on your Base Attack Bonus (BAB):\n"
        "- BAB +3 to +7: 1d6 damage (medium creature).\n"
        "- BAB +8 to +11: 1d8 damage (medium creature).\n"
        "- BAB +12 or higher: 1d10 damage (medium creature).\n"
        "Additionally, your unarmed strikes are treated as both magic and a specific material type (silver, cold iron, or adamantine) "
        "for the purposes of overcoming damage reduction (choose the material type when you take this feat)."
    ),
    "limitations": (
        "This feat applies only to unarmed strikes and does not extend to natural weapons or improvised melee attacks. "
        "The damage increase is based on your BAB and does not stack with other effects that increase unarmed strike damage (e.g., monk progression)."
    ),
    "tags": ["Combat", "Unarmed", "Melee"]
    },
#-----------------------------------------tactical combat feats-----------------------------------------




{
    "name": "Spring Attack",
    "type": "Tactical",
    "source": "Player's Handbook (D&D 3.5)",
    "description": "You can move both before and after you make a melee attack.",
    "prerequisites": {"Dex": ">= 13", "Dodge": True, "Mobility": True, "Base Attack Bonus": ">= 4"},
    "benefit": "When using the attack action with a melee weapon, you can move both before and after the attack, provided that your total distance moved is not greater than your speed.",
    "limitations": "You cannot use this feat if you are wearing heavy armor or carrying a heavy load.",
    "tags": ["Combat", "Melee", "Tactical"]
    },
{
    "name": "Whirlwind Attack",
    "type": "Tactical",
    "source": "Player's Handbook (D&D 3.5)",
    "description": "You can strike all adjacent foes in one sweeping attack.",
    "prerequisites": {"Dex": ">= 13", "Int": ">= 13", "Combat Expertise": True, "Dodge": True, "Mobility": True, "Spring Attack": True, "Base Attack Bonus": ">= 4"},
    "benefit": "When you use the full-attack action, you can give up your regular attacks to instead make one melee attack at your full base attack bonus against each opponent within reach.",
    "limitations": "Requires the full-attack action and affects only creatures within reach.",
    "tags": ["Combat", "Melee", "Tactical"]
    },
{
    "name": "Improved Feint",
    "type": "Tactical",
    "source": "Player's Handbook (D&D 3.5)",
    "description": "You are skilled at misleading your opponent in combat.",
    "prerequisites": {"Int": ">= 13", "Combat Expertise": True},
    "benefit": "You can make a Bluff check to feint in combat as a move action instead of as a standard action.",
    "limitations": "Only applicable during combat and requires a successful Bluff check.",
    "tags": ["Combat", "Tactical"]
    },
{
    "name": "Bull Rush",
    "type": "Combat",
    "source": "Player's Handbook (D&D 3.5)",
    "description": (
        "You are skilled at charging into your opponents with brute force, pushing them back or knocking them off balance."
    ),
    "prerequisites": {
        "Strength": ">= 13",
        "Base Attack Bonus": ">= 1"
    },
    "benefit": (
        "You gain a +4 bonus on Strength checks made to perform a bull rush. "
        "Additionally, if you succeed in pushing an opponent back, you may choose to follow them into the square they vacated, "
        "as long as it is not impassable terrain or otherwise inaccessible."
    ),
    "limitations": (
        "The bonus applies only to bull rush attempts. You must declare that you are attempting a bull rush during a charge, "
        "and it provokes attacks of opportunity unless you have other abilities that negate this (e.g., Improved Bull Rush)."
    ),
    "tags": ["Combat", "Melee", "Strength"]
    },
{
    "name": "Tactical Advantage",
    "type": "Combat",
    "source": "Homebrew/Expanded Rules (D&D 3.5)",
    "description": (
        "Your ability to read the battlefield and adapt to the flow of combat allows you to exploit opportunities others may miss. "
        "You excel at gaining a superior position and turning small advantages into decisive victories."
    ),
    "prerequisites": {
        "Base Attack Bonus": ">= 5",
        "Intelligence": ">= 13",
        "Combat Expertise": True
    },
    "benefit": (
        "You gain the following tactical benefits:\n"
        "- **Flanking Advantage**: When flanking an opponent, you gain an additional +2 bonus on attack rolls (total +4).\n"
        "- **Mobility Advantage**: When fighting defensively or using the total defense action, you gain an additional +2 dodge bonus to AC.\n"
        "- **Positional Mastery**: Once per round, when you successfully hit an opponent, you may take a free 5-foot step, even if you have already moved this round."
    ),
    "limitations": (
        "These benefits apply only when the conditions are met (e.g., flanking, fighting defensively). "
        "The free 5-foot step cannot be used in terrain that restricts movement or when your movement speed is reduced (e.g., by heavy armor or a condition like entangled)."
    ),
    "tags": ["Combat", "Tactical", "Positional"]
    },
{
    "name": "Overwhelming Assault",
    "type": "Tactical",
    "source": "Player's Handbook II (D&D 3.5)",
    "description": "You gain a combat advantage when your foes cannot retaliate effectively.",
    "prerequisites": {"Base Attack Bonus": ">= 6", "Power Attack": True},
    "benefit": "If you start your turn adjacent to an opponent and do not move during your turn, you gain a +4 bonus on melee attack rolls against that opponent until the start of your next turn.",
    "limitations": "This feat only applies if you remain adjacent to your opponent and do not move during your turn.",
    "tags": ["Combat", "Tactical"]
    },
{
    "name": "Flanking Maneuver",
    "type": "Combat",
    "source": "Homebrew/Expanded Rules (D&D 3.5)",
    "description": (
        "Your skill in coordinating with allies allows you to exploit openings in your enemies' defenses. "
        "You are especially adept at using flanking positions to maximize your effectiveness in combat."
    ),
    "prerequisites": {
        "Base Attack Bonus": ">= 3",
        "Dexterity": ">= 13",
        "Combat Reflexes": True
    },
    "benefit": (
        "You gain the following benefits when flanking an opponent:\n"
        "- You deal an additional 1d6 precision damage on successful attacks.\n"
        "- Your flanking bonus to attack rolls increases to +3 (instead of the standard +2).\n"
        "- When an ally threatens the same opponent you are flanking, they also gain the increased flanking bonus (+3)."
    ),
    "limitations": (
        "The additional precision damage applies only to creatures vulnerable to critical hits. "
        "This feat does not stack with similar effects that increase flanking bonuses or precision damage, such as sneak attack."
    ),
    "tags": ["Combat", "Tactical", "Flanking"]
    },
{
    "name": "Improved Tactical Maneuvering",
    "type": "Combat",
    "source": "Homebrew/Expanded Rules (D&D 3.5)",
    "description": (
        "Your refined battlefield awareness and coordination allow you to maneuver and position yourself and your allies with unmatched precision. "
        "You excel at controlling combat flow and exploiting openings created by movement."
    ),
    "prerequisites": {
        "Base Attack Bonus": ">= 6",
        "Intelligence": ">= 13",
        "Tactical Advantage": True
    },
    "benefit": (
        "You gain the following tactical benefits:\n"
        "- **Coordinated Movement**: Once per round, as a free action, you may grant an adjacent ally a 5-foot step, even if it is not their turn. "
        "This step does not provoke attacks of opportunity.\n"
        "- **Enhanced Positional Mastery**: When you take a 5-foot step, you may simultaneously grant yourself a +1 bonus to AC or attack rolls until the start of your next turn.\n"
        "- **Opportunistic Control**: When an enemy moves within your threatened area, you may make an attack of opportunity and immediately reposition yourself by taking a free 5-foot step."
    ),
    "limitations": (
        "The granted 5-foot step to an ally cannot be used in terrain that restricts movement or when the ally is immobilized. "
        "Enhanced Positional Mastery bonuses do not stack with themselves if triggered multiple times in a single round."
    ),
    "tags": ["Combat", "Tactical", "Positioning"]
    },
{
    "name": "Sweeping Strike",
    "type": "Combat",
    "source": "Homebrew/Expanded Rules (D&D 3.5)",
    "description": (
        "Your combat prowess allows you to strike multiple foes with a single, powerful swing. "
        "You use your weapon's momentum to attack multiple targets in close proximity."
    ),
    "prerequisites": {
        "Base Attack Bonus": ">= 6",
        "Strength": ">= 13",
        "Cleave": True
    },
    "benefit": (
        "When making a melee attack, you may choose to perform a sweeping strike. "
        "If your attack hits, you may make a second attack roll using the same attack bonus against an adjacent enemy within reach. "
        "This second attack deals half damage but uses the same roll to confirm a critical hit if applicable."
    ),
    "limitations": (
        "A sweeping strike cannot be used with a weapon that cannot logically target multiple creatures with one swing (e.g., piercing-only weapons like a spear). "
        "The second attack must target a creature adjacent to the original target and within your reach."
    ),
    "tags": ["Combat", "Melee", "Area Attack"]
    },
{
    "name": "Improved Flanking",
    "type": "Combat",
    "source": "Homebrew/Expanded Rules (D&D 3.5)",
    "description": (
        "Your mastery of combat positioning allows you to take full advantage of flanking an opponent. "
        "You and your allies are more effective at exploiting openings created during flanking."
    ),
    "prerequisites": {
        "Base Attack Bonus": ">= 4",
        "Dexterity": ">= 13",
        "Combat Expertise": True
    },
    "benefit": (
        "When flanking an opponent, you gain an additional +2 bonus on attack rolls (total +4). "
        "Additionally, allies flanking the same opponent with you also gain an additional +1 bonus to their attack rolls. "
        "You also deal an extra 1d6 precision damage to flanked opponents."
    ),
    "limitations": (
        "The extra precision damage applies only to creatures that are vulnerable to critical hits. "
        "This feat does not stack with other effects that increase flanking bonuses or precision damage, such as sneak attack."
    ),
    "tags": ["Combat", "Tactical", "Flanking"]
    },
{
    "name": "Giant Slayer",
    "type": "Combat",
    "source": "Homebrew/Expanded Rules (D&D 3.5)",
    "description": (
        "You are trained to fight against much larger opponents, exploiting their size and slower movements. "
        "You are especially effective at dealing with giants and other creatures of similar size."
    ),
    "prerequisites": {
        "Base Attack Bonus": ">= 5",
        "Strength": ">= 13",
        "Combat Reflexes": True
    },
    "benefit": (
        "You gain the following benefits when fighting creatures larger than yourself:\n"
        "- You deal an additional 1d6 damage on all melee attacks against creatures at least two size categories larger than you.\n"
        "- You gain a +2 dodge bonus to AC against attacks made by creatures of Large size or larger.\n"
        "- When such a creature provokes an attack of opportunity, you gain a +2 bonus on the attack roll for that opportunity."
    ),
    "limitations": (
        "These benefits only apply to creatures that are at least two size categories larger than you. "
        "The bonus damage applies only to melee attacks, not ranged or magical attacks."
    ),
    "tags": ["Combat", "Melee", "Anti-Giant"]
    },
{
    "name": "Improved Tactical Strike",
    "type": "Combat",
    "source": "Homebrew/Expanded Rules (D&D 3.5)",
    "description": (
        "Your advanced combat tactics allow you to strike in a way that disrupts your enemies and opens them to further attacks. "
        "You can coordinate your strikes with your allies for maximum impact."
    ),
    "prerequisites": {
        "Base Attack Bonus": ">= 8",
        "Intelligence": ">= 13",
        "Tactical Advantage": True
    },
    "benefit": (
        "When you make a successful melee attack, you may choose to activate one of the following tactical effects:\n"
        "- **Disrupting Strike**: The target takes a -2 penalty to AC until the start of your next turn.\n"
        "- **Exploiting Strike**: The next attack made against the target by one of your allies gains a +4 bonus to the attack roll.\n"
        "- **Positioning Strike**: You may force the target to move 5 feet in a direction of your choice, provided the space is not occupied or impassable."
    ),
    "limitations": (
        "Each tactical effect can only be used once per round, and only one effect may be applied per successful attack. "
        "The target must be susceptible to the effects (e.g., immune to forced movement or penalties if they have specific resistances or immunities)."
    ),
    "tags": ["Combat", "Tactical", "Melee"]
},
#-------------------------------utility feats---------------------------------
{
    "name": "Leadership",
    "type": "Utility",
    "source": "Player's Handbook (D&D 3.5)",
    "description": "You attract followers and a loyal cohort to assist you.",
    "prerequisites": {"Character Level": ">= 6"},
    "benefit": "This feat allows you to attract loyal companions and devoted followers. The number of followers and the level of your cohort depend on your Leadership score, which is equal to your character level + your Charisma modifier + any bonuses or penalties based on your actions or reputation.",
    "limitations": "Followers gained through this feat are NPCs controlled by the GM. A cohort is a separate NPC character that adventurers alongside you but is not an equal party member.",
    "tags": ["Utility"]
}
]