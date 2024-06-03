
""" Methods starting with a double underscore ( __ ) and
    ending with a double underscore ( __ ) represent dunder methods.

     --> Operator overloading means giving new meanings to an operator. eg= '+'(int = add , str = join)
     --> Dunder methods are used for operator overloading

    """

class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    def __add__(self, other):
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __repr__(self):
        return f"Employee('{self.name}', {self.salary}, '{self.role}')"

    def __str__(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

emp1 =Employee("Harry", 345, "Programmer")
emp2 =Employee("Rohan", 5, "Cleaner")

print(emp1.printdetails())
print(emp2.printdetails())

print(f"sum of both salary is {emp1 + emp2}")
print(f"division of both salary is {emp1 / emp2}")

print(repr(emp1))
print(str(emp1))