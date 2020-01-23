cars = ['bmw', 'audi', 'toyota', 'subaru']
#Sort this list alphabetically with sort(). It's sorted permanently btw
cars.sort()
print(cars)

cars.sort(reverse = True)
print(cars)

################### 
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nHere is the original list: ")
print(cars)

#Temporarily sort lists with sorted(var)
print("\nHere is the sorted list: ")
print(sorted(cars))

print("\nHere's the original list again: ")
print(cars)

#Reverse sorts list from the end to the from permanently
cars.reverse()
print(cars)

#len() finds the length of a list
print(len(cars))