class Employee():
    """takes in first name, last name and annual salary"""

    def __init__(self, first_name, last_name, annual_salary):
        """Init first name, last name and salary attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
        
    def give_raise(self, salary_raise = 5000):
        new_salary = self.annual_salary + salary_raise
        self.annual_salary = new_salary

