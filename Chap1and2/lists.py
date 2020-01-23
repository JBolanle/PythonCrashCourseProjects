bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[1].title()) # I can use methods on a list
print(bicycles[0].title())
print(bicycles[-1].title()) # '[-1]' accesses the last index in a list

#Concatenating lists with strings
message = 'My first bicycle was a ' + bicycles[0].title() + " bicycle."
print(message)

#Challenge 3.1 - Store names of friends in a list called 'names' and print each persons name one at-a-time
friends_names = ['herman', 'jekoven', 'dante', 'dalton', 'austin', 'carlos']
print(friends_names[0])
print(friends_names[1])
print(friends_names[2])
print(friends_names[3])
print(friends_names[4])
print(friends_names[-1]) #could have use 5 but to access last element in list, this is the way

#Challenge 3.2 - Use list in 3.1 -> print a message with the name, personalized but w/ same text
print('Hey ' + friends_names[0].title() + ', nice to see you again!')
print('Hey ' + friends_names[1].title() + ', nice to see you again!')
print('Hey ' + friends_names[2].title() + ', nice to see you again!')
print('Hey ' + friends_names[3].title() + ', nice to see you again!')
print('Hey ' + friends_names[4].title() + ', nice to see you again!')
print('Hey ' + friends_names[5].title() + ', nice to see you again!')

#Challenge 3.3 - pick fav mode of transportation -> List examples
cars_i_like = ['audi r8', 'lexus rc-f', 'porsche taycan']
print('I would like to own a ' + cars_i_like[-1].title() + '!')

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

#.append() adds items to a list
motorcycles.append('honda')
print(motorcycles)

#insert() adds items to the list by their index number -> (index #, item)
motorcycles.insert(0, 'bmw')
print(motorcycles)

#del deletes items in a list given that you know their index number
del motorcycles[2]
print(motorcycles)

#pop() lets you remove an item from a list but still work with that item. pop() by itsle
#will remove the last item. pop(index) will remove the item at the index location
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a " + first_owned.title())

#Using .remove() removes an item by its value. That value can still be worked with just like .pop()
motorcycles.remove('ducati')
print(motorcycles)

#Challenge 3.4 - guest list of three people you want at a dinner
guest_list = ['Jordan Belfort', 'Michelle Obama', 'Olugbade Bolanle']

print("Hello " + guest_list[0] + " you've been invited to a dinner hosted by me!")
print("Hello " + guest_list[1] + " you've been invited to a dinner hosted by me!")
print("Hello " + guest_list[2] + " you've been invited to a dinner hosted by me!")

#Challenge 3.4 - change the guest list cuz someone couldn't make it
print(guest_list.pop(2))
guest_list.append('Dave Ramsey')

print("Hello " + guest_list[0] + " you've been invited to a dinner hosted by me!")
print("Hello " + guest_list[1] + " you've been invited to a dinner hosted by me!")
print("Hello " + guest_list[2] + " you've been invited to a dinner hosted by me!")

#Challenge 3.5 - add new guest to the beginning, middle and end
print("Hey guests, I've found a bigger table and we can now have a larger group of people!")
guest_list.insert(0, 'Jim Rohn')
guest_list.insert(1, 'Donald Trump')
guest_list.append('Lewis Hamilton')

print("Hello " + guest_list[0] + " you've been invited to a dinner hosted by me!")
print("Hello " + guest_list[1] + " you've been invited to a dinner hosted by me!")
print("Hello " + guest_list[2] + " you've been invited to a dinner hosted by me!")
print("Hello " + guest_list[3] + " you've been invited to a dinner hosted by me!")
print("Hello " + guest_list[4] + " you've been invited to a dinner hosted by me!")
print("Hello " + guest_list[5] + " you've been invited to a dinner hosted by me!")

#Challenge 3.7 - remove people from the list cuz the table shrank - use pop() to remove one at a time until only two people
print("Hey sorry y'all, they decided I couldn't have that big a table after all. I'll need to rescind some invitations unfortunately.")
print("Sorry, " + guest_list.pop() + ". I gotta let you go")
print("Sorry, " + guest_list.pop() + ". I gotta let you go")
print("Sorry, " + guest_list.pop() + ". I gotta let you go")
print("Sorry, " + guest_list.pop() + ". I gotta let you go")

print(guest_list[0] + " and " + guest_list[1] + "! You two are still invited!")

del guest_list[0]
del guest_list[0]

print(guest_list)