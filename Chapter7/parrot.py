age = int(input("Please enter your age: "))

if age > 18:
    print("You are " + str(age) + " years old. You're eligable to vote!")
else:
    print("You are too young to vote!")

car = input("What care make would you like to rent today: ")
print("Lets see if I can find you a " + car.title() + " vehicle.")

group_size = int(input("How many people are in your dinner group?: "))

if group_size > 8:
    print("Alright, have a seat. We need to wait before some tables are available.")
else:
    print("The table is ready.")

active = True
while active:
    message = input("Tell me something and I will repeat it back to you: \nEnter 'quit to end the program.")
    if message == 'quit':
        active = False
    else:
        print(message)

active_1 = True
while active_1:
    message_1 = input("How old are you?: " )
    if int(message_1) < 3:
        print("The ticket is free")
        active_1 = False
    elif int(message_1) >= 3 and int(message_1) < 12:
        print("The ticket is $10")
        active_1 = False
    elif int(message_1) > 12:
        print("The ticket is $15")
        active_1 = False
    else:
        active_1 = False