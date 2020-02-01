"""Reads favorite number from a file. If file does not exist, creates file and populates with fav num"""

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

def read_fav_num():
    """Reads the users favorite number from file 'fav_num.json'"""
    with open(filename) as f_obj:
       fav_num = json.load(f_obj)
    return fav_num

try:
    print("Your fav num is: " + str(read_fav_num()))
except FileNotFoundError:
    save_to_file()