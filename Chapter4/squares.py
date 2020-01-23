squares = []
for value in range(1,11):
    squares.append(value**2)

print(squares)

#List Comprehensions

squares_two = [value**2 for value in range(1,11)]
print(squares_two)

#Challenge 4.3 - use a for loop to print numbers from 1 to 20
for number in range(1,21):
    print(number)

#Challenge 4.4 - Make list of numbers from 1 to 1mill; use a loop to print the numbers
milly = [number for number in range(1,1000001)]
print(milly)

#Challenge 4.5 - print min, max and sum of list earlier
print(min(milly))
print(max(milly))
print(sum(milly))

#4.6 make list of odd numbers from 1 to 20 using range(). Use for loop to print numbers
odd_numbers = [number for number in range(1,21,2)]
for value in odd_numbers:
    print(value)

#Challenge 4.7 - Make a list of multiples from 3 to 30. Use for loop to print numbers in the list
multiples_of_three = [number for number in range (3,31,3)]
for value in multiples_of_three:
    print(value)

#Challenge 4.8 - make list of first 10 cubed numbers (1-10) and use for loop to print out the value of each cube
for number in range(1,11):
    print(number**3)

print("Challenge 4.9 - use list comprehension to build a list of the first 10 cubes")

first_ten_cubes = [number**3 for number in range(1,11)]
print(first_ten_cubes)