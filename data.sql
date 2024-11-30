--Renewing Database
drop database if exists pokemon_game;
create database pokemon_game;  
use pokemon_game;

--Strength table of the form (strong, weak)
--all possible combinations are listed here for considering type effectiveness
CREATE TABLE Strengths (
    strong VARCHAR(255),
    weak VARCHAR(255)
);

--inserting the values
INSERT INTO Strengths (strong, weak) VALUES
('fire','grass'),
('fire','ice'),
('fire','steel'),
('fire','fairy'),
('water','fire'),
('water','ice'),
('water','ground'),
('water','rock'),
('grass','water'),
('grass','electric'),
('grass','ground'),
('grass','rock'),
('electric','water'),
('electric','steel'),
('electric','flying'),
('ice','grass'),
('ice','dragon'),
('ice','ground'),
('ice','flying'),
('dragon','fire'),
('dragon','water'),
('dragon','grass'),
('dragon','electric'),
('ground','fire'),
('ground','electric'),
('ground','rock'),
('ground','steel'),
('rock','fire'),
('rock','ice'),
('rock','normal'),
('rock','flying'),
('steel','ice'),
('steel','dragon'),
('steel','rock'),
('steel','normal'),
('steel','fairy'),
('normal',''),
('normal','rock'),
('normal','steel'),
('normal','fighting'),
('normal','ghost'),
('fairy','dragon'),
('fairy','fighting'),
('fairy','dark'),
('fighting','ice'),
('fighting','rock'),
('fighting','steel'),
('fighting','normal'),
('fighting','dark'),
('dark','psychic'),
('dark','ghost'),
('psychic','fighting'),
('psychic','poison'),
('ghost','normal'),
('ghost','fairy'),
('ghost','fighting'),
('ghost','psychic'),
('ghost','bug'),
('ghost','poison'),
('flying','grass'),
('flying','ground'),
('flying','fighting'),
('flying','bug'),
('bug','grass'),
('bug','rock'),
('bug','fighting'),
('bug','dark'),
('bug','psychic'),
('poison','grass'),
('poison','fairy'),
('poison','fighting');


--Moves table of the form (move_id, name, type, power, contact, accuracy)
CREATE TABLE Moves (
    move_id INT PRIMARY KEY AUTO_INCREMENT,     --auto incrementing move_id
    name VARCHAR(20),
    type VARCHAR(20),
    power INT,
    contact VARCHAR(20),
    accuracy INT
);

