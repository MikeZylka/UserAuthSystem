import sqlite3
import hashlib
import re
import configHandler
from getpass import getpass
from os.path import exists

DB_FILE_NAME = None

def validPass(password):
    """
    Validates the password so that it fits the 
    minimum criteria for a secure password. 

    Args:
        password (String): The password supplied by the user

    Returns:
        Boolean: Returns true or false depending on if the password matches the criteria
    """
    validpass = True
    if re.match(".*[A-Z]", password) == None:
        print("Password must contain at least one uppercase character.")
        validpass = False
    if re.match(".*[a-z]", password) == None:
        print("Password must contain at least one lowercase character.")
        validpass = False
    if re.match(".*\d", password) == None:
        print("Password must contain at least one number.")
        validpass = False
    special_char= re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if special_char.search(password) == None:
        print("Password must contain at least one special character.")
        validpass = False
    if len(password) < 8:
        print("Password must be at least 8 characters long.")
        validpass = False
    return validpass


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

def add_user(username, password):
    """
    Adds the user to the database file

    Args:
        username (String): The username supplied by the user
        password (String): The password supplied by the user
    """
    global DB_FILE_NAME
    passHash = hash_string(password)

    con = sqlite3.connect(DB_FILE_NAME)
    cur = con.cursor()

    cur.execute("INSERT INTO users (username, password_hash) VALUES (:user, :pass)", {"user":username, "pass":passHash})
    con.commit()

def user_exists(username):
    """
    Check to see if the username exists in the database already

    Args:
        username (String): Username supplid by the user

    Returns:
        Booean: True or false depending on whether the user exists
    """
    global DB_FILE_NAME
    con = sqlite3.connect(DB_FILE_NAME)
    cur = con.cursor()

    userAmt = cur.execute("SELECT COUNT(*) FROM users WHERE username=:user", {"user":username}).fetchall()
    if userAmt[0][0] == 0:
        return False
    return True 

def main():
    global DB_FILE_NAME
    
    #Initializes the configuration handler and checks if the config file exists
    config = configHandler.ConfigHandler()
    if not config.fileExists():
        print("Error: Configuration file does not exist. Please download the configuration file.")
        return
    DB_FILE_NAME = config.getDbFile()
    
    #Checks to see if database file exists    
    if not exists(DB_FILE_NAME):
        print("Error: Database does not exist. Please run setup_db.py to initialize the database.")
        return

    #Asks user for a username
    while True:
        username = input("Please enter your username: ")
        if user_exists(username):
            print("Username already exists.")
            print()
        else:
            break

    #Asks user for a password
    while True:
        password = getpass("Please enter your password: ")
        if validPass(password):
            break
        print()
        
    
    add_user(username, password)
    print()
    print("User successfully added.")


if __name__ == "__main__":
    main()