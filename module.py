""" Builtin module --> random , enum , math , calender """

import random

# gives random number between given range.
#
# random_number = random.randint(0, 11)
# print(random_number)

rad = random.random()*1000
print(rad)

list = ["starplus" , "zeeTv" , "cartoonnet" , "pogo"]
choice = random.choice(list)
print(choice)
