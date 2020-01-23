def describe_pets(animal_type, pet_name):
    """Display information about a pet"""
    print("I have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pets(animal_type='cat', pet_name='morty')

def make_shirt(size, shirt_text='I love Python'):
    print("Order for shirt saying '" + shirt_text + "', in size " + size + ".")

make_shirt("Medium", "Love Laugh")
make_shirt(shirt_text="L4FREE", size="Small")
make_shirt("Small")
make_shirt("Large")
make_shirt("Medium", shirt_text="3.AM.CO")

def describe_city(city, country="Nigeria"):
    print(city.title() + " is in " + country.title() + ".")

describe_city('lagos')
describe_city('abuja')
describe_city('accra', country="Ghana")