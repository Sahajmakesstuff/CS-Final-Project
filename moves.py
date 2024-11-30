#importing modules
import random
import math

#function to get a move from a move id
def from_move_id(datastore,move_id):
    move_id,name,type_,power,contact,accuracy=datastore.get_move(move_id)
    return Move(move_id,name,type_,power,contact,accuracy)

#The move class
class Move:
    
    #constructor
    def __init__(self,move_id,name,type_,power,contact,accuracy): 
        self.move_id=move_id
        self.name=name
        self.type=type_
        self.power=power
        self.contact=contact
        self.accuracy=accuracy  
    
    #function to use the move taking the attacker and defender pokemon objects as args
    def use_move(self, datastore,attacker, defender):
        attack=0
        defe=0
        if self.contact=="physical":        #physical move
            attack=attacker.att
            defe=defender.defe
        else:                               #special move
            attack=attacker.spatt
            defe=defender.spdef
        
        #var for stab
        stab=1

        #if same type
        if self.type==attacker.type:
            stab=1.5
        
        #vars for effectiveness
        effect=1
        super_effective=False
        not_effective=False

        #fetching strengths and weaknesses
        strengths=datastore.strengths(defender.type)
        weaknesses=datastore.weaknesses(defender.type)

        #if super effective
        if self.type in weaknesses:
            effect=2
            super_effective=True

        #if not very effective
        elif self.type in strengths:
            effect=0.5
            not_effective=True

        #variable for natural randomness in damage
        rand=random.randint(85,115)/100
        
        #calculating damage
        damage=math.ceil((((((2*10)+2)*
                                self.power*
                                attack/defe)/25)+2)*
                                stab *rand *effect)
        
        #1/16 chance of crit
        critical = random.randint(1, 16) == 1

        if critical:
            damage = int(damage * 1.5)  # Critical hit does 1.5x damage

        #so hp does not go below 0
        damage = min(damage, defender.hpIG) #clamp

        #updating hp
        defender.hpIG -= damage
        
        #returning the final calculated values
        return damage, critical, super_effective, not_effective