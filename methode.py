class Employee:
    college = "dit"


    def printdetails(self):
            return f" The name is {self.name} . salary is {self.salary} and the role  {self.role}"



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

