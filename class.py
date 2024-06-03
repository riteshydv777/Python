class student:
    pass
Tony = student()
jack = student()

print(Tony,jack)  # tony and jack at different memory location.

Tony.name = "Tony"
Tony.std = 12
Tony.sec = "A"

jack.name = "jack"
jack.std = 12
jack.sec = "D"
jack.sub = ["hindi","math"]

print(Tony.name,Tony.std,Tony.sec)
#usin f string.
print(f"{Tony.name} is in class {Tony.std} and section is {Tony.sec}")

print(f"{Tony.name} and {jack.name} are best friend")

print(f" subjects of {jack.name} are {jack.sub} ")

# using join function .
sep = ','
print(f" subject of {jack.name} are { sep.join(jack.sub)}")

a = ",".join(jack.sub)
print(a)