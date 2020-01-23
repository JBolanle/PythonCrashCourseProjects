class Restaurant():
    """Describes restaurant, prints information and lets you know if it's open"""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Create attributes for Restaurant class"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        """Describe restaurants name and type of food"""
        print("\nRestaurant Name: " + self.restaurant_name.title())
        print("Cuisine Type: " + self.cuisine_type.title())

    def open_restaurant(self):
        """Lets user know restaurant is open"""
        print("The restaurant " + self.restaurant_name.title() + " is open!")
