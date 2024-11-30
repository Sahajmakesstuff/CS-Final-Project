#Importing sql
import mysql.connector

#Database class
class DataStore:
    def __init__(self):
        # Connect to MySQL database
        self.database = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",        #Change password to your MySQL password
        )

        #creating sql cursor
        self.cur = self.database.cursor()

        #Load the SQL file
        with open(r"C:\Users\ss130\Desktop\sahaj\cs project\FINAL PROJECT\data.sql", "r") as file:      
            sql_script = file.read()            #change the path to the location of the data.sql file

        # Split the SQL script into individual statements and execute
        for statement in sql_script.split(';'):
            if statement.strip():  # Skip empty statements
                self.cur.execute(statement)
    
    #Function to get the list of all the pokemons
    def opponents_list(self):
        self.cur.execute("SELECT name FROM pokemon")
        return self.cur.fetchall()
    
    #Function to get the specific move using move_id
    def get_move(self,move_id):
        self.cur.execute("SELECT move_id,name,type,power,contact,accuracy FROM moves WHERE move_id=%s",(move_id,))
        return self.cur.fetchone()    
    
    #Function to get the specific pokemon using its name
    def get_pokemon(self,name):
        self.cur.execute("SELECT pokemon_id,name,type,hp,att,defe,spatt,spdef,spd,cov_1,cov_2 FROM pokemon WHERE name=%s",(name,))
        return self.cur.fetchone()
    
    #Function to get the list of all the natures
    def nature_list(self):
        self.cur.execute("SELECT nature_id,name,att,defe,spatt,spdef,spd FROM nature")
        return self.cur.fetchall()
    
    #Function to get all the moves of a particular type
    def get_moves_by_type(self,type_):
        self.cur.execute("SELECT move_id,name,type,power,contact,accuracy FROM moves WHERE type=%s",(type_,))
        return self.cur.fetchall()
    
    #extracting strengths of a particular type
    def strengths(self,type_):
        self.cur.execute("select weak from strengths where strong = %s",(type_,))
        return [i[0] for i in self.cur.fetchall()]   
    
    #extracting weaknesses of a particular type
    def weaknesses(self,type_):
        self.cur.execute("select strong from strengths where weak = %s",(type_,))
        return [i[0] for i in self.cur.fetchall()]

    #closing the connection
    def close_connection(self):
        self.cur.close()
        self.database.close()