--inserting the values
INSERT INTO Moves (name, type, power, contact, accuracy) VALUES
    ("Flamethrower", "fire", 90, "special", 95),
    ("Fire Blast", "fire", 110, "special", 85),
    ("Fire Punch", "fire", 75, "physical", 95),
    ("Flare Blitz", "fire", 120, "physical", 85),           --fire type moves
    ("Fire Fang", "fire", 65, "physical", 90),
    ("Heat Wave", "fire", 95, "special", 90),
    ("Lava Plume", "fire", 80, "special", 95),

    ("Surf", "water", 90, "special", 95),
    ("Crabhammer", "water", 100, "physical", 90),
    ("Hydro Pump", "water", 110, "special", 80),
    ("Liquidation", "water", 85, "physical", 95),       --water type moves
    ("Muddy Water", "water", 90, "special", 85),
    ("Scald", "water", 80, "special", 95),
    ("Waterfall", "water", 80, "physical", 95),

    ("Energy Ball", "grass", 90, "special", 95),
    ("Seed Bomb", "grass", 80, "physical", 95),
    ("Giga Drain", "grass", 75, "special", 95),         --grass type moves
    ("Leaf Blade", "grass", 90, "physical", 95),
    ("Leaf Storm", "grass", 130, "special", 80),

    ("Thunderbolt", "electric", 90, "special", 95),
    ("Discharge", "electric", 80, "special", 95),
    ("Thunder Fang", "electric", 65, "physical", 90),       --electric type moves
    ("Thunder", "electric", 110, "special", 70),
    ("Thunder Punch", "electric", 75, "physical", 95),
    ("Wild Charge", "electric", 90, "physical", 90),

    ("Ice Beam", "ice", 90, "special", 95),
    ("Blizzard", "ice", 110, "special", 70),
    ("Icicle Crash", "ice", 80, "physical", 90),        --ice type moves
    ("Ice Fang", "ice", 65, "physical", 90),
    ("Ice Punch", "ice", 75, "physical", 95),

    ("Dragon Claw", "dragon", 80, "physical", 95),
    ("Dragon Breath", "dragon", 60, "special", 95),
    ("Draco Meteor", "dragon", 130, "special", 85),
    ("Dragon Pulse", "dragon", 85, "special", 95),          --dragon type moves
    ("Outrage", "dragon", 120, "physical", 90),
    ("Dragon Tail", "dragon", 60, "physical", 90),
    ("Dual Chop", "dragon", 80, "physical", 95),

    ("Earthquake", "ground", 100, "physical", 95),
    ("Dig", "ground", 60, "physical", 95),
    ("Bulldoze", "ground", 60, "physical", 95),      --ground type moves
    ("Earth Power", "ground", 80, "special", 95),
    ("Stomping Tantrum", "ground", 75, "physical", 95),
    ("High Horsepower", "ground", 95, "physical", 90),

    ("Rock Slide", "rock", 75, "physical", 90),
    ("Stone Edge", "rock", 100, "physical", 80),
    ("Power Gem", "rock", 80, "special", 95),       --rock type moves
    ("Ancient Power", "rock", 60, "special", 95),
    ("Head Smash", "rock", 150, "physical", 80),

    ("Flash Cannon", "steel", 80, "special", 95),
    ("Iron Head", "steel", 80, "physical", 95),
    ("Smart Strike", "steel", 70, "physical", 100),     --steel type moves
    ("Meteor Mash", "steel", 100, "physical", 85),
    ("Mirror Shot", "steel", 65, "special", 95),
    ("Steel Wing", "steel", 70, "physical", 95),

    ("Body Slam", "normal", 80, "physical", 95),
    ("Headbutt", "normal", 70, "physical", 95),
    ("Strength", "normal", 80, "physical", 95),             --normal type moves
    ("Hyper Voice", "normal", 90, "special", 95),
    ("Hyper Beam", "normal", 150, "special", 90),
    ("Explosion", "normal", 200, "physical", 95),

    ("Moonblast", "fairy", 95, "special", 95),
    ("Dazzling Gleam", "fairy", 80, "special", 95),
    ("Play Rough", "fairy", 90, "physical", 90),                --fairy type moves
    ("Spirit Break", "fairy", 75, "physical", 95),
    ("Misty Explosion", "fairy", 100, "physical", 95),

    ("Brick Break", "fighting", 75, "physical", 95),
    ("Aura Sphere", "fighting", 80, "special", 100),
    ("Close Combat", "fighting", 120, "physical", 90),          --fighting type moves
    ("Cross Chop", "fighting", 100, "physical", 80),
    ("Focus Blast", "fighting", 120, "special", 70),
    ("Superpower", "fighting", 120, "physical", 85),

    ("Dark Pulse", "dark", 80, "special", 95),
    ("Knock Off", "dark", 65, "physical", 95),
    ("Crunch", "dark", 80, "physical", 95),             --dark type moves
    ("Night Slash", "dark", 70, "physical", 95),
    ("Sucker Punch", "dark", 70, "physical", 95),
    ("Throat Chop", "dark", 80, "physical", 95),

    ("Psychic", "psychic", 90, "special", 95),
    ("Psybeam", "psychic", 65, "special", 95),
    ("Psyche Punch", "psychic", 90, "physical", 95),    --psychic type moves
    ("Psyshock", "psychic", 80, "special", 95),
    ("Psycho Cut", "psychic", 70, "physical", 95),

    ("Shadow Ball", "ghost", 80, "special", 95),
    ("Shadow Claw", "ghost", 65, "physical", 90),
    ("Hex", "ghost", 65, "special", 95),                    --ghost type moves
    ("Shadow Punch", "ghost", 75, "physical", 95),
    ("Poltergeist", "ghost", 110, "physical", 85),

    ("Brave Bird", "flying", 120, "physical", 90),
    ("Air Slash", "flying", 75, "special", 95),
    ("Fly", "flying", 90, "physical", 85),          --flying type moves
    ("Drill Peck", "flying", 80, "physical", 95),
    ("Hurricane", "flying", 110, "special", 70),
    ("Dual Wingbeat", "flying", 80, "physical", 80),

    ("X-Scissor", "bug", 80, "physical", 95),
    ("Bug Buzz", "bug", 90, "special", 95),
    ("Leech Life", "bug", 80, "physical", 95),          --bug type moves
    ("Megahorn", "bug", 120, "physical", 85),
    ("Lunge", "bug", 80, "special", 95),

    ("Sludge Bomb", "poison", 90, "special", 95),
    ("Poison Jab", "poison", 80, "physical", 95),
    ("Sludge Wave", "poison", 95, "special", 90),               --poison type moves
    ("Gunk Shot", "poison", 120, "physical", 80),   
    ("Cross Poison", "poison", 70, "physical", 95);

