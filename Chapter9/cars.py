class Car():
    """A simple attempt to describe a car"""

    def __init__(self, make, model, year):
        """Initialize attributes"""
        self.make = make
        self.model = model
        self.year = year
    
    def get_descriptive_name(self):
        self.odometer_reading = 0
        """makes text given pretty"""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print("Odometer reading: " + str(self.odometer_reading) + " miles")

    def update_reading(self, mileage):
        """Updates odometer reading. Reject attempts to rollback"""
        
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't rollback the odometer!")