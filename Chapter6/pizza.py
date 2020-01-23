#Lists Inside Dictionaries
pizza = {
    'crust': 'thick',
    'toppings': ['mushroom', 'pineapple', 'extra cheese']
}

print("You ordered a " + pizza['crust'] +
    "-crust pizza with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)

tom = {
    'type_of_pet': 'dog',
    'owner': 'kahlynn'
}

nana = {
    'type_of_pet': 'cat',
    'owner': 'precious'
}

sarabi = {
    'type_of_pet': 'bird',
    'owner': 'jumoke'
}

pets = [tom, nana, sarabi]

for pet in pets:
    print(pet)

favorite_places = {
    'detroit': 'jumoke',
    'london': 'jummy',
    'atlanta': 'bisi'
}

for k,v in favorite_places.items():
    print(v.title() + "'s favorite city is " + k.title())