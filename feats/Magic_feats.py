#---------------------------------------Metamagic Feats
Magic_feats_library = [
{
      "name": "Empower Spell",
      "description": "You can cast spells to greater effect. All variable, numeric effects of an empowered spell are increased by half, including bonuses to those rolls. For example, an empowered magic missile deals 1.5 times the rolled damage.",
      "prerequisites": {
        "minimum_level": 3,
        "class_requirements": ["Spellcaster"],
        "other": "Ability to cast 2nd-level spells."
      },
      "effects": {
        "spell_slot_modifier": 2,
        "bonus": {
          "type": "variable_numeric_increase",
          "value": 1.5
        }
      },
      "source": "Player's Handbook, page 93",
      "progression_rules": {
        "valid_levels": ">= 3",
        "scaling_effects": False
      }
    },
{
      "name": "Extend Spell",
      "description": "You can make your spells last twice as long as normal. A spell with a duration of concentration, instantaneous, or permanent is not affected by this feat.",
      "prerequisites": {
        "minimum_level": 3,
        "class_requirements": ["Spellcaster"],
        "other": "Ability to cast 2nd-level spells."
      },
      "effects": {
        "spell_slot_modifier": 1,
        "bonus": {
          "type": "duration_multiplier",
          "value": 2
        }
      },
      "source": "Player's Handbook, page 94",
      "progression_rules": {
        "valid_levels": ">= 3",
        "scaling_effects": False
      }
    },
{
      "name": "Maximize Spell",
      "description": "You can cast spells to maximum effect. All variable, numeric effects of a maximized spell are maximized. For example, a maximized fireball deals 6 points of damage per caster level (up to 60 points at 10th level) instead of rolling for damage.",
      "prerequisites": {
        "minimum_level": 5,
        "class_requirements": ["Spellcaster"],
        "other": "Ability to cast 3rd-level spells."
      },
      "effects": {
        "spell_slot_modifier": 3,
        "bonus": {
          "type": "variable_numeric_maximum",
          "value": "maximum"
        }
      },
      "source": "Player's Handbook, page 94",
      "progression_rules": {
        "valid_levels": ">= 5",
        "scaling_effects": False
      }
    },
{
      "name": "Quicken Spell",
      "description": "You can cast a spell as a free action. You can perform another action, even casting another spell, in the same round as you cast a quickened spell. A quickened spell’s casting time is reduced to a free action. You can perform only one quickened spell per round, and the spell must have a casting time of 1 round or less.",
      "prerequisites": {
        "minimum_level": 9,
        "class_requirements": ["Spellcaster"],
        "other": "Ability to cast 5th-level spells."
      },
      "effects": {
        "spell_slot_modifier": 4,
        "bonus": {
          "type": "casting_time_reduction",
          "value": "free_action"
        }
      },
      "source": "Player's Handbook, page 98",
      "progression_rules": {
        "valid_levels": ">= 9",
        "scaling_effects": False
      }
    },
{
      "name": "Silent Spell",
      "description": "You can cast a spell without verbal components. A silent spell can be cast with no verbal component, and the spell operates normally. Spells without verbal components are not affected.",
      "prerequisites": {
        "minimum_level": None,
        "class_requirements": ["Spellcaster"],
        "other": "Ability to cast 1st-level spells."
      },
      "effects": {
        "spell_slot_modifier": 1,
        "bonus": {
          "type": "remove_verbal_component",
          "value": True
        }
      },
      "source": "Player's Handbook, page 100",
      "progression_rules": {
        "valid_levels": ">= 1",
        "scaling_effects": False
      }
    },
{
      "name": "Still Spell",
      "description": "You can cast a spell without somatic components. A stilled spell can be cast with no somatic component, and the spell operates normally. Spells without somatic components are not affected.",
      "prerequisites": {
        "minimum_level": None,
        "class_requirements": ["Spellcaster"],
        "other": "Ability to cast 1st-level spells."
      },
      "effects": {
        "spell_slot_modifier": 1,
        "bonus": {
          "type": "remove_somatic_component",
          "value": True
        }
      },
      "source": "Player's Handbook, page 101",
      "progression_rules": {
        "valid_levels": ">= 1",
        "scaling_effects": False
      }
    },
{
      "name": "Heighten Spell",
      "description": "You can cast a spell as if it were a higher-level spell. A heightened spell has a higher spell level for determining saving throw DCs and other effects, up to a maximum of the caster’s highest spell level.",
      "prerequisites": {
        "minimum_level": None,
        "class_requirements": ["Spellcaster"],
        "other": "Ability to cast 1st-level spells."
      },
      "effects": {
        "spell_slot_modifier": "variable",
        "bonus": {
          "type": "spell_level_increase",
          "value": "caster_choice"
        }
      },
      "source": "Player's Handbook, page 101",
      "progression_rules": {
        "valid_levels": ">= 1",
        "scaling_effects": True
      }
    },
{
      "name": "Widen Spell",
      "description": "You can increase the area of your spells. Any numeric measurements of an area of effect are increased by 100%. For example, a fireball’s radius doubles from 20 feet to 40 feet.",
      "prerequisites": {
        "minimum_level": None,
        "class_requirements": ["Spellcaster"],
        "other": "Ability to cast 3rd-level spells."
      },
      "effects": {
        "spell_slot_modifier": 3,
        "bonus": {
          "type": "area_of_effect_increase",
          "value": 2
        }
      },
      "source": "Player's Handbook, page 102",
      "progression_rules": {
        "valid_levels": ">= 5",
        "scaling_effects": False
      }
    },
{
      "name": "Twin Spell",
      "description": "You can cast a single-target spell simultaneously on two targets within range. Both targets must be legal targets for the spell, and the caster must spend an additional spell slot to create the duplicate effect.",
      "prerequisites": {
        "minimum_level": None,
        "class_requirements": ["Spellcaster"],
        "other": "Ability to cast 4th-level spells."
      },
      "effects": {
        "spell_slot_modifier": "+4 levels",
        "bonus": {
          "type": "duplicate_single_target_spell",
          "value": 2
        }
      },
      "source": "Player's Handbook, page 103",
      "progression_rules": {
        "valid_levels": ">= 7",
        "scaling_effects": False
      }
    },
{
      "name": "Energy Substitution",
      "description": "You can modify a spell with an energy descriptor to use another type of energy instead. Choose one energy type (acid, cold, electricity, fire, or sonic). This energy type replaces the normal energy type of the spell, and the spell operates normally except for the changed energy descriptor.",
      "prerequisites": {
        "minimum_level": None,
        "class_requirements": ["Spellcaster"],
        "other": "Knowledge (arcana) 5 ranks."
      },
      "effects": {
        "spell_slot_modifier": 0,
        "bonus": {
          "type": "change_energy_type",
          "value": "chosen_energy"
        }
      },
      "source": "Player's Handbook, page 104",
      "progression_rules": {
        "valid_levels": ">= 1",
        "scaling_effects": False
      }
    },
{
      "name": "Chain Spell",
      "description": "You can cast a spell that arcs from one target to another. A chained spell affects a primary target normally and then arcs to a number of secondary targets equal to your caster level (maximum 20). Secondary targets take half damage or suffer half the effect of the spell (if applicable).",
      "prerequisites": {
        "minimum_level": None,
        "class_requirements": ["Spellcaster"],
        "other": "Ability to cast 5th-level spells."
      },
      "effects": {
        "spell_slot_modifier": "+3 levels",
        "bonus": {
          "type": "chain_spell_effect",
          "value": {
            "primary_target": "full_effect",
            "secondary_targets": "half_effect"
          }
        }
      },
      "source": "Player's Handbook, page 104",
      "progression_rules": {
        "valid_levels": ">= 9",
        "scaling_effects": True
      }
    },
{
      "name": "Persistent Spell",
      "description": "You can cast a spell that lasts all day. A persistent spell has its duration increased to 24 hours, provided the spell has a fixed or personal range and a duration measured in rounds, minutes, or hours. Spells with an instantaneous or concentration duration cannot be affected by this feat.",
      "prerequisites": {
        "minimum_level": None,
        "class_requirements": ["Spellcaster"],
        "other": "Ability to cast 6th-level spells."
      },
      "effects": {
        "spell_slot_modifier": "+6 levels",
        "bonus": {
          "type": "duration_increase",
          "value": "24_hours"
        }
      },
      "source": "Player's Handbook, page 105",
      "progression_rules": {
        "valid_levels": ">= 11",
        "scaling_effects": False
      }
    },
{
      "name": "Sculpt Spell",
      "description": "You can modify the area of your spells. A sculpted spell allows you to reshape an area spell’s effect to exclude certain areas, such as creating pockets of safety within the area of effect. You can choose to create up to four 10-foot cubes within the spell’s normal area of effect.",
      "prerequisites": {
        "minimum_level": None,
        "class_requirements": ["Spellcaster"],
        "other": "Ability to cast 2nd-level spells."
      },
      "effects": {
        "spell_slot_modifier": "+1 level",
        "bonus": {
          "type": "area_modification",
          "value": {
            "shape": "up_to_four_10_foot_cubes"
          }
        }
      },
      "source": "Player's Handbook, page 106",
      "progression_rules": {
        "valid_levels": ">= 3",
        "scaling_effects": False
      }
    },
{
      "name": "Reach Spell",
      "description": "You can cast spells at a greater distance. A spell with a range of touch can instead target creatures or objects within 30 feet. Spells with ranges other than touch are unaffected.",
      "prerequisites": {
        "minimum_level": None,
        "class_requirements": ["Spellcaster"],
        "other": "Ability to cast 2nd-level spells."
      },
      "effects": {
        "spell_slot_modifier": "+1 level",
        "bonus": {
          "type": "range_increase",
          "value": "30_feet_for_touch_spells"
        }
      },
      "source": "Player's Handbook, page 107",
      "progression_rules": {
        "valid_levels": ">= 3",
        "scaling_effects": False
      }
    },
{
      "name": "Split Ray",
      "description": "You can split a ray spell to affect two targets. A split ray spell allows you to aim the ray at two targets, making a separate attack roll for each target. Damage and other effects are rolled separately for each ray.",
      "prerequisites": {
        "minimum_level": None,
        "class_requirements": ["Spellcaster"],
        "other": "Ability to cast ray spells."
      },
      "effects": {
        "spell_slot_modifier": "+2 levels",
        "bonus": {
          "type": "ray_split",
          "value": "two_targets"
        }
      },
      "source": "Player's Handbook, page 108",
      "progression_rules": {
        "valid_levels": ">= 5",
        "scaling_effects": False
      }
    },
{
      "name": "Invisible Spell",
      "description": "You can cast a spell with no visible effect. An invisible spell has no visual manifestation, making it undetectable to creatures that rely on sight. This feat does not affect spells with tangible effects (like summoned objects or creatures).",
      "prerequisites": {
        "minimum_level": None,
        "class_requirements": ["Spellcaster"],
        "other": "Ability to cast 2nd-level spells."
      },
      "effects": {
        "spell_slot_modifier": "+0 levels",
        "bonus": {
          "type": "remove_visual_component",
          "value": True
        }
      },
      "source": "Player's Handbook, page 109",
      "progression_rules": {
        "valid_levels": ">= 3",
        "scaling_effects": False
      }
    },
{
      "name": "Ocular Spell",
      "description": "You can cast a spell and store it within your eyes. An ocular spell is treated as a ranged spell that targets an area or creature. The spell remains dormant in your eyes until you choose to activate it as a standard action. Only one spell can be stored at a time in each eye.",
      "prerequisites": {
        "minimum_level": None,
        "class_requirements": ["Spellcaster"],
        "other": "Ability to cast 3rd-level spells."
      },
      "effects": {
        "spell_slot_modifier": "+2 levels",
        "bonus": {
          "type": "store_spell_in_eyes",
          "value": "one_per_eye"
        }
      },
      "source": "Player's Handbook, page 110",
      "progression_rules": {
        "valid_levels": ">= 5",
        "scaling_effects": False
      }
    },
{
      "name": "Sanctum Spell",
      "description": "You can cast spells that are more potent within a particular sanctum. When you cast a sanctum spell within your sanctum (a designated area), the spell is treated as if it were one level higher for all purposes, including determining saving throw DCs and overcoming spell resistance. Outside of your sanctum, the spell is treated as one level lower for all purposes.",
      "prerequisites": {
        "minimum_level": None,
        "class_requirements": ["Spellcaster"],
        "other": "Ability to cast 1st-level spells."
      },
      "effects": {
        "spell_slot_modifier": 0,
        "bonus": {
          "type": "level_modifier_in_sanctum",
          "value": {
            "in_sanctum": "+1 level",
            "outside_sanctum": "-1 level"
          }
        }
      },
      "source": "Player's Handbook, page 111",
      "progression_rules": {
        "valid_levels": ">= 1",
        "scaling_effects": False
      }
    },
{
      "name": "Earthbound Spell",
      "description": "You can cast spells that are tied to the earth. An earthbound spell functions normally when the caster is in contact with the ground, but loses effectiveness if cast while airborne. Grounded spells are treated as one level higher for overcoming spell resistance and for determining duration.",
      "prerequisites": {
        "minimum_level": None,
        "class_requirements": ["Spellcaster"],
        "other": "Ability to cast 1st-level spells."
      },
      "effects": {
        "spell_slot_modifier": 0,
        "bonus": {
          "type": "ground_contact_effectiveness",
          "value": {
            "in_contact": "+1 level",
            "not_in_contact": "normal effectiveness"
          }
        }
      },
      "source": "Player's Handbook, page 112",
      "progression_rules": {
        "valid_levels": ">= 1",
        "scaling_effects": False
      }
    },
{
      "name": "Cooperative Spell",
      "description": "You and another spellcaster can cast spells together to increase their power. When you cast a cooperative spell with another caster who also has this feat, the spell’s saving throw DCs increase by +2, and both casters must cast the same spell simultaneously for the effect to apply.",
      "prerequisites": {
        "minimum_level": None,
        "class_requirements": ["Spellcaster"],
        "other": "Ability to cast 1st-level spells."
      },
      "effects": {
        "spell_slot_modifier": 0,
        "bonus": {
          "type": "cooperative_casting_bonus",
          "value": "+2 to saving throw DCs"
        }
      },
      "source": "Player's Handbook, page 113",
      "progression_rules": {
        "valid_levels": ">= 1",
        "scaling_effects": False
      }
    },
{
      "name": "Selective Spell",
      "description": "You can shape your spells to avoid harming certain targets. When casting an area spell, you can designate a number of targets equal to your spellcasting ability modifier to automatically succeed on their saving throws and take no damage or effects from the spell.",
      "prerequisites": {
        "minimum_level": None,
        "class_requirements": ["Spellcaster"],
        "other": "Ability to cast 2nd-level spells."
      },
      "effects": {
        "spell_slot_modifier": "+1 level",
        "bonus": {
          "type": "exclude_targets_from_area",
          "value": "equal_to_spellcasting_modifier"
        }
      },
      "source": "Player's Handbook, page 114",
      "progression_rules": {
        "valid_levels": ">= 3",
        "scaling_effects": False
      }
    },
{
      "name": "Disruptive Spell",
      "description": "You can make your spells more difficult to resist. A disruptive spell imposes disadvantage on concentration checks made to maintain spells affected by it. Targets affected by the spell must also succeed on a concentration check with a DC equal to the spell’s save DC or lose their spellcasting ability for 1 round.",
      "prerequisites": {
        "minimum_level": None,
        "class_requirements": ["Spellcaster"],
        "other": "Ability to cast 2nd-level spells."
      },
      "effects": {
        "spell_slot_modifier": "+1 level",
        "bonus": {
          "type": "concentration_disadvantage",
          "value": "spell_save_DC"
        }
      },
      "source": "Player's Handbook, page 115",
      "progression_rules": {
        "valid_levels": ">= 3",
        "scaling_effects": False
      }
    },
{
      "name": "Dazing Spell",
      "description": "You can daze creatures with the power of your spells. A dazing spell causes creatures that take damage from the spell to be dazed for 1 round (a successful Will save negates the effect). Creatures immune to mind-affecting effects are not affected.",
      "prerequisites": {
        "minimum_level": None,
        "class_requirements": ["Spellcaster"],
        "other": "Ability to cast 3rd-level spells."
      },
      "effects": {
        "spell_slot_modifier": "+2 levels",
        "bonus": {
          "type": "daze_on_damage",
          "value": "1 round"
        }
      },
      "source": "Player's Handbook, page 116",
      "progression_rules": {
        "valid_levels": ">= 5",
        "scaling_effects": False
      }
    },
{
      "name": "Fortify Spell",
      "description": "You can increase the effectiveness of your spells against spell resistance. A fortified spell increases your caster level by +2 for the purpose of overcoming spell resistance.",
      "prerequisites": {
        "minimum_level": None,
        "class_requirements": ["Spellcaster"],
        "other": "Ability to cast 1st-level spells."
      },
      "effects": {
        "spell_slot_modifier": "+1 level",
        "bonus": {
          "type": "caster_level_increase_against_SR",
          "value": "+2"
        }
      },
      "source": "Player's Handbook, page 117",
      "progression_rules": {
        "valid_levels": ">= 1",
        "scaling_effects": False
      }
    },
{
      "name": "Subdual Substitution",
      "description": "You can modify a spell that deals energy damage to deal nonlethal damage instead. A subdual substituted spell changes all damage dealt by the spell to nonlethal damage, with no other effects altered.",
      "prerequisites": {
        "minimum_level": None,
        "class_requirements": ["Spellcaster"],
        "other": "Knowledge (arcana) 5 ranks."
      },
      "effects": {
        "spell_slot_modifier": "+0 levels",
        "bonus": {
          "type": "convert_to_nonlethal_damage",
          "value": True
        }
      },
      "source": "Player's Handbook, page 118",
      "progression_rules": {
        "valid_levels": ">= 1",
        "scaling_effects": False
      }
    },
{
      "name": "Ectoplasmic Spell",
      "description": "You can cast spells that affect incorporeal creatures as if they were corporeal. An ectoplasmic spell affects incorporeal creatures without the normal miss chance associated with their incorporeal nature.",
      "prerequisites": {
        "minimum_level": None,
        "class_requirements": ["Spellcaster"],
        "other": "Ability to cast 2nd-level spells."
      },
      "effects": {
        "spell_slot_modifier": "+1 level",
        "bonus": {
          "type": "affect_incorporeal_creatures",
          "value": True
        }
      },
      "source": "Player's Handbook, page 119",
      "progression_rules": {
        "valid_levels": ">= 3",
        "scaling_effects": False
      }
    },
{
      "name": "Delay Spell",
      "description": "You can cast a spell to activate at a later time. A delayed spell does not activate until 1 to 5 rounds after you finish casting it, as determined by you at the time of casting. Once set, the delay cannot be changed. A delayed spell creates no effect until it activates.",
      "prerequisites": {
        "minimum_level": None,
        "class_requirements": ["Spellcaster"],
        "other": "Ability to cast 3rd-level spells."
      },
      "effects": {
        "spell_slot_modifier": "+3 levels",
        "bonus": {
          "type": "delayed_activation",
          "value": "1 to 5 rounds"
        }
      },
      "source": "Player's Handbook, page 120",
      "progression_rules": {
        "valid_levels": ">= 5",
        "scaling_effects": False
      }
    },
{
      "name": "Fell Drain",
      "description": "You can infuse your spells with negative energy, draining life from those they affect. A fell drain spell bestows one negative level on any creature that takes damage from the spell. This effect applies only once per casting, even if a creature takes damage multiple times from the spell.",
      "prerequisites": {
        "minimum_level": None,
        "class_requirements": ["Spellcaster"],
        "other": "Ability to cast 3rd-level spells."
      },
      "effects": {
        "spell_slot_modifier": "+2 levels",
        "bonus": {
          "type": "bestow_negative_level",
          "value": 1
        }
      },
      "source": "Player's Handbook, page 121",
      "progression_rules": {
        "valid_levels": ">= 5",
        "scaling_effects": False
    },
    },
{
      "name": "Fell Frighten",
      "description": "You can infuse your spells with fear, causing creatures affected to become shaken. A fell frighten spell causes any creature that takes damage from the spell to become shaken for 1 minute. Creatures immune to fear effects are not affected.",
      "prerequisites": {
        "minimum_level": None,
        "class_requirements": ["Spellcaster"],
        "other": "Ability to cast 3rd-level spells."
      },
      "effects": {
        "spell_slot_modifier": "+2 levels",
        "bonus": {
          "type": "inflict_shaken_condition",
          "value": "1 minute"
        }
      },
      "source": "Player's Handbook, page 122",
      "progression_rules": {
        "valid_levels": ">= 5",
        "scaling_effects": False
      }
    },
{
      "name": "Fell Weaken",
      "description": "You can infuse your spells with enfeebling energy, causing creatures affected to take a penalty to Strength. A fell weaken spell causes any creature that takes damage from the spell to take a -4 penalty to Strength for 1 minute. This effect does not stack with other Strength penalties from the same source.",
      "prerequisites": {
        "minimum_level": None,
        "class_requirements": ["Spellcaster"],
        "other": "Ability to cast 3rd-level spells."
      },
      "effects": {
        "spell_slot_modifier": "+2 levels",
        "bonus": {
          "type": "inflict_strength_penalty",
          "value": "-4 Strength for 1 minute"
        }
      },
      "source": "Player's Handbook, page 123",
      "progression_rules": {
        "valid_levels": ">= 5",
        "scaling_effects": False
      }
    },
{
      "name": "Explosive Spell",
      "description": "You can make your spells cause violent explosions that knock creatures back. An explosive spell causes creatures in the area of effect to be pushed 10 feet away from the spell’s point of origin if they fail a Reflex save. Creatures that are pushed must also succeed on a Balance check (DC equal to the spell’s save DC) or fall prone.",
      "prerequisites": {
        "minimum_level": None,
        "class_requirements": ["Spellcaster"],
        "other": "Ability to cast 3rd-level spells."
      },
      "effects": {
        "spell_slot_modifier": "+2 levels",
        "bonus": {
          "type": "knockback_and_prone",
          "value": "10 feet knockback, prone on failed Balance check"
        }
      },
      "source": "Player's Handbook, page 124",
      "progression_rules": {
        "valid_levels": ">= 5",
        "scaling_effects": False
      }
    },
{
      "name": "Residual Magic",
      "description": "You can harness the leftover energy of previously cast spells. After casting a spell of 3rd level or higher, you gain a residual magic charge that lasts until the end of your next turn. You can expend this charge to either reduce the spell slot cost of a metamagic-enhanced spell by one level or increase the caster level of a spell by 1.",
      "prerequisites": {
        "minimum_level": None,
        "class_requirements": ["Spellcaster"],
        "other": "Ability to cast 3rd-level spells."
      },
      "effects": {
        "spell_slot_modifier": "-1 level when charge used",
        "bonus": {
          "type": "residual_magic_charge",
          "value": {
            "reduce_metamagic_cost": "-1 level",
            "increase_caster_level": "+1"
          }
        }
      },
      "source": "Player's Handbook, page 125",
      "progression_rules": {
        "valid_levels": ">= 5",
        "scaling_effects": True
      }
    },


#--------------------------------------------Item Creation Feats
{
      "name": "Brew Potion",
      "description": "You can create potions of spells. You can brew potions of any spell of 3rd level or lower that you know and that targets a creature or creatures. Brewing a potion takes 1 day for each 1,000 gp in its base price. The base price of a potion is its spell level × caster level × 50 gp.",
      "prerequisites": {
        "minimum_level": 3,
        "class_requirements": ["Spellcaster"],
        "other": "Caster level 3rd.",
        "milestone_requirement": "Requires milestone resource expenditure equivalent to XP cost."
      },
      "effects": {
        "spell_slot_modifier": "n/a",
        "bonus": {
          "type": "create_potions",
          "value": "spells of 3rd level or lower"
        }
      },
      "source": "Player's Handbook, page 126",
      "progression_rules": {
        "valid_levels": ">= 3",
        "scaling_effects": False
      }
    },
{
      "name": "Craft Magic Arms and Armor",
      "description": "You can create magical weapons, armor, and shields. Crafting a magic item requires 1 day for each 1,000 gp of its base price. You must spend 1/25 of the base price in XP and use up raw materials costing half the base price. Milestone leveling replaces the XP requirement with equivalent milestone resource expenditure.",
      "prerequisites": {
        "minimum_level": 5,
        "class_requirements": ["Spellcaster"],
        "other": "Caster level 5th.",
        "milestone_requirement": "Requires milestone resource expenditure equivalent to XP cost."
      },
      "effects": {
        "spell_slot_modifier": "n/a",
        "bonus": {
          "type": "create_magic_arms_armor",
          "value": "any magical weapons, armor, and shields"
        }
      },
      "source": "Player's Handbook, page 128",
      "progression_rules": {
        "valid_levels": ">= 5",
        "scaling_effects": False
      }
    },
{
      "name": "Craft Rod",
      "description": "You can create magic rods. Crafting a rod requires 1 day for each 1,000 gp of its base price. You must spend 1/25 of the base price in XP and use up raw materials costing half the base price. Milestone leveling replaces the XP requirement with equivalent milestone resource expenditure.",
      "prerequisites": {
        "minimum_level": 9,
        "class_requirements": ["Spellcaster"],
        "other": "Caster level 9th.",
        "milestone_requirement": "Requires milestone resource expenditure equivalent to XP cost."
      },
      "effects": {
        "spell_slot_modifier": "n/a",
        "bonus": {
          "type": "create_magic_rods",
          "value": "any magical rods"
        }
      },
      "source": "Player's Handbook, page 129",
      "progression_rules": {
        "valid_levels": ">= 9",
        "scaling_effects": False
      }
    },
{
      "name": "Craft Staff",
      "description": "You can create magic staves. Crafting a staff requires 1 day for each 1,000 gp of its base price. You must spend 1/25 of the base price in XP and use up raw materials costing half the base price. Milestone leveling replaces the XP requirement with equivalent milestone resource expenditure.",
      "prerequisites": {
        "minimum_level": 12,
        "class_requirements": ["Spellcaster"],
        "other": "Caster level 12th.",
        "milestone_requirement": "Requires milestone resource expenditure equivalent to XP cost."
      },
      "effects": {
        "spell_slot_modifier": "n/a",
        "bonus": {
          "type": "create_magic_staves",
          "value": "any magical staves"
        }
      },
      "source": "Player's Handbook, page 130",
      "progression_rules": {
        "valid_levels": ">= 12",
        "scaling_effects": False
      }
    },
{
      "name": "Craft Wand",
      "description": "You can create magic wands. Crafting a wand requires 1 day for each 1,000 gp of its base price. You must spend 1/25 of the base price in XP and use up raw materials costing half the base price. Milestone leveling replaces the XP requirement with equivalent milestone resource expenditure.",
      "prerequisites": {
        "minimum_level": 5,
        "class_requirements": ["Spellcaster"],
        "other": "Caster level 5th.",
        "milestone_requirement": "Requires milestone resource expenditure equivalent to XP cost."
      },
      "effects": {
        "spell_slot_modifier": "n/a",
        "bonus": {
          "type": "create_magic_wands",
          "value": "any magical wands"
        }
      },
      "source": "Player's Handbook, page 131",
      "progression_rules": {
        "valid_levels": ">= 5",
        "scaling_effects": False
      }
    },
{
      "name": "Craft Wondrous Item",
      "description": "You can create wondrous magic items. Crafting a wondrous item requires 1 day for each 1,000 gp of its base price. You must spend 1/25 of the base price in XP and use up raw materials costing half the base price. Milestone leveling replaces the XP requirement with equivalent milestone resource expenditure.",
      "prerequisites": {
        "minimum_level": 3,
        "class_requirements": ["Spellcaster"],
        "other": "Caster level 3rd.",
        "milestone_requirement": "Requires milestone resource expenditure equivalent to XP cost."
      },
      "effects": {
        "spell_slot_modifier": "n/a",
        "bonus": {
          "type": "create_magic_wondrous_items",
          "value": "any magical wondrous items"
        }
      },
      "source": "Player's Handbook, page 132",
      "progression_rules": {
        "valid_levels": ">= 3",
        "scaling_effects": False
      }
    },
{
      "name": "Forge Ring",
      "description": "You can create magic rings. Crafting a ring requires 1 day for each 1,000 gp of its base price. You must spend 1/25 of the base price in XP and use up raw materials costing half the base price. Milestone leveling replaces the XP requirement with equivalent milestone resource expenditure.",
      "prerequisites": {
        "minimum_level": 12,
        "class_requirements": ["Spellcaster"],
        "other": "Caster level 12th.",
        "milestone_requirement": "Requires milestone resource expenditure equivalent to XP cost."
      },
      "effects": {
        "spell_slot_modifier": "n/a",
        "bonus": {
          "type": "create_magic_rings",
          "value": "any magical rings"
        }
      },
      "source": "Player's Handbook, page 133",
      "progression_rules": {
        "valid_levels": ">= 12",
        "scaling_effects": False
      }
    },
{
      "name": "Scribe Scroll",
      "description": "You can create magic scrolls. Scribing a scroll requires 1 day for each 1,000 gp of its base price. You must spend 1/25 of the base price in XP and use up raw materials costing half the base price. Milestone leveling replaces the XP requirement with equivalent milestone resource expenditure.",
      "prerequisites": {
        "minimum_level": 1,
        "class_requirements": ["Spellcaster"],
        "other": "Caster level 1st.",
        "milestone_requirement": "Requires milestone resource expenditure equivalent to XP cost."
      },
      "effects": {
        "spell_slot_modifier": "n/a",
        "bonus": {
          "type": "create_magic_scrolls",
          "value": "any magical scrolls"
        }
      },
      "source": "Player's Handbook, page 134",
      "progression_rules": {
        "valid_levels": ">= 1",
        "scaling_effects": False
      }
    },
{
      "name": "Craft Construct",
      "description": "You can create constructs, such as golems and other magical creatures. Crafting a construct requires 1 day for each 1,000 gp of its base price. You must spend 1/25 of the base price in XP and use up raw materials costing half the base price. Milestone leveling replaces the XP requirement with equivalent milestone resource expenditure. Additionally, you must have access to the appropriate spells and a suitable workshop.",
      "prerequisites": {
        "minimum_level": 9,
        "class_requirements": ["Spellcaster"],
        "other": "Caster level 9th, must have access to the Craft Magic Arms and Armor feat.",
        "milestone_requirement": "Requires milestone resource expenditure equivalent to XP cost."
      },
      "effects": {
        "spell_slot_modifier": "n/a",
        "bonus": {
          "type": "create_constructs",
          "value": "any magical constructs"
        }
      },
      "source": "Player's Handbook, page 135",
      "progression_rules": {
        "valid_levels": ">= 9",
        "scaling_effects": False
      }
    },
{
      "name": "Craft Contingent Spell",
      "description": "You can store a spell to be triggered under specific conditions. Crafting a contingent spell requires 1 day for each 1,000 gp of its base price. You must spend 1/25 of the base price in XP and use up raw materials costing half the base price. Milestone leveling replaces the XP requirement with equivalent milestone resource expenditure. The conditions for triggering must be clear and specified at the time of creation.",
      "prerequisites": {
        "minimum_level": 11,
        "class_requirements": ["Spellcaster"],
        "other": "Caster level 11th, must have access to the Craft Wondrous Item feat.",
        "milestone_requirement": "Requires milestone resource expenditure equivalent to XP cost."
      },
      "effects": {
        "spell_slot_modifier": "n/a",
        "bonus": {
          "type": "store_triggered_spells",
          "value": "any contingent spells"
        }
      },
      "source": "Player's Handbook, page 136",
      "progression_rules": {
        "valid_levels": ">= 11",
        "scaling_effects": False
      }
    },
#-----------------------------------------------------Psionic Feats
{
        "name": "Empower Power",
        "description": "You can manifest psionic powers to greater effect. All variable, numeric effects of an empowered power are increased by half, including bonuses to those rolls. For example, an empowered energy ray deals 1.5 times the rolled damage.",
        "prerequisites": {
            "minimum_level": None,
            "class_requirements": ["Psionic"],
            "other": "Ability to manifest 2nd-level powers."
        },
        "effects": {
            "power_point_cost_increase": "+2 points",
            "bonus": {
                "type": "variable_numeric_increase",
                "value": 1.5
            }
        },
        "source": "Expanded Psionics Handbook, page 46",
        "progression_rules": {
            "valid_levels": ">= 3",
            "scaling_effects": False
        }
    },
{
        "name": "Extend Power",
        "description": "You can manifest psionic powers with extended duration. An extended power lasts twice as long as normal. Powers with a duration of instantaneous or concentration are not affected by this feat.",
        "prerequisites": {
            "minimum_level": None,
            "class_requirements": ["Psionic"],
            "other": "Ability to manifest 2nd-level powers."
        },
        "effects": {
            "power_point_cost_increase": "+2 points",
            "bonus": {
                "type": "duration_multiplier",
                "value": 2
            }
        },
        "source": "Expanded Psionics Handbook, page 46",
        "progression_rules": {
            "valid_levels": ">= 3",
            "scaling_effects": False
        }
    },
{
        "name": "Maximize Power",
        "description": "You can manifest psionic powers to maximum effect. All variable, numeric effects of a maximized power are maximized. For example, a maximized energy ray deals maximum possible damage instead of rolling for damage.",
        "prerequisites": {
            "minimum_level": None,
            "class_requirements": ["Psionic"],
            "other": "Ability to manifest 3rd-level powers."
        },
        "effects": {
            "power_point_cost_increase": "+4 points",
            "bonus": {
                "type": "variable_numeric_maximum",
                "value": "maximum"
            }
        },
        "source": "Expanded Psionics Handbook, page 46",
        "progression_rules": {
            "valid_levels": ">= 5",
            "scaling_effects": False
        }
    },
{
        "name": "Quicken Power",
        "description": "You can manifest a psionic power as a swift action. A quickened power’s manifesting time is reduced to a swift action, but you can perform only one quickened power per round.",
        "prerequisites": {
            "minimum_level": None,
            "class_requirements": ["Psionic"],
            "other": "Ability to manifest 5th-level powers."
        },
        "effects": {
            "power_point_cost_increase": "+8 points",
            "bonus": {
                "type": "casting_time_reduction",
                "value": "swift_action"
            }
        },
        "source": "Expanded Psionics Handbook, page 46",
        "progression_rules": {
            "valid_levels": ">= 9",
            "scaling_effects": False
        }
    },
{
        "name": "Twin Power",
        "description": "You can manifest a single-target psionic power simultaneously on two targets within range. Both targets must be legal targets for the power, and you must spend additional power points to create the duplicate effect.",
        "prerequisites": {
            "minimum_level": None,
            "class_requirements": ["Psionic"],
            "other": "Ability to manifest 4th-level powers."
        },
        "effects": {
            "power_point_cost_increase": "+6 points",
            "bonus": {
                "type": "duplicate_single_target_power",
                "value": 2
            }
        },
        "source": "Expanded Psionics Handbook, page 47",
        "progression_rules": {
            "valid_levels": ">= 7",
            "scaling_effects": False
        }
    },
{
        "name": "Overchannel",
        "description": "You can increase your manifester level when manifesting psionic powers, potentially causing yourself damage. By overchanneling, you increase your effective manifester level by 1 to 3 levels, but you take 1d8 points of damage for each level increase beyond your normal manifester level.",
        "prerequisites": {
            "minimum_level": None,
            "class_requirements": ["Psionic"],
            "other": "Must be able to manifest psionic powers."
        },
        "effects": {
            "manifester_level_increase": {
                "value": "+1 to +3 levels",
                "damage": "1d8 per level increase beyond normal"
            }
        },
        "source": "Expanded Psionics Handbook, page 48",
        "progression_rules": {
            "valid_levels": ">= 1",
            "scaling_effects": False
        }
    },
{
        "name": "Psionic Meditation",
        "description": "You can focus your mind more quickly than normal, allowing you to regain psionic focus as a move action instead of a full-round action.",
        "prerequisites": {
            "minimum_level": None,
            "class_requirements": ["Psionic"],
            "other": "Must have the ability to gain psionic focus."
        },
        "effects": {
            "focus_regain_time": "move action"
        },
        "source": "Expanded Psionics Handbook, page 48",
        "progression_rules": {
            "valid_levels": ">= 1",
            "scaling_effects": False
        }
    },
{
        "name": "Psicrystal Affinity",
        "description": "You gain a psicrystal, a fragment of your personality that becomes a loyal companion. The psicrystal grants you a specific benefit depending on its personality and can act as an extension of your senses.",
        "prerequisites": {
            "minimum_level": None,
            "class_requirements": ["Psionic"],
            "other": "Must be able to manifest 1st-level powers."
        },
        "effects": {
            "gain_psicrystal": "true",
            "benefits": "Dependent on psicrystal's personality"
        },
        "source": "Expanded Psionics Handbook, page 49",
        "progression_rules": {
            "valid_levels": ">= 1",
            "scaling_effects": True
        }
    },
{
        "name": "Psicrystal Containment",
        "description": "You can store an additional psionic focus in your psicrystal, allowing you to maintain two psionic foci simultaneously. You can expend the focus stored in the psicrystal just as you would expend your own psionic focus.",
        "prerequisites": {
            "minimum_level": None,
            "class_requirements": ["Psionic"],
            "other": "Must have the Psicrystal Affinity feat."
        },
        "effects": {
            "additional_focus_storage": "true",
            "usage": "Psicrystal can store and expend psionic focus."
        },
        "source": "Expanded Psionics Handbook, page 50",
        "progression_rules": {
            "valid_levels": ">= 1",
            "scaling_effects": False
        }
    },
{
        "name": "Deep Impact",
        "description": "You can strike your opponent with a melee weapon as if making a touch attack, ignoring armor and natural armor bonuses to AC. You must expend your psionic focus to use this feat.",
        "prerequisites": {
            "minimum_level": None,
            "class_requirements": ["Psionic"],
            "other": "Base attack bonus +1, must be able to expend psionic focus."
        },
        "effects": {
            "ignore_ac_bonuses": "true",
            "usage": "Expend psionic focus to make a touch attack with a melee weapon."
        },
        "source": "Expanded Psionics Handbook, page 51",
        "progression_rules": {
            "valid_levels": ">= 1",
            "scaling_effects": False
        }
    },
{
        "name": "Greater Psionic Weapon",
        "description": "You can charge your melee weapon with additional psionic energy for greater damage. When expending your psionic focus, your melee attack deals an extra 4d6 points of damage.",
        "prerequisites": {
            "minimum_level": None,
            "class_requirements": ["Psionic"],
            "other": "Base attack bonus +5, must be able to expend psionic focus."
        },
        "effects": {
            "extra_damage": "4d6",
            "usage": "Expend psionic focus to deal extra damage with a melee attack."
        },
        "source": "Expanded Psionics Handbook, page 51",
        "progression_rules": {
            "valid_levels": ">= 5",
            "scaling_effects": False
        }
    },
{
        "name": "Psionic Body",
        "description": "Your mind reinforces your body. You gain 2 bonus hit points for each psionic feat you have, including this one.",
        "prerequisites": {
            "minimum_level": None,
            "class_requirements": ["Psionic"],
            "other": "None."
        },
        "effects": {
            "bonus_hit_points_per_psionic_feat": 2
        },
        "source": "Expanded Psionics Handbook, page 51",
        "progression_rules": {
            "valid_levels": ">= 1",
            "scaling_effects": True
        }
    },
{
        "name": "Psionic Fist",
        "description": "You can charge your unarmed strike with psionic energy for greater damage. When expending your psionic focus, your unarmed strike deals an extra 2d6 points of damage.",
        "prerequisites": {
            "minimum_level": None,
            "class_requirements": ["Psionic"],
            "other": "Base attack bonus +1, must be able to expend psionic focus."
        },
        "effects": {
            "extra_damage": "2d6",
            "usage": "Expend psionic focus to deal extra damage with an unarmed strike."
        },
        "source": "Expanded Psionics Handbook, page 52",
        "progression_rules": {
            "valid_levels": ">= 1",
            "scaling_effects": False
        }
    },
{
        "name": "Psionic Weapon",
        "description": "You can charge your melee weapon with psionic energy for greater damage. When expending your psionic focus, your melee attack deals an extra 2d6 points of damage.",
        "prerequisites": {
            "minimum_level": None,
            "class_requirements": ["Psionic"],
            "other": "Base attack bonus +1, must be able to expend psionic focus."
        },
        "effects": {
            "extra_damage": "2d6",
            "usage": "Expend psionic focus to deal extra damage with a melee attack."
        },
        "source": "Expanded Psionics Handbook, page 52",
        "progression_rules": {
            "valid_levels": ">= 1",
            "scaling_effects": False
        }
    },
{
        "name": "Speed of Thought",
        "description": "Your quick mind and psionic ability allow you to react faster than normal. As long as you are psionically focused and unarmored, you gain a +10-foot bonus to your speed.",
        "prerequisites": {
            "minimum_level": None,
            "class_requirements": ["Psionic"],
            "other": "Must be psionically focused and unarmored."
        },
        "effects": {
            "speed_bonus": "+10 feet",
            "conditions": "Psionically focused and unarmored."
        },
        "source": "Expanded Psionics Handbook, page 52",
        "progression_rules": {
            "valid_levels": ">= 1",
            "scaling_effects": False
        }
    },
{
        "name": "Up the Walls",
        "description": "You can run on walls for a short time. If you begin and end your movement on a horizontal surface, you can move up vertical surfaces as part of your normal movement. You must be psionically focused to use this feat.",
        "prerequisites": {
            "minimum_level": None,
            "class_requirements": ["Psionic"],
            "other": "Must be psionically focused."
        },
        "effects": {
            "wall_movement": "true",
            "conditions": "Begin and end movement on a horizontal surface."
        },
        "source": "Expanded Psionics Handbook, page 52",
        "progression_rules": {
            "valid_levels": ">= 1",
            "scaling_effects": False
        }
    },
{
        "name": "Greater Psicrystal",
        "description": "Your psicrystal’s abilities are more powerful than normal. Your psicrystal gains an additional +1 bonus to its Intelligence and an additional special ability based on its personality type.",
        "prerequisites": {
            "minimum_level": None,
            "class_requirements": ["Psionic"],
            "other": "Must have the Psicrystal Affinity feat."
        },
        "effects": {
            "bonus_intelligence": "+1",
            "additional_ability": "Dependent on psicrystal's personality."
        },
        "source": "Expanded Psionics Handbook, page 53",
        "progression_rules": {
            "valid_levels": ">= 1",
            "scaling_effects": True
        }
    },
{
        "name": "Ectopic Form (choose variant)",
        "description": "You manifest an astral construct of a specific, preselected shape. When you manifest an astral construct, it always takes the form you choose at the time you take this feat. The construct gains specific benefits based on the chosen variant.",
        "prerequisites": {
            "minimum_level": None,
            "class_requirements": ["Psionic"],
            "other": "Ability to manifest the astral construct power."
        },
        "effects": {
            "custom_astral_construct": "true",
            "variant_benefits": "Dependent on chosen variant."
        },
        "source": "Expanded Psionics Handbook, page 54",
        "progression_rules": {
            "valid_levels": ">= 1",
            "scaling_effects": True
        }
    },
#----------------------------------------------------General Magic-Enhancing Feats
{
        "name": "Spell Focus (choose a school)",
        "description": "You have a greater aptitude for casting spells from a particular school of magic. Add +1 to the Difficulty Class for all saving throws against spells from the school of magic you select when you choose this feat.",
        "prerequisites": {
            "minimum_level": None,
            "class_requirements": ["Spellcaster"],
            "other": "None."
        },
        "effects": {
            "dc_increase_for_school": "+1",
            "chosen_school": "Determined at the time this feat is taken."
        },
        "source": "Player's Handbook, page 101",
        "progression_rules": {
            "valid_levels": ">= 1",
            "scaling_effects": False
        }
    },
{
        "name": "Greater Spell Focus (choose a school)",
        "description": "You have an exceptional aptitude for casting spells from a particular school of magic. Add an additional +1 to the Difficulty Class for all saving throws against spells from the school of magic you select when you choose this feat. This bonus stacks with the bonus from Spell Focus.",
        "prerequisites": {
            "minimum_level": None,
            "class_requirements": ["Spellcaster"],
            "other": "Spell Focus in the chosen school."
        },
        "effects": {
            "additional_dc_increase_for_school": "+1",
            "chosen_school": "Determined at the time this feat is taken."
        },
        "source": "Player's Handbook, page 101",
        "progression_rules": {
            "valid_levels": ">= 1",
            "scaling_effects": False
        }
    },
{
        "name": "Spell Penetration",
        "description": "You are adept at breaking through spell resistance with your spells. You get a +2 bonus on caster level checks (1d20 + caster level) made to overcome a creature’s spell resistance.",
        "prerequisites": {
            "minimum_level": None,
            "class_requirements": ["Spellcaster"],
            "other": "None."
        },
        "effects": {
            "bonus_to_caster_level_checks": "+2"
        },
        "source": "Player's Handbook, page 101",
        "progression_rules": {
            "valid_levels": ">= 1",
            "scaling_effects": False
        }
    },
{
        "name": "Greater Spell Penetration",
        "description": "You are exceptionally skilled at breaking through spell resistance with your spells. You get an additional +2 bonus on caster level checks (1d20 + caster level) made to overcome a creature’s spell resistance. This bonus stacks with the bonus from Spell Penetration.",
        "prerequisites": {
            "minimum_level": None,
            "class_requirements": ["Spellcaster"],
            "other": "Spell Penetration feat."
        },
        "effects": {
            "additional_bonus_to_caster_level_checks": "+2",
            "stacking_with_spell_penetration": "True"
        },
        "source": "Player's Handbook, page 101",
        "progression_rules": {
            "valid_levels": ">= 1",
            "scaling_effects": False
        }
    },
{
        "name": "Spell Mastery",
        "description": "You have mastered a small number of spells so completely that you can prepare them without referring to a spellbook. Each time you take this feat, choose a number of spells equal to your Intelligence modifier. From that point on, you can prepare these spells without a spellbook.",
        "prerequisites": {
            "minimum_level": None,
            "class_requirements": ["Spellcaster"],
            "other": "Wizard class."
        },
        "effects": {
            "prepare_spells_without_spellbook": "true",
            "number_of_spells": "equal to Intelligence modifier"
        },
        "source": "Player's Handbook, page 101",
        "progression_rules": {
            "valid_levels": ">= 1",
            "scaling_effects": True
        }
    },
{
        "name": "Eschew Materials",
        "description": "You can cast spells without needing material components unless they have a cost. Spells with a material component costing 1 gp or more are not affected by this feat.",
        "prerequisites": {
            "minimum_level": None,
            "class_requirements": ["Spellcaster"],
            "other": "None."
        },
        "effects": {
            "ignore_material_components": "true",
            "exception": "Material components costing 1 gp or more."
        },
        "source": "Player's Handbook, page 101",
        "progression_rules": {
            "valid_levels": ">= 1",
            "scaling_effects": False
        }
    },
{
        "name": "Augment Summoning",
        "description": "Your summoned creatures are more powerful than normal. Each creature you conjure with any summon spell gains a +4 enhancement bonus to Strength and Constitution for the duration of the spell.",
        "prerequisites": {
            "minimum_level": None,
            "class_requirements": ["Spellcaster"],
            "other": "Spell Focus (Conjuration)."
        },
        "effects": {
            "summoned_creature_bonus": {
                "strength": "+4",
                "constitution": "+4"
            }
        },
        "source": "Player's Handbook, page 101",
        "progression_rules": {
            "valid_levels": ">= 1",
            "scaling_effects": False
        }
    },
{
        "name": "Arcane Preparation",
        "description": "You can prepare arcane spells ahead of time, as a wizard does. You can prepare any spell you know, allowing you to cast it as if it were a prepared spell. This feat is primarily used by spontaneous spellcasters like sorcerers.",
        "prerequisites": {
            "minimum_level": None,
            "class_requirements": ["Spellcaster"],
            "other": "Ability to cast arcane spells spontaneously."
        },
        "effects": {
            "prepare_arcane_spells": "true",
            "applies_to": "Spontaneous casters."
        },
        "source": "Player's Handbook, page 101",
        "progression_rules": {
            "valid_levels": ">= 1",
            "scaling_effects": False
        }
    },
{
        "name": "Exceptional Artisan",
        "description": "You are more efficient at crafting magic items. The time required to craft any magic item is reduced by 25%.",
        "prerequisites": {
            "minimum_level": None,
            "class_requirements": ["Spellcaster"],
            "other": "Must have a crafting feat (e.g., Craft Wondrous Item)."
        },
        "effects": {
            "crafting_time_reduction": "25%"
        },
        "source": "Eberron Campaign Setting, page 52",
        "progression_rules": {
            "valid_levels": ">= 1",
            "scaling_effects": False
        }
    },
{
        "name": "Extraordinary Artisan",
        "description": "You are more resourceful when crafting magic items. The gold piece cost to craft any magic item is reduced by 25%.",
        "prerequisites": {
            "minimum_level": None,
            "class_requirements": ["Spellcaster"],
            "other": "Must have a crafting feat (e.g., Craft Wondrous Item)."
        },
        "effects": {
            "crafting_cost_reduction": "25%"
        },
        "source": "Eberron Campaign Setting, page 52",
        "progression_rules": {
            "valid_levels": ">= 1",
            "scaling_effects": False
        }
    },
{
        "name": "Legendary Artisan",
        "description": "You are extremely efficient when crafting magic items. The experience point cost to craft any magic item is reduced by 25%.",
        "prerequisites": {
            "minimum_level": None,
            "class_requirements": ["Spellcaster"],
            "other": "Must have a crafting feat (e.g., Craft Wondrous Item)."
        },
        "effects": {
            "crafting_xp_cost_reduction": "25%"
        },
        "source": "Eberron Campaign Setting, page 52",
        "progression_rules": {
            "valid_levels": ">= 1",
            "scaling_effects": False
        }
    },
{
        "name": "Reserve Feat: Fiery Burst",
        "description": "You can channel latent magical energy into a burst of fire. As long as you have a 2nd-level or higher fire spell available to cast, you can create a 5-foot-radius burst of fire as a standard action, dealing 1d6 fire damage per level of the highest-level fire spell you have available. The burst appears within 30 feet and requires a Reflex save for half damage (DC 10 + spell level + your casting ability modifier).",
        "prerequisites": {
            "minimum_level": None,
            "class_requirements": ["Spellcaster"],
            "other": "Must have a 2nd-level or higher fire spell prepared or available."
        },
        "effects": {
            "usable_ability": "Fiery Burst",
            "damage_scaling": "1d6 per spell level"
        },
        "source": "Complete Mage, page 43",
        "progression_rules": {
            "valid_levels": ">= 1",
            "scaling_effects": True
        }
    },
    {
        "name": "Reserve Feat: Dimensional Jaunt",
        "description": "You can use your mastery of dimensional magic to teleport short distances. As long as you have a 4th-level or higher teleportation spell available to cast, you can teleport up to 10 feet as a move action. This ability does not provoke attacks of opportunity.",
        "prerequisites": {
            "minimum_level": None,
            "class_requirements": ["Spellcaster"],
            "other": "Must have a 4th-level or higher teleportation spell prepared or available."
        },
        "effects": {
            "usable_ability": "Dimensional Jaunt",
            "teleport_range": "10 feet"
        },
        "source": "Complete Mage, page 43",
        "progression_rules": {
            "valid_levels": ">= 1",
            "scaling_effects": True
        }
    },
    {
        "name": "Reserve Feat: Storm Bolt",
        "description": "You can channel the power of storms into a bolt of lightning. As long as you have a 2nd-level or higher electricity spell available to cast, you can unleash a 20-foot line of electricity as a standard action, dealing 1d6 electricity damage per level of the highest-level electricity spell you have available. Creatures in the line can attempt a Reflex save for half damage (DC 10 + spell level + your casting ability modifier).",
        "prerequisites": {
            "minimum_level": None,
            "class_requirements": ["Spellcaster"],
            "other": "Must have a 2nd-level or higher electricity spell prepared or available."
        },
        "effects": {
            "usable_ability": "Storm Bolt",
            "damage_scaling": "1d6 per spell level"
        },
        "source": "Complete Mage, page 43",
        "progression_rules": {
            "valid_levels": ">= 1",
            "scaling_effects": True
        }
    },
#--------------------------------------------------------Specialized Feats

 {
        "name": "Arcane Strike",
        "description": "You can channel your arcane energy into your melee attacks. As a swift action, you can sacrifice an arcane spell slot to grant your weapon a magical bonus on attack and damage rolls equal to the spell slot's level. This effect lasts until the end of your turn.",
        "prerequisites": {
            "minimum_level": None,
            "class_requirements": ["Spellcaster"],
            "other": "Ability to cast arcane spells."
        },
        "effects": {
            "swift_action": "Sacrifice an arcane spell slot to enhance attacks.",
            "bonus": {
                "attack_and_damage": "Equal to spell slot level",
                "duration": "Until the end of your turn"
            }
        },
        "source": "Complete Warrior, page 98",
        "progression_rules": {
            "valid_levels": ">= 1",
            "scaling_effects": False
        }
    },
{
        "name": "Practiced Spellcaster",
        "description": "Your caster level for one spellcasting class increases by up to 4. This bonus can’t increase your caster level beyond your Hit Dice. However, even if you can’t benefit from the full bonus immediately, if you later gain Hit Dice, you might be able to apply the rest of the bonus.",
        "prerequisites": {
            "minimum_level": None,
            "class_requirements": ["Spellcaster"],
            "other": "None."
        },
        "effects": {
            "caster_level_increase": "Up to +4",
            "maximum": "Caster level cannot exceed total Hit Dice"
        },
        "source": "Complete Arcane, page 82",
        "progression_rules": {
            "valid_levels": ">= 1",
            "scaling_effects": False
        }
    },
{
        "name": "Rapid Metamagic",
        "description": "You can apply metamagic feats to your spells faster than normal. Using a metamagic feat no longer increases the casting time of your spells.",
        "prerequisites": {
            "minimum_level": None,
            "class_requirements": ["Spellcaster"],
            "other": "Ability to spontaneously cast spells."
        },
        "effects": {
            "casting_time_increase": "None when applying metamagic feats"
        },
        "source": "Complete Arcane, page 82",
        "progression_rules": {
            "valid_levels": ">= 1",
            "scaling_effects": False
        }
    },
{
        "name": "Touch Spell Specialization",
        "description": "You are adept at dealing damage with touch spells. You gain a +2 bonus on touch attack rolls made with spells that require a melee touch attack.",
        "prerequisites": {
            "minimum_level": None,
            "class_requirements": ["Spellcaster"],
            "other": "Base attack bonus +2."
        },
        "effects": {
            "bonus_to_touch_attack_rolls": "+2"
        },
        "source": "Complete Arcane, page 83",
        "progression_rules": {
            "valid_levels": ">= 1",
            "scaling_effects": False
        }
    },
{
        "name": "Improved Counterspell",
        "description": "You are skilled at countering the spells of others. When counterspelling, you may use a spell of the same school that is one or more levels higher than the target spell.",
        "prerequisites": {
            "minimum_level": None,
            "class_requirements": ["Spellcaster"],
            "other": "None."
        },
        "effects": {
            "counterspell_school_bonus": "Use a higher-level spell of the same school."
        },
        "source": "Player's Handbook, page 95",
        "progression_rules": {
            "valid_levels": ">= 1",
            "scaling_effects": False
        }
    },
{
        "name": "Reactive Counterspell",
        "description": "You can counterspell as an immediate action, allowing you to disrupt spells outside of your turn.",
        "prerequisites": {
            "minimum_level": None,
            "class_requirements": ["Spellcaster"],
            "other": "Improved Counterspell."
        },
        "effects": {
            "immediate_counterspell": "True"
        },
        "source": "Complete Mage, page 45",
        "progression_rules": {
            "valid_levels": ">= 1",
            "scaling_effects": False
        }
    },
{
        "name": "Epic Counterspell",
        "description": "You can counterspell with exceptional precision and power. You may counterspell any spell as if using Improved Counterspell, and you gain a +10 bonus on caster level checks made to counterspell.",
        "prerequisites": {
            "minimum_level": 21,
            "class_requirements": ["Spellcaster"],
            "other": "Improved Counterspell."
        },
        "effects": {
            "universal_counterspell": "True",
            "bonus_to_counterspell_checks": "+10"
        },
        "source": "Epic Level Handbook, page 55",
        "progression_rules": {
            "valid_levels": ">= 21",
            "scaling_effects": False
        }
    },
{
        "name": "Sudden Empower",
        "description": "You can cast a spell with the Empower Spell metamagic feat without increasing the spell’s casting time or level. You can use this ability once per day.",
        "prerequisites": {
            "minimum_level": None,
            "class_requirements": ["Spellcaster"],
            "other": "None."
        },
        "effects": {
            "empower_spell_no_increase": "True",
            "usage": "Once per day"
        },
        "source": "Complete Arcane, page 83",
        "progression_rules": {
            "valid_levels": ">= 1",
            "scaling_effects": False
        }
    },
{
        "name": "Sudden Maximize",
        "description": "You can cast a spell with the Maximize Spell metamagic feat without increasing the spell’s casting time or level. You can use this ability once per day.",
        "prerequisites": {
            "minimum_level": None,
            "class_requirements": ["Spellcaster"],
            "other": "None."
        },
        "effects": {
            "maximize_spell_no_increase": "True",
            "usage": "Once per day"
        },
        "source": "Complete Arcane, page 83",
        "progression_rules": {
            "valid_levels": ">= 1",
            "scaling_effects": False
        }
    },
{
        "name": "Sudden Quicken",
        "description": "You can cast a spell with the Quicken Spell metamagic feat without increasing the spell’s casting time or level. You can use this ability once per day.",
        "prerequisites": {
            "minimum_level": None,
            "class_requirements": ["Spellcaster"],
            "other": "None."
        },
        "effects": {
            "quicken_spell_no_increase": "True",
            "usage": "Once per day"
        },
        "source": "Complete Arcane, page 83",
        "progression_rules": {
            "valid_levels": ">= 1",
            "scaling_effects": False
        }
    },
{
        "name": "Sudden Silent",
        "description": "You can cast a spell with the Silent Spell metamagic feat without increasing the spell’s casting time or level. You can use this ability once per day.",
        "prerequisites": {
            "minimum_level": None,
            "class_requirements": ["Spellcaster"],
            "other": "None."
        },
        "effects": {
            "silent_spell_no_increase": "True",
            "usage": "Once per day"
        },
        "source": "Complete Arcane, page 83",
        "progression_rules": {
            "valid_levels": ">= 1",
            "scaling_effects": False
        }
    },
{
        "name": "Sudden Still",
        "description": "You can cast a spell with the Still Spell metamagic feat without increasing the spell’s casting time or level. You can use this ability once per day.",
        "prerequisites": {
            "minimum_level": None,
            "class_requirements": ["Spellcaster"],
            "other": "None."
        },
        "effects": {
            "still_spell_no_increase": "True",
            "usage": "Once per day"
        },
        "source": "Complete Arcane, page 83",
        "progression_rules": {
            "valid_levels": ">= 1",
            "scaling_effects": False
        }
    },
 {
        "name": "Sudden Widen",
        "description": "You can cast a spell with the Widen Spell metamagic feat without increasing the spell’s casting time or level. You can use this ability once per day.",
        "prerequisites": {
            "minimum_level": None,
            "class_requirements": ["Spellcaster"],
            "other": "None."
        },
        "effects": {
            "widen_spell_no_increase": "True",
            "usage": "Once per day"
        },
        "source": "Complete Arcane, page 83",
        "progression_rules": {
            "valid_levels": ">= 1",
            "scaling_effects": False
        }
    },
{
        "name": "Arcane Thesis",
        "description": "You have studied a single spell extensively. When you apply metamagic feats to this spell, the total level adjustment is reduced by 1 (to a minimum of +0).",
        "prerequisites": {
            "minimum_level": None,
            "class_requirements": ["Spellcaster"],
            "other": "Must choose a specific spell to apply this feat to."
        },
        "effects": {
            "metamagic_level_adjustment_reduction": "-1",
            "applies_to": "Chosen spell"
        },
        "source": "Player's Handbook II, page 74",
        "progression_rules": {
            "valid_levels": ">= 1",
            "scaling_effects": False
        }
    },
{
        "name": "Spell Thematics",
        "description": "Your spells manifest with a distinct and recognizable appearance that reflects your personal style or magical signature. This customization provides a +1 bonus on saving throw DCs to resist your spells against creatures that recognize your signature.",
        "prerequisites": {
            "minimum_level": None,
            "class_requirements": ["Spellcaster"],
            "other": "None."
        },
        "effects": {
            "unique_spell_appearance": "True",
            "bonus_to_spell_save_dc": "+1 (situational)"
        },
        "source": "Player's Handbook II, page 75",
        "progression_rules": {
            "valid_levels": ">= 1",
            "scaling_effects": False
        }
    },
{
        "name": "Rapid Spell",
        "description": "You can cast spells with a longer casting time more quickly. A rapid spell with a casting time of 1 full round or longer instead has a casting time reduced by one step: 1 full-round action becomes 1 standard action, 1 minute becomes 1 full round, and so on. Rapid Spell increases the spell level by +1.",
        "prerequisites": {
            "minimum_level": None,
            "class_requirements": ["Spellcaster"],
            "other": "None."
        },
        "effects": {
            "casting_time_reduction": "One step",
            "spell_slot_modifier": "+1 level"
        },
        "source": "Complete Divine, page 84",
        "progression_rules": {
            "valid_levels": ">= 1",
            "scaling_effects": False
        }
    },
{
        "name": "Heightened Turning",
        "description": "Your turning or rebuking attempts are more powerful than normal. When determining the most powerful undead you can affect, you calculate your turning check as if you were four levels higher than your actual cleric level.",
        "prerequisites": {
            "minimum_level": None,
            "class_requirements": ["Cleric"],
            "other": "Ability to turn or rebuke undead."
        },
        "effects": {
            "turning_check_bonus": "+4 effective cleric levels"
        },
        "source": "Complete Divine, page 85",
        "progression_rules": {
            "valid_levels": ">= 1",
            "scaling_effects": False
        }
    },
#---------------------------------------------------------------------Crafting & Ritual Feats


{
        "name": "Magical Artisan",
        "description": "You have mastered the art of creating magic items, reducing the resources required. When creating a magic item, you reduce the gold, XP, and time cost by 25%. This feat must be chosen for a specific item creation feat.",
        "prerequisites": {
            "minimum_level": None,
            "class_requirements": ["Spellcaster"],
            "other": "Must have the item creation feat for the chosen item type."
        },
        "effects": {
            "resource_cost_reduction": "25%",
            "applies_to": "Specific item creation feat"
        },
        "source": "Forgotten Realms Campaign Setting, page 37",
        "progression_rules": {
            "valid_levels": ">= 1",
            "scaling_effects": False
        }
    },
{
        "name": "Cooperative Crafting",
        "description": "You can work with another spellcaster to craft magic items more efficiently. When you cooperate with another spellcaster who also has the necessary item creation feat, you reduce the crafting time by 10%. This bonus stacks with other effects that reduce crafting time.",
        "prerequisites": {
            "minimum_level": None,
            "class_requirements": ["Spellcaster"],
            "other": "Must have an item creation feat."
        },
        "effects": {
            "additional_crafting_time_reduction": "10%",
            "requires_cooperation": "True"
        },
        "source": "Pathfinder Core Rulebook, page 120",
        "progression_rules": {
            "valid_levels": ">= 1",
            "scaling_effects": False
        }
    },
{
        "name": "Item Familiar",
        "description": "You have forged a powerful magical bond with a specific item, turning it into a source of strength and power. You gain bonuses and abilities based on your bond with the item, such as increased skill points, additional spells, or combat bonuses. The item gains sentience and can aid you in various ways, depending on its chosen form and your character level.",
        "prerequisites": {
            "minimum_level": 3,
            "class_requirements": ["Spellcaster"],
            "other": "None."
        },
        "effects": {
            "item_bond": "Sentient item with special abilities",
            "customizable_effects": "Skill points, spells, or combat bonuses"
        },
        "source": "Unearthed Arcana, page 170",
        "progression_rules": {
            "valid_levels": ">= 3",
            "scaling_effects": True
        }
    },
#----------------------------------------------------------------Psionic/Magic Hybrid Feats



{
        "name": "Metapower",
        "description": "You have mastered the art of combining metapsionic feats with specific powers more efficiently. Choose one metapsionic feat and one psionic power you know. When applying the chosen feat to the chosen power, the total cost in power points is reduced by 2 (to a minimum of 1 power point).",
        "prerequisites": {
            "minimum_level": None,
            "class_requirements": ["Psionic"],
            "other": "Must have the chosen metapsionic feat and the chosen psionic power."
        },
        "effects": {
            "reduced_power_point_cost": "-2 when combining chosen feat and power",
            "applies_to": "Specific metapsionic feat and psionic power"
        },
        "source": "Complete Psionic, page 68",
        "progression_rules": {
            "valid_levels": ">= 1",
            "scaling_effects": False
        }
    },
{
        "name": "Mind Over Matter",
        "description": "You have exceptional control over your body and can shrug off physical harm through psionic focus. Once per day, you can expend your psionic focus to gain temporary hit points equal to your manifester level + your key ability modifier. These temporary hit points last for 10 minutes.",
        "prerequisites": {
            "minimum_level": None,
            "class_requirements": ["Psionic"],
            "other": "Must be able to gain psionic focus."
        },
        "effects": {
            "temporary_hit_points": "Manifester level + key ability modifier",
            "duration": "10 minutes",
            "usage": "Once per day"
        },
        "source": "Complete Psionic, page 69",
        "progression_rules": {
            "valid_levels": ">= 1",
            "scaling_effects": False
        }
    },
{
        "name": "Expanded Knowledge",
        "description": "You learn a new power from a psionic class list. The chosen power must be of a level no higher than the highest level of power you can manifest, and it is treated as a power of your class list.",
        "prerequisites": {
            "minimum_level": None,
            "class_requirements": ["Psionic"],
            "other": "Must be able to manifest psionic powers."
        },
        "effects": {
            "additional_power": "Gain one power from another psionic class list",
            "restrictions": "Must be of a level you can manifest."
        },
        "source": "Expanded Psionics Handbook, page 46",
        "progression_rules": {
            "valid_levels": ">= 1",
            "scaling_effects": False
        }
    },
 {
        "name": "Linked Power",
        "description": "You can manifest two powers in rapid succession. When you manifest a power using this feat, you can manifest a second power with a manifesting time of 1 standard action as a swift action in the next round. The second power’s power point cost is reduced by 2 (minimum 1 point).",
        "prerequisites": {
            "minimum_level": None,
            "class_requirements": ["Psionic"],
            "other": "Must be able to manifest psionic powers."
        },
        "effects": {
            "additional_manifestation": "Second power as a swift action in the next round",
            "power_point_cost_reduction": "-2 points (minimum 1 point)"
        },
        "source": "Complete Psionic, page 63",
        "progression_rules": {
            "valid_levels": ">= 1",
            "scaling_effects": False
        }
    },
{
        "name": "Dual-Manifester",
        "description": "You can manifest two powers simultaneously. When you use this feat, you may manifest two powers at the same time, both of which must have a manifesting time of 1 standard action. The total power point cost for both powers is increased by 4.",
        "prerequisites": {
            "minimum_level": None,
            "class_requirements": ["Psionic"],
            "other": "Must be able to manifest psionic powers."
        },
        "effects": {
            "simultaneous_manifestation": "Manifest two powers at the same time",
            "power_point_cost_increase": "+4 points"
        },
        "source": "Custom Source",
        "progression_rules": {
            "valid_levels": ">= 1",
            "scaling_effects": False
        }
    },
#--------------------------------------------------------------------------Other Feats



{
        "name": "Aligned Spellcaster",
        "description": "Your spells are imbued with the power of your alignment, making them more effective against creatures with opposing alignments. You gain a +1 bonus to caster level checks to overcome spell resistance of creatures with an alignment opposed to yours.",
        "prerequisites": {
            "minimum_level": None,
            "class_requirements": ["Spellcaster"],
            "other": "Must have an alignment other than Neutral."
        },
        "effects": {
            "bonus_to_caster_level_checks": "+1 against opposed alignment creatures"
        },
        "source": "Custom Source",
        "progression_rules": {
            "valid_levels": ">= 1",
            "scaling_effects": False
        }
    },
{
        "name": "Arcane Defense",
        "description": "You are especially resistant to spells from a specific school of magic. You gain a +2 bonus on saving throws against spells and effects from the chosen school of magic.",
        "prerequisites": {
            "minimum_level": None,
            "class_requirements": ["Spellcaster"],
            "other": "None."
        },
        "effects": {
            "saving_throw_bonus": "+2 against chosen school of magic"
        },
        "source": "Player's Handbook, page 95",
        "progression_rules": {
            "valid_levels": ">= 1",
            "scaling_effects": False
        }
    },
{
        "name": "Arcane Flourish",
        "description": "You can channel magical energy into a dazzling display to intimidate or inspire. As a standard action, you can expend an unused spell slot to gain a bonus on Intimidate or Perform checks equal to twice the spell slot’s level for 1 minute.",
        "prerequisites": {
            "minimum_level": None,
            "class_requirements": ["Spellcaster"],
            "other": "None."
        },
        "effects": {
            "skill_check_bonus": "+2 per spell level",
            "duration": "1 minute"
        },
        "source": "Custom Source",
        "progression_rules": {
            "valid_levels": ">= 1",
            "scaling_effects": False
        }
    },
{
        "name": "Energy Admixture",
        "description": "You can modify a spell with an energy descriptor to include a second type of energy, creating a hybrid effect. Choose an energy type (acid, cold, electricity, fire, or sonic) when you take this feat. Any spell you cast with an energy descriptor deals half of its damage as the chosen type in addition to its normal type. This increases the spell level by +4.",
        "prerequisites": {
            "minimum_level": None,
            "class_requirements": ["Spellcaster"],
            "other": "Energy Substitution feat."
        },
        "effects": {
            "additional_energy_type": "Chosen energy type",
            "spell_slot_modifier": "+4 levels"
        },
        "source": "Complete Arcane, page 79",
        "progression_rules": {
            "valid_levels": ">= 1",
            "scaling_effects": False
        }
    },
{
        "name": "Focused Specialist",
        "description": "You have chosen to specialize further in a single school of magic, gaining additional spell slots and power at the expense of access to other schools. As a focused specialist, you gain one additional spell slot per spell level for your specialty school but must forfeit one more spell school beyond those already prohibited by being a specialist wizard.",
        "prerequisites": {
            "minimum_level": None,
            "class_requirements": ["Wizard"],
            "other": "Must be a specialist wizard."
        },
        "effects": {
            "additional_spell_slots": "+1 per spell level for specialty school",
            "additional_prohibited_school": "One more prohibited school."
        },
        "source": "Complete Mage, page 34",
        "progression_rules": {
            "valid_levels": ">= 1",
            "scaling_effects": False
        }
    },
{
        "name": "Multispell",
        "description": "You can cast multiple quickened spells in the same round. When you cast a quickened spell, you can cast an additional quickened spell as a free action. This feat allows you to cast one extra quickened spell per round.",
        "prerequisites": {
            "minimum_level": 21,
            "class_requirements": ["Spellcaster"],
            "other": "Quicken Spell feat."
        },
        "effects": {
            "extra_quickened_spell": "One additional quickened spell per round"
        },
        "source": "Epic Level Handbook, page 60",
        "progression_rules": {
            "valid_levels": ">= 21",
            "scaling_effects": False
        }
    },
{
        "name": "Improved Metamagic",
        "description": "The spell level cost of your metamagic feats is reduced by 1, to a minimum of +1 spell level. This applies to all metamagic feats you use.",
        "prerequisites": {
            "minimum_level": 21,
            "class_requirements": ["Spellcaster"],
            "other": "None."
        },
        "effects": {
            "metamagic_level_cost_reduction": "-1 (minimum +1 level)"
        },
        "source": "Epic Level Handbook, page 61",
        "progression_rules": {
            "valid_levels": ">= 21",
            "scaling_effects": False
        }
    },
{
        "name": "Heightened Awareness",
        "description": "You are exceptionally aware of your surroundings, allowing you to react quickly to danger. You gain a +2 bonus on initiative checks and a +2 bonus on Perception checks.",
        "prerequisites": {
            "minimum_level": None,
            "class_requirements": ["None"],
            "other": "None."
        },
        "effects": {
            "initiative_bonus": "+2",
            "perception_bonus": "+2"
        },
        "source": "Custom Source",
        "progression_rules": {
            "valid_levels": ">= 1",
            "scaling_effects": False
        }
    },
{
        "name": "Spellcasting Prodigy",
        "description": "You have an exceptional gift for magic, making your spells more potent. For the purpose of determining bonus spells per day and the saving throw DCs of your spells, treat the ability score that controls your spellcasting as 2 points higher than its actual value.",
        "prerequisites": {
            "minimum_level": None,
            "class_requirements": ["Spellcaster"],
            "other": "None."
        },
        "effects": {
            "bonus_to_spellcasting_stat": "+2 for bonus spells and DCs"
        },
        "source": "Forgotten Realms Campaign Setting, page 36",
        "progression_rules": {
            "valid_levels": ">= 1",
            "scaling_effects": False
        }
    }
]