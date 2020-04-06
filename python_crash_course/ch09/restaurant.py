class Restaurant:
    """A Class to model a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Init the resturant name & cuisine type"""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.title()

    def describe_restaurant(self):
        """Provides the restaurant name and cuisine type"""
        print(f"The name of the resturant is: {self.restaurant_name}")
        print(f"The restaurant servers {self.cuisine_type} food.")

    def open_restaurant(self):
        """Informs that the restaurant is open"""
        print(f"The {self.restaurant_name.title()} is now open!")
