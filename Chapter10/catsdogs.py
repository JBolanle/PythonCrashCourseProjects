cat_file = 'cats.txt'
dog_file = 'dogs.txt'

def print_pet_names(filename):
    """Print pet's name listed in a text file"""
    try:
        with open(filename) as f_obj:
            for lines in f_obj.readlines():
                print(lines.rstrip())
    except FileNotFoundError:
        # pass
        print("The file '" + filename + "' does not exist.")

print_pet_names(cat_file)
print_pet_names(dog_file)