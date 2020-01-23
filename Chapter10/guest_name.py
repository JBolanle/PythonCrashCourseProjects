filename = 'guest.txt'

print("Enter 'quit' at any time to leave the program.")

while True:
    name = input("What's your name?: ")
    if name == 'quit':
        break
    else:
        with open(filename, 'a') as f:
            f.write(f"{name}\n")
        print(f"Hi {name}, you've been added to the guest book")