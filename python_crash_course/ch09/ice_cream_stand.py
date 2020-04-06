class Restaurant:
    """A Class to model a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Init the resturant name & cuisine type"""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.num_served = 0

    def describe_restaurant(self):
        """Provides the restaurant name and cuisine type"""
        print(f"The name of the resturant is: {self.restaurant_name}")
        print(f"The restaurant servers {self.cuisine_type} food.")

    def open_restaurant(self):
        """Informs that the restaurant is open"""
        print(f"The {self.restaurant_name.title()} is now open!")

    def people_served(self):
        """Returns the amount of people servered in the restaurant"""
        print(f"The number of people served is: {self.num_served}")

    def increment_num_people_served(self, people_served):
        """Increment the amount of people served in the restaurant"""
        self.num_served += people_served


class IceCreamStand(Restaurant):
    """A Class to define an ice-cream stand"""

    def __init__(self, restaurant_name, cuisine_type='ice-cream'):
        """Init attributes of parent class"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []


    def show_flavors(self):
        for flavor in self.flavors:
            print(f"The current ice-cream flavours we have is: {flavor}")



my_restaurant = Restaurant('Moes Grill', 'americian style')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.people_served()

my_restaurant.num_served = 40
my_restaurant.people_served()

my_restaurant.increment_num_people_served(100)
my_restaurant.people_served()

my_restaurant.increment_num_people_served(250)
my_restaurant.people_served()
print(f"----------------------------------------------------------------------")
mauds = IceCreamStand('Mauds Shop')
mauds.flavors = ['bubblegum', 'strawberry', 'raspberry ripple', 'honeycomb', 'carmel chew chew']

mauds.describe_restaurant()
mauds.show_flavors()
