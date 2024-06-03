class Employee:
    college = "dit"
    pass

raja = Employee()
golu = Employee()

raja.name = "raja"
raja.salary = 45000
raja.role = "reception"

golu.name = "golu"
golu.salary = 35000
golu.role = "office"

print(raja.name , raja.salary , raja.role)
print(golu.name , golu.salary , golu.role)

# its a class variable present in our class
print(raja.college)

print(raja.__dict__)
print(golu.__dict__)

print(Employee.__dict__)

# instant variable
raja.college = "tnb"
print(raja.college)

print(Employee.college)
print(Employee.__dict__)

Employee.college = "bn college"
print(Employee.college)

print(Employee.__dict__)