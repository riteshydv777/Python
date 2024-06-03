class Employee:
    college = "dit"

    # its our constructor.
    def __init__(self ,aname,asalary,arole):
         self.name = aname
         self.salary = asalary
         self.role = arole


raju = Employee("raju" , 45000, "office")
golu = Employee("golu",35000,"guard")

print(f"name is {raju.name} salary is {raju.salary} and work is in {raju.role} ")
print(f"name is {golu.name} salary is {golu.salary} and work is in {golu.role} ")