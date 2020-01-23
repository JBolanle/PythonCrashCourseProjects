#Looping through all key-value pairs

user_0 = {
    'username': 'redlio89',
    'first': 'jumoke',
    'last': 'bolanle'
}

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

#Looping through all the keys in a dictionary
favorite_languages = {
    'jumoke': 'French',
    'grace': 'yoruba',
    'bisi': 'puerto...'
}

for name in favorite_languages.keys():
    print(name.title())

friends = ['bisi', 'grace']

for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(" Hey, " + name.title() +
        ", your favorite language is " +
        favorite_languages[name].title() + "!")

print("Challenge 6-5. Rivers: Make a dictionary containing three major rivers and the country each river runs through . One key-value pair might be 'nile': 'egypt' .")

major_rivers = {
    'nile': 'egypt',
    'pearl': 'china',
    'seine': 'france'
}

for k, v in major_rivers.items():
    print("The " + k.title() +
          " runs through " + v.title() + ".")

for river in major_rivers.keys():
    print(river.title())

for city in major_rivers.values():
    print(city.title())