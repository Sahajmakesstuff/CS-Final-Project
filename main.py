#importing modules
import tkinter as tk
import random
import math
from Pokemon import *
from moves import *
from database import DataStore

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

#creating a database object, and getting the list of opponents and natures
datastore=DataStore()
opp=datastore.opponents_list()
natures=datastore.nature_list()
nat_list=[Nature(i) for i in natures]
opponents = [i[0] for i in opp]

#the main class
class Mainframe:
    def __init__(self, root):
        self.root = root
        self.root.title("Pokemon Battle Simulator")
        self.root.geometry("1000x800")
        self.root.configure(bg="#F0F8FF")
        self.splash_screen()

    # Splash screen to start the game
    def splash_screen(self):
        self.battles_left = 10  # Max of 10 battles
        self.available_opponents = opponents[:]  # Create a list of available opponents
        self.player_pokemon = None
        self.player_lost = False

        self.splash_frame = tk.Frame(self.root, bg="#F0F8FF")
        self.splash_frame.pack(expand=True)

        welcome_label = tk.Label(self.splash_frame, text="Welcome to the Pokémon Battle Simulator", font=("Helvetica", 24, "bold"), bg="#F0F8FF")
        welcome_label.pack(pady=20)

        start_button = tk.Button(self.splash_frame, text="Start", font=("Helvetica", 16), command=self.show_starter_selection, bg="#87CEEB")
        start_button.pack(pady=20)

    #starter selection screen
    def show_starter_selection(self):
        self.splash_frame.pack_forget()
        self.selection_frame = tk.Frame(self.root, bg="#F0F8FF")
        self.selection_frame.pack(expand=True)

        label = tk.Label(self.selection_frame, text="Choose Your Starter Pokémon", font=("Helvetica", 18), bg="#F0F8FF")
        label.pack(pady=10)
        
        self.starter_options=[] #list of starter options

        opponents_dummy=opponents[:]   #dummy list of pokemon to choose starters from

        #choosing 3 starters from the 18 available pokemon
        for i in range(3):
            mon=random.choice(opponents_dummy)
            self.starter_options.append(mon)
            opponents_dummy.remove(mon)
        
        # Create a button for each starter option
        for idx, starter in enumerate(self.starter_options):
            button = tk.Button(self.selection_frame, text=starter, font=("Helvetica", 16),
                               command=lambda idx=idx: self.choose_starter(idx), bg="#87CEEB")
            button.pack(pady=5)
    
    #choose starter function
    def choose_starter(self, idx):
        chosen_starter = self.starter_options[idx]

        #create a pokemon object for the player's pokemon
        self.player_pokemon = Pokemon(datastore,chosen_starter,nat_list)
        self.player_pokemon.nat_b()
        self.player_pokemon.calc_stats()
        self.available_opponents.remove(chosen_starter)  # Remove chosen starter from available opponents

        # Clear the selection screen and start the first battle
        self.selection_frame.pack_forget()
        self.show_battle_screen()
    
    def show_battle_screen(self):
        self.battle_frame = tk.Frame(self.root, bg="#F0F8FF")
        self.battle_frame.pack(expand=True)

        # Randomly select an opponent Pokémon that hasn't been used yet
        if len(self.available_opponents) > 0:
            opponent_data = random.choice(self.available_opponents)
            self.available_opponents.remove(opponent_data)  # Remove this opponent from available list
        else:
            # If no opponents are left, end the game
            self.end_game("No more opponents available! You've won all battles!")

        # Create a Pokémon object for the opponent
        self.opponent_pokemon = Pokemon(datastore,opponent_data,nat_list)
        self.opponent_pokemon.nat_b()
        self.opponent_pokemon.calc_stats()

        self.battle_log = tk.Text(self.battle_frame, height=20, width=100, state=tk.DISABLED, bg="#FFFFFF")
        self.battle_log.pack(pady=10)
        
        # Display the player's and opponent's Pokémon names and HP
        self.player_label = tk.Label(self.battle_frame, text=f"{self.player_pokemon.name}: {self.player_pokemon.hpIG}/{self.player_pokemon.hp} HP",
                                     font=("Helvetica", 16), bg="#F0F8FF")
        self.player_label.pack(pady=5)
        
        # Display the opponent's Pokémon name and HP
        self.opponent_label = tk.Label(self.battle_frame, text=f"{self.opponent_pokemon.name}: {self.opponent_pokemon.hpIG}/{self.opponent_pokemon.hp} HP",
                                       font=("Helvetica", 16), bg="#F0F8FF")
        self.opponent_label.pack(pady=5)

        # Create a button for each move the player's Pokémon has
        self.move_buttons = []
        for move in self.player_pokemon.moves:
            button = tk.Button(self.battle_frame, text=f"{move.name} ({move.type})", font=("Helvetica", 16),
                               command=lambda move=move: self.execute_turn(move), bg=MOVE_TYPE_COLORS[move.type])
            button.pack(pady=5)
            self.move_buttons.append(button)
    
    #main battle function
    def execute_turn(self,player_move):

        #if player's pokemon is faster
        if self.player_pokemon.spd>=self.opponent_pokemon.spd:
            for button in self.move_buttons:
                button.config(state=tk.DISABLED)    #disable move buttons for the opponent's turn

            # Player's turn
            damage, critical,super_effective,not_effective = player_move.use_move(datastore,self.player_pokemon, self.opponent_pokemon)
            self.log_message(f"{self.player_pokemon.name} used {player_move.name}! It dealt {damage} damage{' (Critical Hit!)' if critical else ''}{' (Super Effective!)' if super_effective else ''}{' (Not Very Effective!)' if not_effective else ''}.")
            self.update_health_bars()

            # Check if the opponent's Pokémon has fainted
            if self.opponent_pokemon.is_fainted():
                self.log_message(f"{self.opponent_pokemon.name} fainted!")
                self.battles_left -= 1
                self.root.update()
                self.check_for_more_battles()   #check if more battles are left
                return
            
            # Opponent's turn
            opponent_move = random.choice(self.opponent_pokemon.moves)
            damage, critical,super_effective,not_effective = opponent_move.use_move(datastore,self.opponent_pokemon, self.player_pokemon)
            self.log_message(f"{self.opponent_pokemon.name} used {opponent_move.name}! It dealt {damage} damage{' (Critical Hit!)' if critical else ''}{' (Super Effective!)' if super_effective else ''}{' (Not Very Effective!)' if not_effective else ''}.")
            self.update_health_bars()

            # Check if the player's Pokémon has fainted
            if self.player_pokemon.is_fainted():
                self.log_message(f"{self.player_pokemon.name} fainted!")
                self.root.update()
                self.player_lost = True
                self.check_for_more_battles()
                return
            else:
                # Re-enable move buttons for the player's next turn
                for button in self.move_buttons:
                    button.config(state=tk.NORMAL)
        
        #if opponent's pokemon is faster
        else:
            for button in self.move_buttons:
                button.config(state=tk.DISABLED)  # Disable move buttons for the opponent's turn

            # Opponent's turn
            opponent_move = random.choice(self.opponent_pokemon.moves)
            damage, critical,super_effective,not_effective = opponent_move.use_move(datastore,self.opponent_pokemon, self.player_pokemon)
            self.log_message(f"{self.opponent_pokemon.name} used {opponent_move.name}! It dealt {damage} damage{' (Critical Hit!)' if critical else ''}{' (Super Effective!)' if super_effective else ''}{' (Not Very Effective!)' if not_effective else ''}.")
            self.update_health_bars()

            # Check if the player's Pokémon has fainted
            if self.player_pokemon.is_fainted():
                self.log_message(f"{self.player_pokemon.name} fainted!")
                self.root.update()
                self.player_lost = True
                self.check_for_more_battles()   #check if more battles are left
                return
            else:
                # Re-enable move buttons for the player's next turn
                for button in self.move_buttons:
                    button.config(state=tk.NORMAL)
            
            # Player's turn
            damage, critical, super_effective,not_effective = player_move.use_move(datastore,self.player_pokemon, self.opponent_pokemon)
            self.log_message(f"{self.player_pokemon.name} used {player_move.name}! It dealt {damage} damage{' (Critical Hit!)' if critical else ''}{' (Super Effective!)' if super_effective else ''}{' (Not Very Effective!)' if not_effective else ''}.")
            self.update_health_bars()

            # Check if the opponent's Pokémon has fainted
            if self.opponent_pokemon.is_fainted():
                self.log_message(f"{self.opponent_pokemon.name} fainted!")
                self.root.update()
                self.check_for_more_battles()
                return

    #function to update health bars
    def update_health_bars(self):
        self.player_label.config(text=f"{self.player_pokemon.name}: {self.player_pokemon.hpIG}/{self.player_pokemon.hp} HP")
        self.opponent_label.config(text=f"{self.opponent_pokemon.name}: {self.opponent_pokemon.hpIG}/{self.opponent_pokemon.hp} HP")

    #function to log messages
    def log_message(self, message):
        self.battle_log.config(state=tk.NORMAL)
        self.battle_log.insert(tk.END, message + "\n")
        self.battle_log.config(state=tk.DISABLED)

    #function to check for more battles
    def check_for_more_battles(self):
        if self.player_lost:        #if player lost
            self.root.after(3000,self.end_game("You lost! Game Over."))
            return

        if self.battles_left == 0:  #if all battles are won
            self.root.update()
            self.root.after(3000,self.end_game("Congratulations! You've won all 10 battles!"))  
        else:
            # Heal the player's Pokémon before the next battle
            self.heal_player_pokemon()
            # Continue to next battle after a short delay
            self.root.after(2000, self.next_battle)

    def heal_player_pokemon(self):
        self.player_pokemon.hpIG = self.player_pokemon.hp  # Restore player's Pokémon HP to max
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

        #button to restart the game
        restart_button = tk.Button(self.end_frame, text="Restart", font=("Helvetica", 16), command=self.restart_game, bg="#87CEEB")
        restart_button.pack(pady=10)
    
    #function to restart the game
    def restart_game(self):
        self.end_frame.pack_forget()
        self.battles_left = 10
        self.available_opponents = opponents[:]  # Reset available opponents
        self.splash_screen()
            

# Create the Tkinter root window and start the game
root = tk.Tk()
battle_gui = Mainframe(root)
root.mainloop()

#close the database connection
datastore.close_connection()