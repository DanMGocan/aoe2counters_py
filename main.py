# Software designed to simulate the fight between
# different AOE2 units and decide what counter
# best different units. Made in Python for a 
# Codecademy project. 

from dataclasses import dataclass

# Unit constructors.
# All units available to more than one civilization are not unique
# even if they are available to a limited few

@dataclass
class Unit:
    name: str
    elite: bool
    type: str
    trained_at: dict # For example { barracks: 13, castle: 16}
    cost: dict # For example {food: 0, wood: 0, gold: 0, stone: 0}
    hit_points: list
    attack: list
    attack_bonuses: list # List of two dictionaries, one for elite, one for non-elite
    rate_of_fire: float
    melee_armour: list
    pierce_armour: list
    armour_class: list
    speed: float    
    line_of_sight: list

@dataclass
class Archer(Unit):
    frame_delay: int
    range: list
    projectile_speed: int
    accuracy: list

@dataclass
class Unique(Unit):
    civilization: str




longbowman = Archer("Longbowman", False, "Archer", {"castle": 18}, {"food": 0, "wood": 35, "gold": 40, "stone": 0}, [35, 40], [6, 7], [{"Spearman": 2}, {}], 2.0, [0, 0],
                    [0, 0], ["Archer", "Unique unit"], 0.96, [7, 8], 10, [5, 6], 7, [70, 80])        


