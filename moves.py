#importing module
import random
import math
from typechart import *

#The move class
class Move:
    def __init__(self,name,type,power,contact,accuracy): 
        self.name=name
        self.type=type
        self.power=power
        self.contact=contact
        self.accuracy=accuracy

    def use_move(self, attacker, defender):
        attack=0
        defe=0
        if self.contact=="physical":
            attack=attacker.att
            defe=defender.defe
        else:
            attack=attacker.spatt
            defe=defender.spdef
        
        #var for missing
        Miss=False

        #var for accuracy check
        rand_acc=random.randrange(1,101)*100

        #if we hit
        if rand_acc<=self.accuracy:
            Miss=False
        
        #if we miss
        else:
            Miss=True  
        
        #var for stab
        stab=1

        #if same type
        if self.type==attacker.type:
            stab=1.5
        
        #vars for effectiveness
        effect=1
        super_effective=False
        not_effective=False

        #if super effective
        if self.type in type_chart[defender.type][1]:
            effect=2
            super_effective=True

        #if not very effective
        elif self.type in type_chart[defender.type][0]:
            effect=0.5
            not_effective=True

        rand=random.randint(85,115)/100

        damage=math.ceil((((((2*10)+2)*
                                self.power*
                                attack/defe)/25)+2)*
                                stab *rand *effect)
        
        critical = random.randint(1, 16) == 1

        if critical:
            damage = int(damage * 1.5)  # Critical hit does 1.5x damage

        damage = min(damage, defender.hpIG) #clamp

        defender.hpIG -= damage
        
        return damage, critical, super_effective, not_effective

