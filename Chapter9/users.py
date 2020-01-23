class User():
    """Creates user profile"""

    def __init__(self, first_name, last_name, age, email):
        """Initialize user profile attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.login_attempt = 0

    def describe_user(self):
        """Method that prints user information"""
        print(
            "Name: " + self.first_name.title() + 
            " " + self.last_name.title()
            )
        print("Age: " + str(self.age))
        print("Email: " + self.email)

    def greet_user(self):
        print("Hello " + self.first_name + ". Welcome to Silk Road Online!")

    def login_attempts(self):
        self.login_attempt += 1

    def reset_login_attempts(self):
        self.login_attempt = 0

class Admin(User):
    """Super user"""
    def __init__(self, first_name, last_name, age, email):
        super().__init__(first_name, last_name, age, email)

        privileges = ['post', 'delete post', 'ban', 'destroy']
        self.privileges = privileges
    
    def show_privileges(self):
        print(self.privileges)

zezema = User('Jumoke', 'Bolanle', 22, 'jumoke.bolanle@gmail.com')

redlio89 = Admin('Jumoke', 'bolanle', 22, 'jumoke.bolanle1@gmail.com')

redlio89.show_privileges()