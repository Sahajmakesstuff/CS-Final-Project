import tkinter as tk
import random
from tkinter import ttk
import math
from Pokemon import *
from moves import *
# import mysql.connector

wins=0

# Define a dictionary for move types and their corresponding colors
MOVE_TYPE_COLORS = {
    "electric": "#FFD700",  # Gold
    "normal": "#A8A77A",    # Light Brown
    "steel": "#B7B7CE",     # Gray
    "fire": "#EE8130",      # Orange Red
    "water": "#6390F0",     # Light Blue
    "grass": "#7AC74C",     # Light Green
    "ice": "#96D9D6",       # Light Cyan
    "fighting": "#C22E28",  # Red
    "poison": "#A33EA1",    # Purple
    "ground": "#E2BF65",    # Brown
    "flying": "#A98FF3",    # Light Purple
    "psychic": "#F95587",   # Pink
    "bug": "#A6B91A",       # Olive Green
    "rock": "#B6A136",      # Brownish Yellow
    "ghost": "#735797",     # Dark Purple
    "dragon": "#6F35FC",    # Dark Purple
    "dark": "#705746",      # Dark Brown
    "fairy": "#D685AD",     # Pinkish Purple
}

# # Connect to MySQL database
# database = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="Sahaj@1234",
#     # database="pokemon_game"  # Use the target database directly if needed
# )

# cur = database.cursor()

# # Step 2: Load the SQL file
# with open(r"D:\Sahaj PYQs\CS-Final-Project-main\data.sql", "r") as file:
#     sql_script = file.read()

# # Split the SQL script into individual statements and execute
# for statement in sql_script.split(';'):
#     if statement.strip():  # Skip empty statements
#         cur.execute(statement)

# # Step 3: Fetch data from the 'pokemon' table
# pokemon_query = "SELECT name FROM pokemon;"
# cur.execute(pokemon_query)
# opp = cur.fetchall()

# # Prepare the opponents list
# opponents = [i[0] for i in opp]
# print("Opponents:", opponents)

# cur.close()
# database.close()

opponents=["Flamey","Bubbly","Leafy","Zapper","Icy","Dracomenace","Groundian","Stoney","Metaleon","Chunky",
           "Misteon","Fisty","Nasty","Brainy","Spooky","Birdy","Beetlebug","Sludgemound"]

