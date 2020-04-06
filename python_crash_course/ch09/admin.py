from users import User


class Admin(User):
    """Class to profile a User of type Admin"""

    def __init__(self, first_name, last_name, age, date_of_birth, email, location):
        """Inherit from User Class"""
        super().__init__(first_name, last_name, age, date_of_birth, email, location)
        self.privileges = ['wite', 'read', 'execute', 'delete']

    def show_privileges(self):
        for privilege in self.privileges:
            print(f"Admin prilivages - {privilege}")


