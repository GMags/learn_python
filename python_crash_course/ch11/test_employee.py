import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    """Tests for the employee class"""

    def setUp(self):
        """
        Create an employee and return their salary
        """
        self.employee = Employee('sharon', 'maguire', 35000)

    def test_give_default_raise(self):
        self.employee.give_employee_raise()
        self.assertEqual(self.employee.annual_salary, 40000)

    def test_give_custom_raise(self):
        self.employee.give_employee_raise(10000)
        self.assertEqual(self.employee.annual_salary, 45000)


if __name__ == '__main__':
    unittest.main()






