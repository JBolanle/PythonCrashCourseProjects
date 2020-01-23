age = 21

if age < 4:
    print("Admission is free ($0)")
elif age >= 4 and age <= 18:
    print("Admission is $5")
elif age > 18:
    print("Admission is $10")

print("Challenge 5.3 - create variable 'alien_color' and assgin it to green, yellow, or red; write if statement that test if color is green. If true, player earns 5 points.")
alien_color = 'Green' 
player_points = 0

if alien_color.lower() == 'green':
    player_points += 5 
    print("Player earned 5 points")
    print("Points: " + str(player_points))
else:
    print("Nothing, smh")

print("\nChallenge 5.4 - 5.3 but with elif's. if not green +10 points")
alien_color_1 = 'Yellow'
player_points_1 = 0

if alien_color_1.lower() == 'green':
    player_points_1 += 5 
    print("Player earned 5 points")
    print("Points: " + str(player_points_1))
elif alien_color_1.lower() == 'red' or 'yellow': #could also have done != 'green' but wanted to try that way
    player_points_1 += 10
    print("Player earned 10 points")
    print("Points: " + str(player_points_1))

print("\nChallenge 5.6 - Stages of Life: Write an if-elif-else chain that determines a person’s stage of life . Set a value for the variable age")
persons_age = 3

if persons_age < 2:
    print("This person is a baby")
elif persons_age >= 2 and persons_age < 4:
    print("This person is a toddler")
elif persons_age >= 4 and persons_age < 13:
    print("This person is a kid")
else:
    print("Code works")

print("\nChallenge 5.7 - Favorite Fruit: Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list .")
favorite_fruits = ['pineapple', 'kiwi', 'lemon']

if 'pineapple' in favorite_fruits:
    print("You really like pineapples")
if 'apple' in favorite_fruits:
    print("You really like apples")
if 'pear' in favorite_fruits:
    print("You really like pears")
if 'kiwi' in favorite_fruits:
    print("You really like kiwis")
if 'lemon' in favorite_fruits:
    print("You really like lemons")