class Mainframe:
    def __init__(self, root):
        self.root = root
        self.root.title("Pokemon Battle Simulator")
        self.root.geometry("1000x800")
        self.root.configure(bg="#F0F8FF")
        self.splash_screen()

    def splash_screen(self):
        self.battles_left = 10  # Max of 10 battles
        opponents=["Flamey","Bubbly","Leafy","Zapper","Icy","Dracomenace","Groundian","Stoney","Metaleon","Chunky",
           "Misteon","Fisty","Nasty","Brainy","Spooky","Birdy","Beetlebug","Sludgemound"]
        self.available_opponents = opponents[:]  # Create a list of available opponents
        self.player_pokemon = None
        self.player_lost = False

        self.splash_frame = tk.Frame(self.root, bg="#F0F8FF")
        self.splash_frame.pack(expand=True)

        welcome_label = tk.Label(self.splash_frame, text="Welcome to the Pokémon Battle Simulator", font=("Helvetica", 24, "bold"), bg="#F0F8FF")
        welcome_label.pack(pady=20)

        start_button = tk.Button(self.splash_frame, text="Start", font=("Helvetica", 16), command=self.show_starter_selection, bg="#87CEEB")
        start_button.pack(pady=20)

    def show_starter_selection(self):
        self.splash_frame.pack_forget()
        self.selection_frame = tk.Frame(self.root, bg="#F0F8FF")
        self.selection_frame.pack(expand=True)

        label = tk.Label(self.selection_frame, text="Choose Your Starter Pokémon", font=("Helvetica", 18), bg="#F0F8FF")
        label.pack(pady=10)
        
        self.starter_options=[]

        opponents_dummy=opponents

        for i in range(3):
            mon=random.choice(opponents_dummy)
            self.starter_options.append(mon)
            opponents_dummy.remove(mon)

        for idx, starter in enumerate(self.starter_options):
            button = tk.Button(self.selection_frame, text=starter, font=("Helvetica", 16),
                               command=lambda idx=idx: self.choose_starter(idx), bg="#87CEEB")
            button.pack(pady=5)
    
    def choose_starter(self, idx):
        chosen_starter = self.starter_options[idx]
        self.player_pokemon = Pokemon(chosen_starter)
        self.player_pokemon.nat_b()
        self.player_pokemon.calc_stats()
        self.available_opponents.remove(chosen_starter)  # Remove chosen starter from available opponents

        self.selection_frame.pack_forget()
        self.show_battle_screen()
    
    def show_battle_screen(self):
        self.battle_frame = tk.Frame(self.root, bg="#F0F8FF")
        self.battle_frame.pack(expand=True)

        opponents=["Flamey","Bubbly","Leafy","Zapper","Icy","Dracomenace","Groundian","Stoney","Metaleon","Chunky",
           "Misteon","Fisty","Nasty","Brainy","Spooky","Birdy","Beetlebug","Sludgemound"]
        opponents.remove(self.player_pokemon.name)
        self.available_opponents = opponents[:]  # Create a list of available opponents

        # Randomly select an opponent Pokémon that hasn't been used yet
        if len(self.available_opponents) > 0:
            opponent_data = random.choice(self.available_opponents)
            self.available_opponents.remove(opponent_data)  # Remove this opponent from available list
        else:
            # If no opponents are left, end the game
            self.end_game("No more opponents available! You've won all battles!")

        self.opponent_pokemon = Pokemon(opponent_data)
        self.opponent_pokemon.nat_b()
        self.opponent_pokemon.calc_stats()

        self.battle_log = tk.Text(self.battle_frame, height=20, width=100, state=tk.DISABLED, bg="#FFFFFF")
        self.battle_log.pack(pady=10)
        
        self.player_label = tk.Label(self.battle_frame, text=f"{self.player_pokemon.name}: {self.player_pokemon.hpIG}/{self.player_pokemon.hp} HP",
                                     font=("Helvetica", 16), bg="#F0F8FF")
        self.player_label.pack(pady=5)

        self.opponent_label = tk.Label(self.battle_frame, text=f"{self.opponent_pokemon.name}: {self.opponent_pokemon.hpIG}/{self.opponent_pokemon.hp} HP",
                                       font=("Helvetica", 16), bg="#F0F8FF")
        self.opponent_label.pack(pady=5)

        self.move_buttons = []
        for move in self.player_pokemon.moves:
            button = tk.Button(self.battle_frame, text=f"{move.name} ({move.type})", font=("Helvetica", 16),
                               command=lambda move=move: self.execute_turn(move), bg=MOVE_TYPE_COLORS[move.type])
            button.pack(pady=5)
            self.move_buttons.append(button)
    
    def execute_turn(self,player_move):
        if self.player_pokemon.spd>=self.opponent_pokemon.spd:
            for button in self.move_buttons:
                button.config(state=tk.DISABLED)

            # Player's turn
            damage, critical,super_effective,not_effective = player_move.use_move(self.player_pokemon, self.opponent_pokemon)
            self.log_message(f"{self.player_pokemon.name} used {player_move.name}! It dealt {damage} damage{' (Critical Hit!)' if critical else ''}{' (Super Effective!)' if super_effective else ''}{' (Not Very Effective!)' if not_effective else ''}.")
            self.update_health_bars()

            if self.opponent_pokemon.is_fainted():
                self.log_message(f"{self.opponent_pokemon.name} fainted!")
                self.battles_left -= 1
                self.root.update()
                self.check_for_more_battles()
                return
            # else:
            #     self.root.after(1000, self.opponent_turn)
            
            opponent_move = random.choice(self.opponent_pokemon.moves)
            damage, critical,super_effective,not_effective = opponent_move.use_move(self.opponent_pokemon, self.player_pokemon)
            self.log_message(f"{self.opponent_pokemon.name} used {opponent_move.name}! It dealt {damage} damage{' (Critical Hit!)' if critical else ''}{' (Super Effective!)' if super_effective else ''}{' (Not Very Effective!)' if not_effective else ''}.")
            self.update_health_bars()

            if self.player_pokemon.is_fainted():
                self.log_message(f"{self.player_pokemon.name} fainted!")
                self.root.update()
                self.player_lost = True
                self.check_for_more_battles()
                # self.root.after(3000,self.end_game("You lost! Game Over."))
                return
            else:
                # Re-enable move buttons for the player's next turn
                for button in self.move_buttons:
                    button.config(state=tk.NORMAL)
        else:
            for button in self.move_buttons:
                button.config(state=tk.DISABLED)

            opponent_move = random.choice(self.opponent_pokemon.moves)
            damage, critical,super_effective,not_effective = opponent_move.use_move(self.opponent_pokemon, self.player_pokemon)
            self.log_message(f"{self.opponent_pokemon.name} used {opponent_move.name}! It dealt {damage} damage{' (Critical Hit!)' if critical else ''}{' (Super Effective!)' if super_effective else ''}{' (Not Very Effective!)' if not_effective else ''}.")
            self.update_health_bars()

            if self.player_pokemon.is_fainted():
                self.log_message(f"{self.player_pokemon.name} fainted!")
                self.root.update()
                self.player_lost = True
                self.check_for_more_battles()
                # self.root.after(5000,self.end_game("You lost! Game Over."))
                return
            else:
                # Re-enable move buttons for the player's next turn
                for button in self.move_buttons:
                    button.config(state=tk.NORMAL)
            
            # Player's turn
            damage, critical, super_effective,not_effective = player_move.use_move(self.player_pokemon, self.opponent_pokemon)
            self.log_message(f"{self.player_pokemon.name} used {player_move.name}! It dealt {damage} damage{' (Critical Hit!)' if critical else ''}{' (Super Effective!)' if super_effective else ''}{' (Not Very Effective!)' if not_effective else ''}.")
            self.update_health_bars()

            if self.opponent_pokemon.is_fainted():
                self.log_message(f"{self.opponent_pokemon.name} fainted!")
                self.root.update()
                self.check_for_more_battles()
                return

    def update_health_bars(self):
        self.player_label.config(text=f"{self.player_pokemon.name}: {self.player_pokemon.hpIG}/{self.player_pokemon.hp} HP")
        self.opponent_label.config(text=f"{self.opponent_pokemon.name}: {self.opponent_pokemon.hpIG}/{self.opponent_pokemon.hp} HP")

    def log_message(self, message):
        self.battle_log.config(state=tk.NORMAL)
        self.battle_log.insert(tk.END, message + "\n")
        self.battle_log.config(state=tk.DISABLED)

    def check_for_more_battles(self):
        if self.player_lost:
            self.root.after(3000,self.end_game("You lost! Game Over."))
            return

        if self.battles_left == 0:
            self.root.update()
            self.root.after(3000,self.end_game("Congratulations! You've won all 10 battles!"))  
        else:
            # Heal the player's Pokémon before the next battle
            self.heal_player_pokemon()
            # Continue to next battle after a short delay
            self.root.after(2000, self.next_battle)

    def heal_player_pokemon(self):
        self.player_pokemon.hpIG = self.player_pokemon.hp  # Restore player's Pokémon HP to max
        global wins
        wins+=1
        self.log_message(f"{self.player_pokemon.name} has been healed to full health!")

    def next_battle(self):
        # Clear the current battle screen and start a new one
        self.battle_frame.pack_forget()
        self.show_battle_screen()

    def end_game(self, message):
        # End the game and display the final message
        self.battle_frame.pack_forget()
        self.end_frame = tk.Frame(self.root, bg="#F0F8FF")
        self.end_frame.pack(expand=True)

        end_label = tk.Label(self.end_frame, text=message, font=("Helvetica", 24), bg="#F0F8FF")
        end_label.pack(pady=20)

        restart_button = tk.Button(self.end_frame, text="Restart", font=("Helvetica", 16), command=self.restart_game, bg="#87CEEB")
        restart_button.pack(pady=10)

    def restart_game(self):
        self.end_frame.pack_forget()
        self.battles_left = 10
        self.available_opponents = opponents[:]  # Reset available opponents
        self.splash_screen()
            

# Create the Tkinter root window and start the game
root = tk.Tk()
battle_gui = Mainframe(root)
root.mainloop()