class User:
    """Class to describe a user"""

    def __init__(self, first_name, last_name, age, date_of_birth, email, location):
        """Init user with profile details"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.date_of_birth = date_of_birth
        self.email = email
        self.location = location.title()

    def describe_user(self):
        """Prints the user's profile information"""
        print(f"User {self.first_name} {self.last_name} has the following details:")
        print(self.age)
        print(self.date_of_birth)
        print(self.location)
        print(self.email)

    def greet_user(self):
        """Provide a greeting to the user"""
        print(f"\nWelcome {self.first_name} {self.last_name} to the site")


ellie = User('ellie', 'maguire', '14', '07/07/2005', 'ellie.maguire@testdomain.com', 'cookstown')
ellie.describe_user()
ellie.greet_user()

print("\n")

nathan = User('nathan', 'colhoun', '34', '01/011984', 'nathan@natedogg.com', 'carrick')
nathan.describe_user()
nathan.greet_user()