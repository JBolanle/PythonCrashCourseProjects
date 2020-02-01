import json

def read_fav_num():
    """Reads the users favorite number from file 'fav_num.json'"""
    with open('fav_num.json') as f_obj:
       fav_num = json.load(f_obj)
    return fav_num

fav_num = read_fav_num()

print("I know your favorite number! It's " + str(fav_num) + ".")