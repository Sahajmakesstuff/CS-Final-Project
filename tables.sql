create table Strengths 
  (varchar(20) strong,
  varchar(20) weak);

create table Moves (
  int move_id primary key auto_increment,
  varchar(20) name,
  varchar(20) type,
  int power,
  varchar(20) contact,
  int accuracy
);

create table Pokemon (
  int pokemon_id primary key auto_increment
  int cov_1 foreign key references Moves.move_id not null
  int cov_2 foreign key references Moves.move_id not null
  ...stats
  varchar(20) type
)

create table Nature (
  int nature_id primary key auto_increment
  int att
  int spd
  .... 
)







