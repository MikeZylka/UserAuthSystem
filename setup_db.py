import sqlite3
import os
import configHandler

DB_FILE_NAME = None

def createDb():
    """
    Creates the database file called users.db and creates the table users
    """

    global DB_FILE_NAME
    open(DB_FILE_NAME, "x")
    con = sqlite3.connect(DB_FILE_NAME)
    cur = con.cursor()

    cur.execute('''CREATE TABLE users (
        username VARCHAR, 
        password_hash VARCHAR
        )''')
    con.commit()


def dbInfo():
    """
    Scans the current database file to determine the amount of rows in the table. 

    Returns:
        Tuple: Returns the table name and the amount of rows in the table (table_name, row_count)
    """
    
    global DB_FILE_NAME
    con = sqlite3.connect(DB_FILE_NAME)
    cur = con.cursor()

    count = cur.execute("SELECT COUNT(*) FROM users").fetchall()
    return ("users", count[0])
     


def main():
    global DB_FILE_NAME
    
    #Initializes the configuration handler and checks if the config file exists
    config = configHandler.ConfigHandler()
    if not config.fileExists():
        print("Error: Configuration file does not exist. Please download the configuration file.")
        return
    DB_FILE_NAME = config.getDbFile()

    #Checks if the database file exists
    if os.path.exists(DB_FILE_NAME):
        print("It seems like users.db already exists.")
        dbi = dbInfo()
        print("There are {0} lines in the table {1}".format(dbi[1][0], dbi[0]))
        print()
        #Takes in user input and asks if the user would like to delete and recreate the database
        while True:
            userInput = input("Would you like to delete and recreate it? (y/n): ")

            if userInput == "y":
                os.remove(DB_FILE_NAME)
                createDb()
                print()
                break
            elif userInput == "n":
                return
            else:
                print("Sorry, that was not a valid option.")
                print()
    else:
        createDb()
    print("Database users.db sucessfully created.")

        

if __name__ == "__main__":
    main()