#move list
moves = {
    "Flamethrower": Move("Flamethrower", "fire", 90,"special",95),
    "Fire Blast": Move("Fire Blast","fire",110,"special",85),
    "Fire Punch": Move("Fire Punch","fire",75,"physical",95),
    "Flare Blitz": Move("Flare Blitz","fire",120,"physical",85),
    "Fire Fang": Move("Fire Fang","fire",65,"physical",90),
    "Heat Wave": Move("Heat Wave","fire",95,"special",90),
    "Lava Plume": Move("Lava Plume","fire",80,"special",95),

    "Surf": Move("Surf","water",90,"special",95),
    "Crabhammer": Move("Crabhammer","water",100,"physical",90),
    "Hydro Pump": Move("Hydro Pump","water",110,"special",80),
    "Liquidation": Move("Liquidation","water",85,"physical",95),
    "Muddy Water": Move("Muddy Water","water",90,"special",85),
    "Scald": Move("Scald","water",80,"special",95),
    "Waterfall": Move("Waterfall","water",80,"physical",95),

    "Energy Ball": Move("Solar Beam","grass",90,"special",95),
    "Seed Bomb": Move("Seed Bomb","grass",80,"physical",95),
    "Giga Drain": Move("Giga Drain","grass",75,"special",95),
    "Leaf Blade": Move("Leaf Blade","grass",90,"physical",95),
    "Leaf Storm": Move("Leaf Storm","grass",130,"special",80),

    "Thunderbolt": Move("Thunderbolt","electric",90,"special",95),
    "Discharge": Move("Discharge","electric",80,"special",95),
    "Thunder Fang": Move("Thunder Fang","electric",65,"physical",90),
    "Thunder": Move("Thunder","electric",110,"special",70),
    "Thunder Punch": Move("Thunder Punch","electric",75,"physical",95),
    "Wild Charge": Move("Wild Charge","electric",90,"physical",90),

    "Ice Beam": Move("Ice Beam","ice",90,"special",95),
    "Blizzard": Move("Blizzard","ice",110,"special",70),
    "Icicle Crash": Move("Icicle Crash","ice",80,"physical",90),
    "Ice Fang": Move("Ice Fang","ice",65,"physical",90),
    "Ice Punch": Move("Ice Punch","ice",75,"physical",95),

    "Dragon Claw": Move("Dragon Claw","dragon",80,"physical",95),
    "Dragon Breath": Move("Dragon Breath","dragon",60,"special",95),
    "Draco Meteor": Move("Draco Meteor","dragon",130,"special",85),
    "Dragon Pulse": Move("Dragon Pulse","dragon",85,"special",95),
    "Outrage": Move("Outrage","dragon",120,"physical",90),
    "Dragon Tail": Move("Dragon Tail","dragon",60,"physical",90),
    "Dual Chop": Move("Dual Chop","dragon",80,"physical",95),

    "Earthquake": Move("Earthquake","ground",100,"physical",95),
    "Dig": Move("Dig","ground",60,"physical",95),
    "Bulldoze": Move("Bulldoze","ground",60,"physical",95),
    "Earth Power": Move("Earth Power","ground",80,"special",95),
    "Stomping Tantrum": Move("Stomping Tantrum","ground",75,"physical",95),
    "High Horsepower": Move("High Horsepower","ground",95,"physical",90),

    "Rock Slide": Move("Rock Slide","rock",75,"physical",90),
    "Stone Edge": Move("Stone Edge","rock",100,"physical",80),
    "Power Gem": Move("Power Gem","rock",80,"special",95),
    "Ancient Power": Move("Ancient Power","rock",60,"special",95),
    "Head Smash": Move("Head Smash","rock",150,"physical",80),

    "Flash Cannon": Move("Flash Cannon","steel",80,"special",95),
    "Iron Head": Move("Iron Head","steel",80,"physical",95),
    "Smart Strike": Move("Smart Strike","steel",70,"physical",100),
    "Meteor Mash": Move("Meteor Mash","steel",100,"physical",85),
    "Mirror Shot": Move("Mirror Shot","steel",65,"special",95),
    "Steel Wing": Move("Steel Wing","steel",70,"physical",95),

    "Body Slam": Move("Body Slam","normal",80,"physical",95),
    "Headbutt": Move("Headbutt","normal",70,"physical",95),
    "Strength": Move("Hyper Fang","normal",80,"physical",95),
    "Hyper Voice": Move("Hyper Voice","normal",90,"special",95),
    "Hyper Beam": Move("Hyper Beam","normal",150,"special",90),
    "Explosion": Move("Explosion","normal",200,"physical",95),

    "Moonblast": Move("Moonblast","fairy",95,"special",95),
    "Dazzling Gleam": Move("Dazzling Gleam","fairy",80,"special",95),
    "Play Rough": Move("Play Rough","fairy",90,"physical",90),
    "Spirit Break": Move("Spirit Break","fairy",75,"physical",95),
    "Misty Explosion": Move("Misty Explosion","fairy",100,"physical",95),

    "Brick Break": Move("Brick Break","fighting",75,"physical",95),
    "Aura Sphere": Move("Aura Sphere","fighting",80,"special",100),
    "Close Combat": Move("Close Combat","fighting",120,"physical",90),
    "Cross Chop": Move("Cross Chop","fighting",100,"physical",80),
    "Focus Blast": Move("Focus Blast","fighting",120,"special",70),
    "Superpower": Move("Superpower","fighting",120,"physical",85),

    "Dark Pulse": Move("Dark Pulse","dark",80,"special",95),
    "Knock Off": Move("Knock Off","dark",65,"physical",95),
    "Crunch": Move("Crunch","dark",80,"physical",95),
    "Night Slash": Move("Night Slash","dark",70,"physical",95),
    "Sucker Punch": Move("Sucker Punch","dark",70,"physical",95),
    "Throat Chop": Move("Throat Chop","dark",80,"physical",95),

    "Psychic": Move("Psychic","psychic",90,"special",95),
    "Psybeam": Move("Psybeam","psychic",65,"special",95),
    "Psyche Punch": Move("Psyche Punch","psychic",90,"physical",95),
    "Psyshock": Move("Psyshock","psychic",80,"special",95),
    "Psycho Cut": Move("Psycho Cut","psychic",70,"physical",95),

    "Shadow Ball": Move("Shadow Ball","ghost",80,"special",95),
    "Shadow Claw": Move("Shadow Claw","ghost",65,"physical",90),
    "Hex": Move("Hex","ghost",65,"special",95),
    "Shadow Punch": Move("Shadow Punch","ghost",75,"physical",95),
    "Poltergeist": Move("Poltergeist","ghost",110,"physical",85),

    "Brave Bird": Move("Brave Bird","flying",120,"physical",90),
    "Air Slash": Move("Air Slash","flying",75,"special",95),
    "Fly": Move("Fly","flying",90,"physical",85),
    "Drill Peck": Move("Drill Peck","flying",80,"physical",95),
    "Hurricane": Move("Hurricane","flying",110,"special",70),
    "Dual Wingbeat": Move("Dual Wingbeat","flying",80,"physical",80),

    "X-Scissor": Move("X-Scissor","bug",80,"physical",95),
    "Bug Buzz": Move("Bug Buzz","bug",90,"special",95),
    "Leech Life": Move("Leech Life","bug",80,"physical",95),
    "Megahorn": Move("Megahorn","bug",120,"physical",85),
    "Lunge": Move("Lunge","bug",80,"special",95),
    
    "Sludge Bomb": Move("Sludge Bomb","poison",90,"special",95),
    "Poison Jab": Move("Poison Jab","poison",80,"physical",95),
    "Sludge Wave": Move("Sludge Wave","poison",95,"special",90),
    "Gunk Shot": Move("Gunk Shot","poison",120,"physical",80),
    "Cross Poison": Move("Cross Poison","poison",70,"physical",95),
}