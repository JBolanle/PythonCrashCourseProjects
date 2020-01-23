players = ['charles', 'tyler', 'lewis', 'eli', 'moke']
print(players[0:3])
print(players[:3]) #same as above cuz python starts count at 0 without starting index

print(players[2:4])
print(players[2:]) #will automatically go to end of list
print(players[-2:]) #negative index will start processing from end of the list

#Looping through a list with slices
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())