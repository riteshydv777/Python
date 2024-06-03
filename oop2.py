class Employee:
    college = "dit"

    # its our constructor.
    # def __init__(self,aname,asalary,arole):
    #     self.name = aname
    #     self.salary = asalary
    #     self.role = arole

    def printdetails(self):
            return f" The name is {self.name} . salary is {self.salary} and the role  {self.role}"



# raju = Employee("raju" , 45000, "office")
# golu = Employee("golu",35000,"guard")
#
# print(f"name is {raju.name} salary is {raju.salary} and work is in {raju.role} ")
# print(f"name is {golu.name} salary is {golu.salary} and work is in {golu.role} ")


raju = Employee()
golu = Employee()

raju.name = "raju"
raju.salary = 45000
raju.role = "office"

golu.name = "golu"
golu.salary = 35000
golu.role = "guard"

print(raju.printdetails())
print(golu.printdetails())



