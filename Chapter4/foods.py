#Copying a list
my_foods = ['pizza', 'milkshake', 'breadsticks']
friends_food = my_foods[:] #This -> [:] <- tells python to create a slice at the beginning and at the end. Essentially copying it
print(my_foods)
print(friends_food)

my_foods.append('chicken wings')
friends_food.append('latte')

print(my_foods)
print(friends_food)

print('Challenge 4.10 - Using a program you wrote before, add lines to the end that print the first three items, middles items and the last three')
print(my_foods[:3])
print(my_foods[1:4])
print(my_foods[-2:])

print('Challenge 4.11 - use my_pizzas.py - add new pizza to original list and add diff pizza to friends list; use for loop to print the first and second list')

pizzas = ['hawian', 'veggie', 'pepperoni']
friends_pizza = pizzas[:]

pizzas.append('cheese')
friends_pizza.append('buffalo')

print('My favorite pizzas are: ')
for pizza in pizzas:
    print(pizza.title())

print("\nMy friends favorite pizzas are: ")
for pizza in friends_pizza:
    print(pizza.title())