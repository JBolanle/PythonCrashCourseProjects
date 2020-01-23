def add_nums(a, b):
    """Add two integers together"""
    answer = int(a) + int(b)
    return answer

while True:
    try:
        print("Give me two numbers and I will add them!")
        num1 = input("\nFirst number: ")
        num2 = input("Second number: ")
        answer = add_nums(num1, num2)
    except ValueError:
        print("We can only accept numbers! Try again \n")
    else:
        print(str(answer))
        break
    