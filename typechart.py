#dictionary for type chart

# Strengths:

# strong weak
# fire grass
# fire isice
# fire steel
# fire fairy

# select weak from strengths where strong = "fire"
# select strong from strenghts where weak = "fire"




type_chart={
    "fire": [
        ["grass","ice","steel","fairy"],
        ["water","dragon","ground","rock"]
    ],
    "water": [
        ["fire","ice","ground","rock"],
        ["grass","electric","dragon"]
    ],
    "grass": [
        ["water","electric","ground","rock"],
        ["fire","ice","dragon","steel","flying","poison"]
    ],
    "electric": [
        ["water","steel","flying"],
        ["grass","dragon","ground"]
    ],
    "ice": [
        ["grass","dragon","ground","flying"],
        ["fire","water","rock","steel","fighting"]
    ],
    "dragon": [
        ["fire","water","grass","electric"],
        ["ice","steel","fairy"]
    ],
    "ground": [
        ["fire","electric","rock","steel"],
        ["water","grass","ice","flying"]
    ],
    "rock": [
        ["fire","ice","normal","flying"],
        ["water","grass","ground","steel","fighting"]
    ],
    "steel": [
        ["ice","dragon","rock","normal","fairy","grass","flying","bug"],
        ["fire","electric","ground","fighting"]
    ],
    "normal": [
        [],
        ["rock","steel","fighting","ghost"]
    ],
    "fairy": [                                                      
        ["dragon","fighting","dark"],                               
        ["fire","steel","ghost","poison"]                           
    ],
    "fighting": [
        ["ice","rock","steel","normal","dark"],
        ["fairy","psychic","ghost","flying","bug","poison"]
    ],
    "dark": [
        ["psychic","ghost"],
        ["fairy","fighting","bug"]
    ],
    "psychic": [
        ["fighting","poison"],
        ["dark","ghost","bug"]
    ],
    "ghost": [
        ["normal","fairy","fighting","psychic","bug","poison"],
        ["dark"]
    ],
    "flying": [
        ["grass","ground","fighting","bug"],
        ["electric","ice","rock","steel"]
    ],
    "bug": [
        ["grass","rock","fighting","dark","psychic"],
        ["fire","steel","ghost","flying","poison"]
    ],
    "poison": [
        ["grass","fairy","fighting","bug"],
        ["ground","steel","psychic","ghost"]
    ]
}