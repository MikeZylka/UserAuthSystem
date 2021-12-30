User Authentication System

# USER AUTHENTICATION SYSTEM

## About the project

This project is a simple local user sign up and login system that utilizes cyber security standards for a login system such as password hashing, password hygiene, and using an SQLITE database with the correct api calls to prevent injection. Please note that this github is a demostration of python and login system knowledge and should not be used in real life situations. More security implementations could be put in place such as Multi-Factor authentication, login limit, and email/account corespondance for password resets. These implementations may be put in place in this github repository in the future. 

## Built with
- [python](www.python.org)
- [sqlite](www.sqlite.org)

## Getting Started

First clone or download the github repository. Then make sure to install the requirements.txt file.
``` 
pip install -r requirements.txt
```
	
That's it for the installation!

## Usage
Every program accepts standard input in the terminal so no arguments need to be passed for the program. Simply run `python3 [filename]`. 

First you need to set up the database. You can set it up by running: 
```
python3 setup_db.py
```

Then you need to create an account or multiple accounts. You can do this by running:
```
python3 signup.py
```

Finally, you can login to any user account that you created by running:
```
python3 login.py
```
 That's it!
 
 There is also a feature that allows you to delete and recreate the database just by running the database set up file again. 
 
 
 ## Roadmap
- Database Set up system
- User sign up system
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Checks for good password hygiene
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Saves passwords as hashes in the database
- User login system
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Validates user login by comparing password hashs in the database. 

	
