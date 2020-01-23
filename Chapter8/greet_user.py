def greet_user(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['redlio89', 'zezema', 'seriousburn']

greet_user(usernames)

magicians = ['houdini', 'zoro', 'some dude']

def show_magicians(magician_names):
    for name in magician_names:
        print("Hello, " + name.title() + "!")



def make_great(magician_names):
    for name in magician_names:
        name + " the Great!"

#make_great(magician_names=magicians)

show_magicians(magician_names=magicians)

make_great(magician_names=magicians[:])

show_magicians(magician_names=magicians)