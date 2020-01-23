#Tuples - tuples are lists that can't be changed.
#Tuples can still be accessed like a regular list tho
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#example of trying to change tuple - will get errors
#dimensions[0] = 250

# Traceback (most recent call last):
#   File "dimensions.py", line 8, in <module>
#     dimensions[0] = 250
# TypeError: 'tuple' object does not support item assignment

#Looping through all values in a tuple
for dimension in dimensions:
    print(dimension)

#Tuples can still be written over like any other variable
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions")
for dimension in dimensions:
    print(dimension)

print("Challenge 4.13 - create list of common buffet items in a menu and print them out using a for loop; The restaurant changes the menu so overwrite and print again")

buffet_menu = ('chicken', 'pounded yam', 'jollof rice', 'biscuits')

print("Original buffet menu")
for item in buffet_menu:
    print(item.title())

buffet_menu = ('chicken', 'amala', 'fried rice', 'gravy')

print("\nNew buffet menu")
for item in buffet_menu:
    print(item.title())