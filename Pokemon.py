#importing modules
import random
import math
from moves import *
import mysql.connector

#list of natures
list_nat=["lonely (+att -defe)","brave (+att -spd)","adamant (+att -spatt)","naughty (+att -spdef)",
         "bold (+defe -att)","relaxed (+defe -spd)","impish (+defe -spatt)","lax (+defe -spdef)",
         "timid (+spd -att)","hasty (+spd -defe)","jolly (+spd -spatt)","naive (+spd -spdef)",
         "modest (+spatt -att)","mild (+spatt -defe)","quiet (+spatt -spd)","rash (+spatt -spdef)",
         "calm (+spdef -att)","gentle (+spdef -defe)","sassy (+spdef -spd)","careful (+spdef -spatt)",
         "bashful (neutral)"]

#pokemon class
class Pokemon:
    def __init__(self,name): #1 parameter name

        self.name=name

        # # Connect to MySQL database
        # database = mysql.connector.connect(
        #     host="localhost",
        #     user="root",
        #     password="Sahaj@1234",
        #     database="pokemon_game"  # Ensure this matches your database name
        # )

        # cur = database.cursor()

        # # Query to fetch all natures
        # nature_query = "SELECT name, att, defe, spatt, spdef, spd FROM Nature;"
        # cur.execute(nature_query)

        # # Fetch results
        # results = cur.fetchall()

        # list_nat=[]
        # for i in results:
        #     list_nat.append(i)
    
        # # Close the connection
        # cur.close()
        # database.close()

        # data2=mysql.connector.connect(
        #     host="localhost",
        #     user="root",
        #     password="Sahaj@1234",
        #     database="pokemon_game"
        # )
        # cur=data2.cursor()

        # pokemon_query = "SELECT * FROM pokemon WHERE name = %s"
        # cur.execute(pokemon_query, (self.name,))
        # pokemon=list(cur.fetchall()[0])              

        #selecting random nature
        self.nature=random.choice(list_nat)

        #list of moves
        self.moves=[]
        self.stab_options=[]

        self.hp_dif=0

        self.accuracy=100

        #IV's
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

        #Flamey stats and moves
        if self.name=="Flamey":
            self.type="fire"
            self.lvl=50
            self.base_hp=70
            self.base_att=100   
            self.base_def=75
            self.base_spd=80
            self.base_spatt=100
            self.base_spdef=75

            self.stab_options=["Flamethrower","Fire Blast","Fire Punch",
                              "Flare Blitz","Fire Fang","Heat Wave","Lava Plume"]
            
            self.stab_move_1=random.choice(self.stab_options)
            self.stab_options.remove(self.stab_move_1)
            self.stab_move_2=random.choice(self.stab_options)
            self.stab_options.remove(self.stab_move_2)

            self.moves=[
                moves[self.stab_move_1],
                moves[self.stab_move_2],
                moves["Psychic"],
                moves["Earthquake"]
            ]

        #bubbly  
        elif self.name=="Bubbly":
            self.type="water"
            self.lvl=50
            self.base_hp=100
            self.base_att=70
            self.base_def=90
            self.base_spd=60
            self.base_spatt=100
            self.base_spdef=80

            self.stab_options=["Surf","Crabhammer","Hydro Pump",
                              "Liquidation","Muddy Water","Scald","Waterfall"]
            
            self.stab_move_1=random.choice(self.stab_options)
            self.stab_options.remove(self.stab_move_1)
            self.stab_move_2=random.choice(self.stab_options)
            self.stab_options.remove(self.stab_move_2)

            self.moves=[
                moves[self.stab_move_1],
                moves[self.stab_move_2],
                moves["Dual Wingbeat"],
                moves["Ice Beam"]
            ]
        
        #leafy
        elif self.name=="Leafy":
            self.type="grass"
            self.lvl=50
            self.base_hp=70
            self.base_att=75
            self.base_def=65
            self.base_spd=110   
            self.base_spatt=100
            self.base_spdef=80

            self.stab_options=["Energy Ball","Seed Bomb",
                              "Giga Drain","Leaf Storm","Leaf Blade"]
            
            self.stab_move_1=random.choice(self.stab_options)
            self.stab_options.remove(self.stab_move_1)
            self.stab_move_2=random.choice(self.stab_options)
            self.stab_options.remove(self.stab_move_2)

            self.moves=[
                moves[self.stab_move_1],
                moves[self.stab_move_2],
                moves["Dragon Claw"],
                moves["Sludge Bomb"]
            ]
        
        #zapper
        elif self.name=="Zapper":
            self.type="electric"
            self.lvl=50
            self.base_hp=60
            self.base_att=70
            self.base_def=60
            self.base_spd=120
            self.base_spatt=110
            self.base_spdef=80

            self.stab_options=["Thunderbolt","Discharge",
                              "Thunder Fang","Thunder","Thunder Punch","Wild Charge"]
            
            self.stab_move_1=random.choice(self.stab_options)
            self.stab_options.remove(self.stab_move_1)
            self.stab_move_2=random.choice(self.stab_options)
            self.stab_options.remove(self.stab_move_2)

            self.moves=[
                moves[self.stab_move_1],
                moves[self.stab_move_2],
                moves["Brick Break"],
                moves["Flash Cannon"]
            ]
        
        #icy
        elif self.name=="Icy":
            self.type="ice"
            self.lvl=50
            self.base_hp=60
            self.base_att=50
            self.base_def=80
            self.base_spd=110
            self.base_spatt=110
            self.base_spdef=100

            self.stab_options=["Ice Beam","Blizzard",
                              "Icicle Crash","Ice Fang","Ice Punch"]
            
            self.stab_move_1=random.choice(self.stab_options)
            self.stab_options.remove(self.stab_move_1)
            self.stab_move_2=random.choice(self.stab_options)
            self.stab_options.remove(self.stab_move_2)

            self.moves=[
                moves[self.stab_move_1],
                moves[self.stab_move_2],
                moves["Crunch"],
                moves["Moonblast"]
            ]
        
        #dracomenace
        elif self.name=="Dracomenace":
            self.type="dragon"
            self.lvl=50
            self.base_hp=80
            self.base_att=120
            self.base_def=80
            self.base_spd=80
            self.base_spatt=60
            self.base_spdef=80

            self.stab_options=["Dragon Claw","Dragon Breath","Draco Meteor","Dragon Pulse",
                              "Outrage","Dragon Tail","Dual Chop"]
            
            self.stab_move_1=random.choice(self.stab_options)
            self.stab_options.remove(self.stab_move_1)
            self.stab_move_2=random.choice(self.stab_options)
            self.stab_options.remove(self.stab_move_2)

            self.moves=[
                moves[self.stab_move_1],
                moves[self.stab_move_2],
                moves["Earthquake"],
                moves["Flamethrower"]
            ]
        
        #groundian
        elif self.name=="Groundian":
            self.type="ground"
            self.lvl=50
            self.base_hp=90
            self.base_att=140
            self.base_def=80
            self.base_spd=80
            self.base_spatt=60
            self.base_spdef=100

            self.stab_options=["Earthquake","Dig","Bulldoze",
                              "Earth Power","Stomping Tantrum","High Horsepower"]
            
            self.stab_move_1=random.choice(self.stab_options)
            self.stab_options.remove(self.stab_move_1)
            self.stab_move_2=random.choice(self.stab_options)
            self.stab_options.remove(self.stab_move_2)

            self.moves=[
                moves[self.stab_move_1],
                moves[self.stab_move_2],
                moves["Dark Pulse"],
                moves["Rock Slide"]
            ]

        #stoney
        elif self.name=="Stoney":
            self.type="rock"
            self.lvl=50
            self.base_hp=90
            self.base_att=100
            self.base_def=120
            self.base_spd=60
            self.base_spatt=50
            self.base_spdef=80

            self.stab_options=["Rock Slide","Stone Edge","Power Gem",
                              "Ancient Power","Head Smash"]
            
            self.stab_move_1=random.choice(self.stab_options)
            self.stab_options.remove(self.stab_move_1)
            self.stab_move_2=random.choice(self.stab_options)
            self.stab_options.remove(self.stab_move_2)

            self.moves=[
                moves[self.stab_move_1],
                moves[self.stab_move_2],
                moves["Body Slam"],
                moves["Earthquake"]
            ]
        
        #metaleon
        elif self.name=="Metaleon":
            self.type="steel"
            self.lvl=50
            self.base_hp=130
            self.base_att=80
            self.base_def=100
            self.base_spd=50
            self.base_spatt=70
            self.base_spdef=80

            self.stab_options=["Flash Cannon","Iron Head","Smart Strike",
                              "Meteor Mash","Mirror Shot","Steel Wing"]
            
            self.stab_move_1=random.choice(self.stab_options)
            self.stab_options.remove(self.stab_move_1)
            self.stab_move_2=random.choice(self.stab_options)
            self.stab_options.remove(self.stab_move_2)

            self.moves=[
                moves[self.stab_move_1],
                moves[self.stab_move_2],
                moves["Dragon Pulse"],
                moves["Earthquake"]
            ]
        
        #chunky
        elif self.name=="Chunky":
            self.type="normal"
            self.lvl=50
            self.base_hp=130
            self.base_att=100
            self.base_def=100
            self.base_spd=20
            self.base_spatt=20
            self.base_spdef=130

            self.stab_options=["Body Slam","Headbutt","Strength",
                              "Hyper Voice","Hyper Beam","Explosion"]
            
            self.stab_move_1=random.choice(self.stab_options)
            self.stab_options.remove(self.stab_move_1)
            self.stab_move_2=random.choice(self.stab_options)
            self.stab_options.remove(self.stab_move_2)

            self.moves=[
                moves[self.stab_move_1],
                moves[self.stab_move_2],
                moves["Ice Punch"],
                moves["Flamethrower"]
            ]
        
        #misteon
        elif self.name=="Misteon":
            self.type="fairy"
            self.lvl=50
            self.base_hp=60
            self.base_att=60
            self.base_def=80
            self.base_spd=100
            self.base_spatt=120
            self.base_spdef=80

            self.stab_options=["Moonblast","Dazzling Gleam","Play Rough",
                              "Spirit Break","Misty Explosion"]
            
            self.stab_move_1=random.choice(self.stab_options)
            self.stab_options.remove(self.stab_move_1)
            self.stab_move_2=random.choice(self.stab_options)
            self.stab_options.remove(self.stab_move_2)

            self.moves=[
                moves[self.stab_move_1],
                moves[self.stab_move_2],
                moves["Shadow Ball"],
                moves["Psychic"]
            ]
        
        #fisty
        elif self.name=="Fisty":
            self.type="fighting"
            self.lvl=50
            self.base_hp=55
            self.base_att=140
            self.base_def=95
            self.base_spd=70
            self.base_spatt=65
            self.base_spdef=75

            self.stab_options=["Brick Break","Aura Sphere","Close Combat",
                              "Cross Chop","Focus Blast","Superpower"]
            
            self.stab_move_1=random.choice(self.stab_options)
            self.stab_options.remove(self.stab_move_1)
            self.stab_move_2=random.choice(self.stab_options)
            self.stab_options.remove(self.stab_move_2)

            self.moves=[
                moves[self.stab_move_1],
                moves[self.stab_move_2],
                moves["Earth Power"],
                moves["Rock Slide"]
            ]

        #nasty
        elif self.name=="Nasty":
            self.type="dark"
            self.lvl=50
            self.base_hp=70
            self.base_att=90
            self.base_def=80
            self.base_spd=90
            self.base_spatt=80
            self.base_spdef=90

            self.stab_options=["Dark Pulse","Knock Off","Crunch",
                              "Night Slash","Sucker Punch","Throat Chop"]
            
            self.stab_move_1=random.choice(self.stab_options)
            self.stab_options.remove(self.stab_move_1)
            self.stab_move_2=random.choice(self.stab_options)
            self.stab_options.remove(self.stab_move_2)

            self.moves=[
                moves[self.stab_move_1],
                moves[self.stab_move_2],
                moves["X-Scissor"],
                moves["Shadow Ball"]
            ]
        
        #brainy
        elif self.name=="Brainy":
            self.type="psychic"
            self.lvl=50
            self.base_hp=60
            self.base_att=50
            self.base_def=60
            self.base_spd=70
            self.base_spatt=140
            self.base_spdef=120

            self.stab_options=["Psychic","Psyche Punch",
                              "Psyshock","Psycho Cut"]
            
            self.stab_move_1=random.choice(self.stab_options)
            self.stab_options.remove(self.stab_move_1)
            self.stab_move_2=random.choice(self.stab_options)
            self.stab_options.remove(self.stab_move_2)

            self.moves=[
                moves[self.stab_move_1],
                moves[self.stab_move_2],
                moves["Strength"],
                moves["Moonblast"]
            ]
        
        #spooky
        elif self.name=="Spooky":
            self.type="ghost"
            self.lvl=50
            self.base_hp=90
            self.base_att=80
            self.base_def=90
            self.base_spd=70
            self.base_spatt=90
            self.base_spdef=80

            self.stab_options=["Shadow Ball","Shadow Claw","Hex","Shadow Punch",
                              "Poltergeist"]
            
            self.stab_move_1=random.choice(self.stab_options)
            self.stab_options.remove(self.stab_move_1)
            self.stab_move_2=random.choice(self.stab_options)
            self.stab_options.remove(self.stab_move_2)

            self.moves=[
                moves[self.stab_move_1],
                moves[self.stab_move_2],
                moves["Play Rough"],
                moves["Ice Beam"]
            ]
        
        #birdy
        elif self.name=="Birdy":
            self.type="flying"
            self.lvl=50
            self.base_hp=70
            self.base_att=100
            self.base_def=80
            self.base_spd=110
            self.base_spatt=60
            self.base_spdef=80  

            self.stab_options=["Brave Bird","Air Slash",
                              "Fly","Drill Peck","Hurricane","Dual Wingbeat"]
            
            self.stab_move_1=random.choice(self.stab_options)
            self.stab_options.remove(self.stab_move_1)
            self.stab_move_2=random.choice(self.stab_options)
            self.stab_options.remove(self.stab_move_2)

            self.moves=[
                moves[self.stab_move_1],
                moves[self.stab_move_2],
                moves["Close Combat"],
                moves["Earthquake"]
            ]
        
        #Beetlebug
        elif self.name=="Beetlebug":
            self.type="bug"
            self.lvl=50
            self.base_hp=80
            self.base_att=90
            self.base_def=70
            self.base_spd=90
            self.base_spatt=70
            self.base_spdef=100

            self.stab_options=["X-Scissor","Bug Buzz","Leech Life",
                              "Megahorn","Lunge"]
            
            self.stab_move_1=random.choice(self.stab_options)
            self.stab_options.remove(self.stab_move_1)
            self.stab_move_2=random.choice(self.stab_options)
            self.stab_options.remove(self.stab_move_2)

            self.moves=[
                moves[self.stab_move_1],
                moves[self.stab_move_2],
                moves["Stone Edge"],
                moves["Sludge Bomb"]
            ]

        #Sludgemound
        elif self.name=="Sludgemound":
            self.type="poison"
            self.lvl=50
            self.base_hp=60 
            self.base_att=110
            self.base_def=80
            self.base_spd=70    
            self.base_spatt=100
            self.base_spdef=80

            self.stab_options=["Sludge Bomb","Poison Jab","Sludge Wave","Gunk Shot",
                              "Cross Poison"]
            
            self.stab_move_1=random.choice(self.stab_options)
            self.stab_options.remove(self.stab_move_1)
            self.stab_move_2=random.choice(self.stab_options)
            self.stab_options.remove(self.stab_move_2)

            self.moves=[
                moves[self.stab_move_1],
                moves[self.stab_move_2],
                moves["Dark Pulse"],
                moves["Earthquake"]
            ]

    def is_fainted(self):
        return self.hpIG <= 0

    #nature boost
    def nat_b(self):
        # self.nature=list(self.nature)
        # self.att_b=self.nature[1]
        # self.def_b=self.nature[2]
        # self.spatt_b=self.nature[3]
        # self.spdef_b=self.nature[4]
        # self.spd_b=self.nature[5]
        if self.nature=="lonely (+att -defe)":
            self.att_b=1.2
            self.def_b=0.8
            
        elif self.nature=="brave (+att -spd)":
            self.att_b=1.2
            self.spd_b=0.8

        elif self.nature=="adamant (+att -spatt)":
            self.att_b=1.2
            self.spatt_b=0.8
        
        elif self.nature=="naughty (+att -spdef)":
            self.att_b=1.2
            self.spdef_b=0.8

        elif self.nature=="bold (+defe -att)":
            self.def_b=1.2
            self.att_b=0.8
        
        elif self.nature=="relaxed (+defe -spd)":
            self.def_b=1.2
            self.spd_b=0.8
        
        elif self.nature=="impish (+defe -spatt)":
            self.def_b=1.2
            self.spatt_b=0.8
        
        elif self.nature=="lax (+defe -spdef)":
            self.def_b=1.2
            self.spdef_b=0.8
        
        elif self.nature=="timid (+spd -att)":
            self.spd_b=1.2
            self.att_b=0.8

        elif self.nature=="hasty (+spd -defe)":
            self.spd_b=1.2
            self.def_b=0.8

        elif self.nature=="jolly (+spd -spatt)":
            self.spd_b=1.2
            self.spatt_b=0.8

        elif self.nature=="naive (+spd -spdef)":
            self.spd_b=1.2
            self.spdef_b=0.8
        
        elif self.nature=="modest (+spatt -att)":
            self.spatt_b=1.2
            self.att_b=0.8

        elif self.nature=="mild (+spatt -defe)":
            self.spatt_b=1.2
            self.def_b=0.8

        elif self.nature=="quiet (+spatt -spd)":
            self.spatt_b=1.2
            self.spd_b=0.8

        elif self.nature=="rash (+spatt -spdef)":
            self.spatt_b=1.2
            self.spdef_b=0.8
        
        elif self.nature=="calm (+spdef -att)":
            self.spdef_b=1.2
            self.att_b=0.8
        
        elif self.nature=="gentle (+spdef -defe)":
            self.spdef_b=1.2
            self.def_b=0.8
        
        elif self.nature=="sassy (+spdef -spd)":
            self.spdef_b=1.2
            self.spd_b=0.8
        
        elif self.nature=="careful (+spdef -spatt)":
            self.spdef_b=1.2
            self.spatt_b=0.8


    #calculating stats
    def calc_stats(self):
        self.hp=math.ceil((self.base_hp*3+0.15*self.hp_IV*self.lvl/50)+1)
        self.att=math.ceil((self.base_att*2+0.1*self.att_IV)*self.att_b*self.lvl/50)
        self.defe=math.ceil((self.base_def*2+0.1*self.def_IV)*self.def_b*self.lvl/50)
        self.spd=math.ceil((self.base_spd*2+0.1*self.spd_IV)*self.spd_b*self.lvl/50)
        self.spatt=math.ceil((self.base_spatt*2+0.1*self.spatt_IV)*self.spatt_b*self.lvl/50)
        self.spdef=math.ceil((self.base_spdef*2+0.1*self.spdef_IV)*self.spdef_b*self.lvl/50)

        self.hpIG=self.hp
        self.attIG=self.att
        self.defeIG=self.defe
        self.spdIG=self.spd
        self.spattIG=self.spatt
        self.spdefIG=self.spdef

        #adding stats to list
        self.stats=[self.hp,self.att,self.defe,self.spd,self.spatt,self.spdef]
