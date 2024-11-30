#importing modules
import random
import math
from moves import *
import mysql.connector

#Nature Class
class Nature:
    def __init__(self,nature_details):
        self.nature_id,self.name,self.att,self.defe,self.spatt,self.spdef,self.spd=nature_details

#pokemon class
class Pokemon:
    def __init__(self,datastore,name,nat_list): 
        
        #fetching pokemon details
        self.pokemon_id,self.name,self.type,self.base_hp,self.base_att,self.base_def,self.base_spatt,self.base_spdef,self.base_spd,self.cov_1,self.cov_2=datastore.get_pokemon(name)

        #selecting random nature
        self.nature=random.choice(nat_list)

        #setting level=50
        self.lvl=50

        #list of moves
        self.moves=[]
        self.stab_options=[]  

        #coverage moves
        self.cov_1=Move(*datastore.get_move(self.cov_1))        #* unpacks the tuple and passes value into function accordingly
        self.cov_2=Move(*datastore.get_move(self.cov_2))

        #STAB moves                             
        self.stab_options=[Move(*i) for i in datastore.get_moves_by_type(self.type)]
        self.stab_1=random.choice(self.stab_options)
        self.stab_options.remove(self.stab_1)
        self.stab_2=random.choice(self.stab_options)                #Moves of same type as pokemon
        self.stab_options.remove(self.stab_2)                       #STAB --> Same Type Attack Bonus

        #final list of pokemon's moves
        self.moves=[self.stab_1,self.stab_2,self.cov_1,self.cov_2]

        #IV's                                      
        #Random Values between 0 and 31 which help in determining the stats of the pokemon
        self.hp_IV=random.randrange(0,32)
        self.att_IV=random.randrange(0,32)
        self.def_IV=random.randrange(0,32)
        self.spd_IV=random.randrange(0,32)
        self.spatt_IV=random.randrange(0,32)
        self.spdef_IV=random.randrange(0,32)

        #nature boosts
        self.att_b=1
        self.def_b=1
        self.spd_b=1
        self.spatt_b=1
        self.spdef_b=1

    #function to check if pokemon is fainted
    def is_fainted(self):
        return self.hpIG <= 0

    #nature boost
    def nat_b(self):
        self.att_b=self.nature.att
        self.def_b=self.nature.defe
        self.spatt_b=self.nature.spatt
        self.spdef_b=self.nature.spdef
        self.spd_b=self.nature.spd

    #calculating stats
    def calc_stats(self):

        #calculating stats
        #for hp --> 3*base+0.15*IV*lvl/50+1
        #for others --> 2*base+0.1*IV*lvl/50

        self.hp=math.ceil((self.base_hp*3+0.15*self.hp_IV*self.lvl/50)+1)
        self.att=math.ceil((self.base_att*2+0.1*self.att_IV)*self.att_b*self.lvl/50)
        self.defe=math.ceil((self.base_def*2+0.1*self.def_IV)*self.def_b*self.lvl/50)
        self.spd=math.ceil((self.base_spd*2+0.1*self.spd_IV)*self.spd_b*self.lvl/50)
        self.spatt=math.ceil((self.base_spatt*2+0.1*self.spatt_IV)*self.spatt_b*self.lvl/50)
        self.spdef=math.ceil((self.base_spdef*2+0.1*self.spdef_IV)*self.spdef_b*self.lvl/50)

        #variable for hp in battle
        self.hpIG=self.hp               #hp --> Hit Points

        #adding stats to list
        self.stats=[self.hp,self.att,self.defe,self.spd,self.spatt,self.spdef]
