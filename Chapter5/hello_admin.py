current_users = ['mkhdir', 'jbolanle', 'exzedo', 'bisiboy', 'naruto123']

new_users = ['loveless', 'jumoke', 'JBOLANLE', 'kthunt', 'bisiboy']

for user in new_users:
    user = user.lower()
    if user in current_users:
        print("The username " + user + " is already taken\n")

ordinal_numbers = [num for num in range(1,10)]

for num in ordinal_numbers:
    if num == 1:
        print(str(num) + 'st')
    elif num == 2:
        print(str(num) + 'nd')
    elif num == 3:
        print(str(num) + 'rd')
    else:
        print(str(num) + 'th')