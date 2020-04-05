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


my_restaurant = Restaurant('Moes Grill', 'americian style')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

print("\n")
district_80 = Restaurant('District 80 Bistro', 'Bistro/Grill')
district_80.describe_restaurant()
district_80.open_restaurant()

print("\n")
pg = Restaurant('PG Chips', 'chip shop')
pg.describe_restaurant()
pg.open_restaurant()