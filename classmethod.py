# we cannot change the value of a variable defined in the class from outside.

class Employee:
    no_of_leaves = 7
    ''''constructor'''
    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printDetails(self):
        return f"name is {self.name}. Salary is {self.salary}. and Role is {self.role}"

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves = newleaves

Ram = Employee("Ram",75000,"Protector")
Shiv = Employee("Shiv",80000,"destroyer")

Employee.change_leaves(108)
print(f"number of leaves is {Employee.no_of_leaves}")

Ram.change_leaves(111)
print(f"number of leaves is {Ram.no_of_leaves}")
