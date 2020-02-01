import json

# Load the username if it has been store previously.
# Otherwise, prompt user for the username and store it.
filename = 'username.json'

def greet_user():
    """Greet the user by name"""
    username = get_new_username()
    print("Welcome back, " + username + "!")

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def get_stored_username():
    """Get stored username if available"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username - json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

greet_user()