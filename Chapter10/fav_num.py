import json

filename = 'fav_num.json'

def prompt_for_fav_num():
    """Prompts the user for their favorite number"""
    fav_num = input("What is your favorite number?")
    fav_num = int(fav_num)
    return fav_num

def save_to_file():
    """Saves favorite number to 'fav_num.json'"""
    with open(filename, 'w') as f_obj:
        json.dump(prompt_for_fav_num(), f_obj)
    print("Number saved")

save_to_file()