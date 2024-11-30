import mysql.connector

class DataStore:
    def __init__(self):
        # Connect to MySQL database
        self.database = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            # database="pokemon_game"  # Use the target database directly if needed
        )

        self.cur = self.database.cursor()

        # Step 2: Load the SQL file
        with open(r"C:\Users\ss130\Desktop\sahaj\cs project\CS-Final-Project-main\data.sql", "r") as file:
            sql_script = file.read()

        # Split the SQL script into individual statements and execute
        for statement in sql_script.split(';'):
            if statement.strip():  # Skip empty statements
                self.cur.execute(statement)
    
    def opponents_list(self):
        self.cur.execute("SELECT name FROM pokemon")
        return self.cur.fetchall()
    
    def get_move(self,move_id):
        self.cur.execute("SELECT move_id,name,type,power,contact,accuracy FROM moves WHERE move_id=%s",(move_id,))
        return self.cur.fetchone()    
    
    def get_pokemon(self,name):
        self.cur.execute("SELECT pokemon_id,name,type,hp,att,defe,spatt,spdef,spd,cov_1,cov_2 FROM pokemon WHERE name=%s",(name,))
        return self.cur.fetchone()
    
    def nature_list(self):
        self.cur.execute("SELECT nature_id,name,att,defe,spatt,spdef,spd FROM nature")
        return self.cur.fetchall()
    
    def get_moves_by_type(self,type_):
        self.cur.execute("SELECT move_id,name,type,power,contact,accuracy FROM moves WHERE type=%s",(type_,))
        return self.cur.fetchall()
    
    def strengths(self,type_):
        self.cur.execute("select weak from strengths where strong = %s",(type_,))
        return [i[0] for i in self.cur.fetchall()]
    
    def weaknesses(self,type_):
        self.cur.execute("select strong from strengths where weak = %s",(type_,))
        return [i[0] for i in self.cur.fetchall()]

    def close_connection(self):
        self.cur.close()
        self.database.close()