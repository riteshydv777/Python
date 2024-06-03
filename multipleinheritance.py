class Employee:
    no_of_leaves = 7

    #create constructor
    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"the name is {self.name}. salary is {self.salary}. and role is {self.role}"

class Player:
    no_of_games = 1
    #create constructor
    def __init__(self,name,game):
        self.name = name
        self.game = game
    def printdetails(self):
        return f"the name is {self.name} and plays {self.game}"

# child class having feature of both Employee and Player class.

class coolprog( Employee , Player):
    language = "java"

    # def __init__(self,language):
    #     self.language = language

    def printlanguage(self):
        # self.language = language
        # return f"language is {self.language}"
        print(f"language is {self.language}")


# only Employee class
ram = Employee("ram",75000,"proctector")
shiv = Employee("shiv",80000,"destroyer")

print(ram.printdetails())
print(shiv.printdetails())

# Only Player class
rohan = Player("rohan","cricket")
print(rohan.printdetails())

jack = coolprog("jack",80000,"coder")
det = jack.printdetails()
print(det)

print(jack.printlanguage())

