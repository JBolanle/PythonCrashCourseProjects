alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y-position'] = 25
print(alien_0)

alien_1 = {}

alien_1['color'] = 'blue'
alien_1['points'] = 10
print(alien_1)

print("\nChallenge 6-1. Use a dictionary to store information about a person you know . Store their first name, last name, age, and the city in which they live .")

person = {'first_name': 'jumoke', 
          'last_name': 'bolanle', 
          'age': 22, 
          'city': 'detroit'}

print(person['first_name'].title())
print(person['last_name'].title())
print(person['age'])
print(person['city'].title())

print("\nChallenge 6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers . Think of five names, and use them as keys in your dictionary . Think of a favorite number for each person, and store each as a value in your dictionary . Print each person’s name and their favorite number .")

favorite_color = {'jumoke': 'burgundy',
                    'kahlynn': 'green',
                    'tokunbo': 'pink',
                    'grace': 'purple',
                    'sadea': 'lavender'}

print("Jumoke's favorite color is " +
      favorite_color['jumoke'] +
      ".")
print("Kah'lynn's favorite color is " +
      favorite_color['kahlynn'] +
      ".")

#Nesting

aliens = []

for alien_number in range(30):
    new_alien = {'color': 'blue', 'speed': 'slow', 'points': 5}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
print("...")