--Pokemon table of the form (pokemon_id, cov_1, cov_2, hp, att, defe, spatt, spdef, spd, type, name)
CREATE TABLE Pokemon (
    pokemon_id INT PRIMARY KEY AUTO_INCREMENT,
    cov_1 INT NOT NULL,             --move id for coverage move 1
    cov_2 INT NOT NULL,             --move id for coverage move 2
    hp INT,
    att INT,
    defe INT,                       --stats of the pokemon
    spatt INT,
    spdef INT,
    spd INT,
    type VARCHAR(20),
    FOREIGN KEY (cov_1) REFERENCES Moves(move_id),          
    FOREIGN KEY (cov_2) REFERENCES Moves(move_id),
    Name varchar(30)
);

--inserting the values
INSERT INTO Pokemon (cov_1, cov_2, hp, att, defe, spatt, spdef, spd, type,name) VALUES
    (38, 78, 80, 75, 70, 100, 95, 110, 'fire','Flamey'),
    (26,55, 100, 70, 110, 80, 100, 70, 'water', "Bubbly"),
    (99,31, 75, 85, 100, 85, 105, 80, 'grass','Leafy'),
    (66, 49, 60, 70, 60, 130, 50, 140, 'electric', "Zapper"),
    (74, 61, 60, 50, 80, 110, 100, 110, 'ice',"Icy"),
    (38, 1, 80, 130, 80, 100, 80, 80, 'dragon',"Dracomenace"),
    (72, 44, 90, 140, 80, 60, 100, 80, 'ground',"Groundian"),
    (55,38,70,105,140,50,90,55,"rock","Stoney"),
    (34,38, 130, 80, 100, 70, 80, 50, 'steel',"Metaleon"),
    (30, 1, 140, 80, 100, 65, 85, 40, 'normal',"Chunky"),
    (83, 78, 80, 75, 85, 110, 100, 100, 'fairy',"Misteon"),
    (41, 44, 45, 150, 120, 30, 80, 85, 'fighting',"Fisty"),
    (94, 83, 100, 80, 60, 80, 60, 130, 'dark',"Nasty"),
    (57, 61, 50, 40, 60, 150, 110, 100, 'psychic',"Brainy"),
    (63,26 , 80, 90, 50, 90, 100, 100, 'ghost','Spooky'),
    (68, 38, 100, 110, 80, 75, 75, 70, 'flying','Birdy'),
    (45,99, 100, 80, 60, 80, 60, 130, 'bug',"Beetlebug"),
    (72, 38, 70, 105, 70, 100, 70, 95, 'poison',"Sludgemound");

--Nature table of the form (nature_id, name, att, defe, spatt, spdef, spd)
create table Nature (
  nature_id int primary key auto_increment,     --auto incrementing nature_id
  name varchar(20),
  att float,
  defe float,
  spatt float,              --provide stat multipliers determined by nature
  spdef float,              --values - 1.2,1,0.8
  spd float
);

--inserting the values
insert into Nature (name, att, defe, spatt, spdef, spd) values
("lonely",1.2,0.8,1,1,1),
("brave",1.2,1,1,1,0.8),
("adamant",1.2,1,0.8,1,1),
("naughty",1.2,1,1,0.8,1),
("bold",0.8,1.2,1,1,1),
("relaxed",1,1.2,1,1,0.8),
("impish",1,1.2,0.8,1,1),
("lax",1,1.2,1,0.8,1),
("timid",0.8,1,1,1,1.2),
("hasty",1,0.8,1,1,1.2),
("jolly",1,1,0.8,1,1.2),
("naive",1,1,1,0.8,1.2),
("modest",0.8,1,1.2,1,1),
("mild",1,0.8,1.2,1,1),
("quiet",1,1,1.2,1,0.8),
("rash",1,1,1.2,0.8,1),
("calm",0.8,1,1,1.2,1),
("gentle",1,0.8,1,1.2,1),
("sassy",1,1,1,1.2,0.8),
("careful",1,1,0.8,1.2,1);







