class Employee:
    """A class to define the details of an employee"""

    def __init__(self, first_name, last_name, annual_salary):
        """Init the employee details"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.annual_salary = annual_salary

    def get_employee_name(self):
        """Return the name of the employee"""
        fullname = f"{self.first_name} {self.last_name}"
        return print(f"Employee Name: - {fullname}")

    def get_employee_salary(self):
        """Return the salary of the employee"""
        return print(f"Employee Salary: - {self.annual_salary}")

    def give_employee_raise(self, raise_amount=5000):
        """Give the employee a salary raise"""
        self.annual_salary += raise_amount
        return print(f"\nEmployee Salary: - {self.annual_salary}")


employee = Employee('sharon', 'maguire', 35000)
employee.get_employee_name()
employee.get_employee_salary()
employee.give_employee_raise()

