# Challenge 10-6:
# - Write a program that prompts for 2 numbs
# - add nums together and print the result
# - Catch the TypeError is they input something other than a number
# - print friendly error message

#Challenge 10-7:
# - wrap code in while loop

program_active = True
while program_active:
    try:
        num1 = input("First num: ")
        num2 = input("Second num: ")

        num1 = int(num1)
        num2 = int(num2)
        sum = num1 + num2
    except TypeError:
        print("Only whole numbers are allow")
    except ValueError:
        #Just found out I can do multiple except blocks just like if/else
        print("Only whole numbers are allow")
    else:
        print(sum)
        program_active = False