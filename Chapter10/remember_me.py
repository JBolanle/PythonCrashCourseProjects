import json

# Load the username if it has been store previously.
# Otherwise, prompt user for the username and store it.
filename = 'username.json'


def greet_user():
    """Greet the user by name"""
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
        print("Welcome back, " + username + "!")
    except FileNotFoundError:
        username = input("What is your name? ")
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print("We'll remember you when you come back " + username + "!")

greet_user()