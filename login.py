import hashlib
import sqlite3
import configHandler
from os.path import exists
from getpass import getpass

DB_FILE_NAME = None
    

def hash_string(password):
    """
    Hashes the password using sha512.

    Args:
        password (String): The password supplied by the user 

    Returns:
        String: The hashed password
    """
    byteArray = bytearray(password.encode())
    h = hashlib.sha512(byteArray)
    return h.hexdigest()

def check_credentials(username, password):
    """
    Validates the username and password. 

    Args:
        username (String): The username of the user
        password (String): The password of the user

    Returns:
        boolean: Returns true or false if the username and passowrd matches
    """
    global DB_FILE_NAME
    username = username.lower()
    con = sqlite3.connect(DB_FILE_NAME)
    cur = con.cursor()

    for row in cur.execute("SELECT username, password_hash FROM users WHERE username=:user", {"user": username}):
        if username == row[0] and hash_string(password) == row[1]:
            return True
    return False 

def main():
    global DB_FILE_NAME
    
    #Initializes the configuration handler and checks if the config file exists
    config = configHandler.ConfigHandler()
    if not config.fileExists():
        print("Error: Configuration file does not exist. Please download the configuration file.")
        return
    DB_FILE_NAME = config.getDbFile()

    #checks to see if the database is set up
    if not exists(DB_FILE_NAME):
        print("Error: Database does not exist. Please run setup_db.py to initialize the database.")
        return

    #gets the user inputs
    username = input("Username: ")
    password = getpass("Password: ")
    print()

    #runs the function call and prints output
    if check_credentials(username, password) == True:
        print("Sucessfully logged in as {0}.".format(username))
    else:
        print("Invalid Login.")

if __name__ == "__main__":
    main()